---
slug: "r-pdcch"
url: "/mobilnisite/slovnik/r-pdcch/"
type: "slovnik"
title: "R-PDCCH – Relay Physical Downlink Control Channel"
date: 2025-01-01
abbr: "R-PDCCH"
fullName: "Relay Physical Downlink Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/r-pdcch/"
summary: "Řídicí kanál pro downlink používaný v přenosových uzlech LTE k přenosu přidělení prostředků a řídicích informací od dárce eNB (DeNB) přenosového uzlu k samotnému přenosovému uzlu. Je nezbytný pro umož"
---

R-PDCCH je Relay Physical Downlink Control Channel (řídicí kanál fyzické vrstvy pro přenosové uzly) používaný v přenosových uzlech LTE k přenosu přidělení prostředků a řídicích informací od dárce eNB k přenosovému uzlu, což umožňuje provoz přenosového uzlu v pásmu.

## Popis

Relay Physical Downlink Control Channel (R-PDCCH) je specializovaný kanál fyzické vrstvy definovaný ve specifikacích 3GPP LTE pro podporu provozu přenosových uzlů typu 1. Přenosový uzel je nízkovýkonová základnová stanice, která rozšiřuje pokrytí a kapacitu bezdrátovým připojením k dárci [eNB](/mobilnisite/slovnik/enb/) (DeNB) prostřednictvím backhaulového spoje známého jako rozhraní Un. R-PDCCH je klíčovou součástí tohoto backhaulového spoje, speciálně navrženou pro přenos řídicích informací pro downlink ([DCI](/mobilnisite/slovnik/dci/)) z DeNB k přenosovému uzlu. Tyto řídicí informace zahrnují přidělení prostředků pro downlinkové i uplinkové přenosy na backhaulovém spoji přenosového uzlu, příkazy pro řízení výkonu a další nezbytnou signalizaci.

Z architektonického hlediska je R-PDCCH vysílán DeNB a přijímán přenosovým uzlem. Funguje v rámci backhaulových podrámců přenosového uzlu, což jsou časová období, kdy je přenosový uzel nakonfigurován pro příjem od DeNB namísto vysílání k uživatelským zařízením (UE) na svém přístupovém spoji. Toto časové dělení je klíčové pro přenosové uzly pracující v pásmu, aby se zabránilo vlastnímu rušení. R-PDCCH je mapován na specifické zdrojové elementy v rámci bloků fyzických zdrojů ([PRB](/mobilnisite/slovnik/prb/)) těchto backhaulových podrámců. Jeho návrh se liší od konvenčního [PDCCH](/mobilnisite/slovnik/pdcch/) používaného pro přímou komunikaci s UE; R-PDCCH se nachází v datové oblasti podrámce (oblast [PDSCH](/mobilnisite/slovnik/pdsch/)) a může být vysílán s využitím frekvenčního dělení, což umožňuje flexibilnější přidělování prostředků a zvýšenou kapacitu pro řídicí signalizaci k přenosovým uzlům.

Z procesního hlediska DeNB používá R-PDCCH k dynamickému přidělování bloků fyzických zdrojů (PRB) na PDSCH pro přenos dat k přenosovému uzlu (přidělení pro downlink) a na [PUSCH](/mobilnisite/slovnik/pusch/) pro příjem dat od přenosového uzlu (přidělení pro uplink). Přenosový uzel průběžně monitoruje nakonfigurované prohledávací oblasti R-PDCCH ve vyhrazených backhaulových podrámcích, aby tyto příkazy dekódoval. R-PDCCH podporuje jak lokalizovaný, tak distribuovaný režim přenosu pro zajištění frekvenční diverzity nebo zisků z frekvenčně selektivního plánování. Jeho spolehlivý provoz je zásadní pro schopnost přenosového uzlu přeposílat data mezi DeNB a UE připojenými k přenosovému uzlu, což z něj činí klíčový prvek pro efektivní nasazení sítě v oblastech bez pokrytí a na okrajích buněk.

## K čemu slouží

R-PDCCH byl zaveden, aby vyřešil specifické výzvy spojené s řídicími kanály při nasazování přenosových uzlů LTE, zejména přenosových uzlů pracujících v pásmu. Přenos v pásmu znamená, že backhaulový spoj přenosového uzlu (k DeNB) a jeho přístupový spoj (k UE) fungují na stejném kmitočtu nosné. To vytváří problém: přenosový uzel nemůže na stejném kmitočtu současně vysílat a přijímat bez vážného vlastního rušení. Proto přenosový uzel pracuje v poloduplexním režimu, který vyžaduje specifické, naplánované podrámce pro backhaulovou komunikaci.

Konvenční [PDCCH](/mobilnisite/slovnik/pdcch/), umístěný v prvních několika symbolech každého podrámce, je vysílán všem UE a není vhodný pro tuto naplánovanou, na přenosový uzel specifickou operaci. DeNB potřebuje vyhrazený mechanismus pro zasílání řídicích informací (jako jsou přidělení prostředků) konkrétně k přenosovému uzlu během těchto vyhrazených backhaulových podrámců. R-PDCCH byl vytvořen, aby tuto potřebu naplnil. Poskytuje vyhrazený, dynamicky plánovatelný řídicí kanál, který existuje pouze v podrámcích, kdy přenosový uzel naslouchá DeNB, což zajišťuje spolehlivou a efektivní řídicí signalizaci pro backhaulový spoj bez rušení přenosů na přístupovém spoji přenosového uzlu.

Historicky, před standardizovanými přenosovými uzly, bylo rozšíření pokrytí dosahováno pomocí dalších makro stanovišť nebo opakovačů. Opakovače jsou jednodušší zařízení, která zesilují a přeposílají signály, ale také zesilují šum a rušení. Přenosový uzel 3GPP, podporovaný kanály jako je R-PDCCH, je chytřejším řešením. Dekóduje, znovu kóduje a retransmituje signály, čímž zlepšuje kvalitu signálu. R-PDCCH byla nezbytnou inovací pro umožnění této inteligentní, plánovatelné a efektivní operace přenosového uzlu v pásmu, což byla klíčová vlastnost pro zahušťování sítě a optimalizaci pokrytí v LTE-Advanced (Rel-10).

## Klíčové vlastnosti

- Vysílán v oblasti PDSCH vyhrazených backhaulových podrámců
- Přenáší řídicí informace pro downlink (DCI) pro backhaulový spoj přenosového uzlu
- Podporuje dynamická přidělení prostředků pro backhaulová data jak pro downlink (PDSCH), tak pro uplink (PUSCH)
- Využívá jak lokalizované, tak distribuované mapování virtuálních bloků zdrojů (VRB) pro frekvenční diverzitu nebo selektivní plánování
- Definuje specifické prohledávací oblasti R-PDCCH pro monitorování přenosovým uzlem
- Umožňuje provoz přenosového uzlu v pásmu s poloduplexním režimem tím, že je omezen na podrámce bez přístupu

## Související pojmy

- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.216** (Rel-19) — LTE Relay Node Physical Layer
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview

---

📖 **Anglický originál a plná specifikace:** [R-PDCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/r-pdcch/)
