#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skript pro stažení benchmark dat z Artificial Analysis API.

Stahuje benchmarky pro LLM modely a ukládá je do cache souboru.
Data jsou použita při generování LLM karet.

Použití:
    python scripts/fetch_llm_benchmarks.py                    # Stáhnout vše
    python scripts/fetch_llm_benchmarks.py --model claude-3.5 # Konkrétní model
    python scripts/fetch_llm_benchmarks.py --list             # Zobrazit dostupné modely

Vyžaduje:
    - ARTIFICIALANALYSIS_API_KEY v env proměnných (volitelné)
"""

import json
import os
import sys
import argparse
import requests
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any

# Načíst .env soubor pokud existuje
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


class BenchmarkFetcher:
    """Fetcher pro LLM benchmarky z Artificial Analysis API."""

    API_URL = "https://artificialanalysis.ai/api/v2/data/llms/models"

    # Cache soubor
    CACHE_FILE = Path(__file__).parent.parent / "_data" / "llm_benchmarks_cache.json"

    # Cache TTL v hodinách
    CACHE_TTL_HOURS = 24

    # Mapování model ID: Artificial Analysis → OpenRouter
    # AA používá slug, OpenRouter používá provider/model
    MODEL_ID_MAPPING = {
        # Anthropic
        "claude-3-5-sonnet": "anthropic/claude-3.5-sonnet",
        "claude-3-5-haiku": "anthropic/claude-3.5-haiku",
        "claude-3-opus": "anthropic/claude-3-opus",
        "claude-3-haiku": "anthropic/claude-3-haiku",
        "claude-sonnet-4": "anthropic/claude-sonnet-4",
        "claude-opus-4": "anthropic/claude-opus-4",
        "claude-opus-4-5": "anthropic/claude-opus-4.5",
        "claude-sonnet-4-5": "anthropic/claude-sonnet-4.5",

        # OpenAI
        "gpt-4o": "openai/gpt-4o",
        "gpt-4o-mini": "openai/gpt-4o-mini",
        "gpt-4-turbo": "openai/gpt-4-turbo",
        "o1": "openai/o1",
        "o1-mini": "openai/o1-mini",
        "o1-pro": "openai/o1-pro",
        "o3-mini": "openai/o3-mini",
        "gpt-4-5": "openai/gpt-4.5",

        # Google
        "gemini-1-5-pro": "google/gemini-pro-1.5",
        "gemini-1-5-flash": "google/gemini-flash-1.5",
        "gemini-2-0-flash": "google/gemini-2.0-flash-001",
        "gemini-2-5-pro": "google/gemini-2.5-pro",
        "gemini-2-5-flash": "google/gemini-2.5-flash",
        "gemini-3-pro": "google/gemini-3-pro-preview",

        # DeepSeek
        "deepseek-v3": "deepseek/deepseek-chat",
        "deepseek-r1": "deepseek/deepseek-r1",

        # Mistral
        "mistral-large": "mistralai/mistral-large",
        "mistral-medium": "mistralai/mistral-medium",
        "mistral-small": "mistralai/mistral-small-24b-instruct-2501",

        # Meta
        "llama-3-1-405b": "meta-llama/llama-3.1-405b-instruct",
        "llama-3-1-70b": "meta-llama/llama-3.1-70b-instruct",
        "llama-3-3-70b": "meta-llama/llama-3.3-70b-instruct",

        # xAI
        "grok-2": "x-ai/grok-2",
        "grok-3": "x-ai/grok-3",
        "grok-3-mini": "x-ai/grok-3-mini",
    }

    # 9 kategorií hodnocení podle dokumentu
    # fallback_index = záložní AA index když chybí jednotlivé benchmarky
    CATEGORIES = {
        'science': {
            'name': 'Věda & Matematika',
            'icon': '🧮',
            'benchmarks': ['aime_2025', 'gpqa_diamond', 'math_500'],
            'weights': [0.40, 0.40, 0.20],
            'fallback_index': 'artificial_analysis_math_index'
        },
        'coding': {
            'name': 'Programování',
            'icon': '💻',
            'benchmarks': ['swe_bench_verified', 'livecodebench', 'aider_polyglot'],
            'weights': [0.45, 0.35, 0.20],
            'fallback_index': 'artificial_analysis_coding_index'
        },
        'agentic': {
            'name': 'Agenti & Nástroje',
            'icon': '🤖',
            'benchmarks': ['tau2_bench', 'terminal_bench', 'osworld'],
            'weights': [0.50, 0.30, 0.20]
        },
        'intelligence': {
            'name': 'Obecná inteligence',
            'icon': '🧠',
            'benchmarks': ['mmlu_pro', 'hle', 'arc_agi_2'],
            'weights': [0.50, 0.30, 0.20],
            'fallback_index': 'intelligence_index'
        },
        'extraction': {
            'name': 'Extrakce dat',
            'icon': '📄',
            'benchmarks': ['zerobench', 'ocrbench', 'ruler_niah'],
            'weights': [0.40, 0.40, 0.20]
        },
        'multimodal': {
            'name': 'Multimodalita',
            'icon': '👁',
            'benchmarks': ['mmmu', 'video_mmmu', 'mathvista'],
            'weights': [0.40, 0.30, 0.30]
        },
        'safety': {
            'name': 'Bezpečnost',
            'icon': '🛡',
            'benchmarks': ['truthfulqa', 'safetybench'],
            'weights': [0.60, 0.40]
        },
        'speed': {
            'name': 'Rychlost',
            'icon': '⚡',
            'metrics': ['tps', 'ttft'],
            'weights': [0.50, 0.50]
        },
        'languages': {
            'name': 'Jazyky (Čeština)',
            'icon': '🌍',
            'benchmarks': ['mmmlu', 'mgsm'],
            'weights': [0.70, 0.30]
        }
    }

    # Rating tiers
    RATING_TIERS = [
        (90, 5, 'Excelentní'),
        (75, 4, 'Výborný'),
        (60, 3, 'Dobrý'),
        (40, 2, 'Průměrný'),
        (0, 1, 'Slabý'),
    ]

    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        self.api_key = os.getenv('ARTIFICIALANALYSIS_API_KEY', '')
        self.raw_data = None
        self.processed_data = {}

    def log(self, message: str):
        if self.verbose:
            print(message)

    def _is_cache_valid(self) -> bool:
        """Zkontroluje, zda je cache stále platná."""
        if not self.CACHE_FILE.exists():
            return False

        try:
            data = json.loads(self.CACHE_FILE.read_text(encoding='utf-8'))
            cached_at = datetime.fromisoformat(data.get('metadata', {}).get('cached_at', ''))
            age_hours = (datetime.now() - cached_at).total_seconds() / 3600
            return age_hours < self.CACHE_TTL_HOURS
        except (json.JSONDecodeError, ValueError, KeyError):
            return False

    def _load_cache(self) -> Optional[Dict]:
        """Načte data z cache."""
        if self._is_cache_valid():
            self.log("📦 Načítám data z cache...")
            return json.loads(self.CACHE_FILE.read_text(encoding='utf-8'))
        return None

    def _save_cache(self, data: Dict):
        """Uloží data do cache."""
        self.CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        data['metadata'] = {
            'cached_at': datetime.now().isoformat(),
            'source': 'artificial_analysis',
            'model_count': len(data.get('models', {}))
        }
        self.CACHE_FILE.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )
        self.log(f"💾 Cache uložena: {self.CACHE_FILE}")

    def fetch_from_api(self) -> list:
        """Stáhne data z Artificial Analysis API."""
        headers = {
            'Content-Type': 'application/json',
        }
        if self.api_key:
            headers['x-api-key'] = self.api_key

        self.log("📡 Stahuji data z Artificial Analysis API...")

        try:
            response = requests.get(self.API_URL, headers=headers, timeout=60)
            response.raise_for_status()
            response_data = response.json()

            # API vrací dict s klíčem 'data' obsahujícím list modelů
            if isinstance(response_data, dict) and 'data' in response_data:
                self.raw_data = response_data['data']
            elif isinstance(response_data, list):
                self.raw_data = response_data
            else:
                self.log(f"⚠️ Neočekávaný formát odpovědi: {type(response_data)}")
                self.raw_data = []

            self.log(f"   Staženo {len(self.raw_data)} modelů")
            return self.raw_data
        except requests.RequestException as e:
            self.log(f"❌ Chyba při stahování: {e}")
            raise

    def _normalize_benchmark_name(self, name: str) -> str:
        """Normalizuje název benchmarku na standardní formát."""
        # Mapování AA názvů na naše interní názvy
        mapping = {
            'artificial_analysis_intelligence_index': 'intelligence_index',
            'mmlu_pro': 'mmlu_pro',
            'gpqa': 'gpqa_diamond',
            'gpqa_diamond': 'gpqa_diamond',
            'livecodebench': 'livecodebench',
            'live_code_bench': 'livecodebench',
            'swe_bench_verified': 'swe_bench_verified',
            'swe_bench': 'swe_bench_verified',
            'math_500': 'math_500',
            'math': 'math_500',
            'aime': 'aime_2025',
            'aime_2025': 'aime_2025',
            'aime25': 'aime_2025',
            'mmmu': 'mmmu',
            'mmmu_pro': 'mmmu',
            'mmmlu': 'mmmlu',
            'tau2': 'tau2_bench',
            'tau2_bench': 'tau2_bench',
            'hle': 'hle',
            'humanitys_last_exam': 'hle',
        }
        return mapping.get(name.lower(), name.lower())

    def _extract_benchmarks(self, model_data: Dict) -> Dict:
        """Extrahuje benchmarky z dat modelu."""
        benchmarks = {}

        # Evaluations z AA API
        evaluations = model_data.get('evaluations', {})
        if isinstance(evaluations, dict):
            for key, value in evaluations.items():
                if value is not None:
                    norm_key = self._normalize_benchmark_name(key)
                    # Převést na procenta pokud je to desetinné číslo
                    if isinstance(value, (int, float)):
                        if value <= 1.0 and value > 0:
                            value = value * 100
                        benchmarks[norm_key] = round(value, 2)

        return benchmarks

    def _extract_performance(self, model_data: Dict) -> Dict:
        """Extrahuje výkonnostní metriky."""
        return {
            'tps': model_data.get('median_output_tokens_per_second'),
            'ttft_seconds': model_data.get('median_time_to_first_token_seconds'),
            'throughput': model_data.get('throughput'),
        }

    def _calculate_category_score(self, benchmarks: Dict, performance: Dict,
                                   category_key: str) -> Dict:
        """Vypočítá skóre pro jednu kategorii."""
        category = self.CATEGORIES[category_key]

        if category_key == 'speed':
            # Speciální výpočet pro rychlost
            tps = performance.get('tps')
            ttft = performance.get('ttft_seconds')

            if tps is None and ttft is None:
                return {'score': None, 'rating': None, 'tier': 'Nehodnoceno'}

            # Normalizace: TPS max ~200 = 100%, TTFT <0.3s = 100%
            tps_score = min((tps or 0) / 200 * 100, 100)
            ttft_score = max(0, (1 - (ttft or 1)) * 100) if ttft else 0

            weights = category['weights']
            score = tps_score * weights[0] + ttft_score * weights[1]
        else:
            # Standardní výpočet pro benchmark kategorie
            benchmark_keys = category['benchmarks']
            weights = category['weights']

            values = []
            used_weights = []

            for i, key in enumerate(benchmark_keys):
                if key in benchmarks and benchmarks[key] is not None:
                    values.append(benchmarks[key])
                    used_weights.append(weights[i])

            # Pokud máme méně než 2 benchmarky, zkusíme použít fallback index
            fallback_index = category.get('fallback_index')
            if len(values) < 2 and fallback_index and fallback_index in benchmarks:
                fallback_value = benchmarks[fallback_index]
                if fallback_value is not None:
                    if values:
                        # Máme jeden benchmark - použijeme vyšší z:
                        # a) samotný benchmark, nebo
                        # b) kombinace benchmarku (60%) + fallback (40%)
                        combined_score = values[0] * 0.6 + fallback_value * 0.4
                        score = max(values[0], combined_score)
                        used_fallback = score == combined_score
                    else:
                        # Nemáme žádný benchmark, použijeme pouze fallback index
                        score = fallback_value
                        used_fallback = True

                    # Určit rating a tier pro fallback
                    rating = None
                    tier = 'Nehodnoceno'
                    for threshold, r, t in self.RATING_TIERS:
                        if score >= threshold:
                            rating = r
                            tier = t
                            break
                    return {
                        'score': round(score, 1),
                        'rating': rating,
                        'tier': tier,
                        'used_fallback': used_fallback
                    }

            if not values:
                return {'score': None, 'rating': None, 'tier': 'Nehodnoceno'}

            # Normalizovat váhy
            weight_sum = sum(used_weights)
            normalized_weights = [w / weight_sum for w in used_weights]

            score = sum(v * w for v, w in zip(values, normalized_weights))

        # Určit rating a tier
        rating = None
        tier = 'Nehodnoceno'
        for threshold, r, t in self.RATING_TIERS:
            if score >= threshold:
                rating = r
                tier = t
                break

        return {
            'score': round(score, 1),
            'rating': rating,
            'tier': tier
        }

    def _calculate_all_categories(self, benchmarks: Dict, performance: Dict) -> Dict:
        """Vypočítá skóre pro všechny kategorie."""
        categories = {}

        for cat_key in self.CATEGORIES:
            cat_data = self._calculate_category_score(benchmarks, performance, cat_key)
            cat_data['name'] = self.CATEGORIES[cat_key]['name']
            cat_data['icon'] = self.CATEGORIES[cat_key]['icon']

            # Přidat raw benchmark hodnoty
            if cat_key == 'speed':
                cat_data['metrics'] = {
                    'tps': performance.get('tps'),
                    'ttft_seconds': performance.get('ttft_seconds')
                }
            else:
                cat_data['benchmarks'] = {
                    k: benchmarks.get(k)
                    for k in self.CATEGORIES[cat_key]['benchmarks']
                }

            categories[cat_key] = cat_data

        return categories

    def _calculate_summary(self, categories: Dict) -> Dict:
        """Vypočítá souhrnné hodnocení."""
        # Váhy pro celkové skóre
        # Rychlost má nižší váhu - neměla by příliš penalizovat kvalitní modely
        category_weights = {
            'science': 1.0,
            'coding': 1.0,
            'agentic': 1.0,
            'intelligence': 1.0,
            'extraction': 0.5,
            'multimodal': 0.5,
            'safety': 0.5,  # Sníženo - často chybí data
            'speed': 0.25,  # Sníženo z 0.5 - rychlost by neměla příliš penalizovat
            'languages': 0.5  # Sníženo - často chybí data pro češtinu
        }

        scores = []
        weights = []

        for cat_key, cat_data in categories.items():
            if cat_data['score'] is not None:
                scores.append(cat_data['score'])
                weights.append(category_weights.get(cat_key, 1.0))

        if not scores:
            return {
                'overall_score': None,
                'overall_rating': None,
                'overall_tier': 'Nehodnoceno',
                'strengths': [],
                'weaknesses': []
            }

        # Vážený průměr
        overall_score = sum(s * w for s, w in zip(scores, weights)) / sum(weights)

        # Určit rating
        overall_rating = None
        overall_tier = 'Nehodnoceno'
        for threshold, r, t in self.RATING_TIERS:
            if overall_score >= threshold:
                overall_rating = r
                overall_tier = t
                break

        # Najít silné a slabé stránky
        scored_categories = [
            (cat_key, cat_data['score'], cat_data['name'], cat_data['icon'])
            for cat_key, cat_data in categories.items()
            if cat_data['score'] is not None
        ]
        scored_categories.sort(key=lambda x: x[1], reverse=True)

        strengths = [
            {'category': c[0], 'label': c[2], 'icon': c[3], 'score': c[1]}
            for c in scored_categories[:3]
        ]
        weaknesses = [
            {'category': c[0], 'label': c[2], 'icon': c[3], 'score': c[1]}
            for c in scored_categories[-3:]
        ]

        return {
            'overall_score': round(overall_score, 1),
            'overall_rating': overall_rating,
            'overall_tier': overall_tier,
            'strengths': strengths,
            'weaknesses': weaknesses
        }

    def process_model(self, model_data: Dict) -> Dict:
        """Zpracuje data jednoho modelu."""
        # Extrakce dat
        benchmarks = self._extract_benchmarks(model_data)
        performance = self._extract_performance(model_data)

        # Výpočet kategorií
        categories = self._calculate_all_categories(benchmarks, performance)

        # Výpočet souhrnu
        summary = self._calculate_summary(categories)

        return {
            'aa_id': model_data.get('id'),
            'aa_name': model_data.get('name'),
            'aa_slug': model_data.get('slug'),
            'benchmarks': benchmarks,
            'performance': performance,
            'categories': categories,
            'summary': summary,
            'processed_at': datetime.now().isoformat()
        }

    def get_openrouter_id(self, aa_model: Dict) -> Optional[str]:
        """Převede Artificial Analysis model ID na OpenRouter ID."""
        slug = aa_model.get('slug', '')

        # Zkusit přímé mapování
        if slug in self.MODEL_ID_MAPPING:
            return self.MODEL_ID_MAPPING[slug]

        # Zkusit odvození z názvu
        name = aa_model.get('name', '').lower()

        # model_creator může být string nebo dict
        creator_data = aa_model.get('model_creator', {})
        if isinstance(creator_data, dict):
            creator = creator_data.get('slug', '').lower()
        else:
            creator = str(creator_data).lower()

        # Mapování providerů
        provider_map = {
            'anthropic': 'anthropic',
            'openai': 'openai',
            'google': 'google',
            'deepseek': 'deepseek',
            'mistral': 'mistralai',
            'meta': 'meta-llama',
            'xai': 'x-ai',
        }

        provider = provider_map.get(creator)
        if provider:
            # Pokusit se sestavit ID
            model_part = slug.replace('-', '-')
            return f"{provider}/{model_part}"

        return None

    def fetch_and_process(self, use_cache: bool = True) -> Dict:
        """Stáhne a zpracuje všechna data."""
        # Zkusit cache
        if use_cache:
            cached = self._load_cache()
            if cached:
                self.processed_data = cached
                return cached

        # Stáhnout z API
        raw_data = self.fetch_from_api()

        # Zpracovat modely
        models = {}
        for model in raw_data:
            try:
                processed = self.process_model(model)

                # Mapovat na OpenRouter ID
                or_id = self.get_openrouter_id(model)
                if or_id:
                    processed['openrouter_id'] = or_id
                    models[or_id] = processed
                else:
                    # Použít AA slug jako klíč
                    models[model.get('slug', model.get('id'))] = processed

            except Exception as e:
                self.log(f"   ⚠️ Chyba při zpracování {model.get('name')}: {e}")

        self.processed_data = {'models': models}

        # Uložit do cache
        self._save_cache(self.processed_data)

        self.log(f"✅ Zpracováno {len(models)} modelů")
        return self.processed_data

    def get_model_data(self, model_id: str) -> Optional[Dict]:
        """Vrátí data pro konkrétní model."""
        if not self.processed_data:
            self.fetch_and_process()

        models = self.processed_data.get('models', {})

        # Zkusit přímý lookup
        if model_id in models:
            return models[model_id]

        # Zkusit normalizovaný lookup
        normalized = model_id.lower().replace('/', '-')
        for key, data in models.items():
            if normalized in key.lower() or key.lower() in normalized:
                return data

        return None

    def list_available_models(self):
        """Zobrazí seznam dostupných modelů."""
        if not self.processed_data:
            self.fetch_and_process()

        models = self.processed_data.get('models', {})

        print("\n" + "=" * 70)
        print("DOSTUPNÉ MODELY S BENCHMARKY")
        print("=" * 70)

        for model_id, data in sorted(models.items()):
            summary = data.get('summary', {})
            score = summary.get('overall_score', 'N/A')
            tier = summary.get('overall_tier', 'N/A')

            print(f"\n{model_id}")
            print(f"   Celkové skóre: {score} ({tier})")

            # Zobrazit kategorie
            categories = data.get('categories', {})
            for cat_key, cat_data in categories.items():
                if cat_data.get('score'):
                    icon = cat_data.get('icon', '')
                    name = cat_data.get('name', cat_key)
                    score = cat_data.get('score', 'N/A')
                    print(f"   {icon} {name}: {score}")


def main():
    parser = argparse.ArgumentParser(
        description='Stažení LLM benchmarků z Artificial Analysis API'
    )
    parser.add_argument(
        '--model', '-m',
        help='Zobrazit data pro konkrétní model'
    )
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='Zobrazit seznam dostupných modelů'
    )
    parser.add_argument(
        '--refresh',
        action='store_true',
        help='Ignorovat cache a stáhnout nová data'
    )
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Tichý režim'
    )

    args = parser.parse_args()

    fetcher = BenchmarkFetcher(verbose=not args.quiet)

    try:
        fetcher.fetch_and_process(use_cache=not args.refresh)

        if args.list:
            fetcher.list_available_models()
        elif args.model:
            data = fetcher.get_model_data(args.model)
            if data:
                print(json.dumps(data, indent=2, ensure_ascii=False))
            else:
                print(f"Model '{args.model}' nenalezen")
                sys.exit(1)
        else:
            print(f"✅ Data stažena a zpracována")
            print(f"   Cache: {fetcher.CACHE_FILE}")

    except Exception as e:
        print(f"❌ Chyba: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
