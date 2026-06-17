---
slug: "mdsr"
url: "/mobilnisite/slovnik/mdsr/"
type: "slovnik"
title: "MDSR – Modified Dual Symbol Rate"
date: 2025-01-01
abbr: "MDSR"
fullName: "Modified Dual Symbol Rate"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mdsr/"
summary: "Modulační technika zavedená v rámci vývoje GSM/EDGE pro zvýšení přenosových rychlostí úpravou symbolové rychlosti a tvarováním impulsu. Zlepšuje spektrální účinnost a podporuje vyšší modulace jako 16-"
---

MDSR je modulační technika pro GSM/EDGE, která zvyšuje přenosové rychlosti a spektrální účinnost úpravou symbolové rychlosti a tvarováním impulsu, aby umožnila vyšší modulace v rámci stávajících šířek přenosového pásma.

## Popis

Modified Dual Symbol Rate (MDSR) je vylepšení fyzické vrstvy definované ve specifikaci 3GPP TS 45.912 pro vývoj GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Funguje tak, že modifikuje základní symbolovou rychlost a používá pokročilé filtry pro tvarování impulsu, konkrétně modifikovaný Gaussův tvar impulsu, aby lépe využila dostupné spektrum. To umožňuje přenos více symbolů za sekundu ve stejném 200 kHz pásmu nosné používaném v tradičním GSM, čímž se zvyšuje hrubá přenosová rychlost bez rozšíření šířky kanálu. Tato technika je klíčovou součástí funkcí Enhanced Data rates for GSM Evolution (EDGE) a EDGE Evolution, která umožňuje vyšší spektrální účinnost a podporuje zavedení schémat vyšších modulací.

Z architektonického hlediska MDSR ovlivňuje návrh vysílače a přijímače v základnové stanici ([BTS](/mobilnisite/slovnik/bts/)) a mobilní stanici ([MS](/mobilnisite/slovnik/ms/)). Vysílač zahrnuje modifikovaný filtr pro tvarování impulsu ke snížení mezisymbolového rušení ([ISI](/mobilnisite/slovnik/isi/)) a emisí mimo pásmo, což je zásadní při práci s vyššími symbolovými rychlostmi. Přijímač musí používat ekvalizéry schopné pracovat s modifikovaným časováním symbolů a výslednými charakteristikami kanálu. MDSR je navržena tak, aby byla do určité míry zpětně kompatibilní se staršími terminály GSM/EDGE, přičemž pro plné využití výhod často vyžaduje podporu vylepšených funkcí v síti i zařízeních. Funguje ve spojení s dalšími vylepšeními, jako je vyšší symbolová rychlost ([HSR](/mobilnisite/slovnik/hsr/)) a downlink s dvěma nosnými, aby posunula teoretické špičkové přenosové rychlosti v GERAN za hranice klasického EDGE.

V síti je úlohou MDSR poskytnout cenově efektivní cestu upgradu pro operátory GSM, což jim umožňuje dosáhnout vyšších přenosových rychlostí a lepšího uživatelského zážitku bez nutnosti nového spektra nebo kompletní přestavby sítě. Je součástí souboru funkcí v rámci pracovní položky vývoje GERAN, jejímž cílem bylo udržet GSM konkurenceschopné vůči vznikajícím technologiím 3G a později 4G v oblasti datových služeb, zejména na trzích, kde bylo spektrum GSM hojné, ale přeřazení pro UMTS/LTE nebylo okamžitě proveditelné. Implementace zahrnuje aktualizace základnového pásma v síťových i uživatelských zařízeních, které podléhají přísným požadavkům na výkon, aby bylo zajištěno soužití se staršími signály.

## K čemu slouží

MDSR byla vytvořena, aby řešila rostoucí poptávku po vyšších mobilních datových rychlostech v rámci omezení stávajících přidělení spektra GSM. Před jejím zavedením klasický GSM a dokonce i standardní [EDGE](/mobilnisite/slovnik/edge/) (používající [8-PSK](/mobilnisite/slovnik/8-psk/)) dosahovaly svých limitů spektrální účinnosti s tradiční modulací Gaussian Minimum Shift Keying (GMSK) a pevnou symbolovou rychlostí. Motivací bylo vyvinout široce rozšířené sítě GSM/EDGE tak, aby podporovaly efektivnější datové služby a překlenuly mezeru směrem k 3G HSPA a LTE, zejména pro operátory s rozsáhlými investicemi do GSM.

Tato technologie řeší problém omezené datové propustnosti na jeden GSM časový slot tím, že umožňuje vyšší symbolovou rychlost a pokročilejší modulaci ve stejném 200 kHz kanálu. To přímo zvyšuje špičkovou přenosovou rychlost na časový slot, což je zásadní pro zlepšení uživatelského zážitku u služeb mobilního internetu. Historicky byla součástí iniciativy 'EDGE Evolution' ve 3GPP Release 7 a novějších, jejímž cílem bylo významně posílit schopnosti sítí GSM jako doplňkové technologie k UMTS/HSPA.

MDSR překonala omezení předchozích přístupů tím, že se posunula za pouhé změny modulace a také optimalizovala základní přenosové parametry, jako je symbolová rychlost a tvar impulsu. To umožnilo komplexnější zlepšení výkonu spoje a podpořilo zavedení modulací 16-QAM a 32-QAM, které vyžadují čistší signálovou konstelaci. Umožnila sítím GSM zůstat relevantní pro datové služby v prostředí s více rádiovými přístupovými technologiemi (multi-RAT).

## Klíčové vlastnosti

- Zvýšená symbolová rychlost ve srovnání se staršími systémy GSM/EDGE
- Využívá modifikované Gaussovo tvarování impulsu pro snížení rušení
- Podporuje schémata vyšších modulací (např. 16-QAM, 32-QAM)
- Zvyšuje spektrální účinnost v rámci 200 kHz nosné
- Zohlednění zpětné kompatibility se staršími zařízeními
- Součást vývoje GERAN pro vyšší špičkové přenosové rychlosti

## Související pojmy

- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [MDSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdsr/)
