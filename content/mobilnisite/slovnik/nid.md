---
slug: "nid"
url: "/mobilnisite/slovnik/nid/"
type: "slovnik"
title: "NID – Network Identifier"
date: 2026-01-01
abbr: "NID"
fullName: "Network Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nid/"
summary: "NID je jedinečný identifikátor používaný ve spojení s PLMN ID k vytvoření úplného identifikátoru pro samostatnou neveřejnou síť (SNPN). Umožňuje zařízením jedinečně identifikovat a vybírat privátní 5G"
---

NID je jedinečný identifikátor používaný společně s PLMN ID k vytvoření úplného identifikátoru pro samostatnou neveřejnou síť (SNPN), což umožňuje jedinečnou identifikaci a výběr privátních 5G sítí zařízeními.

## Popis

Network Identifier (NID) je klíčovou součástí architektury 3GPP pro samostatné neveřejné sítě (SNPN), zavedenou pro umožnění nasazení privátních celulárních sítí. SNPN je 5G síť provozovaná pro soukromé účely (např. podnikem, továrnou nebo energetickou společností), která se pro funkce jádra sítě nespoléhá na veřejnou pozemní mobilní síť (PLMN). Pro globálně jedinečnou identifikaci takové sítě se používá dvoudílný identifikátor: PLMN ID (Public Land Mobile Network Identity) a NID. PLMN ID ([MCC](/mobilnisite/slovnik/mcc/)+[MNC](/mobilnisite/slovnik/mnc/)) v tomto kontextu identifikuje operátora SNPN, což může být samotný podnik nebo poskytovatel privátní sítě, a nemusí se nutně jednat o tradiční kód veřejného operátora. NID je 20bitová až 32bitová hodnota (typicky reprezentovaná 5 až 8 hexadecimálními číslicemi), která jedinečně identifikuje konkrétní síť pod tímto PLMN ID.

Architektonicky je NID vysílán v systémové informaci (SIB1) 5G rádiovými buňkami (gNB) patřícími do SNPN. Uživatelské zařízení (UE) nakonfigurované pro přístup k SNPN má jeden nebo více identifikátorů předplatného SNPN uložených ve svém univerzálním modulu identifikace účastníka (USIM) nebo v konfiguraci zařízení. Tento identifikátor je kombinací PLMN ID a NID. Během počátečního výběru buňky a registrace do sítě UE přečte vysílané PLMN ID a NID a porovná je se svým nakonfigurovaným seznamem. Pokud najde shodu, pokračuje v připojení k této SNPN. NID je přenášen v klíčových zprávách [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum), jako je Registrační žádost, aby informoval jádro sítě o konkrétní síti, ke které se UE pokouší přistoupit.

Fungování zahrnuje několik vrstev. Na fyzické a [RRC](/mobilnisite/slovnik/rrc/) vrstvě je NID vysílán, což umožňuje objevování UE. Na NAS vrstvě je používán pro výběr sítě a registraci. Uvnitř jádra sítě síťová funkce ([NF](/mobilnisite/slovnik/nf/)) zodpovědná za správu přístupu, funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)), používá přijaté PLMN ID a NID k směrování registrační žádosti ke správnému síťovému řezu a autentizační infrastruktuře specifické pro danou SNPN. Funkce autentizačního serveru ([AUSF](/mobilnisite/slovnik/ausf/)) použije úplný identifikátor SNPN (PLMN ID + NID) k výběru správných přihlašovacích údajů a autentizační metody pro tuto privátní síť. Tím je zajištěna úplná logická izolace mezi různými SNPN, i když sdílejí stejné rádiové spektrum nebo jsou spravovány stejným poskytovatelem infrastruktury.

Klíčové komponenty zahrnují samotnou hodnotu NID, vysílací mechanismus v systémové informaci, úložiště konfigurace UE pro identifikátory SNPN a směrování v jádře sítě a vyhledávání předplatného založené na kombinaci PLMN+NID. Jeho role je zásadní pro koncept SNPN, poskytuje granularitu potřebnou pro podporu více nezávislých privátních sítí v rámci sdíleného prostoru operátora. Umožňuje funkce jako uzavřené přístupové skupiny, kde pouze předem nakonfigurovaná UE mohou přistupovat k síti, a tvoří základ pro bezpečný, izolovaný provoz privátních sítí, jak je zamýšleno pro Průmysl 4.0, kampusové sítě a kritickou infrastrukturu.

## K čemu slouží

NID byl vytvořen k řešení základního problému identifikace a izolace privátních celulárních sítí v rámci standardizovaného globálního rámce. Před jeho zavedením privátní sítě často používaly uzavřené skupiny účastníků ([CSG](/mobilnisite/slovnik/csg/)) uvnitř veřejného PLMN nebo fungovaly jako zcela izolované ostrovy s nestandardními identifikátory, což vedlo k problémům s interoperabilitou a složitosti správy. Vzestup Průmyslu 4.0, chytrých továren a kritické infrastruktury vyžadoval vyhrazené, bezpečné a spolehlivé 5G sítě, které by mohly fungovat nezávisle na veřejných MNO. Koncept SNPN, umožněný NID, byl standardizovanou odpovědí 3GPP na tuto poptávku.

Řeší omezení samotného PLMN ID, které je navrženo pro veřejné operátory. Podnik nasazující privátní síť není veřejným operátorem a neměl by potřebovat globálně jedinečný MNC z omezené množiny spravované ITU pouze pro svou interní síť. NID poskytuje potřebný dodatečný jmenný prostor pod určeným PLMN ID (což může být vyhrazený rozsah pro použití privátními sítěmi, např. použití MCC '999' definovaného pro testovací/privátní sítě). To umožňuje vytvořit nekonečný počet privátních sítí pod jedním PLMN ID, což zjednodušuje správu a zároveň zajišťuje globální jedinečnost prostřednictvím kombinace.

Dále NID umožňuje jasný výběr sítě pro zařízení. Zařízení může být nakonfigurováno s předplatnými pro více různých SNPN (např. pro různé podnikové areály nebo role). Vysílaný NID umožňuje zařízení automaticky identifikovat a připojit se ke správné síti. To je zásadní pro automatizovaná průmyslová zařízení, drony a senzory, které musí fungovat v konkrétních, řízených síťových prostředích. Vytvoření NID a rámce SNPN v 3GPP Release 16 byla přímou reakcí na silnou poptávku trhu po standardizované privátní 5G síti, což znamenalo posun od proprietárních řešení a zajištění interoperability zařízení a sítí napříč různými dodavateli a vertikálními odvětvími.

## Klíčové vlastnosti

- 20bitový až 32bitový identifikátor používaný v kombinaci s PLMN ID k jedinečné identifikaci samostatné neveřejné sítě (SNPN)
- Vysílán v 5G systémové informaci (SIB1) pro objevování a výběr UE
- Umožňuje logickou izolaci a nezávislý provoz více privátních sítí pod jedním PLMN ID operátora
- Uložen v USIM UE nebo v konfiguraci zařízení jako součást identifikátoru předplatného SNPN
- Používán v signalizaci NAS (např. Registrační žádost) pro směrování v jádře sítě a autentizaci
- Základní pro model řízení přístupu a zabezpečení privátních 5G sítí

## Definující specifikace

- **TS 23.287** (Rel-19) — 5G V2X Architecture Enhancements
- **TS 23.289** (Rel-20) — Mission Critical services over 5G System
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.368** (Rel-19) — NAS Configuration Management Object
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 24.558** (Rel-19) — Edge Enabler APIs Stage 3
- **TS 24.588** (Rel-19) — UE Policies for V2X Services in 5GS
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TR 28.828** (Rel-18) — Charging Aspects for Non-Public Networks
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- … a dalších 19 specifikací

---

📖 **Anglický originál a plná specifikace:** [NID na 3GPP Explorer](https://3gpp-explorer.com/glossary/nid/)
