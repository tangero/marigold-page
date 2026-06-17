---
slug: "dvb"
url: "/mobilnisite/slovnik/dvb/"
type: "slovnik"
title: "DVB – Digital Video Broadcasting"
date: 2025-01-01
abbr: "DVB"
fullName: "Digital Video Broadcasting"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dvb/"
summary: "Soubor mezinárodních otevřených standardů pro digitální televizní a datové vysílání. Definuje přenosové systémy pro terestrické, satelitní, kabelové a mobilní doručování, což umožňuje efektivní distri"
---

DVB je soubor mezinárodních otevřených standardů pro digitální televizní a datové vysílání, integrovaný v 3GPP pro podporu služeb vysílání a multicastu přes různé přenosové systémy.

## Popis

Digital Video Broadcasting (DVB) je soubor mezinárodně přijímaných otevřených standardů pro digitální televizní a datové vysílání, vyvíjený projektem DVB Project. V ekosystému 3GPP jsou standardy DVB odkazovány a integrovány za účelem umožnění služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a jejího vývoje (eMBMS), což usnadňuje efektivní point-to-multipoint doručování lineární televize a obsahu na vyžádání přes mobilní sítě. Architektura využívá vysílací/multicastová servisní centra a využívá existující transportní stream DVB a protokoly pro servisní informace k zapouzdření a doručení IP datagramů přenášejících mediální streamy.

Technologie funguje definováním přenosových systémů fyzické vrstvy (jako [DVB-T](/mobilnisite/slovnik/dvb-t/), DVB-S2) a protokolů vyšších vrstev pro objevování služeb, programově specifické informace a podmíněný přístup. Ve scénáři vysílání integrovaném s 3GPP může být vysílací síť samostatná DVB síť nebo konvergovaná síť, kde základnové stanice mobilní sítě vysílají signály ve formátu DVB. Mezi klíčové komponenty patří servisní vrstva pro přípravu obsahu, transportní vrstva využívající [MPEG-2](/mobilnisite/slovnik/mpeg-2/) Transport Stream nebo IP a modulace fyzické vrstvy (např. [OFDM](/mobilnisite/slovnik/ofdm/) pro terestrické vysílání).

Její role v síti spočívá v poskytování standardizovaného, efektivního mechanismu pro vysílací doručování hromadných mediálních služeb, který doplňuje unicastové doručování v mobilních sítích. To operátorům umožňuje odlehčit síť od oblíbeného živého video provozu, snížit zahlcení páteřní sítě a zlepšit spektrální účinnost. Integrace zajišťuje kontinuitu služeb a umožňuje hybridní vysílací-broadbandové služby, kde vysílání doručuje hlavní stream a unicast poskytuje personalizaci nebo interaktivní prvky.

## K čemu slouží

DVB bylo vytvořeno za účelem zavedení jednotného, interoperabilního rámce pro přechod od analogového k digitálnímu televiznímu vysílání v Evropě a celosvětově. Vyřešilo problém fragmentovaných proprietárních vysílacích systémů tím, že poskytlo otevřené technické specifikace, které zajišťují kompatibilitu přijímačů a podporují konkurenci na trhu. Motivací bylo zlepšit spektrální účinnost, umožnit vyšší kvalitu videa (SD, [HD](/mobilnisite/slovnik/hd/), UHD) a zavést nové datové služby vedle televize.

V rámci 3GPP je účelem integrace standardů DVB využít zralé vysílací technologie pro multimediální doručování založené na mobilních sítích, konkrétně pro [MBMS](/mobilnisite/slovnik/mbms/). Tím se řeší omezení čistě unicastového doručování pro oblíbené živé události, které mohou přetížit mobilní sítě. Přijetím dobře zavedených standardů DVB pro fyzickou a servisní vrstvu mohou systémy 3GPP efektivně poskytovat vysílací služby, což operátorům umožňuje nabízet lineární televizi a doručování souborů přes sítě LTE a 5G s nižšími náklady na přenesený bit.

## Klíčové vlastnosti

- Standardizovaná modulace fyzické vrstvy (např. COFDM pro terestrické vysílání)
- MPEG-2 Transport Stream pro multiplexování a synchronizaci
- Servisní informace (SI) a programově specifické informace (PSI) pro objevování služeb
- Systémy podmíněného přístupu (CA) pro ochranu služeb
- Podpora datového vysílání (IP datacasting) vedle audio/video
- Škálovatelnost pro různé přenosová média: satelit, kabel, terestrické vysílání, mobilní sítě

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [DVB-T – Digital Video Broadcasting - Terrestrial](/mobilnisite/slovnik/dvb-t/)

## Definující specifikace

- **TR 22.816** (Rel-14) — 3GPP TV Service Enhancement Technical Report
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks
- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [DVB na 3GPP Explorer](https://3gpp-explorer.com/glossary/dvb/)
