# Health Check System - Quick Start Guide

Rychlý průvodce pro nastavení a použití Tech News Health Check systému.

## 🚀 5-Minute Setup

### 1. Ověřit, že systém funguje lokálně

```bash
cd /Users/patrickzandl/GitHub/marigold-page

# Spustit health check
python3 scripts/tech_news_health_check.py

# Měli byste vidět výstup typu:
# ============================================================
# TECH NEWS HEALTH CHECK: OK/WARNING/CRITICAL
# ============================================================
# Status: OK | Články 24h: 15 | Čeština: 92.3%
```

### 2. Zkontrolovat vygenerovaný JSON

```bash
cat _data/tech_news_health.json | jq '.'
```

Měli byste vidět strukturu:
```json
{
  "status": "OK",
  "timestamp": "2025-11-14T...",
  "metrics": { ... },
  "checks": { ... },
  "alerts": [ ... ]
}
```

### 3. Build a test Jekyll

```bash
bundle exec jekyll build

# Test JSON endpoint
cat _site/health-check/index.html | jq '.status'

# Test HTML dashboard
open _site/health-status/index.html
```

### 4. Deploy na GitHub

```bash
git add scripts/tech_news_health_check.py
git add health-check.html
git add health-status.html
git add _data/tech_news_health.json
git add .github/workflows/tech-news.yml
git add tests/test_health_check.py
git add docs/

git commit -m "Add tech-news health check system"
git push
```

### 5. Nastavit Uptimerobot (5 minut)

1. **Přihlásit se do Uptimerobot:** https://uptimerobot.com/

2. **Vytvořit Primary Monitor:**
   - Kliknout "Add New Monitor"
   - Monitor Type: `HTTP(s)`
   - Friendly Name: `Marigold Tech News - Health Check`
   - URL: `https://marigold.cz/health-check/`
   - Monitoring Interval: `5 minutes`
   - Scroll dolů na "Advanced Settings"
   - Enable "Keyword monitoring"
   - Keyword Type: `Keyword Exists`
   - Keyword: `"status": "OK"`
   - Alert Contacts: Přidat svůj email
   - Create Monitor

3. **Test Monitor:**
   - Počkat 5 minut na první check
   - Zkontrolovat, že status je "Up" (zelený)
   - Pokud je "Down", zkontrolovat keyword matching

4. **Optional: Vytvořit Language Monitor:**
   - Add New Monitor
   - Monitor Type: `HTTP(s)`
   - Friendly Name: `Marigold Tech News - Language Check`
   - URL: `https://marigold.cz/health-check/`
   - Interval: `5 minutes`
   - Keyword Type: `Keyword NOT Exists`
   - Keyword: `"status": "CRITICAL"`
   - Create Monitor

**Hotovo! 🎉** Systém nyní automaticky monitoruje tech-news zdraví.

---

## 📊 Denní Použití

### Zkontrolovat zdraví systému

**Rychlá kontrola (30 sekund):**
```bash
# Otevřít health status dashboard
open https://marigold.cz/health-status/
```

**Programmatický check:**
```bash
# JSON endpoint
curl -s https://marigold.cz/health-check/ | jq '.status'

# Pokud vrátí "OK" → vše v pořádku
# Pokud vrátí "WARNING" → drobné problémy
# Pokud vrátí "CRITICAL" → vyžaduje pozornost
```

### Při obdržení alertu z Uptimerobot

**Krok 1: Diagnóza (2 minuty)**

```bash
# 1. Otevřít health status
open https://marigold.cz/health-status/

# 2. Zkontrolovat sekci "Alerty"
# Přečíst si, jaké konkrétní problémy byly detekovány

# 3. Zkontrolovat metriky
# - Články 24h: Mělo by být ≥ 10
# - Poměr češtiny: Mělo by být ≥ 85%
# - Stáří nejnovějšího: Mělo by být ≤ 6h
```

**Krok 2: Zkontrolovat GitHub Actions (1 minuta)**

```bash
# Zkontrolovat poslední workflow run
gh run list --workflow=tech-news.yml --limit 5

# Pokud poslední run selhal:
gh run view --workflow=tech-news.yml

# Zkontrolovat logy
gh run view --log
```

**Krok 3: Běžné problémy a řešení**

| Alert | Možná příčina | Řešení |
|-------|---------------|--------|
| "Pouze X% článků v češtině" | LLM API selhání | Zkontrolovat OPENROUTER_API_KEY, zkontrolovat LLM API status |
| "Nejnovější článek starý Xh" | GitHub Actions nesběhl | Zkontrolovat workflow schedule, manuálně spustit workflow |
| "Pouze X článků za 24h" | NewsAPI problém | Zkontrolovat NEWS_API_KEY, zkontrolovat NewsAPI quota |

**Krok 4: Manuální fix (pokud nutné)**

```bash
# Manuálně spustit tech-news generování
cd /Users/patrickzandl/GitHub/marigold-page

# S produkčními credentials
export NEWS_API_KEY="..."
export OPENROUTER_API_KEY="..."

python3 scripts/generate_tech_news_newsapi.py

# Spustit health check
python3 scripts/tech_news_health_check.py

# Pokud nyní OK, commit a push
git add _tech_news/ _data/tech_news_health.json
git commit -m "Manual tech-news update after fixing issue"
git push
```

---

## 🧪 Testing

### Otestovat lokální změny

```bash
# 1. Spustit unit tests
python3 -m pytest tests/test_health_check.py -v

# 2. Spustit health check na produkčních datech
python3 scripts/tech_news_health_check.py

# 3. Build Jekyll a zkontrolovat endpoints
bundle exec jekyll build
cat _site/health-check/index.html | jq '.'
open _site/health-status/index.html
```

### Simulovat failure scénáře

**Scénář: Nízký poměr češtiny**

```bash
# Dočasně upravit threshold v scripts/tech_news_health_check.py
# Řádek cca 30:
THRESHOLDS = {
    'min_czech_ratio': 1.0,  # Změnit z 0.85 na 1.0
}

# Spustit
python3 scripts/tech_news_health_check.py

# Měli byste vidět CRITICAL alert
# Vrátit změnu zpět po testu!
```

**Scénář: Starý obsah**

```bash
# Změnit threshold
THRESHOLDS = {
    'max_age_hours': 0.1,  # Velmi krátký čas
}

# Spustit a ověřit WARNING alert
python3 scripts/tech_news_health_check.py
```

---

## 🔧 Customization

### Upravit thresholdy

Editovat `scripts/tech_news_health_check.py`, sekce `THRESHOLDS`:

```python
THRESHOLDS = {
    'min_articles_24h': 10,      # Změnit podle potřeby
    'min_articles_1h': 1,
    'max_age_hours': 6,          # Zvýšit pokud příliš mnoho false positives
    'min_czech_ratio': 0.85,     # Zvýšit pro přísnější kontrolu
    'min_avg_content_length': 300,
    'max_error_rate': 0.10,
}
```

**Po změně:**

```bash
# Test
python3 scripts/tech_news_health_check.py

# Commit
git add scripts/tech_news_health_check.py
git commit -m "Adjust health check thresholds"
git push
```

### Přidat nová česká slova pro detekci

Editovat `scripts/tech_news_health_check.py`, sekce `CZECH_WORDS`:

```python
CZECH_WORDS = {
    'který', 'která', 'které',
    # ... existing words ...
    'smartphone',  # Přidat nové
    'tablet',
    # atd.
}
```

### Upravit Uptimerobot alert email

V Uptimerobot dashboardu:
1. My Settings → Alert Contacts
2. Edit svůj email contact
3. Customize alert message template
4. Save

---

## 📱 Mobile Monitoring (Optional)

### Uptimerobot Mobile App

1. Stáhnout Uptimerobot app (iOS/Android)
2. Přihlásit se stejným účtem
3. Enable push notifications
4. Nyní dostáváte alerts i na mobil

### Status Page Widget

Vytvořit public status page v Uptimerobot:
1. Public Status Pages → Add New
2. Vybrat tech-news monitors
3. Customize design
4. Publish
5. Sdílet URL s týmem

---

## 🆘 Troubleshooting FAQ

### Q: Health check hlásí CRITICAL ale vše vypadá OK?

**A:** Zkontrolovat:
```bash
# 1. Je deployed nejnovější verze?
curl -s https://marigold.cz/health-check/ | jq '.timestamp'

# 2. Je timestamp aktuální? (měl by být < 4h starý)
# Pokud ne, Jekyll build selhal nebo deployment trvá

# 3. Zkontrolovat GitHub Pages build
gh workflow view pages-build-deployment
```

### Q: Uptimerobot posílá příliš mnoho false positive alertů?

**A:**
```bash
# 1. Zkontrolovat threshold values v health check scriptu
grep -A 6 "THRESHOLDS = {" scripts/tech_news_health_check.py

# 2. Zvážit adjustaci thresholdů (viz Customization)

# 3. Nebo zvýšit Uptimerobot "consecutive failures" threshold
# v Uptimerobot → Edit Monitor → Alert when down for: 3 checks (15 min)
```

### Q: Health check script selhává s chybou?

**A:**
```bash
# 1. Zkontrolovat Python dependencies
pip3 install -r requirements.txt

# Nebo manuálně:
pip3 install pyyaml requests beautifulsoup4 python-dateutil

# 2. Spustit s debug output
python3 scripts/tech_news_health_check.py 2>&1 | tee debug.log

# 3. Zkontrolovat Python verzi (měla by být 3.9+)
python3 --version
```

### Q: JSON endpoint vrací 404?

**A:**
```bash
# 1. Zkontrolovat že health-check.html existuje v root
ls -la health-check.html

# 2. Rebuild Jekyll
bundle exec jekyll build

# 3. Zkontrolovat že je v _site/
ls -la _site/health-check/

# 4. Deploy
git add health-check.html
git commit -m "Add health check endpoint"
git push
```

---

## 📚 Další Dokumentace

- **Kompletní systémová dokumentace:** `docs/HEALTH_CHECK_SYSTEM.md`
- **Uptimerobot detailní setup:** `docs/UPTIMEROBOT_SETUP.md`
- **Test suite:** `tests/test_health_check.py`

## 🎯 Next Steps

1. ✅ Nastavit Uptimerobot monitoring (5 min)
2. ✅ Přidat svůj email jako alert contact
3. ✅ Test alert flow (send test alert v Uptimerobot)
4. ⏰ Naplánovat weekly review (15 min každý týden)
5. 📊 Po 2 týdnech: Review metrics a adjust thresholdy

---

**Potřebujete pomoc?**
- Zkontrolovat full docs: `docs/HEALTH_CHECK_SYSTEM.md`
- GitHub Issues: https://github.com/username/marigold-page/issues
- Email: váš@email.cz
