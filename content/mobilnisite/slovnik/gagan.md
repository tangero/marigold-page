---
slug: "gagan"
url: "/mobilnisite/slovnik/gagan/"
type: "slovnik"
title: "GAGAN – GPS Aided Geo Augmented Navigation"
date: 2025-01-01
abbr: "GAGAN"
fullName: "GPS Aided Geo Augmented Navigation"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gagan/"
summary: "Satelitní augmentační systém (SBAS), který zlepšuje přesnost, integritu a dostupnost signálů GPS pro letectví a další přesné aplikace. Poskytuje korigovaná polohová data pro zvýšení bezpečnosti naviga"
---

GAGAN je satelitní augmentační systém, který zlepšuje přesnost, integritu a dostupnost signálů GPS pro letectví a další přesné aplikace.

## Popis

[GPS](/mobilnisite/slovnik/gps/) Aided Geo Augmented Navigation (GAGAN) je satelitní augmentační systém ([SBAS](/mobilnisite/slovnik/sbas/)) vyvinutý pro indický region a standardizovaný v rámci 3GPP pro integraci s mobilními sítěmi. Zlepšuje výkon globálního polohového systému (GPS) poskytováním korekčních dat a informací o integritě prostřednictvím geostacionárních satelitů. Systém se skládá ze sítě pozemních referenčních stanic, které monitorují signály GPS, hlavních řídicích center, která data zpracovávají za účelem generování korekčních zpráv, a stanic pro uplink, které tyto zprávy vysílají na geostacionární satelity pro následné vysílání uživatelům.

V rámci architektury 3GPP je GAGAN relevantní pro polohové služby, zejména pro funkce Assisted-GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). Specifikace definují, jak mohou být augmentační data GAGAN doručena uživatelskému zařízení (UE) prostřednictvím mobilních sítí za účelem zlepšení přesnosti určení polohy a času do prvního fixu. Systém funguje tak, že měří chyby v signálech GPS způsobené ionosférickým zpožděním, nepřesnostmi satelitních hodin a odchylkami oběžné dráhy. Tyto korekce chyb jsou vypočítány v pozemním segmentu a následně vysílány, což umožňuje přijímačům dosáhnout polohové přesnosti v řádu několika metrů, což je klíčové pro aplikace týkající se bezpečnosti života, jako je letecká navigace.

Mezi klíčové komponenty patří GAGAN Signal-in-Space (SIS), který vysílá korekční zprávy na frekvenci [L1](/mobilnisite/slovnik/l1/) (1575,42 MHz), a síť indických referenčních stanic (INRES). V kontextech 3GPP mohou protokoly jako Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) přenášet pomocná data GAGAN do uživatelských zařízení (UE). Úlohou GAGAN v mobilních sítích je poskytovat spolehlivý zdroj polohování s vysokou přesností, který doplňuje jiné metody, jako je Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) nebo fúze senzorů, zejména v regionech, kde je dostupné pokrytí GAGAN. Tato integrace podporuje aplikace vyžadující přesnou polohu, jako jsou záchranné služby, navigace a geofencing.

## K čemu slouží

GAGAN byl vyvinut za účelem řešení omezení samostatného [GPS](/mobilnisite/slovnik/gps/), kterému chybí dostatečná přesnost, monitoring integrity a dostupnost pro kritické aplikace, jako je navigace letadel v indickém vzdušném prostoru. Samotný GPS může mít chyby až 10 metrů a více kvůli atmosférickým vlivům a chybám satelitních hodin, což je pro přesné přiblížení v letectví nepřijatelné. Motivací bylo vytvořit regionální augmentační systém, který splňuje přísné požadavky Mezinárodní organizace pro civilní letectví (ICAO) pro služby týkající se bezpečnosti života (SoL).

Historicky vyvinuly jiné regiony podobné SBAS, jako jsou WAAS (USA), EGNOS (Evropa) a MSAS (Japonsko). Pro Indii poskytl GAGAN řešení šité na míru pro zlepšení výkonu GPS nad jejím geografickým územím, včetně odlehlých a oceánských oblastí. Jeho integrace do standardů 3GPP, počínaje Release 8, umožnila mobilním sítím využít tuto vylepšenou schopnost určování polohy, což umožnilo nové služby vyžadující vysokou přesnost a spolehlivost. Tím se vyřešilo předchozí omezení, kdy samotné metody polohování v mobilních sítích nedokázaly dosáhnout submetrové přesnosti vyžadované pro aplikace jako autonomní vozidla, precizní zemědělství a pokročilé asistenční systémy řidiče (ADAS).

## Klíčové vlastnosti

- Poskytuje data pro korekci chyb satelitů GPS v reálném čase
- Vysílá výstrahy integrity k varování před nespolehlivými signály GPS
- Zlepšuje horizontální a vertikální přesnost na úroveň do 3 metrů
- Používá geostacionární satelity pro širokoplošné pokrytí nad Indií
- Podporuje aplikace týkající se bezpečnosti života (SoL), včetně letectví
- Integrován s protokoly 3GPP A-GNSS pro doručování do mobilních zařízení

## Související pojmy

- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [SBAS – Satellite Based Augmentation Systems](/mobilnisite/slovnik/sbas/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.455** (Rel-19) — NR Positioning Protocol A (NRPPa)
- **TS 44.031** (Rel-19) — Radio Resource LCS Protocol (RRLP)

---

📖 **Anglický originál a plná specifikace:** [GAGAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/gagan/)
