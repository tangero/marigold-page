# Uptimerobot Health Check Setup Guide

Komplexní návod pro konfiguraci Uptimerobot monitoringu tech-news generování na Marigold.cz.

## Přehled Architektury

```
┌─────────────────────────────────────────┐
│  Uptimerobot Cloud Service              │
│  - Monitor 1: JSON Health Endpoint      │
│  - Monitor 2: HTML Status Page          │
│  - Monitor 3: Language Check (Keyword)  │
└────────────────┬────────────────────────┘
                 │ HTTP(S) Polling každých 5 min
                 ▼
┌─────────────────────────────────────────┐
│  https://marigold.cz/health-check/      │
│  - JSON endpoint s metrics              │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  _data/tech_news_health.json            │
│  - Generováno při každém build          │
│  - Obsahuje výsledky všech checks       │
└─────────────────────────────────────────┘
```

## Uptimerobot Monitor Konfigurace

### Monitor 1: Primary Health Check (HTTP/JSON)

**Účel:** Primární monitoring dostupnosti a základních metrik

**Konfigurace:**
- **Monitor Type:** HTTP(s)
- **Friendly Name:** `Marigold Tech News - Health Check`
- **URL:** `https://marigold.cz/health-check/`
- **Monitoring Interval:** 5 minutes
- **Monitor Timeout:** 30 seconds

**Keyword Monitoring:**
- **Type:** Keyword Exists
- **Keywords:** `"status": "OK"`
- **Description:** Kontroluje, že celkový status je OK

**Alert Contacts:**
- Email: váš@email.cz
- Threshold: Alert if down for 2 checks (10 minut)

**Advanced Settings:**
- HTTP Method: GET
- Custom HTTP Headers: None required
- Expected Status Code: 200

---

### Monitor 2: Czech Language Ratio Check (Keyword)

**Účel:** Detekce poklesu poměru českých článků (hlavní indikátor selhání překladu)

**Konfigurace:**
- **Monitor Type:** HTTP(s) - Keyword
- **Friendly Name:** `Marigold Tech News - Czech Language Check`
- **URL:** `https://marigold.cz/health-check/`
- **Monitoring Interval:** 5 minutes

**Keyword Monitoring:**
- **Type:** Keyword Exists
- **Primary Keyword:** `"czech_ratio": 0.`
- **Description:** Detekuje přítomnost czech_ratio pole

**Alert Threshold Logic:**

Pro detekci nízkého poměru češtiny použijte **Regex Monitoring** (pokud podporováno):
- **Regex Pattern:** `"czech_ratio":\s*0\.[0-8]`
- **Alert When:** Pattern matches (hodnota < 0.9)

**Alternative approach (bez regex):**
- Kombinovat s Monitor 1, který kontroluje `"status": "WARNING"` nebo `"status": "CRITICAL"`

---

### Monitor 3: Article Freshness Check

**Účel:** Detekce stagnace generování článků

**Konfigurace:**
- **Monitor Type:** HTTP(s) - Keyword
- **Friendly Name:** `Marigold Tech News - Freshness Check`
- **URL:** `https://marigold.cz/health-check/`
- **Monitoring Interval:** 15 minutes

**Keyword Monitoring:**
- **Type:** Keyword NOT Exists
- **Keyword:** `"newest_article_age_hours": 99`
- **Description:** Alert pokud je nejnovější článek starší než očekávané maximum

**Alert Logic:**
- Alert if keyword matches for 2 consecutive checks (30 minut)

---

### Monitor 4: Human-Readable Status Page (Optional)

**Účel:** Sekundární monitoring s vizuální kontrolou

**Konfigurace:**
- **Monitor Type:** HTTP(s)
- **Friendly Name:** `Marigold Tech News - Status Page`
- **URL:** `https://marigold.cz/health-status/`
- **Monitoring Interval:** 10 minutes

**Keyword Monitoring:**
- **Type:** Keyword Exists
- **Keyword:** `Status: <strong>OK</strong>`
- **Description:** Kontrola že status page zobrazuje OK

---

## Alert Contact Konfigurace

### Email Alert

**Doporučené nastavení:**
- **Alert When:**
  - Monitor goes DOWN
  - Monitor goes UP (recovery notification)
- **Threshold:** 2 consecutive failures (10 minut pro 5min interval)
- **Email Template:**

```
Monitor: {{monitorFriendlyName}}
Status: {{monitorAlertType}}
URL: {{monitorURL}}
Reason: {{alertDetails}}
Time: {{alertDateTime}}

Check status: https://marigold.cz/health-status/
```

### Webhook Alert (Optional - pro Slack/Discord)

**Pro integraci se Slackem:**

```json
{
  "text": "🚨 Tech News Health Alert",
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*{{monitorFriendlyName}}*\nStatus: `{{monitorAlertType}}`"
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "*URL:*\n{{monitorURL}}"
        },
        {
          "type": "mrkdwn",
          "text": "*Time:*\n{{alertDateTime}}"
        }
      ]
    },
    {
      "type": "actions",
      "elements": [
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "View Status"
          },
          "url": "https://marigold.cz/health-status/"
        }
      ]
    }
  ]
}
```

---

## Testování Konfigurace

### Manuální Test Před Deploy

```bash
# 1. Spustit health check lokálně
cd /path/to/marigold-page
python scripts/tech_news_health_check.py --output _data/tech_news_health.json

# 2. Build Jekyll s novými daty
bundle exec jekyll build

# 3. Zkontrolovat vygenerovaný JSON
cat _site/health-check/index.html

# 4. Zkontrolovat HTML status stránku
open _site/health-status/index.html
```

### Simulace Failure Scénářů

**Scénář 1: Nízký poměr češtiny (LLM selhání)**

Dočasně upravit threshold v `tech_news_health_check.py`:

```python
THRESHOLDS = {
    'min_czech_ratio': 1.0,  # Nerealisticky vysoký threshold
}
```

Spustit check a ověřit, že vytvoří CRITICAL alert.

**Scénář 2: Starý obsah (generování stagnuje)**

```python
THRESHOLDS = {
    'max_age_hours': 0.1,  # Velmi krátký čas
}
```

**Scénář 3: Nedostatek článků**

Dočasně přesunout soubory z `_tech_news/` a spustit check.

---

## Uptimerobot Dashboard Setup

### Public Status Page (Doporučeno)

**Účel:** Transparentní zobrazení uptime pro uživatele

**Konfigurace:**
1. V Uptimerobot dashboardu: `Public Status Pages` → `Add New`
2. **Custom Domain:** `status.marigold.cz` (pokud chcete vlastní doménu)
3. **Monitored Services:** Vybrat všechny Tech News monitors
4. **Design:**
   - Logo: Marigold.cz logo
   - Theme: Light nebo Dark
   - Show uptime percentages: YES

---

## Threshold Tuning Guide

### Doporučené Thresholdy pro Produkci

```python
THRESHOLDS = {
    # Články - závisí na frekvenci generování
    'min_articles_24h': 10,     # 10+ článků denně (cca 2-3/4h run)
    'min_articles_1h': 1,       # Alespoň 1 článek v poslední hodině

    # Čerstvost - závisí na GitHub Actions schedule
    'max_age_hours': 6,         # Max 6h stáří (1.5x interval 4h cron)

    # Jazyk - kritický indikátor
    'min_czech_ratio': 0.85,    # Min 85% českých článků (15% tolerance)

    # Kvalita obsahu
    'min_avg_content_length': 300,  # Min 300 znaků průměrně
    'max_error_rate': 0.10,     # Max 10% chyb ve front matter
}
```

### Alert Sensitivity Matrix

| Threshold | Conservative | Balanced | Aggressive |
|-----------|-------------|----------|------------|
| `min_articles_24h` | 5 | 10 | 15 |
| `max_age_hours` | 12 | 6 | 3 |
| `min_czech_ratio` | 0.70 | 0.85 | 0.95 |
| `max_error_rate` | 0.20 | 0.10 | 0.05 |

**Doporučení:** Začít s **Balanced** a adjustovat na základě false positive/negative rate.

---

## Troubleshooting

### False Positive: Alert i když vše funguje

**Možné příčiny:**
1. Jekyll build selhal → endpoint vrací starý JSON
2. Uptimerobot cache → Force refresh
3. Threshold příliš přísný → Adjustovat

**Debug kroky:**
```bash
# Zkontrolovat aktuální JSON na live site
curl https://marigold.cz/health-check/ | jq .

# Zkontrolovat poslední build
gh run list --workflow=tech-news.yml --limit 5

# Zkontrolovat lokální health data
cat _data/tech_news_health.json | jq .
```

### False Negative: Žádný alert i když je problém

**Možné příčiny:**
1. Keyword match je příliš benevolentní
2. Uptimerobot interval příliš dlouhý
3. Alert threshold příliš vysoký

**Řešení:**
- Použít kombinaci multiple keywords (AND logic)
- Snížit interval na 5 minut
- Snížit consecutive failures threshold na 2

---

## Maintenance & Monitoring Best Practices

### Pravidelné Kontroly (Weekly)

1. **Review Alert History**
   - Zkontrolovat Uptimerobot alert log
   - Identifikovat false positives
   - Adjustovat thresholdy pokud nutné

2. **Validate Metrics Trends**
   - Otevřít `/health-status/` a zkontrolovat trendy
   - Zkontrolovat `czech_ratio` stabilitu
   - Analyzovat `articles_24h` průměr

3. **Test Alert Flow**
   - Manuálně spustit test alert (Uptimerobot UI)
   - Ověřit, že notifikace přicházejí správně

### Monthly Review

1. Analyze false positive/negative rate
2. Review threshold effectiveness
3. Update documentation s findings
4. Consider adding new checks based on issues

---

## Integrace s Dalšími Systémy

### GitHub Actions Integration

**Alert on Workflow Failure:**

Přidat do `.github/workflows/tech-news.yml`:

```yaml
- name: Check health status after generation
  run: |
    python scripts/tech_news_health_check.py

    if [ $? -eq 2 ]; then
      echo "::error::Health check CRITICAL"
      exit 1
    elif [ $? -eq 1 ]; then
      echo "::warning::Health check WARNING"
    fi
```

### Slack Webhook (Advanced)

**Python skript pro posting do Slacku při CRITICAL:**

```python
import requests

def send_slack_alert(health_results):
    if health_results['status'] == 'CRITICAL':
        webhook_url = os.getenv('SLACK_WEBHOOK_URL')
        payload = {
            'text': f"🚨 Tech News Health: {health_results['status']}",
            'blocks': [
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f"*Status:* `{health_results['status']}`\n*Summary:* {health_results['summary']}"
                    }
                }
            ]
        }
        requests.post(webhook_url, json=payload)
```

---

## Cheat Sheet - Rychlá Reference

### Uptimerobot Quick Config

```
Monitor 1 (Primary):
  URL: https://marigold.cz/health-check/
  Keyword: "status": "OK"
  Interval: 5 min
  Alert: 2 consecutive failures

Monitor 2 (Language):
  URL: https://marigold.cz/health-check/
  Keyword NOT: "status": "CRITICAL"
  Interval: 5 min
  Alert: 2 consecutive failures

Monitor 3 (Freshness):
  URL: https://marigold.cz/health-check/
  Keyword: "articles_24h":
  Interval: 15 min
  Alert: Immediate
```

### Important URLs

- **JSON Endpoint:** https://marigold.cz/health-check/
- **HTML Status:** https://marigold.cz/health-status/
- **GitHub Workflow:** https://github.com/username/marigold-page/actions/workflows/tech-news.yml

### Emergency Contacts

- **Primary:** váš@email.cz
- **Secondary:** backup@email.cz
- **Slack:** #tech-news-alerts

---

## Changelog

- **2025-11-14:** Initial setup documentation created
- **YYYY-MM-DD:** (přidat updates při změnách)
