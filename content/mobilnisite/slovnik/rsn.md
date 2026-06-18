---
slug: "rsn"
url: "/mobilnisite/slovnik/rsn/"
type: "slovnik"
title: "RSN – Retransmission Sequence Number"
date: 2026-01-01
abbr: "RSN"
fullName: "Retransmission Sequence Number"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rsn/"
summary: "Sekvenční číslo používané v rádiových linkových protokolech 3GPP (jako PDCP a RLC) k identifikaci a uspořádání datových paketů pro retransmise. Zajišťuje spolehlivé doručování tím, že umožňuje přijíma"
---

RSN je sekvenční číslo používané v rádiových linkových protokolech 3GPP pro identifikaci a uspořádání datových paketů určených k retransmisím, což umožňuje spolehlivé doručování díky sledování chybějících paketů.

## Popis

Číslo sekvence pro retransmise (RSN) je základním mechanismem v protokolech pro opakované vysílání dat na rádiovém rozhraní 3GPP, konkrétně ve vrstvě Protokolu pro konvergenci paketových dat ([PDCP](/mobilnisite/slovnik/pdcp/)) a ve vrstvě Řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)). Jeho primární funkcí je jednoznačně identifikovat datové pakety (nebo segmenty), které jsou určeny pro retransmisi nebo se v ní nacházejí, což umožňuje řádné a efektivní zotavení z chyb přenosu.

Z architektonického hlediska spravují přenos dat mezi UE a základnovou stanicí (gNB/[eNB](/mobilnisite/slovnik/enb/)) obě vrstvy, PDCP i RLC. Pro zajištění spolehlivosti využívají protokoly založené na potvrzení (jako je Režim s potvrzením ([AM](/mobilnisite/slovnik/am/)) v RLC). Při přenosu paketu je mu přiděleno sekvenční číslo ([SN](/mobilnisite/slovnik/sn/)). Pokud přijímač nepotvrdí jeho příjem (kvůli chybě, ztrátě), může být paket vyžadovat retransmisi. RSN je samostatný číselný prostor nebo podpole používané speciálně ke sledování instancí retransmise těchto paketů. V některých implementacích je RSN čítač inkrementovaný pokaždé, když je konkrétní paket retransmitován.

Jak to funguje: Při prvotním přenosu je paket odeslán se svým primárním SN. Pokud je přijato negativní potvrzení ([NACK](/mobilnisite/slovnik/nack/)) nebo vyprší časovač, vysílač naplánuje retransmisi. Pro tuto retransmisi je paket označen hodnotou RSN (např. RSN=1 pro první retransmisi). Přijímač použije tuto hodnotu RSN k pochopení, že se jedná o retransmisi dříve přijatého paketu (identifikovaného jeho primárním SN). To pomáhá přijímači při opětovném sestavení a odstranění duplicit. V protokolech podporujících více retransmisí (jako [HARQ](/mobilnisite/slovnik/harq/) na [MAC](/mobilnisite/slovnik/mac/) nebo RLC) se RSN může s každým dalším pokusem inkrementovat, což umožňuje oběma stranám sledovat počet retransmisí, který lze využít pro adaptivní strategie, jako je změna modulace nebo výkonu.

Jeho role v síti je klíčová pro udržení integrity dat na nespolehlivém bezdrátovém kanálu. Tím, že jasně označuje retransmise, RSN zabraňuje tomu, aby přijímač interpretoval retransmitovaný paket jako nový, což by způsobilo duplikaci a mezery v sekvenci. Dále napomáhá správě vyrovnávací paměti na straně vysílače i přijímače. Pro vysílač pomáhá sledování RSN implementovat limity pro opakované vysílání a stanovit prioritu pokusů o ně. Pro přijímač napomáhá ke správnému přeuspořádání paketů před jejich předáním vyšším vrstvám. Tento mechanismus je nezbytný pro služby vyžadující vysokou spolehlivost, jako je VoIP, online hry nebo kritické IoT komunikace, protože zajišťuje plynulý tok dat i přes občasné rádiové chyby.

## K čemu slouží

Koncept RSN existuje pro řešení inherentní nespolehlivosti bezdrátového přenosového média v mobilních komunikacích. Rádiové spoje trpí útlumem, interferencí a šumem, což způsobuje ztrátu nebo poškození paketů. Pro zaručení doručení dat jsou nezbytné protokoly pro opakované vysílání. Jednoduchá retransmise bez správného označení však vede k problémům: přijímač může přijmout retransmitovaný paket jako nový, duplicitní paket, což naruší datový tok; vysílač může ztratit přehled o tom, kolikrát byl paket již opakovaně odeslán, což může plýtvat prostředky na opakovaně selhávající pakety.

Historicky používaly rané bezdrátové datové protokoly pro řazení jednoduchá sekvenční čísla, ale postrádaly vyhrazené sledování retransmisí. Zavedení RSN v protokolech 3GPP (patrné od Rel-6) poskytlo propracovanější nástroj pro správu retransmisí. Vyřešilo problém duplikace tím, že umožnilo přijímači rozlišit mezi novým paketem a retransmisí starého paketu, i když nesou stejná uživatelská data. To je klíčové pro protokoly jako RLC AM, které mohou doručovat velké datové bloky segmentované do mnoha paketů.

Motivací bylo zvýšit efektivitu a spolehlivost rádiové linkové vrstvy, zejména s rostoucími datovými rychlostmi a požadavky služeb u HSPA, LTE a 5G. Zahrnutím RSN mohly protokoly podporovat sofistikovanější strategie retransmisí, včetně inkrementální redundance (kde retransmise vysílají komplementární kódování) a adaptivní retransmise založené na počtu. Také umožňuje jasnější hlášení stavu (např. ve stavových hlášeních RLC) a lepší správu rádiových prostředků. RSN je v konečném důsledku klíčovou součástí, která umožňuje vysokou spolehlivost a kvalitu služeb poskytovaných moderními mobilními datovými sítěmi, a to i v náročných rádiových podmínkách.

## Klíčové vlastnosti

- Unikátní identifikátor pro pakety podstupující retransmisi
- Zabraňuje chybné interpretaci retransmitovaných paketů jako nových dat na straně přijímače
- Umožňuje sledování počtu retransmisí pro adaptivní přenosové strategie
- Používá se ve vrstvách PDCP i RLC pro spolehlivé doručování dat
- Podporuje protokoly jako Režim s potvrzením (AM) v RLC a procesy HARQ
- Napomáhá správnému přeuspořádání a opětovnému sestavení paketů po retransmisích

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 29.502** (Rel-19) — 5G System; Nsmf Service Based Interface; Stage 3
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [RSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/rsn/)
