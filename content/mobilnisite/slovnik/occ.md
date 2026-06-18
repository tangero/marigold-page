---
slug: "occ"
url: "/mobilnisite/slovnik/occ/"
type: "slovnik"
title: "OCC – Orthogonal Covering Code"
date: 2025-01-01
abbr: "OCC"
fullName: "Orthogonal Covering Code"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/occ/"
summary: "Sekvence aplikovaná pro modulaci nebo rozprostření signálů od více uživatelů nebo anténních portů ve stejných časově-frekvenčních zdrojích, aby byly oddělitelné. Je klíčová pro uplink multi-user MIMO"
---

OCC je ortogonální krycí kód aplikovaný pro modulaci nebo rozprostření signálů od více uživatelů nebo anténních portů ve stejných časově-frekvenčních zdrojích, aby byly oddělitelné, což umožňuje efektivní multiplexování a potlačení interference v 5G NR.

## Popis

Ortogonální krycí kód (OCC) je matematická sekvence, často založená na Walshových-Hadamardových kódech nebo vektorech diskrétní Fourierovy transformace ([DFT](/mobilnisite/slovnik/dft/)), používaná v bezdrátových komunikačních systémech k ortogonalizaci signálů vysílaných přes stejné fyzické zdroje. V 5G New Radio (NR) se OCC primárně uplatňují v uplink směru pro dva klíčové účely: pro demodulační referenční signály ([DM-RS](/mobilnisite/slovnik/dm-rs/)) u multi-user [MIMO](/mobilnisite/slovnik/mimo/) ([MU-MIMO](/mobilnisite/slovnik/mu-mimo/)) a pro rozprostření řídicích informací na fyzickém uplink řídicím kanálu ([PUCCH](/mobilnisite/slovnik/pucch/)). U DM-RS, když je více uživatelských zařízení (UE) naplánováno na stejné časově-frekvenční bloky zdrojů ve schématu MU-MIMO, musí být jejich referenční signály na přijímači gNodeB rozlišitelné. Toho je dosaženo aplikací různých, ortogonálních OCC přes sousední symboly nebo subnosné na DM-RS sekvence různých UE. Vlastnost ortogonality zajišťuje, že gNodeB může oddělit a odhadnout kanál pro každé UE nezávisle, což je zásadní pro koherentní detekci jejich dat. U formátů PUCCH, které nesou uplink řídicí informace ([UCI](/mobilnisite/slovnik/uci/)) jako [HARQ-ACK](/mobilnisite/slovnik/harq-ack/) a [CSI](/mobilnisite/slovnik/csi/), jsou OCC aplikovány napříč symboly v rámci slotu, aby poskytly zisk rozprostření a umožnily multiplexování více UE na stejném bloku zdrojů. Konkrétní délka OCC a způsob aplikace jsou definovány formátem PUCCH a jeho nakonfigurovanou délkou trvání. gNodeB přiřazuje index OCC UE prostřednictvím downlink řídicích informací (DCI), čímž spravuje ortogonalitu mezi současně vysílajícími uživateli. Generování a aplikace OCC jsou zpracovány v řetězci základního pásma, zahrnujícím fáze mapování vrstev, předkódování a mapování prvků zdrojů podle 3GPP TS 38.211. Jejich správná aplikace je kritická pro udržení nízké interference mezi uživateli, což přímo ovlivňuje spektrální účinnost uplink a kapacitu systému v hustých scénářích nasazení.

## K čemu slouží

Účelem ortogonálního krycího kódu je umožnit neinterferenční multiplexování více datových nebo řídicích toků v identických časově-frekvenčních zdrojích. Tím řeší základní problém nedostatku zdrojů v rozhraní rádiového přístupu tím, že umožňuje obsluhovat více uživatelů nebo datových vrstev současně, čímž zvyšuje spektrální účinnost. V kontextu ambiciózních cílů 5G NR na kapacitu a konektivitu jsou techniky jako MU-MIMO nezbytné. MU-MIMO však vyžaduje přesný odhad kanálu pro každého uživatele, což by bylo nemožné, pokud by si jejich referenční signály vzájemně interferovaly. OCC aplikované na DM-RS poskytují toto potřebné oddělení. U řídicích kanálů efektivní přenos malých datových bloků od mnoha uživatelů (např. pro masivní IoT) vyžaduje metodu sdílení zdrojů bez složité režie plánování. Rozprostření založené na OCC na PUCCH umožňuje toto multiplexování s nízkou režií. Motivací pro jeho zavedení a zdokonalení v Rel-15 a novějších bylo podpořit pokročilé anténní systémy a rozmanité případy užití 5G. Předchozí systémy jako LTE používaly podobné koncepty (např. ortogonální kódy pro referenční signály), ale flexibilnější číselný systém 5G NR a širší škála scénářů nasazení si vyžádaly předefinovaný a přizpůsobivější rámec OCC. Řeší omezení jednoduchého multiplexování s časovým/frekvenčním dělením tím, že poskytuje vrstvu oddělení v kódové doméně, která je odolnější vůči určitým typům útlumu a umožňuje hustější uspořádání uživatelů.

## Klíčové vlastnosti

- Umožňuje oddělení DM-RS pro více UE ve scénářích uplink MU-MIMO.
- Používá se pro rozprostření a multiplexování UCI od více UE na zdrojích PUCCH.
- Založen na ortogonálních sekvencích (např. Walshovy kódy) aplikovaných napříč časovými symboly nebo frekvenčními subnosnými.
- Konfigurovatelná délka a způsob aplikace vázané na specifické formáty PUCCH a konfigurace DM-RS.
- Dynamicky přiřazován UE prostřednictvím udělení plánování v DCI.
- Kritický pro potlačení interference a zvýšení kapacity uplink a spektrální účinnosti.

## Související pojmy

- [DM-RS – Demodulation Reference Signal](/mobilnisite/slovnik/dm-rs/)
- [MU-MIMO – Multi-User Multiple Input Multiple Output](/mobilnisite/slovnik/mu-mimo/)
- [PUCCH – Physical Uplink Control Channel](/mobilnisite/slovnik/pucch/)
- [UCI – Uplink Control Information](/mobilnisite/slovnik/uci/)

## Definující specifikace

- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TR 38.812** (Rel-16) — Study on NOMA for NR

---

📖 **Anglický originál a plná specifikace:** [OCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/occ/)
