---
slug: "eop"
url: "/mobilnisite/slovnik/eop/"
type: "slovnik"
title: "EOP – Earth Orientation Parameters"
date: 2025-01-01
abbr: "EOP"
fullName: "Earth Orientation Parameters"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/eop/"
summary: "Parametry popisující orientaci Země vůči nebeské referenční soustavě. Jsou klíčové pro přesné satelitní polohovací systémy, jako je GNSS, a umožňují přesnou konverzi mezi pozemskými a kosmickými souřa"
---

EOP je soubor parametrů popisujících orientaci Země vůči nebeské soustavě, který umožňuje přesnou převod souřadnic pro satelitní polohování v mobilních sítích.

## Popis

Parametry orientace Země (EOP) jsou souborem časově proměnných měření, která definují orientaci zemské osy v prostoru. Popisují nepravidelnosti v rotaci Země, včetně jevů jako precese, nutace a pohyb pólů. V kontextu norem 3GPP se data EOP používají primárně polohovými službami, zejména těmi, které využívají globální navigační satelitní systémy ([GNSS](/mobilnisite/slovnik/gnss/)), jako jsou [GPS](/mobilnisite/slovnik/gps/), Galileo nebo BeiDou. Tyto parametry jsou nezbytné pro transformaci souřadnic mezi pozemskou referenční soustavou (používanou pro mapování a určení polohy uživatele) a nebeskou referenční soustavou (používanou satelity pro určování oběžné dráhy).

Z architektonického hlediska jsou data EOP distribuována uživatelskému zařízení (UE) nebo polohovým serverům za účelem zvýšení přesnosti polohových výpočtů. V operacích asistovaného GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)) může polohový server poskytnout data EOP uživatelskému zařízení jako součást asistenčních dat, což umožní zařízení provádět přesnější korekce satelitních drah a hodin. Uživatelské zařízení tyto parametry využívá ve svých polohovacích algoritmech pro zohlednění variace v rotaci Země, které by, pokud by nebyly korigovány, mohly způsobit chyby v řádu metrů ve vypočtené poloze. Proces zahrnuje aplikaci komplexních transformačních matic, které zahrnují hodnoty EOP, aby sladily vysílaná efemeridní data satelitu se skutečnou orientací Země v čase měření.

Klíčové komponenty související s EOP v 3GPP zahrnují LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) a NR Positioning Protocol (NRPP), které přenášejí asistenční data mezi polohovým serverem (např. Enhanced Serving Mobile Location Center - [E-SMLC](/mobilnisite/slovnik/e-smlc/) nebo Location Management Function - [LMF](/mobilnisite/slovnik/lmf/)) a uživatelským zařízením. Specifikace jako 36.355 a 37.355 definují informační prvky a kódování pro asistenční data GNSS, která mohou zahrnovat EOP. Data [EP](/mobilnisite/slovnik/ep/) obvykle zahrnují parametry jako složky x a y pohybu pólů, rozdíl mezi univerzálním časem ([UT1](/mobilnisite/slovnik/ut1/)) a koordinovaným světovým časem (UTC) známý jako UT1-UTC, a odchylky nebeského pólu. Integrací těchto parametrů dosahují polohové služby 3GPP vyšší přesnosti, což je klíčové pro aplikace jako lokalizace nouzových volání, autonomní vozidla a precizní zemědělství.

## K čemu slouží

EOP byly začleněny do norem 3GPP, aby řešily potřebu vysoce přesného polohování v celulárních sítích. Jak se požadavky na služby založené na poloze a lokalizaci nouzových hovorů zpřísňovaly, staly se zjevnými omezení samostatného GNSS. Faktory jako atmosférická zpoždění, chyby satelitních hodin a nerigidní rotace Země přispívají k nepřesnostem polohování. Zatímco jiné zdroje chyb jsou často korigovány pomocí modelů nebo datových proudů v reálném čase, změny orientace Země jsou méně předvídatelné a vyžadují externí parametry.

Zařazení EOP do asistenčních dat řeší problém degradace přesnosti polohování způsobený dynamickou orientací Země. Bez těchto parametrů by převod mezi referenční soustavou satelitu a polohou uživatele na Zemi byl založen na zjednodušeném, statickém modelu Země, což by vedlo k chybám, které se v čase zvětšují. Poskytnutím EOP umožňuje 3GPP přesnější asistovaný GNSS, což je zásadní pro splnění regulatorních požadavků na lokalizaci nouzových volajících (např. E911 v USA) a pro podporu pokročilých komerčních služeb vyžadujících přesnost na úrovni decimetrů nebo centimetrů.

## Klíčové vlastnosti

- Umožňuje přesnou transformaci mezi nebeskými a pozemskými referenčními soustavami
- Přenášeny jako součást asistenčních dat GNSS prostřednictvím protokolů LPP/NRPP
- Zahrnují parametry pro pohyb pólů a časový rozdíl UT1-UTC
- Zvyšuje přesnost polohování pro režimy A-GNSS a samostatného GNSS
- Podporuje více konstelací GNSS (GPS, Galileo, GLONASS, BeiDou)
- Nezbytné pro vysoce přesné polohové služby a nouzové určování polohy

## Definující specifikace

- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [EOP na 3GPP Explorer](https://3gpp-explorer.com/glossary/eop/)
