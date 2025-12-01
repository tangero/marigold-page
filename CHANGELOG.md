# Changelog

Všechny významné změny v projektu Marigold.cz jsou dokumentovány v tomto souboru.

Formát vychází z [Keep a Changelog](https://keepachangelog.com/cs/1.0.0/),
a projekt dodržuje [Semantic Versioning](https://semver.org/lang/cs/).

## [Unreleased]

### Changed
- **LLM model pro tech-news změněn z `qwen/qwen3-max` na `x-ai/grok-4.1-fast:free`** (`scripts/generate_tech_news_newsapi.py`)
  - Nový primární model: `x-ai/grok-4.1-fast:free` (bezplatný)
  - Automatický fallback na `anthropic/claude-haiku-4.5` při selhání (HTTP 402, 429, 503)
  - Nová helper metoda `_call_llm_with_fallback()` s retry logikou
  - Logging aktuálně použitého modelu na konci běhu
  - Konfigurace modelů centralizována do class konstant `PRIMARY_MODEL` a `FALLBACK_MODEL`

### Added
- **Seznam.cz Discussion System** - nativní diskuzní systém místo commentbox.io
  - Nahrazen commentbox.io systém za Seznam.cz diskuze (service-name: `marigoldcz`)
  - Přidány include soubory: `szn-discussion.html`, `szn-discussion-meta.html`, `szn-discussion-jsonld.html`
  - Meta tag `szn:permalink` pro propojení s Homepage Seznamu
  - JSON-LD strukturovaná data s `discussionUrl` pro SEO
  - Diskuze aktivní v layoutech: `post.html` a `tech_news_article.html`
  - Obrazy kolekce nadále bez diskuzí (stejně jako předtím)
- **Diagnostic Dashboard** (`scripts/tech_news_diagnostic_dashboard.py`) - komplexní monitoring tech-news pipeline
  - Rejection analysis s breakdown důvodů zamítnutí (content_filter vs low_importance)
  - Sample zamítnutých článků s jejich skóre a důvody
  - LLM cost metriky (daily/weekly breakdown podle operací)
  - Freshness check s alerts pro staré články
  - Success rate trend za 7 dní s grafem
  - Importance distribution pro analýzu kvality
  - Automated recommendations na základě detekovaných problémů
  - JSON output do `_data/tech_news_diagnostic.json`
- Archivní stránka `/tech-news/archiv/` s přehledem článků po měsících a dnech
- Zdravotní monitoring systém pro tech-news (`scripts/tech_news_health_check.py`)
- JSON endpoint `/health-check/` pro Uptimerobot monitoring
- HTML dashboard `/health-status/` pro debugging
- Komplexní test suite pro health check systém (`tests/test_health_check.py`)
- Rozsáhlá dokumentace pro health check systém (5 guidů v `docs/`)
- Kompletní CLAUDE.md dokumentace s pokyny pro _posts vs _tech_news
- Povinnost aktualizovat CHANGELOG.md po každém commitu
- Archiv odkaz v headeru `/tech-news/` stránky - viditelný hned při načtení
- HTML verze CHANGELOGu dostupná na `/changelog/` s odkazem v patičce webu
- Sekce "Tech News" na titulní stránce - zobrazuje striktně 5 nejnovějších článků s vysokou důležitostí (importance >= 4)
  - Použití dvoustupňového filtru: `slice: 0, 5` + `limit: 5` v for loop pro garantovaný limit
- **Kompletní monitoring a logging systém pro tech-news pipeline:**
  - `ProcessingLogger` třída (`scripts/processing_logger.py`) - sleduje celý processing pipeline
  - SQLite databáze (`_data/tech_news_metrics.db`) - ukládá processing sessions, hourly a daily metriky
  - JSON Lines logy (`_data/processing_logs/*.jsonl`) - append-only logy pro každý den
  - Dashboard data generátor (`scripts/generate_dashboard_data.py`) - agreguje 30denní statistiky
  - Rozšířený `/health-status/` dashboard s grafy, pipeline funnelem a performance metrikami
  - Sledování: API fetch → LLM processing → Save pipeline s důvody přeskočení článků
  - Metriky: počty článků, LLM náklady, tokeny, časy zpracování, error rate, skip reasons

### Fixed
- **Seznam Diskuze API errors (401/404)** - oprava canonical string formátu
  - Problém: widget používal relativní cestu místo plné URL v canonical stringu
  - Způsobovalo chyby "Api Error" při pokusu o odeslání komentáře
  - Řešení: změna z `{{ page.url }}` na `{{ site.url }}{{ page.url }}` v `szn-discussion.html` a `szn-discussion-meta.html`
  - Canonical string nyní: `https://www.marigold.cz/item/...` místo `/item/...`
- **NewsAPI freshness** - přechod z `/v2/top-headlines` na `/v2/everything` endpoint
  - Problém: top-headlines vracel články staré 48-72h, žádné dnešní články
  - Řešení: `/v2/everything` s `from` parametrem pro poslední 48h a `sortBy: publishedAt`
  - Zvýšen `pageSize` z 40 → 100 článků pro větší výběr
  - Přidána freshness validace s logging stáří článků
  - Očekávaný dopad: Article age 48-72h → <24h (67% rychlejší)
- **LLM cost tracking** - přidán debug logging a fallback approximation
  - Problém: `llm_costs.db` měla 0 záznamů, nebyla viditelnost LLM nákladů
  - Přidán debug logging pro detekci chybějících `usage` dat z OpenRouter API
  - Fallback aproximace tokenů pomocí heuristiky (~4 znaky = 1 token)
  - Enhanced logging - vždy logovat API calls i když chybí přesná cost data
  - Warning v logu pokud OpenRouter response nemá `usage` klíč
- Permalinky v `_layouts/tech_news_day.html` - články nyní vedou na interní stránky `/tech-news/YYYY-MM-DD/slug/` místo externích URL
- Permalinky v `_pages/tech-news-archiv.html` - odkazy vedou na interní stránky článků
- LLM model aktualizován z `openrouter/polaris-alpha` na `qwen/qwen3-max` ve všech tech-news skriptech:
  - `scripts/generate_tech_news_newsapi.py` (5 míst)
  - `scripts/generate_tech_news_with_images.py` (4 místa)
  - `scripts/fetch_tech_news_batch.py` (1 místo)
  - `scripts/fetch_tech_news.py` (1 místo)
- URL v tech-news manifestu - odstraněn trailing dash ze slugu (`scripts/generate_tech_news_manifest.py`)
  - Před: `/tech-news/2025-11-12/review-new-framework-laptop-16-takes-a-fresh-stab-/` (404)
  - Po: `/tech-news/2025-11-12/review-new-framework-laptop-16-takes-a-fresh-stab/` (200)
- Trailing dash v URL na titulní stránce (Tech News sekce) - odstranění trailing dashe ze slugu v `index.html`

### Changed
- **Filtering thresholds** - rozšířený tech whitelist v content filteru
  - Problém: 76.5% článků filtrováno jako hry/sport (příliš agresivní)
  - Rozšířen whitelist tech indicators z 9 → 34 položek
  - Nové kategorie: AI/ML v gamingu, Cloud gaming tech, Hardware/GPU, VR/AR technology
  - Gaming platforms (Steam Deck, ROG Ally), Game engines (Unreal 5), Performance optimization
  - Tech-relevant gaming články nyní ponechány místo zamítnutí
  - Očekávaný dopad: Snížení false positive rejections z 76% → ~40%
- **Přepracován systém hodnocení důležitosti článků (importance 1-5)** v `scripts/generate_tech_news_newsapi.py`:
  - **LLM prompt** - rozšířena kritéria s jasným zaměřením na AI, robotiku, Apple, Tesla, Elon Musk, Sam Altman (importance 4-5)
  - **Nízká priorita** (2) pro čínské telefony (OnePlus, Xiaomi, Huawei), rutinní Android/Windows updaty, spekulace
  - **Fallback funkce** `detect_importance()` - přidáno keyword-based hodnocení s 80+ klíčovými slovy
  - Cíl: lepší využití celé škály 1-5 (dříve 85% článků mělo importance 3-4)
- GitHub Actions workflow `.github/workflows/tech-news.yml` - health check je nyní non-blocking (`|| true`)
- Health check přidán jako automatický krok do tech-news workflow
- UI/UX redesign úvodní stránky `/tech-news/` - kompaktnější layout, archiv v headeru
  - Odstraněn redundantní "18 nejnovějších článků" box (úspora ~120px)
  - Zkrácený popis s přímým odkazem na archiv
  - Zjednodušené filtry (odstranění filtru "Kritická" importance)
  - Kompaktní badge s počtem článků místo celého navigation boxu
- Tech News sekce na titulní stránce - zmenšeny mezery mezi články (10px → 6px)

---

## [1.0.0] - 2025-08-25

### Added
- Základní Jekyll struktura projektu
- Kolekce: `_posts`, `_tech_news`, `_ai`, `_mobilnisite`, `_obrazy`
- Tech-news automatizace přes NewsAPI
- LLM cost tracking systém
- GitHub Actions CI/CD

### Changed
- Initial release

---

## Semantic Versioning Guide

Formát: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes, zásadní přepisy
- **MINOR**: Nové funkce, zpětně kompatibilní
- **PATCH**: Bugfixy, drobné změny

### Příklad

```
2.1.3
│ │ │
│ │ └─> PATCH - Oprava permalinků
│ └───> MINOR - Nový health check systém
└─────> MAJOR - Přechod na nový framework
```

---

**Aktualizováno**: 2025-11-15
