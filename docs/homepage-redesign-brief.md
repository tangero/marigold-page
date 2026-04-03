# Zadani redesignu titulni stranky Marigold.cz

## 1. O projektu

**Marigold.cz** je osobni blog Patricka Zandla o technologiich, AI a mobilnich sitich. Web existuje od roku 2002, obsahuje 2973 clanku. Cilova skupina: technicti profesionalove, vyvojari, manazeři v IT, lide zajimajici se o AI a telekomunikace.

**Technologicky stack:**
- **Generator**: Hugo 0.159.1 (extended, SCSS support)
- **Hosting**: GitHub Pages + GitHub Actions
- **Sablony**: Go templates (`layouts/`)
- **Styly**: SCSS (`assets/scss/main.scss`), kompilace pres Hugo Pipes
- **Obrazky**: Cloudinary CDN pro transformace thumbnailů
- **Dark/Light mode**: `data-theme` atribut na `<html>`, localStorage persistence, auto-sunset (18:00-06:00)
- **Kontejner**: max-width 740px, centrovany
- **Font**: System font stack (-apple-system, BlinkMacSystemFont, Segoe UI, Roboto)
- **Barvy**: `$blue: #4183C4`, dark mode `#6db3f2`, pozadi light `#fff` / dark `#1a1a2e`

---

## 2. Soucasny stav titulni stranky

### Struktura shora dolu:

```
+--------------------------------------------------+
| #bar - scroll progress indicator (5px, fixed)    |
+--------------------------------------------------+
| HLAVICKA                                          |
| [Avatar 70px] Marigold.cz        Nav: 🔍 | AI.. |
|               Technologie a Svet       [☰][🌙]  |
+--------------------------------------------------+
| AUDIO PREHRAVAC (sticky, top: 10px)              |
| [▶️] [⏮️] [⏭️] Nazev skladby...    ▬▬▬ 0:00    |
+--------------------------------------------------+
| POST 1 (s thumbnailem)                           |
| Nadpis H2                                        |
| [Thumb 200x150] Excerpt text 300 znaku...        |
| dd. mesic YYYY - POKRACUJ VE CTENI 👉            |
| ─────────────────────────────────────             |
| POST 2 (bez thumbnailu)                          |
| Nadpis H2                                        |
| Excerpt text 300 znaku...                        |
| dd. mesic YYYY - POKRACUJ VE CTENI 👉            |
| ─────────────────────────────────────             |
| ... (celkem 15 postu na stranku)                 |
+--------------------------------------------------+
| PAGINACE                                          |
| « Novejsi  1 2 [3] 4 5 ... 199  Starsi »        |
+--------------------------------------------------+
| PATICKA                                           |
| [📧] [FB] [X] [LI] [RSS]                        |
| © 2026 Patrick Zandl                              |
| ─────────────────────                              |
| Projekty        | Dalsi                           |
| Marigold.cz     | Kurz AI zdarma                  |
| VibeCoding.cz   | Workshopy Claude Code           |
| AI ve firmach   | Patrickuv newsletter            |
| ...             | ...                              |
| ─────────────────────                              |
| [GitHub last commit badge]                        |
+--------------------------------------------------+
```

### Obsahove bloky a jejich data

| # | Blok | Datovy zdroj | Podminky zobrazeni |
|---|------|-------------|-------------------|
| 1 | Progress bar | JS scroll event | Vzdy |
| 2 | Hlavicka | `hugo.toml` params | Vzdy |
| 3 | Audio prehravac | Posty s `audio_url` (80 ks) | Jen pokud existuji audio posty |
| 4 | Workshop banner | Hardcoded v `layouts/posts/single.html` | Jen na clancich (NE na homepage) |
| 5 | Seznam postu | `posts` + `ai` + `mobilnisite` kolekce, filtrovane `hide != true`, razene dle data | Vzdy, 15 na stranku |
| 6 | Paginace | Hugo paginator | Pokud vice nez 1 stranka |
| 7 | Paticka | Hardcoded odkazy + `hugo.toml` params | Vzdy |

### Klicove metriky obsahu

| Metrika | Hodnota |
|---------|---------|
| Celkem clanku | 2 973 |
| Clanky s thumbnailem | 171 (5.7%) |
| Clanky s audio | 80 (2.7%) |
| Clanku na stranku | 15 |
| Celkem stranek paginace | ~199 |
| AI clanky | 22 |
| Mobilni site clanky | 26 |

---

## 3. Problemy soucasneho designu

### Vizualni

1. **Monotonni layout** -- vsechny posty vypadaji stejne (nadpis + text), jen 5.7% ma thumbnail. Vysledek je zed textu bez vizualniho rozliseni.
2. **Zadna hierarchie dulezitosti** -- nejnovejsi clanek vypada stejne jako 15. v poradi. Ctenar nema vizualni vodítko, co je dulezite.
3. **Thumbnail jen u mala casti** -- 94% clanku nema obrazek, takze layout thumbnailů je spise vyjimka nez pravidlo.
4. **Audio prehravac** -- vizualne oddelen od obsahu, neni jasne, proc tam je a co nabizi.
5. **"POKRACUJ VE CTENI 👉"** -- opakujici se CTA na kazdem postu je redundantni (cely nadpis je uz odkaz).
6. **Zadne kategoricke rozliseni** -- ctenar nevidi, zda clanek je o AI, mobilnich sitich nebo necemu jinem.

### Funkcni

7. **Homepage nenabizi zkratky** -- ctenar musi scrollovat pres 15 postu, neni zadny "featured" nebo "editor's pick" blok.
8. **Zadne sticky/promoted clanky** -- dulezite evergreen clanky (napr. prehled AI, mobilni site tutorialy) se ztrati v chronologickem proudu.
9. **Chybi "co cist dal"** -- po poslednich 15 postach je jen paginace, zadna tematicka nabidka.
10. **Substack/newsletter** -- na homepage neni zadna newsletter CTA (je jen v clancich).

### Technicke

11. **Float-based thumbnail** -- `.thumbnail { float: left }` je funkcni ale krehky. Na mobilech se thumbnail zobrazuje nad textem na celou sirku.
12. **Inline styly audio prehravace** -- CSS je v `<style>` tagu primo v layoutu, ne v centralnim SCSS.
13. **Kontejner 740px** -- pro moderní web uzký, ale odpovida blogovemu formatu.

---

## 4. Co redesign MUSI zachovat

1. **Vsechny URL** -- zadne zmeny v URL strukture
2. **Dark/Light mode** -- fungujici prepinac + auto-sunset
3. **Audio prehravac** -- playlist poslednich 20 audio clanku
4. **Scroll progress bar** -- gradientni indikator cteni
5. **Paginace** -- pristup ke vsem 2973 clankum
6. **SEO** -- meta tagy, OG images, sitemap, RSS feed
7. **Rychlost** -- Hugo build pod 10s, zadne externi JS frameworky
8. **Accessibility** -- ARIA atributy, keyboard navigace, focus styly
9. **Responsive** -- mobil-first, funguje od 320px
10. **Cloudinary** -- thumbnail optimalizace pres CDN

---

## 5. Navrhove otazky k diskusi

### A. Layout hlavni plochy

**Varianta A1: Featured + chronologicky proud**
- Prvni clanek velky (hero-style, plna sirka, velky thumbnail)
- 2.-4. clanek stredne velke (2 sloupce nebo horizontalni karty)
- Zbytek (5.-15.) kompaktni seznam

**Varianta A2: Tematicke bloky + proud**
- Blok "AI" (3 nejnovejsi AI clanky)
- Blok "Mobilni site" (3 nejnovejsi)
- Chronologicky proud vsech clanku

**Varianta A3: Zachovat proud, vylepsit karty**
- Kazdy post jako karta s jemnym pozadim
- Kategorie badge (AI/5G/obecne)
- Datum prominentnejsi
- Posts s thumbnailem vizualne odlisene

### B. Navigace a kategorie

**Otazka**: Ma homepage ukazovat filtraci podle kategorii (AI / Mobilni site / Vsechno)?

### C. Newsletter CTA

**Otazka**: Kam umistit newsletter CTA na homepage?
- Pod prvni clanek?
- Mezi 5. a 6. clankem?
- Sticky sidebar (pokud rozsirrime kontejner)?

### D. Workshop/promo banner

**Otazka**: Ma byt promo banner (workshop, kniha, atd.) na homepage? Kde?

### E. Audio prehravac

**Otazka**: Ma audio prehravac zustat sticky nahore, nebo byt integrovany do clanku ktere maji audio?

### F. Sirka kontejneru

**Otazka**: Zachovat 740px (citelny sloupec), nebo rozsirit na 960-1100px (vice prostoru pro 2-sloupcovy layout)?

---

## 6. Technicke omezeni

| Omezeni | Detail |
|---------|--------|
| Generator | Hugo -- Go templates, zadne React/Vue/JS frameworky |
| CSS | SCSS kompilace pres Hugo Pipes, jeden soubor `main.scss` |
| JavaScript | Vanilla JS, zadne npm dependencies |
| Hosting | GitHub Pages -- staticky hosting, zadne serverove funkce |
| Obrazky | Cloudinary CDN pro transformace, ne lokalni zpracovani |
| Build cas | Musi zustat pod 15s (aktualne ~8s) |
| Fonts | System font stack, zadne vlastni fonty (rychlost) |
| Dark mode | `[data-theme="dark"]` selektor, vsechny styly musi mit dark variantu |
| Obsah | 94% clanku nema thumbnail -- design musi fungovat i bez obrazku |
| Retrokompatibilita | Stare clanky (2002-2022) nemaji thumbnail ani kategorie |

---

## 7. Reference a inspirace

Blogy s podobnym obsahem a estetickym cilem:
- **Stratechery.com** -- cistu typograficky blog, premium obsah
- **Daring Fireball** -- minimalisticky, silna typografie
- **CSS-Tricks** -- kategorizovany tech blog
- **Smashing Magazine** -- featured + proud, karty

---

## 8. Dalsi kroky

1. Oponovat tento brief -- doplnit chybejici pozadavky
2. Navrhnout 2-3 wireframe varianty
3. Vybrat smer
4. Implementovat v Hugo (Go templates + SCSS)
5. Otestovat dark/light, mobile, a11y
6. Deploy
