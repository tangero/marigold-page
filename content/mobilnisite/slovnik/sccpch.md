---
slug: "sccpch"
url: "/mobilnisite/slovnik/sccpch/"
type: "slovnik"
title: "SCCPCH – Secondary Common Control Physical Channel"
date: 2025-01-01
abbr: "SCCPCH"
fullName: "Secondary Common Control Physical Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sccpch/"
summary: "Downlinkový fyzický kanál v UMTS (UTRA), který přenáší transportní kanály nepřiřazené k Primary CCPCH. Primárně přenáší Forward Access Channel (FACH) pro řídicí zprávy a Paging Channel (PCH) pro konta"
---

SCCPCH je downlinkový fyzický kanál v UMTS, který přenáší transportní kanály FACH a PCH pro řídicí zprávy a paging, a používá pevný spreading factor pro spolehlivý příjem.

## Popis

Secondary Common Control Physical Channel (SCCPCH) je vyhrazený downlinkový fyzický kanál v rádiovém rozhraní UMTS [WCDMA](/mobilnisite/slovnik/wcdma/). Je definován ve specifikacích fyzické vrstvy a používá se k přenosu společných transportních kanálů, které nepřenáší Primary Common Control Physical Channel ([PCCPCH](/mobilnisite/slovnik/pccpch/)). Dva hlavní transportní kanály mapované na SCCPCH jsou Forward Access Channel ([FACH](/mobilnisite/slovnik/fach/)) a Paging Channel ([PCH](/mobilnisite/slovnik/pch-text-pch/)). Ty mohou být mapovány na stejný nebo na samostatné SCCPCH v závislosti na konfiguraci sítě.

Z pohledu fyzické vrstvy má SCCPCH definovanou strukturu slotů a rámců, ale na rozdíl od PCCPCH nepřenáší primární synchronizační sekvence. Používá pevný spreading factor (typicky [SF](/mobilnisite/slovnik/sf/)=256), aby zajistil, že jej mohou přijímat všechn uživatelská zařízení (UE) v buňce, včetně těch na jejím okraji. Kanál je nepřetržitě vysílán Node B a jeho časování je synchronizováno s PCCPCH. Data na SCCPCH jsou časově multiplexována s bity Transport Format Combination Indicator ([TFCI](/mobilnisite/slovnik/tfci/)), které informují UE o formátu přenášených dat, a volitelně také s pilotními bity pro odhad kanálu.

Operační role SCCPCH je mnohostranná. FACH, přenášený na SCCPCH, se používá k vysílání řídicích informací k UE, která síť identifikovala (např. při odpovědi na náhodný přístup), nebo k odeslání malého množství uživatelských dat. [PCH](/mobilnisite/slovnik/pch/), rovněž přenášený na SCCPCH, se používá k pagingu UE při příchozím hovoru nebo datové relaci. UE v idle nebo connected módu periodicky monitorují PCH kvůli své identitě. Síť může konfigurovat více SCCPCH s různými charakteristikami (např. různými spreading kódy) pro správu zatížení a priorizaci provozu, například jeden SCCPCH pro paging a druhý pro data FACH.

## K čemu slouží

SCCPCH byl v UMTS zaveden, aby řešil omezení pouze jednoho Primary [CCPCH](/mobilnisite/slovnik/ccpch/). PCCPCH je vyhrazen pro přenos Broadcast Channel (BCH) s nejkritičtějšími systémovými informacemi a používá specifický kanalizační kód. Síť však potřebuje dodatečnou kapacitu pro přenos dalších společných řídicích informací, jako jsou pagingové zprávy a odpovědi na náhodný přístup, stejně jako pro doručování malých datových paketů bez nutnosti zřídit vyhrazený kanál. SCCPCH poskytuje tento potřebný dodatečný společný kanálový zdroj.

Jeho zavedení bylo motivováno potřebou efektivity a flexibility signalizace na společných kanálech. Vyčleněním samostatného fyzického kanálu pro FACH a PCH může síť tyto funkce spravovat nezávisle na broadcastovém proudu. Toto oddělení umožňuje optimalizovat různé úrovně vysílacího výkonu, spreading factory a kódovací schémata pro pokrytí pagingu oproti přenosu dat na FACH. Také zabraňuje kolizím a interferencím mezi kritickými broadcastovými informacemi a ostatním společným signalizačním provozem.

Dále SCCPCH umožňuje efektivní úsporu energie UE. UE v idle módu mohou spát a probouzet se pouze k naslouchání na své přiřazené pagingové okno (Paging Occasion) na SCCPCH, namísto nepřetržitého monitorování kanálu, který přenáší i jiný provoz. Tento návrh, klíčový pro strukturu společných kanálů UMTS, podporoval nezbytné procedury jako převýběr buňky, náhodný přístup a zahájení paketového přenosu dat v rané éře 3G, ještě před zavedením vysokorychlostních vyhrazených kanálů.

## Klíčové vlastnosti

- Přenáší Forward Access Channel (FACH) pro řídicí zprávy a malé datové pakety
- Přenáší Paging Channel (PCH) pro kontakt s UE iniciovaný sítí
- Používá pevný, vysoký spreading factor (např. SF=256) pro široké pokrytí buňky
- Časově multiplexuje data s TFCI bity pro indikaci transportního formátu
- Lze konfigurovat ve více instancích pro vyrovnávání zatížení
- Nepřetržitě vysílán Node B s časováním synchronizovaným s PCCPCH

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol

---

📖 **Anglický originál a plná specifikace:** [SCCPCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sccpch/)
