---
slug: "ifsd"
url: "/mobilnisite/slovnik/ifsd/"
type: "slovnik"
title: "IFSD – Information Field Size for the Terminal"
date: 2025-01-01
abbr: "IFSD"
fullName: "Information Field Size for the Terminal"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ifsd/"
summary: "IFSD definuje maximální velikost informačního pole, kterou může terminál přijmout v jednom datovém bloku během výměny protokolu T=0 nebo T=1. Jde o klíčový parametr pro komunikaci se čipovou kartou, k"
---

IFSD je maximální velikost informačního pole, kterou může terminál přijmout v jednom datovém bloku během výměny protokolu T=0 nebo T=1 s kartou UICC/SIM.

## Popis

Informační velikost pole pro terminál (IFSD) je základní parametr specifikovaný v 3GPP TS 21.905 pro komunikaci mezi terminálem (mobilním zařízením) a čipovou kartou, konkrétně UICC (Universal Integrated Circuit Card) nebo [SIM](/mobilnisite/slovnik/sim/) (Subscriber Identity Module). Funguje v rámci asynchronních poloduplexních přenosových protokolů [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 7816-3 T=0 a T=1. Hodnota IFSD představuje maximální počet datových bajtů, které je terminál schopen přijmout v jednom bloku od karty. Tento parametr je vyměňován během úvodní procedury Answer-to-Reset ([ATR](/mobilnisite/slovnik/atr/)) nebo prostřednictvím specifického příkazu ([IFS](/mobilnisite/slovnik/ifs/) request) za účelem stanovení výchozího stavu komunikace.

V praxi, když je zahájena relace, karta odešle svůj ATR, který obsahuje navrhovanou hodnotu IFSD od karty. Terminál tuto hodnotu může přijmout nebo navrhnout jinou pomocí vyhrazeného příkazu. Dohodnutá hodnota IFSD je pak použita pro všechny následující dvojice příkaz-odpověď ([APDU](/mobilnisite/slovnik/apdu/)) od karty k terminálu. Tento mechanismus zabraňuje přetečení vyrovnávací paměti v terminálu tím, že zajistí, aby karta neodeslala informační pole větší, než terminál dokáže zpracovat. Správa IFSD je klíčová pro správné parsování složitých odpovědí, jako jsou například ty obsahující obsah souborů nebo seznamy ze souborového systému SIM.

Role IFSD se vztahuje na všechny 3GPP definované aplikace [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module) a SIM. Jde o nízkourovňový, základní prvek rozhraní čipové karty, který podporuje funkce vyšších vrstev, jako je autentizace, správa profilu účastníka a přidané služby. Přestože je pro koncového uživatele často neviditelný, jeho správná implementace je nezbytná pro spolehlivou a bezpečnou interoperabilitu mezi zařízením a kartou a tvoří jádro souladu terminálu s 3GPP specifikacemi pro podporu čipových karet.

## K čemu slouží

IFSD byl zaveden k řešení základního problému interoperability v komunikaci čipových karet: nesouladu kapacit vyrovnávacích pamětí mezi terminály a kartami. Bez dohodnuté maximální velikosti informačního pole by karta mohla odeslat datový blok větší, než dokáže vstupní vyrovnávací paměť terminálu přijmout, což by vedlo k selhání komunikace, poškození dat nebo pádům terminálu. Parametr poskytuje jasnou, standardizovanou metodu, jak se obě entity na začátku relace dohodnou na bezpečné velikosti přenosu dat.

Historicky, jak se čipové karty vyvíjely, aby podporovaly složitější aplikace a větší datové sady (např. pro GSM fáze 2+ a 3G [USIM](/mobilnisite/slovnik/usim/)), stala se potřeba flexibilního, vyjednávaného parametru zřejmou. Dřívější pevné nebo předpokládané velikosti vyrovnávacích pamětí byly nedostatečné. IFSD umožňuje škálovatelnost a budoucí rozvoj, což terminálům s většími vyrovnávacími paměťmi umožňuje efektivně přijímat větší datové bloky, a zároveň zachovává zpětnou kompatibilitu s kartami, které navrhují menší velikosti. Řeší omezení fyzické vrstvy sériového rozhraní tím, že poskytuje mechanismus logického řízení toku dat.

## Klíčové vlastnosti

- Definuje maximální velikost přijatelného datového bloku od karty k terminálu
- Vyjednává se během úvodní procedury Answer-to-Reset (ATR)
- Použitelný pro oba přenosové protokoly T=0 i T=1
- Zabraňuje přetečení vyrovnávací paměti terminálu a zajišťuje integritu dat
- Umožňuje škálovatelnou komunikaci pro karty s různými datovými možnostmi
- Základní pro soulad s ISO/IEC 7816-3 v 3GPP terminálech

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [APDU – Application Protocol Data Unit](/mobilnisite/slovnik/apdu/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [IFSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/ifsd/)
