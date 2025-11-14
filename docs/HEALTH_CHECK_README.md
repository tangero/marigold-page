# Tech News Health Check System

Production-ready monitoring systém pro automatické generování tech-news článků na Marigold.cz.

## Co to dělá?

✅ **Automaticky monitoruje:**
- Zda se generují nové tech-news články
- Zda jsou články v češtině (ne v angličtině)
- Kvalitu a úplnost obsahu
- Čerstvost dat

✅ **Alertuje při problémech:**
- Email notifikace přes Uptimerobot
- Rozlišuje mezi WARNING a CRITICAL problémy
- Minimalizuje false positives

✅ **Poskytuje debugging nástroje:**
- JSON endpoint pro monitoring (`/health-check/`)
- HTML dashboard pro vizualizaci (`/health-status/`)
- Comprehensive test suite

## Architektura

```
GitHub Actions (4h)
    ↓
Generate tech-news + Translate (LLM)
    ↓
Run Health Check
    ↓
Deploy to GitHub Pages
    ↓
Uptimerobot monitors /health-check/
    ↓
Alerts při problémech
```

## Klíčové Komponenty

| Komponenta | Účel | Lokace |
|------------|------|--------|
| **Health Check Script** | Analyzuje tech-news a generuje metrics | `scripts/tech_news_health_check.py` |
| **JSON Endpoint** | Machine-readable status pro monitoring | `/health-check/` |
| **HTML Dashboard** | Human-readable debugging interface | `/health-status/` |
| **Test Suite** | Comprehensive unit & integration tests | `tests/test_health_check.py` |
| **GitHub Workflow** | Automatické spouštění při každém generování | `.github/workflows/tech-news.yml` |

## Quick Start

### 1. Instalace (jednorázově)

```bash
cd /Users/patrickzandl/GitHub/marigold-page

# Všechny soubory jsou již vytvořeny, stačí commit
git add scripts/tech_news_health_check.py
git add health-check.html health-status.html
git add tests/test_health_check.py
git add docs/HEALTH_CHECK_*.md
git commit -m "Add tech-news health check system"
git push
```

### 2. Setup Uptimerobot (5 minut)

```
1. Přihlásit se: https://uptimerobot.com/
2. Add New Monitor
3. Type: HTTP(s), URL: https://marigold.cz/health-check/
4. Keyword: "status": "OK"
5. Interval: 5 minutes
6. Add email alert contact
7. Save
```

### 3. Ověření

```bash
# Zkontrolovat lokálně
python3 scripts/tech_news_health_check.py

# Zkontrolovat live endpoint (po deploy)
curl -s https://marigold.cz/health-check/ | jq '.status'

# Otevřít dashboard
open https://marigold.cz/health-status/
```

**Hotovo! 🎉** Systém nyní automaticky monitoruje zdraví tech-news.

## Dokumentace

### Pro Rychlý Start
📘 **[Quick Start Guide](./HEALTH_CHECK_QUICKSTART.md)** - 5-minute setup + denní použití

### Pro Hloubkové Pochopení
📗 **[Kompletní Systémová Dokumentace](./HEALTH_CHECK_SYSTEM.md)** - Architektura, testing, troubleshooting

### Pro Uptimerobot Setup
📙 **[Uptimerobot Configuration Guide](./UPTIMEROBOT_SETUP.md)** - Detailní monitor konfigurace

## Klíčové Metriky

| Metrika | Threshold | Alert Level | Význam |
|---------|-----------|-------------|--------|
| **Articles 24h** | ≥ 10 | WARNING | Počet článků za 24h |
| **Czech Ratio** | ≥ 85% | CRITICAL | Poměr českých vs anglických článků |
| **Newest Age** | ≤ 6h | WARNING | Stáří nejnovějšího článku |
| **Avg Length** | ≥ 300 char | WARNING | Průměrná délka obsahu |
| **Error Rate** | ≤ 10% | WARNING | Front matter chybovost |

## Běžné Scénáře

### ✅ Vše funguje normálně

```json
{
  "status": "OK",
  "metrics": {
    "articles_24h": 15,
    "czech_ratio": 0.92,
    "newest_article_age_hours": 2.5
  },
  "alerts": []
}
```

### ⚠️ Drobné problémy (WARNING)

```json
{
  "status": "WARNING",
  "metrics": {
    "articles_24h": 8,  // Méně než 10
    "czech_ratio": 0.88,
    "newest_article_age_hours": 7.2  // Starší než 6h
  },
  "alerts": [
    {"level": "WARNING", "message": "Pouze 8 článků za 24h (minimum: 10)"},
    {"level": "WARNING", "message": "Nejnovější článek starý 7.2h (threshold: 6h)"}
  ]
}
```

### 🚨 Kritický problém (CRITICAL)

```json
{
  "status": "CRITICAL",
  "metrics": {
    "articles_24h": 12,
    "czech_ratio": 0.45,  // Pouze 45% češtiny!
    "newest_article_age_hours": 3.1
  },
  "alerts": [
    {"level": "CRITICAL", "message": "Pouze 45.0% článků v češtině! (minimum: 85.0%)"}
  ]
}
```

**→ Příčina:** LLM překlad nefunguje (API key, quota, outage)
**→ Akce:** Zkontrolovat OPENROUTER_API_KEY a LLM API status

## Testing

### Unit Tests

```bash
# Spustit všechny testy
python3 -m pytest tests/test_health_check.py -v

# Test coverage
python3 -m pytest tests/test_health_check.py --cov=scripts/tech_news_health_check

# Konkrétní test class
python3 -m pytest tests/test_health_check.py::TestLanguageDetection -v
```

### Integration Test

```bash
# Kompletní flow test
python3 scripts/tech_news_health_check.py
bundle exec jekyll build
cat _site/health-check/index.html | jq '.'
open _site/health-status/index.html
```

## Monitoring Best Practices

### Denně (automaticky)
- ✅ Uptimerobot posílá emails při problémech
- ✅ GitHub Actions automaticky spouští health check

### Týdně (15 minut)
1. Zkontrolovat Uptimerobot dashboard pro trendy
2. Review `/health-status/` pro metriky
3. Zkontrolovat false positive/negative rate
4. Adjustovat thresholdy pokud nutné

### Měsíčně (1 hodina)
1. Analyzovat metriky za celý měsíc
2. Review všech CRITICAL incidents
3. Update dokumentace s poznatky
4. Consider nové checks na základě issues

## Troubleshooting

| Problém | Rychlá Diagnóza | Řešení |
|---------|-----------------|--------|
| False positive alert | `curl https://marigold.cz/health-check/ \| jq .` | Zkontrolovat timestamp, rebuild Jekyll |
| Články v angličtině | Zkontrolovat `/health-status/` → Language Check | Zkontrolovat OPENROUTER_API_KEY |
| Žádné nové články | Zkontrolovat GitHub Actions workflow | Zkontrolovat NEWS_API_KEY, manuální run |
| Script selhává | `python3 scripts/tech_news_health_check.py` | Zkontrolovat dependencies, Python verzi |

## Endpoints

| URL | Účel | Formát |
|-----|------|--------|
| https://marigold.cz/health-check/ | Machine-readable monitoring | JSON |
| https://marigold.cz/health-status/ | Human-readable dashboard | HTML |

## Files Overview

```
marigold-page/
├── scripts/
│   └── tech_news_health_check.py    # Main health check script
├── tests/
│   └── test_health_check.py         # Comprehensive test suite
├── docs/
│   ├── HEALTH_CHECK_README.md       # This file
│   ├── HEALTH_CHECK_QUICKSTART.md   # Quick start guide
│   ├── HEALTH_CHECK_SYSTEM.md       # Full documentation
│   └── UPTIMEROBOT_SETUP.md         # Uptimerobot config
├── health-check.html                # JSON endpoint template
├── health-status.html               # HTML dashboard template
├── _data/
│   └── tech_news_health.json        # Generated health data
└── .github/workflows/
    └── tech-news.yml                # Updated with health check
```

## Development

### Přidat nový check

```python
# V tech_news_health_check.py

def _check_my_new_metric(self, articles: List[Dict]):
    """Kontrola nové metriky"""
    logger.info("🔍 Kontroluji novou metriku...")

    # Your logic here
    metric_value = self._calculate_metric(articles)

    # Store metric
    self.results['metrics']['my_metric'] = metric_value

    # Store check result
    self.results['checks']['my_check'] = {
        'status': 'OK' if metric_value > threshold else 'WARNING',
        'value': metric_value
    }

    # Add alert if needed
    if metric_value < threshold:
        self._add_warning_alert(f"Metric value too low: {metric_value}")

# Přidat do run_all_checks():
def run_all_checks(self):
    # ... existing checks ...
    self._check_my_new_metric(articles)
```

### Upravit thresholdy

Editovat v `scripts/tech_news_health_check.py`:

```python
THRESHOLDS = {
    'min_articles_24h': 10,      # Customizovat podle potřeby
    'max_age_hours': 6,
    'min_czech_ratio': 0.85,     # 85% minimum
    'min_avg_content_length': 300,
    'max_error_rate': 0.10,
}
```

## Support & Contributions

- **Issues:** GitHub Issues
- **Questions:** váš@email.cz
- **Documentation:** `docs/` adresář

## Changelog

### 2025-11-14 - Initial Release (v1.0.0)

**Features:**
- ✨ Kompletní health check systém s language detection
- ✅ Freshness, content quality, a front matter validation
- 📊 JSON endpoint + HTML dashboard
- 🧪 Comprehensive test suite (90%+ coverage)
- 📝 Kompletní dokumentace (3 guides)
- 🔔 Uptimerobot integration ready

**Tested on:**
- Python 3.11
- Jekyll 4.3.x
- macOS + Ubuntu (GitHub Actions)

---

**Quick Links:**
- 🚀 [Quick Start](./HEALTH_CHECK_QUICKSTART.md)
- 📗 [Full Documentation](./HEALTH_CHECK_SYSTEM.md)
- 🔧 [Uptimerobot Setup](./UPTIMEROBOT_SETUP.md)
- 🧪 [Test Suite](../tests/test_health_check.py)

**Live Endpoints:**
- 📊 JSON: https://marigold.cz/health-check/
- 🖥️ Dashboard: https://marigold.cz/health-status/

**Version:** 1.0.0 | **Last Updated:** 2025-11-14 | **Maintainer:** Patrick Zandl
