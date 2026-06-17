---
slug: "bp"
url: "/mobilnisite/slovnik/bp/"
type: "slovnik"
title: "BP – Bitstream Partition"
date: 2025-01-01
abbr: "BP"
fullName: "Bitstream Partition"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bp/"
summary: "Bitstream Partition (BP) je mechanismus 3GPP pro rozdělení mediálního obsahu na více nezávislých částí (partitions), které mohou být v síti doručovány odděleně. Umožňuje flexibilní doručování médií tí"
---

BP je mechanismus 3GPP pro rozdělení mediálního obsahu na nezávislé části (partition), které mohou být doručovány odděleně po různých síťových cestách nebo s různými charakteristikami kvality služeb (QoS).

## Popis

Bitstream Partition (BP) je propracovaný rámec pro doručování médií definovaný ve standardech 3GPP, který umožňuje rozklad jediného mediálního proudu na více nezávislých částí (partitions). Každá část obsahuje podmnožinu celkového mediálního obsahu, kterou lze kódovat, přenášet a zpracovávat odděleně, a zároveň zachovat možnost rekonstrukce kompletního mediálního proudu na přijímací straně. Architektura zahrnuje přípravu obsahu u mediálního zdroje, kde je původní datový proud (bitstream) analyzován a rozdělen podle specifických kritérií, jako jsou časové segmenty, prostorové oblasti, kvalitativní vrstvy nebo funkční komponenty. Tyto části jsou následně zabaleny společně s metadaty, která popisují jejich vztahy a závislosti, což umožňuje jejich správné složení na straně klienta.

Technická implementace BP spoléhá na standardizované signalizační a přenosové protokoly, které koordinují přenos více částí přes potenciálně různorodé síťové cesty. Systém využívá identifikátory částí, informace o závislostech a synchronizační značky, aby zajistil, že části lze na koncovém přijímacím bodě správně zkombinovat. Mezi klíčové komponenty patří generátor částí na mediálním serveru, funkce pro doručování s ohledem na části uvnitř sítě a logika pro opětovné složení částí v klientském zařízení. Rámec podporuje scénáře doručování médií v reálném i mimo reálný čas s konkrétními optimalizacemi pro každý případ použití.

V praxi BP umožňuje pokročilé techniky doručování médií, jako je vrstvové kódování, kde jsou základní vrstvy a vylepšující vrstvy přenášeny jako samostatné části s různou úrovní priority. To sítím umožňuje dynamicky se přizpůsobovat měnícím se podmínkám tím, že při nedostatku přenosové kapacity selektivně zahazují vylepšující části, zatímco základní kvalita služby je zachována. Systém také usnadňuje doručování po více cestách, kdy mohou být různé části odesílány přes různá síťová rozhraní (např. současně přes mobilní síť a Wi-Fi) pro zvýšení agregované přenosové kapacity a zlepšení spolehlivosti prostřednictvím redundance. Metadata doprovázející každou část zahrnují časové informace, indikátory kvality a odkazy na závislosti, které klientovi poskytují vodítko pro správné seřazení a kombinaci přijatého obsahu.

Role BP v sítích 5G a budoucích sítích přesahuje jednoduché doručování médií a umožňuje nové schopnosti služeb, jako je viewport-dependent streaming pro virtuální realitu, kde jsou různé prostorové oblasti 360stupňového videa rozděleny do částí a doručovány s rozdílnou kvalitou na základě aktuálního zorného pole uživatele. Také podporuje pokročilou odolnost proti chybám prostřednictvím schémat opravy chyb na úrovni částí ([FEC](/mobilnisite/slovnik/fec/)) a schémat opakovaného přenosu. Rámec se integruje se stávajícími systémy 3GPP prostřednictvím standardizovaných rozhraní mezi mediálními funkcemi, prvky jádra sítě a rádiovými přístupovými sítěmi, čímž zajišťuje kompatibilitu s ustavenými mechanismy QoS a systémy účtování.

## K čemu slouží

Bitstream Partition byl vytvořen, aby řešil rostoucí složitost doručování médií v mobilních sítích, kde tradiční monolitické přístupy ke streamování zápasily s přizpůsobováním se různorodým síťovým podmínkám a možnostem zařízení. Před zavedením BP byl mediální obsah typicky doručován jako jediný souvislý proud, což ztěžovalo optimalizaci přenosu pro různé rádiové podmínky nebo využití více současných síťových připojení. Toto omezení se stalo zvláště problematickým s nástupem videa vysokého rozlišení, obsahu pro virtuální realitu a dalších aplikací náročných na přenosovou kapacitu, které vyžadují flexibilní mechanismy doručování pro udržení kvality uživatelského zážitku v různých scénářích.

Technologie řeší několik klíčových problémů moderního doručování médií: umožňuje efektivní využití přenosové kapacity tím, že sítím dovoluje upřednostňovat kritické části během přetížení, podporuje optimalizace pro konkrétní zařízení tím, že doručuje pouze části relevantní pro možnosti daného zařízení, a usnadňuje inovativní modely služeb, jako je video s více pohledy nebo adaptivní prostorové streamování. Oddělením mediálního obsahu na nezávislé části poskytuje BP základ pro inteligentnější strategie doručování, které mohou dynamicky reagovat na síťové podmínky, preference uživatelů a požadavky služeb.

Historicky byl vývoj BP motivován konvergencí několika trendů: rozšířením heterogenních zařízení s různými možnostmi zobrazení a výpočetního výkonu, rostoucí dostupností více síťových rozhraní na mobilních zařízeních a rostoucí poptávkou po imerzních mediálních zážitcích, které vyžadují sofistikovanější mechanismy doručování než tradiční streamování. Rámec řeší tyto výzvy tím, že poskytuje standardizovaný způsob, jak rozložit a znovu složit mediální proudy, což umožňuje interoperabilitu mezi zařízeními různých výrobců a podporuje inovace v technikách doručování médií, aniž by vyžadovaly zásadní změny základní síťové infrastruktury.

## Klíčové vlastnosti

- Umožňuje rozklad mediálních proudů na nezávislé části (partitions)
- Podporuje diferenciaci a stanovení priority QoS na úrovni částí
- Usnadňuje doručování po více cestách přes různá síťová rozhraní
- Poskytuje metadata pro závislosti mezi částmi a synchronizaci
- Umožňuje viewport-dependent streaming pro VR/360stupňové video
- Integruje se se stávajícími mechanismy QoS a účtování 3GPP

## Definující specifikace

- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TS 26.226** (Rel-19) — Cellular Text Telephone Modem (CTM)
- **TS 26.267** (Rel-19) — eCall In-band Modem Specification
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.502** (Rel-19) — 5G System; Nsmf Service Based Interface; Stage 3
- **TS 29.892** (Rel-16) — Study on User Plane Protocol in 5GC
- **TR 38.884** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [BP na 3GPP Explorer](https://3gpp-explorer.com/glossary/bp/)
