# Technologické zpravodajství - Jekyll & GitHub Pages

## 🚀 Přehled

Automatizované technologické zpravodajství pro Jekyll site s GitHub Pages hostingem. Zprávy se stahují z NewsAPI, překládají pomocí OpenRouter AI a publikují jako Markdown soubory.

## 📁 Struktura souborů

```
marigold-page/
├── .github/workflows/
│   └── tech-news.yml           # GitHub Actions workflow
├── _layouts/
│   ├── tech_news_index.html    # Layout pro /tech-news/
│   └── tech_news.html          # Layout pro jednotlivé zprávy
├── _tech_news/                 # Kolekce technologických zpráv
│   ├── index.md                # Hlavní stránka
│   └── *.md                    # Automaticky generované zprávy
├── scripts/
│   └── fetch_tech_news.py      # Python skript pro stahování
└── _config.yml                 # Jekyll konfigurace (aktualizovaná)
```

## 🛠️ Nastavení

### 1. GitHub Secrets

Přidejte do GitHub repozitáře tyto secrets (Settings → Secrets and variables → Actions):

```
NEWS_API_KEY          # Klíč z https://newsapi.org
OPENROUTER_API_KEY    # Klíč z https://openrouter.ai
```

### 2. Aktivace workflow

GitHub Actions workflow se spustí automaticky:
- **Každé 4 hodiny** (cron: `0 */4 * * *`)
- **Manuálně** přes GitHub Actions tab
- **Po push** změn workflow souboru

### 3. První spuštění

1. Commitněte všechny soubory do main větve
2. Jděte do GitHub → Actions
3. Klikněte na "Tech News Fetcher"
4. Klikněte "Run workflow" pro manuální spuštění

## 📊 Jak to funguje

### Workflow proces

1. **Stahování zpráv**: NewsAPI → technologické zdroje (TechCrunch, The Verge, Wired...)
2. **Překlad**: OpenRouter AI → DeepSeek model přeloží do češtiny
3. **Kategorizace**: AI detekuje kategorii (AI, Programování, Hardware...)
4. **Generování**: Vytvoří Markdown soubory v `_tech_news/`
5. **Publikování**: Git commit → Jekyll build → GitHub Pages

### Jekyll konfigurace

```yaml
collections:
  tech_news:
    output: true
    permalink: /tech-news/:title/
    sort_by: date
```

### Supported kategorie

- 🤖 **AI & ML** - Umělá inteligence
- 💻 **Programování** - Jazyky, frameworky
- 🖥️ **Hardware** - CPU, GPU, komponenty
- 🚀 **Startupy** - Investice, akvizice
- 🔒 **Bezpečnost** - Kybernetika, vulnerabilities
- 📱 **Mobilní** - iOS, Android, aplikace
- 🌐 **Web** - Browsery, webové technologie
- 🎮 **Hry** - Gaming, konzole, esport
- ₿ **Kryptoměny** - Blockchain, DeFi
- 🔬 **Věda** - Kvantové počítače, výzkum

## 🎨 Funkce

### Technické zpravodajství

- ✅ **Automatický překlad** do češtiny pomocí AI
- ✅ **Kategorizace** podle obsahu
- ✅ **Responsivní design** pro všechna zařízení
- ✅ **Filtrování** podle kategorií
- ✅ **Breadcrumb navigace**
- ✅ **Podobné články** na detailu
- ✅ **SEO optimalizované** URL a metadata

### Jekyll integrace

- ✅ **Kolekce** `_tech_news` pro články
- ✅ **Layouty** pro index i detail stránky
- ✅ **Liquid templating** pro filtrování
- ✅ **Automatické buildy** přes GitHub Pages

## 🔧 Přizpůsobení

### Změna zdrojů

V `scripts/fetch_tech_news.py` upravte:

```python
sources = 'techcrunch,the-verge,wired,ars-technica,engadget,hacker-news,the-next-web'
```

### Změna kategorií

V `scripts/fetch_tech_news.py` upravte `TECH_CATEGORIES`:

```python
TECH_CATEGORIES = {
    'new_category': {'emoji': '🔥', 'name': 'New Category', 'cs_name': 'Nová kategorie'}
}
```

### Styling

Upravte CSS v `_layouts/tech_news_index.html` a `_layouts/tech_news.html`.

## 🐛 Řešení problémů

### Workflow selhává

1. **Zkontrolujte GitHub Actions logy**:
   ```
   GitHub → Actions → Tech News Fetcher → View logs
   ```

2. **Časté problémy**:
   - `NEWS_API_KEY není nastaven` → Přidejte do GitHub Secrets
   - `OPENROUTER_API_KEY není nastaven` → Přidejte do GitHub Secrets
   - `NewsAPI limit exceeded` → Free tier má 1000 req/den
   - `OpenRouter kredit vyčerpán` → Zkontrolujte kredit

### Žádné články se nezobrazují

1. **První build trvá čas** - počkejte na dokončení workflow
2. **Jekyll nevidí kolekci** - zkontrolujte `_config.yml`
3. **Commit selhal** - zkontrolujte Actions logy

### Špatné překlady

- **OpenRouter model**: Můžete změnit na jiný v `fetch_tech_news.py`
- **Temperature**: Snižte pro konzistentnější překlady
- **Prompt**: Upravte instrukce pro překlad

## 📈 Monitoring

### GitHub Actions

- **Úspěšné běhy**: Zelené checkmarky
- **Chyby**: Červené kříže s detailními logy
- **Čas spuštění**: Každé 4 hodiny od prvního spuštění

### Jekyll build

- **GitHub Pages**: Settings → Pages → zkontrolujte build status
- **Logy**: GitHub → Actions → pages-build-deployment

### API usage

- **NewsAPI**: 1000 požadavků/den na free tier
- **OpenRouter**: Spotřeba creditů podle použití

## 🔄 Maintenance

### Pravidelné úkoly

- **Týdně**: Zkontrolujte úspěšnost workflow
- **Měsíčně**: Ověřte API kredity a limity
- **Při chybách**: Zkontrolujte logy a opravte

### Updates

- **NewsAPI zdroje**: Přidejte nové tech weby
- **Kategorisace**: Vylepšete klíčová slova
- **Design**: Aktualizujte styling podle potřeby

## 🔗 Užitečné odkazy

- [NewsAPI dokumentace](https://newsapi.org/docs)
- [OpenRouter API](https://openrouter.ai/docs)
- [Jekyll Collections](https://jekyllrb.com/docs/collections/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [GitHub Pages](https://pages.github.com/)

---

**Aplikace nepoužívá mock data - vyžaduje správně nastavené API klíče pro funkčnost.**