# CLAUDE.md - Agent Guide for Marigold.cz

> **Komplexní průvodce pro práci s projektem Marigold.cz**
> Verze: 2.0 | Poslední aktualizace: 2025-11-15

---

## 📋 Obsah

1. [Projekt Overview](#projekt-overview)
2. [Struktura Projektu](#struktura-projektu)
3. [Rozdíl: _posts vs _tech_news](#rozdíl-_posts-vs-_tech_news)
4. [Build Commands](#build-commands)
5. [Tech-News Systém](#tech-news-systém)
6. [Audio Content](#audio-content)
7. [CHANGELOG.md - POVINNÉ](#changelogmd---povinné)
8. [Coding Conventions](#coding-conventions)
9. [Deployment](#deployment)
10. [Vibecoding.cz](#vibecoding-web)

---

## Vibecoding Web

**Vibecoding.cz** je separátní web hostovaný na Cloudflare Pages, který sdílí tento repozitář.

**Pro práci s vibecoding.cz viz kompletní dokumentaci: [`docs/VIBECODING_GUIDE.md`](docs/VIBECODING_GUIDE.md)**

### Quick Reference

| Aspekt | Hodnota |
|--------|---------|
| URL | https://www.vibecoding.cz |
| Hosting | Cloudflare Pages |
| Config | `_config_vibecoding.yml` |
| Kolekce | `_vibecoding/` |
| Build | `bundle exec jekyll build --config _config_vibecoding.yml` |

### Klíčové body

- Články jsou v `_vibecoding/[kategorie]/YYYY-MM-DD-slug.md`
- Články **nemají `date:` ve front matter** - datum se bere z názvu souboru
- Při přidávání nových stránek do `_pages/` zkontrolovat, zda nepoužívají kolekce nedefinované pro vibecoding
- Build selhává s "Cannot sort a null object" pokud stránka používá neexistující kolekci

---

## Projekt Overview

**Marigold.cz** je Jekyll-based web zaměřený na technologie, AI a mobilní sítě. Kombinuje:
- 📝 **Ruční blog posty** - dlouhodobé, editované články (_posts)
- 📰 **Automatické tech-news** - denně generované zprávy z NewsAPI (_tech_news)
- 🤖 **AI kolekce** - specializovaný obsah o umělé inteligenci (_ai)
- 📱 **Mobilní sítě** - články o telekomunikacích (_mobilnisite)
- 🖼️ **Obrazy** - vizuální galerie (_obrazy)

### Klíčové Technologie

- **Jekyll 3.10.0** - Static site generator
- **Python 3.11+** - Skripty pro automatizaci
- **OpenRouter API** - LLM překlady (qwen/qwen3-max)
- **NewsAPI** - Zdroj tech-news
- **GitHub Actions** - CI/CD automatizace
- **GitHub Pages** - Hosting

---

## Struktura Projektu

```
marigold-page/
├── _posts/              # 📝 Ruční blog posty (hlavní obsah)
├── _tech_news/          # 📰 Automatické tech-news články (3000+ souborů)
├── _ai/                 # 🤖 AI kolekce
├── _mobilnisite/        # 📱 Mobilní sítě kolekce
├── _obrazy/             # 🖼️ Obrazy kolekce
├── _pages/              # 📄 Statické stránky
├── _layouts/            # 🎨 Jekyll layouts
├── _includes/           # 🧩 Reusable components
├── _data/               # 💾 Data files (YAML, JSON)
├── _sass/               # 🎨 SCSS styles
├── scripts/             # 🐍 Python automatizační skripty
│   ├── generate_tech_news_newsapi.py      # Hlavní tech-news generátor
│   ├── llm_cost_tracker.py                # LLM cost monitoring
│   ├── tech_news_health_check.py          # Health check systém
│   └── ...
├── tests/               # 🧪 Test suite
├── docs/                # 📚 Dokumentace
├── .github/workflows/   # ⚙️ GitHub Actions
├── CHANGELOG.md         # 📋 Change log (POVINNÝ!)
└── CLAUDE.md            # 📖 Tento soubor
```

---

## Rozdíl: _posts vs _tech_news

### 📝 `_posts/` - Ruční Blog Posty

**Účel**: Dlouhodobý, pečlivě editovaný obsah, který vytvářejí lidé.

**Charakteristika**:
- ✍️ Ručně psané nebo AI-asistované
- 📅 Nižší frekvence (týdny/měsíce)
- 🎯 Hloubková analýza, tutoriály, názory
- 🔧 Vyžaduje manuální edit a schválení
- 📝 Markdown formát s bohatým front matter

**Formát souboru**:
```
_posts/YYYY-MM-DD-title.md
```

**Front Matter Příklad**:
```yaml
---
layout: post
title: "Jak funguje 5G standalone"
date: 2025-11-15 14:30:00
categories: [mobilnisite, technologie]
tags: [5G, telekomunikace]
author: Patrick Zandl
summary_points:
  - Standalone 5G nepotřebuje 4G infrastrukturu
  - Nižší latence než NSA varianta
  - Vyšší náklady na deployment
image: /images/5g-standalone.jpg
---
```

**Permalink**: `/item/:title/`

**Kdy použít**:
- Tutoriály a návody
- Hloubkové analýzy
- Názorové články
- Recenze produktů
- Dlouhodobě relevantní obsah

---

### 📰 `_tech_news/` - Automatické Tech-News

**Účel**: Aktuální technologické zprávy, automaticky stahované, překládané a publikované.

**Charakteristika**:
- 🤖 Plně automatizované (NewsAPI → LLM překlad → Jekyll)
- ⚡ Vysoká frekvence (každé 4 hodiny via GitHub Actions)
- 🌍 Přeloženo z angličtiny do češtiny
- 📊 Hodnocení důležitosti (1-5 hvězdiček)
- 🔄 Krátkodobě relevantní (dny/týdny)

**Formát souboru**:
```
_tech_news/YYYY-MM-DD-slug.md
```

**Front Matter Příklad**:
```yaml
---
layout: tech_news_article
title: "Apple představil iPhone 17 Pro"
original_title: "Apple Announces iPhone 17 Pro"
slug: apple-predstavil-iphone-17-pro
description: "Apple dnes oficiálně odhalil iPhone 17 Pro..."
publishedAt: '2025-11-15T14:30:00+00:00'
date: '2025-11-15 14:30:00'
url: https://techcrunch.com/...
category: hardware
importance: 4
source:
  emoji: 🚀
  name: TechCrunch
companies:
  - Apple
urlToImage: https://...
---
```

**Permalink**: `/tech-news/:year-:month-:day/:slug/`

**Generování**:
```bash
# Automaticky (GitHub Actions každé 4h)
python scripts/generate_tech_news_newsapi.py

# Manuálně
python scripts/generate_tech_news_newsapi.py
```

**Kdy použít**:
- NIKDY ručně - je to automatický systém!
- Nedotýkejte se souborů v `_tech_news/` ručně
- Pro manuální tech články použijte `_posts/`

---

### 🎯 Rozhodovací Strom

```
Chci přidat článek
    │
    ├─> Je to časově citlivá zpráva o technologiích?
    │       │
    │       ├─> ANO → Nechte to na automatizaci (_tech_news)
    │       └─> NE  → Pokračuj níže
    │
    └─> Je to hloubková analýza/tutoriál/názor?
            │
            ├─> ANO → _posts/ (ruční článek)
            └─> NE  → Zvažte, zda je to vůbec potřeba
```

---

## Build Commands

### Vývoj

```bash
# Spustit lokální server s live reload
bundle exec jekyll serve --livereload

# Spustit s draft posty
bundle exec jekyll serve --drafts

# Build bez serveru
bundle exec jekyll build

# Build s drafty
bundle exec jekyll build --drafts
```

### Tech-News Generování

```bash
# Vygenerovat tech-news (vyžaduje NEWS_API_KEY a OPENROUTER_API_KEY)
python3 scripts/generate_tech_news_newsapi.py

# Health check
python3 scripts/tech_news_health_check.py --output _data/tech_news_health.json

# LLM cost report
python3 scripts/generate_llm_cost_report.py --summary-only
```

### Testování

```bash
# Všechny testy
pytest

# Konkrétní test soubor
pytest tests/test_health_check.py

# S coverage
pytest --cov=scripts tests/
```

---

## Tech-News Systém

### Architektura

```
NewsAPI → Python Script → LLM Translation (qwen/qwen3-max) → Jekyll Collection → GitHub Pages
```

### Komponenty

1. **Generator**: `scripts/generate_tech_news_newsapi.py`
   - Stahuje články z NewsAPI
   - Překládá do češtiny pomocí OpenRouter/qwen3-max
   - Detekuje důležitost (1-5)
   - Vytváří markdown soubory v `_tech_news/`

2. **Health Check**: `scripts/tech_news_health_check.py`
   - Kontroluje čerstvost článků
   - Detekuje % článků v češtině
   - Validuje kvalitu obsahu
   - Generuje `_data/tech_news_health.json`

3. **Cost Tracker**: `scripts/llm_cost_tracker.py`
   - Sleduje LLM API volání
   - Ukládá do `_data/llm_costs.db`
   - Generuje reporty

### Layouts

- **tech_news_article.html** - Jednotlivé články (`/tech-news/YYYY-MM-DD/slug/`)
- **tech_news_day.html** - Denní přehledy (`/tech-news/YYYY-MM-DD/`)
- **tech-news.html** - Hlavní stránka (`/tech-news/`)
- **tech-news-archiv.html** - Archiv (`/tech-news/archiv/`)

### Monitoring

**Uptimerobot Setup**:
```
Type: HTTP(s) - Keyword
URL: https://marigold.cz/health-check/
Keyword: "status": "OK"
Interval: 5 minutes
Alert: Keyword NOT found for 2 consecutive checks
```

**Dokumentace**: `docs/UPTIMEROBOT_SETUP.md`

---

## Audio Content

### Generování Audio

**POZNÁMKA**: Audio generování není aktuálně implementováno.

**Plánovaná funkcionalita**:
- TTS (Text-to-Speech) pro články v `_posts/`
- Použití: OpenAI TTS API nebo ElevenLabs
- Formát: MP3, uložené v `assets/audio/`
- Front matter: `audio_url: /assets/audio/2025-11-15-article.mp3`

**Implementace (TODO)**:
```bash
# Budoucí skript
python scripts/generate_audio.py --post _posts/2025-11-15-article.md
```

---

## CHANGELOG.md - POVINNÉ

### 🚨 KRITICKÉ PRAVIDLO

**PO KAŽDÉM COMMITU DO GITHUBU MUSÍTE AKTUALIZOVAT `CHANGELOG.md`!**

### Formát

```markdown
# Changelog

Všechny významné změny v projektu jsou dokumentovány v tomto souboru.

Formát vychází z [Keep a Changelog](https://keepachangelog.com/cs/1.0.0/),
a projekt dodržuje [Semantic Versioning](https://semver.org/lang/cs/).

## [Unreleased]

### Added
- (čekající změny před příštím release)

## [X.Y.Z] - YYYY-MM-DD

### Added
- Nové funkce a vlastnosti

### Changed
- Změny v existující funkcionalitě

### Deprecated
- Brzy odstraněné funkce

### Removed
- Nyní odstraněné funkce

### Fixed
- Opravy bugů

### Security
- Bezpečnostní záplaty
```

### Verzování (Semantic Versioning)

```
MAJOR.MINOR.PATCH  (např. 2.1.3)
```

- **MAJOR** (X.0.0): Breaking changes, zásadní přepisy
  - Změna struktury projektu
  - Odstranění starých features
  - Nekompatibilní API změny

- **MINOR** (x.Y.0): Nové funkce, zpětně kompatibilní
  - Nový tech-news health check systém
  - Nový layout nebo kolekce
  - Nové skripty

- **PATCH** (x.y.Z): Bugfixy, drobné změny
  - Oprava permalinků
  - CSS tweaky
  - Dokumentace update

### Příklad Workflow

```bash
# 1. Provedení změn
git add _layouts/tech_news_day.html
git add _pages/tech-news-archiv.html

# 2. PŘED COMMITEM - Aktualizovat CHANGELOG.md
# Přidat pod ## [Unreleased] sekci:

### Fixed
- Opraveny permalinky v tech_news_day layoutu - články nyní vedou na interní stránky
- Vytvořena archivní stránka /tech-news/archiv/ s přehledem po měsících

# 3. Commit s odkazem na CHANGELOG
git commit -m "Fix: Tech-news permalinky a archiv

- Opraveny odkazy v tech_news_day.html na interní permalinky
- Vytvořena archivní stránka /tech-news/archiv/
- Detaily v CHANGELOG.md"

# 4. Push
git push

# 5. Při vytváření release - přesunout [Unreleased] do [X.Y.Z]
```

### Ukázkový CHANGELOG.md Entry

```markdown
## [Unreleased]

### Added
- Archivní stránka `/tech-news/archiv/` s přehledem článků po měsících a dnech
- Health check systém pro monitoring tech-news generování

### Fixed
- Permalinky v `tech_news_day.html` - články nyní vedou na `/tech-news/YYYY-MM-DD/slug/` místo externích URL
- Model pro tech-news aktualizován z `openrouter/polaris-alpha` na `qwen/qwen3-max`

### Changed
- GitHub Actions workflow - health check je nyní non-blocking (|| true)
```

---

## Coding Conventions

### Python (PEP 8 + Black)

```python
# ✅ SPRÁVNĚ
def generate_tech_news(api_key: str, output_dir: Path) -> bool:
    """
    Generuje tech-news články z NewsAPI.

    Args:
        api_key: NewsAPI klíč
        output_dir: Výstupní adresář pro markdown soubory

    Returns:
        True pokud úspěšné, jinak False
    """
    logger.info(f"🚀 Spouštím generování do {output_dir}")

    try:
        articles = fetch_articles(api_key)
        return process_articles(articles, output_dir)
    except Exception as e:
        logger.error(f"❌ Chyba: {e}")
        return False

# ❌ ŠPATNĚ
def gen(k,o):
    print("Starting...")
    try:
        a=fetch(k)
        return proc(a,o)
    except:
        print("Error")
        return False
```

**Pravidla**:
- Type hints pro všechny funkce
- Docstrings (Google style)
- Logging místo print()
- Specifické exception handling
- Black formátování (`black .`)
- Meaningful variable names

### Jekyll/Liquid

```liquid
{%- comment -%}
✅ SPRÁVNĚ - mezery kolem proměnných
{%- endcomment -%}
{{ article.title }}
{{ article.date | date: '%Y-%m-%d' }}

{%- comment -%}
❌ ŠPATNĚ - bez mezer
{%- endcomment -%}
{{article.title}}
{{article.date|date:'%Y-%m-%d'}}
```

### YAML Front Matter

```yaml
# ✅ SPRÁVNĚ
---
layout: post
title: "Článek s uvozovkami"
date: 2025-11-15 14:30:00
categories:
  - technologie
  - ai
tags: [5g, mobilní sítě]
summary_points:
  - První bod se všemi detaily
  - Druhý bod také podrobný
---

# ❌ ŠPATNĚ
---
layout:post
title:Článek bez uvozovek
date:2025-11-15
categories:[technologie,ai]
tags:5g,mobilní sítě
---
```

---

## Deployment

### GitHub Pages

**Automatický deployment**:
1. Push do `main` větve
2. GitHub Actions build Jekyll
3. Deploy do GitHub Pages
4. Dostupné na `https://www.marigold.cz`

### GitHub Actions Workflows

**`.github/workflows/tech-news.yml`**:
- Trigger: Každé 4 hodiny + manual
- Kroky:
  1. Checkout repo
  2. Install Python dependencies
  3. Generate tech-news (`generate_tech_news_newsapi.py`)
  4. Optimize images
  5. Generate manifest
  6. Health check (non-blocking)
  7. Commit změny
  8. Push do `main`

### Environment Variables (Secrets)

Nastavené v GitHub repo settings:

```
NEWS_API_KEY=sk-...           # NewsAPI klíč
OPENROUTER_API_KEY=sk-...     # OpenRouter API pro LLM
```

---

## Quick Reference

### Časté úkoly

```bash
# Nový blog post
touch _posts/$(date +%Y-%m-%d)-title.md

# Lokální development
bundle exec jekyll serve --livereload

# Vygenerovat tech-news
python3 scripts/generate_tech_news_newsapi.py

# Health check
python3 scripts/tech_news_health_check.py --output _data/tech_news_health.json

# LLM cost report
python3 scripts/generate_llm_cost_report.py --summary-only

# Před commitem
# 1. Aktualizovat CHANGELOG.md
# 2. git add, commit, push
```

### Důležité soubory

```
_config.yml                              # Jekyll konfigurace
CHANGELOG.md                             # Change log (POVINNÝ!)
CLAUDE.md                                # Tento soubor
_data/tech_news_sources.yaml            # Tech-news zdroje
_data/tech_news_health.json              # Health status
scripts/generate_tech_news_newsapi.py    # Tech-news generátor
scripts/tech_news_health_check.py        # Health monitoring
```

### Užitečné odkazy

- **Živý web**: https://www.marigold.cz
- **Health status**: https://www.marigold.cz/health-status/
- **Health JSON**: https://www.marigold.cz/health-check/
- **Tech-news**: https://www.marigold.cz/tech-news/
- **Archiv**: https://www.marigold.cz/tech-news/archiv/

---

## Troubleshooting

### Tech-News negeneruje články

```bash
# 1. Zkontrolovat API klíče
echo $NEWS_API_KEY
echo $OPENROUTER_API_KEY

# 2. Zkontrolovat health status
python3 scripts/tech_news_health_check.py --output _data/tech_news_health.json

# 3. Zkontrolovat logy
tail -f _data/llm_costs.db
```

### Jekyll build fails

```bash
# Vyčistit cache
rm -rf _site .jekyll-cache

# Reinstall dependencies
bundle install

# Build s verbose
bundle exec jekyll build --verbose --trace
```

### Permalinky nefungují

```bash
# Zkontrolovat _config.yml collections
grep -A10 "collections:" _config.yml

# Rebuild site
bundle exec jekyll build

# Zkontrolovat _site adresář
ls -la _site/tech-news/2025-11-15/
```

---

## Historie Verzí

- **2.0** (2025-11-15): Přidán CHANGELOG requirement, audio info, rozšířená dokumentace
- **1.0** (2025-08-25): Initial verze

---

**Konec dokumentace** | Pro dotazy: Aktualizujte CHANGELOG.md! 📋
