---
slug: "mrb"
url: "/mobilnisite/slovnik/mrb/"
type: "slovnik"
title: "MRB – MBMS Point to Multipoint Radio Bearer"
date: 2025-01-01
abbr: "MRB"
fullName: "MBMS Point to Multipoint Radio Bearer"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mrb/"
summary: "Rádiový přenosový kanál používaný v LTE a 5G NR k doručování obsahu služby Multimedia Broadcast Multicast Service (MBMS) z jednoho síťového bodu k více uživatelským zařízením současně. Je klíčový pro"
---

MRB je bod–více bodů rádiový přenosový kanál (radio bearer) používaný v LTE a 5G NR k efektivnímu doručování obsahu MBMS, jako je mobilní TV, z jednoho síťového bodu k více uživatelským zařízením současně.

## Popis

[MBMS](/mobilnisite/slovnik/mbms/) Point to Multipoint Radio Bearer (MRB) je základní transportní mechanismus v architektuře 3GPP Radio Access Network (RAN), speciálně navržený pro vysílací (broadcast) a skupinový (multicast) provoz. Funguje jako jednosměrný přenosový kanál zřízený mezi rádiovými přístupovými uzly sítě, jako je eNodeB v LTE nebo gNB v 5G NR, a skupinou uživatelských zařízení (UE) v rámci specifické oblasti služby Multicast/Broadcast Service Area (MBSA). Na rozdíl od individuálních (unicast) přenosových kanálů, které vytvářejí samostatné logické spojení pro každé UE, MRB využívá jediný sdílený rádiový prostředek k přenosu identických datových proudů ke všem přihlášeným UE ve své pokryté oblasti. Tato sdílená povaha je jádrem jeho efektivity, neboť zabraňuje zahlcení sítě redundantními datovými přenosy, když mnoho uživatelů žádá stejný obsah současně.

Z architektonické perspektivy je MRB zřizován a spravován RAN ve spolupráci s MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) a Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) v jádru sítě. Tento přenosový kanál je charakterizován specifickými rádiovými konfiguracemi, včetně modulačních a kódovacích schémat, které jsou optimalizovány pro spolehlivý příjem na okraji buňky, kde mohou být podmínky signálu horší. MRB podporuje oba režimy přenosu: [MBSFN](/mobilnisite/slovnik/mbsfn/) (Multicast-Broadcast Single Frequency Network) a SC-PTM (Single Cell Point to Multipoint). Režim MBSFN synchronizuje přenosy z více buněk tak, aby vypadaly jako jediný přenos, čímž zlepšuje spektrální efektivitu a kvalitu příjmu prostřednictvím makro-diverzity. Režim SC-PTM se používá pro skupinové doručování v rámci jedné buňky a nabízí větší flexibilitu pro lokalizované služby.

Na vrstvě protokolu je MRB realizován prostřednictvím specifických konfigurací ve vrstvách PDCP (Packet Data Convergence Protocol), RLC (Radio Link Control) a [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control). Data pro MRB jsou plánována pomocí specifických logických kanálů, jako je [MTCH](/mobilnisite/slovnik/mtch/) (Multicast Traffic Channel), a řídicí informace jsou poskytovány přes [MCCH](/mobilnisite/slovnik/mcch/) (Multicast Control Channel). Vrstva [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control) v UE spravuje přihlášení k těmto kanálům. Výkon MRB je úzce spojen s parametry QoS definovanými pro službu MBMS, což zajišťuje, že vysílací proud splňuje požadované cíle spolehlivosti a latence. Jeho role je klíčová pro umožnění škálovatelného a síťově efektivního doručování oblíbeného živého mediálního obsahu a vysílání kritických informací.

## K čemu slouží

MRB byl vytvořen, aby vyřešil zásadní neefektivitu používání individuálních (unicast) spojení pro doručování oblíbeného obsahu v reálném čase masovému publiku. Před jeho zavedením, pokud tisíce uživatelů v oblasti chtěly sledovat stejnou živou sportovní událost nebo zpravodajské vysílání, musela by síť zřídit a udržovat tisíce individuálních datových kanálů, z nichž každý by spotřebovával vyhrazené rádiové prostředky. Tento přístup není škálovatelný a rychle by zahltil rádiové rozhraní, což by zhoršilo službu pro všechny uživatele. MRB to řeší tak, že s obsahem zachází jako s veřejným statkem na rádiovém rozhraní – přenáší jej jednou pro všechny příjemce, čímž šetří cenné a omezené rádiové spektrum a kapacitu sítě.

Vývoj MRB byl hnán komerční touhou nabízet služby mobilní TV a multimediálního vysílání, stejně jako regulatorními požadavky na efektivní systémy varování veřejnosti. Umožňuje obchodní modely pro vysílací služby, které by při použití čistě individuálního přenosu byly ekonomicky neproveditelné. Technicky umožňuje operátorům využít jejich infrastrukturu LTE a později 5G NR pro vysílací účely, čímž vytváří konvergovanou síť namísto potřeby samostatných vysílacích sítí, jako je DVB-H. MRB jako součást širšího rámce MBMS/eMBMS (Evolved MBMS) představuje klíčovou inovaci 3GPP pro komunikaci bod–více bodů, která vyvažuje flexibilitu IP doručování se spektrální efektivitou tradičního vysílání.

## Klíčové vlastnosti

- Umožňuje efektivní přenos dat bod–více bodů přes rádiové rozhraní
- Podporuje oba provozní režimy: MBSFN (synchronizovaný vícebuněčný) a SC-PTM (jednobuněčný)
- Využívá sdílené logické kanály (MTCH, MCCH) pro signalizaci v rovině dat a řízení
- Definován se specifickými charakteristikami QoS pro vysílací/skupinový provoz
- Spravován protokoly RRC pro členství ve skupině UE a konfiguraci přenosového kanálu
- Integruje se s architekturou MBMS v jádru sítě (BM-SC, MBMS-GW) pro autorizaci služby a distribuci dat

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [MTCH – MBMS point-to-multipoint Traffic Channel](/mobilnisite/slovnik/mtch/)
- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.849** (Rel-11) — Study on IMS Roaming Media Optimization
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 32.281** (Rel-19) — Announcement Service for Online Charging
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.323** (Rel-19) — Packet Data Convergence Protocol (PDCP)
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.425** (Rel-19) — NR User Plane Protocol Specification
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [MRB na 3GPP Explorer](https://3gpp-explorer.com/glossary/mrb/)
