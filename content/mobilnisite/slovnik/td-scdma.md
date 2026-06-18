---
slug: "td-scdma"
url: "/mobilnisite/slovnik/td-scdma/"
type: "slovnik"
title: "TD-SCDMA – Time Division Synchronous Code Division Multiple Access"
date: 2025-01-01
abbr: "TD-SCDMA"
fullName: "Time Division Synchronous Code Division Multiple Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/td-scdma/"
summary: "TD-SCDMA je standard pro mobilní komunikaci 3. generace vyvinutý v Číně, využívající duplex s časovým dělením (TDD) a synchronní CDMA. Byl klíčovou součástí rodiny IMT-2000 a poskytoval alternativu ke"
---

TD-SCDMA je standard pro mobilní komunikaci 3. generace vyvinutý v Číně, který využívá duplex s časovým dělením (TDD) a synchronní CDMA. Poskytuje spektrálně efektivní alternativu v rámci rodiny IMT-2000 pro nepárová frekvenční pásma.

## Popis

TD-SCDMA je rádiová přístupová technologie 3. generace standardizovaná organizací 3GPP jako součást rodiny UMTS. Její architektura integruje Node B (základnovou stanici) a Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)), podobně jako [WCDMA](/mobilnisite/slovnik/wcdma/), ale s odlišnými charakteristikami fyzické vrstvy. Technologie využívá hybridní vícekanálový přístup kombinující vícekanálový přístup s časovým dělením ([TDMA](/mobilnisite/slovnik/tdma/)) a vícekanálový přístup s kódovým dělením ([CDMA](/mobilnisite/slovnik/cdma/)). Klíčovým rozlišovacím znakem je použití duplexu s časovým dělením ([TDD](/mobilnisite/slovnik/tdd/)), kde přenosy v uplinku a downlinku probíhají na stejné nosné frekvenci, ale jsou odděleny v čase, což umožňuje dynamické přidělování časových slotů na základě asymetrie provozu.

Fyzická vrstva TD-SCDMA používá šířku pásma nosné 1,6 MHz a čipovou rychlost 1,28 Mcps. Využívá techniky chytrých antén, jako je adaptivní formování svazku a společná detekce, pro zvýšení kapacity a omezení interference. Rámcová struktura má délku 10 ms a je rozdělena na dva 5ms podrámce. Každý podrámec obsahuje sedm hlavních časových slotů pro provoz a několik speciálních slotů pro synchronizaci a ochranné intervaly. Synchronní aspekt odkazuje na synchronizaci uživatelských zařízení (UE) v uplinku, která snižuje interferenci z více přístupů a zlepšuje systémovou kapacitu.

V síti se TD-SCDMA připojuje k jádru sítě přes rozhraní Iu a podporuje jak přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)), tak přepojování paketů ([PS](/mobilnisite/slovnik/ps/)). Byla navržena pro efektivní využití nepárového spektra, které je často dostupnější než párové spektrum. Technologie zahrnuje pokročilé funkce, jako je dynamická alokace kanálů ([DCA](/mobilnisite/slovnik/dca/)) a synchronizace uplinku, které umožňují flexibilní správu zdrojů. Přestože se mimo Čínu nasadila jen omezeně, přispěla k vývoji TDD technik později využitých v LTE-TDD a NR TDD.

## K čemu slouží

TD-SCDMA byl vyvinut, aby poskytl standard mobilní komunikace 3G přizpůsobený čínskému trhu a spektrálním zdrojům a řešil potřebu efektivní technologie založené na TDD. Cílem bylo snížit závislost na zahraniční duševním vlastnictví a nabídnout nákladově efektivní řešení pro nepárové spektrum, které jiné standardy 3G, jako je WCDMA (FDD), nevyužívaly. Technologie řešila problémy spektrální asymetrie v mobilním provozu, což operátorům umožňovalo dynamicky upravovat kapacitu pro uplink/downlink.

Historicky vzešla z čínských výzkumných iniciativ na konci 90. let 20. století jako reakce na globální požadavky IMT-2000. Řešila omezení čistě FDD systémů, které vyžadují párová frekvenční pásma a pevný poměr uplink/downlink. Použitím TDD umožnilo TD-SCDMA flexibilnější využití spektra, což bylo zvláště výhodné pro datové služby s proměnnými charakteristikami provozu. Jeho vytvoření bylo motivováno strategickými, ekonomickými a technickými cíli pro zavedení domácího standardu.

## Klíčové vlastnosti

- Provoz s duplexem s časovým dělením (TDD) v nepárovém spektru
- Synchronní CDMA se synchronizací uplinku pro snížení interference
- Šířka pásma nosné 1,6 MHz a čipová rychlost 1,28 Mcps
- Techniky chytrých antén a společné detekce pro zvýšenou kapacitu
- Dynamická alokace kanálů (DCA) pro efektivní správu zdrojů
- Rámcová struktura s 10ms rámy a flexibilním přidělováním časových slotů

## Související pojmy

- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)
- [IMT-2000 – International Mobile Telecommunications 2000](/mobilnisite/slovnik/imt-2000/)

## Definující specifikace

- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements

---

📖 **Anglický originál a plná specifikace:** [TD-SCDMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/td-scdma/)
