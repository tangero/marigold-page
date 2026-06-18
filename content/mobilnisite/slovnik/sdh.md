---
slug: "sdh"
url: "/mobilnisite/slovnik/sdh/"
type: "slovnik"
title: "SDH – Synchronous Digital Hierarchy"
date: 2025-01-01
abbr: "SDH"
fullName: "Synchronous Digital Hierarchy"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sdh/"
summary: "Synchronous Digital Hierarchy (SDH) je mezinárodní standard pro vysokorychlostní synchronní optické telekomunikační sítě. Definuje strukturovaný, multiplexovaný rámec pro přenos digitálních signálů, p"
---

SDH je mezinárodní standard pro synchronní optickou přenosovou síť, který poskytuje strukturovaný, multiplexovaný rámec pro vytvoření vysokorychlostní, spolehlivé páteřní sítě pro mobilní sítě, jako jsou rozhraní 3GPP RAN a core.

## Popis

Synchronous Digital Hierarchy (SDH), standardizovaná [ITU-T](/mobilnisite/slovnik/itu-t/), je komplexní technologie pro přenos více digitálních bitových toků po optickém vlákně pomocí laserů nebo LED diod. Jejím základním principem je synchronní multiplexování, kdy jsou signály s nižší přenosovou rychlostí (tributary) strukturovaným, bajtově prokládaným způsobem kombinovány do signálu s vyšší rychlostí v rámci pevně definované rámcové struktury. To je v protikladu ke starší Plesiochronous Digital Hierarchy ([PDH](/mobilnisite/slovnik/pdh/)), která používala bitové prokládání a vyžadovala složité kroky multiplexování/demultiplexování. Základním stavebním blokem SDH je Synchronous Transport Module úrovně 1 (STM-1), který pracuje na rychlosti 155,52 Mbit/s. Vyšší rychlosti jsou definovány jako STM-N, kde N je celé číslo (např. STM-4 na 622 Mbit/s, STM-16 na 2,5 Gbit/s, STM-64 na 10 Gbit/s), dosažené bajtovým prokládáním N rámců STM-1.

Rámcová struktura SDH je vysoce organizovaná a skládá se z přenosových (payload) a servisních (overhead) bajtů. Servisní část je rozdělena na Section Overhead (SOH) a Path Overhead (POH). SOH, dále rozdělená na Regenerator Section Overhead (RSOH) a Multiplex Section Overhead (MSOH), poskytuje funkce pro zarovnání rámce, monitorování chyb (pomocí Bit Interleaved Parity, BIP) a datové komunikační kanály ([DCC](/mobilnisite/slovnik/dcc/)) pro správu sítě. POH je asociována s přenosovým kontejnerem (Virtual Container, [VC](/mobilnisite/slovnik/vc/)) a zajišťuje end-to-end monitorování výkonu a trasování cesty. Tato bohatá servisní část umožňuje rozsáhlé funkce správy, provozu a údržby ([OAM](/mobilnisite/slovnik/oam/)), což umožňuje rychlou detekci poruch, automatické ochranné přepínání (např. pomocí Multiplex Section Protection, [MSP](/mobilnisite/slovnik/msp/)) a monitorování výkonu bez přerušení služby.

V kontextu sítí 3GPP je SDH (a její severoamerický protějšek [SONET](/mobilnisite/slovnik/sonet/)) specifikována jako možnost přenosu fyzické vrstvy pro různá rozhraní. Poskytuje spolehlivý, vysokokapacitní 'přenosový kanál' pro přenos provozu mezi síťovými prvky. Například v rádiové přístupové síti mohou být SDH linky použity v backhaul síti pro připojení NodeB nebo eNodeB k Radio Network Controllerům ([RNC](/mobilnisite/slovnik/rnc/)) nebo přímo do core sítě. V core síti může přenášet provoz mezi přepínacími centry. Její standardizovaná multiplexní hierarchie umožňuje efektivní sdružování více nízkorychlostních TDM kanálů (jako jsou linky E1/T1 přenášející lub nebo lu-cs provoz) do vysokorychlostních optických spojů, čímž optimalizuje využití vlákna. Zatímco přenos založený na paketech (jako Ethernet/IP) je nyní dominantní, robustnost a možnosti správy SDH zajistily její dlouhodobou roli v poskytování spolehlivosti na úrovni operátora pro infrastrukturu mobilních sítí.

## K čemu slouží

SDH byla vyvinuta za účelem překonání významných omezení svého předchůdce, Plesiochronous Digital Hierarchy (PDH). Sítě PDH byly složité na správu, obtížně se multiplexovaly a demultiplexovaly, nabízely omezené a výrobci specifické možnosti OAM a měly neefektivní využití šířky pásma. Rozmach digitálních služeb a optických vláken v 80. letech 20. století si vyžádal robustnější, flexibilnější a lépe spravovatelný přenosový standard.

Vytvoření SDH bylo motivováno potřebou synchronní, globálně standardizované hierarchie, která zjednodušuje síťové operace. Jejím klíčovým účelem bylo umožnit přímé přidávání/odebírání nízkorychlostních signálů bez nutnosti demultiplexovat celý vysokorychlostní tok (pomocí Add-Drop Multiplexerů), poskytnout výkonné, standardizované OAM pro rychlou izolaci a obnovu po poruše, zajistit kompatibilitu mezi zařízeními různých výrobců (mid-span meet) a nabídnout škálovatelnou šířku pásma prostřednictvím jasné multiplexní cesty. Pro sítě 3GPP, zejména od 3G (R99) dále, poskytovala SDH spolehlivou, vysokokapacitní a spravovatelnou přenosovou vrstvu potřebnou pro podporu rostoucích požadavků na šířku pásma a přísné požadavky na dostupnost mobilních hlasových a datových služeb, čímž tvořila kritickou část síťové infrastruktury.

## Klíčové vlastnosti

- Synchronní, bajtově prokládané multiplexování (hierarchie STM-N)
- Komplexní servisní část (overhead) pro OAM, monitorování výkonu a DCC
- Podpora automatického ochranného přepínání (např. 1+1 MSP)
- Schopnost přímého přidávání/odebírání multiplexování zjednodušující síťovou architekturu
- Kompatibilita mezi zařízeními více výrobců (mid-span meet)
- Přenos různých klientských signálů (PDH, ATM, Ethernet přes GFP)

## Související pojmy

- [SONET – Synchronous Optical Networking](/mobilnisite/slovnik/sonet/)
- [PDH – Plesiochronous Digital Hierarchy](/mobilnisite/slovnik/pdh/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.411** (Rel-19) — Iu Interface Layer 1 Specification
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 29.202** (Rel-19) — SS7 Signalling Transport Protocol Architectures
- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.424** (Rel-8) — H.248 Profile for Trunking Media Gateways
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.854** (Rel-11) — FMC Federated Network Information Model

---

📖 **Anglický originál a plná specifikace:** [SDH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sdh/)
