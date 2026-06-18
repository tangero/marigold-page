---
slug: "sib1"
url: "/mobilnisite/slovnik/sib1/"
type: "slovnik"
title: "SIB1 – System Information Block Type 1"
date: 2025-01-01
abbr: "SIB1"
fullName: "System Information Block Type 1"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sib1/"
summary: "SIB1 je primární plánovací blok v 5G NR, který obsahuje nejdůležitější informace, aby si UE mohlo určit, zda je mu povolen přístup k buňce. Poskytuje stav uzamčení buňky, seznam identit PLMN a plánova"
---

SIB1 je primární plánovací blok v 5G NR, který obsahuje základní informace, jako je stav přístupu k buňce a podrobnosti plánování pro všechny ostatní bloky systémových informací (System Information Blocks).

## Popis

System Information Block Type 1 (SIB1) je specifický, klíčový [SIB](/mobilnisite/slovnik/sib/) v systému 5G New Radio (NR), definovaný od 3GPP Release 15. Je vysílán na sdíleném kanálu pro downlink ([DL-SCH](/mobilnisite/slovnik/dl-sch/)) a je plánován Master Information Block ([MIB](/mobilnisite/slovnik/mib/)). Po úspěčné synchronizaci a dekódování MIB musí UE dekódovat SIB1, aby mohlo pokračovat v připojení k buňce (camping). Obsah SIB1 je strukturován tak, aby poskytoval dvě hlavní kategorie informací: parametry související s přístupem k buňce a plánovací informace pro ostatní SIB (SIB2 a další).

Technicky je SIB1 vysílán v definovaném časovém okně (SI-window) s konfigurovatelnou periodicitou, typicky 160 ms. Jeho přenos používá stejnou numerologii jako zbytek minimálních systémových informací ([RMSI](/mobilnisite/slovnik/rmsi/)), jehož je součástí. Klíčové informační prvky v SIB1 zahrnují seznam identit [PLMN](/mobilnisite/slovnik/plmn/), který UE sděluje, kterým sítím buňka patří; informace o uzamčení a rezervaci buňky, které indikují, zda je buňka dostupná pro přístup; kód oblasti sledování (tracking area code) a identitu buňky. Dále obsahuje si-SchedulingInfo, který poskytuje mapovací seznam s podrobnostmi o periodicitě a přenosovém okně pro každý další typ SIB, který síť vysílá.

Role SIB1 je ústřední pro řízení přístupu k síti a správu systémových informací. Přečtením SIB1 může UE okamžitě určit, zda je mu povoleno vybrat si tuto buňku pro připojení (camping) na základě svého předplaceného PLMN a stavu uzamčení buňky. Pokud je přístup povolen, UE použije plánovací informace k efektivnímu získání všech ostatních potřebných systémových informací (např. SIB2 pro konfiguraci rádiových zdrojů) bez nutnosti slepého hledání, čímž šetří životnost baterie. V flexibilní architektuře 5G také SIB1 přenáší informace relevantní pro síťové řezy (network slicing), jako je informace pro pomoc při výběru řezu specifická pro buňku (cell-SSAI). Jeho návrh zajišťuje, že nejvíce časově kritické parametry přístupu jsou doručeny v jediném, plánovatelném bloku, odděleně od méně často se měnících konfiguračních podrobností v ostatních SIB.

## K čemu slouží

SIB1 byl zaveden s 5G NR, aby sloužil jako základní kámen pro získávání systémových informací a řízení přístupu v dynamičtější a službami orientované síti. V předchozích generacích, jako je LTE, hrál SIB1 také plánovací roli, ale návrh pro 5G jeho účel a obsah upřesnil, aby odpovídal novým požadavkům, jako je komunikace s ultra-spolehlivým nízkým zpožděním ([URLLC](/mobilnisite/slovnik/urllc/)), hromadný IoT (massive IoT) a síťové řezy (network slicing). Primární problém, který řeší, je poskytnout UE minimální nezbytné informace pro okamžité rozhodnutí 'jít/nejít' ohledně přístupu k buňce a pro efektivní plánování získávání všech ostatních systémových dat.

Motivace vychází z potřeby rychlejšího počátečního přístupu a efektivnější úspory energie UE v 5G. Konsolidací informací o uzamčení buňky, [PLMN](/mobilnisite/slovnik/plmn/) ID a plánovacích informací do jednoho bloku plánovaného přímo [MIB](/mobilnisite/slovnik/mib/) může UE rychle zjistit vhodnost buňky. Pokud je buňka uzamčena nebo nepatří k vhodnému PLMN, může UE okamžitě ukončit další pokusy o získání informací z této buňky, čímž ušetří čas a energii během hledání buňky. To je obzvláště důležité pro zařízení IoT s omezenou energií.

Navíc explicitní plánovací informace pro ostatní SIB v SIB1 poskytují předvídatelnost a flexibilitu. Síť může konfigurovat různé periocity pro různé SIB na základě toho, jak často se jejich informace mění (např. SIB se seznamy sousedních buněk mohou být vysílány častěji než ty s méně proměnlivými daty). Tento strukturovaný přístup, iniciovaný SIB1, řeší omezení méně podrobného plánování, umožňuje optimalizované využití rádiových zdrojů pro vysílání systémových informací a umožňuje škálovatelné zavádění nových typů SIB pro budoucí funkce 5G.

## Klíčové vlastnosti

- Obsahuje parametry pro výběr/přístup k buňce, jako je PLMN ID a informace o uzamčení buňky
- Poskytuje kompletní plánovací informace (si-SchedulingInfo) pro všechny ostatní SIB
- Je součástí 5G Remaining Minimum System Information (RMSI)
- Vysílán s pevnou periodicitou (např. 160 ms) v rámci SI-window
- Obsahuje kód oblasti sledování (tracking area code) a identitu buňky pro registraci v síti
- Může přenášet pomocné informace pro síťové řezy (network slicing assistance information - cell-SSAI)

## Související pojmy

- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)
- [RMSI – Remaining Minimum System Information](/mobilnisite/slovnik/rmsi/)
- [SIB – System Information Block](/mobilnisite/slovnik/sib/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TS 37.470** (Rel-19) — W1 Interface Introduction for ng-eNB
- **TR 37.911** (Rel-19) — 3GPP 5G NTN Self-Evaluation Report
- **TS 38.470** (Rel-19) — F1 Interface Introduction

---

📖 **Anglický originál a plná specifikace:** [SIB1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/sib1/)
