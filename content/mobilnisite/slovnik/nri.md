---
slug: "nri"
url: "/mobilnisite/slovnik/nri/"
type: "slovnik"
title: "NRI – Network Resource Identifier"
date: 2025-01-01
abbr: "NRI"
fullName: "Network Resource Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nri/"
summary: "Část dočasné identity mobilního účastníka (TMSI) používaná v systémech GSM, UMTS a LTE k směrování signalizačních zpráv ke správnému uzlu páteřní sítě (MSC nebo SGSN) v rámci pool oblasti. Umožňuje ef"
---

NRI je součástí dočasné identity mobilního účastníka (TMSI) používané k směrování signalizačních zpráv ke správnému uzlu páteřní sítě (MSC nebo SGSN) v rámci pool oblasti pro účely správy mobility a vyrovnávání zatížení.

## Popis

Network Resource Identifier (NRI) je specifické pole ve struktuře dočasné identity mobilního účastníka ([TMSI](/mobilnisite/slovnik/tmsi/)) a jejích derivátů, jako je [P-TMSI](/mobilnisite/slovnik/p-tmsi/) v [GPRS](/mobilnisite/slovnik/gprs/)/UMTS. TMSI je dočasný identifikátor přidělený sítí mobilnímu účastníkovi za účelem ochrany trvalého mezinárodního identifikátoru mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)) před odposlechem. NRI je podmnožina bitů v hodnotě TMSI, která se používá pro směrování v rámci poolu uzlů páteřní sítě. V obvodu přepínaných ([CS](/mobilnisite/slovnik/cs/)) doménách směruje ke správnému Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a v paketově přepínaných ([PS](/mobilnisite/slovnik/ps/)) doménách směruje ke správnému Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)).

Architektonicky je tento koncept používán v oblasti poolu NRI (Network Resource Identifier). Jedná se o geografickou oblast obsluhovanou skupinou (poolem) MSC nebo SGSN. Když se UE registruje v síti, uzel páteřní sítě (např. MSC z poolu) přidělí TMSI, které obsahuje hodnotu NRI odpovídající tomuto konkrétnímu uzlu. Struktura TMSI, včetně délky a pozice pole NRI, je konfigurována operátorem sítě. Například operátor může určit 10 nejvýznamnějších bitů TMSI jako NRI. Zbývající bity slouží jako lokální identifikátor jedinečný v rámci daného uzlu.

Princip fungování je klíčový pro správu mobility a relací. Když UE odešle signalizační zprávu (např. Location Update Request nebo Service Request) a obsahuje své TMSI, uzel přístupové rádiové sítě (RAN) (BSC v GSM, RNC v UMTS nebo eNodeB v LTE) prozkoumá pole NRI. RAN je nakonfigurován mapovací tabulkou, která přiřazuje každou možnou hodnotu NRI konkrétnímu uzlu páteřní sítě (MSC nebo SGSN) z poolu. RAN použije toto NRI k směrování počáteční zprávy přímo ke správnému uzlu páteřní sítě, aniž by bylo nutné žádost rozesílat všem uzlům v poolu. Tento mechanismus je znám jako směrování na základě NRI. Umožňuje, aby bylo UE efektivně spravováno stejným uzlem páteřní sítě, když se pohybuje v rámci pool oblasti, a podporuje funkce jako MSC/SGSN pooling pro sdílení zátěže a redundanci. Pokud se UE přesune do oblasti, kde NRI není rozpoznáno (např. mimo svůj domovský pool), RAN použije výchozí postupy směrování, což často vede k přidělení nového TMSI s lokálním NRI.

## K čemu slouží

NRI bylo vytvořeno za účelem řešení problému efektivního a škálovatelného směrování signalizace mobilních účastníků ve sdílené přístupové rádiové síti připojené k více uzlům páteřní sítě. V raných nasazeních GSM byl BSC typicky připojen k jedinému MSC. S růstem sítí operátoři nasadili pooly MSC nebo SGSN pro zvýšení kapacity a zajištění redundancy (MSC/SGSN Pool). Bez mechanismu NRI by RAN neměl způsob, jak zjistit, který MSC v poolu obsluhuje konkrétní UE při navázání kontaktu, což by mohlo vyžadovat neefektivní broadcastové dotazy nebo by vynucovalo statická, nepružná propojení mezi rádiovými buňkami a uzly páteřní sítě.

NRI tento problém řeší vložením směrovacích informací přímo do dočasného identifikátoru účastníka. To umožňuje bezstavové směrování na straně RAN: RAN jednoduše extrahuje bity NRI z TMSI a přepošle zprávu příslušnému uzlu. To umožňuje skutečné vyrovnávání zatížení a redundanci v rámci poolu. Pokud jeden MSC selže, jiný MSC v poolu může převzít jeho provoz a UE mohou být redistribuována přidělením nových TMSI s různými NRI. Odděluje topologii rádiové sítě od topologie páteřní sítě, což poskytuje významnou provozní flexibilitu.

Historicky bylo jeho zavedení (koncepčně od R99 pro UMTS/GPRS) klíčovým prvkem pro pooling páteřní sítě, který zlepšuje odolnost sítě, zjednodušuje plánování sítě (není potřeba definovat hraniční oblasti MSC) a zvyšuje využití zdrojů. Vyřešilo omezení dřívějších, rigidnějších architektur a zůstává základním konceptem pro správu mobility v sítích 2G, 3G a 4G, i když 5G zavádí jiné mechanismy, jako je 5G-GUTI a servisně orientovaná architektura.

## Klíčové vlastnosti

- Konfigurovatelné bitové pole ve struktuře TMSI/P-TMSI
- Umožňuje RAN (BSC/RNC/eNodeB) směrovat počáteční zprávy UE ke správnému MSC nebo SGSN v poolu
- Podporuje architektury MSC Pool a SGSN Pool pro vyrovnávání zatížení a redundanci
- Definuje oblast poolu NRI (Network Resource Identifier) pro plynulou mobilitu
- Umožňuje dynamické přeřazení UE mezi uzly páteřní sítě v rámci poolu
- Chrání soukromí účastníka tím, že je součástí dočasného identifikátoru (TMSI)

## Související pojmy

- [TMSI – Temporary Mobile Subscriber Identifier](/mobilnisite/slovnik/tmsi/)
- [P-TMSI – Packet-Temporary Mobile Subscriber Identity](/mobilnisite/slovnik/p-tmsi/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 48.018** (Rel-19) — BSS-SGSN Interface for GPRS Control

---

📖 **Anglický originál a plná specifikace:** [NRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nri/)
