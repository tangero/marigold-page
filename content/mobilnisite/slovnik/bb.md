---
slug: "bb"
url: "/mobilnisite/slovnik/bb/"
type: "slovnik"
title: "BB – Backbone Bearer"
date: 2025-01-01
abbr: "BB"
fullName: "Backbone Bearer"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bb/"
summary: "Logické transportní spojení mezi síťovými prvky v architektuře 3GPP, které přenáší uživatelská data a řídicí signalizaci. Poskytuje spolehlivý transport s podporou QoS pro provoz mezi uzly páteřní sít"
---

BB je logické transportní spojení mezi síťovými prvky, které přenáší uživatelská data a řídicí signalizaci a poskytuje spolehlivý transport s podporou QoS pro provoz mezi uzly páteřní sítě.

## Popis

Backbone Bearer (BB) je základní transportní koncept v sítích 3GPP, který vytváří logická spojení mezi síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) a síťovými prvky. Funguje na transportní vrstvě, abstrahuje od podkladové fyzické síťové infrastruktury a poskytuje standardizované komunikační kanály. BB je charakterizován specifickými parametry kvality služeb (QoS), bezpečnostními politikami a konfiguracemi směrování, které zajišťují předvídatelný výkon pro různé typy provozu, včetně dat uživatelské roviny, signalizace řídicí roviny a managementového provozu.

Architektonicky jsou BB implementovány napříč různými rozhraními a referenčními body 3GPP. Jsou zvláště klíčové v architektuře založené na službách (SBA) pro 5G, kde usnadňují komunikaci mezi síťovými funkcemi (NF) prostřednictvím rozhraní založených na službách. Každý BB je spojen se specifickými transportními požadavky definovanými ve specifikacích 3GPP, včetně charakteristik latence, šířky pásma, spolehlivosti a zabezpečení. Koncept BB umožňuje síťovým operátorům implementovat diferencované transportní služby bez nutnosti modifikace protokolů aplikační vrstvy, které přes ně běží.

Při implementaci jsou BB typicky realizovány pomocí IP technologií s vhodnými tunelovacími a zapouzdřovacími mechanismy. Mohou využívat protokoly jako [GTP-U](/mobilnisite/slovnik/gtp-u/) ([GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol for User Plane) pro přenos uživatelských dat a různé konfigurace [IPsec](/mobilnisite/slovnik/ipsec/) pro zabezpečenou komunikaci řídicí roviny. Správa BB zahrnuje koordinaci mezi více síťovými doménami, včetně rádiových přístupových sítí, páteřních sítí a externích datových sítí, a zajišťuje kontinuitu služeb a záruky výkonu end-to-end.

Klíčové součásti architektury BB zahrnují funkci vázání přenosu a hlášení událostí ([BBERF](/mobilnisite/slovnik/bberf/)) v určitých architekturách, která mapuje toky servisních dat na příslušné přenosy na základě pravidel politik. BB také spolupracuje se systémy řízení politik a účtování (PCC) k vynucování QoS politik a účtovacích pravidel. V sítích 5G se koncept BB vyvinul tak, aby podporoval síťové segmenty (network slicing), kde různé segmenty mohou využívat vyhrazené nebo sdílené páteřní přenosy se specifickými výkonnostními charakteristikami přizpůsobenými požadavkům segmentu.

## K čemu slouží

Backbone Bearer byl zaveden, aby řešil rostoucí složitost transportních sítí v architekturách 3GPP, zejména jak se sítě vyvíjely od přepojování okruhů k paradigmatu přepojování paketů. Před standardizovanými koncepty přenosů byl transport mezi síťovými prvky často implementován pomocí proprietárních nebo ad-hoc řešení, kterým chybělo konzistentní řízení QoS, vynucování zabezpečení a interoperabilita mezi zařízeními různých dodavatelů. To vytvářelo výzvy pro škálování sítě, zajištění kvality služeb a nasazení v multi-vendor prostředí.

Koncept BB poskytuje standardizovaný rámec pro transportní konektivitu, který odděluje servisní logiku od transportní implementace. Tato abstrakce umožňuje síťovým operátorům vyvíjet jejich transportní infrastrukturu nezávisle na službách, které přes ni běží. Definováním jasných rozhraní a charakteristik pro páteřní přenosy umožňuje 3GPP konzistentní implementaci napříč různými síťovými doménami a usnadňuje zavádění nových služeb bez nutnosti kompletního přepracování transportní sítě.

V kontextu 5G a dalších generací se BB staly stále důležitějšími pro podporu různorodých požadavků služeb, včetně ultra-spolehlivé komunikace s nízkou latencí (URLLC), rozšířeného mobilního širokopásmového přístupu (eMBB) a komunikace s hromadnými strojovými zařízeními (mMTC). Architektura páteřního přenosu umožňuje síťové segmentování tím, že poskytuje izolované transportní cesty se specifickými výkonnostními charakteristikami pro různé segmenty, což je nezbytné pro podporu aplikací vertikálních průmyslů s přísnými požadavky.

## Klíčové vlastnosti

- Transport s podporou QoS s konfigurovatelnými parametry včetně latence, šířky pásma a spolehlivosti
- Podpora více typů provozu včetně uživatelských dat, řídicí signalizace a managementového provozu
- Integrace s řízením politik a účtováním (PCC) pro dynamické vynucování politik
- Bezpečnostní funkce včetně šifrování, ochrany integrity a autentizačních mechanismů
- Podpora síťového segmentování (network slicing) s vyhrazenými nebo sdílenými transportními prostředky
- Interoperabilita napříč různými síťovými doménami a zařízeními různých dodavatelů

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TR 37.880** (Rel-17) — High-power UE for fixed-wireless/vehicle use
- **TS 38.774** (Rel-19) — Rel-19 LP-WUS/WUR RF Requirements TR
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR
- **TR 38.877** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [BB na 3GPP Explorer](https://3gpp-explorer.com/glossary/bb/)
