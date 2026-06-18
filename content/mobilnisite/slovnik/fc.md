---
slug: "fc"
url: "/mobilnisite/slovnik/fc/"
type: "slovnik"
title: "FC – Carrier Center Frequency"
date: 2025-01-01
abbr: "FC"
fullName: "Carrier Center Frequency"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fc/"
summary: "Přesná střední frekvence rádiového nosiče, odvozená z referenční RF frekvence umístěné na globálním frekvenčním rastru. Je základním ukotvením pro přidělení šířky pásma kanálu a definuje spektrální po"
---

FC je přesná střední frekvence rádiového nosiče, odvozená z globálního frekvenčního rastru, která slouží jako ukotvení pro přidělení šířky pásma kanálu a definuje spektrální polohu nosiče pro danou numerologii.

## Popis

Střední frekvence nosiče (FC) je absolutní rádiová frekvence definující středový bod přiděleného pásma nosiče. Není volena libovolně, ale je odvozena přesným vzorcem založeným na kanálovém rastru definovaném ve specifikacích 3GPP. Proces začíná referenční [RF](/mobilnisite/slovnik/rf/) frekvencí (F_REF), což je bod na globálním frekvenčním rastru (např. mřížka 100 kHz, 15 kHz nebo 5 kHz v závislosti na frekvenčním pásmu a technologii). Tato F_REF je namapována na střední frekvenci nosiče FC podle specifického offsetu definovaného rozestupem podnosných (numerologií) a šířkou pásma kanálu.

Technicky se pro LTE a NR počítá FC jako F_REF + ΔF. ΔF je offset, který zajišťuje, že bloky zdrojů (RBs) nosiče jsou symetricky zarovnány kolem FC. Přesný výpočet závisí na numerologii (μ), která definuje rozestup podnosných ([SCS](/mobilnisite/slovnik/scs/) = 15 * 2^μ kHz). Šířka pásma kanálu, definovaná určitým počtem [RB](/mobilnisite/slovnik/rb/) (N_RB), je pak umístěna kolem této FC. Toto strukturované mapování zaručuje, že různé nosiče, i s různou numerologií, mohou být umístěny na frekvenčním rastru bez nedefinovaného překrývání a usnadňuje agregaci nosičů.

FC slouží jako ukotvení pro všechny funkce fyzické vrstvy. Základnové pásmo generuje ortogonální frekvenčně dělené multiplexní ([OFDM](/mobilnisite/slovnik/ofdm/)) symboly, kde jsou podnosné indexovány vzhledem k FC. RF vysílač převádí signál základnového pásma na tuto střední frekvenci pro vyzáření. Naopak přijímač používá FC jako frekvenci místního oscilátoru pro sestupnou konverzi. Synchronizační signály ([PSS](/mobilnisite/slovnik/pss/)/[SSS](/mobilnisite/slovnik/sss/)) a fyzický vysílací kanál ([PBCH](/mobilnisite/slovnik/pbch/)) jsou vysílány vzhledem k FC, což umožňuje uživatelskému zařízení (UE) detekovat a naladit se na buňku. Dále jsou požadavky na RF výkon, jako nežádoucí emise vysílače a citlivost přijímače, specifikovány ve vztahu k FC.

## K čemu slouží

Střední frekvence nosiče existuje proto, aby poskytla standardizovanou, jednoznačnou a globálně konzistentní metodu pro identifikaci spektrální polohy rádiového nosiče. Tím řeší kritický problém správy spektra a interoperability zařízení. Bez standardizované definice by operátoři sítí a výrobci zařízení mohli implementovat nosiče na mírně odlišných frekvencích, což by vedlo k interferencím a neúspěšným spojením.

Historicky, jak se buněčné systémy vyvíjely z úzkopásmového [FDMA](/mobilnisite/slovnik/fdma/) na širokopásmový OFDMA, potřeba přesného a flexibilního frekvenčního rastru se stala prvořadou. V GSM byl rozestup nosičů pevných 200 kHz. U 3G UMTS se používal pevný 5 MHz kanál. LTE a NR zavedly škálovatelné šířky pásma a více numerologií, což učinilo pevný rastr nedostatečným. Účelem definice FC, s její závislostí na numerologii a šířce pásma kanálu, je umožnit tuto flexibilitu při zachování předvídatelného a bezkonfliktního frekvenčního plánu. Umožňuje efektivní uspořádání nosičů různých šířek pásma v rámci licencovaného pásma, podporuje agregaci nosičů definováním přesného rozestupu mezi komponentními nosiči a zajišťuje, že UE mohou přesně vyhledávat a měřit buňky v širokém frekvenčním rozsahu. Je to základní kámen předvídatelného chování RF a soužití ve spektru.

## Klíčové vlastnosti

- Odvozena z referenční RF frekvence umístěné na definovaném kanálovém rastru
- Výpočet zahrnuje numerologii (rozestup podnosných) a šířku pásma kanálu
- Slouží jako centrální ukotvení pro indexování OFDM podnosných a mapování bloků zdrojů
- Základní pro generování místního oscilátoru v RF pro vysílání i příjem
- Zásadní pro procedury hledání buněk a synchronizace prováděné UE
- Klíčový referenční bod pro všechna RF testování shody (např. výstupní výkon, spektrální masky)

## Související pojmy

- [ARFCN – Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/arfcn/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TS 36.790** (Rel-15) — LAA/eLAA for CBRS 3.5GHz Band in US
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TS 37.812** (Rel-11) — Multi-band Multi-standard Radio BS Requirements
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [FC na 3GPP Explorer](https://3gpp-explorer.com/glossary/fc/)
