# CLAUDE.md - Agent Guide for Marigold.cz

> **Komplexni pruvodce pro praci s projektem Marigold.cz**
> Verze: 3.0 | Posledni aktualizace: 2026-04-06

---

## Obsah

1. [Projekt Overview](#projekt-overview)
2. [Struktura Projektu](#struktura-projektu)
3. [Rozdil: posts vs tech-news](#rozdil-posts-vs-tech-news)
4. [Build Commands](#build-commands)
5. [Tech-News System](#tech-news-system)
6. [Audio Content](#audio-content)
7. [CHANGELOG.md - POVINNE](#changelogmd---povinne)
8. [Coding Conventions](#coding-conventions)
9. [Deployment](#deployment)
10. [Vibecoding.cz](#vibecoding-web)

---

## Vibecoding Web

**Vibecoding.cz** je separatni web hostovany na Cloudflare Pages, ktery sdili tento repozitar.

**Pro praci s vibecoding.cz viz kompletni dokumentaci: [`docs/VIBECODING_GUIDE.md`](docs/VIBECODING_GUIDE.md)**

### Quick Reference

| Aspekt | Hodnota |
|--------|---------|
| URL | https://www.vibecoding.cz |
| Hosting | Cloudflare Pages |
| Config | `_config_vibecoding.yml` (Jekyll build pro Cloudflare) |
| Kolekce | `_vibecoding/` |
| Build | `bundle exec jekyll build --config _config_vibecoding.yml` |

### Klicove body

- Clanky jsou v `_vibecoding/[kategorie]/YYYY-MM-DD-slug.md`
- Clanky **nemaji `date:` ve front matter** - datum se bere z nazvu souboru
- Pri pridavani novych stranek do `_pages/` zkontrolovat, zda nepouzivaji kolekce nedefinovane pro vibecoding
- Build selhava s "Cannot sort a null object" pokud stranka pouziva neexistujici kolekci
- Vibecoding pouziva stale Jekyll (na Cloudflare Pages), NE Hugo

---

## Projekt Overview

**Marigold.cz** je **Hugo-based** web zamereny na technologie, AI a mobilni site. Kombinuje:
- Rucni blog posty - dlouhodobe, editovane clanky (content/posts)
- Automaticke tech-news - denne generovane zpravy z NewsAPI (content/tech-news) - **POZASTAVENO od 2026-03-29**
- AI kolekce - specializovany obsah o umele inteligenci (content/ai)
- Mobilni site - clanky o telekomunikacich (content/mobilnisite)
- Obrazy - vizualni galerie (content/obrazy)

### Klicove Technologie

- **Hugo 0.159.1 (extended)** - Static site generator
- **Python 3.11+** - Skripty pro automatizaci
- **OpenRouter API** - LLM preklady (qwen/qwen3-max)
- **NewsAPI** - Zdroj tech-news (pozastaveno)
- **GitHub Actions** - CI/CD automatizace
- **GitHub Pages** - Hosting (hugo-build.yml workflow)

---

## Struktura Projektu

```
marigold-page/
├── content/                 # Hugo content directory
│   ├── posts/               # Rucni blog posty (podle roku: 2002/-2026/)
│   ├── tech-news/           # Automaticke tech-news clanky
│   ├── ai/                  # AI kolekce
│   ├── mobilnisite/         # Mobilni site kolekce
│   ├── obrazy/              # Obrazy kolekce
│   ├── _index.md            # Hlavni stranka
│   ├── about.md, search.md  # Staticke stranky
│   └── vibecoding*.md       # Vibecoding stranky (pro Hugo verzi)
├── layouts/                 # Hugo layouts
│   ├── _default/            # Zakladni layouty (baseof, single, list)
│   ├── partials/            # Reusable komponenty (nav, footer, meta...)
│   ├── posts/               # Layout pro blog posty
│   ├── tech-news/           # Layout pro tech-news
│   ├── ai/                  # Layout pro AI kolekci
│   ├── mobilnisite/         # Layout pro mobilni site
│   └── obrazy/              # Layout pro obrazy
├── static/                  # Staticke soubory (kopiruji se 1:1 do output)
│   ├── images/              # Favicony, loga, avatar
│   └── assets/              # Obrazky k clankum (assets/ -> /assets/)
├── assets/                  # Hugo assets (obrazky v clancich, historicke)
├── data/                    # Hugo data files (YAML, JSON)
├── hugo.toml                # HLAVNI Hugo konfigurace
├── scripts/                 # Python automatizacni skripty
│   ├── generate_tech_news_newsapi.py   # Tech-news generator
│   ├── llm_cost_tracker.py             # LLM cost monitoring
│   ├── tech_news_health_check.py       # Health check system
│   └── ...
├── tests/                   # Test suite
├── docs/                    # Dokumentace
├── .github/workflows/       # GitHub Actions
│   ├── hugo-build.yml       # HLAVNI build & deploy workflow
│   ├── tech-news.yml        # Tech-news fetcher (POZASTAVENO)
│   └── ...
├── CHANGELOG.md             # Change log (POVINNY!)
└── CLAUDE.md                # Tento soubor
```

### Legacy Jekyll soubory (stale v repu)

Repozitar stale obsahuje puvodne Jekyll soubory, ktere se pouzivaji pro vibecoding.cz build na Cloudflare:
- `_config.yml`, `_config_vibecoding.yml` - Jekyll konfigurace
- `_posts/`, `_tech_news/`, `_ai/`, `_mobilnisite/`, `_obrazy/` - puvodne Jekyll kolekce
- `_layouts/`, `_includes/`, `_sass/`, `_pages/` - Jekyll layouty a komponenty
- `Gemfile`, `Gemfile.lock` - Ruby dependencies

**Pro marigold.cz se pouziva Hugo** (`hugo.toml`, `content/`, `layouts/`).

---

## Rozdil: posts vs tech-news

### `content/posts/` - Rucni Blog Posty

**Ucel**: Dlouhodoby, peclive editovany obsah.

**Charakteristika**:
- Rucne psane nebo AI-asistovane
- Nizsi frekvence (tydny/mesice)
- Hloubkova analyza, tutorialy, nazory
- Markdown format s bohatym front matter

**Format souboru**:
```
content/posts/YYYY/YYYY-MM-DD-slug.md
```
Posty jsou organizovane podle roku ve slozce (2002/, 2003/, ... 2026/).

**Front Matter Priklad** (aktualni format):
```yaml
---
slug: karpathy-llm-knowledgebase
author: Patrick Zandl
categories:
- AI
- LLM
layout: post
post_excerpt: Strucny popis clanku...
summary_points:
  - Prvni bod
  - Druhy bod
title: Nazev clanku
thumbnail: https://www.marigold.cz/assets/obrazek.jpg
---
```

**Poznamky k front matter**:
- `date` se **nebere z front matter** ale z nazvu souboru (nastaveno v hugo.toml: `date = [":filename", ":default"]`)
- `layout: post` je volitelne, Hugo pouzije `layouts/posts/single.html`
- `thumbnail` muze byt plna URL nebo lokalni cesta `/assets/obrazek.jpg`
- Lokalni obrazky pro thumbnaily ukladejte do `static/assets/` nebo `assets/`

**Permalink**: `/item/:slug/`

---

### `content/tech-news/` - Automaticke Tech-News

**STAV: POZASTAVENO od 2026-03-29** (workflow disabled)

**Ucel**: Aktualni technologicke zpravy, automaticky stahovane, prekladane a publikovane.

**Charakteristika**:
- Plne automatizovane (NewsAPI -> LLM preklad -> Hugo)
- Prelozeno z anglictiny do cestiny
- Hodnoceni dulezitosti (1-5 hvezdicek)
- Kratkodobe relevantni (dny/tydny)

**Format souboru**:
```
content/tech-news/YYYY-MM-DD-slug.md
```

**Front Matter Priklad**:
```yaml
---
author: Jmeno autora
category: ai bezpecnost
companies:
- MIT
date: '2026-02-20 01:00:38'
description: Popis clanku...
importance: 5
original_title: English Title
publishedAt: '2026-02-20T01:00:38+00:00'
slug: slug-clanku
source:
  emoji: ikona
  name: ZDNet
title: Cesky nazev
source_url: https://...
urlToImage: https://...
---
```

**Permalink**: `/tech-news/:year-:month-:day/:slug/`

**Kdy pouzit**:
- NIKDY rucne - je to automaticky system!
- Pro manualni tech clanky pouzijte `content/posts/`

---

## Build Commands

### Vyvoj

```bash
# Spustit lokalni server s live reload
hugo server

# Spustit s draft posty
hugo server -D

# Build bez serveru
hugo --minify

# Build s drafty
hugo -D
```

### Tech-News Generovani (POZASTAVENO)

```bash
# Vygenerovat tech-news (vyzaduje NEWS_API_KEY a OPENROUTER_API_KEY)
python3 scripts/generate_tech_news_newsapi.py

# Health check
python3 scripts/tech_news_health_check.py --output _data/tech_news_health.json

# LLM cost report
python3 scripts/generate_llm_cost_report.py --summary-only
```

### Testovani

```bash
# Vsechny testy
pytest

# Konkretni test soubor
pytest tests/test_health_check.py

# S coverage
pytest --cov=scripts tests/
```

---

## Tech-News System

**STAV: POZASTAVENO od 2026-03-29** - workflow `tech-news.yml` ma `if: false`

### Architektura

```
NewsAPI -> Python Script -> LLM Translation (qwen/qwen3-max) -> Hugo Collection -> GitHub Pages
```

### Komponenty

1. **Generator**: `scripts/generate_tech_news_newsapi.py`
   - Stahuje clanky z NewsAPI
   - Preklada do cestiny pomoci OpenRouter/qwen3-max
   - Detekuje dulezitost (1-5)
   - Vytvari markdown soubory v `content/tech-news/`

2. **Health Check**: `scripts/tech_news_health_check.py`
   - Kontroluje cerstvost clanku
   - Detekuje % clanku v cestine
   - Validuje kvalitu obsahu
   - Generuje `_data/tech_news_health.json`

3. **Cost Tracker**: `scripts/llm_cost_tracker.py`
   - Sleduje LLM API volani
   - Uklada do `_data/llm_costs.db`
   - Generuje reporty

### Layouts (Hugo)

- `layouts/tech-news/single.html` - Jednotlive clanky
- `layouts/tech-news/list.html` - Seznam/archiv

---

## Audio Content

Audio soubory existuji v `audio/` a `static/audio/` (historicke MP3 z podcastu).

Podcast generovani bylo **pozastaveno** (workflow `generate_podcast.yml` ma `if: false` od 2026-03-29).

---

## CHANGELOG.md - POVINNE

### KRITICKE PRAVIDLO

**PO KAZDEM COMMITU DO GITHUBU MUSITE AKTUALIZOVAT `CHANGELOG.md`!**

### Format

```markdown
# Changelog

Vsechny vyznamne zmeny v projektu jsou dokumentovany v tomto souboru.

Format vychazi z [Keep a Changelog](https://keepachangelog.com/cs/1.0.0/),
a projekt dodrzuje [Semantic Versioning](https://semver.org/lang/cs/).

## [Unreleased]

### Added
- Nove funkce a vlastnosti

### Changed
- Zmeny v existujici funkcionalite

### Fixed
- Opravy bugu
```

### Verzovani (Semantic Versioning)

- **MAJOR** (X.0.0): Breaking changes, zasadni prepisy
- **MINOR** (x.Y.0): Nove funkce, zpetne kompatibilni
- **PATCH** (x.y.Z): Bugfixy, drobne zmeny

---

## Coding Conventions

### Python (PEP 8 + Black)

- Type hints pro vsechny funkce
- Docstrings (Google style)
- Logging misto print()
- Specificke exception handling
- Black formatovani (`black .`)
- Meaningful variable names

### Hugo Templates (Go Templates)

```go-html-template
{{/* SPRAVNE - mezery kolem promennych */}}
{{ .Title }}
{{ .Date.Format "2006-01-02" }}

{{/* SPATNE - bez mezer */}}
{{.Title}}
{{.Date.Format "2006-01-02"}}
```

### YAML Front Matter

```yaml
# SPRAVNE
---
title: "Clanek s uvozovkami"
slug: clanek-slug
categories:
  - technologie
  - ai
summary_points:
  - Prvni bod
  - Druhy bod
thumbnail: https://www.marigold.cz/assets/obrazek.jpg
---
```

---

## Deployment

### GitHub Pages (Hugo)

**Automaticky deployment**:
1. Push do `main` vetve
2. GitHub Actions (`hugo-build.yml`) build Hugo s `--minify`
3. Deploy do GitHub Pages pres `actions/deploy-pages@v4`
4. Dostupne na `https://www.marigold.cz`

**Hugo verze v CI**: 0.159.1 (extended)

### Environment Variables (Secrets)

Nastavene v GitHub repo settings:

```
NEWS_API_KEY=sk-...           # NewsAPI klic (pro tech-news)
OPENROUTER_API_KEY=sk-...     # OpenRouter API pro LLM
```

---

## Quick Reference

### Caste ukoly

```bash
# Novy blog post
mkdir -p content/posts/$(date +%Y)
touch content/posts/$(date +%Y)/$(date +%Y-%m-%d)-title.md

# Lokalni development
hugo server

# Build
hugo --minify

# Kde ukladat obrazky pro thumbnail
# -> static/assets/nazev.jpg  (dostupne jako /assets/nazev.jpg)

# Pred commitem
# 1. Aktualizovat CHANGELOG.md
# 2. git add, commit, push
```

### Dulezite soubory

```
hugo.toml                                # Hugo konfigurace
CHANGELOG.md                             # Change log (POVINNY!)
CLAUDE.md                                # Tento soubor
data/tech_news_sources.yaml              # Tech-news zdroje
scripts/generate_tech_news_newsapi.py    # Tech-news generator
.github/workflows/hugo-build.yml         # Hlavni build workflow
```

### Uzitecne odkazy

- **Zivy web**: https://www.marigold.cz
- **Tech-news**: https://www.marigold.cz/tech-news/
- **Vibecoding**: https://www.vibecoding.cz

---

## Troubleshooting

### Hugo build fails

```bash
# Vycistit cache
rm -rf public/ resources/

# Build s verbose
hugo --minify --verbose

# Zkontrolovat verzi
hugo version
```

### Permalinky nefunguji

```bash
# Zkontrolovat hugo.toml permalinks sekci
grep -A10 "permalinks" hugo.toml

# Rebuild site
hugo --minify

# Zkontrolovat public/ adresar
ls -la public/item/
```

---

## Historie Verzi

- **3.0** (2026-04-06): Aktualizace na Hugo, pozastaveni tech-news a podcastu, oprava struktury
- **2.0** (2025-11-15): Pridan CHANGELOG requirement, audio info, rozsirena dokumentace
- **1.0** (2025-08-25): Initial verze

---

**Konec dokumentace** | Pro dotazy: Aktualizujte CHANGELOG.md!
