---
slug: "tlli"
url: "/mobilnisite/slovnik/tlli/"
type: "slovnik"
title: "TLLI – Temporary Logical Link Identifier"
date: 2025-01-01
abbr: "TLLI"
fullName: "Temporary Logical Link Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tlli/"
summary: "Dočasný identifikátor používaný v sítích GSM a GPRS k jednoznačné adresaci mobilní stanice (MS) na vrstvě řízení logického spoje (LLC). Je přidělován sítí během procedur GPRS připojení nebo aktualizac"
---

TLLI je dočasný identifikátor používaný v sítích GSM a GPRS k jednoznačné adresaci mobilní stanice (MS) na vrstvě LLC pro přenos dat a signalizaci se SGSN.

## Popis

Temporary Logical Link Identifier (TLLI) je 32bitový identifikátor hrající klíčovou roli v provozu sítí [GPRS](/mobilnisite/slovnik/gprs/) a [EDGE](/mobilnisite/slovnik/edge/). Jednoznačně identifikuje spojení logického spoje mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a obsluhujícím GPRS uzlem ([SGSN](/mobilnisite/slovnik/sgsn/)) na podsložce [LLC](/mobilnisite/slovnik/llc/) (Logical Link Control). TLLI je odvozen od identifikátoru [P-TMSI](/mobilnisite/slovnik/p-tmsi/) (Packet-Temporary Mobile Subscriber Identity) a používá se v souvislosti s ním. Existuje několik typů TLLI definovaných způsobem odvození: Lokální TLLI (odvozené od P-TMSI přiděleného aktuálním SGSN), Cizí TLLI (odvozené od P-TMSI přiděleného předchozím SGSN), Náhodné TLLI (náhodně zvolené MS, pokud nemá platné P-TMSI) a Pomocné TLLI (používané v určitých specifických procedurách). MS zahrnuje TLLI v hlavičce každého LLC rámce, který vysílá směrem k síti (uplink). Síť (SGSN) používá toto TLLI k asociaci rámce se správným kontextem MS, který obsahuje parametry relace, údaje o předplatném a informace o poloze. Opačně, když SGSN posílá data směrem k MS (downlink), adresuje LLC rámec pomocí TLLI dané MS. Platnost TLLI je omezena na směrovací oblast; pokud se MS přesune do nové směrovací oblasti obsluhované jiným SGSN, je odvozeno nové TLLI z nového P-TMSI. Tato lokální platnost poskytuje vrstvu ochrany soukromí identity účastníka, protože skutečný [IMSI](/mobilnisite/slovnik/imsi/) je přes rozhraní přenášen jen zřídka. TLLI je zásadní pro multiplexování – síťová infrastruktura jej používá ke směrování LLC datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)) mezi správným SGSN a správnou základnovou stanicí (BSS) pro cílovou MS, čímž spravuje sdílené rádiové zdroje mezi více simultánními uživateli.

## K čemu slouží

TLLI bylo zavedeno spolu s GPRS, aby poskytlo efektivní a bezpečnou metodu pro identifikaci mobilních datových relací na vrstvě logického spoje. Předchozí okruhově spínaný GSM používal pro signalizaci TMSI (Temporary Mobile Subscriber Identity), ale neměl ekvivalentní trvalý identifikátor pro paketové datové toky. Cíle návrhu TLLI byly několikeré: Za prvé, vyhnout se častému přenosu trvalé identity účastníka (IMSI) přes rozhraní rádiového přístupu, čímž se zvyšuje soukromí a bezpečnost. Za druhé, poskytnout síti prostředek pro správu stavu spojení logického spoje, včetně řízení toku a obnovy chyb na vrstvě LLC. Za třetí, umožnit efektivní správu zdrojů v BSS a SGSN, protože tyto uzly mohou použít kompaktní TLLI k rychlému vyhledání rozsáhlého kontextu MS potřebného pro zpracování každého datového paketu. Svou dočasností a lokální platností zjednodušuje přenos kontextu během aktualizací směrovací oblasti mezi SGSN. TLLI vyřešilo problém, jak podporovat více souběžných paketových datových relací (logických spojů) k jedné MS a od ní a přes sdílený rádiový kanál, čímž vytvořilo základní adresovací mechanismus pro paketovou mobilitu 2G/3G.

## Klíčové vlastnosti

- 32bitový lokálně jednoznačný identifikátor pro spojení na vrstvě LLC
- Odvozen od P-TMSI pro zachování vazby na kontext účastníka
- Typy zahrnují Lokální, Cizí, Náhodné a Pomocné TLLI
- Přítomen v hlavičce každého LLC rámce pro adresaci uplink i downlink
- Platnost je omezena na směrovací oblast z důvodu soukromí a efektivní správy kontextu
- Umožňuje multiplexování datových toků od více MS přes sdílená rozhraní Gb/lu-ps

## Související pojmy

- [P-TMSI – Packet-Temporary Mobile Subscriber Identity](/mobilnisite/slovnik/p-tmsi/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 24.065** (Rel-4) — GPRS Subnetwork Dependent Convergence Protocol
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.065** (Rel-19) — GPRS SNDCP Specification

---

📖 **Anglický originál a plná specifikace:** [TLLI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tlli/)
