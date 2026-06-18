# Automatizované generování SVG schémat přes LLM — zjištění a směry výzkumu

> Stav: **průzkumný / rozpracováno**. Tento dokument shrnuje, co jsme zjistili při
> pokusu automatizovaně generovat čitelné technické infografiky pro pojmy slovníku
> 3GPP (`/mobilnisite/slovnik/`), a vytyčuje, co je potřeba dál prozkoumat.
> Cílem je samostatně vyřešit spolehlivé generování **funkčních a čitelných** schémat.

---

## 1. Kontext a cíl

Slovník 3GPP má ~2750 pojmů bez vizuálů. Uživatel ručně vyrobil jednu infografiku
(`acelp.jpg`, přes ChatGPT obrazový model) a chce stejný typ schématu automatizovat
pro ručně vybranou sadu nejdůležitějších pojmů (AMF, 5GC, NSSF, network slicing…).

Požadavky na výstup:
- technické schéma (bloky, šipky, datové toky), ne dekorativní obrázek
- **bezchybná čeština** včetně diakritiky
- jednotný vizuální styl napříč desítkami pojmů
- čitelné na webové stránce pojmu

---

## 2. Cesta a klíčová rozhodnutí (chronologicky)

### 2.1 Obrazový model (gpt-image-1) — ZAMÍTNUTO
První pokus: OpenAI `gpt-image-1` generoval rastrovou infografiku z textového promptu.

- **Funguje:** vizuální styl, kompozice, barevná legenda — model si hodně domyslí.
- **Fatální problém:** text se renderuje jako **pixely**, ne znaky. Anglicky obstojně,
  ale **českou diakritiku konzistentně komolí** (á/č/ř/ž/í) — a žádný prompt to spolehlivě
  neopraví, protože model „kreslí" tvary, ne sází text. Ověřeno na pilotu AMF
  (např. „úputorizace jeji přečes a k niti" v legendě).
- Náklady: ~0,04–0,17 $/obrázek.

**Závěr:** obrazové modely jsou pro česky popsaná technická schémata nevhodné.

### 2.2 LLM generuje SVG — ZVOLENO
Místo rastru nechat LLM vygenerovat **SVG kód**. Text je pak nativní → **bezchybná
čeština**, ostré škálování, malé soubory (4–10 KB), editovatelné.

Dvoukrokový pipeline (skript `scripts/generate_infographics.py`):
1. **Destilace**: z českého popisu pojmu (markdown) → strukturovaná osnova diagramu
   (číslovaný seznam komponent zleva doprava + toky + parametry).
2. **Vykreslení**: osnova → SVG diagram podle pevného „house-style" promptu.

### 2.3 Model pro SVG: qwen vs Sonnet
- **qwen/qwen3-max**: validní SVG, ale **nedeterministický layout** — text přetékal
  z bloků, kvalita kolísala mezi běhy. Nevhodné.
- **anthropic/claude-sonnet-4-6**: výrazně lepší — drží prostorová omezení, bohatší
  a přesnější diagramy, bez přetékání. **Zvoleno jako výchozí.**

Destilaci (krok 1) i vykreslení (krok 2) dělá stejný model přes OpenRouter.

---

## 3. Co funguje

- **Čeština je bezchybná** — hlavní výhra SVG přístupu. Diakritika, dlouhá slova, vše OK.
- **Jednotný styl** — pevný house-style prompt (paleta `#2563EB` modrá / `#EA580C`
  oranžová / `#16A34A` zelená, layout zleva doprava, legenda, titulek + podtitulek)
  drží konzistentní vizuální jazyk napříč pojmy.
- **Destilace obsahu** (qwen i Sonnet) z českého popisu funguje dobře — vytvoří
  smysluplnou osnovu komponent, toků a parametrů.
- **Čitelnost po dvou opatřeních:**
  - **větší písmo v SVG** (min. 24px popisky / 30px bloky / 46px titulek; původně 13–14px,
    což po zmenšení na šířku stránky dávalo ~7px — nečitelné),
  - **širší zobrazení na stránce** — breakout z úzkého textového sloupce (`.container`
    max-width 800px) na `min(1100px, 96vw)`, vycentrováno (viz `assets/scss/main.scss`,
    `.slovnik-infografika`).
- **Zobrazení bez front-matter pole** — layout `layouts/slovnik/single.html` odvozuje
  obrázek z názvu souboru přes `fileExists` (`static/assets/slovnik/<slug>.{svg,jpg,png}`),
  takže se napojení **nemůže ztratit** při přegenerování slovníku. (Předchozí varianta
  s polem `infografika:` ve front matteru se ztrácela, když generátor markdownu pojem přepsal.)
- **Sanitizace SVG** — odstranění XML komentářů (model do nich občas vkládá `--`,
  což je nevalidní XML a rozbije render).

---

## 4. Co NEfunguje spolehlivě (otevřené problémy)

### 4.1 Kolize popisků a šipek (hlavní problém)
LLM umisťuje text a čáry na **fixní souřadnice bez kontroly kolizí**. Výsledek:
- popisky šipek se překrývají s bloky („Datová relace (N29)" přes blok NSSF v AMF),
- šipky procházejí **skrz** bloky, které jim stojí v cestě (strukturní chyba rozmístění),
- občas stlačený layout (NSSF — nízká výška obsahu → po zmenšení nečitelné).

Anti-kolizní pravidla v promptu (vyhrazené y-zóny, min. odstupy, „mentálně zkontroluj
překryvy") **výrazně pomohla** — z „spousta kolizí" na „obvykle 1 drobná" — ale
**100 % nedosáhnou**. LLM nemá skutečnou geometrickou zpětnou vazbu.

### 4.2 Nedeterminismus
Každý běh dopadne jinak: stejný pojem jednou čistý, podruhé s kolizí. Bez verifikační
smyčky nelze zaručit kvalitu.

### 4.3 Faktická přesnost detailů
Model občas zamění číslo rozhraní (např. dvakrát „N12") — destilace to zmírnila,
ale ne odstranila.

### 4.4 Stav pilotu (3 pojmy, model Sonnet)
- **5gc** — po **ruční** úpravě jednoho popisku čistý a reprezentativní.
- **amf** — strukturní vada: šipka SMF→PDU relace prochází přes blok NSSF, popisek N29 koliduje.
- **nssf** — stlačený layout, text v horní části se tlačí.

→ Tj. ze 3 jen 1 čistý bez ruční práce. Kvalita kolísá.

---

## 5. Směry k dalšímu prozkoumání

Seřazeno zhruba od nejslibnějšího:

1. **Verifikační smyčka (render → zpětná vazba → oprava).**
   Vygenerovat SVG → vyrenderovat na bitmapu (`rsvg-convert`, k dispozici lokálně) →
   poslat obrázek zpět LLM (vision) s dotazem „označ kolize/přetékání a oprav SVG" →
   iterovat, dokud čisté. Tohle dává modelu chybějící geometrickou zpětnou vazbu.
   Případně programová detekce kolizí (bounding-boxy `<rect>` vs `<text>`) bez LLM.

2. **Best-of-N + automatický výběr.**
   Vygenerovat N variant, programově skórovat (počet překryvů bounding-boxů) a vybrat
   nejlepší. Obchází nedeterminismus za cenu více volání.

3. **Layout engine místo volného SVG.**
   Nechat LLM vygenerovat jen **graf** (uzly + hrany + popisky) ve strukturovaném
   formátu (Mermaid / Graphviz DOT / JSON) a layout spočítat deterministickým enginem
   (Graphviz `dot`, ELK, Mermaid). Engine řeší rozmístění a hrany bez kolizí; LLM řeší
   jen obsah. Kompromis: méně volný vizuální styl, nutný build krok / renderer.
   **Pozn.:** Mermaid je v projektu dostupný (MCP `mcp__claude_ai_Mermaid_Chart`),
   stojí za otestování kvality výstupu pro tyto diagramy.

4. **Šablonové layouty pro typové diagramy.**
   Většina 3GPP schémat má pár archetypů (hvězda kolem centrální funkce; lineární
   signal flow; protokolový zásobník; sekvenční diagram). Připravit parametrizovatelné
   SVG/HTML šablony a LLM jen plní obsah do slotů. Nejvyšší konzistence, nejmíň volnosti.

5. **Hybrid: SVG diagram bez textu + HTML/SVG overlay popisků.**
   LLM/engine udělá geometrii (bloky, šipky), popisky se vykreslí jako samostatná
   textová vrstva s CSS pozicováním (žádné přetékání, plná typografická kontrola).

6. **Doladění house-style promptu** (krátkodobé zlepšení bez architektonické změny):
   tvrdší pravidla na rozestupy, povinné zalomení dlouhých popisků, zákaz vést šipku
   přes blok (směrovat kolem), explicitnější popisky (např. „Oddělení řídicí (CP) a
   uživatelské (UP) roviny" místo zkratkového „oddělení / CP / UP").

---

## 6. Reference na současný stav v repu

| Co | Kde |
|----|-----|
| Generátor (Python, 2 kroky, OpenRouter/Sonnet) | `scripts/generate_infographics.py` |
| Allowlist pojmů | `scripts/infographic-terms.txt` (amf, 5gc, nssf) |
| Pilotní SVG | `static/assets/slovnik/{amf,5gc,nssf}.svg` |
| Ruční pilot (rastr, referenční styl) | `static/assets/slovnik/acelp.jpg` |
| Zobrazení (odvození z názvu souboru) | `layouts/slovnik/single.html` |
| Styly (breakout šířka, dark mode) | `assets/scss/main.scss` → `.slovnik-infografika` |
| Python prostředí | `.venv-img/` (gitignorováno; `openai`, `python-dotenv`) |
| Klíče | `.env` → `OPENROUTER_API_KEY` (Sonnet/qwen), `OPENAI_API_KEY` (nepoužито po přechodu na SVG) |

### Spuštění
```bash
.venv-img/bin/python scripts/generate_infographics.py --dry-run        # náhled osnov
.venv-img/bin/python scripts/generate_infographics.py --only amf       # jeden pojem
.venv-img/bin/python scripts/generate_infographics.py --force          # přegenerovat vše z allowlistu
.venv-img/bin/python scripts/generate_infographics.py --model anthropic/claude-sonnet-4-6
# render náhledu na bitmapu:
rsvg-convert -w 1100 static/assets/slovnik/amf.svg -o /tmp/amf.png
```

---

## 7. Doporučení

Pro produkční nasazení na desítky pojmů **nestačí samotný prompt** — kvalita kolísá a
ruční dolaďování každého SVG je pracné. Nejslibnější je **verifikační smyčka** (bod 5.1)
nebo **layout engine** (bod 5.3). Než bude jeden z nich ověřen, držet generování jen na
ručně vybraných pojmech s **ruční vizuální kontrolou a doladěním** každého výstupu.

Bezchybná čeština a jednotný styl jsou vyřešené — zbývá vyřešit **spolehlivý layout bez kolizí**.
