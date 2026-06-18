---
slug: "mwab"
url: "/mobilnisite/slovnik/mwab/"
type: "slovnik"
title: "MWAB – Mobile gNB with Wireless Access Backhauling"
date: 2026-01-01
abbr: "MWAB"
fullName: "Mobile gNB with Wireless Access Backhauling"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mwab/"
summary: "MWAB označuje 5G gNB základnovou stanici, která pro připojení přenosové trasy (backhaul) k jádru sítě využívá bezdrátové spoje namísto pevného vlákna. Umožňuje rychlé a flexibilní nasazení v oblastech"
---

MWAB je 5G gNB základnová stanice, která pro svou přenosovou trasu (backhaul) využívá bezdrátové spoje, což umožňuje rychlé nasazení v oblastech bez kabelové infrastruktury.

## Popis

Mobile gNB with Wireless Access Backhauling (MWAB, mobilní gNB s bezdrátovou přenosovou trasou) je koncept síťového uzlu v 5G, ve kterém gNodeB (gNB) pro přenosovou trasu (backhaul) využívá bezdrátový spoj namísto tradičního pevného připojení, jako je vlákno nebo point-to-point mikrovlnný spoj. Samotné gNB je umístěno na mobilní platformě, například na vozidle, dronu nebo přenosné jednotce, díky čemuž je celý přístupový uzel přemístitelný. Primární bezdrátový backhaulový spoj je typicky zřízen prostřednictvím samostatného 5G rádiového spoje, často využívajícího vyšší frekvenční pásmo s podstatnou šířkou pásma, k dárci (donor gNB) nebo k vyhrazenému agregačnímu uzlu přenosové trasy, který má pevné připojení k 5G Core síti. Tím vzniká dvouskoková bezdrátová cesta: první skok je bezdrátová přenosová trasa mezi MWAB a dárcovským místem a druhý skok je přístupový spoj mezi MWAB a koncovými uživatelskými zařízeními (UE).

Z architektonického hlediska obsahuje MWAB všechny standardní funkce gNB – zahrnující Centrální jednotku ([CU](/mobilnisite/slovnik/cu/)) a Distribuovanou jednotku ([DU](/mobilnisite/slovnik/du/)) – ale jeho transportní síťová vrstva je navržena tak, aby zvládala specifické výzvy bezdrátové přenosové trasy. To zahrnuje robustní protokoly vrstvy 2 a vrstvy 3 pro směrování, kvalitu služeb (QoS) a synchronizaci přes bezdrátové médium. Klíčem pro jeho fungování je technologie integrovaného přístupu a přenosové trasy ([IAB](/mobilnisite/slovnik/iab/)), standardizovaná v 3GPP, která umožňuje dynamické sdílení stejného spektra a rozhraní mezi přístupovými a backhaulovými funkcemi, ačkoli MWAB může používat i vyhrazené spektrum. MWAB musí zvládat správu mobility sám pro sebe, pokud se jeho platforma pohybuje, což vyžaduje procedury předávání (handover) pro jeho vlastní backhaulový spoj, aby byla zajištěna nepřetržitá služba pro připojená UE.

Jeho úlohou v síti je poskytovat extrémní flexibilitu nasazení a zhušťování sítě. Působí jako posilovač kapacity a pokrytí, který může být dynamicky umístěn na základě aktuální poptávky, například během sportovní akce, přírodní pohromy, kdy je infrastruktura poškozena, nebo v rozvíjející se oblasti bez vybudovaného vlákna. MWAB rozšiřuje dosah 5G sítě vytvořením pohyblivé lokalitě buňky, která není omezena dostupností fyzických backhaulových kabelů, což umožňuje neterestriální sítě, rychlá vojenská nasazení a nákladově efektivní pokrytí ve venkovských nebo dočasných scénářích.

## K čemu slouží

MWAB byl vyvinut, aby překonal základní omezení pevné backhaulové infrastruktury, která je drahá, časově náročná na nasazení a neflexibilní. Tradiční lokalitě buňky vyžadují výkopové práce pro vlákno nebo pečlivé zaměření pro mikrovlnné spoje, což činí rychlé nasazení nebo dočasné pokrytí ekonomicky neproveditelným. To představovalo významnou výzvu pro poskytnutí okamžité konektivity v situacích nouzového zásahu, pro dodatečnou kapacitu při velkých akcích nebo pro pokrytí odlehlých oblastí. Motivace pro MWAB úzce souvisí s vizí 5G o všudypřítomné, ultra-spolehlivé a vysokokapacitní konektivitě kdekoli a kdykoli.

Vznik MWAB je poháněn konvergencí několika technologických faktorů: vysokou propustností a nízkou latencí 5G New Radio (NR), díky nimž je výkon bezdrátové přenosové trasy konkurenceschopný s pevnými spoji; pokročilým formováním svazku a mmWave spektrem, které poskytují potřebný směrový zisk a šířku pásma; a standardizací integrovaného přístupu a přenosové trasy ([IAB](/mobilnisite/slovnik/iab/)) v 3GPP Release 16. MWAB řeší problém 'poslední míle' přenosové trasy pro mobilní uzly, což umožňuje síťovým operátorům nasazovat buňky na požádání bez předem existující infrastruktury. To je klíčové pro naplnění plného potenciálu 5G ve scénářích, jako jsou síťové sítě, kde by gNB na autobusu mohlo poskytovat lokalizované hotspotové pokrytí, nebo při obnově po katastrofách, kdy je existující síť narušena.

## Klíčové vlastnosti

- Využívá bezdrátové 5G NR spoje pro připojení přenosové trasy (backhaul), čímž odstraňuje potřebu pevného kabelu
- Integrovaná funkce gNB na mobilní platformě (vozidlo, letecká platforma, přenosná jednotka)
- Podporuje dynamické zřizování backhaulového spoje a jeho předávání (handover) pro mobilitu uzlu
- Může využívat technologii Integrated Access and Backhaul (IAB) pro efektivitu spektra
- Umožňuje rychlé nasazení sítě a vstřikování kapacity na požádání
- Poskytuje redundanci a odolnost přenosové trasy v případě výpadku pevné infrastruktury

## Související pojmy

- [IAB – Integrated Access and Backhaul](/mobilnisite/slovnik/iab/)
- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)

## Definující specifikace

- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.515** (Rel-19) — Ngmlc Service Based Interface Protocol
- **TS 29.572** (Rel-19) — Nlmf Service Based Interface Stage 3

---

📖 **Anglický originál a plná specifikace:** [MWAB na 3GPP Explorer](https://3gpp-explorer.com/glossary/mwab/)
