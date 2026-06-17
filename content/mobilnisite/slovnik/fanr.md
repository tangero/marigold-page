---
slug: "fanr"
url: "/mobilnisite/slovnik/fanr/"
type: "slovnik"
title: "FANR – Fast Ack/Nack Reporting"
date: 2025-01-01
abbr: "FANR"
fullName: "Fast Ack/Nack Reporting"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fanr/"
summary: "Funkce GSM/EDGE, která urychluje doručování potvrzovacích (ACK) nebo záporně potvrzovacích (NACK) zpráv paketových dat ze sítě k mobilní stanici. Snižuje dobu odezvy (RTT), čímž zvyšuje propustnost da"
---

FANR je funkce GSM/EDGE, která urychluje doručování potvrzovacích zpráv paketových dat, čímž snižuje dobu odezvy (RTT) a zvyšuje propustnost.

## Popis

Fast Ack/Nack Reporting (FANR, rychlé hlášení potvrzení/negativního potvrzení) je vylepšení vrstvy řízení rádiového spoje (RLC) v sítích GSM/[EDGE](/mobilnisite/slovnik/edge/), konkrétně v kontextu protokolu paketových dat ([GPRS](/mobilnisite/slovnik/gprs/), EDGE). Jeho hlavní funkcí je optimalizace procesu potvrzování datových bloků přenášených po směru dolů (downlink) ze sítě ([BSS](/mobilnisite/slovnik/bss/)) k mobilní stanici ([MS](/mobilnisite/slovnik/ms/)). Ve standardním provozu odesílá MS potvrzení o přijatých datových blocích na uplinkovém kanálu PACCH (Packet Associated Control Channel) podle předdefinovaného okna a časování. FANR umožňuje síti tato hlášení [ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/) výrazně urychlit jejich 'přibalováním' do hlaviček downlinkových datových bloků, které jsou již přenášeny.

Z architektonického hlediska FANR funguje ve vrstvě protokolu RLC/[MAC](/mobilnisite/slovnik/mac/) definované v BSS a v MS. Klíčovou součástí je rozšířená hlavička RLC datového bloku, která obsahuje pole pro 'Relative Reserved Block Period (RRBP)'. Toto pole používá síť k přidělení uplinkového zdroje MS pro odesílání potvrzení. V mechanismu FANR může síť také zahrnout indikátor 'Interleaving Depth' a další řídicí prvky, které jí umožňují naplánovat vysílání potvrzení od MS s minimálním zpožděním. Když má síť připraven downlinkový datový blok k odeslání, může vypočítat očekávaný stav potvrzení z předchozích přenosů a zahrnout preventivní hlášení ACK/NACK pro uplinková data MS v hlavičce downlinkového bloku.

Jak to funguje, zahrnuje těsnou koordinaci uplinkových a downlinkových přenosů. Síť, která má lepší celkový přehled o plánech přenosů, používá pole RRBP k přiřazení konkrétního uplinkového bloku, na kterém má MS odeslat svou řídicí zprávu RLC/MAC (obsahující ACK/NACK). Pečlivým plánováním tohoto přiřazení síť snižuje dobu čekání v cyklu potvrzování. Tím se efektivně zkracuje doba odezvy (RTT) vrstvy RLC. Kratší RTT umožňuje efektivně používat menší velikost přenosového okna, snižuje zpoždění při retransmisích a umožňuje rychlejší adaptaci modulačního a kódového schématu ([MCS](/mobilnisite/slovnik/mcs/)). Celkovým efektem je významné zvýšení vnímané datové propustnosti a odezvy služby paketových dat, zejména pro provoz založený na TCP, který je citlivý na zpoždění odezvy.

## K čemu slouží

FANR byl vyvinut k řešení klíčového výkonnostního omezení v paketových datech GSM/EDGE (EGPRS): latence procesu potvrzování. V původním návrhu GPRS/EDGE mohla být doba mezi odesláním downlinkového datového bloku a přijetím jeho potvrzení od MS značná kvůli pevným časovým strukturám (rádiové bloky) a zpožděním v plánování. Tato dlouhá doba odezvy (RTT) omezovala efektivní propustnost, zejména pro interaktivní aplikace jako prohlížení webu, a zvyšovala latenci při retransmisích v případě chyb.

Tato technologie byla motivována potřebou učinit sítě EDGE konkurenceschopnějšími vůči nově se objevujícím 3G datovým službám vytěžením maximálního výkonu z existujícího GSM spektra a infrastruktury. Řeší problém neefektivního využití rádiového spoje způsobeného obdobími čekání na potvrzení. Urychlením hlášení ACK/NACK umožňuje FANR protokolu RLC pracovat s těsnějšími časovými okny, což vede k rychlejším retransmisím chybných bloků (zlepšení spolehlivosti spoje) a rychlejšímu sledu nových datových bloků (zvýšení datového toku). Jeho zavedení bylo součástí souboru funkcí EDGE Evolution, jejichž cílem bylo posunout teoretické a praktické limity technologie GSM/EDGE pro podporu vyšších datových rychlostí a nižších latencí bez nutnosti zásadní přestavby sítě.

## Klíčové vlastnosti

- Snižuje dobu odezvy (RTT) vrstvy RLC pro potvrzení
- Využívá přibalování řídicích informací do hlaviček downlinkových datových bloků
- Používá pole Relative Reserved Block Period (RRBP) pro rychlé plánování uplinku
- Zvyšuje propustnost a snižuje latenci služeb paketových dat
- Optimalizuje výkon pro TCP/IP a interaktivní aplikace
- Je součástí souboru funkcí EDGE Evolution pro sítě GSM

## Související pojmy

- [EGPRS – Enhanced GPRS](/mobilnisite/slovnik/egprs/)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 45.001** (Rel-19) — GSM Physical Layer Introduction
- **TS 45.002** (Rel-19) — GSM/EDGE Radio Physical Layer Specification
- **TS 45.003** (Rel-19) — Channel Coding and Multiplexing for GSM/EDGE
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [FANR na 3GPP Explorer](https://3gpp-explorer.com/glossary/fanr/)
