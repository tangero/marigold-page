# Vibecoding.cz - Technická dokumentace

> Kompletní průvodce pro práci s webem vibecoding.cz
> Poslední aktualizace: 2025-12-09

---

## Architektura

**Vibecoding.cz** je **separátní web** hostovaný na Cloudflare Pages, který sdílí repozitář s marigold.cz, ale používá vlastní konfiguraci.

```
marigold-page/
├── _vibecoding/           # Kolekce článků pro vibecoding.cz
│   ├── claude-code/       # Články o Claude Code
│   ├── cursor/            # Články o Cursor
│   ├── gemini-cli/        # Články o Gemini CLI
│   ├── lovable-dev/       # Články o Lovable
│   ├── replit/            # Články o Replit
│   ├── windsurf/          # Články o Windsurf
│   ├── ostatni/           # Ostatní AI nástroje
│   └── ...
├── _config_vibecoding.yml # Konfigurace pro vibecoding build
├── vibecoding-index.md    # Hlavní stránka (index)
├── _pages/vibecoding-*.md # Kategorizační stránky
└── _layouts/vibecoding-*.html # Layouty specifické pro vibecoding
```

## Klíčové soubory

| Soubor | Účel |
|--------|------|
| `_config_vibecoding.yml` | Jekyll konfigurace pro vibecoding build |
| `vibecoding-index.md` | Hlavní stránka webu |
| `_pages/vibecoding-cursor.md` | Stránka kategorie Cursor |
| `_pages/vibecoding-claude.md` | Stránka kategorie Claude Code |
| `_layouts/vibecoding-default.html` | Výchozí layout |
| `assets/vibecoding-index.css` | Styly pro vibecoding |

## Hosting a Deployment

### Cloudflare Pages

- **URL**: https://www.vibecoding.cz
- **Build command**: `bundle exec jekyll build --config _config_vibecoding.yml`
- **Output directory**: `_site`
- **Branch**: `main`

Build se spouští automaticky při každém push do main větve.

### Environment Variables (Cloudflare)

```
JEKYLL_ENV = production
RUBY_VERSION = 3.2.0
```

## Struktura článků

### Umístění

Články jsou v `_vibecoding/[kategorie]/YYYY-MM-DD-slug.md`

### Front Matter

```yaml
---
author: Patrick Zandl
categories:
- AI
- Cursor
- název kategorie
layout: post
post_excerpt: Krátký popis článku pro náhledy
title: Název článku
---
```

**POZOR**: Články **nemají `date:` v front matter** - datum se bere z názvu souboru!

### Kategorie (adresáře)

| Adresář | Obsah |
|---------|-------|
| `claude-code/` | Anthropic Claude Code CLI |
| `cursor/` | Cursor IDE |
| `gemini-cli/` | Google Gemini CLI |
| `lovable-dev/` | Lovable.dev |
| `replit/` | Replit |
| `windsurf/` | Windsurf IDE |
| `ostatni/` | Další nástroje (Bolt, Kiro, n8n...) |
| `databutton/` | Databutton |
| `memex/` | Memex |
| `tempolabs/` | Tempo Labs |

## Konfigurace `_config_vibecoding.yml`

### Kritické nastavení

```yaml
collections:
  vibecoding:
    output: true
    permalink: /articles/:title/

defaults:
  - scope:
      path: "_vibecoding"
      type: "vibecoding"
    values:
      layout: "post"
```

### Exclude seznam

**DŮLEŽITÉ**: Musí obsahovat všechny soubory/kolekce z marigold.cz, které by způsobily chybu buildu:

```yaml
exclude:
  - _posts
  - _ai
  - _mobilnisite
  - _obrazy
  - _tech_news
  - _llm
  - _pages/llm.md          # Používá site.llm kolekci
  - _pages/tech-news*.html # Používá site.tech_news kolekci
  - TECH_NEWS_*.md         # Dokumentace v rootu
  - CHANGELOG.md
  - CLAUDE.md
  # ... a další
```

## Časté problémy a řešení

### 1. Build error: "Cannot sort a null object"

**Příčina**: Stránka používá kolekci, která není definována v `_config_vibecoding.yml`

**Řešení**: Přidat problematickou stránku do `exclude:` v `_config_vibecoding.yml`

```yaml
exclude:
  - _pages/problematicka-stranka.md
```

### 2. Nové články se nezobrazují

**Kontrolní seznam**:
1. Je článek ve správném adresáři `_vibecoding/[kategorie]/`?
2. Má správný formát názvu `YYYY-MM-DD-slug.md`?
3. Má správný front matter s `layout: post`?
4. Byl proveden push do main větve?
5. Proběhl Cloudflare Pages build úspěšně?

**Jak zkontrolovat Cloudflare build**:
- Cloudflare Dashboard → Pages → vibecoding-page → Deployments

### 3. Lokální testování

```bash
# Build pro vibecoding
bundle exec jekyll build --config _config_vibecoding.yml

# Serve lokálně
bundle exec jekyll serve --config _config_vibecoding.yml
```

### 4. Články z jiného webu pronikají do vibecoding

**Příčina**: Chybí exclude pro daný soubor/adresář

**Řešení**: Přidat do `exclude:` v `_config_vibecoding.yml`

## Přidání nového článku

### Postup

1. Vytvořit soubor v odpovídající kategorii:
   ```
   _vibecoding/cursor/2025-12-09-nazev-clanku.md
   ```

2. Přidat front matter:
   ```yaml
   ---
   author: Patrick Zandl
   categories:
   - AI
   - Cursor
   layout: post
   post_excerpt: Stručný popis pro náhled
   title: Cursor představil novou funkci XYZ
   ---
   ```

3. Napsat obsah článku v Markdown

4. Commit a push:
   ```bash
   git add _vibecoding/
   git commit -m "Nový článek: Cursor XYZ"
   git push
   ```

5. Cloudflare Pages automaticky zbuiluje a nasadí

## Přidání nové kategorie

1. Vytvořit adresář `_vibecoding/nova-kategorie/`

2. Vytvořit stránku kategorie `_pages/vibecoding-nova-kategorie.md`:
   ```yaml
   ---
   layout: vibecoding-default
   title: Nova Kategorie - Vibecoding
   permalink: /nova-kategorie/
   ---

   # Nova Kategorie

   {% for article in site.vibecoding %}
     {% if article.path contains 'nova-kategorie' %}
       ...
     {% endif %}
   {% endfor %}
   ```

3. Přidat odkaz do navigace (pokud existuje)

## Vztah s marigold.cz

| Aspekt | Marigold.cz | Vibecoding.cz |
|--------|-------------|---------------|
| Hosting | GitHub Pages | Cloudflare Pages |
| Config | `_config.yml` | `_config_vibecoding.yml` |
| Kolekce | `_posts`, `_tech_news`, `_ai`... | `_vibecoding` |
| URL | www.marigold.cz | www.vibecoding.cz |
| Build trigger | Push to main | Push to main |

**Oba weby sdílejí**:
- Repozitář `tangero/marigold-page`
- Gemfile a dependencies
- Některé layouty a includes
- Assets (images, CSS základy)

## Debugging

### Kontrola posledního buildu

```bash
# Lokální test build
bundle exec jekyll build --config _config_vibecoding.yml 2>&1 | head -50

# Ověření vygenerovaných článků
ls _site/articles/
```

### Kontrola konfigurace

```bash
# Zobrazit exclude seznam
grep -A 100 "exclude:" _config_vibecoding.yml

# Najít kolekce používané v pages
grep -r "site\." _pages/vibecoding*.md
```

### Log z Cloudflare

Cloudflare Dashboard → Pages → vibecoding-page → Deployments → [deployment] → Build log

## Checklisty

### Před commitem článku

- [ ] Soubor je v `_vibecoding/[kategorie]/YYYY-MM-DD-slug.md`
- [ ] Front matter obsahuje `layout: post`
- [ ] Front matter obsahuje `title:` a `post_excerpt:`
- [ ] Markdown je validní
- [ ] Lokální build projde bez chyb

### Při přidávání nové stránky do _pages

- [ ] Nepoužívá kolekce, které nejsou v `_config_vibecoding.yml`
- [ ] Nebo je přidána do `exclude:` pokud není pro vibecoding

### Po neúspěšném buildu

- [ ] Zkontrolovat Cloudflare build log
- [ ] Lokálně reprodukovat: `bundle exec jekyll build --config _config_vibecoding.yml`
- [ ] Hledat "Cannot sort a null object" nebo podobné chyby
- [ ] Přidat chybějící exclude položky

---

## Kontakt

- **Autor**: Patrick Zandl
- **Web**: https://www.vibecoding.cz
- **Repozitář**: https://github.com/tangero/marigold-page

---

*Tento dokument slouží jako reference pro práci s vibecoding.cz. Aktualizujte při významných změnách v architektuře.*
