---
slug: "hud"
url: "/mobilnisite/slovnik/hud/"
type: "slovnik"
title: "HUD – Heads-Up Display"
date: 2025-01-01
abbr: "HUD"
fullName: "Heads-Up Display"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hud/"
summary: "Heads-Up Display (HUD) označuje servisní nebo aplikační scénář, při kterém jsou informace promítány do zorného pole uživatele, typicky ve vozidlech. 3GPP studuje jeho požadavky, aby umožnil bezdrátové"
---

HUD je servisní scénář, při kterém jsou informace promítány do zorného pole uživatele a který vyžaduje bezdrátové připojení s nízkou latencí a vysokou spolehlivostí, jak jej studuje 3GPP.

## Popis

V terminologii 3GPP je Heads-Up Display (HUD) studován jako reprezentativní případ užití a služba umožňující pokročilé vozidlové aplikace a aplikace rozšířené reality ([AR](/mobilnisite/slovnik/ar/)). Systém HUD promítá kritické informace – jako jsou navigační pokyny, rychlost nebo varování před překážkami – na průhlednou plochu (například čelní sklo vozidla) nebo přímo do zorného pole uživatele prostřednictvím chytrých brýlí, což uživateli umožňuje přijímat informace bez odvrácení pozornosti od hlavního úkolu (např. řízení). Práce 3GPP na HUD se zaměřuje na definování síťových požadavků nezbytných pro podporu takových datově náročných a na latenci citlivých služeb přes mobilní sítě.

Technicky podpora cloudově renderované nebo síťově asistované služby HUD zahrnuje několik klíčových komponent a datových toků. Grafická data ve vysokém rozlišení, často 3D (jako dynamické mapové vrstvy nebo varování před nebezpečím), mohou být generována nebo zpracována na edge cloudovém serveru. Tato data musí být následně streamována s extrémně nízkou latencí a vysokou spolehlivostí do zařízení HUD ve vozidle nebo na uživateli. Systém 5G se svými schopnostmi Ultra-Reliable Low Latency Communication (URLLC) je navržen tak, aby těmto požadavkům vyhověl. Mezi klíčové technické aspekty patří přísné cíle pro koncovou latenci (často v řádu jednotek milisekund), velmi vysoké přenosové rychlosti pro video/AR streamy a bezproblémová podpora mobility při pohybu uživatele vysokou rychlostí.

Úlohou sítě 3GPP je poskytnout deterministickou konektivní strukturu. To zahrnuje síťové funkce, jako je přesné vynucování kvality služeb (QoS) prostřednictvím identifikátorů 5G QoS ([5QI](/mobilnisite/slovnik/5qi/)) přizpůsobených pro imerzivní média, optimalizace cesty uživatelské roviny prostřednictvím Local Area Data Network ([LADN](/mobilnisite/slovnik/ladn/)) nebo Mobile Edge Computing ([MEC](/mobilnisite/slovnik/mec/)) a spolehlivá kontinuita relace. Servisní architektura může zahrnovat aplikační funkce komunikující s 5G Core za účelem vyžádání specifických síťových zdrojů. Specifikace 3GPP, jako jsou ty pro streamování médií přes 5G (26.928) a vylepšení pro vozidlovou komunikaci (38.835), analyzují scénáře HUD, aby odvodily konkrétní požadavky na rádiový přístup, základní síť a systémovou architekturu.

## K čemu slouží

Zařazení Heads-Up Display jako studované položky do specifikací 3GPP je hnací silou vývoje automobilového průmyslu směrem ke spojeným a autonomním vozidlům a širšího rozšíření rozšířené reality. Tradiční mobilní služby zaměřené na hlas, prohlížení webu a streamování videa neměly garantovaný výkon potřebný pro bezpečnostně kritické nebo imerzivní real-time překryvy. Případ užití HUD explicitně identifikuje omezení předchozích mobilních sítí z hlediska kolísání latence, spolehlivosti a konzistence doručování dat.

Práce 3GPP na HUD si klade za cíl vyřešit problém doručování vysoce věrných, dynamických vizuálních informací pohybujícím se uživatelům s téměř okamžitou dobou odezvy. To je motivováno potřebou zvýšit povědomí o situaci a bezpečnost, kde by i zpoždění 100 milisekund ve zobrazení varování před nebezpečím mohlo být katastrofální. Formální specifikací servisních požadavků pro HUD 3GPP usměrňuje vývoj technologií 5G a dalších generací – jako jsou vylepšení rozhraní NR-Uu, síťové slicing a edge computing – aby zajistila, že rádiový přístup a základní síť mohou sloužit jako důvěryhodná platforma pro tyto pokročilé služby. Představuje posun od best-effort mobilního širokopásmového připojení k síti schopné podporovat doručování senzorických informací pro kritické mise.

## Klíčové vlastnosti

- Definuje požadavky na streamování vizuálních dat s ultra-nízkou latencí
- Podněcuje potřebu vysoké spolehlivosti (např. 99,999 %) v doručování paketů
- Využívá edge computing pro lokální renderování a zpracování obsahu
- Využívá mechanismy QoS 5G pro prioritní zpracování provozu
- Podporuje vysokou mobilitu uživatele, včetně vozidlových rychlostí
- Umožňuje integraci dat z real-time senzorů (např. z V2X) s cloudovým obsahem

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 38.835** (Rel-18) — Technical Report on XR Enhancements for NR

---

📖 **Anglický originál a plná specifikace:** [HUD na 3GPP Explorer](https://3gpp-explorer.com/glossary/hud/)
