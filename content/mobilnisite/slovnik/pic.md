---
slug: "pic"
url: "/mobilnisite/slovnik/pic/"
type: "slovnik"
title: "PIC – Parallel Interference Cancellation"
date: 2025-01-01
abbr: "PIC"
fullName: "Parallel Interference Cancellation"
category: "Physical Layer"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pic/"
summary: "Technika zpracování signálu používaná v bezdrátových přijímačích ke zmírnění víceuživatelského rušení, zejména v systémech s kódovým dělením (CDMA) jako UMTS. Funguje na principu paralelního odhadu a"
---

PIC je technika zpracování signálu používaná v bezdrátových přijímačích, zejména v CDMA systémech jako UMTS, ke zmírnění víceuživatelského rušení paralelním odhadem a odečtením rušení od signálů ostatních uživatelů.

## Popis

Parallel Interference Cancellation (PIC, paralelní potlačení rušení) je pokročilý algoritmus přijímače používaný na fyzické vrstvě 3GPP rádiových přístupových sítí, zejména ve systémech Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([WCDMA](/mobilnisite/slovnik/wcdma/)) specifikovaných v UMTS. Jedná se o techniku detekce více uživatelů (MUD) navrženou pro potírání problému blízko-daleko a vnitrobuněčného rušení vlastního [CDMA](/mobilnisite/slovnik/cdma/) systémům. V CDMA vysílá více uživatelů současně ve stejném kmitočtovém pásmu, odlišených jedinečnými rozprostíracími kódy. V přijímači se tyto signály vzájemně ruší, což omezuje kapacitu a výkon. PIC má toto rušení zmírnit.

Algoritmus pracuje iterativně ve více stupních. V prvním stupni poskytnou konvenční korelační detektory (např. RAKE přijímače) počáteční odhady datových symbolů pro všechny uživatele. Tyto odhady se pak použijí k rekonstrukci rušení, které každý uživatel způsobuje ostatním. Tato rekonstrukce zahrnuje znovu rozprostření odhadnutých symbolů příslušným uživatelským rozprostíracím kódem, aplikaci odhadnuté impulsní odezvy kanálu (včetně útlumu a zpoždění) a škálování odhadnutou amplitudou. Rekonstruované rušivé signály jsou pak paralelně pro všechny uživatele odečteny od přijatého složeného signálu, odtud název 'paralelní potlačení rušení'. Tím vznikne sada 'vyčištěných' signálů pro každého uživatele, které jsou následně přivedeny do druhého detekčního stupně pro vylepšený odhad symbolů.

Klíčové součásti přijímače s PIC zahrnují počáteční detekční stupeň (často RAKE přijímač), jednotku rekonstrukce rušení, jednotku paralelního potlačení a následné stupně opakované detekce. Proces lze opakovat v několika iteracích pro další zpřesnění odhadů, přičemž každá iterace může zlepšit výkonnost z hlediska chybovosti ([BER](/mobilnisite/slovnik/ber/)). Zisk ve výkonnosti však závisí na přesnosti počátečních odhadů; chyby v odhadu mohou vést k nesprávnému potlačení a potenciálnímu šíření chyb. Proto PIC často zahrnuje techniky jako částečné potlačení (odečtení pouze zlomku odhadnutého rušení) ke zmírnění efektů šíření chyb.

Role PIC v síti je primárně v uplink přijímači Node B (základnové stanice), kde zlepšuje demodulaci signálů od více mobilních stanic. Účinným snížením vícenásobného přístupového rušení ([MAI](/mobilnisite/slovnik/mai/)) PIC zvyšuje uplink kapacitu a pokrytí buňky, což umožňuje obsloužit více uživatelů současně nebo zlepšit přenosové rychlosti stávajících uživatelů. Jedná se o výpočetně náročnou techniku, která však nabízí významnou výkonnostní výhodu oproti jednodušším přijímačům, zejména ve scénářích s vysokým zatížením. Její specifikace a požadavky na výkonnost jsou podrobně popsány v různých 3GPP technických specifikacích pokrývajících procedury fyzické vrstvy a rádiové požadavky.

## K čemu slouží

PIC byl vyvinut pro řešení základního omezení technologie [CDMA](/mobilnisite/slovnik/cdma/): víceuživatelského rušení. V raných CDMA systémech, jako byl IS-95, používaly přijímače jednoduché korelační detektory (RAKE přijímače), které zacházely se signály od ostatních uživatelů jako s šumem. Tento přístup trpěl problémem blízko-daleko, kdy silný signál od blízkého uživatele mohl přehlušit slabší signály od vzdálených uživatelů, což výrazně omezovalo kapacitu. Techniky detekce více uživatelů (MUD), včetně PIC, byly zavedeny pro aktivní potlačení tohoto rušení, čímž se zvýšila kapacita a odolnost systému.

Motivace pro PIC v 3GPP UMTS ([WCDMA](/mobilnisite/slovnik/wcdma/)) byla splnit náročné požadavky na výkon pro služby mobilní komunikace třetí generace, které slibovaly vyšší přenosové rychlosti a lepší spektrální účinnost. Původní 3GPP specifikace z období [R99](/mobilnisite/slovnik/r99/) zahrnovaly podporu pokročilých přijímacích technik, jako je PIC, pro implementaci v Node B. Řešila problém vnitrobuněčného rušení, které se stává dominantním omezením výkonu s rostoucím zatížením buňky. Potlačením rušení umožňuje PIC síti pracovat blíže jejím teoretickým kapacitním limitům.

Ve srovnání s jednodušším sekvenčním potlačením rušení (SIC), které zpracovává uživatele postupně, PIC zpracovává všechny uživatele paralelně v rámci každé iterace, což může nabídnout rychlejší konvergenci a lepší výkon ve scénářích se symetrickým výkonem. Jeho vývoj byl hnán potřebou praktických, implementovatelných MUD algoritmů, které by mohly být nasazeny v základnových stanicích ke zlepšení výkonu uplink bez nutnosti změn v uživatelských zařízeních. Řešil tak omezení předchozích přístupů detekce jednotlivých uživatelů a umožnil sítím UMTS lépe podporovat kapacitně náročné datové služby.

## Klíčové vlastnosti

- Vícefázové iterativní odhadování a potlačení rušení
- Zpracovává rušení od všech uživatelů paralelně v rámci každé iterace
- Zvyšuje uplink kapacitu a zmírňuje problém blízko-daleko v CDMA
- Lze implementovat s faktory částečného potlačení pro kontrolu šíření chyb
- Zlepšuje poměr signálu k rušení a šumu (SINR) pro detekované uživatele
- Specifikováno jako součást pokročilých přijímacích schopností Node B pro UMTS/WCDMA

## Související pojmy

- [CDMA – Code Division Multiple Access](/mobilnisite/slovnik/cdma/)
- [SINR – Signal to Interference plus Noise Ratio](/mobilnisite/slovnik/sinr/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TR 38.812** (Rel-16) — Study on NOMA for NR

---

📖 **Anglický originál a plná specifikace:** [PIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/pic/)
