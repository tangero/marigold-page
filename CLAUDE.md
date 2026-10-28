# CLAUDE.md - Agent Guide for Marigold.cz

> **Komplexni pruvodce pro praci s projektem Marigold.cz**
> Verze: 3.1 | Posledni aktualizace: 2026-10-28

---

## Obsah

1. [Projekt Overview](#projekt-overview)
2. [Struktura Projektu](#struktura-projektu)
3. [Blog posty a obrazky](#blog-posty-a-obrazky)
4. [Build Commands](#build-commands)
5. [Audio Content](#audio-content)
6. [CHANGELOG.md - POVINNE](#changelogmd---povinne)
7. [Coding Conventions](#coding-conventions)
8. [Deployment](#deployment)
9. [Vibecoding.cz](#vibecoding-web)

---

## Vibecoding Web

**Vibecoding.cz** se uz z tohoto repozitare NEBUDUJE. Bezi ze samostatneho repozitare `~/Github/vibecoding-site` (Astro) jako Cloudflare Pages projekt `vibecoding-site` (domeny vibecoding.cz, agentnivyvoj.cz).

V tomto repu zustavaji jen legacy pozustatky: `_vibecoding/`, `_config_vibecoding.yml`, `docs/VIBECODING_GUIDE.md`. Cloudflare Pages projekt `marigold-page` se z tohoto repa stale buildi, ale bezi jen na `marigold-page.pages.dev` bez vlastni domeny (stav 2026-10-28).

Sdileny je Cloudflare R2 bucket `vibecoding-assets` (doména `media.vibecoding.cz`), viz [Audio Content](#audio-content).

---

## Projekt Overview

**Marigold.cz** je **Hugo-based** web zamereny na technologie, AI a mobilni site. Kombinuje:
- Rucni blog posty - dlouhodobe, editovane clanky (content/posts)
- AI kolekce - specializovany obsah o umele inteligenci (content/ai)
- Mobilni site - clanky o telekomunikacich (content/mobilnisite)
- Obrazy - vizualni galerie (content/obrazy)

### Klicove Technologie

- **Hugo 0.159.1 (extended)** - Static site generator
- **Python 3.11+** - Skripty pro automatizaci
- **GitHub Actions** - CI/CD automatizace
- **GitHub Pages** - Hosting (hugo-build.yml workflow)

---

## Struktura Projektu

```
marigold-page/
├── content/                 # Hugo content directory
│   ├── posts/               # Rucni blog posty (podle roku: 2002/-2026/)
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
│   ├── ai/                  # Layout pro AI kolekci
│   ├── mobilnisite/         # Layout pro mobilni site
│   └── obrazy/              # Layout pro obrazy
├── static/                  # Staticke soubory (kopiruji se 1:1 do output)
│   ├── images/              # Favicony, loga, avatar
│   └── assets/              # Obrazky k clankum ve WebP (assets/ -> /assets/)
├── assets/scss/             # Hugo assets: jen SCSS (main.scss pres resources.Get)
├── data/                    # Hugo data files (YAML, JSON)
├── hugo.toml                # HLAVNI Hugo konfigurace
├── scripts/                 # Python skripty (LLM katalog, infografiky, migrace)
├── docs/                    # Dokumentace
├── .github/workflows/       # GitHub Actions
│   ├── hugo-build.yml       # HLAVNI build & deploy workflow
│   └── build.yml            # Stary Jekyll build (DISABLED)
├── CHANGELOG.md             # Change log (POVINNY!)
└── CLAUDE.md                # Tento soubor
```

### Legacy Jekyll soubory (stale v repu)

Repozitar stale obsahuje puvodni Jekyll soubory (nepublikuji se na zadnou vlastni domenu):
- `_config.yml`, `_config_vibecoding.yml` - Jekyll konfigurace
- `_posts/`, `_ai/`, `_mobilnisite/`, `_obrazy/` - puvodne Jekyll kolekce
- `_layouts/`, `_includes/`, `_sass/`, `_pages/` - Jekyll layouty a komponenty
- `Gemfile`, `Gemfile.lock` - Ruby dependencies

**Pro marigold.cz se pouziva Hugo** (`hugo.toml`, `content/`, `layouts/`).

---

## Blog posty a obrazky

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
thumbnail: https://www.marigold.cz/assets/obrazek.webp
---
```

**Poznamky k front matter**:
- `date` se **nebere z front matter** ale z nazvu souboru (nastaveno v hugo.toml: `date = [":filename", ":default"]`)
- `layout: post` je volitelne, Hugo pouzije `layouts/posts/single.html`
- `thumbnail` muze byt plna URL nebo lokalni cesta `/assets/obrazek.webp`
- Obrazky ukladejte do `static/assets/` (NE do `assets/` - ten Hugo nepublikuje)

**Permalink**: `/item/:slug/`

### Obrazky - VZDY WebP

Obrazky v `static/assets/` jsou ve WebP (od 2026-10-28, puvodne 350 MB JPG/PNG -> 49 MB). Novy obrazek pred commitem prevest:

```bash
magick vstup.jpg -auto-orient -colorspace sRGB -resize '2000x>' -strip -quality 82 -define webp:method=6 static/assets/nazev.webp
```

- Max sirka 2000 px, kvalita 82. Pokud by WebP vysel vetsi nez original (mala grafika), nechat original
- Pozor na velikost pismen v nazvu: GitHub Pages ji rozlisuje, macOS ne - odkaz musi sedet presne
- Velka media (audio, video) do repa nepatri, patri do R2 (viz Audio Content)

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

---

## Audio Content

Audio soubory (historicke MP3/M4A z podcastu) jsou v Cloudflare R2: bucket `vibecoding-assets` (sdileny s vibecoding.cz), prefix `marigold/audio/`, verejne na `https://media.vibecoding.cz/marigold/audio/<soubor>`. Do repozitare audio NEPRIDAVAT (zvetsuje deploy na GitHub Pages). Nahrani: `wrangler r2 object put vibecoding-assets/marigold/audio/<soubor> --file=<soubor> --content-type=audio/mpeg --remote`, v clanku pak `audio_url: https://media.vibecoding.cz/marigold/audio/<soubor>`.

Podcast generovani bylo **odstraneno** (workflowy smazany 2026-07-11; drive `if: false` od 2026-03-29).
Push notifikace (OneSignal, FCM/Firebase) byly take **odstraneny** z GitHub Actions — nefungovaly (legacy cesty `_posts/`).

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

**Rychlost deploye** (stav 2026-10-28): cely beh ~1,5-2,5 min, Pages artefakt ~140 MB.
- Checkout je `fetch-depth: 1` - build nepouziva `.GitInfo`, plna historie ma 6,5 GB. Pokud by se nekdy zapnulo `enableGitInfo`, je potreba `fetch-depth: 0`
- GitHub Pages: limit 1 GB na web a 10 min na deploy. Driv byl artefakt 760 MB a deploy trval az 8 min - velke soubory (audio, nekomprimovane obrazky) do `static/` nedavat
- Workflow bezi i denne v 5:15 UTC (cron) kvuli obnove Substack promo
- Lokalni Hugo z brew (0.169+) build odmitne kvuli `content/aiprace.html` (`security.allowContent`). Pro lokalni test: `hugo --config hugo.toml,sec.toml`, kde `sec.toml` obsahuje `[security]\n  allowContent = [".*"]`. Pri upgradu Huga v CI totez pridat do `hugo.toml`

### Environment Variables (Secrets)

Nastavene v GitHub repo settings:

```
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
# -> static/assets/nazev.webp  (dostupne jako /assets/nazev.webp)

# Pred commitem
# 1. Aktualizovat CHANGELOG.md
# 2. git add, commit, push
```

### Dulezite soubory

```
hugo.toml                                # Hugo konfigurace
CHANGELOG.md                             # Change log (POVINNY!)
CLAUDE.md                                # Tento soubor
.github/workflows/hugo-build.yml         # Hlavni build workflow
```

### Uzitecne odkazy

- **Zivy web**: https://www.marigold.cz
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

- **3.1** (2026-10-28): Smazany tech-news, audio v R2, obrazky ve WebP, vibecoding.cz v samostatnem repu
- **3.0** (2026-04-06): Aktualizace na Hugo, pozastaveni tech-news a podcastu, oprava struktury
- **2.0** (2025-11-15): Pridan CHANGELOG requirement, audio info, rozsirena dokumentace
- **1.0** (2025-08-25): Initial verze

---

**Konec dokumentace** | Pro dotazy: Aktualizujte CHANGELOG.md!
