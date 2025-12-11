#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bulk stažení a zpracování LLM modelů z OpenRouter API za rok 2024.

Jednorázový skript pro lokální použití - stáhne modely od vybraných
providerů a vytvoří Jekyll posty v _llm/ adresáři.

POZOR: OpenRouter API obsahuje simulovaná data s budoucími timestampy.
Tento skript filtruje pouze reálně existující modely.

Funkce:
- Filtruje jen modely s reálným timestampem (ne budoucí)
- Deduplikuje verze modelů (gpt-4o-2024-11-20 vs gpt-4o)
- Ignoruje varianty :free, :extended, :exacto (jsou to aliasy)
- Vybírá nejnovější verzi z každé skupiny modelů

Použití:
    python scripts/bulk_fetch_llm_2025.py --dry-run          # Náhled bez zpracování
    python scripts/bulk_fetch_llm_2025.py --limit 10         # Zpracovat max 10 modelů
    python scripts/bulk_fetch_llm_2025.py --no-analyze       # Bez LLM analýzy
    python scripts/bulk_fetch_llm_2025.py --year 2024        # Modely za rok 2024
    python scripts/bulk_fetch_llm_2025.py                    # Plné zpracování

Podporovaní provideři:
    - anthropic (Claude)
    - google (Gemini)
    - openai (GPT)
    - deepseek (DeepSeek)
    - mistralai (Mistral)
    - meta-llama (Llama)
    - x-ai (Grok)
"""

import json
import os
import re
import sys
import argparse
import requests
import time
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict

# Načíst .env soubor pokud existuje
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Import benchmark fetcheru
try:
    from fetch_llm_benchmarks import BenchmarkFetcher
    BENCHMARKS_AVAILABLE = True
except ImportError:
    try:
        # Zkusit import z aktuálního adresáře
        sys.path.insert(0, str(Path(__file__).parent))
        from fetch_llm_benchmarks import BenchmarkFetcher
        BENCHMARKS_AVAILABLE = True
    except ImportError:
        BENCHMARKS_AVAILABLE = False


class BulkLLMFetcher:
    """Bulk fetcher pro LLM modely z OpenRouter."""

    API_URL = "https://openrouter.ai/api/v1/models"
    CHAT_API_URL = "https://openrouter.ai/api/v1/chat/completions"

    # Výstupní adresář pro Jekyll posty
    OUTPUT_DIR = Path(__file__).parent.parent / "_llm"

    # Backup adresář pro JSON data
    BACKUP_DIR = Path(__file__).parent.parent / "_data" / "llm_backup"

    # Časové konstanty
    # Reálný aktuální čas - dynamicky z time.time()
    # (dříve byl statický, což způsobovalo odfiltrování nových modelů)
    REAL_NOW_TIMESTAMP = int(time.time())

    # Timestampy pro začátky roků
    YEAR_STARTS = {
        2023: 1672531200,  # 1.1.2023
        2024: 1704067200,  # 1.1.2024
        2025: 1735689600,  # 1.1.2025
        2026: 1767225600,  # 1.1.2026
    }

    # Výchozí rok pro filtraci
    DEFAULT_YEAR = 2025

    # Cíloví provideři
    TARGET_PROVIDERS = [
        'anthropic',
        'google',
        'openai',
        'deepseek',
        'mistralai',
        'meta-llama',
        'x-ai'
    ]

    # Všichni hlavní provideři pro srovnání v analýze
    COMPETITOR_PROVIDERS = ['anthropic', 'google', 'openai', 'x-ai', 'mistralai', 'deepseek']

    # Model pro analýzu
    ANALYZER_MODEL = "google/gemini-2.0-flash-001"

    # Pauza mezi API voláními (sekundy)
    API_DELAY = 2

    # Suffixes které ignorujeme (jsou to aliasy/varianty)
    IGNORED_SUFFIXES = [':free', ':extended', ':exacto']

    # Master Prompt v4.0 (Ultimate Edition) - podle dokumentu LLM-testy.pdf
    ANALYSIS_PROMPT_TEMPLATE = """Jsi expertní AI analytik. Tvým úkolem je vytvořit detailní "kreditní skóre" pro LLM model na základě vstupních dat. Musíš vyvážit technickou kvalitu, cenu, rychlost a použitelnost v praxi.

=== VSTUPNÍ DATA ===

MODEL:
- Název: {model_name}
- ID: {model_id}
- Cena: ${prompt_price}/1M vstup, ${completion_price}/1M výstup
- Blend cena: ${blend_price}/1M
- Kontext: {context_length} tokenů
- Max výstup: {max_completion} tokenů
- Modality: {input_modalities} → {output_modalities}

BENCHMARK SKÓRE:
{benchmark_section}

KATEGORIE (předpočítané):
{categories_section}

POPIS MODELU:
{description}

KONKURENČNÍ MODELY:
{competitor_models}

=== ANALYTICKÁ LOGIKA ===

KROK 1: 360° Kategorizace
Zařaď model do jedné nebo více kategorií:
- Programátor (LiveCodeBench, SWE-bench)
- Vědec (AIME, GPQA)
- Kreativec/Lokalizace (MMMLU - čeština, tvůrčí psaní)
- Agent/Data (Tau-Bench, ZeroBench)
- Speedster (Vysoké TPS, nízké TTFT)

KROK 2: Analýza benchmarků
Využij poskytnutá data pro přesné hodnocení. Porovnej s průměry kategorie a konkurencí.

KROK 3: Výpočet "Real-World Value"
Value Score = (Logic Core + Agent Core) / (Blend cena * 10)
Interpretace: Kolik "inteligence" dostanu za 1 dolar.

KROK 4: Výstup
Vrať POUZE validní JSON v následujícím formátu:

{{
  "profile": {{
    "developer": "Název společnosti",
    "architecture": "Popis architektury (Transformer, MoE, počet parametrů)",
    "parameters": "Počet parametrů nebo null",
    "focus": ["primární zaměření 1", "primární zaměření 2"],
    "model_category": "Programátor/Vědec/Kreativec/Agent/Speedster"
  }},

  "radar": {{
    "logic_code": {logic_score},
    "agentic": {agentic_score},
    "languages": {languages_score},
    "safety": {safety_score},
    "speed": "{speed_tier}"
  }},

  "economy": {{
    "blend_price": {blend_price},
    "value_score": 0.0,
    "context_sufficient_for_rag": true
  }},

  "characteristics": "1-3 věty o tom, co dělá tento model technicky unikátním. Využij benchmark data.",

  "strengths": [
    {{"area": "Krátký název oblasti", "description": "Specifická síla s fakty/benchmarky"}}
  ],

  "weaknesses": [
    {{"area": "Krátký název oblasti", "description": "Specifická slabina"}}
  ],

  "competitors": [
    {{
      "provider": "Název poskytovatele",
      "model": "Konkrétní model ze seznamu konkurentů",
      "model_id": "model/id ze seznamu",
      "price_comparison": "Jak se liší ceny (např. '2x levnější vstup, podobný výstup')",
      "comparison": "Proč konkuruje, co je lepší/horší"
    }}
  ],

  "recommendation": {{
    "target_users": ["Cílová skupina 1", "Cílová skupina 2"],
    "use_cases": ["Dobrý use case 1", "Dobrý use case 2"],
    "avoid_for": ["Kdy NEPOUŽÍVAT 1", "Kdy NEPOUŽÍVAT 2"]
  }},

  "expert_verdict": {{
    "killer_feature": "To jedno, v čem je model nejlepší",
    "hidden_risk": "Skryté riziko (např. 'Pomalá inference kvůli CoT', 'Slabá čeština')",
    "recommended_use_case": "Konkrétní doporučený scénář použití"
  }},

  "verdict": "1-2 věty shrnutí - kdo by měl tento model používat a proč"
}}

=== PRAVIDLA ===
- Vrať POUZE JSON, žádný markdown/text
- Všechny hodnoty česky
- Min 2 silné stránky, 2 slabiny, 4 konkurenti
- Vyber konkurenty z POSKYTNUTÉHO SEZNAMU
- Buď objektivní, bez superlativů ("revoluční", "neuvěřitelný")
- Zaměř se na měřitelné rozdíly
- Využij benchmark data pro konkrétní argumentaci
- Pokud benchmark chybí, neodhaduj - uveď "data nejsou k dispozici"
- Polož důraz na MMMLU pro hodnocení češtiny (kritické pro lokální nasazení)"""

    # Prompt pro překlad popisu
    TRANSLATE_PROMPT = """Přelož následující anglický text do češtiny. Zachovej technickou terminologii.
Vrať POUZE přeložený text, nic jiného.

Text k překladu:
{text}"""

    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        self.api_key = os.getenv('OPENROUTER_API_KEY', '')
        self.models_data = None
        self.processed_count = 0
        self.error_count = 0

        # Inicializace benchmark fetcheru
        self.benchmark_fetcher = None
        self.benchmark_data = None
        if BENCHMARKS_AVAILABLE:
            self.benchmark_fetcher = BenchmarkFetcher(verbose=verbose)
            try:
                self.benchmark_data = self.benchmark_fetcher.fetch_and_process()
                self.log("📊 Benchmark data načtena")
            except Exception as e:
                self.log(f"⚠️ Benchmark data nejsou dostupná: {e}")

    def log(self, message: str):
        """Vypíše zprávu pokud je verbose mode."""
        if self.verbose:
            print(message)

    def fetch_models(self) -> list:
        """Stáhne seznam všech modelů z OpenRouter API."""
        headers = {}
        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'

        self.log("📡 Stahuji seznam modelů z OpenRouter API...")
        response = requests.get(self.API_URL, headers=headers, timeout=30)
        response.raise_for_status()

        data = response.json()
        self.models_data = data.get('data', [])
        self.log(f"   Nalezeno {len(self.models_data)} modelů celkem")
        return self.models_data

    def extract_base_model(self, model_id: str) -> str:
        """
        Extrahuje základní název modelu bez verze a suffixů.

        Příklady:
        - openai/gpt-4o-2024-11-20 -> openai/gpt-4o
        - anthropic/claude-3-opus-20240229 -> anthropic/claude-3-opus
        - mistralai/mistral-large-2411 -> mistralai/mistral-large
        - meta-llama/llama-3.2-3b-instruct:free -> meta-llama/llama-3.2-3b-instruct
        """
        # Odstraň suffixes jako :free, :extended, :exacto
        base = re.sub(r':[a-z]+$', '', model_id)

        provider = base.split('/')[0] if '/' in base else ''
        name = base.split('/')[-1] if '/' in base else base

        # Odstraň date-based verze (YYYY-MM-DD nebo YYYYMMDD nebo -YYMM)
        name = re.sub(r'-20\d{2}-\d{2}-\d{2}$', '', name)  # -2024-11-20
        name = re.sub(r'-20\d{6}$', '', name)              # -20240229
        name = re.sub(r'-\d{4}$', '', name)                # -2411, -2501

        return f'{provider}/{name}' if provider else name

    def is_ignored_variant(self, model_id: str) -> bool:
        """Zkontroluje, zda je model ignorovaná varianta (:free, :extended, atd.)."""
        for suffix in self.IGNORED_SUFFIXES:
            if model_id.endswith(suffix):
                return True
        return False

    def filter_models(self, providers: list = None, year: int = None) -> list:
        """
        Filtruje modely podle providerů a roku s deduplikací verzí.

        Args:
            providers: Seznam providerů k filtraci
            year: Rok pro filtraci (default: 2024)

        Returns:
            Seznam unikátních modelů (nejnovější verze z každé skupiny)
        """
        if not self.models_data:
            self.fetch_models()

        providers = providers or self.TARGET_PROVIDERS
        year = year or self.DEFAULT_YEAR

        year_start = self.YEAR_STARTS.get(year, self.YEAR_STARTS[2024])
        year_end = self.YEAR_STARTS.get(year + 1, self.REAL_NOW_TIMESTAMP)

        # Omezit na reálný čas (ne budoucí data)
        max_timestamp = min(year_end, self.REAL_NOW_TIMESTAMP)

        self.log(f"   Filtruji modely za rok {year}")
        self.log(f"   Časové rozmezí: {datetime.fromtimestamp(year_start)} - {datetime.fromtimestamp(max_timestamp)}")

        # První průchod: základní filtrace
        candidates = []
        for model in self.models_data:
            model_id = model.get('id', '')
            created = model.get('created', 0)

            # Filtr: reálný timestamp (ne budoucí)
            if created > self.REAL_NOW_TIMESTAMP:
                continue

            # Filtr: rok
            if created < year_start or created >= max_timestamp:
                continue

            # Filtr: provider
            provider = model_id.split('/')[0] if '/' in model_id else ''
            if provider not in providers:
                continue

            # Filtr: ignorované varianty (:free, :extended)
            if self.is_ignored_variant(model_id):
                continue

            candidates.append(model)

        self.log(f"   Kandidátů po základní filtraci: {len(candidates)}")

        # Druhý průchod: deduplikace verzí - vybrat nejnovější z každé skupiny
        from collections import defaultdict
        model_groups = defaultdict(list)

        for model in candidates:
            base = self.extract_base_model(model['id'])
            model_groups[base].append(model)

        # Vybrat nejnovější verzi z každé skupiny
        filtered = []
        for base, models in model_groups.items():
            # Seřadit podle created timestamp (nejnovější první)
            models.sort(key=lambda x: x.get('created', 0), reverse=True)
            newest = models[0]

            # Pokud je více verzí, logovat
            if len(models) > 1:
                self.log(f"   Deduplikace {base}: vybráno {newest['id']} z {len(models)} verzí")

            filtered.append(newest)

        # Seřadit podle data vytvoření (nejstarší první)
        filtered.sort(key=lambda x: x.get('created', 0))

        self.log(f"   Výsledek: {len(filtered)} unikátních modelů za rok {year} od {len(providers)} providerů")
        return filtered

    def get_competitor_models_text(self, exclude_id: str = None) -> str:
        """Připraví textový přehled konkurenčních modelů pro prompt."""
        if not self.models_data:
            self.fetch_models()

        lines = []

        for provider in self.COMPETITOR_PROVIDERS:
            provider_models = [
                m for m in self.models_data
                if m['id'].startswith(provider + '/') and m['id'] != exclude_id
            ]

            if not provider_models:
                continue

            provider_models.sort(key=lambda x: x.get('created', 0), reverse=True)

            lines.append(f"\n{provider.upper()}:")
            for m in provider_models[:3]:
                pricing = m.get('pricing', {})
                prompt_price = float(pricing.get('prompt', 0)) * 1_000_000
                compl_price = float(pricing.get('completion', 0)) * 1_000_000
                ctx = m.get('context_length', 0)
                lines.append(
                    f"  - {m['id']}: ${prompt_price:.2f}/${compl_price:.2f} per 1M, "
                    f"context {ctx:,} tokens"
                )

        return '\n'.join(lines)

    def get_benchmark_data(self, model_id: str) -> Optional[Dict]:
        """Získá benchmark data pro model z cache."""
        if not self.benchmark_data:
            return None

        models = self.benchmark_data.get('models', {})

        # Přímý lookup
        if model_id in models:
            return models[model_id]

        # Zkusit normalizované varianty
        normalized = model_id.lower()
        for key in models:
            if key.lower() == normalized:
                return models[key]

        # Zkusit verzi bez suffixu za dvojtečkou (:thinking, :beta, :free atd.)
        if ':' in model_id:
            base_without_suffix = model_id.rsplit(':', 1)[0]
            if base_without_suffix in models:
                return models[base_without_suffix]
            # Zkusit i lowercase
            for key in models:
                if key.lower() == base_without_suffix.lower():
                    return models[key]

        # Zkusit částečnou shodu (base model bez verze)
        base = self.extract_base_model(model_id)
        for key in models:
            if self.extract_base_model(key) == base:
                return models[key]

        return None

    def format_benchmark_section(self, benchmark_data: Dict) -> str:
        """Formátuje benchmark sekci pro LLM prompt."""
        if not benchmark_data:
            return "Benchmark data nejsou k dispozici pro tento model."

        benchmarks = benchmark_data.get('benchmarks', {})
        if not benchmarks:
            return "Benchmark data nejsou k dispozici pro tento model."

        lines = []

        # Benchmark hodnoty
        benchmark_names = {
            'aime_2025': 'AIME 2025 (matematika)',
            'gpqa_diamond': 'GPQA Diamond (věda)',
            'math_500': 'MATH-500 (matematika)',
            'swe_bench_verified': 'SWE-bench Verified (kód)',
            'livecodebench': 'LiveCodeBench (kód)',
            'aider_polyglot': 'Aider Polyglot (kód)',
            'tau2_bench': 'τ2-Bench (agenti)',
            'terminal_bench': 'Terminal-Bench (CLI)',
            'osworld': 'OSWorld (desktop)',
            'mmlu_pro': 'MMLU Pro (znalosti)',
            'hle': 'HLE (hard logic)',
            'arc_agi_2': 'ARC-AGI-2 (abstrakce)',
            'zerobench': 'ZeroBench (extrakce)',
            'ocrbench': 'OCRBench (OCR)',
            'ruler_niah': 'RULER NIAH (retrieval)',
            'mmmu': 'MMMU (multimodal)',
            'video_mmmu': 'Video-MMMU',
            'mathvista': 'MathVista',
            'truthfulqa': 'TruthfulQA (pravdivost)',
            'safetybench': 'SafetyBench (bezpečnost)',
            'mmmlu': 'MMMLU (multilingvální)',
            'mgsm': 'MGSM (multilingvální mat.)',
            'intelligence_index': 'AI Intelligence Index',
        }

        for key, value in benchmarks.items():
            if value is not None:
                name = benchmark_names.get(key, key)
                lines.append(f"- {name}: {value:.1f}%")

        # Performance metriky
        performance = benchmark_data.get('performance', {})
        if performance.get('tps'):
            lines.append(f"- TPS (tokens/s): {performance['tps']:.1f}")
        if performance.get('ttft_seconds'):
            lines.append(f"- TTFT (latence): {performance['ttft_seconds']:.3f}s")

        return '\n'.join(lines) if lines else "Benchmark data nejsou k dispozici."

    def format_categories_section(self, benchmark_data: Dict) -> str:
        """Formátuje kategorii sekci pro LLM prompt."""
        if not benchmark_data:
            return "Kategorie nejsou k dispozici."

        categories = benchmark_data.get('categories', {})
        if not categories:
            return "Kategorie nejsou k dispozici."

        lines = []
        for cat_key, cat_data in categories.items():
            icon = cat_data.get('icon', '')
            name = cat_data.get('name', cat_key)
            score = cat_data.get('score')
            tier = cat_data.get('tier', 'N/A')

            if score is not None:
                lines.append(f"{icon} {name}: {score:.1f}/100 ({tier})")
            else:
                lines.append(f"{icon} {name}: Nedostupné")

        # Celkové hodnocení
        summary = benchmark_data.get('summary', {})
        if summary.get('overall_score'):
            lines.append(f"\n📊 CELKOVÉ SKÓRE: {summary['overall_score']:.1f}/100 ({summary.get('overall_tier', 'N/A')})")

        return '\n'.join(lines)

    def get_radar_values(self, benchmark_data: Dict) -> Dict:
        """Extrahuje hodnoty pro radar chart z benchmark dat."""
        default_values = {
            'logic_score': 0,
            'agentic_score': 0,
            'languages_score': 0,
            'safety_score': 0,
            'speed_tier': 'Nehodnoceno'
        }

        if not benchmark_data:
            return default_values

        categories = benchmark_data.get('categories', {})

        # Logic = průměr science + coding
        science_score = categories.get('science', {}).get('score') or 0
        coding_score = categories.get('coding', {}).get('score') or 0
        logic_score = (science_score + coding_score) / 2 if (science_score or coding_score) else 0

        return {
            'logic_score': round(logic_score, 1),
            'agentic_score': categories.get('agentic', {}).get('score') or 0,
            'languages_score': categories.get('languages', {}).get('score') or 0,
            'safety_score': categories.get('safety', {}).get('score') or 0,
            'speed_tier': categories.get('speed', {}).get('tier') or 'Nehodnoceno'
        }

    def translate_text(self, text: str) -> str:
        """Přeloží text do češtiny pomocí LLM."""
        if not self.api_key:
            return text

        if not text or len(text.strip()) < 10:
            return text

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'HTTP-Referer': 'https://marigold.cz',
            'X-Title': 'LLM Bulk Fetcher'
        }

        data = {
            'model': 'google/gemini-2.0-flash-001',
            'messages': [
                {'role': 'user', 'content': self.TRANSLATE_PROMPT.format(text=text[:2000])}
            ],
            'max_tokens': 2000,
            'temperature': 0.1
        }

        try:
            response = requests.post(
                self.CHAT_API_URL,
                headers=headers,
                json=data,
                timeout=60
            )
            response.raise_for_status()

            result = response.json()
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content'].strip()
        except Exception as e:
            self.log(f"   ⚠️ Překlad selhal: {e}")

        return text

    def analyze_model(self, model: dict) -> dict:
        """Analyzuje model pomocí LLM s integrovanými benchmark daty."""
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY není nastaven")

        context_length = model.get('context_length') or model.get('top_provider', {}).get('context_length') or 'N/A'
        max_completion = model.get('top_provider', {}).get('max_completion_tokens') or 'N/A'

        pricing = model.get('pricing', {})
        prompt_price = float(pricing.get('prompt', 0)) * 1_000_000
        completion_price = float(pricing.get('completion', 0)) * 1_000_000
        # Blend cena = (3 * prompt + 1 * completion) / 4 - typický poměr
        blend_price = (prompt_price * 3 + completion_price) / 4

        architecture = model.get('architecture', {})
        input_modalities = ', '.join(architecture.get('input_modalities', ['text']))
        output_modalities = ', '.join(architecture.get('output_modalities', ['text']))

        competitor_models = self.get_competitor_models_text(exclude_id=model['id'])

        # Získat benchmark data
        benchmark_data = self.get_benchmark_data(model['id'])
        benchmark_section = self.format_benchmark_section(benchmark_data)
        categories_section = self.format_categories_section(benchmark_data)
        radar_values = self.get_radar_values(benchmark_data)

        if benchmark_data:
            self.log(f"   📊 Benchmark data nalezena pro {model['id']}")
        else:
            self.log(f"   ⚠️ Benchmark data nenalezena pro {model['id']}")

        prompt = self.ANALYSIS_PROMPT_TEMPLATE.format(
            model_name=model.get('name', model['id']),
            model_id=model['id'],
            context_length=f"{context_length:,}" if isinstance(context_length, int) else context_length,
            max_completion=f"{max_completion:,}" if isinstance(max_completion, int) else max_completion,
            input_modalities=input_modalities,
            output_modalities=output_modalities,
            prompt_price=f"{prompt_price:.2f}",
            completion_price=f"{completion_price:.2f}",
            blend_price=f"{blend_price:.2f}",
            description=model.get('description', 'Popis není k dispozici.')[:1000],
            competitor_models=competitor_models,
            benchmark_section=benchmark_section,
            categories_section=categories_section,
            logic_score=radar_values['logic_score'],
            agentic_score=radar_values['agentic_score'],
            languages_score=radar_values['languages_score'],
            safety_score=radar_values['safety_score'],
            speed_tier=radar_values['speed_tier']
        )

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'HTTP-Referer': 'https://marigold.cz',
            'X-Title': 'LLM Model Analyzer'
        }

        data = {
            'model': self.ANALYZER_MODEL,
            'messages': [
                {'role': 'user', 'content': prompt}
            ],
            'max_tokens': 4000,
            'temperature': 0.2,
            'response_format': {'type': 'json_object'}
        }

        self.log(f"   🤖 Analyzuji pomocí {self.ANALYZER_MODEL}...")

        response = requests.post(
            self.CHAT_API_URL,
            headers=headers,
            json=data,
            timeout=120
        )
        response.raise_for_status()

        result = response.json()

        if 'choices' in result and len(result['choices']) > 0:
            raw_response = result['choices'][0]['message']['content']

            usage = result.get('usage', {})
            self.log(f"   Tokeny: {usage.get('prompt_tokens', 'N/A')} / {usage.get('completion_tokens', 'N/A')}")

            try:
                clean_response = raw_response.strip()
                if clean_response.startswith('```'):
                    clean_response = clean_response.split('\n', 1)[1]
                    clean_response = clean_response.rsplit('```', 1)[0]

                analysis = json.loads(clean_response)
                self.log("   ✅ JSON úspěšně rozparsován")
                return analysis
            except json.JSONDecodeError as e:
                self.log(f"   ⚠️ Chyba parsování JSON: {e}")
                return {'_raw_text': raw_response, '_parse_error': str(e)}
        else:
            raise ValueError("Neplatná odpověď z API")

    def create_slug(self, model_id: str) -> str:
        """Vytvoří URL-friendly slug z model ID."""
        slug = model_id.replace('/', '-')
        slug = re.sub(r'[^a-zA-Z0-9\-]', '-', slug)
        slug = re.sub(r'-+', '-', slug)
        slug = slug.strip('-')
        return slug.lower()

    def _dict_to_yaml(self, d: dict, indent: int = 0) -> str:
        """Jednoduchý převod dict na YAML string."""
        lines = []
        prefix = '  ' * indent

        for key, value in d.items():
            if value is None:
                lines.append(f"{prefix}{key}: null")
            elif isinstance(value, bool):
                lines.append(f"{prefix}{key}: {str(value).lower()}")
            elif isinstance(value, (int, float)):
                lines.append(f"{prefix}{key}: {value}")
            elif isinstance(value, str):
                if '\n' in value or ':' in value or '"' in value or value.startswith('['):
                    escaped = value.replace('"', '\\"').replace('\n', '\\n')
                    lines.append(f'{prefix}{key}: "{escaped}"')
                else:
                    lines.append(f"{prefix}{key}: {value}")
            elif isinstance(value, list):
                if not value:
                    lines.append(f"{prefix}{key}: []")
                elif all(isinstance(v, str) for v in value):
                    lines.append(f"{prefix}{key}:")
                    for item in value:
                        lines.append(f"{prefix}  - {item}")
                else:
                    lines.append(f"{prefix}{key}:")
                    for item in value:
                        if isinstance(item, dict):
                            first = True
                            for k, v in item.items():
                                if first:
                                    if isinstance(v, str) and (':' in v or '"' in v):
                                        lines.append(f'{prefix}  - {k}: "{v}"')
                                    else:
                                        lines.append(f"{prefix}  - {k}: {v}")
                                    first = False
                                else:
                                    if isinstance(v, str) and (':' in v or '"' in v):
                                        lines.append(f'{prefix}    {k}: "{v}"')
                                    else:
                                        lines.append(f"{prefix}    {k}: {v}")
                        else:
                            lines.append(f"{prefix}  - {item}")
            elif isinstance(value, dict):
                lines.append(f"{prefix}{key}:")
                lines.append(self._dict_to_yaml(value, indent + 1).rstrip())
            else:
                lines.append(f"{prefix}{key}: {value}")

        return '\n'.join(lines) + '\n'

    def generate_jekyll_post(self, model: dict, analysis: dict = None) -> Path:
        """Vygeneruje Jekyll post pro model s benchmark daty."""
        self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        created_ts = model.get('created', 0)
        created_date = datetime.fromtimestamp(created_ts)
        date_str = created_date.strftime('%Y-%m-%d')
        slug = self.create_slug(model['id'])

        filename = f"{date_str}-{slug}.md"
        file_path = self.OUTPUT_DIR / filename

        # Extrakce dat
        pricing = model.get('pricing', {})
        prompt_price = float(pricing.get('prompt', 0)) * 1_000_000
        completion_price = float(pricing.get('completion', 0)) * 1_000_000
        blend_price = (prompt_price * 3 + completion_price) / 4

        architecture = model.get('architecture', {})
        context_length = model.get('context_length') or model.get('top_provider', {}).get('context_length') or 0
        max_output = model.get('top_provider', {}).get('max_completion_tokens') or 0

        # Provider z model ID
        provider = model['id'].split('/')[0].title()
        provider_map = {
            'X-Ai': 'xAI',
            'Meta-Llama': 'Meta',
            'Mistralai': 'Mistral',
            'Deepseek': 'DeepSeek'
        }
        provider = provider_map.get(provider, provider)

        # Překlad popisu
        description = model.get('description', '')
        self.log("   📝 Překládám popis...")
        description_cs = self.translate_text(description) if description else ''

        # Získat benchmark data
        benchmark_data = self.get_benchmark_data(model['id'])

        # Příprava dat z analýzy
        if analysis and '_raw_text' not in analysis:
            profile = analysis.get('profile', {})
            focus = profile.get('focus', [])
            strengths = analysis.get('strengths', [])
            weaknesses = analysis.get('weaknesses', [])
            competitors = analysis.get('competitors', [])
            recommendation = analysis.get('recommendation', {})
            verdict = analysis.get('verdict', '')
            characteristics = analysis.get('characteristics', '')
            radar = analysis.get('radar', {})
            expert_verdict = analysis.get('expert_verdict', {})
        else:
            focus = []
            strengths = []
            weaknesses = []
            competitors = []
            recommendation = {}
            verdict = ''
            characteristics = ''
            radar = {}
            expert_verdict = {}

        # Připravit kategorie z benchmark dat
        categories_data = {}
        overall_score = None
        overall_tier = None

        if benchmark_data:
            categories = benchmark_data.get('categories', {})
            for cat_key, cat_data in categories.items():
                if cat_data.get('score') is not None:
                    categories_data[cat_key] = {
                        'name': cat_data.get('name'),
                        'icon': cat_data.get('icon'),
                        'score': cat_data.get('score'),
                        'tier': cat_data.get('tier')
                    }
            summary = benchmark_data.get('summary', {})
            overall_score = summary.get('overall_score')
            overall_tier = summary.get('overall_tier')

        # Front matter
        front_matter = {
            'layout': 'llm_review',
            'title': model.get('name', model['id']),
            'date': created_date.strftime('%Y-%m-%d %H:%M:%S'),
            'model_id': model['id'],
            'slug': slug,
            'provider': provider,
            'pricing': {
                'prompt_per_m': round(prompt_price, 4),
                'completion_per_m': round(completion_price, 4),
                'blend_per_m': round(blend_price, 4)
            },
            'context_length': f"{context_length:,}" if context_length else "N/A",
            'max_output': f"{max_output:,}" if max_output else "N/A",
            'input_modalities': architecture.get('input_modalities', ['text']),
            'output_modalities': architecture.get('output_modalities', ['text']),
            'focus': focus[:5] if focus else [],
            'strengths': strengths[:4] if strengths else [],
            'weaknesses': weaknesses[:4] if weaknesses else [],
            'competitors': competitors[:4] if competitors else [],
            'recommendation': recommendation,
            'verdict': verdict,
            'benchmark_categories': categories_data if categories_data else None,
            'overall_score': overall_score,
            'overall_tier': overall_tier,
            'radar': radar if radar else None,
            'expert_verdict': expert_verdict if expert_verdict else None,
            'analyzer_model': self.ANALYZER_MODEL if analysis else None,
            'analyzed_at': datetime.now().strftime('%Y-%m-%d %H:%M') if analysis else None
        }

        # Generování obsahu
        content_parts = []

        if description_cs:
            content_parts.append(description_cs)
            content_parts.append("")

        if characteristics:
            content_parts.append("## Unikátní charakteristiky")
            content_parts.append("")
            content_parts.append(characteristics)
            content_parts.append("")

        if strengths:
            content_parts.append("## Silné stránky")
            content_parts.append("")
            for s in strengths:
                content_parts.append(f"### {s.get('area', '')}")
                content_parts.append(s.get('description', ''))
                content_parts.append("")

        if weaknesses:
            content_parts.append("## Slabé stránky")
            content_parts.append("")
            for w in weaknesses:
                content_parts.append(f"### {w.get('area', '')}")
                content_parts.append(w.get('description', ''))
                content_parts.append("")

        # Sestavení souboru
        yaml_content = "---\n"
        yaml_content += self._dict_to_yaml(front_matter)
        yaml_content += "---\n\n"
        yaml_content += '\n'.join(content_parts)

        file_path.write_text(yaml_content, encoding='utf-8')
        return file_path

    def save_backup(self, models: list):
        """Uloží JSON backup všech modelů."""
        self.BACKUP_DIR.mkdir(parents=True, exist_ok=True)

        backup_file = self.BACKUP_DIR / f"models_2025_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        backup_file.write_text(
            json.dumps(models, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )
        self.log(f"💾 Backup uložen: {backup_file}")

    def check_existing(self, model_id: str) -> bool:
        """Zkontroluje, zda již existuje Jekyll post pro model."""
        slug = self.create_slug(model_id)
        existing = list(self.OUTPUT_DIR.glob(f"*-{slug}.md"))
        return len(existing) > 0

    def run(self, dry_run: bool = False, limit: int = None,
            no_analyze: bool = False, skip_existing: bool = True,
            year: int = None) -> list:
        """
        Hlavní metoda - stáhne a zpracuje modely.

        Args:
            dry_run: Pouze zobrazit, nezpracovávat
            limit: Maximální počet modelů
            no_analyze: Přeskočit LLM analýzu
            skip_existing: Přeskočit modely, které již mají Jekyll post
            year: Rok pro filtraci (default: 2024)

        Returns:
            Seznam zpracovaných modelů
        """
        # Stáhnout a filtrovat modely
        models = self.filter_models(year=year)

        if not models:
            self.log("❌ Žádné modely k zpracování")
            return []

        # Uložit backup
        self.save_backup(models)

        # Filtrovat existující
        if skip_existing:
            original_count = len(models)
            models = [m for m in models if not self.check_existing(m['id'])]
            skipped = original_count - len(models)
            if skipped > 0:
                self.log(f"   Přeskočeno {skipped} existujících modelů")

        # Aplikovat limit
        if limit and len(models) > limit:
            models = models[:limit]
            self.log(f"   Omezeno na {limit} modelů")

        # Statistiky
        self.log(f"\n{'='*60}")
        self.log("PŘEHLED MODELŮ K ZPRACOVÁNÍ")
        self.log(f"{'='*60}")

        providers_count = {}
        for m in models:
            provider = m['id'].split('/')[0]
            providers_count[provider] = providers_count.get(provider, 0) + 1

        for provider, count in sorted(providers_count.items()):
            self.log(f"   {provider}: {count} modelů")

        self.log(f"\n   CELKEM: {len(models)} modelů")
        self.log(f"{'='*60}\n")

        if dry_run:
            self.log("DRY RUN - výpis modelů:\n")
            for i, m in enumerate(models, 1):
                created = datetime.fromtimestamp(m.get('created', 0)).strftime('%Y-%m-%d')
                self.log(f"   {i:3}. [{created}] {m['id']}")
                self.log(f"        {m.get('name', 'N/A')}")
            return models

        # Zpracování
        processed = []
        models_without_benchmarks = []

        for i, model in enumerate(models, 1):
            self.log(f"\n{'='*60}")
            self.log(f"[{i}/{len(models)}] {model['id']}")
            self.log(f"{'='*60}")

            try:
                # Zkontrolovat dostupnost benchmarků
                benchmark_data = self.get_benchmark_data(model['id'])
                if not benchmark_data:
                    models_without_benchmarks.append(model['id'])

                analysis = None
                if not no_analyze and self.api_key:
                    analysis = self.analyze_model(model)
                    time.sleep(self.API_DELAY)

                file_path = self.generate_jekyll_post(model, analysis)
                self.log(f"   ✅ Uloženo: {file_path.name}")

                processed.append(model)
                self.processed_count += 1

            except Exception as e:
                self.log(f"   ❌ Chyba: {e}")
                self.error_count += 1

            # Rate limiting
            if i < len(models):
                time.sleep(self.API_DELAY)

        # Souhrn
        self.log(f"\n{'='*60}")
        self.log("SOUHRN")
        self.log(f"{'='*60}")
        self.log(f"   Úspěšně zpracováno: {self.processed_count}")
        self.log(f"   Chyby: {self.error_count}")
        self.log(f"   Jekyll posty: {self.OUTPUT_DIR}")

        # Výpis modelů bez benchmarků
        if models_without_benchmarks:
            self.log(f"\n   ⚠️ Modely bez benchmark dat ({len(models_without_benchmarks)}):")
            for model_id in models_without_benchmarks:
                self.log(f"      - {model_id}")

        self.log(f"{'='*60}\n")

        return processed


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(
        description='Bulk stažení LLM modelů z OpenRouter'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Pouze zobrazit modely bez zpracování'
    )
    parser.add_argument(
        '--limit', '-n',
        type=int,
        default=None,
        help='Maximální počet modelů k zpracování'
    )
    parser.add_argument(
        '--year', '-y',
        type=int,
        default=2025,
        help='Rok pro filtraci modelů (default: 2025)'
    )
    parser.add_argument(
        '--no-analyze',
        action='store_true',
        help='Přeskočit LLM analýzu (rychlejší, ale méně dat)'
    )
    parser.add_argument(
        '--include-existing',
        action='store_true',
        help='Zpracovat i modely, které již mají Jekyll post'
    )
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Tichý režim'
    )

    args = parser.parse_args()

    fetcher = BulkLLMFetcher(verbose=not args.quiet)

    if not fetcher.api_key:
        print("⚠️  OPENROUTER_API_KEY není nastaven!")
        print("   Export: export OPENROUTER_API_KEY='sk-or-v1-xxx'")
        if not args.no_analyze:
            print("   Použijte --no-analyze pro spuštění bez API klíče")
            sys.exit(1)

    try:
        processed = fetcher.run(
            dry_run=args.dry_run,
            limit=args.limit,
            no_analyze=args.no_analyze,
            skip_existing=not args.include_existing,
            year=args.year
        )

        if not args.quiet:
            print(f"\n🎉 Hotovo! Zpracováno {len(processed)} modelů.")

        sys.exit(0)

    except Exception as e:
        print(f"❌ Chyba: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
