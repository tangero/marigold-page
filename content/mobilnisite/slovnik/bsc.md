---
slug: "bsc"
url: "/mobilnisite/slovnik/bsc/"
type: "slovnik"
title: "BSC – Base Station Controller"
date: 2025-01-01
abbr: "BSC"
fullName: "Base Station Controller"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bsc/"
summary: "BSC je klíčový síťový prvek v sítích 2G (GSM/EDGE), který spravuje a řídí více základnových přijímacích stanic (BTS). Zajišťuje správu radiových prostředků (RRM), zřizování hovorů, provedení předání h"
---

BSC je síťový prvek v sítích 2G (GSM/EDGE), který spravuje více základnových přijímacích stanic (BTS), zajišťuje správu radiových prostředků, zřizování hovorů, předávání hovorů (handover) a řízení výkonu.

## Popis

Řadič základnových stanic (Base Station Controller, BSC) je kritický přepínací a řídicí uzel v GSM radiové přístupové síti (RAN), konkrétně v podsystému základnových stanic ([BSS](/mobilnisite/slovnik/bss/)). Nachází se mezi základnovými přijímacími stanicemi ([BTS](/mobilnisite/slovnik/bts/)), které obsahují radiové vybavení, a ústřednou mobilního přepojování ([MSC](/mobilnisite/slovnik/msc/)) v jádře sítě. Primární funkcí BSC je správa radiových prostředků pro jemu přiřazené BTS, kterých mohou být stovky. Je zodpovědný za přidělování a uvolňování rádiových kanálů, správu přeskakování kmitočtů (frequency hopping) a řízení vysílacího výkonu jak BTS, tak mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) za účelem optimalizace kvality signálu a minimalizace interference. Tato centralizovaná kontrola umožňuje efektivní využití vzácného rádiového spektra a zajišťuje konzistentní kvalitu služeb napříč buňkami pod jeho správou.

Z architektonického hlediska rozhraní BSC s BTS přes rozhraní Abis, což je standardizovaný, často proprietární spoj přenášející provoz a řídicí signalizaci. Na straně jádra sítě se BSC připojuje k MSC pomocí rozhraní A, které je plně standardizováno, aby umožňovalo interoperabilitu mezi zařízeními BSS a jádra sítě od různých výrobců. BSC zajišťuje překódování řeči mezi komprimovaným formátem používaným přes rozhraní rádiového rozhraní (např. Full Rate, Enhanced Full Rate) a standardním [PCM](/mobilnisite/slovnik/pcm/) o rychlosti 64 kbit/s používaným v jádře sítě. Provádí také koncentraci provozu z mnoha BTS na méně okruhů směrem k MSC, čímž zvyšuje účinnost využití přenosových tras.

Základní provozní funkcí BSC je správa událostí mobility. Neustále monitoruje hlášení o síle a kvalitě signálu od mobilních stanic. Na základě předdefinovaných algoritmů a prahových hodnot činí BSC rozhodnutí o předání hovoru (handover). Dokáže autonomně provádět intra-BSC handovery (když se mobilní stanice pohybuje mezi BTS řízenými stejným BSC). Při inter-BSC handoverech koordinuje s cílovým BSC prostřednictvím MSC. BSC také spravuje převýběr buňky pro mobilní stanice v nečinném režimu (idle mode) a zajišťuje procedury okamžitého přidělení pro přidělení kanálu během zřizování hovoru nebo aktualizace polohy. Jeho role zahrnuje správu 2. vrstvy (layer 2) rádiového spoje a přenos signalizace vyšších vrstev mezi MS a MSC.

## K čemu slouží

BSC byl vytvořen, aby řešil základní výzvu škálování raných mobilních sítí za rámec jednoduché skupiny nezávislých rádiových věží. V základní buněčné architektuře bez BSC by každá [BTS](/mobilnisite/slovnik/bts/) potřebovala přímé, řízené spojení do ústředny jádra sítě ([MSC](/mobilnisite/slovnik/msc/)), což by vedlo k obrovské složitosti, špatnému využití prostředků a neschopnosti koordinovat činnosti mezi sousedními buňkami. BSC zavedl vrstvu centralizované inteligence a sdružování prostředků v rámci radiové přístupové sítě.

Jeho vytvoření vyřešilo několik klíčových problémů. Za prvé umožnil efektivní správu radiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)) napříč skupinou buněk, což umožnilo dynamické přidělování kanálů, plánování opakovaného využití kmitočtů a kontrolu interference, což je nezbytné pro kapacitu a kvalitu v buněčném systému. Za druhé lokalizoval složitý proces předání hovoru (handover). Zpracováním intra-BSC handoverů interně snížil signalizační zátěž na jádru sítě a umožnil rychlejší a spolehlivější handovery, což je klíčové pro udržení kvality hovoru pro pohybující se účastníky. Za třetí poskytl koncentrační bod, agregující provoz z mnoha nízkokapacitních spojů BTS do menšího počtu vyšších kapacitních tras k MSC, což výrazně snížilo přenosové náklady a složitost sítě.

Historicky architektura BSC definovaná ve standardu GSM (2G) představovala významný vývoj oproti dřívějším analogovým systémům. Ustavila jasné oddělení mezi rádiovým transceiverem (BTS) a rádiovým řadičem (BSC), což je model, který ovlivnil pozdější standardy 3GPP, ačkoli byl později nahrazen RNC ve standardu UMTS a distribuovaným eNB v LTE. Účelem BSC bylo vytvořit robustní, řiditelnou a nákladově efektivní RAN, která by mohla podporovat masovou mobilní telefonii.

## Klíčové vlastnosti

- Centralizovaná správa radiových prostředků (RRM) pro více BTS
- Provedení a řízení intra-cell a intra-BSC handoverů
- Funkčnost jednotky pro překódování a adaptaci rychlosti (Transcoding and Rate Adaptation Unit, TRAU) pro převod kódování řeči
- Koncentrace provozu z rozhraní Abis na rozhraní A směrem k MSC
- Řízení výkonu a správa přeskakování kmitočtů pro snížení interference
- Správa rozhraní Abis a zpracování 2. vrstvy pro rádiový spoj

## Související pojmy

- [BTS – Base Transceiver Station](/mobilnisite/slovnik/bts/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS
- **TS 26.193** (Rel-19) — AMR-WB Source Controlled Rate (SCR) Operation
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- … a dalších 16 specifikací

---

📖 **Anglický originál a plná specifikace:** [BSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/bsc/)
