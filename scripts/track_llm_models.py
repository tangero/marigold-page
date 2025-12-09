#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skript pro automatické sledování nových LLM modelů z OpenRouter API.

Používá watermark mechanismus - pamatuje si poslední známý nejnovější model
a analyzuje pouze modely, které byly přidány po něm.

Použití:
    python scripts/track_llm_models.py                    # Analyzovat nové modely
    python scripts/track_llm_models.py --dry-run          # Pouze zobrazit nové modely
    python scripts/track_llm_models.py --reset-watermark  # Resetovat watermark
    python scripts/track_llm_models.py --list-tracked     # Zobrazit sledované modely

Výstupy:
    - _data/llm_models_tracked.json  - Seznam sledovaných modelů a watermark
    - _llm/YYYY-MM-DD-model-slug.md  - Jekyll posty pro každý model
"""

import json
import os
import re
import sys
import argparse
import requests
from datetime import datetime
from pathlib import Path
from typing import Optional

# Načíst .env soubor pokud existuje
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


class LLMModelTracker:
    """Sledovač nových LLM modelů z OpenRouter."""

    API_URL = "https://openrouter.ai/api/v1/models"
    CHAT_API_URL = "https://openrouter.ai/api/v1/chat/completions"

    # Soubor pro ukládání stavu sledování
    DATA_FILE = Path(__file__).parent.parent / "_data" / "llm_models_tracked.json"

    # Výstupní adresář pro Jekyll posty
    OUTPUT_DIR = Path(__file__).parent.parent / "_llm"

    # Výchozí watermark model (považovaný za nejnovější známý)
    DEFAULT_WATERMARK = "openai/gpt-5.1-codex-max"

    # Minimální interval mezi analýzami jednoho modelu (hodiny)
    MIN_REANALYSIS_INTERVAL = 168  # 7 dní

    # Maximální počet modelů k analýze v jednom běhu
    MAX_MODELS_PER_RUN = 5

    # Model pro analýzu
    ANALYZER_MODEL = "google/gemini-3-pro-preview"

    # Hlavní poskytovatelé pro srovnání
    COMPETITOR_PROVIDERS = ['anthropic', 'google', 'openai', 'x-ai', 'mistralai', 'deepseek']

    # Prompt pro analýzu modelu - strukturovaný JSON výstup
    ANALYSIS_PROMPT_TEMPLATE = """Role: Senior AI Researcher and Technical Analyst.

Task: Evaluate the LLM model below. Provide factual, objective analysis for technical audience.

TARGET MODEL:
- Name: {model_name}
- ID: {model_id}
- Context: {context_length} tokens
- Max Output: {max_completion} tokens
- Modalities: {input_modalities} → {output_modalities}
- Pricing: ${prompt_price}/1M input, ${completion_price}/1M output
- Description: {description}

CURRENT COMPETITOR MODELS (December 2025 - use these for comparison):
{competitor_models}

Instructions:
1. Analyze the target model objectively.
2. Compare with CURRENT competitors from the list above - pick the most relevant based on:
   - Similar price tier (within 2-3x price range)
   - Similar capabilities/focus
   - Same market segment
3. Output in Czech language.
4. Return ONLY valid JSON.

Required JSON:
{{
  "profile": {{
    "developer": "Company name",
    "architecture": "Architecture description (Transformer, MoE, parameter count if known)",
    "parameters": "Parameter count or null",
    "focus": ["primary focus 1", "primary focus 2"],
    "release_date": "YYYY-MM or null"
  }},
  "characteristics": "1-3 sentences about what makes this model technically unique",
  "strengths": [
    {{"area": "Short area name", "description": "Specific strength with facts/benchmarks"}}
  ],
  "weaknesses": [
    {{"area": "Short area name", "description": "Specific limitation"}}
  ],
  "competitors": [
    {{
      "provider": "Provider name",
      "model": "Specific model name from the competitor list",
      "model_id": "model/id from the list",
      "price_comparison": "How prices compare (e.g. '2x cheaper input, similar output')",
      "comparison": "Why it competes, what's better/worse"
    }}
  ],
  "recommendation": {{
    "target_users": ["Target group 1", "Target group 2"],
    "use_cases": ["Good use case 1", "Good use case 2"],
    "avoid_for": ["When NOT to use 1", "When NOT to use 2"]
  }},
  "verdict": "1-2 sentence summary - who should use this model"
}}

RULES:
- Return ONLY JSON, no markdown/text
- All values in Czech
- Min 2 strengths, 2 weaknesses, 3 competitors
- Pick competitors from the PROVIDED LIST only
- Be objective, no superlatives ("revolutionary", "incredible")
- Focus on measurable differences"""

    # Prompt pro překlad popisu
    TRANSLATE_PROMPT = """Přelož následující anglický text do češtiny. Zachovej technickou terminologii.
Vrať POUZE přeložený text, nic jiného.

Text k překladu:
{text}"""

    def __init__(self, verbose: bool = True):
        """
        Inicializace trackeru.

        Args:
            verbose: Pokud True, vypisuje podrobné informace
        """
        self.verbose = verbose
        self.api_key = os.getenv('OPENROUTER_API_KEY', '')
        self.models_data = None
        self.tracking_data = self._load_tracking_data()

    def _log(self, message: str):
        """Vypíše zprávu pokud je verbose mode."""
        if self.verbose:
            print(message)

    def _load_tracking_data(self) -> dict:
        """Načte data o sledovaných modelech ze souboru."""
        if self.DATA_FILE.exists():
            try:
                return json.loads(self.DATA_FILE.read_text(encoding='utf-8'))
            except json.JSONDecodeError:
                self._log("Chyba při načítání tracking dat, vytvářím nová")

        # Výchozí struktura
        return {
            "watermark": {
                "model_id": None,
                "created_timestamp": None,
                "updated_at": None
            },
            "analyzed_models": {},
            "statistics": {
                "total_analyzed": 0,
                "last_check": None,
                "last_new_models_found": 0
            }
        }

    def _save_tracking_data(self):
        """Uloží data o sledovaných modelech."""
        self.DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        self.DATA_FILE.write_text(
            json.dumps(self.tracking_data, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )
        self._log(f"Tracking data uložena: {self.DATA_FILE}")

    def fetch_models(self) -> list:
        """Stáhne seznam všech modelů z OpenRouter API."""
        headers = {}
        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'

        response = requests.get(self.API_URL, headers=headers, timeout=30)
        response.raise_for_status()

        data = response.json()
        self.models_data = data.get('data', [])
        return self.models_data

    def get_model_by_id(self, model_id: str) -> dict:
        """Najde model podle ID."""
        if not self.models_data:
            self.fetch_models()

        for model in self.models_data:
            if model['id'] == model_id:
                return model

        raise ValueError(f"Model '{model_id}' nebyl nalezen")

    def _get_watermark_timestamp(self) -> int:
        """
        Získá timestamp watermarku.
        Pokud watermark není nastaven, najde ho podle DEFAULT_WATERMARK modelu.
        """
        watermark = self.tracking_data.get("watermark", {})

        if watermark.get("created_timestamp"):
            return watermark["created_timestamp"]

        # Najít výchozí watermark model
        self._log(f"Hledám výchozí watermark model: {self.DEFAULT_WATERMARK}")
        self.fetch_models()

        for model in self.models_data:
            if model['id'] == self.DEFAULT_WATERMARK:
                timestamp = model.get('created', 0)
                self._log(f"   Nalezen s timestamp: {timestamp} ({datetime.fromtimestamp(timestamp)})")
                return timestamp

        # Fallback - použít nejstarší model od hlavních poskytovatelů jako referenci
        self._log("Výchozí watermark model nenalezen, používám nejnovější model")
        newest = max(self.models_data, key=lambda m: m.get('created', 0))
        return newest.get('created', 0)

    def set_watermark(self, model_id: str, timestamp: int):
        """Nastaví nový watermark."""
        self.tracking_data["watermark"] = {
            "model_id": model_id,
            "created_timestamp": timestamp,
            "updated_at": datetime.now().isoformat()
        }
        self._save_tracking_data()

    def reset_watermark(self):
        """Resetuje watermark na výchozí hodnotu."""
        self._log("Resetuji watermark...")
        self.fetch_models()

        for model in self.models_data:
            if model['id'] == self.DEFAULT_WATERMARK:
                self.set_watermark(model['id'], model.get('created', 0))
                self._log(f"Watermark nastaven na: {model['id']}")
                return

        newest = max(self.models_data, key=lambda m: m.get('created', 0))
        self.set_watermark(newest['id'], newest.get('created', 0))
        self._log(f"Watermark nastaven na nejnovější model: {newest['id']}")

    def get_new_models(self) -> list:
        """Najde modely novější než watermark."""
        self._log("Stahuji seznam modelů z OpenRouter API...")
        self.fetch_models()
        self._log(f"   Nalezeno {len(self.models_data)} modelů celkem")

        watermark_ts = self._get_watermark_timestamp()
        watermark_date = datetime.fromtimestamp(watermark_ts) if watermark_ts else "N/A"
        self._log(f"Watermark: {watermark_ts} ({watermark_date})")

        new_models = [
            m for m in self.models_data
            if m.get('created', 0) > watermark_ts
        ]

        new_models.sort(key=lambda x: x.get('created', 0))
        self._log(f"Nalezeno {len(new_models)} nových modelů")

        return new_models

    def is_model_analyzed(self, model_id: str) -> bool:
        """Zkontroluje, zda byl model již analyzován."""
        return model_id in self.tracking_data.get("analyzed_models", {})

    def should_reanalyze(self, model_id: str) -> bool:
        """Zkontroluje, zda by měl být model znovu analyzován."""
        analyzed = self.tracking_data.get("analyzed_models", {}).get(model_id)
        if not analyzed:
            return True

        last_analyzed = analyzed.get("analyzed_at")
        if not last_analyzed:
            return True

        try:
            last_dt = datetime.fromisoformat(last_analyzed)
            hours_since = (datetime.now() - last_dt).total_seconds() / 3600
            return hours_since >= self.MIN_REANALYSIS_INTERVAL
        except (ValueError, TypeError):
            return True

    def mark_as_analyzed(self, model: dict, success: bool = True, file_path: str = None):
        """Označí model jako analyzovaný."""
        if "analyzed_models" not in self.tracking_data:
            self.tracking_data["analyzed_models"] = {}

        self.tracking_data["analyzed_models"][model['id']] = {
            "name": model.get('name', model['id']),
            "created_timestamp": model.get('created'),
            "analyzed_at": datetime.now().isoformat(),
            "success": success,
            "file_path": file_path
        }

        if success:
            self.tracking_data["statistics"]["total_analyzed"] = \
                self.tracking_data["statistics"].get("total_analyzed", 0) + 1

    def get_competitor_models_text(self, exclude_id: str = None) -> str:
        """Připraví textový přehled aktuálních konkurenčních modelů pro prompt."""
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
            'X-Title': 'LLM Model Tracker'
        }

        data = {
            'model': 'google/gemini-2.0-flash-001',  # Rychlejší model pro překlad
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
            self._log(f"   Překlad selhal: {e}")

        return text

    def analyze_model(self, model: dict) -> dict:
        """Analyzuje model pomocí LLM."""
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY není nastaven - analýza není možná")

        context_length = model.get('context_length') or model.get('top_provider', {}).get('context_length') or 'N/A'
        max_completion = model.get('top_provider', {}).get('max_completion_tokens') or 'N/A'

        pricing = model.get('pricing', {})
        prompt_price = float(pricing.get('prompt', 0)) * 1_000_000
        completion_price = float(pricing.get('completion', 0)) * 1_000_000

        architecture = model.get('architecture', {})
        input_modalities = ', '.join(architecture.get('input_modalities', ['text']))
        output_modalities = ', '.join(architecture.get('output_modalities', ['text']))

        competitor_models = self.get_competitor_models_text(exclude_id=model['id'])

        prompt = self.ANALYSIS_PROMPT_TEMPLATE.format(
            model_name=model.get('name', model['id']),
            model_id=model['id'],
            context_length=f"{context_length:,}" if isinstance(context_length, int) else context_length,
            max_completion=f"{max_completion:,}" if isinstance(max_completion, int) else max_completion,
            input_modalities=input_modalities,
            output_modalities=output_modalities,
            prompt_price=f"{prompt_price:.2f}",
            completion_price=f"{completion_price:.2f}",
            description=model.get('description', 'Popis není k dispozici.')[:1000],
            competitor_models=competitor_models
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

        self._log(f"   Analyzuji pomocí {self.ANALYZER_MODEL}...")

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
            self._log(f"   Tokeny: {usage.get('prompt_tokens', 'N/A')} / {usage.get('completion_tokens', 'N/A')}")

            try:
                clean_response = raw_response.strip()
                if clean_response.startswith('```'):
                    clean_response = clean_response.split('\n', 1)[1]
                    clean_response = clean_response.rsplit('```', 1)[0]

                analysis = json.loads(clean_response)
                self._log("   JSON úspěšně rozparsován")
                return analysis
            except json.JSONDecodeError as e:
                self._log(f"   Chyba parsování JSON: {e}")
                return {'_raw_text': raw_response, '_parse_error': str(e)}
        else:
            raise ValueError("Neplatná odpověď z API")

    def create_slug(self, model_id: str) -> str:
        """Vytvoří URL-friendly slug z model ID."""
        # Nahradit / za -
        slug = model_id.replace('/', '-')
        # Nahradit speciální znaky
        slug = re.sub(r'[^a-zA-Z0-9\-]', '-', slug)
        # Odstranit vícenásobné pomlčky
        slug = re.sub(r'-+', '-', slug)
        # Odstranit pomlčky na začátku a konci
        slug = slug.strip('-')
        return slug.lower()

    def generate_jekyll_post(self, model: dict, analysis: dict) -> Path:
        """Vygeneruje Jekyll post pro model."""
        self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Datum a slug
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

        architecture = model.get('architecture', {})
        context_length = model.get('context_length') or model.get('top_provider', {}).get('context_length') or 0
        max_output = model.get('top_provider', {}).get('max_completion_tokens') or 0

        # Provider z model ID
        provider = model['id'].split('/')[0].title()
        if provider.lower() == 'x-ai':
            provider = 'xAI'

        # Překlad popisu
        description = model.get('description', '')
        self._log("   Překládám popis...")
        description_cs = self.translate_text(description) if description else ''

        # Příprava dat z analýzy
        profile = analysis.get('profile', {})
        focus = profile.get('focus', [])
        strengths = analysis.get('strengths', [])
        weaknesses = analysis.get('weaknesses', [])
        competitors = analysis.get('competitors', [])
        recommendation = analysis.get('recommendation', {})
        verdict = analysis.get('verdict', '')
        characteristics = analysis.get('characteristics', '')

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
                'completion_per_m': round(completion_price, 4)
            },
            'context_length': f"{context_length:,}" if context_length else "N/A",
            'max_output': f"{max_output:,}" if max_output else "N/A",
            'input_modalities': architecture.get('input_modalities', ['text']),
            'output_modalities': architecture.get('output_modalities', ['text']),
            'focus': focus[:5] if focus else [],
            'competitors': competitors[:3] if competitors else [],
            'recommendation': recommendation,
            'verdict': verdict,
            'analyzer_model': self.ANALYZER_MODEL,
            'analyzed_at': datetime.now().strftime('%Y-%m-%d %H:%M')
        }

        # Generování obsahu
        content_parts = []

        # Popis
        if description_cs:
            content_parts.append(description_cs)
            content_parts.append("")

        # Charakteristiky
        if characteristics:
            content_parts.append("## Unikátní charakteristiky")
            content_parts.append("")
            content_parts.append(characteristics)
            content_parts.append("")

        # Silné stránky
        if strengths:
            content_parts.append("## Silné stránky")
            content_parts.append("")
            for s in strengths:
                content_parts.append(f"### {s.get('area', '')}")
                content_parts.append(s.get('description', ''))
                content_parts.append("")

        # Slabé stránky
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
        self._log(f"   Jekyll post: {file_path}")

        return file_path

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
                # Escapovat speciální znaky
                if '\n' in value or ':' in value or '"' in value or value.startswith('['):
                    escaped = value.replace('"', '\\"').replace('\n', '\\n')
                    lines.append(f'{prefix}{key}: "{escaped}"')
                else:
                    lines.append(f"{prefix}{key}: {value}")
            elif isinstance(value, list):
                if not value:
                    lines.append(f"{prefix}{key}: []")
                elif all(isinstance(v, str) for v in value):
                    items = [f'"{v}"' if ':' in v or '"' in v else v for v in value]
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

    def analyze_new_models(self, dry_run: bool = False, limit: int = None) -> list:
        """Analyzuje nové modely."""
        limit = limit or self.MAX_MODELS_PER_RUN
        new_models = self.get_new_models()

        if not new_models:
            self._log("Žádné nové modely k analýze")
            return []

        to_analyze = [
            m for m in new_models
            if not self.is_model_analyzed(m['id']) or self.should_reanalyze(m['id'])
        ][:limit]

        self._log(f"\nK analýze: {len(to_analyze)} modelů")
        for i, model in enumerate(to_analyze, 1):
            created = datetime.fromtimestamp(model.get('created', 0)).strftime('%Y-%m-%d')
            self._log(f"   {i}. {model['id']} (přidán: {created})")

        if dry_run:
            self._log("\nDRY RUN - analýza nebyla provedena")
            return to_analyze

        analyzed = []
        for model in to_analyze:
            self._log(f"\n{'='*60}")
            self._log(f"Analyzuji: {model['name']} ({model['id']})")
            self._log(f"{'='*60}")

            try:
                # LLM analýza
                analysis = self.analyze_model(model)

                # Generování Jekyll postu
                file_path = self.generate_jekyll_post(model, analysis)

                self.mark_as_analyzed(model, success=True, file_path=str(file_path))
                analyzed.append(model)
                self._log(f"Hotovo: {model['id']}")

            except Exception as e:
                self._log(f"Chyba při analýze {model['id']}: {e}")
                self.mark_as_analyzed(model, success=False)

        # Aktualizovat watermark
        if analyzed:
            newest_analyzed = max(analyzed, key=lambda x: x.get('created', 0))
            current_watermark_ts = self._get_watermark_timestamp()

            if newest_analyzed.get('created', 0) > current_watermark_ts:
                self.set_watermark(
                    newest_analyzed['id'],
                    newest_analyzed.get('created', 0)
                )
                self._log(f"\nNový watermark: {newest_analyzed['id']}")

        self.tracking_data["statistics"]["last_check"] = datetime.now().isoformat()
        self.tracking_data["statistics"]["last_new_models_found"] = len(new_models)
        self._save_tracking_data()

        return analyzed

    def list_tracked_models(self):
        """Zobrazí přehled sledovaných modelů."""
        print("\n" + "="*70)
        print("PŘEHLED SLEDOVANÝCH LLM MODELŮ")
        print("="*70)

        watermark = self.tracking_data.get("watermark", {})
        print(f"\nWatermark:")
        print(f"   Model: {watermark.get('model_id', 'Nenastaveno')}")
        if watermark.get('created_timestamp'):
            ts = watermark['created_timestamp']
            print(f"   Timestamp: {ts} ({datetime.fromtimestamp(ts)})")
        if watermark.get('updated_at'):
            print(f"   Aktualizováno: {watermark['updated_at']}")

        stats = self.tracking_data.get("statistics", {})
        print(f"\nStatistiky:")
        print(f"   Celkem analyzováno: {stats.get('total_analyzed', 0)}")
        print(f"   Poslední kontrola: {stats.get('last_check', 'Nikdy')}")
        print(f"   Poslední nové modely: {stats.get('last_new_models_found', 0)}")

        analyzed = self.tracking_data.get("analyzed_models", {})
        print(f"\nAnalyzované modely ({len(analyzed)}):")

        if analyzed:
            sorted_models = sorted(
                analyzed.items(),
                key=lambda x: x[1].get('analyzed_at', ''),
                reverse=True
            )

            for model_id, data in sorted_models[:20]:
                status = "OK" if data.get('success') else "FAIL"
                analyzed_at = data.get('analyzed_at', 'N/A')[:16]
                print(f"   [{status}] {model_id}")
                print(f"         Analyzováno: {analyzed_at}")

            if len(sorted_models) > 20:
                print(f"   ... a dalších {len(sorted_models) - 20} modelů")
        else:
            print("   Žádné modely zatím nebyly analyzovány")

        print("\n" + "="*70)

    def get_status_summary(self) -> dict:
        """Vrátí souhrn stavu pro API/monitoring."""
        self.fetch_models()
        watermark_ts = self._get_watermark_timestamp()

        new_models = [
            m for m in self.models_data
            if m.get('created', 0) > watermark_ts
        ]

        return {
            "status": "OK",
            "watermark_model": self.tracking_data.get("watermark", {}).get("model_id"),
            "watermark_timestamp": watermark_ts,
            "total_models_on_openrouter": len(self.models_data),
            "new_models_since_watermark": len(new_models),
            "total_analyzed": self.tracking_data.get("statistics", {}).get("total_analyzed", 0),
            "last_check": self.tracking_data.get("statistics", {}).get("last_check"),
            "checked_at": datetime.now().isoformat()
        }


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(
        description='Automatické sledování nových LLM modelů z OpenRouter API'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Pouze zobrazit nové modely bez analýzy'
    )
    parser.add_argument(
        '--reset-watermark',
        action='store_true',
        help='Resetovat watermark na výchozí model'
    )
    parser.add_argument(
        '--list-tracked', '-l',
        action='store_true',
        help='Zobrazit přehled sledovaných modelů'
    )
    parser.add_argument(
        '--status', '-s',
        action='store_true',
        help='Zobrazit JSON status pro monitoring'
    )
    parser.add_argument(
        '--limit', '-n',
        type=int,
        default=None,
        help='Maximální počet modelů k analýze'
    )
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Tichý režim - méně výpisů'
    )

    args = parser.parse_args()
    tracker = LLMModelTracker(verbose=not args.quiet)

    try:
        if args.status:
            status = tracker.get_status_summary()
            print(json.dumps(status, indent=2, ensure_ascii=False))
            return

        if args.list_tracked:
            tracker.list_tracked_models()
            return

        if args.reset_watermark:
            tracker.reset_watermark()
            return

        analyzed = tracker.analyze_new_models(
            dry_run=args.dry_run,
            limit=args.limit
        )

        if not args.quiet:
            print(f"\nHotovo! Analyzováno {len(analyzed)} nových modelů.")
            print(f"Jekyll posty v: {tracker.OUTPUT_DIR}")

        sys.exit(0)

    except Exception as e:
        print(f"Chyba: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
