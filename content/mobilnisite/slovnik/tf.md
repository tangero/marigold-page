---
slug: "tf"
url: "/mobilnisite/slovnik/tf/"
type: "slovnik"
title: "TF – Transparent Forwarding"
date: 2025-01-01
abbr: "TF"
fullName: "Transparent Forwarding"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tf/"
summary: "Síťová funkce, která přeposílá uživatelská data a signalizaci mezi síťovými uzly bez interpretace nebo úpravy obsahu. Jedná se o klíčový mechanismus pro zajištění efektivního přenosu dat, zejména ve s"
---

TF je síťová funkce, která přeposílá uživatelská data a signalizaci mezi uzly bez interpretace nebo úpravy obsahu, aby zajistila efektivní přenos dat a jejich integritu.

## Popis

Transparentní přeposílání (TF) je základní provozní režim v architektuře radiového přístupového sítě (RAN) podle 3GPP, jehož hlavním účelem je nezměněný přenos protokolových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)) mezi síťovými entitami. Funguje jako průchozí mechanismus, kdy přeposílající uzel neukončuje uživatelskou ani řídicí rovinu protokolů pro přeposílaný provoz. To znamená, že uzel neinterpretuje, nezpracovává ani nemodifikuje obsah nebo hlavičky paketů nad rámec nezbytný pro základní směrování a přenos. Jeho role spočívá v rozšíření dosahu sítě nebo optimalizaci datové cesty bez přidání složitosti zpracování v mezilehlém bodě.

Architektonicky je TF implementováno v různých síťových prvcích, nejvýznamněji v reléových uzlech ([RN](/mobilnisite/slovnik/rn/)) definovaných pro LTE-Advanced a 5G NR. V tomto kontextu se relé využívající transparentní přeposílání jeví uživatelskému zařízení (UE) jako jednoduchý rádiový opakovač nebo zesilovač. UE komunikuje přímo s dárkovou základnovou stanicí (např. gNB nebo [eNB](/mobilnisite/slovnik/enb/)) a reléový uzel pouze zesílí a přepošle rádiové signály. Dárková základnová stanice zpracovává veškeré ukončení protokolů, plánování a správu rádiových prostředků. Relé není pro UE viditelné jako samostatná buňka, což z pohledu UE zjednodušuje procedury mobility a předávání spojení.

Z pohledu protokolového zásobníku funguje transparentní přeposílání na nižších vrstvách, typicky na fyzické vrstvě (Layer 1) nebo kombinovaných vrstvách [PHY](/mobilnisite/slovnik/phy/)/[MAC](/mobilnisite/slovnik/mac/). Nezahrnuje vyšší vrstvy protokolů, jako jsou [RLC](/mobilnisite/slovnik/rlc/), [PDCP](/mobilnisite/slovnik/pdcp/) nebo [RRC](/mobilnisite/slovnik/rrc/). Při přenosu na Layer 1 uzel přijme, zesílí a znovu vysílá analogový rádiový signál. Pokročilejší implementace mohou dekódovat a znovu kódovat digitální signál (decode-and-forward), stále však bez interpretace logického obsahu nebo správy rádiového kanálu. Klíčovým principem je absence vlastního identifikátoru buňky (Cell ID) pro relé; funguje pod identitou buňky dárkové základnové stanice.

Role TF je klíčová pro zhušťování sítě a rozšiřování pokrytí, zejména v náročných prostředích, jako jsou venkovské oblasti, vnitřní prostory nebo okraje buněk. Poskytuje nákladově efektivní řešení ve srovnání s nasazením plnohodnotných základnových stanic, protože reléový uzel vyžaduje méně složitý hardware a software, jelikož náročné zpracování přesouvá na dárkový uzel. Zajišťuje, aby uživatelská data a řídicí signalizace zachovaly svou koncovou integritu mezi základní sítí (nebo dárkovou základnovou stanicí) a UE, a tím umožňuje bezproblémové poskytování služeb.

## K čemu slouží

Transparentní přeposílání bylo zavedeno, aby řešilo základní výzvu nákladově efektivního rozšíření rádiového pokrytí a zlepšení kapacity na okrajích buněčné sítě. Nasazení plnohodnotné makro základnové stanice se vším souvisejícím hardwarem, přenosovou sítí a náklady na získání lokality je často příliš drahé pro vyplnění malých mezer v pokrytí nebo pro zlepšení síly signálu v konkrétních oblastech. TF poskytuje kompromisní řešení prostřednictvím reléových uzlů, které jsou jednodušší a levnější. Řeší problém „mrtvých zón“ a špatné kvality signálu bez složitosti správy další buňky s vlastními procedurami předávání spojení a mobility.

Historicky, před standardizací konceptu relé v 3GPP, používali operátoři proprietární zesilovače nebo opakovače signálu. Tato zařízení často způsobovala interference a problémy se správou sítě, protože nebyla pod přímou kontrolou radiové přístupové sítě. Standardizace TF v 3GPP, počínaje Release 9 pro LTE-Advanced, začlenila tyto funkce do působnosti sítě. Umožnila síti spravovat a optimalizovat využití reléových uzlů a zajistit, že doplňují, nikoli narušují celkové schémata správy rádiových prostředků a koordinace interference.

Technologie je motivována potřebou flexibilního nasazení sítě. Umožňuje rychlé nasazení v dočasných scénářích (např. události, obnova po katastrofě) a poskytuje škálovatelný způsob zvýšení hustoty sítě pro odlehčování kapacity. Tím, že přeposílání zůstává transparentní, zachovává kompatibilitu se stávajícími UE – pro připojení přes relé nejsou vyžadovány žádné nové schopnosti UE. Tato zpětná kompatibilita byla klíčovým faktorem pro její přijetí, protože umožnila operátorům vylepšovat své sítě bez nutnosti upgradů koncových zařízení.

## Klíčové vlastnosti

- Přeposílá data uživatelské a řídicí roviny bez ukončení protokolů
- Nemodifikuje obsah ani strukturu přeposílaných PDU
- Funguje jako rozšíření dárkové buňky, nikoli jako samostatná buňka
- Typicky implementováno na vrstvě PHY nebo nižších vrstvách MAC
- Zlepšuje pokrytí a kapacitu s nižšími náklady než plnohodnotné základnové stanice
- Zachovává koncovou integritu a zabezpečení původního datového toku

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 28.403** (Rel-19) — WLAN Performance Measurements
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [TF na 3GPP Explorer](https://3gpp-explorer.com/glossary/tf/)
