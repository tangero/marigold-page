---
slug: "icmp"
url: "/mobilnisite/slovnik/icmp/"
type: "slovnik"
title: "ICMP – Internet Control Message Protocol"
date: 2025-01-01
abbr: "ICMP"
fullName: "Internet Control Message Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/icmp/"
summary: "Síťový protokol používaný pro diagnostiku a hlášení chyb v IP sítích. Umožňuje zařízením komunikovat stav sítě, jako jsou nedostupné cíle nebo překročení času, a podporuje nástroje jako ping a tracero"
---

ICMP je síťový protokol používaný pro diagnostiku a hlášení chyb v IP sítích, který umožňuje zařízením komunikovat stav sítě a podporuje nástroje jako ping a traceroute.

## Popis

Internet Control Message Protocol (ICMP) je podpůrný protokol v rámci sady protokolů Internet Protocol (IP), který funguje na síťové vrstvě (vrstva 3). Primárně jej používají síťová zařízení, jako jsou směrovače a hostitelé, k odesílání chybových zpráv a provozních informací oznamujících například, že požadovaná služba není dostupná nebo že hostitel či směrovač nelze dosáhnout. Zprávy ICMP jsou zapouzdřeny v IP paketech, ale na rozdíl od TCP nebo [UDP](/mobilnisite/slovnik/udp/) se nepoužívají pro přenos dat koncového uživatele. Mezi běžné typy zpráv ICMP patří Echo Request a Echo Reply (používané příkazem ping), Destination Unreachable, Time Exceeded (používané příkazem traceroute) a Redirect. V sítích 3GPP je ICMP relevantní pro IP komunikaci mezi uživatelským zařízením (UE) a externími sítěmi, stejně jako v rámci jádra sítě pro provoz a údržbu. Protokol je bezstavový, což znamená, že každá zpráva je zpracována nezávisle, a obsahuje kontrolní součet pro detekci chyb. Zatímco ICMP je základní pro funkčnost IP sítí, specifikace 3GPP na něj často odkazují v kontextu spolupráce s externími IP sítěmi (např. Internet) a pro testování konektivity, ale samotné jádrové protokoly 3GPP (jako [GTP](/mobilnisite/slovnik/gtp/) nebo Diameter) zpracovávají většinu signalizace řídicí roviny interně.

## K čemu slouží

ICMP byl vytvořen, aby poskytl mechanismus pro komunikaci řídicích a chybových informací mezi zařízeními v IP síti. V počátcích vývoje Internetu byl protokol IP navržen pro doručování datagramů metodou "best-effort" bez vnitřních mechanismů pro hlášení selhání doručení nebo zahlcení sítě. ICMP tento problém řeší tím, že umožňuje směrovačům a cílovým hostitelům odesílat zpětnou vazbu zdroji o problémech zjištěných při zpracování paketů, jako jsou nedostupní hostitelé, potřeba fragmentace nebo přesměrování směrování. Tato schopnost je klíčová pro síťovou diagnostiku, umožňuje správcům identifikovat problémy s konektivitou, měřit doby odezvy a trasovat síťové cesty. V kontextu 3GPP, zatímco jádro mobilní sítě (např. [GPRS](/mobilnisite/slovnik/gprs/), EPS, 5GC) používá vlastní sadu protokolů pro správu mobility a relací, ICMP zůstává nezbytný, když UE komunikují s externími IP sítěmi. Zajišťuje, že IP aplikace běžící přes přístup 3GPP mohou využívat standardní internetové diagnostické nástroje, a tím zachovávají interoperabilitu s globálním Internetem.

## Klíčové vlastnosti

- Hlášení chyb při zpracování IP paketů
- Podpora síťových diagnostických nástrojů (ping, traceroute)
- Zapouzdření v rámci IP paketů (číslo protokolu 1)
- Bezstavový provoz s typy zpráv a kódy
- Pole kontrolního součtu pro ověření integrity dat
- Zpracovává zprávy o nedostupnosti cíle, překročení času a problémech s parametry

## Související pojmy

- [IP – IP Packet eXchange](/mobilnisite/slovnik/ip/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 33.749** (Rel-19) — Study on security aspects of edge computing enhancement

---

📖 **Anglický originál a plná specifikace:** [ICMP na 3GPP Explorer](https://3gpp-explorer.com/glossary/icmp/)
