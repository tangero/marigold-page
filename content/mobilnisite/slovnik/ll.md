---
slug: "ll"
url: "/mobilnisite/slovnik/ll/"
type: "slovnik"
title: "LL – Last OFDM Symbol index for R-PDCCH"
date: 2025-01-01
abbr: "LL"
fullName: "Last OFDM Symbol index for R-PDCCH"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ll/"
summary: "Parametr v LTE a 5G NR, který udává index posledního ortogonálního frekvenčně děleného multiplexního (OFDM) symbolu v podrámci vyhrazeného pro Relay-Physical Downlink Control Channel (R-PDCCH). Je klí"
---

LL je index posledního OFDM symbolu v rámci podrámce vyhrazeného pro Relay-Physical Downlink Control Channel (R-PDCCH), který definuje řídicí oblast pro přenosové spoje (backhaul) přes přenosový uzel (relay).

## Popis

Parametr 'LL' (Last [OFDM](/mobilnisite/slovnik/ofdm/) Symbol index for [R-PDCCH](/mobilnisite/slovnik/r-pdcch/)) je specifický konfigurační parametr používaný v kontextu pokročilých přenosových uzlů (Relay Nodes, [RN](/mobilnisite/slovnik/rn/)) v LTE-Advanced. Definuje časovou hranici oblasti řídicího kanálu na přenosovém spoji (backhaul) směrem dolů (downlink) mezi dárciovským [eNB](/mobilnisite/slovnik/enb/) (DeNB) a přenosovým uzlem (Relay Node). R-PDCCH je specializovaný fyzický kanál zavedený pro přenos řídicích informací (jako jsou například přiřazení plánování) specificky pro přenosový spoj přes přenosový uzel. Na rozdíl od běžného [PDCCH](/mobilnisite/slovnik/pdcch/), který je vysílán v prvních několika symbolech podrámce všem UE, může být R-PDCCH umístěn na různých pozicích symbolů, včetně využití zdrojů tradičně vyhrazených pro Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)).

Hodnota LL je celočíselný index (např. 0, 1, 2,... až do maximálního počtu symbolů v podrámci, což je typicky 14 pro normální cyklickou předponu), který ukazuje na poslední OFDM symbol obsazený R-PDCCH v rámci jemu přiřazeného páru bloků zdrojů (resource block pair). Tento parametr spolu s indexem počátečního symbolu definuje přesné zdroje v časové doméně, které musí přenosový uzel sledovat a dekódovat, aby přijímal své řídicí informace od DeNB. Konfigurace je signalizována přenosovému uzlu prostřednictvím signalizace vyšší vrstvy [RRC](/mobilnisite/slovnik/rrc/), což umožňuje flexibilní přidělování řídicí oblasti na základě zatížení přenosového spoje a podmínek interference.

Jeho role je klíčová pro správnou funkci přenosových uzlů s vnitropásmovým přenosem (in-band relaying), kde přenosový spoj (rozhraní Un) a přístupový spoj (rozhraní Uu) sdílejí stejnou nosnou frekvenci. Aby se zabránilo situaci, kdy přenosový uzel vysílá k UE v době, kdy má přijímat od DeNB, jsou specifické podrámce na přístupovém spoji označeny jako '[MBSFN](/mobilnisite/slovnik/mbsfn/) podrámce'. Během těchto podrámců může přenosový uzel přijímat přenosový spoj směrem dolů. Parametr LL zajišťuje, že přenosový uzel přesně ví, kdy přenos R-PDCCH končí, a poté může buď přijímat data R-PDSCH (Relay-PDSCH), nebo přepnout na jiné operace. Tato přesná časová koordinace předchází vlastní interferenci a je zásadní pro časově dělený provoz přenosového uzlu mezi přenosovým a přístupovým spojem.

## K čemu slouží

LL byl zaveden pro podporu funkce pokročilého přenosového uzlu (Relay Node) v LTE-Advanced, která byla standardizována v 3GPP Release 10. Účelem vnitropásmového přenosu je rozšířit pokrytí a zlepšit propustnost na okraji buňky bez vysokých nákladů na nasazení nových makro stanic s vyhrazeným přenosovým spojem. Klíčovou výzvou pro vnitropásmové přenosové uzly je, že nemohou současně vysílat a přijímat na stejné frekvenci kvůli obrovské vlastní interferenci, která by nastala na přijímači přenosového uzlu.

K vyřešení tohoto problému se používá časově dělený přístup, kdy se přenosový uzel střídá mezi nasloucháním dárciovské buňce (přenosový spoj downlink) a obsluhou vlastních uživatelských zařízení (přístupový spoj downlink). R-PDCCH byl vytvořen pro přenos specifických řídicích informací přenosového uzlu a jeho umístění v rámci podrámce muselo být flexibilní, aby se zabránilo pevným konfliktům zdrojů. Parametr LL jako součást konfigurace R-PDCCH poskytuje tuto nezbytnou flexibilitu. Umožňuje síti dynamicky upravovat velikost řídicí oblasti pro přenosový spoj a optimalizovat tak využití zdrojů. Bez takového konfigurovatelného parametru by měl řídicí kanál přenosového uzlu pevné umístění, což by snížilo flexibilitu plánování a efektivitu pro smíšený provoz přenosových uzlů a přímých UE obsluhovaných dárciovským eNB.

## Klíčové vlastnosti

- Definuje koncovou hranici oblasti R-PDCCH v časové doméně (OFDM symboly)
- Umožňuje flexibilní konfiguraci velikosti řídicího kanálu pro přenosový spoj (backhaul)
- Signalizován přenosovému uzlu prostřednictvím RRC pro dynamické přizpůsobení
- Klíčový pro časové duplexování přenosového a přístupového spoje přenosového uzlu
- Předchází vlastní interferenci na přenosovém uzlu definováním jasných přijímacích oken
- Podporuje efektivní přidělování zdrojů v buňkách s přenosovými uzly

## Související pojmy

- [R-PDCCH – Relay Physical Downlink Control Channel](/mobilnisite/slovnik/r-pdcch/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.247** (Rel-19) — 5G Multicast/Broadcast Service Architecture
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.996** (Rel-19) — ISAR Split Rendering Audio Characterization
- **TR 26.997** (Rel-19) — IVAS Codec Specification
- **TS 36.216** (Rel-19) — LTE Relay Node Physical Layer
- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [LL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ll/)
