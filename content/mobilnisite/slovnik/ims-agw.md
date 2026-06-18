---
slug: "ims-agw"
url: "/mobilnisite/slovnik/ims-agw/"
type: "slovnik"
title: "IMS-AGW – IMS Access Media Gateway"
date: 2025-01-01
abbr: "IMS-AGW"
fullName: "IMS Access Media Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ims-agw/"
summary: "Funkce v médiové rovině v rámci architektury IMS, která poskytuje schopnosti zpracování médií, ukotvení a propojování. Zpracovává mediální toky pro služby jako hlas a video, umožňuje transkódování, zá"
---

IMS-AGW je funkce v médiové rovině v rámci architektury IMS, která poskytuje zpracování médií, ukotvení a propojování pro služby jako hlas a video, a funguje pod řízením funkce řízení mediální brány (Media Gateway Control Function).

## Popis

IMS Access Media Gateway (IMS-AGW) je entita pro zpracování médií definovaná v architektuře médiové roviny IMS. Nesignalizační prvek, nýbrž funkce přenosové roviny zodpovědná za manipulaci a přeposílání uživatelských mediálních toků (hlas, video). IMS-AGW funguje pod řízením Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) nebo, konkrétněji v pozdějších architekturách, IMS Media Gateway Control Function (IMS-MGW-CF) či Media Resource Function Controller ([MRFC](/mobilnisite/slovnik/mrfc/)). Její činnost se řídí protokoly jako H.248 (Megaco) nebo jeho IMS profilem, což umožňuje řadiči dávat IMS-AGW pokyny k vytváření, modifikaci a mazání kontextů zpracování médií a terminací.

Funkčně IMS-AGW plní několik klíčových rolí. Za prvé funguje jako ukotvovací bod pro média. To je zásadní pro služby jako Voice Call Continuity ([VCC](/mobilnisite/slovnik/vcc/)) nebo Single Radio Voice Call Continuity ([SRVCC](/mobilnisite/slovnik/srvcc/)), kde je potřeba hovor plynule přenést mezi různými přístupovými sítěmi (např. z LTE/VoLTE na 3G okruhově komutovanou síť). Ukotvením média v IMS-AGW zůstává mediální cesta k protistraně nezměněna a přepojí se pouze větev k pohyblivému UE, čímž se minimalizuje přerušení. Za druhé poskytuje funkce pro propojování médií, jako je transkódování mezi různými hlasovými kodeky (např. [AMR-NB](/mobilnisite/slovnik/amr-nb/) používaný v legacy sítích na [EVS](/mobilnisite/slovnik/evs/) používaný ve VoLTE) a konverzi paketizačních protokolů (např. [RTP](/mobilnisite/slovnik/rtp/) na okruhově komutované [TDM](/mobilnisite/slovnik/tdm/) nosiče).

Za třetí IMS-AGW umožňuje služby založené na médiích, jako je konferenční hovor (míchání více audio/video toků), přehrávání tónů a oznámení a usnadnění zákonného odposlechu tím, že poskytuje řízený bod pro duplikaci mediálních toků. Architektonicky se nachází na hranici mezi plně IP doménou IMS a legacy okruhově komutovanými sítěmi nebo jinými IP sítěmi s odlišnými schopnostmi. Obsahuje prostředky jako digitální signálové procesory (DSP) pro operace s kodeky a enginy pro zpracování paketů. Oddělení řídicí (MGCF/MRFC) a mediální (IMS-AGW) složky následuje model dekompozice brány, což podporuje škálovatelnost, flexibilitu a použití standardních rozhraní.

## K čemu slouží

IMS-AGW byla zavedena, aby řešila specifické výzvy při evoluci směrem k čisté, koncové IP multimediální síti. Rané vize IMS předpokládaly přímé IP mediální cesty mezi koncovými body. Praktické nasazení však odhalilo několik scénářů, kde bylo nutné inteligentní zásahy v médiové rovině. Legacy sítě (2G/3G okruhově komutované) měly s IMS koexistovat po desetiletí, což vyžadovalo bezproblémové propojování pro hlasové hovory. Navíc ne všechna uživatelská zařízení nebo přístupové sítě podporují stejnou sadu pokročilých kodeků, což si vyžádalo transkódování pro zajištění interoperability.

Klíčovým impulzem byla potřeba kontinuity služeb při událostech mobility, zejména SRVCC. Bez mediálního ukotvení by předání VoLTE hovoru z LTE do 3G okruhově komutované sítě vyžadovalo znovunavázání celé mediální cesty s protistranou, což by způsobilo nepřijatelné přerušení zvuku. IMS-AGW poskytuje stabilní ukotvovací bod v domovské IMS síti, což umožňuje rychlou aktualizaci pouze jedné větve hovoru. Tím byl vyřešen hlavní problém pro komerční spuštění VoLTE, protože zaručil kontinuitu hlasové služby i při pohybu uživatelů mimo pokrytí LTE.

Dále regulační požadavky na zákonný odposlech vyžadovaly síťově řízený bod, kde lze média kopírovat. Distribuovaný, peer-to-peer mediální model to ztěžoval. Koncentrace zpracování médií ve spravované síťové funkci, jako je IMS-AGW, poskytla přirozený bod pro takové odposlechy. Dekompozice na samostatnou řídicí funkci (MGCF) a mediální bránu (IMS-AGW) také odpovídala širším průmyslovým trendům směrem k architekturám softswitch, což operátorům umožnilo nezávisle pořizovat hardware a software pro řízení a média a škálovat je podle různých vzorců provozu.

## Klíčové vlastnosti

- Ukotvení médií pro kontinuitu služeb při předávání mezi přístupovými sítěmi (např. SRVCC)
- Transkódování mezi různými audio a video kodeky (např. AMR na EVS, G.711)
- Propojování protokolů mezi RTP/IP a legacy okruhově komutovanými TDM nosiči
- Míchání médií pro konferenční služby pod řízením MRFC
- Podpora přehrávání tónů, oznámení a hlasových výzev
- Poskytuje řízený přístupový bod pro zákonný odposlech mediálních toků

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [SRVCC – Single Radio Voice Call Continuity](/mobilnisite/slovnik/srvcc/)
- [MRFC – Multimedia Resource Function Controller](/mobilnisite/slovnik/mrfc/)

## Definující specifikace

- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TS 29.866** (Rel-19) — IMS Disaster Prevention & Restoration Enhancement
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [IMS-AGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/ims-agw/)
