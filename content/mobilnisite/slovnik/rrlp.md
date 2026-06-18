---
slug: "rrlp"
url: "/mobilnisite/slovnik/rrlp/"
type: "slovnik"
title: "RRLP – Radio Resource LCS Protocol"
date: 2025-01-01
abbr: "RRLP"
fullName: "Radio Resource LCS Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rrlp/"
summary: "Radio Resource LCS Protocol (RRLP) je lokalizační protokol používaný v sítích GSM a UMTS pro výměnu lokalizačně relevantních informací mezi mobilní stanicí (MS) a sítí. Podporuje síťově asistované i m"
---

RRLP je protokol Radio Resource LCS Protocol používaný v sítích GSM a UMTS pro výměnu lokalizačních informací mezi mobilní stanicí (MS) a sítí, který podporuje metody jako Cell-ID, OTDOA a A-GPS.

## Popis

Radio Resource [LCS](/mobilnisite/slovnik/lcs/) Protocol (RRLP) je aplikační protokol vrstvy 3 definovaný pro funkci Location Services (LCS) v sítích 2G GSM a 3G UMTS. Funguje jako peer-to-peer protokol mezi cílovou mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a Serving Mobile Location Centre ([SMLC](/mobilnisite/slovnik/smlc/)) nebo Location Measurement Unit ([LMU](/mobilnisite/slovnik/lmu/)). Zprávy protokolu jsou přenášeny přes stávající signalizační spojení rádiového rozhraní, typicky pomocí mechanismu [DTAP](/mobilnisite/slovnik/dtap/) (Direct Transfer Application Part), který je přenáší uvnitř zpráv vyšších vrstev mezi MS a jádrem sítě, které je následně předává SMLC.

RRLP definuje sadu požadavků a odpovědí pro usnadnění různých metod určování polohy. Klíčové procedury zahrnují poskytnutí asistenčních dat ze sítě MS a doručení lokalizačních měření nebo vypočítané polohy z MS do sítě. Například při určování polohy Assisted-GPS ([A-GPS](/mobilnisite/slovnik/a-gps/)) odešle SMLC zprávu RRLP Assistance Data obsahující efemeridy [GPS](/mobilnisite/slovnik/gps/) satelitů, almanach a časové informace do MS. MS tato data použije pro rychlé zachycení GPS signálů a následně odpoví zprávou RRLP Measure Position Response obsahující měření pseudovzdáleností nebo vypočítanou zeměpisnou šířku/délku.

Protokol podporuje více metod určování polohy: Cell-ID (s volitelným časovým předstihem), Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) pro UMTS a Enhanced Observed Time Difference (E-OTD) pro GSM. Pro OTDOA síť poskytuje asistenční data o časování sousedních buněk a MS měří pozorované časové rozdíly přijímaných pilotních signálů. RRLP přenáší tato měření zpět do SMLC, která polohu vypočítá. Protokol je navržen tak, aby byl efektivní při omezené šířce pásma rádiového rozhraní, a používá kompaktní informační elementy (IE) pro kódování asistenčních dat a výsledků měření. Jeho činnost je řízena požadavkem LCS klienta, který specifikuje požadovanou kvalitu služby (QoS) pro lokalizaci, jako je přesnost a doba odezvy.

## K čemu slouží

RRLP byl vytvořen za účelem standardizace signalizace potřebné pro síťově a mobilně založené určování polohy v sítích GSM a UMTS, aby splňoval regulatorní (např. E911) a komerční požadavky na služby založené na poloze. Před standardizovanými protokoly, jako je RRLP, existovala proprietární řešení, která bránila interoperabilitě mezi síťovými prvky a terminály od různých výrobců. RRLP poskytl univerzální jazyk pro komunikaci související s polohou přes rozhraní vzdušného přenosu.

Vyřešil problém s umožněním přesného určování polohy v terminálech, které nemusí mít plné, autonomní GPS schopnosti. Poskytnutím síťové asistence (A-GPS) RRLP dramaticky snižuje čas do prvního určení polohy (TTFF), zlepšuje citlivost pro provoz v interiérech a snižuje spotřebu energie terminálu. Pro síťově založené metody, jako je OTDOA, poskytl mechanismus pro síť, aby mohla vyžádat specifická rádiová měření z terminálu pro výpočet jeho polohy, a to i bez GPS. Vytvoření RRLP bylo klíčovým krokem k tomu, aby se spolehlivé, standardizované lokalizační služby staly všudypřítomnou vlastností mobilních sítí, což umožnilo služby záchranného systému, navigaci, sledování vozového parku a řadu dalších aplikací.

## Klíčové vlastnosti

- Podporuje více metod určování polohy (Cell-ID, OTDOA/E-OTD, A-GPS)
- Definuje procedury pro přenos asistenčních dat pro určování polohy ze sítě do MS
- Přenáší lokalizační měření (např. pseudovzdálenosti, OTDOA) nebo vypočítanou polohu z MS do sítě
- Funguje přes standardní signalizační kanály rádiového rozhraní (s využitím transportu DTAP)
- Obsahuje parametry QoS pro lokalizační požadavky (přesnost, doba odezvy)
- Protokol definován v ASN.1, což zajišťuje jednoznačné kódování/dekódování

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification
- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol
- **TS 48.018** (Rel-19) — BSS-SGSN Interface for GPRS Control

---

📖 **Anglický originál a plná specifikace:** [RRLP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rrlp/)
