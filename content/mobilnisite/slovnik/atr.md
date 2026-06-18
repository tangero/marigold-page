---
slug: "atr"
url: "/mobilnisite/slovnik/atr/"
type: "slovnik"
title: "ATR – Answer To Reset"
date: 2025-01-01
abbr: "ATR"
fullName: "Answer To Reset"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/atr/"
summary: "ATR je standardizovaná odpověď odeslaná UICC (Universal Integrated Circuit Card) nebo SIM kartou koncovému zařízení po přijetí resetovacího signálu. Stanovuje počáteční komunikační parametry a potvrzu"
---

ATR je standardizovaná odpověď, kterou UICC nebo SIM karta odešle terminálu po resetu za účelem navázání komunikačních parametrů a potvrzení svého provozního stavu.

## Popis

Odpověď na reset (Answer To Reset, ATR) je klíčový inicializační protokol definovaný ve specifikacích 3GPP, který řídí navázání komunikace mezi koncovým zařízením (např. mobilním telefonem nebo zařízením IoT) a UICC (Universal Integrated Circuit Card) nebo [SIM](/mobilnisite/slovnik/sim/) kartou. Když koncové zařízení přivede na UICC napájení a odešle resetovací signál, UICC odpoví zprávou ATR, která obsahuje zásadní informace o schopnostech karty, komunikačních parametrech a provozních charakteristikách. Tato výměna probíhá na fyzické a elektrické rozhraní a vytváří základ pro veškerou následnou komunikaci mezi terminálem a čipovou kartou.

Struktura zprávy ATR se řídí standardy [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 7816-3 a sestává z více polí, která definují komunikační parametry karty. Patří mezi ně počáteční znak (TS), formátovací bajt (T0), rozhraní bajtů (TA1, TB1, TC1, TD1), historické bajty a kontrolní bajt (TCK). Znak TS udává, zda karta používá pro přenos dat přímou nebo inverzní konvenci. Bajt T0 určuje počet historických bajtů a indikuje přítomnost rozhraní bajtů TA1 až TD1. Rozhraní bajtů definují klíčové parametry, jako je převodní faktor hodinového kmitočtu, požadavky na programovací napětí, hodnoty ochranného času a výběr dalšího typu protokolu.

Z pohledu technické implementace dochází k výměně ATR během procedur studeného nebo teplého resetu, když terminál poprvé napájí UICC. Terminál odešle resetovací puls na lince [RST](/mobilnisite/slovnik/rst/) a UICC odpoví sekvencí ATR na lince I/O. Tento handshake stanoví elektrické charakteristiky, přenosové protokoly (T=0 nebo T=1) a časovací parametry pro následnou výměnu aplikačních protokolových datových jednotek ([APDU](/mobilnisite/slovnik/apdu/)). Historické bajty v rámci ATR mohou obsahovat informace specifické pro kartu, včetně údajů výrobce, schopností karty a podporovaných aplikací, které terminál používá k odpovídající konfiguraci své komunikační vrstvy.

ATR hraje v sítích 3GPP zásadní roli tím, že zajišťuje interoperabilitu mezi různorodými koncovými zařízeními a kartami UICC od více výrobců. Umožňuje terminálu přizpůsobit své komunikační parametry tak, aby odpovídaly specifickým požadavkům vložené karty UICC, čímž podporuje zpětnou i dopřednou kompatibilitu napříč různými generacemi karet. Toto automatické vyjednávání parametrů eliminuje potřebu ruční konfigurace a umožňuje bezproblémový provoz modulů identifikace účastníka napříč různými síťovými technologiemi, od 2G GSM až po 5G NR a dále. Mechanismus ATR také poskytuje počáteční bezpečnostní ověření tím, že potvrzuje správnou odezvu UICC před zahájením citlivých autentizačních procedur.

## K čemu slouží

Protokol odpovědi na reset (ATR) byl vytvořen za účelem stanovení standardizované metody pro inicializaci komunikace mezi koncovými zařízeními a čipovými kartami v systémech mobilní telekomunikace. Před standardizací vytvářely proprietární inicializační protokoly problémy s interoperabilitou mezi zařízeními různých výrobců, což omezovalo flexibilitu síťových operátorů a zvyšovalo náklady na certifikaci zařízení. Protokol ATR, založený na standardech [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 7816, poskytuje univerzální handshake mechanismus, který umožňuje jakémukoli kompatibilnímu terminálu komunikovat s jakoukoli kompatibilní kartou UICC bez ohledu na výrobce.

Primární problém, který ATR řeší, je automatické vyjednávání komunikačních parametrů mezi zařízeními, která mohou mít různé elektrické charakteristiky, časovací požadavky a schopnosti protokolů. Bez této standardizované inicializační sekvence by terminály potřebovaly předem nakonfigurovanou znalost každého možného typu UICC, což by znemožnilo globální roaming a komplikovalo výrobu zařízení. ATR umožňuje UICC deklarovat své schopnosti terminálu, což terminálu umožňuje dynamicky přizpůsobit svou komunikační vrstvu. To je obzvláště důležité, protože technologie UICC se vyvinula od základních [SIM](/mobilnisite/slovnik/sim/) karet až po sofistikované víceaplikační platformy podporující USIM, ISIM a různé přidané služby.

Historicky přijetí ATR ve specifikacích 3GPP (počínaje Release 4) představovalo formalizaci standardů komunikace čipových karet, které již byly v odvětví široce používány. Začleněním standardů ISO/IEC 7816 do specifikací 3GPP organizace zajistila, že autentizace v mobilních sítích a správa identity účastníka zůstanou kompatibilní s širším ekosystémem čipových karet. Tento přístup řešil omezení dřívějších proprietárních řešení a zároveň poskytl základ pro budoucí vylepšení v oblasti zabezpečení, výkonu a funkčnosti, jak se technologie UICC vyvíjela v následujících vydáních 3GPP.

## Klíčové vlastnosti

- Standardizovaná inicializační sekvence podle ISO/IEC 7816-3
- Automatické vyjednávání komunikačních parametrů mezi terminálem a UICC
- Podpora přenosových protokolů T=0 (znakově orientovaný) i T=1 (blokově orientovaný)
- Dynamické přizpůsobení elektrických charakteristik a časovacích parametrů
- Zpětná kompatibilita napříč více generacemi technologie UICC
- Poskytování historických bajtů pro identifikaci karty a indikaci schopností

## Související pojmy

- [SIM – Subscriber Identity Module / Universal Subscriber Identity Module](/mobilnisite/slovnik/sim/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [APDU – Application Protocol Data Unit](/mobilnisite/slovnik/apdu/)

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification

---

📖 **Anglický originál a plná specifikace:** [ATR na 3GPP Explorer](https://3gpp-explorer.com/glossary/atr/)
