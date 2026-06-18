---
slug: "tti"
url: "/mobilnisite/slovnik/tti/"
type: "slovnik"
title: "TTI – Transmission Timing Interval"
date: 2025-01-01
abbr: "TTI"
fullName: "Transmission Timing Interval"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tti/"
summary: "Transmission Timing Interval (TTI) je základní jednotka času pro plánování přenosů dat přes rozhraní rádiového přístupu v systémech 3GPP. Definuje dobu, po kterou je přenosový blok kódován, prokládán"
---

TTI je základní jednotka času pro plánování přenosů dat přes rozhraní rádiového přístupu, která definuje dobu zpracování a odeslání přenosového bloku a přímo ovlivňuje latenci a výkon systému.

## Popis

Transmission Timing Interval (TTI) je základní koncept fyzické vrstvy, který definuje časový úsek, po který je přenosový blok dat zpracováván a přenášen přes rozhraní vzdušného přenosu. Prakticky jde o minimální jednotku plánování v časové doméně pro vrstvu řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)). Jednomu TTI odpovídá přenos jednoho přenosového bloku (nebo v některých konfiguracích [MIMO](/mobilnisite/slovnik/mimo/) více bloků) z vyšší vrstvy, který prochází kanálovým kódováním, přizpůsobením rychlosti, prokládáním a modulací, než je namapován na fyzické zdroje (např. resource bloky v LTE, resource gridy v NR). Délka TTI je vnitřně propojena se strukturou subrámce a slotu rádiového rámce. Například v LTE je základní TTI 1 ms, což odpovídá jednomu subrámci. V 5G NR je TTI vázáno na délku slotu, která je proměnná (např. 1 ms, 0,5 ms, 0,25 ms, 0,125 ms) na základě nastaveného rozestupu subnosných, což umožňuje flexibilní numerologii pro podporu různorodých požadavků služeb.

Fungování [HARQ](/mobilnisite/slovnik/harq/) (Hybrid Automatic Repeat Request) je těsně synchronizováno s TTI. Každý proces HARQ je spojen s konkrétním TTI pro přenos a následným TTI pro příjem potvrzení ([ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/)). Délka TTI tedy určuje dobu odezvy pro HARQ retransmise, což je hlavní složka latence na uživatelské rovině. Kratší TTI umožňuje rychlejší retransmise a nižší latenci. Rozhodnutí o plánování, které učiní základnová stanice (eNodeB v LTE, gNB v NR), přiděluje fyzické zdroje uživatelskému zařízení (UE) pro konkrétní TTI. Toto rozhodnutí zohledňuje ukazatele kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), stav vyrovnávací paměti a požadavky QoS. Řídicí informace (např. Downlink Control Information - [DCI](/mobilnisite/slovnik/dci/)), která toto plánovací pověření přenáší, je sama přenášena v řídicí oblasti uvnitř TTI.

Klíčové komponenty zapojené do fungování založeného na TTI zahrnují plánovač MAC v základnové stanici, entitu HARQ na straně základnové stanice i UE a řetězce zpracování fyzické vrstvy. TTI je kritický parametr pro dimenzování systému a optimalizaci výkonu. Operátoři sítí a výrobci zařízení ladí parametry související s TTI, aby vyvážili latenci, propustnost a režii řídicích kanálů. Například velmi krátká TTI snižují latenci, ale mohou zvýšit režii řídicích kanálů a složitost zpracování. Koncept byl rozšířen technikami jako zkrácené TTI (sTTI) v LTE a mini-sloty v NR, které umožňují dobu přenosu kratší než nominální slot/TTI, aby vyhověly provozu pro ultra spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)), který nemůže čekat na hranici slotu.

## K čemu slouží

TTI bylo zavedeno, aby poskytlo standardizovanou, synchronizovanou časovou jednotku pro přenos a příjem dat v digitálních celulárních systémech, což je nezbytné pro efektivní multiplexování více uživatelů a předvídatelný chod systému. V raných standardech UMTS (3G) (R99) se používalo 10ms TTI, které bylo vhodné pro hlas a rané datové služby, ale vedlo k relativně vysoké latenci. Hlavním problémem, který TTI řeší, je potřeba společné časové reference pro plánování, HARQ a zpracování fyzické vrstvy napříč všemi síťovými prvky a uživatelskými zařízeními. Bez takto definovaného intervalu by koordinovaný přenos a efektivní využití sdíleného rádiového spektra byly nemožné.

Vývoj délky TTI byl primárně motivován poptávkou po nižší latenci a vyšší propustnosti v mobilních širokopásmových službách. Přechod na 1ms TTI v LTE (Rel-8) byl revolučním krokem, který výrazně snížil latenci rádiové sítě ve srovnání s 3G a umožnil citlivější uživatelský zážitek pro interaktivní služby. Toto kratší TTI umožnilo rychlejší HARQ retransmise a častější příležitosti pro plánování, což zlepšilo spektrální účinnost a propustnost. S nástupem služeb jako online hry, komunikace autonomních vozidel a průmyslová automatizace se však ještě nižší latence stala kritickým požadavkem.

To vedlo k dalším inovacím v pozdějších vydáních, jako je zkrácené TTI (sTTI) v LTE Rel-14 a flexibilní, škálovatelné TTI (slot/mini-slot) v 5G NR (Rel-15). Tato vylepšení řešila omezení pevného, relativně dlouhého TTI tím, že umožnila dynamickou adaptaci časového intervalu přenosu na základě potřeb služby. Například paket URLLC může být naplánován v mini-slotu trvajícím jen několik OFDM symbolů, čímž se obejde nutnost čekat na hranici celého slotu, a dosáhne se tak submilisekundové latence. Koncept TTI se tedy vyvinul z pevného systémového parametru na flexibilní nástroj pro optimalizaci přidělování zdrojů v časové doméně pro heterogenní profily provozu.

## Klíčové vlastnosti

- Definuje základní časovou jednotku pro plánování MAC a přenos přenosového bloku
- Přímo určuje dobu odezvy pro procesy Hybrid ARQ (HARQ), což ovlivňuje latenci
- Jeho délka je vázána na strukturu subrámce/slotu a může být proměnná (např. v 5G NR na základě numerologie)
- Umožňuje synchronizovaný provoz mezi vysílačem a přijímačem pro dekódování a zpětnou vazbu
- Klíčový parametr pro služby kritické na latenci; kratší TTI umožňují nižší latenci
- Podporuje pokročilé funkce jako zkrácené TTI (sTTI) a mini-sloty pro provoz URLLC

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- … a dalších 37 specifikací

---

📖 **Anglický originál a plná specifikace:** [TTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tti/)
