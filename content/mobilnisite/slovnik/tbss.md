---
slug: "tbss"
url: "/mobilnisite/slovnik/tbss/"
type: "slovnik"
title: "TBSS – Target BSS"
date: 2025-01-01
abbr: "TBSS"
fullName: "Target BSS"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tbss/"
summary: "TBSS označuje subsystém základnové stanice (BSS), ke kterému mobilní stanice přechází během procedury předávání spojení v sítích GSM nebo UMTS. Jedná se o cílový síťový prvek, který připravuje prostře"
---

TBSS je subsystém základnové stanice (Base Station Subsystem), ke kterému mobilní stanice přechází během procedury předávání spojení v sítích GSM nebo UMTS.

## Popis

Cílový [BSS](/mobilnisite/slovnik/bss/) (TBSS) je termín používaný v sítích GSM a UMTS pro označení subsystému základnové stanice, ke kterému se má mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) připojit během procedury předávání spojení. TBSS je cílový BSS, který přijímá požadavek na předání spojení od obsluhujícího BSS ([SBSS](/mobilnisite/slovnik/sbss/)) a alokuje potřebné prostředky, jako jsou rádiové kanály a kapacitu zpracování, aby umožnil plynulý přechod. Tento koncept je klíčový pro správu mobility a zajišťuje, že aktivní hovory nebo datové relace jsou zachovány bez přerušení, když se MS pohybuje mezi různými oblastmi pokrytí. Specifikace jako TS 25.401 a TS 43.130 podrobně popisují protokoly a signalizaci spojené s operacemi TBSS.

Jak TBSS funguje, zahrnuje koordinovaný proces mezi síťovými entitami. Když obsluhující BSS určí, že je potřeba předání spojení z důvodů jako degradace signálu nebo vyrovnávání zátěže, odešle zprávu 'handover required' do jádra sítě s identifikací TBSS. Jádro sítě pak přepošle požadavek na předání spojení do TBSS, který vyhodnotí dostupnost prostředků a připraví příkaz k předání spojení. Tento příkaz obsahuje parametry jako přiřazení nového kanálu a je odeslán zpět přes jádro sítě do SBSS, který nařídí MS, aby se přepnula na TBSS. Jakmile MS přistoupí k TBSS, odešle zprávu 'handover complete', čímž se přechod dokončí.

Klíčové komponenty v TBSS zahrnují základnovou přijímací a vysílací stanici ([BTS](/mobilnisite/slovnik/bts/)) v GSM nebo Node B v UMTS, která zajišťuje rádiový přenos, a řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) nebo řadič rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)), který spravuje alokaci prostředků a signalizaci. Role TBSS je kritická pro udržení kvality služeb (QoS), minimalizaci přerušených hovorů a optimalizaci výkonu sítě. Efektivní správou předávání spojení TBSS podporuje nepřetržitou mobilitu, umožňuje uživatelům volný pohyb při zachování připojení, což je zásadní pro spolehlivost celulárních sítí.

## K čemu slouží

TBSS byl zaveden pro efektivní správu předávání spojení v celulárních sítích, aby řešil výzvu udržení probíhajících relací při pohybu uživatelů. Před standardizovanými procedurami předávání spojení trpěly rané mobilní systémy častými přerušeními hovorů a špatnou kontinuitou služeb během událostí mobility. Koncept TBSS poskytuje strukturovaný přístup pro koordinaci mezi zdrojovými a cílovými síťovými prvky, zajišťuje, že prostředky jsou předem alokovány a připraveny předtím, než se [MS](/mobilnisite/slovnik/ms/) přepne.

Historicky, s rozšiřováním sítí GSM, se stala zřejmou potřeba robustních mechanismů předávání spojení pro podporu rostoucí mobility účastníků. Rámec TBSS, stanovený ve specifikacích 3GPP, vyřešil omezení ad-hoc metod předávání spojení definováním jasných rolí pro obsluhující a cílový [BSS](/mobilnisite/slovnik/bss/). To umožnilo předvídatelné a spolehlivé přechody, které zlepšily uživatelský zážitek a efektivitu sítě. Také umožnil funkce jako předávání spojení mezi BSS a mezi systémy, což umožňuje plynulý pohyb mezi různými technologiemi nebo operátory.

Určením konkrétního TBSS může síť připravit přechod předem, čímž se snižuje latence předávání spojení a předchází se přerušením služeb. To je obzvláště důležité pro aplikace v reálném čase, jako jsou hlasové hovory a video streamování. Koncept TBSS tvoří základ pokročilých technik správy mobility v pozdějších technologiích jako LTE a 5G, které se vyvíjejí pro podporu rychlejších a složitějších scénářů předávání spojení v heterogenních sítích.

## Klíčové vlastnosti

- Určuje cílový BSS během procedur předávání spojení
- Alokuje rádiové prostředky a kapacitu zpracování pro příchozí spojení
- Koordinuje s obsluhujícím BSS a jádrem sítě pro plynulé přechody
- Podporuje předávání spojení uvnitř systému a mezi systémy v GSM/UMTS
- Minimalizuje přerušené hovory a udržuje kontinuitu relace
- Integruje se s protokoly správy mobility pro spolehlivost

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 43.130** (Rel-19) — Iur-g Interface Overview

---

📖 **Anglický originál a plná specifikace:** [TBSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tbss/)
