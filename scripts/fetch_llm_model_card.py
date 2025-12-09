#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skript pro stažení dat o LLM modelu z OpenRouter API
a vygenerování HTML karty s detaily modelu.

Použití:
    python scripts/fetch_llm_model_card.py [model_id] [--analyze]

Příklady:
    python scripts/fetch_llm_model_card.py                              # Nejnovější model
    python scripts/fetch_llm_model_card.py openai/gpt-4o                # Konkrétní model
    python scripts/fetch_llm_model_card.py openai/gpt-4o --analyze      # S LLM analýzou
"""

import requests
import json
import os
import sys
import argparse
from datetime import datetime
from pathlib import Path

# Načíst .env soubor pokud existuje
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv není nainstalován, použijeme jen env proměnné


class LLMModelCardGenerator:
    """Generátor HTML karet pro LLM modely z OpenRouter API."""

    API_URL = "https://openrouter.ai/api/v1/models"
    CHAT_API_URL = "https://openrouter.ai/api/v1/chat/completions"
    TEMPLATE_PATH = Path(__file__).parent / "templates" / "llm_model_card.html"
    OUTPUT_DIR = Path(__file__).parent.parent / "_site" / "llm-test"

    # Model pro analýzu
    ANALYZER_MODEL = "google/gemini-3-pro-preview"

    # Maximální kontext pro výpočet progress baru (2M tokenů)
    MAX_CONTEXT_REFERENCE = 2_000_000

    # Cenové prahy pro barevné kódování (za 1M tokenů)
    PRICE_THRESHOLDS = {
        'free': 0,
        'cheap': 1.0,
        'expensive': 10.0
    }

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

    # Hlavní poskytovatelé pro srovnání
    COMPETITOR_PROVIDERS = ['anthropic', 'google', 'openai', 'x-ai', 'mistralai', 'deepseek']

    def __init__(self):
        self.api_key = os.getenv('OPENROUTER_API_KEY', '')
        self.models_data = None

    def get_competitor_models_text(self, exclude_id: str = None) -> str:
        """
        Připraví textový přehled aktuálních konkurenčních modelů pro prompt.
        Vrací formátovaný text s top modely od každého poskytovatele.
        """
        if not self.models_data:
            self.fetch_models()

        lines = []

        for provider in self.COMPETITOR_PROVIDERS:
            # Filtrovat modely tohoto poskytovatele
            provider_models = [
                m for m in self.models_data
                if m['id'].startswith(provider + '/') and m['id'] != exclude_id
            ]

            if not provider_models:
                continue

            # Seřadit podle data (nejnovější první)
            provider_models.sort(key=lambda x: x.get('created', 0), reverse=True)

            # Vzít top 3 modely
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

    def get_newest_model(self) -> dict:
        """Vrátí nejnovější model podle timestampu created."""
        if not self.models_data:
            self.fetch_models()

        return max(self.models_data, key=lambda m: m.get('created', 0))

    def get_model_by_id(self, model_id: str) -> dict:
        """Najde model podle ID."""
        if not self.models_data:
            self.fetch_models()

        for model in self.models_data:
            if model['id'] == model_id:
                return model

        raise ValueError(f"Model '{model_id}' nebyl nalezen")

    def analyze_model(self, model: dict) -> dict:
        """
        Analyzuje model pomocí LLM (Gemini 3 Pro) přes OpenRouter API.

        Args:
            model: Data modelu z OpenRouter API

        Returns:
            Strukturovaná analýza modelu jako dict
        """
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY není nastaven - analýza není možná")

        # Připravit data pro prompt
        context_length = model.get('context_length') or model.get('top_provider', {}).get('context_length') or 'N/A'
        max_completion = model.get('top_provider', {}).get('max_completion_tokens') or 'N/A'

        pricing = model.get('pricing', {})
        prompt_price = float(pricing.get('prompt', 0)) * 1_000_000
        completion_price = float(pricing.get('completion', 0)) * 1_000_000

        architecture = model.get('architecture', {})
        input_modalities = ', '.join(architecture.get('input_modalities', ['text']))
        output_modalities = ', '.join(architecture.get('output_modalities', ['text']))

        # Získat seznam konkurenčních modelů
        competitor_models = self.get_competitor_models_text(exclude_id=model['id'])

        # Sestavit prompt
        prompt = self.ANALYSIS_PROMPT_TEMPLATE.format(
            model_name=model.get('name', model['id']),
            model_id=model['id'],
            context_length=self.format_number(context_length) if isinstance(context_length, int) else context_length,
            max_completion=self.format_number(max_completion) if isinstance(max_completion, int) else max_completion,
            input_modalities=input_modalities,
            output_modalities=output_modalities,
            prompt_price=f"{prompt_price:.2f}",
            completion_price=f"{completion_price:.2f}",
            description=model.get('description', 'Popis není k dispozici.')[:1000],
            competitor_models=competitor_models
        )

        # Volání OpenRouter API
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

        print(f"🤖 Analyzuji model pomocí {self.ANALYZER_MODEL}...")

        response = requests.post(
            self.CHAT_API_URL,
            headers=headers,
            json=data,
            timeout=120
        )
        response.raise_for_status()

        result = response.json()

        # Extrahovat odpověď
        if 'choices' in result and len(result['choices']) > 0:
            raw_response = result['choices'][0]['message']['content']

            # Zobrazit usage info
            usage = result.get('usage', {})
            print(f"   Prompt tokens: {usage.get('prompt_tokens', 'N/A')}")
            print(f"   Completion tokens: {usage.get('completion_tokens', 'N/A')}")

            # Parsovat JSON
            try:
                # Odstranit případné markdown code blocks
                clean_response = raw_response.strip()
                if clean_response.startswith('```'):
                    clean_response = clean_response.split('\n', 1)[1]
                    clean_response = clean_response.rsplit('```', 1)[0]

                analysis = json.loads(clean_response)
                print("   ✅ JSON úspěšně rozparsován")
                return analysis
            except json.JSONDecodeError as e:
                print(f"   ⚠️ Chyba parsování JSON: {e}")
                # Vrátit raw text jako fallback
                return {'_raw_text': raw_response, '_parse_error': str(e)}
        else:
            raise ValueError("Neplatná odpověď z API")

    def format_price(self, price_per_token: str) -> tuple:
        """
        Převede cenu za token na cenu za 1M tokenů.
        Vrací tuple (formátovaná_cena, css_třída).
        """
        try:
            price = float(price_per_token) * 1_000_000
        except (ValueError, TypeError):
            return ("N/A", "")

        if price == 0:
            return ("Zdarma", "free")
        elif price < self.PRICE_THRESHOLDS['cheap']:
            return (f"${price:.4f}", "")
        elif price < self.PRICE_THRESHOLDS['expensive']:
            return (f"${price:.2f}", "")
        else:
            return (f"${price:.2f}", "expensive")

    def format_number(self, num: int) -> str:
        """Formátuje číslo s oddělovači tisíců."""
        if num is None:
            return "N/A"
        return f"{num:,}".replace(",", " ")

    def generate_pricing_html(self, pricing: dict) -> str:
        """Generuje HTML pro cenovou sekci."""
        items = []

        price_labels = {
            'prompt': 'Input (prompt)',
            'completion': 'Output (completion)',
            'image': 'Obrázek',
            'audio': 'Audio',
            'web_search': 'Web Search',
            'internal_reasoning': 'Reasoning (thinking)',
            'input_cache_read': 'Cache čtení',
            'input_cache_write': 'Cache zápis'
        }

        for key, label in price_labels.items():
            if key in pricing:
                formatted_price, css_class = self.format_price(pricing[key])
                class_attr = f' class="price-item {css_class}"' if css_class else ' class="price-item"'

                items.append(f'''
                <div{class_attr}>
                    <div class="price-label">{label}</div>
                    <div class="price-value">{formatted_price}</div>
                    <div class="price-unit">za 1M tokenů</div>
                </div>''')

        return '\n'.join(items)

    def generate_modality_badges(self, architecture: dict) -> str:
        """Generuje HTML badges pro modality."""
        badges = []

        input_icons = {
            'text': '📝',
            'image': '🖼️',
            'file': '📁',
            'audio': '🎵',
            'video': '🎬'
        }

        output_icons = {
            'text': '📝',
            'image': '🖼️',
            'embeddings': '🔢'
        }

        for modality in architecture.get('input_modalities', []):
            icon = input_icons.get(modality, '📥')
            badges.append(f'<span class="modality-badge input">{icon} {modality} (vstup)</span>')

        for modality in architecture.get('output_modalities', []):
            icon = output_icons.get(modality, '📤')
            badges.append(f'<span class="modality-badge output">{icon} {modality} (výstup)</span>')

        return '\n'.join(badges)

    def generate_parameter_tags(self, parameters: list) -> str:
        """Generuje HTML tagy pro podporované parametry."""
        return '\n'.join([f'<span class="param-tag">{param}</span>' for param in parameters])

    def generate_default_params_rows(self, defaults: dict) -> str:
        """Generuje řádky tabulky pro výchozí parametry."""
        rows = []

        param_labels = {
            'temperature': 'Temperature',
            'top_p': 'Top P',
            'top_k': 'Top K',
            'frequency_penalty': 'Frequency Penalty',
            'presence_penalty': 'Presence Penalty'
        }

        for key, label in param_labels.items():
            value = defaults.get(key)
            if value is not None:
                rows.append(f'''
                <tr>
                    <td>{label}</td>
                    <td>{value}</td>
                </tr>''')

        if not rows:
            rows.append('<tr><td colspan="2">Žádné výchozí parametry</td></tr>')

        return '\n'.join(rows)

    def calculate_context_percentage(self, context_length: int) -> int:
        """Vypočítá procento pro progress bar kontextu."""
        if not context_length:
            return 0
        percentage = (context_length / self.MAX_CONTEXT_REFERENCE) * 100
        return min(100, max(5, int(percentage)))  # Min 5% pro viditelnost

    def analysis_to_markdown(self, analysis: dict) -> str:
        """Převede strukturovanou analýzu na markdown."""

        if '_raw_text' in analysis:
            return analysis['_raw_text']

        md_parts = []

        # Profil
        profile = analysis.get('profile', {})
        if profile:
            md_parts.append("## Profil modelu\n")
            md_parts.append(f"- **Vývojář:** {profile.get('developer', 'N/A')}")
            md_parts.append(f"- **Architektura:** {profile.get('architecture', 'N/A')}")
            md_parts.append(f"- **Parametry:** {profile.get('parameters') or 'Neznámé'}")
            md_parts.append(f"- **Zaměření:** {', '.join(profile.get('focus', []))}")
            md_parts.append("")

        # Charakteristiky
        characteristics = analysis.get('characteristics', '')
        if characteristics:
            md_parts.append("## Unikátní charakteristiky\n")
            md_parts.append(characteristics)
            md_parts.append("")

        # Silné stránky
        strengths = analysis.get('strengths', [])
        if strengths:
            md_parts.append("## Silné stránky\n")
            for s in strengths:
                md_parts.append(f"### ✅ {s.get('area', '')}")
                md_parts.append(s.get('description', ''))
                md_parts.append("")

        # Slabé stránky
        weaknesses = analysis.get('weaknesses', [])
        if weaknesses:
            md_parts.append("## Slabé stránky\n")
            for w in weaknesses:
                md_parts.append(f"### ⚠️ {w.get('area', '')}")
                md_parts.append(w.get('description', ''))
                md_parts.append("")

        # Konkurence
        competitors = analysis.get('competitors', [])
        if competitors:
            md_parts.append("## Srovnání s konkurencí\n")
            for c in competitors:
                md_parts.append(f"### {c.get('provider', '')} - {c.get('model', '')}")
                md_parts.append(c.get('comparison', ''))
                md_parts.append("")

        # Doporučení
        recommendation = analysis.get('recommendation', {})
        if recommendation:
            md_parts.append("## Doporučení\n")
            md_parts.append(f"**Cílová skupina:** {', '.join(recommendation.get('target_users', []))}\n")
            md_parts.append("**Vhodné pro:**")
            for uc in recommendation.get('use_cases', []):
                md_parts.append(f"- {uc}")
            md_parts.append("")
            md_parts.append("**Nevhodné pro:**")
            for af in recommendation.get('avoid_for', []):
                md_parts.append(f"- {af}")
            md_parts.append("")

        # Verdikt
        verdict = analysis.get('verdict', '')
        if verdict:
            md_parts.append("## Verdikt\n")
            md_parts.append(f"**{verdict}**")

        return '\n'.join(md_parts)

    def generate_analysis_html(self, analysis: dict) -> str:
        """Generuje HTML ze strukturované analýzy."""

        # Fallback pro raw text (když JSON parsing selže)
        if '_raw_text' in analysis:
            return f'<div class="analysis-fallback"><pre>{analysis["_raw_text"]}</pre></div>'

        html_parts = []

        # Profil
        profile = analysis.get('profile', {})
        if profile:
            focus_tags = ''.join([f'<span class="focus-tag">{f}</span>' for f in profile.get('focus', [])])
            html_parts.append(f'''
            <div class="analysis-section">
                <h3>Profil modelu</h3>
                <div class="profile-grid">
                    <div class="profile-item">
                        <span class="profile-label">Vývojář</span>
                        <span class="profile-value">{profile.get('developer', 'N/A')}</span>
                    </div>
                    <div class="profile-item">
                        <span class="profile-label">Architektura</span>
                        <span class="profile-value">{profile.get('architecture', 'N/A')}</span>
                    </div>
                    <div class="profile-item">
                        <span class="profile-label">Parametry</span>
                        <span class="profile-value">{profile.get('parameters') or 'Neznámé'}</span>
                    </div>
                    <div class="profile-item">
                        <span class="profile-label">Zaměření</span>
                        <span class="profile-value">{focus_tags}</span>
                    </div>
                </div>
            </div>''')

        # Charakteristiky
        characteristics = analysis.get('characteristics', '')
        if characteristics:
            html_parts.append(f'''
            <div class="analysis-section">
                <h3>Unikátní charakteristiky</h3>
                <p class="characteristics-text">{characteristics}</p>
            </div>''')

        # Silné stránky
        strengths = analysis.get('strengths', [])
        if strengths:
            strength_items = ''.join([
                f'<div class="strength-item"><span class="strength-area">✅ {s.get("area", "")}</span><p>{s.get("description", "")}</p></div>'
                for s in strengths
            ])
            html_parts.append(f'''
            <div class="analysis-section strengths">
                <h3>Silné stránky</h3>
                <div class="strengths-list">{strength_items}</div>
            </div>''')

        # Slabé stránky
        weaknesses = analysis.get('weaknesses', [])
        if weaknesses:
            weakness_items = ''.join([
                f'<div class="weakness-item"><span class="weakness-area">⚠️ {w.get("area", "")}</span><p>{w.get("description", "")}</p></div>'
                for w in weaknesses
            ])
            html_parts.append(f'''
            <div class="analysis-section weaknesses">
                <h3>Slabé stránky</h3>
                <div class="weaknesses-list">{weakness_items}</div>
            </div>''')

        # Konkurence
        competitors = analysis.get('competitors', [])
        if competitors:
            competitor_items = ''.join([
                f'''<div class="competitor-item">
                    <div class="competitor-header">
                        <span class="competitor-provider">{c.get("provider", "")}</span>
                        <span class="competitor-model">{c.get("model", "")}</span>
                        <code class="competitor-id">{c.get("model_id", "")}</code>
                    </div>
                    <div class="competitor-price">{c.get("price_comparison", "")}</div>
                    <p class="competitor-comparison">{c.get("comparison", "")}</p>
                </div>'''
                for c in competitors
            ])
            html_parts.append(f'''
            <div class="analysis-section competitors">
                <h3>Srovnání s konkurencí</h3>
                <div class="competitors-list">{competitor_items}</div>
            </div>''')

        # Doporučení
        recommendation = analysis.get('recommendation', {})
        if recommendation:
            target_users = ', '.join(recommendation.get('target_users', []))
            use_cases = ''.join([f'<li>{uc}</li>' for uc in recommendation.get('use_cases', [])])
            avoid_for = ''.join([f'<li>{af}</li>' for af in recommendation.get('avoid_for', [])])

            html_parts.append(f'''
            <div class="analysis-section recommendation">
                <h3>Doporučení</h3>
                <div class="recommendation-grid">
                    <div class="recommendation-block">
                        <h4>👥 Cílová skupina</h4>
                        <p>{target_users}</p>
                    </div>
                    <div class="recommendation-block use-cases">
                        <h4>✅ Vhodné pro</h4>
                        <ul>{use_cases}</ul>
                    </div>
                    <div class="recommendation-block avoid">
                        <h4>❌ Nevhodné pro</h4>
                        <ul>{avoid_for}</ul>
                    </div>
                </div>
            </div>''')

        # Verdikt
        verdict = analysis.get('verdict', '')
        if verdict:
            html_parts.append(f'''
            <div class="analysis-section verdict">
                <h3>Verdikt</h3>
                <p class="verdict-text">{verdict}</p>
            </div>''')

        return '\n'.join(html_parts)

    def generate_html(self, model: dict, analysis: dict = None) -> str:
        """Vygeneruje kompletní HTML kartu pro model."""
        # Načíst šablonu
        template = self.TEMPLATE_PATH.read_text(encoding='utf-8')

        # Extrahovat data
        model_id = model['id']
        provider = model_id.split('/')[0].title()
        created_ts = model.get('created', 0)
        created_date = datetime.fromtimestamp(created_ts).strftime('%d. %B %Y')

        # České názvy měsíců
        month_names = {
            'January': 'ledna', 'February': 'února', 'March': 'března',
            'April': 'dubna', 'May': 'května', 'June': 'června',
            'July': 'července', 'August': 'srpna', 'September': 'září',
            'October': 'října', 'November': 'listopadu', 'December': 'prosince'
        }
        for en, cs in month_names.items():
            created_date = created_date.replace(en, cs)

        context_length = model.get('context_length') or model.get('top_provider', {}).get('context_length')
        max_completion = model.get('top_provider', {}).get('max_completion_tokens')

        # Moderation badge
        is_moderated = model.get('top_provider', {}).get('is_moderated', False)
        moderation_badge = '''
            <div class="meta-item">
                <div class="meta-label">Status</div>
                <div class="meta-value"><span class="badge moderated">Moderovaný</span></div>
            </div>''' if is_moderated else ''

        # Nahradit placeholdery
        replacements = {
            '{{model_name}}': model.get('name', model_id),
            '{{model_id}}': model_id,
            '{{created_date}}': created_date,
            '{{provider}}': provider,
            '{{tokenizer}}': model.get('architecture', {}).get('tokenizer') or 'N/A',
            '{{moderation_badge}}': moderation_badge,
            '{{pricing_items}}': self.generate_pricing_html(model.get('pricing', {})),
            '{{context_length_formatted}}': self.format_number(context_length) + ' tokenů',
            '{{max_completion_tokens}}': self.format_number(max_completion) + ' tokenů',
            '{{modality}}': (model.get('architecture', {}).get('modality') or 'N/A').replace('->', ' → '),
            '{{context_percentage}}': str(self.calculate_context_percentage(context_length)),
            '{{modality_badges}}': self.generate_modality_badges(model.get('architecture', {})),
            '{{description}}': model.get('description') or 'Popis není k dispozici.',
            '{{parameter_tags}}': self.generate_parameter_tags(model.get('supported_parameters', [])),
            '{{default_params_rows}}': self.generate_default_params_rows(model.get('default_parameters', {}))
        }

        html = template
        for placeholder, value in replacements.items():
            html = html.replace(placeholder, value)

        # Přidat sekci s LLM analýzou pokud existuje
        if analysis:
            analysis_content = self.generate_analysis_html(analysis)
            analysis_html = f'''
        <!-- LLM Analysis -->
        <div class="card analysis-card">
            <div class="card-header">
                <span class="card-icon">🔬</span>
                <h2 class="card-title">AI Analýza modelu</h2>
                <span class="badge" style="margin-left: auto; background: var(--success);">Gemini 3 Pro</span>
            </div>
            <div class="analysis-content">
                {analysis_content}
            </div>
        </div>
    </div>
</body>
</html>'''
            # Nahradit koncový tag
            html = html.replace('    </div>\n</body>\n</html>', analysis_html)

        return html

    def save_html(self, html: str, model_id: str) -> Path:
        """Uloží HTML do souboru."""
        self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Vytvořit bezpečný název souboru
        safe_name = model_id.replace('/', '_').replace(':', '_')
        output_path = self.OUTPUT_DIR / f"{safe_name}.html"

        output_path.write_text(html, encoding='utf-8')
        return output_path

    def run(self, model_id: str = None, analyze: bool = False) -> Path:
        """
        Hlavní metoda - stáhne data a vygeneruje HTML.

        Args:
            model_id: ID modelu nebo None pro nejnovější
            analyze: Pokud True, provede LLM analýzu modelu

        Returns:
            Cesta k vygenerovanému HTML souboru
        """
        print("📡 Stahuji seznam modelů z OpenRouter API...")
        self.fetch_models()
        print(f"   Nalezeno {len(self.models_data)} modelů")

        if model_id:
            print(f"🔍 Hledám model: {model_id}")
            model = self.get_model_by_id(model_id)
        else:
            print("🆕 Hledám nejnovější model...")
            model = self.get_newest_model()

        print(f"✅ Nalezen: {model['name']} ({model['id']})")
        print(f"   Přidán: {datetime.fromtimestamp(model['created']).strftime('%Y-%m-%d')}")

        # LLM analýza (volitelná)
        analysis = None
        if analyze:
            try:
                analysis = self.analyze_model(model)
                print("✅ Analýza dokončena")
            except Exception as e:
                print(f"⚠️ Analýza selhala: {e}")

        print("🎨 Generuji HTML kartu...")
        html = self.generate_html(model, analysis=analysis)

        output_path = self.save_html(html, model['id'])
        print(f"💾 Uloženo do: {output_path}")

        # Uložit také JSON s raw daty
        json_path = output_path.with_suffix('.json')
        model_export = model.copy()
        if analysis:
            model_export['_llm_analysis'] = analysis
        json_path.write_text(json.dumps(model_export, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"📄 JSON data: {json_path}")

        # Uložit analýzu jako samostatný markdown
        if analysis:
            md_path = output_path.with_suffix('.md')
            md_content = f"# Analýza: {model['name']}\n\n"
            md_content += f"**Model ID:** `{model['id']}`\n\n"
            md_content += f"**Datum analýzy:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
            md_content += f"**Analyzováno pomocí:** {self.ANALYZER_MODEL}\n\n"
            md_content += "---\n\n"
            md_content += self.analysis_to_markdown(analysis)
            md_path.write_text(md_content, encoding='utf-8')
            print(f"📝 Analýza (MD): {md_path}")

        return output_path


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(
        description='Generátor HTML karet pro LLM modely z OpenRouter API'
    )
    parser.add_argument(
        'model_id',
        nargs='?',
        default=None,
        help='ID modelu (např. openai/gpt-4o). Bez zadání použije nejnovější model.'
    )
    parser.add_argument(
        '--analyze', '-a',
        action='store_true',
        help='Provést LLM analýzu modelu pomocí Gemini 3 Pro'
    )

    args = parser.parse_args()

    generator = LLMModelCardGenerator()

    try:
        output_path = generator.run(args.model_id, analyze=args.analyze)
        print(f"\n🎉 Hotovo! Otevřete v prohlížeči:\n   file://{output_path.absolute()}")
    except requests.RequestException as e:
        print(f"❌ Chyba při stahování dat: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"❌ Chyba: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
