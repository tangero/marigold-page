# Tech-News Analytics s Clicky

Implementace pokročilého trackingu a optimalizace tech-news sekce pomocí Clicky Web Analytics.

## 🚀 Funkcionalita

### Tracking implementován:
- ✅ **Kliknutí na články** - kategorie, důležitost, pozice
- ✅ **Externí odkazy** - čtení celých článků
- ✅ **Použití filtrů** - zájem o specifický obsah
- ✅ **Goals pro kategorie** - AI, startupy, programování atd.
- ✅ **Automatická analýza** - týdenní reporty
- ✅ **Optimalizace algoritmu** - na základě skutečných dat

## 📊 Trackované metriky

### Events v Clicky:
```
#tech-news-click/{category}/{importance}     - Základní kliknutí
#tech-news-detail/{category}/{importance}/{position} - Detailní tracking
#tech-news-filter/{type}/{filter}           - Použití filtrů
{external-url}                              - Odchody na původní články
```

### Goals:
- **High Priority Article Click** - Články s důležitostí 4-5
- **Read Full Article** - Konverze na externí odkazy
- **Content Filter Used** - Aktivní filtrování obsahu
- **AI Article Click** - Zájem o AI obsah
- **Startup Article Click** - Zájem o startupy
- Další kategorie...

## ⚙️ Setup

### 1. Clicky konfigurace

V Clicky admin panelu vytvořit goals podle `_data/clicky_goals.yaml`:

```yaml
Goals → Add Goal:
- Name: "High Priority Article Click"
- Type: "Action Goal"
- Target URL/Action: obsahuje "#tech-news-click"
```

### 2. Environment proměnné

Přidat do `.env`:
```bash
CLICKY_SITE_ID=101451859  # již nastaveno
CLICKY_SITEKEY=your_api_key_here  # získat z Clicky → Preferences → API
```

### 3. Dependencies

```bash
pip install requests beautifulsoup4 pyyaml python-dotenv
```

## 📈 Použití

### Ruční analýza
```bash
# Týdenní report
python scripts/analyze_tech_news_clicky.py

# Měsíční report
python scripts/analyze_tech_news_clicky.py --days 30
```

### Automatická optimalizace
```bash
# Simulace změn (dry run)
python scripts/optimize_tech_news.py --dry-run

# Aplikovat optimalizace
python scripts/optimize_tech_news.py

# Optimalizace za delší období
python scripts/optimize_tech_news.py --days 14
```

### Výstupy

**Analytics reporty:**
- `_data/tech_news_analytics/tech_news_report_YYYYMMDD.json`
- `_data/tech_news_analytics/optimization_history.json`

**Co reporty obsahují:**
- 📊 Top články podle kliknutí
- 🎯 Performance podle kategorií
- 📈 Korelace AI důležitosti vs. skutečné CTR
- 📍 Vliv pozice na engagement
- 💡 Doporučení pro optimalizaci

## 🔄 Automatizace

### GitHub Actions (doporučeno)

Přidat do `.github/workflows/tech-news-optimization.yml`:

```yaml
name: Tech News Analytics & Optimization

on:
  schedule:
    - cron: '0 6 * * 1'  # Každé pondělí v 6:00
  workflow_dispatch:

jobs:
  optimize:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: pip install requests beautifulsoup4 pyyaml python-dotenv

      - name: Run analytics
        env:
          CLICKY_SITEKEY: ${{ secrets.CLICKY_SITEKEY }}
        run: python scripts/analyze_tech_news_clicky.py

      - name: Auto-optimize
        env:
          CLICKY_SITEKEY: ${{ secrets.CLICKY_SITEKEY }}
        run: python scripts/optimize_tech_news.py

      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add _data/
          git diff --staged --quiet || git commit -m "🤖 Automatická optimalizace tech-news na základě analytics"
          git push
```

### Cron job (alternativa)

```bash
# Přidat do crontab
0 6 * * 1 cd /path/to/marigold-page && python scripts/optimize_tech_news.py
```

## 📋 Dashboard v Clicky

### Užitečné reporty:

**Actions → Search:**
- Filtr: `#tech-news` - všechny tech-news akce
- Filtr: `#tech-news-click/ai` - pouze AI články
- Filtr: `#tech-news-filter` - použití filtrů

**Goals:**
- Sledovat konverzní rate pro každou kategorii
- Porovnávat performance přes čas

**Heatmaps:**
- Kde uživatelé nejvíc klikají na tech-news stránce
- Optimalizace layoutu

## 🎯 KPI a optimalizace

### Klíčové metriky:
- **CTR tech-news**: % návštěvníků tech-news, kteří kliknou na článek
- **Read-through rate**: % lidí, kteří přečtou celý článek
- **Category balance**: Rozložení zájmu o kategorie
- **Importance accuracy**: Korelace AI důležitosti vs. skutečné CTR
- **Position effect**: Jak pozice ovlivňuje kliknutí

### Cíle:
- CTR tech-news: **15%+**
- Read-through rate: **25%+**
- Importance correlation: **0.8+**

### Automatické optimalizace:
1. **Priority zdrojů** - zvýšení pro zdroje s vysokým engagement
2. **Max články** - více článků z populárních kategorií
3. **Filtry** - zpřísnění pro lepší kvalitu
4. **Importance algoritmus** - rekalirace na základě dat

## 🔍 Debugging

### Ověření trackingu:
1. Otevřít tech-news stránku
2. Otevřit Developer Tools → Console
3. Kliknout na článek
4. Zkontrolovat, že se volají `clicky.log()` a `clicky.goal()`

### Troubleshooting:
- Chybějící Clicky API key → analytics nefunguje
- Nesprávné goals setup → některé konverze se netrackují
- Rate limity → omezit frekvenci API volání

## 📚 Další možnosti

### Rozšíření:
- **A/B testování titulků** - porovnání originálních vs. přeložených
- **Personalizace** - doporučení na základě historie
- **Real-time optimalizace** - úpravy priorit během dne
- **Social sharing tracking** - viral potential článků

### Integrace:
- **Simple Analytics** - pro privacy-first metriky
- **Google Analytics** - pro pokročilé segmentace (pokud povoleno)
- **Newsletter analytics** - propojení s email kampaněmi