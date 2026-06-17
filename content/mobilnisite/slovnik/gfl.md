---
slug: "gfl"
url: "/mobilnisite/slovnik/gfl/"
type: "slovnik"
title: "GFL – Generic Frequency List"
date: 2025-01-01
abbr: "GFL"
fullName: "Generic Frequency List"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gfl/"
summary: "Standardizovaný seznam rádiových frekvencí používaný pro síťové skenování a měření v mobilních zařízeních. Umožňuje efektivní procedury výběru, převýběru a předání spojení tím, že poskytuje strukturov"
---

GFL (Generic Frequency List) je standardizovaný seznam rádiových frekvencí používaný mobilními zařízeními pro síťové skenování, měření a efektivní procedury výběru buňky nebo předání spojení.

## Popis

Generic Frequency List (GFL) je základní datová struktura definovaná ve specifikacích 3GPP, která poskytuje mobilnímu zařízení (User Equipment, UE) prioritizovanou sadu kmitočtů nosných pro monitorování za účelem hledání buněk a měření. Je to klíčová součást procedur mobility v režimu volnoběhu a připojeném režimu, která navádí rádiový přijímač UE k efektivnímu skenování rádiového spektra bez vyčerpávajícího, energeticky náročného prohledávání všech možných pásem. Seznam je typicky vysílán obsluhující buňkou v blocích systémových informací (SIB) nebo poskytován prostřednictvím vyhrazené signalizace [RRC](/mobilnisite/slovnik/rrc/) a může být strukturován podle technologie rádiového přístupu (RAT), jako je [E-UTRA](/mobilnisite/slovnik/e-utra/) nebo UTRA, a podle kmitočtového pásma.

Architektonicky je GFL spravován vrstvou řízení rádiových zdrojů (RRC) v síti a implementován v protokolovém zásobníku UE. Síť sestavuje seznam na základě své topologie nasazení, konfigurace sousedních buněk a politik operátora. Když UE přijme GFL, použije tyto informace ke konfiguraci mezer pro měření na fyzické vrstvě nebo měřicích cyklů v režimu volnoběhu. UE následně provádí měření úrovně a kvality signálu (např. RSRP, RSRQ pro LTE) na uvedených frekvencích a hlásí je zpět síti nebo je používá pro autonomní rozhodování o převýběru buňky.

Role GFL je klíčová pro plynulou mobilitu. V režimu volnoběhu umožňuje UE najít a připojit se k nejlepší dostupné buňce s ohledem na faktory jako síla signálu nebo stav zákazu buňky. V připojeném režimu podporuje přípravu předání spojení tím, že umožňuje síti vyžádat si měření na specifických cílových frekvencích, což vede k rychlejším a spolehlivějším předáním. Seznam může také zahrnovat frekvence pro mobilitu mezi různými RAT, usnadňující přechody např. mezi sítěmi LTE a WCDMA. Strukturou prohledávaného prostoru GFL významně snižuje spotřebu baterie UE a urychluje objevování buněk ve srovnání s neřízeným skenováním, což je zásadní pro uživatelský zážitek a efektivitu sítě.

## K čemu slouží

Generic Frequency List byl vytvořen, aby řešil neefektivitu a zhoršení výkonu spojené s neřízeným nebo vyčerpávajícím skenováním frekvencí mobilními zařízeními. Rané celulární systémy často vyžadovaly, aby UE skenovala široké pásmo rádiového spektra, aby našla vhodné buňky. Tento proces byl časově náročný, energeticky intenzivní a mohl vést ke zpožděnému výběru buňky nebo nezdařeným předáním spojení, zejména v hustých nebo více-RAT síťových prostředích. GFL poskytuje mechanismus inteligentního skenování řízeného sítí.

Jeho zavedení, zvláště zdůrazňované od 3GPP Release 8 s nástupem LTE, bylo motivováno rostoucí složitostí sítí rádiového přístupu. Operátoři začali nasazovat více kmitočtových pásem (např. pro vrstvy kapacity a pokrytí) a více RAT (2G, 3G, 4G). Bez řízeného seznamu by autonomní hledání UE mohlo být suboptimální, což by potenciálně vedlo k přetížení některých buněk při nevyužití jiných. GFL umožňuje síťovému operátorovi řídit a optimalizovat měřicí chování UE, nasměrovat jej na nejrelevantnější frekvence na základě aktuálního zatížení sítě, strategie nasazení a uživatelského předplatného.

Toto řeší klíčové problémy v řízení mobility: minimalizuje dobu přerušení služby během předání spojení, zvyšuje pravděpodobnost úspěšného předání tím, že zajistí, aby UE měřila správné kandidátské buňky, a zlepšuje celkový výkon sítě umožněním vyrovnávání zatížení napříč nosnými a technologiemi. Je to základní prvek pro funkce jako agregace nosných nebo objevování malých buněk řízené sítí, kde je přesná znalost frekvencí nezbytná.

## Klíčové vlastnosti

- Poskytuje strukturovaný, prioritizovaný seznam kmitočtů nosných pro měření UE
- Podporuje organizaci podle RAT a podle kmitočtového pásma
- Snižuje spotřebu energie UE eliminací neřízeného skenování
- Umožňuje rychlejší provedení výběru, převýběru a předání spojení
- Může být doručen prostřednictvím vysílaných systémových informací nebo vyhrazené signalizace RRC
- Usnadňuje správu mobility a vyrovnávání zatížení řízené sítí

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 42.056** (Rel-19) — GSM Cordless Telephony System (CTS)
- **TS 43.052** (Rel-19) — GSM Cordless Telephony System (CTS) Radio Interface
- **TS 45.056** (Rel-19) — GSM CTS-FP Radio Requirements

---

📖 **Anglický originál a plná specifikace:** [GFL na 3GPP Explorer](https://3gpp-explorer.com/glossary/gfl/)
