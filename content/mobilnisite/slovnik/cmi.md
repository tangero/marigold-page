---
slug: "cmi"
url: "/mobilnisite/slovnik/cmi/"
type: "slovnik"
title: "CMI – Codec Mode Indication"
date: 2025-01-01
abbr: "CMI"
fullName: "Codec Mode Indication"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cmi/"
summary: "CMI je signalizační mechanismus v 3GPP, který indikuje režim hlasového kodeku používaný pro hlasový hovor. Je přenášen ze sítě k mobilní stanici a umožňuje příjemci správně dekódovat hlasový rámec. To"
---

CMI je signalizační mechanismus v 3GPP, který indikuje režim hlasového kodeku používaný pro hlasový hovor, což příjemci umožňuje správně dekódovat hlasový rámec.

## Popis

Codec Mode Indication (CMI) je kritický řídicí parametr v rádiové přístupové síti 3GPP, specificky definovaný pro hlasové služby v GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) a později odkazovaný ve specifikacích pro další rádiové technologie. Funguje jako součást signalizace v pásmu (in-band) mezi podsystémem základnové stanice ([BSS](/mobilnisite/slovnik/bss/)) sítě a mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)). CMI je vloženo do protokolových datových jednotek rádiového rozhraní, typicky do struktury samotného hlasového rámce nebo jeho přidruženého řídicího kanálu, aby explicitně signalizovalo, který z několika možných režimů hlasového kodeku je aktivní pro aktuální přenosový burst.

Z architektonického hlediska je CMI generováno na straně sítě, konkrétně jednotkou Transcoder and Rate Adaptation Unit (TRAU) nebo ekvivalentní zpracovatelskou entitou po kódování hlasu. Indikace je pak předána přes BSS a zahrnuta do rádiového bloku vysílaného přes rozhraní vzduchu. Na přijímající mobilní stanici fyzická vrstva a software pro zpracování hlasu extrahují hodnotu CMI před pokusem o dekódování hlasové datové části. To umožňuje dekodéru MS vybrat správný algoritmus, kodek a pravidla pro parsování datové rychlosti odpovídající indikovanému režimu. Mechanismus je těsně integrován s operacemi kodeků Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a AMR-Wideband (WB-AMR), kde může být dynamicky vybráno více režimů kodeku (s různými datovými rychlostmi a kompromisy mezi kvalitou hlasu a odolností proti chybám).

Jeho role je zásadní pro dynamickou adaptaci hlasových služeb. Bez explicitní a spolehlivé CMI by musela mobilní stanice režim kodeku detekovat naslepo, což je náchylné k chybám, zejména v podmínkách špatného rádiového signálu. Nesprávná detekce režimu vede ke katastrofálním selháním dekódování a výraznému zhoršení kvality hlasu. CMI zajišťuje, že oba konce komunikačního spoje jsou synchronizovány v porozumění formátu hlasového rámce. Tato synchronizace je nezbytná pro funkce jako adaptace režimu kodeku (kde síť na základě podmínek kanálu přikáže změnu z jednoho AMR režimu na jiný) a pro zvládnutí předávání hovorů mezi buňkami, které mohou být konfigurovány s různými výchozími režimy kodeku. Specifikace (TS 45.009 pro GERAN, TS 26.102 pro shodu kodeku a TS 26.202 pro funkce zpracování hlasu hlasového kodeku) definují přesné bitové vzory pro CMI, jejich mapování na konkrétní režimy kodeku a postupy pro jeho spolehlivý přenos a interpretaci.

## K čemu slouží

CMI bylo vytvořeno k vyřešení základního problému synchronizace režimu kodeku mezi sítí a mobilním terminálem v digitálních celulárních systémech používajících hlasové kodeky s proměnnou datovou rychlostí. Před zavedením sofistikovaných kodeků, jako je [AMR](/mobilnisite/slovnik/amr/) v 3GPP Release 4/5, používal GSM kodek s pevnou datovou rychlostí (Full Rate, Half Rate). U kódování s pevnou rychlostí byl formát rámce konstantní, takže nebyla potřeba žádná dynamická indikace. Příchod AMR však přinesl více provozních režimů (např. 12,2 kbps, 7,4 kbps, 4,75 kbps), z nichž každý je optimální pro různé podmínky rádiového kanálu. Síť potřebovala schopnost přikázat změnu režimu, aby udržela rovnováhu mezi kvalitou hlasu a kapacitou kanálu (odolnější režimy s nižší datovou rychlostí pro slabé pokrytí).

Hlavním problémem bylo zajistit, aby mobilní stanice přesně věděla, který režim byl použit pro každý přijatý hlasový rámec, aby jej mohla správně dekódovat. Naslepo prováděná detekce ze strany [MS](/mobilnisite/slovnik/ms/) byla výpočetně složitá a nespolehlivá. CMI poskytuje explicitní signalizační řešení s nízkou režií, které je přímo vloženo do hlasových dat. Tím je zaručena spolehlivá synchronizace, která umožňuje klíčovou funkci adaptace spojení (link adaptation) pro hlas. Přímo řešilo omezení předchozích systémů s pevným kodekem tím, že umožnilo dynamické síťové řízení kompromisu mezi kvalitou hlasu a pokrytím/kapacitou. Jeho vytvoření bylo motivováno potřebou zlepšit kvalitu hlasu za špatných podmínek signálu a zvýšit kapacitu systému používáním režimů s nižší datovou rychlostí, pokud je to možné, a to vše bez zavádění dekódovacích chyb na terminálu.

## Klíčové vlastnosti

- Explicitně signalizuje aktivní režim hlasového kodeku (např. AMR 12.2, 7.4, 4.75) ze sítě k mobilní stanici
- Umožňuje spolehlivé dekódování synchronizací vysílače a přijímače na formátu rámce
- Zásadní pro dynamickou adaptaci režimu kodeku (adaptaci spojení) na základě kvality rádiového kanálu
- Podporuje procedury předávání hovorů mezi buňkami s potenciálně různými konfiguracemi kodeků
- Signalizace v pásmu (in-band) s nízkou režií integrovaná do mechanismu přenosu hlasu
- Definováno pro GERAN (GSM/EDGE) a odkazováno v kontextu provozu AMR kodeku napříč systémy 3GPP

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TS 45.009** (Rel-19) — GSM AMR Link Adaptation & Control

---

📖 **Anglický originál a plná specifikace:** [CMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmi/)
