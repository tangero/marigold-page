---
slug: "aes"
url: "/mobilnisite/slovnik/aes/"
type: "slovnik"
title: "AES – Advanced Encryption Standard"
date: 2026-01-01
abbr: "AES"
fullName: "Advanced Encryption Standard"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/aes/"
summary: "AES je symetrická bloková šifra standardizovaná institutem NIST a přijatá organizací 3GPP pro zabezpečení uživatelských dat a signalizace. Poskytuje silnou ochranu důvěrnosti a integrity pro provoz na"
---

AES je standardizovaná symetrická bloková šifra přijatá organizací 3GPP, která poskytuje silnou ochranu důvěrnosti a integrity pro zabezpečení uživatelských dat a signalizačního provozu přes rozhraní vzduchového rozhraní a páteřní síť.

## Popis

Advanced Encryption Standard (AES) je symetrická bloková šifra, která šifruje a dešifruje data v blocích pevné velikosti, typicky 128 bitů, pomocí kryptografických klíčů o délce 128, 192 nebo 256 bitů. V systémech 3GPP je AES implementována jako základní kryptografický prvek v rámci různých bezpečnostních algoritmů definovaných ve specifikacích. Funguje prostřednictvím více kol substitučních, permutačních a míchacích operací (SubBytes, ShiftRows, MixColumns a AddRoundKey) na stavovém poli reprezentujícím datový blok. Počet transformačních kol – 10, 12 nebo 14 – závisí na délce klíče a zajišťuje vysokou úroveň difúze a záměny pro odolnost proti kryptoanalýze.

Z architektonického hlediska je AES integrována do bezpečnostního rámce 3GPP prostřednictvím specifických algoritmů pro důvěrnost a integritu. Například v LTE a 5G jsou algoritmy 128-EEA1 a 128-EIA1 založeny na AES v režimu Counter ([CTR](/mobilnisite/slovnik/ctr/)) pro šifrování a na AES v režimu CMAC pro ochranu integrity. V sadě bezpečnostních algoritmů pro 5G definované v TS 33.501 je AES základní složkou pro algoritmy NEA0, NIA0 (nulové algoritmy pro migraci) a pro 128/256bitové varianty rodin [NEA](/mobilnisite/slovnik/nea/) a [NIA](/mobilnisite/slovnik/nia/). Algoritmus je prováděn v rámci uživatelského zařízení (UE) a bezpečnostních entit sítě, jako je Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) a Security Anchor Function ([SEAF](/mobilnisite/slovnik/seaf/)), aby chránil jak data uživatelské roviny, tak signalizační zprávy řídicí roviny.

Její role v síti je klíčová pro zajištění end-to-end bezpečnosti. Pro ochranu vzduchového rozhraní zabezpečuje AES signalizaci Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a uživatelská data mezi UE a základnovou stanicí (gNB/[eNB](/mobilnisite/slovnik/enb/)) prostřednictvím vrstvy [PDCP](/mobilnisite/slovnik/pdcp/). V páteřní síti může být použita v bezpečnostních protokolech pro zabezpečení síťové domény (NDS/IP), jak je specifikováno v TS 33.210. Návrh algoritmu umožňuje efektivní hardwarovou i softwarovou implementaci, což je zásadní pro splnění požadavků na nízkou latenci a vysokou propustnost moderních mobilních sítí včetně 5G NR. Robustnost AES proti známým útokům, jako je lineární a diferenciální kryptoanalýza, podpírá model důvěry systémů 3GPP a chrání před odposlechem a manipulací s daty.

## K čemu slouží

AES byla vytvořena, aby řešila omezení starších šifrovacích standardů, jako je Data Encryption Standard (DES), který měl malou 56bitovou délku klíče zranitelnou vůči útokům hrubou silou. Národní institut pro standardy a technologie (NIST) vyhlásil v roce 1997 veřejnou soutěž, která vyvrcholila v roce 2001 výběrem algoritmu Rijndael jako AES. Její přijetí organizací 3GPP, počínaje Release 8 pro LTE, bylo motivováno potřebou silné, veřejně prověřené a bezlicenční šifry, která by nahradila zastaralé algoritmy založené na SNOW 3G a Kasumi používané v 3G UMTS, a poskytla tak vylepšenou bezpečnost pro vyvíjející se síťové architektury.

Hlavní problémy, které AES řeší v sítích 3GPP, jsou zajištění robustní důvěrnosti a integrity dat proti stále sofistikovanějším hrozbám. Poskytuje standardizované, vysoce výkonné kryptografické řešení, které lze efektivně implementovat na různorodém hardwaru od zařízení IoT s omezenými zdroji až po vysoce kapacitní síťové servery. Tato univerzálnost podporuje bezproblémovou bezpečnost napříč generacemi od LTE přes 5G a dále, usnadňuje bezpečnou mobilitu a kontinuitu služeb. Flexibilita AES v délkách klíčů navíc umožňuje sítím vyvážit sílu zabezpečení s výpočetní náročností a přizpůsobit se různým požadavkům služeb, jako jsou požadavky pro massive IoT nebo ultra-spolehlivou komunikaci s nízkou latencí (URLLC).

Historicky přechod na AES v 3GPP odrážel širší posun průmyslu směrem k silnější, algoritmicky transparentní bezpečnosti. Její integrace řešila zranitelnosti v předchozích algoritmech a sladila se s globálními regulačními a compliance standardy. Tím, že AES poskytuje budoucí odolný základ, umožňuje systémům 3GPP odolávat dlouhodobým kryptografickým hrozbám a zajišťuje soukromí uživatelů a integritu sítě, jak se mobilní služby rozšiřují do kritické infrastruktury a citlivých aplikací.

## Klíčové vlastnosti

- Symetrická bloková šifra s velikostí bloku 128 bitů
- Podpora délek klíčů 128, 192 a 256 bitů
- Vysoká odolnost vůči lineární a diferenciální kryptoanalýze
- Efektivní implementace jak v hardwaru, tak v softwaru
- Základ pro algoritmy důvěrnosti (EEA) a integrity (EIA) v 3GPP
- Používá se v různých režimech provozu (např. CTR, CMAC) v rámci specifikací 3GPP

## Definující specifikace

- **TR 26.805** (Rel-17) — Study on Media Production over 5G NPN Systems
- **TR 31.822** (Rel-18) — Technical Report on GBA_U based APIs
- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification
- **TS 33.210** (Rel-19) — UMTS Security for IP Networks
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.402** (Rel-19) — Security for non-3GPP access to EPS
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.700** — 3GPP TR 33.700
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)
- **TS 35.205** (Rel-19) — MILENAGE Algorithm Set: General Overview
- **TS 35.234** (Rel-19) — MILENAGE-256 Algorithm Set Specification
- **TS 35.235** (Rel-19) — MILENAGE-256 Algorithm Set Specification
- **TS 35.236** (Rel-19) — MILENAGE-256 Algorithm Set Specification
- **TS 35.249** (Rel-19) — f5** Algorithm for MILENAGE and Tuak
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [AES na 3GPP Explorer](https://3gpp-explorer.com/glossary/aes/)
