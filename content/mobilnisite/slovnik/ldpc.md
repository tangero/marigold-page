---
slug: "ldpc"
url: "/mobilnisite/slovnik/ldpc/"
type: "slovnik"
title: "LDPC – Low-Density Parity-Check"
date: 2025-01-01
abbr: "LDPC"
fullName: "Low-Density Parity-Check"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ldpc/"
summary: "LDPC je výkonný kód pro opravu chyb vpřed (FEC) používaný pro kanálové kódování v 5G NR. Poskytuje výkon blízký Shannonově limitě, což umožňuje vysoké datové rychlosti a spolehlivý přenos, zejména pro"
---

LDPC je výkonný kód pro opravu chyb vpřed (FEC) používaný pro kanálové kódování v 5G NR, který umožňuje vysoké datové rychlosti a spolehlivý přenos, zejména pro velké datové bloky.

## Popis

Kódy LDPC (Low-Density Parity-Check) jsou třídou lineárních blokových kódů charakterizovaných řídkou (s nízkou hustotou) paritní maticí, což znamená, že obsahuje převážně nuly a málo jedniček. Tato řídkost je zásadní pro jejich efektivní iterační dekódovací algoritmy. Ve specifikacích 3GPP 5G New Radio (NR) byly kódy LDPC vybrány jako primární schéma kanálového kódování pro datový kanál ([PDSCH](/mobilnisite/slovnik/pdsch/) a PUSCH), čímž nahradily Turbo kódy používané v 4G LTE pro data. Konstrukce LDPC kódu pro 5G NR je založena na kvazicyklických (QC) LDPC kódech, které nabízejí dobrou rovnováhu mezi výkonem a efektivitou implementace. Jejich struktura je definována základním grafem ([BG](/mobilnisite/slovnik/bg/)), přičemž specifikace definují dva hlavní: BG1 a BG2. BG1 je optimalizován pro větší transportní bloky a vyšší kódové rychlosti, zatímco BG2 je vhodnější pro menší bloky a nižší rychlosti. Proces kódování zahrnuje rozšíření základního grafu podle tzv. lifting faktoru (Z) za účelem vytvoření finální paritní matice pro konkrétní velikost kódového bloku. Tento strukturovaný přístup umožňuje vysoce paralelní implementace dekodérů, což je klíčové pro dosažení nízké latence a vysoké propustnosti požadované v 5G. Dekodér typicky používá iterační algoritmus předávání zpráv, jako je belief propagation ([BP](/mobilnisite/slovnik/bp/)) nebo min-sum algoritmus, který pracuje na bipartitním grafu (Tannerově grafu) reprezentujícím paritní matici. Uzly v tomto grafu si vyměňují pravděpodobnostní zprávy o šanci, že daný bit je 0 nebo 1, a po několika iteracích konvergují k řešení. Tento proces poskytuje výjimečnou schopnost opravy chyb, zejména pro velké velikosti paketů běžné u vysokorychlostních dat. Výkon LDPC kódů je blízký teoretickému Shannonovu limitu, což z nich činí základní technologii pro dosažení špičkových datových rychlostí a spolehlivosti požadovaných standardem 5G NR. Jejich přijetí představovalo významný vývoj fyzické vrstvy oproti předchozím generacím.

## K čemu slouží

Hlavním účelem přijetí LDPC kódů v 5G NR bylo splnění přísných požadavků na datovou rychlost, latenci a spolehlivost definovaných pro IMT-2020. Dosavadní hlavní technologií kanálového kódování pro datové kanály ve 3G a 4G byl Turbo kód. Ačkoli byl Turbo kód ve své době revoluční, pro extrémní výkonnostní cíle 5G představoval výzvy, zejména pokud jde o propustnost a složitost dekodéru pro velmi velké bloky. Dekodéry Turbo kódů mohou trpět delší dekódovací latencí a jejich implementační složitost se s paralelizací škáluje méně příznivě než u LDPC. LDPC kódy se svou inherentní paralelizací a lepším výkonem u velkých bloků a vysokých kódových rychlostí byly identifikovány jako vhodnější kandidát. Na rozhodnutí měl také vliv požadavek na energetickou účinnost v základnových stanicích a zařízeních; efektivní architektury LDPC dekodérů mohou snížit spotřebu energie. Kromě toho kvazicyklická struktura přijatá 3GPP umožňuje efektivní hardwarovou implementaci pomocí jednoduchých posuvných registrů a usnadňuje flexibilní přizpůsobení kódové rychlosti pomocí punktování a opakování. Tím se řeší potřeba jediného univerzálního kódovacího schématu, které se dokáže přizpůsobit různorodým požadavkům scénářů použití 5G, od rozšířeného mobilního širokopásmového přístupu (eMBB) po ultra-spolehlivou komunikaci s nízkou latencí (URLLC), aniž by vyžadovalo více různých kódovacích schémat. Zavedení LDPC v Release 15 tedy bylo zásadní inovací fyzické vrstvy pro budoucí rozvoj rozhraní vzdušného rozhraní.

## Klíčové vlastnosti

- Založeno na kvazicyklické (QC) struktuře pro efektivitu implementace
- Používá dva základní grafy (BG1 a BG2) pro pokrytí širokého rozsahu velikostí bloků a kódových rychlostí
- Podporuje vysoce paralelní iterační dekódovací algoritmy (např. belief propagation)
- Poskytuje výkon opravy chyb blízký Shannonově limitě, zejména pro velké bloky
- Umožňuje flexibilní přizpůsobení kódové rychlosti pomocí punktování, zkracování a opakování
- Základní pro dosažení vícegigabitových datových rychlostí v 5G NR

## Související pojmy

- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 38.201** (Rel-19) — NR Physical Layer General Description
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TR 38.868** (Rel-17) — Optimizations of pi/2 BPSK uplink power in NR
- **TR 38.886** (Rel-16) — NR V2X UE Radio Transmission & Reception
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [LDPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ldpc/)
