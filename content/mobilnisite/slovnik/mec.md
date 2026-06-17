---
slug: "mec"
url: "/mobilnisite/slovnik/mec/"
type: "slovnik"
title: "MEC – Multi-Access Edge Computing"
date: 2026-01-01
abbr: "MEC"
fullName: "Multi-Access Edge Computing"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mec/"
summary: "Síťová architektura, která poskytuje možnosti cloud computingu a prostředí pro IT služby na okraji mobilní sítě, blízko uživatelů. Umožňuje extrémně nízkou latenci, vysokou propustnost a přístup k inf"
---

MEC je síťová architektura, která poskytuje možnosti cloud computingu na okraji mobilní sítě, aby umožnila extrémně nízkou latenci, vysokou propustnost a přístup k informacím z rádiové sítě v reálném čase.

## Popis

Multi-Access Edge Computing (MEC), dříve Mobile Edge Computing, je systémová architektura definovaná [ETSI](/mobilnisite/slovnik/etsi/) a integrovaná do ekosystému 3GPP, která přesouvá hostování aplikací a prostředky cloud computingu z centralizovaných datových center na síťový okraj (edge). Tento 'okraj' je fyzicky i logicky blízko koncového uživatele, typicky v bodech agregace základnových stanic, centrálách nebo přímo v rámci samotné rádiové přístupové sítě (RAN). Platforma MEC se skládá z virtualizační infrastruktury (např. malé datové centrum), která hostuje MEC aplikace a poskytuje základní MEC služby. Tyto aplikace běží nad MEC hostitelem, který zahrnuje MEC platformu a virtualizační infrastrukturu.

Architekturu ukotvuje MEC systém, který zahrnuje MEC hostitele a MEC správu. MEC hostitel obsahuje MEC platformu (poskytující servisní [API](/mobilnisite/slovnik/api/)) a MEC aplikace. MEC správa zahrnuje MEC orchestrátor (pro správu životního cyklu aplikací) a správce MEC platformy. Klíčové je, že MEC poskytuje sadu standardizovaných API, zejména API služby Radio Network Information Service (RNIS), které umožňují autorizovaným aplikacím přistupovat k reálným kontextovým informacím o podmínkách v rádiové síti (např. poloha UE, vytížení buňky, propustnost). Dalším klíčovým API je Location API. Tato expozice síťových schopností je základním aspektem MEC.

Jak to funguje, zahrnuje směrování provozu a hostování aplikací. Provoz v uživatelské rovině může být směrován (odkloněn) k lokální MEC aplikaci namísto přenášení do vzdálené internetové brány. Toho je dosaženo mechanismy jako je výběr User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) a odklon provozu v 5G Core síti. Například aplikace rozšířené reality citlivá na latenci může být hostována na MEC serveru na okraji sítě. Když UE vyžádá tuto službu, Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) sítě vybere UPF, která je umístěna společně s MEC hostitelem. Datový provoz UE je pak směrován na tuto lokální UPF a dále k MEC aplikaci, což vede k minimální latenci. Aplikace může také použít RNIS API k přizpůsobení své služby na základě kvality rádiového spoje nebo polohy uživatele.

## K čemu slouží

MEC byl vytvořen, aby řešil omezení centralizovaných cloudových architektur pro aplikace citlivé na latenci, náročné na šířku pásma a využívající kontext. Řeší problém zahlcení sítě a vysoké latence způsobené přenášením veškerého provozu do vzdálených centrálních datových center. Vzestup aplikací, jako jsou autonomní vozidla, průmyslový IoT, imerzivní VR/[AR](/mobilnisite/slovnik/ar/) a analýza videa v reálném čase, vyžadoval latence v řádu jednotek milisekund a efektivní lokální zpracování dat, což tradiční mobilní sítě nemohly poskytnout.

Historický kontext zahrnuje vývoj směrem k 5G, kde klíčové scénáře použití jako Enhanced Mobile Broadband (eMBB), Ultra-Reliable Low-Latency Communications (URLLC) a Massive Machine Type Communications (mMTC) vyžadují podporu edge computingu. Počáteční koncepty z [ETSI](/mobilnisite/slovnik/etsi/) ISG MEC byly integrovány do specifikací 3GPP počínaje Release 15, aby byla zajištěna bezproblémová interoperabilita s architekturou 5G systému. MEC transformuje síť z čistého přenosového kanálu na distribuovanou výpočetní platformu, což umožňuje nové obchodní modely pro operátory a vertikální odvětví tím, že umožňuje aplikacím třetích stran využívat prostředky na okraji sítě a síťové informace.

## Klíčové vlastnosti

- Hostuje aplikace v bezprostřední blízkosti koncových uživatelů na síťovém okraji
- Poskytuje standardizovaná API (např. RNIS, Location) pro přístup aplikací k síťovému kontextu v reálném čase
- Umožňuje lokální průnik provozu (breakout) a optimalizaci uživatelské roviny prostřednictvím výběru UPF
- Podporuje extrémně nízkou latenci a vysokou propustnost pro náročné aplikace
- Umožňuje správu životního cyklu aplikací (registrace, vytvoření instance, ukončení)
- Zpřístupňuje síť a služby vývojářům aplikací třetích stran (network and service exposure)

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 33.867** (Rel-17) — User Consent for 3GPP Services

---

📖 **Anglický originál a plná specifikace:** [MEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mec/)
