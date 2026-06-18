---
slug: "tid"
url: "/mobilnisite/slovnik/tid/"
type: "slovnik"
title: "TID – Terminal Identification"
date: 2025-01-01
abbr: "TID"
fullName: "Terminal Identification"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tid/"
summary: "Terminal Identification (TID, identifikace terminálu) je standardizovaný identifikátor pro uživatelský terminál nebo mobilní stanici, jak je definován v doporučení CCITT F.200. V systémech 3GPP se pou"
---

TID je standardizovaný identifikátor pro uživatelský terminál, používaný v protokolech 3GPP jako GTP k jednoznačné identifikaci kontextu terminálu pro správu mobility a řízení datových relací.

## Popis

Terminal Identification (TID, identifikace terminálu) je klíčový identifikátor používaný v protokolech jádra sítě 3GPP k jednoznačné referenci konkrétního mobilního terminálu nebo uživatelského zařízení (UE). Jeho formát a použití jsou v souladu s doporučením [ITU-T](/mobilnisite/slovnik/itu-t/) (dříve [CCITT](/mobilnisite/slovnik/ccitt/)) F.200. TID je strukturován ze dvou hlavních částí: pole TID Data a pole TID Type. TID Data obsahuje samotný identifikátor, kterým je často International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)) nebo hodnota odvozená od IMSI. TID Type udává formát a povahu dat obsažených v poli TID Data, což síti umožňuje je správně interpretovat. Jeho hlavní operační role je v rámci [GPRS](/mobilnisite/slovnik/gprs/) Tunnelling Protocol ([GTP](/mobilnisite/slovnik/gtp/)), konkrétně v GTP Control Plane ([GTP-C](/mobilnisite/slovnik/gtp-c/)). Během procedur, jako je aktivace, aktualizace nebo zrušení kontextu Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)), je TID zahrnut v GTP zprávách k jednoznačné identifikaci kontextu UE jak na Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)), tak na Gateway GPRS Support Node (GGSN), které se v EPS vyvinuly na MME/SGW/PGW. To zajišťuje, že signalizační události a události správy mobility jsou přesně asociovány se správným terminálem, zejména ve scénářích zahrnujících aktualizace směrovací oblasti mezi SGSN nebo předávání mezi systémy (handover) mezi sítěmi 2G/3G a 4G.

## K čemu slouží

Účelem TID je poskytnout spolehlivý, standardizovaný a jednoznačný identifikátor pro mobilní terminál v rámci síťových signalizačních protokolů, konkrétně těch, které zpracovávají paketové datové relace. Před rozšířenou standardizací bylo řízení uživatelských relací napříč různými síťovými uzly od různých dodavatelů problematické kvůli možným konfliktům nebo chybným interpretacím identifikátorů. Zavedení TID založeného na CCITT F.200 to vyřešilo tím, že poskytlo dobře definovaný, strukturovaný identifikátor, který může nést různé typy ID terminálů (jako IMSI) s explicitní indikací typu. To bylo zvláště kritické pro vývoj GPRS a později paketových jader 3G/4G, kde bylo třeba přesně sledovat a spravovat datovou relaci uživatele (PDP kontext), když se uživatel pohyboval mezi síťovými oblastmi nebo mezi různými generacemi technologie rádiového přístupu. Umožňuje správné směrování řídicích zpráv, přesnou asociaci záznamů pro účtování a robustní správu mobility, čímž tvoří základní prvek pro bezproblémové mobilní datové služby.

## Klíčové vlastnosti

- Standardizovaný formát založený na doporučení ITU-T F.200
- Skládá se z pole TID Data a pole TID Type
- Primárně používán v signalizačních zprávách GTP-C
- Jednoznačně identifikuje PDP kontext nebo kontext správy relace UE
- Umožňuje správu mobility mezi uzly a mezi systémy
- Běžně nese jako svá data IMSI nebo síťově specifický identifikátor

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)

## Definující specifikace

- **TS 23.044** (Rel-4) — GSM Teletex Service Support
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management

---

📖 **Anglický originál a plná specifikace:** [TID na 3GPP Explorer](https://3gpp-explorer.com/glossary/tid/)
