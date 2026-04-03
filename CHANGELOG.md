# Changelog

Všechny významné změny v projektu Marigold.cz jsou dokumentovány v tomto souboru.

Formát vychází z [Keep a Changelog](https://keepachangelog.com/cs/1.0.0/),
a projekt dodržuje [Semantic Versioning](https://semver.org/lang/cs/).

## [Unreleased]

### Fixed
- Post `prirucka-ai-ve-firmach-zdarma` přesunut z `_posts/` do `content/posts/` pro kompatibilitu s Hugo buildem
- Thumbnail `ebook-ai-ve-firmach.png` zkopírován do `static/assets/` aby byl dostupný v Hugo buildu
- Accessibility: přidán skip-to-content link do default.html a aiprace.html layoutů
- Accessibility: emoji search link doplněn o `aria-label="Hledat"` (WCAG 2.4.6)
- Accessibility: `<p datetime>` opraven na validní `<time datetime>` v post.html
- Accessibility: toast notifikace doplněna o `role="status" aria-live="polite"` (WCAG 4.1.3)
- Accessibility: přidána podpora `prefers-reduced-motion` pro všechny animace
- Performance: Mermaid JS podmíněn přítomností `.language-mermaid` — nenahrává se na každém postu
- Performance: Liquid navigační loop v tech_news.html nahrazen Jekyll built-in `page.previous/next` (O(n²)→O(1))
- Responsive: Substack iframe opraven — `width="480"` odstraněn, přidán `max-width:480px;width:100%`
- Responsive: Audio player tlačítka rozšířena na min 44×44px touch target
- Theming: dark mode paleta nahrazena — odstraněny AI purple-navy barvy (#1a1a2e→#16181c rodina)
- Theming: `#667eea` bullet barva v quick-summary nahrazena proměnnou `$blue`
- Theming: Open Sans legacy font reference nahrazen `$system-font` v `.cd-container`
- Code: inline CSS audio playeru přesunut z index.html do assets/style.scss a assets/scss/main.scss
- Content: Workshop banner aktualizován (prošlá early bird deadline 31.3.2026 nahrazena)

## [3.0.0] - 2026-03-29

### Changed
- **Migrace z Jekyll na Hugo** - build cas z ~500s na ~8s (60x zrychleni)
  - Vsechny layouty prevedeny z Liquid na Go templates
  - Obsah prestan do `content/` struktury (posts, ai, mobilnisite, obrazy, tech-news)
  - SCSS zpracovani pres Hugo Pipes misto Jekyll Sass
  - GitHub Actions workflow `hugo-build.yml` nahradi `build.yml`
  - Vsechny URL zachovany (2957 postu, 10873 archivnich stranek)
- **Dark/Light mode s manualnim prepinacem** - tlacitko slunce/mesic v navigaci
  - Automaticke prepnuti po zapadu slunce (18:00-06:00)
  - Persistence volby v localStorage
  - Kompatibilni s aiprace vlastnim dark mode CSS
- **Redesign paticka** - dva sloupce (Projekty / Dalsi) misto jednoradkoveho seznamu
  - Nove inline SVG socialni ikony (email, Facebook, X, LinkedIn, RSS)
  - Nove odkazy: AI ve firmach, Workshopy Claude Code, Kurz AI zdarma, Vliv AI na pracovni mista
- **Newsletter CTA** - nahrazuje Substack iframe kompaktnim CTA boxem
- **Navigace** - semanticka `<ul>` s `aria-label`, `white-space: nowrap`
  - Aiprace pridano do dropdown menu jako "AI prace"

### Added
- **Ahrefs Analytics** - mereni navstevnosti v `<head>`
- **Table of Contents** - automaticky generovany obsah z h2/h3 nadpisu
  - Cislovane polozky, rozbalitelny, transparentni pozadi
  - Nahrazuje Jekyll `{:toc}` syntaxi
- **Scroll progress bar** - gradientni linka ukazuje pozici cteni v clanku
- **Audio prehravac** - playlist poslednich 20 clanku s audio na homepage
- **Aiprace layout** - plna sirka (1600px) s D3.js vizualizaci
- **Post edit link** - diskretni odkaz "Upravit" na GitHub edit

### Fixed
- **Accessibility** - `lang="cs"`, focus-visible styly, iframe title, touch targety 44px
- **Flexbox layout** - masthead a footer misto float/absolute
- **Thumbnaily** - landscape 4:3 (200x150), nadpis nad thumbnailem
- **Vyhledavani** - opraveny dvojite uvozovky v search indexu (safeJS)
- **Case-sensitive URL** - 10 postu s velkymi pismeny opraveno explicitnim `url:` front matter

### Removed
- **Smazano assets/tech-news/** - 11073 nepouzivanch obrazku (852 MB)
- **Vypnuty workflows** - podcast, OneSignal notifications, tech-news, translate (if: false)
- **Sdilejte clanek** sekce - nahrazena kompaktni navigaci + edit linkem

### Removed
- **LLM rubrika deaktivována** - služba přesunuta na jiný server
  - Smazán GitHub Actions workflow `llm-tracker.yml` (denní generování zastaveno)
  - Odstraněna kolekce `llm` z `_config.yml` (stránky se negenerují)
  - Smazána hlavní stránka `_pages/llm.md`
  - Soubory v `_llm/`, skripty a layouty ponechány jako archiv

### Changed
- **Migrace z OneSignal na Firebase Cloud Messaging (FCM)** - kompletní přepracování push notifikací
  - Nový service worker `firebase-messaging-sw.js` pro FCM
  - Nové include soubory `_includes/fcm-marigold.html` a `_includes/fcm-vibecoding.html`
  - Cloud Functions pro topic subscription (`firebase-functions/`)
  - Nový Python skript `.github/scripts/send_fcm_notifications.py` pro odesílání notifikací
  - Nový workflow `.github/workflows/send-fcm-notifications.yml`
  - Lepší spolehlivost a nulové náklady (Google infrastruktura)
  - Topic-based subscription: `marigold-news` a `vibecoding-news`

### Fixed
- **Stránkování** - přidány chybějící CSS styly pro `.pagination` element
  - Správné odsazení od obsahu a patičky (padding 30px nahoře, 40px dole)
  - Vizuální styling tlačítek stránkování s hover efekty
  - Zvýraznění aktuální stránky modrou barvou

### Removed
- `OneSignalSDKWorker.js` - nahrazeno Firebase service workerem
- `_includes/onesignal.html` - nahrazeno FCM implementací
- `_includes/onesignal-vibecoding.html` - nahrazeno FCM implementací

### Added
- **LLM Model Tracker** - automatický systém pro sledování a analýzu nových LLM modelů z OpenRouter API
  - Nový skript `scripts/track_llm_models.py` - detekuje a analyzuje nové modely
  - Watermark mechanismus - sleduje nejnovější známý model, analyzuje pouze novější
  - Automatická analýza pomocí Gemini 3 Pro s porovnáním konkurence
  - Generuje Jekyll posty do `_llm/` kolekce (formát `YYYY-MM-DD-model-slug.md`)
  - Překlad popisů modelů do češtiny pomocí LLM
  - Data tracking v `_data/llm_models_tracked.json`
  - CLI příkazy: `--dry-run`, `--list-tracked`, `--status`, `--reset-watermark`
  - GitHub Actions workflow `.github/workflows/llm-tracker.yml` - denní spuštění v 6:00 UTC
- **Jekyll kolekce `_llm`** - nová kolekce pro recenze LLM modelů
  - Layout `_layouts/llm_review.html` - kompletní vizuální šablona pro recenze
  - Přehledová stránka `/llm/` s filtry podle providera
  - Kolekce nepřidává články na titulní stránku (oddělená od `_posts`)
  - Permalink struktura: `/llm/:slug/`
- **LLM Model Card Generator** - generátor HTML karet pro jednotlivé modely
  - Skript `scripts/fetch_llm_model_card.py` - stahuje data a generuje vizualizace
  - HTML šablona `scripts/templates/llm_model_card.html` - dark mode design
  - Strukturovaná JSON analýza s profily, silnými/slabými stránkami, konkurencí
  - Dynamické porovnání s aktuálními modely od Anthropic, Google, OpenAI, xAI, Mistral, DeepSeek
- **Hybridní navigační menu** - implementována dropdown navigace s tlačítkem "Další ☰"
  - Hlavní položky zůstávají viditelné: 🔍 | 🧑‍💻 Kurzy AI | 🖥️ Vibecoding | 🗼 4G/5G | 🤖 AI
  - Pod tlačítko "Další" schovány: 💻 Zprávy | 🖼️ Obrazy
  - Čistý minimalistický design s dropdown menu pod tlačítkem "Další"
  - Vanilla JavaScript pro toggle funkčnost (bez závislostí)
  - Kompletní přístupnost: aria-expanded, keyboard navigation (Enter/Space/Escape)
  - Responzivní na mobilu - dropdown centrovaný, fade-in animace
  - Kliknutí mimo nebo Escape zavře menu
- **Archivace tech_news** - automatické převádění starých článků na statické HTML
  - Nový skript `scripts/archive_tech_news.py` - archivuje články starší než 7 dní
  - Staré články se převedou na statické HTML do `tech-news-archive/`
  - Jekyll zpracovává pouze čerstvé články - rychlejší build
  - Integrace do GitHub Actions workflow (build.yml)
  - URL zůstávají zachované: `/tech-news/YYYY-MM-DD/slug/`
- **Optimalizace generátoru tech_news** - snížení počtu článků
  - Práh důležitosti zvýšen z 3 na 4 (pouze "velmi důležité" a "průlomové")
  - PageSize snížen ze 100 na 50 článků
  - Očekávaný výsledek: ~20-30 článků/den místo 300+

### Fixed
- **Vibecoding.cz build** - opravena chyba "Cannot sort a null object" při buildu
  - Přidány chybějící exclude položky do `_config_vibecoding.yml`
  - Vyloučeny stránky využívající kolekce nedefinované pro vibecoding (llm, tech_news atd.)
  - Vyloučeny dokumentační markdown soubory v rootu (TECH_NEWS_*.md, CHANGELOG.md atd.)
  - Build nyní úspěšně projde a články z prosince jsou viditelné
- **Tech-news workflow race condition** - opraveno selhání git push při paralelních jobech
  - Přidán `git pull --rebase` před push v tech-news.yml workflow
  - Přidán tech-news-archive/ do git add pro archivované články

### Changed
- **Kompaktní patička** - redesign footeru na 3 řádky místo 3 sloupců
  - Řádek 1: Sociální ikony (email, facebook, twitter, linkedin, rss) + copyright
  - Řádek 2: Všechny projekty inline (Marigold.cz, Zítřaslavní.cz, VibeCoding.cz, TopFlix.cz, Substack, Fenix svítilny, Vybavení do přírody, Brandýs nad Labem, Letní škola AI, Changelog)
  - Řádek 3: Badges (Clicky analytics, GitHub last commit)
  - Menší výška patičky (~150px místo 300px+)
  - Partnerské odkazy přesunuty z analytics.html do footer.html

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

**Aktualizováno**: 2025-12-08
