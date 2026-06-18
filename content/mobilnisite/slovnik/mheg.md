---
slug: "mheg"
url: "/mobilnisite/slovnik/mheg/"
type: "slovnik"
title: "MHEG – Multimedia and Hypermedia Information Coding Expert Group"
date: 2025-01-01
abbr: "MHEG"
fullName: "Multimedia and Hypermedia Information Coding Expert Group"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mheg/"
summary: "Standard pro interaktivní multimediální aplikace, původně vyvinutý pro služby digitální televize. Definuje formát pro vytváření a prezentaci interaktivního obsahu, jako jsou elektronické programové pr"
---

MHEG je standard 3GPP pro interaktivní multimediální aplikace, původně vyvinutý pro služby digitální televize, jako jsou elektronické programové průvodce, a byl předchůdcem moderních webových technologií v oblasti vysílání.

## Popis

MHEG je standard [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) (ISO/IEC 13522), který specifikuje formát a engine pro interaktivní multimediální aplikace, často používané ve vysílacím prostředí, jako je digitální televize. V kontextu 3GPP byl odkazován pro možnou interoperabilitu multimediálních služeb, ačkoli jeho hlavní nasazení bylo ve vysílání. Jádrem MHEG je objektový model MHEG. Aplikace MHEG neboli 'scéna' se skládá ze souboru objektů, které jsou staženy a interpretovány engine MHEG (virtuálním strojem) v přijímači, například v set-top boxu pro digitální [TV](/mobilnisite/slovnik/tv/). Mezi klíčové typy objektů patří aplikační objekt (kořen), scénové objekty (jednotlivé obrazovky), prezentační objekty (viditelné prvky jako Text, Obdélník, Bitmapa, Video a Tlačítko), linkové objekty (pro definování interaktivity a navigace) a skriptové objekty (pro jednoduchou procedurální logiku). Tyto objekty mají atributy a chování definované ve standardu. Aplikace je typicky doručována jako karusel v rámci vysílacího transportního proudu, což umožňuje přijímači přístup k potřebným objektům. Engine MHEG tyto objekty parsuje, vytváří scénograf, vykresluje viditelné prvky na obrazovku a spravuje interakci uživatele prostřednictvím dálkového ovládání. Například stisknutí červeného tlačítka na ovladači může aktivovat linkový objekt, který způsobí, že engine přejde k novému scénovému objektu a zobrazí interaktivní sportovní výsledkovou tabuli. Široce přijímaný profil MHEG-5 se zaměřoval na odlehčený, deklarativní přístup vhodný pro přijímače s omezenými prostředky, bez nutnosti složitého skriptování. Používal paradigma událost-akce, kde uživatelské nebo systémové události (jako vypršení časovače) spouštěly předdefinované akce (jako přehrání videa). Ačkoli se nejedná o programovací jazyk v pravém slova smyslu, poskytoval standardizovaný způsob vytváření synchronizovaných, interaktivních prezentací kombinujících grafiku, text a video. V 3GPP byl MHEG zvažován jako součást raných rámců multimediálních služeb (jako [MMS](/mobilnisite/slovnik/mms/)) pro standardizaci prezentačních formátů, ale jeho přímá implementace v mobilních sítích byla ve srovnání s pozdějšími technologiemi, jako je SVG-T nebo [SMIL](/mobilnisite/slovnik/smil/), omezená.

## K čemu slouží

MHEG byl vytvořen, aby řešil potřebu standardizovaného, platformně nezávislého formátu pro interaktivní multimediální aplikace, primárně pro vznikající trh digitální televize v 90. letech. Před MHEG byly interaktivní televizní služby proprietární, což uzamklo vysílatele a spotřebitele do ekosystémů konkrétních dodavatelů. Toto roztříštění bránilo růstu interaktivních služeb. MHEG to chtěl vyřešit poskytnutím otevřeného mezinárodního standardu, který by umožnil, aby aplikace vytvořená jednou běžela na jakémkoli kompatibilním přijímači od libovolného výrobce. Jeho návrh byl motivován omezeními vysílacích přijímačů: omezená paměť, výpočetní výkon a jednoduché vstupní zařízení (dálkový ovladač). Proto byl MHEG-5 záměrně deklarativní a odlehčený, aby se vyhnul potřebě plnohodnotného skriptovacího enginu. Umožnil první generaci interaktivních služeb digitální [TV](/mobilnisite/slovnik/tv/), jako jsou elektronické programové průvodce ([EPG](/mobilnisite/slovnik/epg/)), teletext v digitální podobě (náhrada za Ceefax/Teletext) a jednoduché aplikace 'červeného tlačítka'. V oblasti 3GPP byl MHEG odkazován v raných verzích (od Rel-4) jako součást zkoumání standardizovaných formátů pro multimediální zprávy a prezentaci s cílem konvergence mezi telekomunikačními a vysílacími službami. Vývoj webu ([HTML](/mobilnisite/slovnik/html/), JavaScript) a výkonnější mobilní zařízení však nakonec učinily tyto technologie vhodnějšími pro mobilní interaktivní služby, což omezilo roli MHEG v 3GPP především na historický referenční bod pro koncepty interoperability multimediálních aplikací.

## Klíčové vlastnosti

- Deklarativní objektově orientovaný model pro definování interaktivních multimediálních scén
- Standardizovaná sada prezentačních objektů (Text, Bitmapa, Obdélník, Video, Tlačítko) pro tvorbu uživatelského rozhraní
- Model událost-akce pro definování interaktivity (např. při výběru uživatele přechod na novou scénu)
- Mechanismus doručování založený na karuselu, vhodný pro vysílací transportní proudy (jako DVB)
- Odlehčený profil MHEG-5 navržený pro set-top boxy s omezenými prostředky
- Platformně nezávislý aplikační formát umožňující interoperabilitu na různém hardwaru přijímačů

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [SMIL – Synchronized Multimedia Integration Language](/mobilnisite/slovnik/smil/)
- [SVG – Scalable Vector Graphics](/mobilnisite/slovnik/svg/)
- [DVB – Digital Video Broadcasting](/mobilnisite/slovnik/dvb/)
- [EPG – Electronic Program Guide](/mobilnisite/slovnik/epg/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.960** (Rel-4) — UMTS Mobile Multimedia Technical Challenges

---

📖 **Anglický originál a plná specifikace:** [MHEG na 3GPP Explorer](https://3gpp-explorer.com/glossary/mheg/)
