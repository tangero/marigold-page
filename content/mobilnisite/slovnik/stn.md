---
slug: "stn"
url: "/mobilnisite/slovnik/stn/"
type: "slovnik"
title: "STN – Signalling Transport Network"
date: 2025-01-01
abbr: "STN"
fullName: "Signalling Transport Network"
category: "Core Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/stn/"
summary: "Signalling Transport Network (STN) je logická nebo fyzická síťová infrastruktura vyhrazená pro přenos signalizačního provozu mezi síťovými prvky. Zajišťuje spolehlivé, bezpečné a efektivní doručování"
---

STN je vyhrazená síťová infrastruktura, která přenáší signalizační provoz mezi síťovými prvky, aby zajistila spolehlivé, bezpečné a efektivní doručování zpráv řídicí roviny.

## Popis

Signalling Transport Network (STN) označuje podkladovou přenosovou architekturu odpovědnou za přenos zpráv signalizačních protokolů uvnitř a mezi doménami veřejné pozemní mobilní sítě ([PLMN](/mobilnisite/slovnik/plmn/)). Na rozdíl od uživatelské roviny, která přenáší vlastní hlasový, video nebo datový obsah, přenáší signalizační rovina řídicí zprávy, které tyto komunikační relace navazují, spravují a ukončují. STN poskytuje spolehlivé, nízkolatenční a bezpečné cesty pro tyto kritické zprávy. Nejde o jeden konkrétní protokol, ale o síťový koncept zahrnující fyzické spoje, přepínací uzly a protokoly transportní vrstvy (jako [SCTP](/mobilnisite/slovnik/sctp/), [M3UA](/mobilnisite/slovnik/m3ua/), SUA), které zajišťují doručování signalizačních zpráv.

Architektonicky STN propojuje všechny signalizační uzly jádrové sítě, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)), Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) a později Mobility Management Entity (MME) a Home Subscriber Server (HSS). V tradičních sítích s přepojováním okruhů (CS) signalizace často využívala sítě SS7 (Signalling System No. 7) založené na časovém multiplexu (TDM). S vývojem směrem k plně IP jádrovým sítím se STN migroval na infrastrukturu založenou na IP, využívající protokoly jako SIGTRAN (Signalling Transport) pro adaptaci tradiční signalizace SS7 (jako MAP, CAP) přes IP transportní vrstvy, například Stream Control Transmission Protocol (SCTP). Tento IP-based STN poskytuje ve srovnání se staršími TDM sítěmi větší flexibilitu, škálovatelnost a nákladovou efektivitu.

Fungování STN zahrnuje vrstvené protokolové zásobníky. Na nejnižší úrovni spoléhá na standardní IP síťovou infrastrukturu (směrovače, přepínače). Na to navazuje SCTP, které poskytuje spojově orientovanou, spolehlivou transportní službu s možnostmi multi-homingu a multi-streamingu, což je klíčové pro dostupnost signalizace a distribuci zátěže. Adaptační vrstvy jako M3UA (MTP3 User Adaptation) nebo SUA (SCCP User Adaptation) následně mapují nativní signalizační aplikační části (např. ISUP, MAP) na SCTP transport. Úlohou STN je směrovat tyto zapouzdřené signalizační zprávy na základě cílových kódů bodů nebo IP adres. Síťové prvky využívají STN k dotazování databází účastníků (HLR/HSS), provádění předávání hovorů, autentizaci uživatelů a správě relací účtování. Jeho výkon přímo ovlivňuje klíčové síťové metriky, jako je doba navazování hovoru, úspěšnost předání hovoru a celková spolehlivost sítě.

## K čemu slouží

Koncept STN byl formalizován, aby řešil rostoucí složitost a rozsah signalizace v moderních mobilních sítích, které daleko přesahovaly možnosti přidružené nebo kanálově asociované signalizace. Rané mobilní sítě spoléhaly na vyhrazené časové sloty pro signalizaci uvnitř provozních kanálů, což bylo neefektivní a mělo omezenou škálovatelnost. Vytvoření samostatné signalizační sítě se společným kanálem – původně založené na SS7 – to vyřešilo poskytnutím výkonné, mimopásmové sítě vyhrazené výhradně pro řídicí zprávy. Toto oddělení umožnilo sofistikovanější služby, rychlejší navazování hovorů a efektivní databázové dotazy v rámci celé sítě.

Vývoj směrem k IP-based STN, výrazně od 3GPP Release 8 se System Architecture Evolution (SAE), byl motivován několika faktory. Starší TDM-based SS7 sítě byly nákladné na údržbu a škálování, používaly proprietární hardware a nebyly vhodné pro explozivní růst dat a nové služby založené na IP. Přechod odvětví k plně IP jádrovým sítím (IMS, LTE) si vyžádal konvergovanou IP transportní vrstvu pro uživatelskou i řídicí rovinu. IP-based STN využívající SIGTRAN umožnil operátorům využívat levnější, standardizované IP vybavení, zjednodušit síťovou architekturu a hladce integrovat nové IP-based služby a síťové funkce. Vyřešil problém vzájemného propojení mezi starší signalizací s přepojováním okruhů a novými aplikačními servery založenými na IP, což umožnilo plynulejší přechod k sítím další generace.

## Klíčové vlastnosti

- Vyhrazená infrastruktura pro spolehlivý mimopásmový přenos signalizace
- Podporuje jak starší SS7, tak IP-based (SIGTRAN) signalizační paradigmata
- Využívá SCTP pro spolehlivý, spojově orientovaný transport s multi-homingem
- Umožňuje propojení mezi doménami jádrové sítě s přepojováním okruhů a paketů
- Kritická pro správu mobility, řízení relací a přístup k databázím účastníků
- Poskytuje základ pro zabezpečení signalizace a odolnost sítě

## Související pojmy

- [SCTP – Stream Control Transmission Protocol](/mobilnisite/slovnik/sctp/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)

## Definující specifikace

- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 24.216** (Rel-19) — Communication Continuity Management Object
- **TS 24.237** (Rel-19) — IMS Service Continuity Protocol Details
- **TS 28.734** (Rel-19) — STN Interface NRM IRP Requirements
- **TS 28.735** (Rel-19) — STN Interface NRM IRP Information Service
- **TS 28.736** (Rel-19) — STN Interface NRM IRP Solution Set Definitions
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 32.741** (Rel-11) — STN Interface NRM IRP Requirements
- **TS 32.742** (Rel-11) — STN NRM for Configuration Management
- **TS 32.743** (Rel-9) — CORBA Solution Set for STN IRP
- **TS 32.745** (Rel-9) — STN NRM IRP XML File Format Definition
- **TS 32.746** (Rel-11) — STN NRM IRP Solution Set Definitions

---

📖 **Anglický originál a plná specifikace:** [STN na 3GPP Explorer](https://3gpp-explorer.com/glossary/stn/)
