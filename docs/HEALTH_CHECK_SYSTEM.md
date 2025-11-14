# Tech News Health Check System - Kompletní Dokumentace

## Přehled

Robustní health monitoring systém pro automatické generování tech-news článků na Marigold.cz. Systém detekuje problémy s generováním, překladem a kvalitou obsahu a poskytuje real-time monitoring přes Uptimerobot.

## Architektura

### High-Level Overview

```
┌─────────────────────────────────────────────────────────────┐
│  GitHub Actions (každé 4h)                                  │
│  ├─ Fetch tech news (NewsAPI)                               │
│  ├─ Translate to Czech (LLM)                                │
│  ├─ Generate articles → _tech_news/*.md                     │
│  ├─ Run health check → _data/tech_news_health.json          │
│  └─ Jekyll build + deploy                                   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Live Website (GitHub Pages)                                │
│  ├─ /health-check/        (JSON endpoint)                   │
│  └─ /health-status/       (HTML dashboard)                  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Uptimerobot (External Monitor)                             │
│  ├─ Primary Health Check (keyword: "status": "OK")          │
│  ├─ Language Check (czech_ratio monitoring)                 │
│  ├─ Freshness Check (article age monitoring)                │
│  └─ Alerts → Email / Slack / Webhook                        │
└─────────────────────────────────────────────────────────────┘
```

### Datový tok

```
_tech_news/*.md
    ↓
[Health Check Script]
    ↓
_data/tech_news_health.json
    ↓
[Jekyll Build]
    ↓
/health-check/ (JSON)
/health-status/ (HTML)
    ↓
[Uptimerobot Polling]
    ↓
[Alerts při problému]
```

## Komponenty Systému

### 1. Health Check Script (`scripts/tech_news_health_check.py`)

**Funkce:**
- Analyzuje všechny články v `_tech_news/`
- Detekuje jazyk (čeština vs angličtina)
- Kontroluje čerstvost obsahu
- Validuje front matter
- Vypočítává kvalitativní metriky
- Generuje JSON report s výsledky

**Klíčové kontroly:**

| Check | Co kontroluje | Threshold | Alert Level |
|-------|---------------|-----------|-------------|
| **Freshness** | Stáří nejnovějšího článku | Max 6h | WARNING |
| **Article Count** | Počet článků za 24h | Min 10 | WARNING |
| **Language Ratio** | Poměr českých článků | Min 85% | CRITICAL |
| **Content Length** | Průměrná délka obsahu | Min 300 znaků | WARNING |
| **Front Matter** | Validita YAML metadat | Max 10% error rate | WARNING |

**Použití:**

```bash
# Základní spuštění
python scripts/tech_news_health_check.py

# S vlastním výstupním souborem
python scripts/tech_news_health_check.py --output _data/health.json

# S vlastním adresářem tech-news
python scripts/tech_news_health_check.py --tech-news-dir /path/to/articles

# Exit codes:
#   0 = OK (všechny checks prošly)
#   1 = WARNING (některé checks mají varování)
#   2 = CRITICAL (kritický problém detekován)
```

### 2. JSON Health Endpoint (`/health-check/`)

**Účel:** Machine-readable endpoint pro Uptimerobot a API monitoring

**Formát výstupu:**

```json
{
  "status": "OK",
  "timestamp": "2025-11-14T13:30:00+00:00",
  "summary": "Status: OK | Články 24h: 15 | Čeština: 92.3%",
  "metrics": {
    "total_articles": 3041,
    "articles_24h": 15,
    "articles_1h": 2,
    "newest_article_age_hours": 2.5,
    "czech_ratio": 0.923,
    "avg_content_length": 856,
    "median_content_length": 742,
    "articles_with_images_pct": 95.2,
    "articles_with_category_pct": 98.7,
    "front_matter_error_rate": 0.03
  },
  "checks": {
    "freshness": {
      "status": "OK",
      "newest_age_hours": 2.5,
      "articles_24h": 15,
      "articles_1h": 2
    },
    "language": {
      "status": "OK",
      "czech_ratio": 0.923,
      "sample_size": 100,
      "english_articles_sample": []
    },
    "content_quality": {
      "status": "OK",
      "avg_length": 856,
      "median_length": 742
    },
    "front_matter": {
      "status": "OK",
      "error_rate": 0.03,
      "invalid_count": 3
    }
  },
  "alerts": [
    {
      "level": "INFO",
      "message": "Pouze 2 článků za poslední hodinu"
    }
  ]
}
```

**Status hodnoty:**
- `OK` - Vše funguje správně
- `WARNING` - Drobné problémy, není nutná okamžitá akce
- `CRITICAL` - Vážný problém vyžadující pozornost

### 3. HTML Status Dashboard (`/health-status/`)

**Účel:** Human-readable dashboard pro debugging a monitoring

**Funkce:**
- Vizualizace všech metrik s barevným kódováním
- Detail jednotlivých checks
- Seznam aktivních alertů
- Ukázka problémových článků
- Raw JSON data pro debugging

**Přístup:** https://marigold.cz/health-status/

### 4. Uptimerobot Monitoring

Kompletní setup instrukce: viz `docs/UPTIMEROBOT_SETUP.md`

**Základní konfigurace:**

```yaml
Primary Monitor:
  Name: Marigold Tech News - Health Check
  Type: HTTP(s) - Keyword
  URL: https://marigold.cz/health-check/
  Interval: 5 minutes
  Keyword: '"status": "OK"'
  Alert: 2 consecutive failures (10 min)

Language Monitor:
  Name: Marigold Tech News - Czech Language
  Type: HTTP(s) - Keyword
  URL: https://marigold.cz/health-check/
  Interval: 5 minutes
  Keyword NOT: '"status": "CRITICAL"'
  Alert: Immediate

Freshness Monitor:
  Name: Marigold Tech News - Freshness
  Type: HTTP(s) - Keyword
  URL: https://marigold.cz/health-check/
  Interval: 15 minutes
  Keyword: '"articles_24h":'
  Alert: 2 consecutive failures
```

## Detekce Jazykových Problémů

### Jak funguje Language Detection

Systém používá **dual-score approach** pro maximální přesnost:

1. **Czech Character Score (30% váha)**
   - Detekuje české znaky: áčďéěíňóřšťúůýž
   - Skóre: počet českých znaků / 10 (max 1.0)

2. **Czech Word Score (70% váha)**
   - Detekuje česká klíčová slova z předem definované sady
   - Slova jako: který, společnost, podle, během, pouze, atd.
   - Skóre: počet českých slov / 5 (max 1.0)

3. **Kombinované skóre**
   ```python
   final_score = (char_score * 0.3) + (word_score * 0.7)
   # 0.0 = angličtina
   # 0.5 = neutrální / nelze rozhodnout
   # 1.0 = čeština
   ```

4. **Classification threshold**
   - score > 0.5 → čeština
   - score ≤ 0.5 → angličtina

### Testované scénáře

| Text | Detekce | Skóre |
|------|---------|-------|
| "Společnost Google představila novou funkci" | ✅ Čeština | 0.85+ |
| "Google announces new feature" | ✅ Angličtina | 0.15- |
| "Google představuje new feature" | ⚠️ Smíšený | 0.4-0.6 |
| "123 456 789" | ✅ Angličtina | 0.0 |

### Failure Scénáře

**Scénář 1: LLM API nedostupné**
```
Symptom: Články zůstanou v angličtině
Detekce: czech_ratio < 0.85
Alert: CRITICAL
Response:
  1. Zkontrolovat OPENROUTER_API_KEY
  2. Zkontrolovat LLM API status
  3. Zkontrolovat error logy v GitHub Actions
```

**Scénář 2: Částečné selhání překladu**
```
Symptom: Některé články v angličtině, některé v češtině
Detekce: 0.70 < czech_ratio < 0.85
Alert: WARNING
Response:
  1. Zkontrolovat LLM cost limits
  2. Zkontrolovat rate limiting
  3. Review sample anglických článků v /health-status/
```

**Scénář 3: Translation quality degradation**
```
Symptom: Přeloženo, ale špatná kvalita
Detekce: czech_ratio OK, ale avg_content_length nízká
Alert: WARNING (content_quality)
Response:
  1. Zkontrolovat LLM model parametry
  2. Review prompt template
  3. Zkontrolovat input data quality
```

## Failure Detection & Alerting

### Detection Matrix

| Problém | Detekce | Threshold | Alert Level | Response Time |
|---------|---------|-----------|-------------|---------------|
| Generování selhalo | articles_24h < 10 | < 10 | WARNING | 24h |
| Překlad nefunguje | czech_ratio < 0.85 | < 85% | CRITICAL | Immediate |
| Stará data | newest_age > 6h | > 6h | WARNING | 12h |
| Front matter error | error_rate > 0.10 | > 10% | WARNING | 24h |
| Krátký obsah | avg_length < 300 | < 300 char | WARNING | 24h |

### Alert Flow

```
Problem Detected
    ↓
Health Check creates alert
    ↓
Jekyll build includes alert in JSON
    ↓
Uptimerobot detects status change
    ↓
Uptimerobot sends notification
    ↓
Email / Slack / Webhook
    ↓
Manual investigation via /health-status/
```

### Threshold Tuning Strategy

**Phase 1: Observation (první 2 týdny)**
- Nastavit benevolentní thresholdy
- Sledovat metriky bez alertů
- Identifikovat normální rozsah hodnot

**Phase 2: Calibration (týden 3-4)**
- Analyzovat nasbíraná data
- Adjustovat thresholdy na P95 hodnoty
- Test alert flow

**Phase 3: Production (ongoing)**
- Monitor false positive/negative rate
- Monthly review a adjustace
- Document všechny změny

## Testing Strategy

### Unit Tests

```bash
# Spustit všechny testy
cd /Users/patrickzandl/GitHub/marigold-page
python -m pytest tests/test_health_check.py -v

# Spustit konkrétní test class
python -m pytest tests/test_health_check.py::TestLanguageDetection -v

# Test coverage
python -m pytest tests/test_health_check.py --cov=scripts/tech_news_health_check
```

**Test Coverage:**
- ✅ Language detection (czech, english, mixed, edge cases)
- ✅ Article parsing (valid, invalid YAML, missing front matter)
- ✅ Date parsing (multiple formats)
- ✅ Freshness checks (OK, WARNING scenarios)
- ✅ Language quality checks (all czech, too much english)
- ✅ Content quality metrics
- ✅ Front matter validation
- ✅ Overall status calculation
- ✅ Alert generation
- ✅ JSON output
- ✅ Edge cases (empty dir, nonexistent path, large content)

### Integration Tests

**Manual Test Procedure:**

```bash
# 1. Lokální health check
python scripts/tech_news_health_check.py --output _data/tech_news_health.json

# 2. Zkontrolovat výstup
cat _data/tech_news_health.json | jq .

# 3. Build Jekyll
bundle exec jekyll build

# 4. Test JSON endpoint
cat _site/health-check/index.html | jq .

# 5. Test HTML dashboard (otevřít v browseru)
open _site/health-status/index.html

# 6. Simulate failure (dočasně změnit threshold)
# Editovat tech_news_health_check.py:
#   'min_czech_ratio': 1.0  # Nerealisticky vysoký
# Re-run a ověřit CRITICAL status
```

### Failure Simulation Tests

**Test 1: LLM Translation Failure**

```bash
# Dočasně disable OPENROUTER_API_KEY v workflow
# nebo nastavit na invalid value
# → Očekávání: CRITICAL alert, czech_ratio < 0.85
```

**Test 2: NewsAPI Failure**

```bash
# Dočasně disable NEWS_API_KEY
# → Očekávání: CRITICAL alert, articles_24h = 0
```

**Test 3: Stale Content**

```bash
# Dočasně disable GitHub Actions schedule
# Počkat 7+ hodin
# → Očekávání: WARNING alert, newest_age_hours > 6
```

## Monitoring Best Practices

### Daily Checks (Automated)

- ✅ Uptimerobot emails pro CRITICAL alerts
- ✅ Auto-generated health data při každém build
- ✅ GitHub Actions workflow status notifications

### Weekly Review (Manual - 15 min)

```bash
# 1. Zkontrolovat Uptimerobot dashboard
# https://uptimerobot.com/dashboard

# 2. Review /health-status/ trendy
# https://marigold.cz/health-status/

# 3. Zkontrolovat GitHub Actions success rate
gh run list --workflow=tech-news.yml --limit 50 | grep -c "completed.*success"

# 4. Review alert history
# Zkontrolovat email inbox pro uptimerobot alerts

# 5. Check LLM costs (optional)
python scripts/generate_llm_cost_report.py --summary-only
```

### Monthly Deep Dive (Manual - 1 hour)

1. **Metrics Analysis**
   - Download month's health data
   - Plot czech_ratio, articles_24h, avg_content_length trends
   - Identify anomalies or degradation patterns

2. **Threshold Review**
   - Analyze false positive/negative rate
   - Adjust thresholds if needed
   - Document changes in changelog

3. **Test Coverage**
   - Run full test suite
   - Add new tests for discovered edge cases
   - Update documentation

4. **Incident Post-Mortems**
   - Review všechny CRITICAL incidents
   - Root cause analysis
   - Preventive measures

## Troubleshooting Guide

### Problem: False Positive - Alert ale vše funguje

**Debug kroky:**

```bash
# 1. Zkontrolovat live JSON
curl -s https://marigold.cz/health-check/ | jq .

# 2. Zkontrolovat lokální health data
cat _data/tech_news_health.json | jq .

# 3. Porovnat timestamp
# Pokud se liší → Jekyll build selhal nebo není deployed

# 4. Zkontrolovat poslední GitHub Actions run
gh run view --workflow=tech-news.yml

# 5. Zkontrolovat deployment status
gh workflow view pages-build-deployment
```

**Possible causes:**
- Uptimerobot cache (rare)
- Jekyll build failure → starý JSON deployed
- Threshold příliš přísný
- Network glitch (transient)

### Problem: False Negative - Žádný alert ale problém existuje

**Debug kroky:**

```bash
# 1. Zkontrolovat /health-status/ vizuálně
open https://marigold.cz/health-status/

# 2. Zkontrolovat alerts array v JSON
curl -s https://marigold.cz/health-check/ | jq '.alerts'

# 3. Zkontrolovat uptimerobot keyword configuration
# Je keyword matching správně nastavený?

# 4. Manual threshold test
python scripts/tech_news_health_check.py
# Zkontrolovat console output pro expected alerts
```

**Possible causes:**
- Uptimerobot keyword příliš benevolentní
- Threshold příliš tolerantní
- Uptimerobot interval příliš dlouhý
- Alert contact not configured

### Problem: Články v angličtině ale žádný alert

**Diagnóza:**

```bash
# 1. Zkontrolovat czech_ratio metric
curl -s https://marigold.cz/health-check/ | jq '.metrics.czech_ratio'

# 2. Zkontrolovat sample anglických článků
curl -s https://marigold.cz/health-check/ | jq '.checks.language.english_articles_sample'

# 3. Manual language detection test
python3 << EOF
import sys
sys.path.insert(0, 'scripts')
from tech_news_health_check import TechNewsHealthCheck

checker = TechNewsHealthCheck()
score = checker._detect_language("Your test article text here")
print(f"Language score: {score}")
print(f"Classification: {'Czech' if score > 0.5 else 'English'}")
EOF
```

**Možné příčiny:**
1. **Language detection false negative**
   - Text obsahuje některá česká slova → skóre > 0.5
   - Řešení: Adjustovat CZECH_WORDS slovník nebo thresholdy

2. **Threshold příliš nízký**
   - `min_czech_ratio` = 0.85 ale actual = 0.87 (většinou angličtina)
   - Řešení: Zvýšit threshold na 0.95

3. **Sample size příliš malý**
   - Kontroluje se max 100 článků, anglické jsou starší
   - Řešení: Zvýšit sample size nebo kontrolovat nejnovější pouze

### Problem: Health check script selhává

**Debug kroky:**

```bash
# 1. Spustit s verbose logging
python scripts/tech_news_health_check.py 2>&1 | tee health_check.log

# 2. Zkontrolovat Python dependencies
pip list | grep -E 'yaml|requests|beautifulsoup4|python-dateutil'

# 3. Zkontrolovat _tech_news directory permissions
ls -la _tech_news/ | head

# 4. Test s minimal dataset
mkdir /tmp/test_tech_news
cp _tech_news/2025-11-*.md /tmp/test_tech_news/
python scripts/tech_news_health_check.py --tech-news-dir /tmp/test_tech_news

# 5. Spustit unit tests
python -m pytest tests/test_health_check.py -v
```

## Maintenance & Updates

### When to Update Thresholds

**Indicators for threshold adjustments:**

1. **Too many false positives (> 2/week)**
   ```python
   # Loosen thresholds
   'min_articles_24h': 10 → 8
   'max_age_hours': 6 → 8
   'min_czech_ratio': 0.85 → 0.80
   ```

2. **False negatives (missed real issues)**
   ```python
   # Tighten thresholds
   'min_czech_ratio': 0.85 → 0.90
   'max_age_hours': 6 → 4
   ```

3. **Seasonal patterns (weekends, holidays)**
   ```python
   # Consider time-based thresholds
   if is_weekend():
       'min_articles_24h': 5
   else:
       'min_articles_24h': 10
   ```

### When to Add New Checks

**Indicators:**

1. **Recurring manual investigations**
   - Pokud opakovaně manuálně kontrolujete stejnou věc
   - → Automatizovat to jako nový check

2. **New failure mode discovered**
   - Incident post-mortem odhalil nový problém
   - → Přidat check který by to detekoval

3. **Quality regression**
   - Kvalita obsahu klesá ale existing checks to nedetekují
   - → Přidat nové quality metrics

**Example - přidání nového check:**

```python
# V tech_news_health_check.py

def _check_duplicate_articles(self, articles: List[Dict]):
    """Kontrola duplicitních článků"""
    logger.info("🔍 Kontroluji duplicity...")

    seen_urls = set()
    duplicates = []

    for article in articles:
        url = article['front_matter'].get('url')
        if url in seen_urls:
            duplicates.append(url)
        seen_urls.add(url)

    duplicate_rate = len(duplicates) / len(articles) if articles else 0

    self.results['metrics']['duplicate_rate'] = round(duplicate_rate, 3)
    self.results['checks']['duplicates'] = {
        'status': 'CRITICAL' if duplicate_rate > 0.05 else 'OK',
        'duplicate_count': len(duplicates),
        'duplicate_rate': round(duplicate_rate, 3)
    }

    if duplicate_rate > 0.05:
        self._add_critical_alert(
            f"Duplicitní články: {len(duplicates)} ({duplicate_rate*100:.1f}%)"
        )

# Přidat do run_all_checks():
def run_all_checks(self):
    # ... existing checks ...
    self._check_duplicate_articles(articles)
    # ...
```

### Version Control & Changelog

**Důležité změny dokumentovat v:**
- `docs/HEALTH_CHECK_SYSTEM.md` (tento soubor)
- Git commit messages
- GitHub releases/tags pro major updates

**Changelog format:**

```markdown
## 2025-11-14 - Initial Release
- ✨ Implementován základní health check systém
- ✅ Language detection (czech vs english)
- ✅ Freshness monitoring
- ✅ Content quality checks
- ✅ Front matter validation
- 📊 Uptimerobot integration

## 2025-11-XX - Update (example)
- 🔧 Adjusted min_czech_ratio threshold: 0.85 → 0.90
- ✨ Added duplicate article detection
- 🐛 Fixed date parsing for timezone edge cases
- 📝 Updated Uptimerobot setup documentation
```

## Odkazy a Reference

### Dokumentace
- **Tento soubor:** Kompletní systémová dokumentace
- **`docs/UPTIMEROBOT_SETUP.md`:** Detailní Uptimerobot konfigurace
- **`CLAUDE.md`:** Projekt-wide development guidelines

### Scripts
- **`scripts/tech_news_health_check.py`:** Main health check script
- **`tests/test_health_check.py`:** Comprehensive test suite

### Endpoints
- **JSON:** https://marigold.cz/health-check/
- **HTML:** https://marigold.cz/health-status/

### External Services
- **Uptimerobot:** https://uptimerobot.com/
- **GitHub Actions:** https://github.com/username/marigold-page/actions
- **OpenRouter (LLM):** https://openrouter.ai/

### Support
- **Issues:** GitHub Issues
- **Email:** váš@email.cz

---

**Last Updated:** 2025-11-14
**Version:** 1.0.0
**Maintainer:** Patrick Zandl
