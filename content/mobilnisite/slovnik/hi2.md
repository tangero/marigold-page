---
slug: "hi2"
url: "/mobilnisite/slovnik/hi2/"
type: "slovnik"
title: "HI2 – Handover Interface Port 2"
date: 2025-01-01
abbr: "HI2"
fullName: "Handover Interface Port 2"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hi2/"
summary: "HI2 je standardizované rozhraní pro zákonný odposlech, konkrétně pro doručování informací souvisejících s odposlechem (IRI) od operátora sítě k monitorovacímu zařízení orgánů činných v trestním řízení"
---

HI2 je standardizované rozhraní používané v rámci zákonného odposlechu pro doručování informací souvisejících s odposlechem (Intercept Related Information, IRI) od operátora sítě k monitorovacímu zařízení orgánů činných v trestním řízení (Law Enforcement Monitoring Facility, LEMF).

## Popis

Handover Interface Port 2 (HI2) je klíčové rozhraní definované v rámci architektury zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)) podle 3GPP, standardizované v technické specifikaci 33.108. Slouží jako mechanismus pro doručování informací souvisejících s odposlechem (Intercept Related Information, [IRI](/mobilnisite/slovnik/iri/)), což jsou data spojená s hovorem nebo signalizační informace týkající se komunikace sledovaného subjektu. Rozhraní HI2 spojuje mediční funkci (Mediation Function, [MF](/mobilnisite/slovnik/mf/)) nebo doručovací funkci (Delivery Function, [DF](/mobilnisite/slovnik/df/)) v doméně operátora sítě s monitorovacím zařízením orgánů činných v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)) provozovaným vládní agenturou. Hlavní rolí HI2 je přenos strukturovaných dat IRI, která zahrnují podrobnosti jako identity volajícího a volaného (např. [MSISDN](/mobilnisite/slovnik/msisdn/), [IMSI](/mobilnisite/slovnik/imsi/)), čas začátku a konce hovoru, dobu trvání, informace o poloze (pokud jsou dostupné) a události doplňkových služeb. Tato data poskytují kontext a metadata komunikační relace bez samotného hlasového nebo datového obsahu.

Architektura HI2 je navržena tak, aby zajistila bezpečné, spolehlivé a standardizované doručování odposlechových dat. Rozhraní používá specifické protokoly a formáty kódování, typicky založené na ASN.1 a kódované pomocí [BER](/mobilnisite/slovnik/ber/) (Basic Encoding Rules) nebo PER (Packed Encoding Rules), aby byla zajištěna interoperabilita mezi zařízeními různých dodavatelů a systémy LEMF. Komunikace přes HI2 je obecně zahájena odposlechovým systémem operátora sítě při detekci události související s monitorovaným cílem. Data jsou zabalena do definovaných zpráv (např. IRI pro hovor, IRI pro SMS, IRI pro aktualizaci polohy) a přenesena do LEMF. Bezpečnost je prvořadá, proto specifikace rozhraní zahrnuje požadavky na zabezpečený přenos, často implementovaný přes vyhrazené, chráněné sítě nebo pomocí VPN a silného šifrování, aby se zabránilo neoprávněnému přístupu k citlivým odposlechovým datům.

HI2 funguje ve spojení s HI3 (pro obsah komunikace) a HI1 (pro aktivaci a deaktivaci odposlechu). Zatímco HI3 přenáší samotný hlasový hovor nebo datový obsah, HI2 poskytuje nezbytná metadata, která zachycený obsah činí srozumitelným a použitelným pro orgány činné v trestním řízení. Oddělení řídicí/rozhraní pro data (IRI na HI2) a uživatelské roviny (obsah na HI3) sleduje jasný architektonický princip v rámci 3GPP LI. Rozhraní musí podporovat vysokou spolehlivost a přesné řazení událostí za účelem zachování právně přijatelné auditní stopy. Jeho implementace je povinná pro operátory sítí v jurisdikcích se zákonnými požadavky na odposlech, což z něj činí základní komponentu pro splnění požadavků v rámci bezpečnostních a mediačních vrstev jádra sítě.

## K čemu slouží

HI2 bylo vytvořeno za účelem standardizace doručování informací souvisejících s odposlechem (Intercept Related Information, IRI) z telekomunikačních sítí k orgánům činným v trestním řízení. Před zavedením standardizace různé země a dodavatelé síťového vybavení používali proprietární rozhraní a formáty pro doručování odposlechových dat, což vedlo k problémům s interoperabilitou, vysokým nákladům pro orgány činné v trestním řízení na integraci s více sítěmi a potenciálním právním výzvám ohledně přípustnosti důkazů. Standardizace 3GPP, počínaje Release 8, si kladla za cíl vytvořit jednotné, dodavatelsky neutrální rozhraní, které by zjednodušilo zákonný odposlech pro operátory a zajistilo spolehlivé a konzistentní doručování dat pro orgány.

Hnací silou za HI2 a širším rámcem 3GPP LI jsou zákonné mandáty v mnoha zemích, které vyžadují, aby operátoři sítí poskytovali technické možnosti pro zákonný odposlech. Tyto zákony jsou navrženy tak, aby podporovaly národní bezpečnost a vyšetřování trestné činnosti. Definováním HI2 řeší 3GPP provozní potřebu zabezpečeného a efektivního kanálu pro přenos metadat spojených s hovorem. Tato metadata jsou pro vyšetřování často stejně kritická jako samotný obsah komunikace, neboť stanovují kdo, kdy a kde komunikace probíhala. Rozhraní řeší problém fragmentovaných, neinteroperabilních řešení a umožňuje orgánům činným v trestním řízení přijímat standardizované datové přenosy z jakékoli kompatibilní sítě, ať už 2G, 3G, 4G nebo 5G, čímž zajišťuje budoucí použitelnost odposlechových schopností s vývojem síťové technologie.

## Klíčové vlastnosti

- Standardizované doručování informací souvisejících s odposlechem (IRI) k orgánům činným v trestním řízení
- Přenáší metadata spojená s hovorem (např. účastníci, časová razítka, poloha)
- Používá protokoly založené na ASN.1 (např. standardy ETSI LI) pro kódování
- Navrženo pro zabezpečený a spolehlivý přenos přes vyhrazené spoje
- Funguje v tandemu s rozhraními HI1 (aktivace) a HI3 (obsah)
- Zajišťuje splnění zákonných požadavků pro operátory sítí v regulovaných trzích

## Související pojmy

- [HI3 – Handover Interface Port 3](/mobilnisite/slovnik/hi3/)
- [HI1 – Handover Interface Port 1 (for Administrative Information)](/mobilnisite/slovnik/hi1/)
- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [HI2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/hi2/)
