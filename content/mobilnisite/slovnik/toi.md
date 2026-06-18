---
slug: "toi"
url: "/mobilnisite/slovnik/toi/"
type: "slovnik"
title: "TOI – Transmission Object Identifier"
date: 2025-01-01
abbr: "TOI"
fullName: "Transmission Object Identifier"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/toi/"
summary: "Transmission Object Identifier (TOI) je pole protokolu ve FLUTE/ALC používané k identifikaci datových objektů v rámci vysílací/multicastové relace. Umožňuje přijímačům vyžádat si konkrétní objekty pro"
---

TOI je pole protokolu ve FLUTE/ALC, které identifikuje datové objekty v rámci vysílací relace, což přijímačům umožňuje vyžádat si konkrétní objekty pro opravu nebo identifikovat komponenty služby.

## Popis

Transmission Object Identifier (TOI) je základní pole v protokolech Asynchronous Layered Coding ([ALC](/mobilnisite/slovnik/alc/)) a File Delivery over Unidirectional Transport ([FLUTE](/mobilnisite/slovnik/flute/)), které se používají pro spolehlivé doručování obsahu přes vysílací a multicastové sítě, jako jsou ty definované v 3GPP pro službu Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a její vylepšenou verzi evolved MBMS (eMBMS). TOI je číselný identifikátor, typicky o délce 16 nebo 32 bitů, který jednoznačně identifikuje 'přenosový objekt' v rámci jedné relace ALC/FLUTE. Přenosovým objektem může být soubor, segment souboru nebo jakýkoli jiný samostatný blok dat, který chce odesílatel doručit. TOI je přenášeno v hlavičce každého paketu ALC, což přijímačům umožňuje přiřadit příchozí pakety ke správnému objektu pro opětovné složení.

V rámci protokolu FLUTE se TOI používá ve spojení s File Delivery Table ([FDT](/mobilnisite/slovnik/fdt/)). FDT je [XML](/mobilnisite/slovnik/xml/) popis, který mapuje každou hodnotu TOI na metadata o odpovídajícím souboru, jako je jeho [URI](/mobilnisite/slovnik/uri/), typ obsahu, velikost a kontrolní součet. Když přijímač vstoupí do relace FLUTE, nejprve získá FDT (který je sám doručován jako objekt se známým TOI, často TOI=0). Analýzou FDT přijímač zjistí, které TOI odpovídá kterému požadovanému souboru. Jak přicházejí pakety, přijímač používá TOI k nasměrování paketů do správného vyrovnávacího bufferu pro opětovné složení. Pokud pakety chybí, může přijímač použít TOI k přesné žádosti o opětovné vyslání konkrétních paketů pro daný objekt pomocí samostatného opravného protokolu, jako je NORM nebo ALC s [LCT](/mobilnisite/slovnik/lct/) Channel.

Role TOI je klíčová pro škálovatelnost a efektivitu ve vysílacích scénářích. Protože více souborů nebo velké soubory rozdělené na mnoho objektů mohou být přenášeny prokládaně přes stejný multicastový kanál, TOI poskytuje na straně přijímače nezbytný klíč pro demultiplexování. Umožňuje selektivní příjem a opravu, kdy si přijímač může zvolit příjem pouze objektů, o které má zájem (např. konkrétní video segmenty pro [HTTP](/mobilnisite/slovnik/http/) Adaptive Streaming over broadcast), a může žádat o opravu pouze chybějících částí těchto objektů. Tento návrh minimalizuje požadavky na vyrovnávací paměť přijímače a opravný síťový provoz. V architektuře eMBMS od 3GPP se FLUTE s TOI používá na aplikační vrstvě vysílacího přenosu pro doručování souborů a segmentů potenciálně obrovskému počtu UE současně.

## K čemu slouží

TOI bylo vytvořeno k řešení problému identifikace a opětovného složení více samostatných datových objektů v rámci jediného, spojitého multicastového nebo vysílacího datového proudu. Před standardizovanými objektově orientovanými multicastovými protokoly používalo hromadné doručování dat přes vysílání často monolitické proudy nebo proprietární zapouzdření, což ztěžovalo selektivní příjem, náhodný přístup a efektivní obnovu po chybě. TOI jako součást rámce ALC/FLUTE od IETF, který přijala 3GPP, poskytuje pro tuto identifikaci odlehčený, standardizovaný mechanismus.

Jeho zavedení do specifikací 3GPP (např. TS 26.346 pro MBMS) bylo motivováno potřebou efektivního aplikačního protokolu pro služby MBMS a eMBMS. Služby jako mobilní TV, aktualizace softwaru a systémy veřejného varování vyžadují spolehlivé doručení mnoha souborů nebo mediálních segmentů mnoha uživatelům. TOI umožňuje systému MBMS tyto služby efektivně podporovat tím, že síti dovoluje bezstavově vysílat objekty a přijímačům nezávisle spravovat, které objekty konzumují a jak se zotaví ze ztráty paketů. Řeší tak omezení složitosti přijímače, protože síť nemusí spravovat stavy jednotlivých přijímačů; namísto toho je inteligence přesunuta na okraj sítě, přičemž TOI poskytuje společný referenční bod pro všechny strany.

## Klíčové vlastnosti

- Jednoznačně identifikuje datový objekt (soubor nebo segment) v rámci jedné relace ALC/FLUTE
- Přenáší se v hlavičce každého paketu ALC pro demultiplexování a opětovné složení na straně přijímače
- Používá se ve spojení s File Delivery Table (FDT), která mapuje hodnoty TOI na metadata souborů
- Umožňuje selektivní příjem a opravu, což přijímačům dovoluje žádat pouze o chybějící objekty nebo pakety
- Podporuje škálovatelné multicastové doručování oddělením stavu odesílatele od potřeb přijímače
- Základní prvek pro 3GPP eMBMS v aplikacích jako LTE Broadcast a 5G Multicast-Broadcast služby

## Související pojmy

- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)
- [ALC – Asynchronous Layered Coding](/mobilnisite/slovnik/alc/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.852** (Rel-14) — MBMS user service profiles, APIs and transport enabler study
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TR 26.947** (Rel-19) — FEC Evaluation for MBMS Enhancement

---

📖 **Anglický originál a plná specifikace:** [TOI na 3GPP Explorer](https://3gpp-explorer.com/glossary/toi/)
