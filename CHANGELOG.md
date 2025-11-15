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

### Fixed
- Permalinky v `_layouts/tech_news_day.html` - články nyní vedou na interní stránky `/tech-news/YYYY-MM-DD/slug/` místo externích URL
- Permalinky v `_pages/tech-news-archiv.html` - odkazy vedou na interní stránky článků
- LLM model aktualizován z `openrouter/polaris-alpha` na `qwen/qwen3-max` ve všech tech-news skriptech:
  - `scripts/generate_tech_news_newsapi.py` (5 míst)
  - `scripts/generate_tech_news_with_images.py` (4 místa)
  - `scripts/fetch_tech_news_batch.py` (1 místo)
  - `scripts/fetch_tech_news.py` (1 místo)

### Changed
- GitHub Actions workflow `.github/workflows/tech-news.yml` - health check je nyní non-blocking (`|| true`)
- Health check přidán jako automatický krok do tech-news workflow

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
