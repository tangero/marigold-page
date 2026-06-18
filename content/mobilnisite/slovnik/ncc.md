---
slug: "ncc"
url: "/mobilnisite/slovnik/ncc/"
type: "slovnik"
title: "NCC – Network (PLMN) Colour Code"
date: 2025-01-01
abbr: "NCC"
fullName: "Network (PLMN) Colour Code"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ncc/"
summary: "3bitový identifikátor používaný k rozlišení veřejných pozemních mobilních sítí (PLMN), které sdílejí stejný kód lokální oblasti (LAC) nebo směrovací oblasti (RAC). Je zásadní pro procedury výběru sítě"
---

NCC je 3bitový síťový barevný kód, který rozlišuje mezi různými PLMN sdílejícími stejný kód lokální oblasti (LAC) nebo směrovací oblasti (RAC). Je klíčový pro výběr sítě a předávání hovorů.

## Popis

Síťový barevný kód (NCC) je základní identifikátor v architektuře systémů GSM, UMTS a LTE. Jedná se o 3bitový kód (hodnoty 0–7), který je kombinován s barevným kódem základnové stanice ([BCC](/mobilnisite/slovnik/bcc/)) za vzniku 6bitového [BSIC](/mobilnisite/slovnik/bsic/) (Base Station Identity Code) pro GSM/UMTS, nebo je používán v souvisejících procedurách identifikace sítě. Jeho hlavní úlohou je poskytnout druhou úroveň rozlišení sítí vedle kombinace mobilního kódu země ([MCC](/mobilnisite/slovnik/mcc/)) a mobilního kódu sítě ([MNC](/mobilnisite/slovnik/mnc/)). Když mobilní stanice provádí měření na vysílacích řídicích kanálech (jako [BCCH](/mobilnisite/slovnik/bcch/) v GSM nebo příslušné signály v novějších systémech), dekóduje BSIC nebo ekvivalentní informaci a extrahuje NCC. To umožňuje zařízení rozlišit buňky patřící jeho domovské [PLMN](/mobilnisite/slovnik/plmn/), partnerské roamující PLMN nebo zakázané síti, i když tyto sítě používají ve stejné geografické oblasti stejný [LAC](/mobilnisite/slovnik/lac/)/[RAC](/mobilnisite/slovnik/rac/). Toto rozlišení je zásadní pro spolehlivý převýběr buňky a předání hovoru.

Provozně je NCC vysílán buňkou jako část systémové informace. Vrstvy NAS (Non-Access Stratum) a AS (Access Stratum) mobilní stanice používají tuto informaci spolu s uloženým seznamem preferovaných a zakázaných PLMN. Například při výběru/převýběru buňky, pokud buňka vysílá NCC odpovídající zakázané PLMN, mobilní stanice tuto buňku vyloučí z úvahy, i když jsou rádiové podmínky příznivé. Tím se zabrání připojení nebo předání hovoru k neautorizované nebo nežádoucí síti. Ve scénářích sdílení sítě, jako je MORAN (Multiple Operator Radio Access Network) nebo MOCN (Multi-Operator Core Network), mohou různí operátoři jádrové sítě sdílet stejnou infrastrukturu přístupové sítě. NCC (spolu s PLMN-ID) je klíčový parametr, který umožňuje jedné buňce vysílat více síťových identit, což umožňuje zařízením z různých předplatitelských sítí identifikovat a vybrat správnou jádrovou síť.

Specifikace NCC je rozprostřena napříč více technickými specifikacemi 3GPP (TS). TS 24.008 a TS 44.018 detailně popisují jeho použití v GSM, zatímco TS 25.331 pokrývá UMTS. V kontextu LTE a NR se jeho konceptuální použití vyvíjí, ale princip identifikace sítě přetrvává prostřednictvím parametrů jako identita PLMN a kódy sledovacích oblastí, přičemž legacy koncepty ovlivňují procedury. TS 23.122 popisuje pravidla pro výběr PLMN, která inherentně spoléhají na identifikátory jako NCC. Z bezpečnostního hlediska, jak je uvedeno v TS 33.401, je správná identifikace sítě prvním krokem v oboustranné autentizaci, která brání zařízením v připojení k falešným základnovým stanicím, jež by se mohly vydávat za platnou síť, ale používaly by nesprávný nebo neočekávaný NCC.

## K čemu slouží

NCC byl zaveden k řešení praktického problému jednoznačné identifikace sítě v geograficky překrývajících se oblastech. Hlavní identifikátor PLMN, kombinace MCC+MNC, je globálně unikátní, ale v rámci jedné lokální oblasti může být přítomno více operátorů. Samotný kód lokální oblasti (LAC) k jejich rozlišení nestačí. NCC poskytuje jednoduchý, lokálně významný kód pro jejich odlišení. To bylo motivováno zejména potřebou efektivního roamingu a sdílení sítě. Bez NCC by se mobilní zařízení mohlo nesprávně pokusit připojit k buňce nebo na ni předat hovor ze sítě jiného operátora používajícího stejný LAC, což by vedlo k neúspěšným pokusům o registraci, narušení služeb nebo zbytečné signalizační zátěži.

Historicky, jak se sítě GSM rozšiřovaly a pohraniční regiony mezi zeměmi nebo mezi konkurenčními operátory v rámci země stávaly složitějšími, se projevilo omezení pouhého použití MCC+MNC a LAC. NCC přidal potřebnou granularitu. Navíc nástup obchodních modelů sdílení sítě (např. sdílení věží, sdílení RAN) vytvořil scénář, kdy jediná fyzická lokalita buňky musí logicky reprezentovat více operátorů. NCC jako část vysílané systémové informace toto virtuální oddělení umožňuje, což dovoluje jedné rádiové buňce inzerovat se jako patřící několika PLMN, z nichž každá může mít přiřazenou jinou hodnotu NCC sdílenou s MNC. To přímo podporuje snížení nákladů na infrastrukturu při zachování nezávislých síťových identit pro každého operátora.

## Klíčové vlastnosti

- 3bitový identifikátor (hodnoty 0–7)
- Kombinován s BCC za vzniku plného BSIC (Base Station Identity Code)
- Vysílán v systémové informaci buňky (např. na BCCH)
- Používán pro rozlišení PLMN při výběru a převýběru buňky
- Kritický pro rozhodování o předání hovoru v pohraničních oblastech
- Umožňuje scénáře sdílení sítě (MOCN, MORAN) tím, že rozlišuje jádrové sítě na sdíleném rádiu

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [BSIC – Base transceiver Station Identity Code](/mobilnisite/slovnik/bsic/)
- [LAC – L2TP Access Concentrator](/mobilnisite/slovnik/lac/)
- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.843** (Rel-15) — Security Study for ProSe UE-to-Network Relay
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [NCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ncc/)
