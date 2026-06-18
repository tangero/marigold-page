---
slug: "pdch"
url: "/mobilnisite/slovnik/pdch/"
type: "slovnik"
title: "PDCH – Packet Data Channel"
date: 2025-01-01
abbr: "PDCH"
fullName: "Packet Data Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pdch/"
summary: "Vyhrazený fyzický kanál v sítích GSM/GPRS/EDGE používaný pro přenos paketově přepínaného uživatelského datového provozu. Umožňuje efektivní přenos dat dynamickou alokací rádiových zdrojů na základě po"
---

PDCH je vyhrazený fyzický kanál v sítích GSM/GPRS/EDGE, který přenáší paketově přepínaná uživatelská data, a dynamicky alokuje rádiové zdroje pro umožnění služeb mobilního internetu v systémech 2G a 2.5G.

## Popis

Packet Data Channel (PDCH) je základní fyzický zdroj v paketově přepínaných sítích založených na GSM ([GPRS](/mobilnisite/slovnik/gprs/) a [EDGE](/mobilnisite/slovnik/edge/)). Představuje časový slot na GSM rozhraní (rozhraní Um), který je alokován pro přenos paketových dat namísto tradičního okruhově přepínaného hlasu. PDCH je vytvořen z fondu dostupných časových slotů na nosné frekvenci GSM. V síťové architektuře je PDCH spravován podsystémem základnových stanic ([BSS](/mobilnisite/slovnik/bss/)), konkrétně základnovou přenosovou stanicí ([BTS](/mobilnisite/slovnik/bts/)) a řídicí jednotkou paketů ([PCU](/mobilnisite/slovnik/pcu/)). PCU je klíčový logický uzel, často integrovaný do BTS nebo řadiče základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)), odpovědný za správu rádiových zdrojů, plánování a segmentaci/skládání datových paketů pro přenos přes PDCH.

Z pohledu protokolu slouží PDCH jako fyzická vrstva pro protokol řízení rádiového spoje/řízení přístupu k médiu ([RLC](/mobilnisite/slovnik/rlc/)/[MAC](/mobilnisite/slovnik/mac/)). Uživatelská data z protokolu řízení logického spoje (LLC) vyšší vrstvy jsou segmentována do RLC datových bloků. Tyto bloky spolu s hlavičkami MAC pro alokaci zdrojů a řízení jsou pak namapovány na fyzické rádiové bity přenášené na PDCH. Kanál podporuje více kódovacích schémat (CS-1 až CS-4 v GPRS a vyšší modulační a kódovací schémata (MCS) v EDGE) pro přizpůsobení datového toku rádiovým podmínkám. PDCH může pracovat v různých režimech: jako vyhrazený PDCH trvale alokovaný pro paketová data, nebo jako PDCH na vyžádání, který může být vytvořen z kanálu pro přenos (TCH) při vysokém zatížení paketovými daty.

Jeho úlohou v síti je poskytovat základní rádiový přenosový kanál pro služby paketových dat. Kapacita buňky GPRS/EDGE je přímo určena počtem nakonfigurovaných PDCH. Síťoví operátoři spravují alokaci PDCH pro vyvážení okruhově přepínaného hlasového a paketově přepínaného datového provozu. Dynamická a sdílená povaha zdrojů PDCH, kde více uživatelů může být multiplexováno na jediný časový slot, byl revoluční krok odlišný od vyhrazeného, spojově orientovaného modelu GSM hlasu, který umožnil 'vždy připojený' zážitek a efektivní využití spektra pro rané služby mobilních dat.

## K čemu slouží

PDCH byl vytvořen pro zavedení schopností paketově přepínaných dat do původně pouze okruhově přepínané sítě GSM. Před GPRS vyžadovaly služby GSM dat, jako Circuit-Switched Data (CSD) a High-Speed Circuit-Switched Data (HSCSD), vyhrazení celého přenosového kanálu (TCH) jednomu uživateli po dobu trvání relace, což bylo pro trhaný, interaktivní datový provoz typický pro internetové aplikace velmi neefektivní. Tato neefektivita omezovala přijetí dat a uživatelský zážitek.

Hlavním problémem, který PDCH řešil, bylo umožnění efektivního sdíleného využití vzácného a drahého rádiového spektra pro data. Díky možnosti statistického multiplexování datových paketů více uživatelů na jediný fyzický časový slot dramaticky zlepšil spektrální účinnost pro trhaný provoz. Tento přístup sdíleného kanálu také umožnil model připojení 'vždy připojen', kdy uživatel zůstával logicky připojen k síti bez nepřetržitého obsazování vyhrazeného fyzického zdroje, což byl klíčový požadavek pro e-mail, prohlížení webu a instant messaging. Vytvoření PDCH spolu s jádrem sítě GPRS představovalo přechod mobilních sítí od čistě hlasově orientovaných k platformám pro obecné datové služby a položilo základy pro mobilní internet.

## Klíčové vlastnosti

- Dynamická alokace časových slotů z nosné GSM pro paketová data
- Podporuje statistický multiplexing datového provozu více uživatelů
- Využívá více kódovacích schémat (CS-1 až CS-4) pro adaptaci spoje
- Může pracovat jako vyhrazený (trvalý) nebo na vyžádání (přeměněný z TCH)
- Fyzický přenosový kanál pro vrstvu protokolu RLC/MAC
- Základ pro zvýšené datové toky prostřednictvím modulačních a kódovacích schémat (MCS) EDGE

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [PCU – Packet Control Unit](/mobilnisite/slovnik/pcu/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 43.868** (Rel-12) — GERAN Improvements for MTC Feasibility Study
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PDCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdch/)
