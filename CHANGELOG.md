# Changelog

Všechny významné změny v projektu Marigold.cz jsou dokumentovány v tomto souboru.

Formát vychází z [Keep a Changelog](https://keepachangelog.com/cs/1.0.0/),
a projekt dodržuje [Semantic Versioning](https://semver.org/lang/cs/).

## [Unreleased]

### Added
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

### Fixed
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
