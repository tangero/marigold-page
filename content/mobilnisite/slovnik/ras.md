---
slug: "ras"
url: "/mobilnisite/slovnik/ras/"
type: "slovnik"
title: "RAS – Reliability, Availability and Survivability"
date: 2024-01-01
abbr: "RAS"
fullName: "Reliability, Availability and Survivability"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ras/"
summary: "Soubor principů a požadavků zajišťující provozuschopnost a odolnost síťových služeb vůči selháním, katastrofám nebo útokům. Zahrnuje konstrukční, provozní a architektonická opatření pro udržení kontin"
---

RAS je soubor principů a požadavků zajišťující odolnost a provozuschopnost služeb sítě 3GPP vůči selháním, katastrofám nebo útokům prostřednictvím konstrukčních a provozních opatření.

## Popis

Spolehlivost, dostupnost a přežitelnost (Reliability, Availability and Survivability – RAS) je komplexní rámec v rámci standardů 3GPP, který definuje požadavky a mechanismy pro udržení integrity síťových služeb za různých podmínek selhání. Je řešen napříč více technickými specifikacemi, včetně specifikací pro správu sítě (řada 32) a rádiového přístupu (řada 38). RAS není jediný protokol, ale soubor konstrukčních cílů, architektonických vlastností a provozních postupů, které zajišťují, že síť splňuje přísné smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)). Spolehlivost (Reliability) označuje pravděpodobnost, že systém vykonává své zamýšlené funkce bez selhání po stanovené období. Dostupnost (Availability) je podíl času, kdy je systém v provozuschopném stavu, často měřený v procentech (např. 99,999 % neboli 'pět devítek'). Přežitelnost (Survivability) je schopnost sítě udržet kontinuitu služeb během a po závažných selháních, jako jsou přírodní katastrofy, hardwarové poruchy nebo kybernetické útoky.

Architektonicky je RAS implementován prostřednictvím redundance, odolnosti proti poruchám a samoobnovovacích mechanismů na více vrstvách sítě. V jádru sítě to zahrnuje geograficky distribuovaná datová centra, redundantní síťové funkce (např. duálně připojené [MME](/mobilnisite/slovnik/mme/), [SGW](/mobilnisite/slovnik/sgw/), [PGW](/mobilnisite/slovnik/pgw/)) a postupy stavového převzetí služeb při selhání. U rádiové přístupové sítě (RAN) RAS zahrnuje funkce jako duální konektivita, robustní propojení fronthaul/backhaul a odolnost základnových stanic. Mezi klíčové komponenty patří správci redundance, systémy detekce poruch (využívající protokoly jako [OAM](/mobilnisite/slovnik/oam/)) a automatizované skripty pro obnovu. Rámec také zahrnuje plány obnovy po havárii, kde záložní lokality mohou převzít provoz, pokud jsou primární lokality ohroženy.

Provozně je RAS řízen prostřednictvím systému Operations, Administration and Maintenance (OAM), který kontinuálně monitoruje zdraví sítě pomocí dat o výkonu a správě poruch. Když je detekováno selhání, systém spustí předdefinované zmírňující akce, jako je přeměrování provozu, restartování softwarových instancí nebo přepnutí na záložní hardware. V sítích 5G jsou principy RAS rozšířeny prostřednictvím cloud-nativních návrhů využívajících mikroslužby a orchestraci kontejnerů (např. Kubernetes), které umožňují rychlé škálování a hojení. Rámec také zahrnuje požadavky na pravidelné testování, jako jsou cvičení obnovy po havárii a audity odolnosti, aby bylo zajištěno, že RAS mechanismy fungují podle očekávání v reálných scénářích selhání.

## K čemu slouží

Požadavky RAS byly formalizovány v 3GPP, aby řešily kritickou potřebu, aby telekomunikační sítě byly vysoce spolehlivé, zejména s tím, jak se společnost stále více spoléhá na mobilní konektivitu pro základní služby. Před explicitními standardy RAS byla odolnost sítě často závislá na dodavateli nebo implementována ad-hoc, což vedlo k nekonzistentní kvalitě služeb během selhání. Rámec poskytuje jednotnou sadu cílů a metod pro návrh a provoz sítí, které mohou odolat poruchám, katastrofám a útokům při zachování přijatelné úrovně služeb.

Motivace vychází z vývoje mobilních sítí v kritickou infrastrukturu podporující nouzovou komunikaci, finanční transakce, zdravotnictví a průmyslovou automatizaci. Tyto aplikace vyžadují téměř dokonalou dostupnost a rychlé zotavení z narušení. RAS řeší problémy jako jediné body selhání, dlouhé doby výpadků a nedostatečná připravenost na katastrofy. Zavedením principů RAS do síťové architektury od počátku mohou operátoři snížit výpadky, zlepšit spokojenost zákazníků a splnit regulatorní povinnosti týkající se kontinuity služeb.

Historicky RAS získala na významu se zavedením plně IP sítí ve vydání 8, které přineslo nové režimy selhání ve srovnání s tradičními okruhově komutovanými systémy. Byla dále zdůrazněna v 5G (od vydání 15 dále) kvůli podpoře ultra-spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a síťového řezání, kde specifické řezy (např. pro veřejnou bezpečnost) vyžadují výjimečnou odolnost. Rámec řeší omezení dřívějších sítí tím, že ukládá systematické přístupy k redundanci, automatizované správě poruch a geografické disperzi, čímž zajišťuje, že moderní sítě 3GPP mohou poskytovat robustnost očekávanou od základní digitální infrastruktury.

## Klíčové vlastnosti

- Definuje cíle pro metriky spolehlivosti (např. MTBF), dostupnosti (např. procento provozuschopnosti) a přežitelnosti
- Architektonická redundance na úrovni uzlů, spojů a lokalit (redundance N+k, geografická redundance)
- Automatizované mechanismy detekce, izolace a obnovy poruch (samoobnova)
- Integrace se systémy OAM pro kontinuální monitoring a proaktivní údržbu
- Plány obnovy po havárii včetně aktivace záložních lokalit a replikace dat
- Podpora kontinuity služeb během údržby a softwarových aktualizací

## Související pojmy

- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 36.755** (Rel-15) — US 600 MHz LTE Band 71 Technical Report
- **TS 38.807** (Rel-16) — NR beyond 52.6 GHz Study
- **TR 38.820** (Rel-16) — NR; 7-24 GHz Frequency Range Study
- **TR 38.860** (Rel-17) — NR; Study on Extended 600 MHz NR band
- **TR 38.892** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [RAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ras/)
