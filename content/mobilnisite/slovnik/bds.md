---
slug: "bds"
url: "/mobilnisite/slovnik/bds/"
type: "slovnik"
title: "BDS – BeiDou Navigation Satellite System"
date: 2025-01-01
abbr: "BDS"
fullName: "BeiDou Navigation Satellite System"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bds/"
summary: "BDS je čínský globální družicový navigační systém integrovaný do standardů 3GPP, který poskytuje služby polohování, navigace a časové synchronizace (PNT) pro mobilní zařízení. Umožňuje služby založené"
---

BDS je čínský globální družicový navigační systém integrovaný do standardů 3GPP za účelem poskytování služeb polohování, navigace a časové synchronizace (PNT) pro mobilní zařízení, čímž rozšiřuje schopnosti buněčných sítí.

## Popis

Družicový navigační systém BeiDou (BDS) je satelitní rádiový navigační systém vlastněný a provozovaný Čínou. V rámci architektury 3GPP je BDS standardizován jako globální družicový navigační systém ([GNSS](/mobilnisite/slovnik/gnss/)) pro polohování uživatelského zařízení (UE). Architektura systému se skládá ze tří segmentů: kosmického segmentu (družice), pozemního řídicího segmentu (hlavní řídicí stanice, stanice pro upload, monitorovací stanice) a uživatelského segmentu (přijímače v UE). Kosmický segment zahrnuje konstelaci družic na geostacionární dráze ([GEO](/mobilnisite/slovnik/geo/)), na nakloněné geosynchronní dráze ([IGSO](/mobilnisite/slovnik/igso/)) a na střední oběžné dráze ([MEO](/mobilnisite/slovnik/meo/)), což poskytuje globální pokrytí se zvýšenou regionální službou v oblasti Asie a Tichomoří.

BDS funguje tak, že vysílá přesné časové signály a navigační zprávy ze svých družic. UE vybavené přijímačem BDS měří čas příchodu signálů z více viditelných družic. Pomocí těchto měření a známých poloh družic (efemeridní data z navigačních zpráv) si UE vypočítá svou polohu pomocí trilaterace. Systém poskytuje více služebních signálů v různých kmitočtových pásmech (např. [B1](/mobilnisite/slovnik/b1/), [B2](/mobilnisite/slovnik/b2/), B3), nabízejících otevřené (civilní) a autorizované (vojenské/zabezpečené) služby. Signály využívají modulaci s kódovým dělením ([CDMA](/mobilnisite/slovnik/cdma/)) se specifickými pseudonáhodnými šumovými kódy (PRN) pro identifikaci družic.

V architektuře 3GPP je BDS integrován prostřednictvím protokolů pro polohování v řídicí a uživatelské rovině, definovaných ve specifikacích jako TS 36.355 (LTE Positioning Protocol - [LPP](/mobilnisite/slovnik/lpp/)) a TS 38.455 (NR Positioning Protocol A - NRPPa). Síť může asistovat UE poskytováním pomocných dat, jako jsou efemeridy družic, almanach a časové informace, prostřednictvím protokolu LPP nebo NRPPa, což snižuje čas do prvního určení polohy (TTFF) a zlepšuje energetickou účinnost. Funkce správy polohy (LMF) v 5G jádru sítě nebo rozšířené středisko polohy mobilní stanice (E-SMLC) v LTE spravuje tyto relace polohování a vyžaduje BDS měření od UE nebo gNB/ng-eNB.

Role BDS je klíčová pro splnění regulačních požadavků (např. určení polohy nouzového volajícího), pro umožnění služeb založených na poloze (LBS) a pro podporu aplikací, jako je sledování vozidel, monitorování majetku v IoT a navigace. Jeho integrace umožňuje hybridní polohování s jinými systémy GNSS (jako GPS, Galileo) a pozemními metodami (OTDOA, E-CID), čímž se zvyšuje přesnost, dostupnost a spolehlivost. Výkon je charakterizován parametry, jako je přesnost (na úrovni metrů pro otevřenou službu), integrita a kontinuita, specifikovanými v dokumentech s testovacími požadavky, jako je TS 37.571.

## K čemu slouží

BDS byl vytvořen, aby poskytl Číně nezávislou globální družicovou navigační schopnost a snížil závislost na zahraničních systémech, jako je GPS (USA) a GLONASS (Rusko). Jeho integrace do standardů 3GPP reaguje na potřebu diverzifikovaných a odolných zdrojů služeb polohování, navigace a časové synchronizace (PNT) v mobilních sítích. Před jeho zahrnutím bylo buněčné polohování primárně závislé na GPS, což představovalo rizika týkající se dostupnosti, suverenity a kontinuity služeb v určitých regionech nebo během konfliktů.

Motivace pro standardizaci BDS v 3GPP, počínaje Release 8, bylo umožnit celosvětovou interoperabilitu a podporu čínských družicových signálů v komerčních mobilních zařízeních. To umožňuje síťovým operátorům a výrobcům zařízení využívat BDS pro zlepšený výkon polohování, zejména v oblasti Asie a Tichomoří, kde jsou jeho signály silnější díky regionálnímu posílení družic. Řeší problémy selhání jediného bodu v PNT službách a zlepšuje přesnost určení polohy v městských kaňonech nebo náročném prostředí prostřednictvím vícekonstelačních přijímačů GNSS.

Historicky nabízely rané metody buněčného polohování, jako je Cell-ID, nízkou přesnost, zatímco pozdější techniky, jako Assisted-GPS (A-GPS), přesnost zlepšily, ale byly vázány na specifické konstelace GNSS. Integrace BDS spolu s dalšími systémy GNSS poskytuje robustnější a přesnější řešení, které podporuje nové požadavky autonomních vozidel, navigace dronů a přesné časové synchronizace pro synchronizaci sítě. Plní také čínské regulační povinnosti pro nouzové služby a národní bezpečnost, čímž zajišťuje domácí kontrolu nad kritickou infrastrukturou.

## Klíčové vlastnosti

- Poskytuje globální služby polohování, navigace a časové synchronizace (PNT) prostřednictvím družicové konstelace
- Nabízí otevřené (civilní) a autorizované (zabezpečené/vojenské) služební signály v několika kmitočtových pásmech (např. B1, B2, B3)
- Podporuje hybridní polohování s jinými systémy GNSS (GPS, Galileo, GLONASS) a pozemními metodami v sítích 3GPP
- Umožňuje síťově asistované polohování prostřednictvím protokolů LPP/NRPPa ke snížení TTFF a spotřeby energie UE
- Poskytuje zvýšené regionální pokrytí služeb a přesnost v oblasti Asie a Tichomoří prostřednictvím družic GEO/IGSO
- Zahrnuje satelitní systém pro zvýšení přesnosti (SBAS) a službu krátkých textových zpráv v regionálním režimu

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.306** (Rel-19) — UE Radio Access Capabilities Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [BDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/bds/)
