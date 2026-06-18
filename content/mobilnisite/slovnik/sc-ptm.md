---
slug: "sc-ptm"
url: "/mobilnisite/slovnik/sc-ptm/"
type: "slovnik"
title: "SC-PTM – Single-Cell Point-to-Multipoint"
date: 2025-01-01
abbr: "SC-PTM"
fullName: "Single-Cell Point-to-Multipoint"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sc-ptm/"
summary: "Režim přenosu v LTE, který umožňuje efektivní doručování multicastových/broadcastových dat více uživatelům v rámci jedné buňky. Používá sdílené downlinkové zdroje (SC-MTCH) řízené přes společný řídicí"
---

SC-PTM je režim přenosu v LTE, který umožňuje efektivní doručování multicastových/broadcastových dat více uživatelům v rámci jedné buňky za použití sdílených downlinkových zdrojů řízených přes společný řídicí kanál.

## Popis

Single-Cell Point-to-Multipoint (SC-PTM) je režim přenosu a soubor funkcí v rámci LTE rádiové přístupové sítě, který umožňuje síti (konkrétně eNodeB) doručovat stejný obsah více uživatelským zařízením (UE) současně za použití sdílených rádiových zdrojů v pokrytí jedné buňky. Jedná se o doplňkovou technologii k [MBMS](/mobilnisite/slovnik/mbms/) (Multimedia Broadcast Multicast Service) založenou na [MBSFN](/mobilnisite/slovnik/mbsfn/) (Multicast-Broadcast Single Frequency Network), ale funguje bez nutnosti časově synchronizovaného přenosu napříč více buňkami. Architektura SC-PTM zavádí v LTE zásobníku nové logické kanály a procedury pro správu multicastových relací. Dvěma klíčovými logickými kanály jsou Single Cell Multicast Control Channel ([SC-MCCH](/mobilnisite/slovnik/sc-mcch/)) a Single Cell Multicast Transport Channel ([SC-MTCH](/mobilnisite/slovnik/sc-mtch/)). SC-MCCH přenáší řídicí informace, jako je konfigurace, plánování a podrobnosti o změnách dostupných služeb SC-PTM. SC-MTCH přenáší vlastní uživatelská data pro multicastovou službu.

Provoz SC-PTM zahrnuje několik kroků. Nejprve síť vysílá systémovou informaci, která označuje dostupnost SC-PTM a poskytuje konfiguraci pro SC-MCCH, včetně jeho plánování a období pro změny. UE zájemci o multicastové služby (identifikované pomocí Temporary Mobile Group Identity - [TMGI](/mobilnisite/slovnik/tmgi/)) monitorují SC-MCCH, aby zjistily, které služby jsou dostupné a jak je přijímat. Když se UE rozhodne připojit ke službě, extrahuje plánovací informace a přidružený Group [RNTI](/mobilnisite/slovnik/rnti/) ([G-RNTI](/mobilnisite/slovnik/g-rnti/)) pro SC-MTCH této služby. eNodeB následně vysílá multicastová data na Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)) v naplánovaných časech. eNodeB používá G-RNTI ke skramblování odpovídajících zpráv PDCCH, které ukazují na zdroje PDSCH, což umožňuje všem UE přihlášeným k danému G-RNTI dekódovat data. Samostatný pevný RNTI, SC-N-RNTI (Single Cell Notification RNTI), je použit na PDCCH k upozornění UE na změny v informacích SC-MCCH, což umožňuje efektivní úsporu energie.

SC-PTM je integrován do širší architektury protokolů LTE. Na vrstvě Radio Resource Control (RRC) mohou být UE ve stavu RRC_IDLE nebo RRC_CONNECTED během příjmu SC-PTM. Služba sama je iniciována a řízena jádrem sítě, často přes MBMS Gateway (MBMS-GW) a Broadcast Multicast Service Center (BM-SC), ale datová cesta pro SC-PTM obchází MCE (Multi-cell/multicast Coordination Entity) používané pro MBSFN. eNodeB přijímá multicastové IP pakety od jádra sítě a nezávisle zvládá veškeré plánování rádiových zdrojů a přenos pro svou buňku. Tato autonomie jedné buňky je definující charakteristikou. Z hlediska spolehlivosti SC-PTM nepoužívá retransmise HARQ na MAC vrstvě kvůli své point-to-multipoint povaze. Místo toho může být spolehlivost zajištěna na aplikační vrstvě pomocí forward error correction (FEC) nebo prostřednictvím přenosů v RLC unacknowledged módu s možným opakováním. Funkce je navržena jako nenáročná, což ji činí vhodnou pro služby, které jsou lokalizované, sporadické nebo neospravedlňují složitost a režii zřizování oblasti MBSFN.

## K čemu slouží

SC-PTM byl vyvinut pro řešení potřeby flexibilního, efektivního a nasaditelného multicastového řešení pro LTE, které doplňuje stávající MBMS založené na MBSFN. MBSFN je výborné pro vysílání kvalitního, synchronizovaného videa v široké oblasti (jako mobilní TV), ale vyžaduje přesnou synchronizaci mezi všemi eNodeB v oblasti MBSFN, pečlivé síťové plánování a je méně obratné pro dynamické nebo lokalizované služby. Mnoho vznikajících případů užití, jako jsou skupinové komunikace pro veřejnou bezpečnost (Mission Critical Push-To-Talk), softwarové aktualizace pro IoT zařízení nebo cílená reklama na konkrétním místě, nevyžaduje synchronizaci v široké oblasti a těží z jednoduššího, buňkově-centrického přístupu.

Primární problém, který SC-PTM řeší, je neefektivita použití více unicastových přenosů (Dedicated Traffic Channels - DTCH) pro doručení stejného obsahu mnoha uživatelům v jedné buňce. Unicastová replikace plýtvá downlinkovými rádiovými zdroji a výpočetním výkonem eNodeB. SC-PTM umožňuje, aby byl jeden přenos datového paketu vzduchem přijat celou skupinou, což dramaticky zlepšuje spektrální účinnost pro scénáře skupinové komunikace. To je zvláště důležité pro kapacitu sítě a pro obsluhu velkého počtu levných MTC zařízení s omezenou baterií.

Zavedený v 3GPP Release 13 jako součást vylepšení pro Machine-Type Communication (eMTC) a Critical Communications, SC-PTM zaplnil klíčovou mezeru v portfoliu služeb LTE. Poskytl standardizovanou, optimalizovanou metodu pro point-to-multipoint doručování, kterou mohli operátoři rychle nasadit, často pouze softwarovými upgrady stávajících eNodeB, bez nutnosti rozsáhlé synchronizace backhaulu a koordinace vyžadované pro MBSFN. Jeho vytvoření bylo motivováno konkrétními požadavky vertikálních odvětví, jako je veřejná bezpečnost a utility, která potřebovala spolehlivou skupinovou komunikaci pro své provozní pracovní postupy.

## Klíčové vlastnosti

- Umožňuje multicastový/broadcastový přenos dat v rámci jedné LTE buňky bez synchronizace MBSFN.
- Využívá vyhrazené logické kanály: SC-MCCH pro řízení a SC-MTCH pro uživatelská data.
- Používá skupinové identifikátory (G-RNTI) pro plánování a pevný SC-N-RNTI pro oznámení změn.
- Podporuje UE ve stavu RRC_IDLE i RRC_CONNECTED pro příjem služby.
- Zlepšuje spektrální účinnost ve srovnání s unicastovou replikací pro skupinové služby.
- Navrženo pro nízkou režii, vhodné pro sporadický, lokalizovaný nebo IoT orientovaný multicastový provoz.

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [SC-MCCH – Single Cell Multicast Control Channel](/mobilnisite/slovnik/sc-mcch/)
- [SC-MTCH – Single Cell Multicast Transport Channel](/mobilnisite/slovnik/sc-mtch/)
- [SC-N-RNTI – Single Cell Notification RNTI](/mobilnisite/slovnik/sc-n-rnti/)
- [G-RNTI – GERAN Radio Network Temporary Identity](/mobilnisite/slovnik/g-rnti/)
- [TMGI – Temporary Multicast Group Identifier](/mobilnisite/slovnik/tmgi/)

## Definující specifikace

- **TS 23.741** (Rel-13) — MBMS/GCSE_LTE Architecture Enhancements Study
- **TR 23.780** (Rel-14) — MBMS for Mission Critical Communication Services
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 25.446** (Rel-19) — MBMS Synchronisation Protocol (SYNC)
- **TR 26.989** (Rel-19) — MCPTT Enhancement Analysis
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.443** (Rel-19) — M2 Application Protocol (M2AP) for E-UTRAN
- **TS 36.444** (Rel-19) — M3AP Protocol Specification for M3 Interface
- **TS 36.890** (Rel-13) — SC-PTM Support in LTE Study
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TR 38.913** (Rel-19) — Next Gen Access Tech Scenarios & Requirements

---

📖 **Anglický originál a plná specifikace:** [SC-PTM na 3GPP Explorer](https://3gpp-explorer.com/glossary/sc-ptm/)
