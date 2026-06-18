---
slug: "masa"
url: "/mobilnisite/slovnik/masa/"
type: "slovnik"
title: "MASA – Metadata-Assisted Spatial Audio"
date: 2025-01-01
abbr: "MASA"
fullName: "Metadata-Assisted Spatial Audio"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/masa/"
summary: "Vylepšení kodeku 3GPP pro imerzivní zvukové zážitky. Využívá metadata k popisu prostorových zvukových scén, což umožňuje účinnou kompresi a vysoce kvalitní vykreslování na zařízeních s různými konfigu"
---

MASA je vylepšení kodeku 3GPP, které využívá metadata k popisu prostorových zvukových scén pro účinnou kompresi a vysoce kvalitní vykreslování na různých zařízeních; je klíčové pro imerzivní aplikace, jako je rozšířená realita.

## Popis

Metadata-Assisted Spatial Audio (MASA) je standardizovaný rámec v rámci 3GPP pro reprezentaci, kódování a vykreslování imerzivního zvuku. Na rozdíl od tradičního kanálového nebo objektového zvuku používá MASA hybridní přístup, kde je základní zvuk kódován pomocí tradičního kodeku (jako [EVS](/mobilnisite/slovnik/evs/) nebo 3GPP-DRC), zatímco samostatný kompaktní datový proud metadat popisuje prostorové vlastnosti zvukové scény. Tato metadata zahrnují parametry, jako je směr, vzdálenost a velikost zdrojů zvuku, stejně jako akustické vlastnosti prostředí. Architektura je navržena jako nezávislá na kodeku, což umožňuje přidružení prostorových metadat k různým podkladovým zvukovým datovým proudům a poskytuje flexibilitu poskytovatelům služeb. Klíčové komponenty zahrnují kodér metadat, který analyzuje prostorovou zvukovou scénu, a dekodér/vykreslovací modul metadat v přijímacím zařízení, který metadata používá k rekonstrukci imerzivního zvukového pole vhodného pro konkrétní prostředí přehrávání posluchače, ať už jde o sluchátka, stereo reproduktory nebo vícekanálový domácí kinosystém. Jeho role v síti spočívá v umožnění služby, kde jsou zvukové a metadatové proudy paketizovány, přenášeny přes sítě 5G (využívající vysokou šířku pásma a nízkou latenci) a synchronizovány na přijímači, aby doručily ucelený imerzivní zážitek. Specifikace podrobně popisuje syntaxi a sémantiku metadat, čímž zajišťuje interoperabilitu mezi nástroji pro tvorbu obsahu a spotřebitelskými zařízeními.

## K čemu slouží

MASA bylo vytvořeno, aby řešilo rostoucí poptávku po imerzivních zvukových zážitcích, zejména poháněnou rozšířenou realitou ([XR](/mobilnisite/slovnik/xr/)), videem 360° a vysíláním nové generace. Tradiční zvukové kodeky byly navrženy pro pevné kanálové konfigurace (např. stereo, 5.1) a obtížně se vyrovnávají s flexibilitou vyžadovanou pro personalizované, na zařízení adaptivní vykreslování. Objektové zvukové formáty existovaly, ale mohly být neefektivní pro přenos přes mobilní sítě s omezenou šířkou pásma kvůli vysoké přenosové rychlosti potřebné pro četné diskrétní zvukové objekty. MASA to řeší oddělením popisných prostorových metadat (která mají velmi nízkou přenosovou rychlost) od hlavní zvukové datové části. To umožňuje účinný síťový přenos a zároveň umožňuje přijímači vykreslit optimální zvukové pole přizpůsobené jeho specifickým výstupním schopnostem a orientaci posluchače (v případě sledování polohy hlavy). Jeho vytvoření bylo motivováno potřebou standardizovaného, síťově příznivého řešení imerzivního zvuku v rámci ekosystému 3GPP, které by doplnilo pokroky ve videu a službách XR přes 5G, a zajistilo tak vysokou kvalitu zážitku bez prohibitivních nákladů na šířku pásma.

## Klíčové vlastnosti

- Hybridní reprezentace zvuku kombinující základní kódovaný zvuk se samostatnými prostorovými metadaty
- Nezávislý design na kodeku umožňující použití s EVS, 3GPP-DRC a dalšími zvukovými kodeky
- Kompaktní syntaxe metadat pro účinný přenos přes mobilní sítě
- Adaptivní vykreslování pro zařízení: sluchátka, stereo a vícekanálové sestavy
- Podpora dynamických aktualizací scény a sledování polohy hlavy posluchače (6DoF)
- Standardizovaný formát datového proudu zajišťující interoperabilitu mezi zařízeními pro tvorbu obsahu a přehrávání

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 26.250** (Rel-19) — IVAS Codec Introduction
- **TS 26.251** (Rel-19) — IVAS Codec Fixed-Point C Code Specification
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.254** (Rel-19) — IVAS Rendering Functions Specification
- **TS 26.255** (Rel-19) — IVAS Frame Loss Concealment Procedure
- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.261** (Rel-19) — Electro-acoustic specs for immersive terminals
- **TR 26.865** (Rel-18) — Technical Report
- **TR 26.933** (Rel-19) — Study on Diverse Audio Capturing System
- **TR 26.996** (Rel-19) — ISAR Split Rendering Audio Characterization
- **TR 26.997** (Rel-19) — IVAS Codec Specification

---

📖 **Anglický originál a plná specifikace:** [MASA na 3GPP Explorer](https://3gpp-explorer.com/glossary/masa/)
