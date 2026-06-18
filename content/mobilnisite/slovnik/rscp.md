---
slug: "rscp"
url: "/mobilnisite/slovnik/rscp/"
type: "slovnik"
title: "RSCP – Reference Signal Carrier Phase"
date: 2025-01-01
abbr: "RSCP"
fullName: "Reference Signal Carrier Phase"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rscp/"
summary: "RSCP je měření absolutní fáze nosné vlny přijatého referenčního signálu v systémech 3GPP. Je klíčové pro přesnou synchronizaci rádiové frekvence a představuje hlavní vstup pro pokročilé metody určován"
---

RSCP je měření absolutní fáze nosné vlny přijatého referenčního signálu v systémech 3GPP, používané pro přesnou synchronizaci, pokročilé určování polohy a podporu beamformingu.

## Popis

Reference Signal Carrier Phase (RSCP) je klíčové měření na fyzické vrstvě definované napříč více vydáními 3GPP, od [R99](/mobilnisite/slovnik/r99/) až po Rel-19. Kvantifikuje absolutní fázi nosné vlny, na které je specifický referenční signál (např. pilotní nebo synchronizační signál) přijímán uživatelským zařízením (UE) nebo základnovou stanicí. Toto měření se netýká výkonu signálu, ale přesné úhlové pozice rádiové vlny v bodě příjmu. Proces měření zahrnuje uzamčení přijímače na příchozí referenční signál, odstranění datové modulace a porovnání fáze zbylé nosné vlny s lokálním, vysoce stabilním referenčním oscilátorem. Výsledek je typicky vyjádřen v radiánech nebo stupních a představuje akumulovaný fázový posun způsobený přenosovou cestou, včetně uražené vzdálenosti a různých zkreslení kanálu.

Architektonicky je funkce měření RSCP integrována do řetězců zpracování fyzické vrstvy jak v UE, tak v síťovém zařízení. Mezi klíčové zapojené komponenty patří fázové závěsy (PLL) přijímače, lokální oscilátory a specializované jednotky pro zpracování referenčních signálů. Síť poskytuje konfiguraci těchto měření prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), přičemž specifikuje, které referenční signály (např. Primary Synchronization Signal ([PSS](/mobilnisite/slovnik/pss/)), Secondary Synchronization Signal ([SSS](/mobilnisite/slovnik/sss/)) nebo Cell-Specific Reference Signal ([CRS](/mobilnisite/slovnik/crs/))) se mají měřit, a požadovaná kritéria pro hlášení. Naměřená hodnota RSCP je poté hlášena zpět síti, často spolu s dalšími měřeními, jako je Reference Signal Received Power ([RSRP](/mobilnisite/slovnik/rsrp/)), aby vytvořila komplexní obraz o rádiovém spojení.

V síťovém ekosystému hraje RSCP klíčovou roli v pokročilých funkcích, především pro určování polohy. Slouží jako přímý vstup pro metody určování polohy založené na fázi. Například v LTE a 5G NR může metoda určování polohy Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) využívat měření RSCP z více buněk k výpočtu velmi přesných časových rozdílů, které se převádějí na hyperpřesné odhady polohy. Fáze nosné vlny poskytuje mnohem jemnější rozlišení než samotná časová měření, což umožňuje přesnost na úrovni centimetrů za ideálních podmínek. Dále je RSCP nezbytné pro koherentní beamforming a operace Massive [MIMO](/mobilnisite/slovnik/mimo/), kde je znalost absolutní fáze na více anténních prvcích nutná k vytvoření konstruktivních interferenčních vzorů směrem ke konkrétnímu UE, čímž se dramaticky zlepšuje spektrální účinnost a pokrytí.

## K čemu slouží

Vytvoření a standardizace RSCP bylo motivováno rostoucí poptávkou po službách určování polohy s vysokou přesností, které přesahují možnosti globálních navigačních satelitních systémů (GNSS), zejména v interiérech a městských kaňonech, kde jsou satelitní signály slabé nebo nedostupné. Tradiční měření založená na výkonu, jako je RSRP, byla pro špendlíkovou přesnost nedostatečná. Měřením fáze nosné vlny, což je mnohem stabilnější a přesnější metrika než síla signálu nebo hrubé časování, získaly systémy 3GPP nativní schopnost pro sofistikované terestriální určování polohy.

Historicky, před formální integrací a měřením RSCP napříč vydáními 3GPP, se síťové určování polohy silně spoléhalo na metody časového předstihu (timing advance), buněčného ID a úhlu příchodu, které nabízely přesnost pouze v řádu stovek metrů. Zavedení RSCP, zejména jako součásti sady protokolů pro určování polohy v LTE, řešilo omezení hrubého rozlišení. Umožnilo přechod z přesnosti na úrovni metrů na přesnost na úrovni decimetrů nebo dokonce centimetrů pro podporovaná UE, čímž splnilo regulační požadavky na lokalizaci nouzových volajících (např. E911) a umožnilo nové komerční aplikace, jako je sledování majetku, rozšířená realita a automaticky řízená vozidla.

Probíhající evoluce napříč vydáními 3GPP odráží jeho trvalý účel: sloužit jako základní metrika pro jakoukoli síťovou funkci vyžadující extrémní přesnost rádiové frekvence. Jak se sítě vyvíjely ze 4G na 5G a dále, potřeba přesného fázového zarovnání se stala ještě kritičtější pro technologie, jako je koordinovaný vícebodový přenos a příjem (CoMP), a pro synchronizaci distribuovaných anténních systémů v architekturách cloud RAN (C-RAN). RSCP poskytuje surová fázová data nezbytná pro efektivní fungování těchto komplexních kooperativních technik.

## Klíčové vlastnosti

- Měří absolutní fázi nosné vlny specifických referenčních signálů (např. PSS, SSS, CRS)
- Poskytuje vstup pro techniky určování polohy s vysokou přesností, jako je OTDOA
- Nezbytné pro koherentní beamforming a precoding Massive MIMO
- Konfigurováno a hlášeno prostřednictvím signalizačních protokolů RRC
- Používá se pro ověření a kalibraci síťové synchronizace
- Podporuje pokročilé přijímací algoritmy, jako jsou fázové závěsné smyčky

## Související pojmy

- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.215** (Rel-19) — UTRA FDD Measurement Definitions
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TS 25.800** (Rel-12) — UMTS Heterogeneous Networks Study
- **TS 25.865** (Rel-10) — Distributed Antenna Enhancements for TDD
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [RSCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rscp/)
