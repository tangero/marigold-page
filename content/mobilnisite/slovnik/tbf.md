---
slug: "tbf"
url: "/mobilnisite/slovnik/tbf/"
type: "slovnik"
title: "TBF – Temporary Block Flow"
date: 2025-01-01
abbr: "TBF"
fullName: "Temporary Block Flow"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tbf/"
summary: "Jednosměrné logické spojení v sítích GPRS a EDGE používané k přenosu posloupnosti RLC/MAC bloků mezi mobilní stanicí a sítí na paketovém datovém kanálu (PDCH). Je základní jednotkou přidělování prostř"
---

TBF je základní dynamicky navázané jednosměrné logické spojení v sítích GPRS a EDGE pro přenos posloupnosti RLC/MAC bloků na paketovém datovém kanálu pro každý datový burst.

## Popis

Temporary Block Flow (TBF) je klíčový koncept v rádiové přístupové síti General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)) a Enhanced Data rates for GSM Evolution ([EDGE](/mobilnisite/slovnik/edge/)). Představuje spojení na fyzické vrstvě používané pro přenos jedné nebo více jednotek [LLC](/mobilnisite/slovnik/llc/) [PDU](/mobilnisite/slovnik/pdu/) (Logical Link Control Protocol Data Unit) v jednom směru (buď uplink, nebo downlink) mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a sítí. TBF je, jak název napovídá, dočasné a je udržováno pouze po dobu přenosu dat. Přiděluje rádiové prostředky na jednom nebo více paketových datových kanálech ([PDCH](/mobilnisite/slovnik/pdch/)), což jsou časové sloty nakonfigurované pro přenos paketových dat.

Zřízení TBF je iniciováno sítí pro downlinkový přenos nebo mobilní stanicí pro uplinkový přenos, a to na základě potřeby odeslat data. Proces zahrnuje žádost o kanál (na náhodném přístupovém kanálu [RACH](/mobilnisite/slovnik/rach/) nebo paketovém náhodném přístupovém kanálu [PRACH](/mobilnisite/slovnik/prach/)) a následné zprávy o přidělení (na přístupovém grantovém kanálu AGCH nebo přidruženém řídicím kanálu pro pakety PACCH). Zpráva o přidělení specifikuje PDCH(y) a hodnoty příznaku uplinkového stavu (USF) pro uplinková TBF, nebo identifikátor TFI (Temporary Flow Identity) pro adresování bloků. TBF využívá protokol RLC/MAC (Radio Link Control/Medium Access Control). Data jsou segmentována do RLC datových bloků, které jsou přenášeny v rámci přidělených časových slotů PDCH. Každý blok je identifikován pomocí TFI, což příjemci umožňuje znovu sestavit bloky patřící ke stejnému TBF.

Klíčovou charakteristikou je jeho směrovost: mobilní stanice může mít současně jedno uplinkové TBF a jedno downlinkové TBF, která jsou řízena nezávisle. Řízení aktivního TBF, jako jsou potvrzení a řízení prostředků, probíhá na kanálu PACCH přidruženém k přidělenému PDCH. TBF je explicitně uvolněno řídicí zprávou nebo implicitně po vypršení časovače po úspěšném přenosu všech dat. Toto dynamické přidělování na vyžádání umožňuje efektivní sdílené využití rádiových prostředků pro burstový přenos paketových dat, což je v kontrastu s trvalými okruhově spínanými spojeními používanými pro hlas.

## K čemu slouží

TBF bylo vytvořeno za účelem zavedení efektivních paketově spínaných datových služeb do původně okruhově spínané sítě GSM. Před GPRS používaly datové služby GSM okruhově spínané spojení, které na celou dobu relace vyhradilo celý časový slot, což bylo pro přerušovaný, burstový datový provoz, jako je prohlížení webu nebo e-mail, neefektivní a drahé. Mechanismus TBF tento problém vyřešil tím, že umožnil více uživatelům statisticky sdílet stejné fyzické rádiové prostředky (časové sloty).

Řešil základní problém přidělování prostředků pro nepředvídatelná paketová data. Tím, že se spojení navázalo pouze v případě, že byla data k odeslání, a okamžitě se po přenosu uvolnilo, mohla být rádiová kapacita rychle znovu využita mezi mnoha uživateli. To zvýšilo celkovou kapacitu sítě a snížilo cenu za bit. TBF spolu s přidruženým konceptem PDCH bylo klíčovou inovací, která transformovala GSM ze sítě pouze pro hlas na platformu pro mobilní přístup k internetu a položila základy pro pozdější paketově spínané architektury 3G a 4G. Jeho návrh přímo ovlivnil pozdější koncepty, jako je Enhanced Dedicated Channel (E-DCH) v HSPA a přidělování prostředků založené na plánování v LTE a NR.

## Klíčové vlastnosti

- Jednosměrné, point-to-point logické spojení
- Dynamicky navazované a uvolňované pro každý datový burst
- Přiděluje prostředky na jednom nebo více paketových datových kanálech (PDCH)
- Používá identifikátor TFI (Temporary Flow Identity) pro adresování bloků
- Řízeno procedurami vrstvy RLC/MAC
- Umožňuje statistické multiplexování více uživatelů na sdílených kanálech

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)
- [PDCH – Packet Data Channel](/mobilnisite/slovnik/pdch/)
- [TFI – Transport Format Identification](/mobilnisite/slovnik/tfi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.914** (Rel-19) — Multimedia Telephony over IP Optimization
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures
- **TR 45.902** (Rel-19) — Flexible Layer One (FLO) for GERAN

---

📖 **Anglický originál a plná specifikace:** [TBF na 3GPP Explorer](https://3gpp-explorer.com/glossary/tbf/)
