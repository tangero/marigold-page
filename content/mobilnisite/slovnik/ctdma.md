---
slug: "ctdma"
url: "/mobilnisite/slovnik/ctdma/"
type: "slovnik"
title: "CTDMA – Code Time Division Multiple Access"
date: 2025-01-01
abbr: "CTDMA"
fullName: "Code Time Division Multiple Access"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ctdma/"
summary: "CTDMA je hybridní schéma vícenásobného přístupu kombinující CDMA a TDMA, primárně definované pro režim UTRA TDD. Umožňuje více uživatelům sdílet stejné frekvenční pásmo přidělením unikátních rozprostí"
---

CTDMA je hybridní schéma vícenásobného přístupu pro 3G UTRA TDD, které kombinuje CDMA a TDMA a umožňuje více uživatelům sdílet frekvenční pásmo prostřednictvím unikátních rozprostíracích kódů a přiřazených časových slotů.

## Popis

Code Time Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (CTDMA) je základní technologie vícenásobného přístupu specifikovaná pro režim Time Division Duplex (TDD) v rámci Universal Terrestrial Radio Access (UTRA) ve standardech 3GPP počínaje Release 99. Jedná se o hybridní schéma, které spojuje principy Code Division Multiple Access ([CDMA](/mobilnisite/slovnik/cdma/)) a Time Division Multiple Access (TDMA). V CTDMA je rádiový zdroj rozdělen ve dvou dimenzích: v kódové doméně a v časové doméně. Systém používá techniku přímé sekvenčního rozprostření spektra, kde jsou uživatelská data násobena vysokorychlostním pseudonáhodným rozprostíracím kódem, který rozšiřuje šířku pásma signálu. Tento rozprostřený signál je následně vysílán v určených, opakujících se časových slotech. Jeden rádiový rámec je rozdělen na 15 časových slotů a v rámci každého slotu může být multiplexováno více uživatelů přiřazením různých ortogonálních kódů s proměnným rozprostíracím faktorem ([OVSF](/mobilnisite/slovnik/ovsf/)). Rozprostírací faktor může být měněn pro podporu různých datových rychlostí uživatelů, což je koncept známý jako víceúrovňový přenos.

Architektura systému CTDMA, jak je definována v 3GPP TS 25.222, zahrnuje klíčové procedury fyzické vrstvy, jako je kanálové kódování, prokládání, modulace dat, rozprostírání a scramblování. Proces rozprostírání používá OVSF kódy k oddělení různých fyzických kanálů ze stejného zdroje (např. vyhrazené fyzické kanály - [DPCH](/mobilnisite/slovnik/dpch/)) v rámci jednoho časového slotu. Následně je na všechny fyzické kanály v daném slotu aplikován buňkově specifický scrambling kód pro odlišení přenosů z různých buněk. Struktura časového slotu zahrnuje pole pro datovou část, středový symbol (midamble) používaný pro odhad kanálu a společné detekce, a ochrannou periodu. Použití společné detekce v přijímači je klíčové pro zmírnění vnitrobuněčné interference způsobené nedokonalou ortogonalitou kódů, zejména v uplinku.

Fungování CTDMA je vnitřně propojeno s duplexní metodou TDD, kde uplinkové a downlinkové přenosy probíhají na stejné nosné frekvenci, ale v různých časových slotech. To umožňuje asymetrické a dynamické přidělování kapacity mezi uplink a downlink přiřazením proměnného počtu slotů pro každý směr na základě poptávky po přenosu. Kombinace průměrování interference od CDMA a frekvenčního opakování 1 se strukturou časových slotů TDMA poskytuje flexibilní rozhraní vzduchu schopné podporovat jak spojově orientované, tak paketově orientované služby. Jeho role v síti je definovat rádiové rozhraní pro UMTS TDD, umožňující efektivní využití nepárových frekvenčních pásem a podporu aplikací s asymetrickými přenosovými vzory, jako je prohlížení internetu.

## K čemu slouží

CTDMA bylo vytvořeno, aby poskytlo standardizované schéma rádiového přístupu pro 3G systémy pracující v režimu Time Division Duplex (TDD), řešící potřebu efektivního využití nepárových frekvenčních alokací. Před 3G používal GSM čisté TDMA a rané návrhy [CDMA](/mobilnisite/slovnik/cdma/) (jako IS-95) používaly Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)). Hybridní přístup CTDMA byl motivován snahou spojit výhody obou technik: flexibilní kapacitu a frekvenční plánování CDMA s inherentní podporou asymetrického provozu a přesné kontroly interference nabízené časově slotovanou strukturou TDMA. To bylo obzvláště důležité pro operátory, kteří vlastnili licence na nepárové spektrum, pro které nebyly vhodná čistá FDD řešení.

Technologie řešila problém poskytování vysokokapacitních multimediálních mobilních služeb ve frekvenčních pásmech nevyžadujících párové uplink/downlink kanály. Řešila omezení čistého TDMA, jako je rigidní přidělování kapacity a potřeba frekvenčního plánování, a omezení čistého CDMA v FDD, které je méně přizpůsobivé rychle se měnícím poměrům uplink/downlink provozu. Integrací CDMA do TDMA rámce umožnilo CTDMA více uživatelům sdílet jeden časový slot, čímž zvýšilo efektivitu sdružování a umožnilo systému lépe zvládat přerušovaný paketový datový provoz. Jeho návrh také usnadnil pokročilé přijímací techniky, jako je společná detekce, která byla nezbytná pro zvládnutí vnitrobuněčné interference ve směru uplink systému TDD-CDMA, čímž se zlepšila celková kapacita a výkon systému.

## Klíčové vlastnosti

- Hybridní vícenásobný přístup kombinující rozprostírání CDMA a časové sloty TDMA
- Používá ortogonální kódy s proměnným rozprostíracím faktorem (OVSF) pro oddělení kanálů
- Podporuje víceúrovňový přenos prostřednictvím proměnných rozprostíracích faktorů
- Využívá TDD pro dynamické asymetrické přidělování kapacity uplink/downlink
- Používá středové symboly (midambles) pro odhad kanálu a pokročilou společnou detekci
- Operuje v nepárových frekvenčních pásmech, umožňující flexibilní využití spektra

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding

---

📖 **Anglický originál a plná specifikace:** [CTDMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctdma/)
