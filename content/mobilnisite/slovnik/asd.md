---
slug: "asd"
url: "/mobilnisite/slovnik/asd/"
type: "slovnik"
title: "ASD – Azimuth Spread of Departure"
date: 2025-01-01
abbr: "ASD"
fullName: "Azimuth Spread of Departure"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/asd/"
summary: "ASD je parametr modelu kanálu kvantifikující úhlovou disperzi signálů opouštějících anténní pole základnové stanice. Charakterizuje prostorovou bohatost vícecestného šíření v azimutální rovině, což je"
---

ASD je parametr modelu kanálu, který kvantifikuje úhlovou disperzi signálů opouštějících anténní pole základnové stanice v azimutální rovině.

## Popis

Azimuth Spread of Departure (ASD) je statistický parametr definovaný v rámci 3GPP prostorových modelů kanálu ([SCM](/mobilnisite/slovnik/scm/)), konkrétně v modelech typu clustered delay line ([CDL](/mobilnisite/slovnik/cdl/)) a tapped delay line ([TDL](/mobilnisite/slovnik/tdl/)). Kvantifikuje úhlové rozprostření, neboli disperzi, vícecestných komponent v azimutální rovině při jejich odchodu z vysílajícího (základnové stanice) anténního pole. Konceptuálně ASD popisuje, jak se signální energie úhlově rozptyluje od vysílače v důsledku rozptylu a odrazů v prostředí šíření. Nízká hodnota ASD indikuje kanál s omezeným úhlovým rozprostřením, často odpovídající scénáři přímé viditelnosti nebo vysoce směrovému scénáři, zatímco vysoká hodnota ASD značí prostředí s bohatým rozptylem, kde signály odcházejí v širokém úhlovém rozsahu.

Technicky je ASD odvozeno z výkonového úhlového spektra ([PAS](/mobilnisite/slovnik/pas/)) úhlů odchodu. V 3GPP modelování je každému šířicímu clusteru (skupině vícecestných komponent s podobným zpožděním a úhlem) přiřazena hodnota ASD. Celková impulsní odezva kanálu je konstruována sečtením příspěvků z více takových clusterů, z nichž každý má své vlastní ASD, azimutální úhel odchodu (AoD) a další parametry, jako je rozprostření zpoždění a rozprostření elevace. Parametr ASD přímo ovlivňuje prostorovou korelační matici na straně vysílače. Tato korelace určuje, jak efektivně lze více anténních prvků využít pro prostorové multiplexování ([MIMO](/mobilnisite/slovnik/mimo/)) nebo pro formování úzkých svazků (beamforming). Například větší ASD typicky snižuje prostorovou korelaci, což může být prospěšné pro multiplexování více datových toků, ale může vyžadovat složitější beamformingové algoritmy pro soustředění energie.

V rámci specifikací 3GPP (např. TS 38.901) je ASD klíčovým vstupem pro generování realizací kanálu v simulacích na systémové a spojové úrovni. Modely definují několik typických hodnot ASD odpovídajících různým scénářům nasazení, jako jsou Urban Macro (UMa), Urban Micro (UMi), Rural Macro (RMa), Indoor Office (InH) a Factory (InF). Například scénář InF-DL (Indoor Factory s hustými překážkami a nízkou výškou základnové stanice) může mít větší ASD ve srovnání se scénářem RMa kvůli většímu množství lokálních rozptylovačů. Tyto standardizované hodnoty zajišťují konzistentní a srovnatelná hodnocení výkonu v rámci průmyslu pro funkce jako massive MIMO, koordinovaný multipoint (CoMP) a správu mobility.

Role ASD v síti je zásadní pro správu rádiových zdrojů a plánování sítě. Přesným modelováním úhlových charakteristik kanálu mohou výrobci síťových zařízení a operátoři navrhovat anténní pole, beamformingové kodexy a plánovací algoritmy optimalizované pro očekávané podmínky šíření. Například znalost ASD pomáhá určit vhodnou vzdálenost anténních prvků a počet svazků potřebných pro efektivní pokrytí sektoru buňky. Je vnitřně propojena s dalšími parametry kanálu, jako je rozprostření zpoždění ([DS](/mobilnisite/slovnik/ds/)) a rozprostření elevace odchodu ([ESD](/mobilnisite/slovnik/esd/)), a společně poskytují komplexní prostorově-časový profil rádiového kanálu nezbytný pro vývoj a nasazení 5G NR a budoucích 6G systémů.

## K čemu slouží

Parametr ASD byl zaveden, aby umožnil realistické a standardizované modelování prostorových vlastností rádiových kanálů pro pokročilé anténní systémy. Před podrobnými prostorovými modely kanálu v 3GPP se systémové simulace často spoléhaly na příliš zjednodušené předpoklady o kanálu, které přesně nezachycovaly charakteristiky v úhlové doméně. To bylo nedostatečné pro hodnocení výkonu nových technologií, jako jsou [MIMO](/mobilnisite/slovnik/mimo/) a beamforming, které zásadně závisí na prostorové struktuře kanálu. Vytvoření ASD spolu s dalšími parametry úhlového rozprostření řešilo potřebu předpovídat, jak se signální energie úhlově šíří od vysílače, což je klíčové pro hodnocení zisku prostorového multiplexování, zisku beamforming a interference mezi uživateli.

Motivace vychází z vývoje směrem k sítím využívajícím anténní pole s velkým počtem prvků (massive MIMO). Výkon takových systémů je vysoce citlivý na úhlové rozprostření kanálu. Například v prostředí s vysokým ASD se kanály uživatelů více dekorelují, což umožňuje základnové stanici obsluhovat více uživatelů současně na stejném časově-frekvenčním zdroji s minimální interferencí (multi-user MIMO). Naopak ve scénářích s nízkým ASD je beamforming vysoce efektivní pro rozšíření pokrytí. Definováním ASD ve standardech poskytlo 3GPP společný referenční bod pro průmysl, aby mohl navrhovat, testovat a porovnávat výkon různých anténních řešení a algoritmů za konzistentních a realistických podmínek kanálu.

Historicky, jak 3GPP postupovalo od LTE (4G) k NR (5G), modely kanálu se staly sofistikovanějšími, aby podporovaly vyšší frekvence (včetně mmWave) a složitější nasazení. Zařazení ASD do specifikací jako TS 38.901 (model kanálu pro NR) bylo motivováno potřebou přesně modelovat tyto nové scénáře, od tradičních makro buněk po vnitřní továrny a vysokorychlostní vlaky. Řeší problém nerealistických projekcí výkonu tím, že zakládá systémová hodnocení na statistikách kanálu odvozených z měření v reálném světě, a zajišťuje tak, že slibované zisky pokročilých anténních technologií jsou dosažitelné v reálných nasazeních.

## Klíčové vlastnosti

- Kvantifikuje úhlovou disperzi odcházejících vícecestných signálů v azimutální rovině
- Klíčový vstupní parametr pro 3GPP prostorové modely kanálu typu CDL a TDL
- Přímo ovlivňuje prostorovou korelaci na straně vysílače a výkon MIMO
- Definován na každý šířicí cluster ve standardizovaných modelech kanálu
- Scénářově závislé hodnoty (např. UMa, UMi, InF) pro realistické modelování
- Nezbytný pro hodnocení technik beamforming, massive MIMO a CoMP

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.753** (Rel-19) — Spatial Channel Model Study for NR Demodulation
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 38.827** (Rel-16) — NR MIMO OTA Radiated Metrics & Test Methodology
- **TR 38.858** (Rel-18) — Technical Report on Evolution of NR Duplex Operation
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [ASD na 3GPP Explorer](https://3gpp-explorer.com/glossary/asd/)
