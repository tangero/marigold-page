---
slug: "udptl"
url: "/mobilnisite/slovnik/udptl/"
type: "slovnik"
title: "UDPTL – Facsimile UDP Transport Layer"
date: 2025-01-01
abbr: "UDPTL"
fullName: "Facsimile UDP Transport Layer"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/udptl/"
summary: "Protokol definovaný 3GPP pro přenos faxových (facsimile) dat po IP sítích pomocí UDP. Umožňuje přenos faxu v reálném čase v paketově spínaných prostředích, jako je IMS, a poskytuje opravu chyb a adapt"
---

UDPTL je 3GPP protokol pro přenos faxových dat v reálném čase po IP sítích pomocí UDP, který umožňuje přenos v paketově spínaných prostředích, jako je IMS, s možností opravy chyb a adaptací na síť.

## Popis

Facsimile [UDP](/mobilnisite/slovnik/udp/) Transport Layer (UDPTL) je protokol standardizovaný v rámci 3GPP pro podporu služeb faksimilního přenosu (skupina 3) v reálném čase po IP sítích, jako je IP Multimedia Subsystem (IMS). Funguje tak, že zapouzdřuje faxovou signalizaci a obrazová data do UDP datagramů, využívá nízkou latenci UDP a přidává mechanismy pro zvládání ztráty paketů a jitteru, které jsou pro IP sítě typické. UDPTL definuje strukturu paketu, která zahrnuje pořadová čísla pro uspořádání, primární a sekundární schémata pro opravu chyb (jako redundance nebo [FEC](/mobilnisite/slovnik/fec/)) a indikátory pro faxové řídicí signály. To umožňuje faxovým přístrojům nebo bránám bezproblémovou komunikaci přes paketové sítě a napodobuje spolehlivost tradičního faksimile přes okruhově spínanou telefonní síť ([PSTN](/mobilnisite/slovnik/pstn/)).

Architektonicky funguje UDPTL jako adaptační vrstva mezi faxovým protokolem T.30 – používaným pro navázání relace a přenos stránek – a podkladovým transportem UDP/IP. V typickém nasazení 3GPP, jako je fax-over-IP založený na IMS, používá uživatelské zařízení (UE) nebo mediální brána UDPTL pro odesílání a příjem faxových paketů. Protokol funguje tak, že rozděluje faxová data na samostatné UDPTL pakety, z nichž každý obsahuje část naskenovaného obrazu nebo řídicí příkaz. Pro potlačení ztráty paketů může obsahovat redundantní kopie předchozích dat nebo kódy pro opravu chyb vpřed (FEC), což umožňuje přijímači rekonstruovat chybějící informace bez zpoždění způsobeného opakovaným přenosem. To je klíčové pro fax v reálném čase, kde přísné časové požadavky vylučují použití opakovaných přenosů ve stylu TCP.

Role UDPTL v sítích 3GPP je primárně v rámci služebních prostředků pro multimediální komunikaci, zajišťuje zpětnou kompatibilitu se staršími faxovými službami během přechodu na plně IP infrastruktury. Je specifikován v kontextech jako IMS Multimedia Telephony (MMTel) a circuit-switched fallback, což operátorům umožňuje nabízet fax jako součást jejich hlasových služeb. Návrh protokolu vyvažuje efektivitu a robustnost: použitím UDP se vyhne latenci spojovaného navazování spojení u TCP, ale díky vestavěné opravě chyb si zachovává dostatečnou spolehlivost pro faxový přenos. To činí z UDPTL klíčovou komponentu pro konvergenci tradičních telefonních služeb na moderní paketové sítě a podporuje tak obchodní a regulatorní požadavky na faxovou komunikaci v mobilním i pevném prostředí.

## K čemu slouží

UDPTL byl vyvinut pro řešení výzvy přenosu faksimilního provozu v reálném čase po IP sítích, která vyvstala s migrací z okruhově spínané na paketově spínanou telefonii. Tradiční fax přes [PSTN](/mobilnisite/slovnik/pstn/) spoléhal na vyhrazené okruhy se zaručenou šířkou pásma a minimálním zpožděním, zatímco IP sítě přinášejí ztrátu paketů, proměnnou latenci a jitter, které mohou narušit faxové relace. Počáteční pokusy použít standardní TCP pro fax vedly k vypršením časových limitů a selháním kvůli zpožděním při opakovaném přenosu a řízení přetížení u TCP, které jsou nekompatibilní s přísnými požadavky faxu na přenos v reálném čase.

3GPP přijalo UDPTL, aby umožnilo spolehlivé faxové služby v IMS a dalších architekturách založených na IP, a vyřešilo tak problém zachování kompatibility faxu ve světě plně IP. Bylo motivováno potřebou podporovat starší obchodní a regulatorní faxové aplikace – jako je podepisování dokumentů a právní oznámení – během přechodu na sítě 4G a 5G. UDPTL poskytuje speciální transportní vrstvu, která napodobuje spolehlivost okruhově spínaného faxu, aniž by obětovala efektivitu [UDP](/mobilnisite/slovnik/udp/), a zahrnuje techniky opravy chyb, které umožňují faxovým datům přečkat typické poruchy IP sítí. To zajišťuje, že operátoři mohou nabízet nepřetržité faxové služby při vyřazování starších sítí, a usnadňuje tak hladký vývoj směrem k plně paketovým komunikačním systémům.

## Klíčové vlastnosti

- Zapouzdřuje protokol T.30 pro fax přes UDP pro transport s nízkou latencí
- Obsahuje pořadová čísla pro uspořádání paketů a detekci ztrát
- Podporuje opravu chyb pomocí redundance a opravy chyb vpřed (FEC)
- Adaptuje se na síťové podmínky s konfigurovatelnými intervaly paketizace
- Umožňuje přenos faxu v reálném čase v IMS a paketově spínaných sítích
- Poskytuje zpětnou kompatibilitu se staršími faxovými přístroji skupiny 3

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [UDP – User Datagram Protocol](/mobilnisite/slovnik/udp/)
- [MMTEL – Multimedia Telephony Service for IMS](/mobilnisite/slovnik/mmtel/)

## Definující specifikace

- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling

---

📖 **Anglický originál a plná specifikace:** [UDPTL na 3GPP Explorer](https://3gpp-explorer.com/glossary/udptl/)
