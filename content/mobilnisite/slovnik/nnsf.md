---
slug: "nnsf"
url: "/mobilnisite/slovnik/nnsf/"
type: "slovnik"
title: "NNSF – NAS Node Selection Function"
date: 2025-01-01
abbr: "NNSF"
fullName: "NAS Node Selection Function"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nnsf/"
summary: "NNSF je funkce v jádru sítě, která vybírá vhodný uzel NAS (Non-Access Stratum) pro UE. Zajišťuje efektivní směrování NAS signalizace, optimalizuje využití zdrojů a správu relací v mobilních sítích."
---

NNSF je funkce jádra sítě, která vybírá vhodný uzel Non-Access Stratum pro uživatelské zařízení, aby zajistila efektivní směrování signalizace a optimalizovanou správu relací.

## Popis

Funkce pro výběr uzlu [NAS](/mobilnisite/slovnik/nas/) (NNSF) je funkce jádra sítě odpovědná za výběr vhodného uzlu Non-Access Stratum (NAS) pro uživatelské zařízení (UE) během připojování k síti nebo navazování relace. NAS označuje protokolovou vrstvu mezi UE a jádrem sítě, která zpracovává signalizaci pro správu mobility, správu relací a autentizaci nezávisle na technologii rádiového přístupu. NNSF určuje, který uzel NAS (např. [MME](/mobilnisite/slovnik/mme/) v LTE/EPC, [AMF](/mobilnisite/slovnik/amf/) v 5GC) má obsluhovat UE na základě kritérií, jako je identita UE, topologie sítě, stav zatížení a zásady.

Při provozu, když se UE pokouší připojit k síti, přístupová síť (např. [eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v 5G) přijme počáteční zprávu NAS a může vyvolat NNSF, aby zvolil správný uzel NAS. NNSF vyhodnocuje faktory, jako je síťový řez, na který je UE přihlášeno, geografická poloha, aktuální zatížení dostupných uzlů NAS a případné specifické směrovací zásady. Poté nasměruje NAS signalizaci na vybraný uzel, čímž zajistí, že UE je spravováno vhodnou entitou pro své služby a požadavky.

Klíčové komponenty zapojené do NNSF zahrnují prvky přístupové sítě, které spouštějí výběr, samotné uzly NAS (MME, AMF) a případně vyhrazenou logiku výběru uvnitř jádra sítě. V systémech 5G je NNSF integrována do funkcí přístupové sítě nebo jádra sítě pro podporu síťového řezování a flexibilního směrování NAS. Tato funkce zvyšuje efektivitu sítě vyvažováním zatížení mezi uzly NAS, umožňuje řezově specifické směrování a snižuje latenci signalizace.

NNSF hraje klíčovou roli v optimalizaci využití zdrojů jádra sítě a podpoře pokročilých funkcí, jako je síťové řezování. Inteligentním výběrem uzlů NAS zajišťuje, že jsou UE připojena k uzlům schopným obsloužit jejich specifické požadavky na služby, čímž zlepšuje celkový výkon sítě a uživatelský zážitek. Je obzvláště důležitá v sítích 5G, kde různé služby (např. IoT, vylepšené mobilní širokopásmové připojení) vyžadují diferencované zpracování NAS.

## K čemu slouží

NNSF byla zavedena, aby řešila potřebu efektivního a inteligentního výběru uzlů [NAS](/mobilnisite/slovnik/nas/) v mobilních jádrových sítích. Jak se sítě vyvíjely, aby podporovaly více UE, rozmanité služby a složité topologie, pouhé přiřazování uzlů NAS na základě statických konfigurací se stalo neefektivním. NNSF řeší problémy, jako je nevyvážené zatížení mezi uzly NAS, suboptimální směrování pro specifické služby a nedostatek flexibility při zpracování síťových řezů nebo geografických variací.

Historicky měly dřívější verze jednodušší mechanismy směrování NAS, ale s verzí Rel-5 a následnými vylepšeními poskytla NNSF možnosti dynamického výběru. Byla motivována růstem rozsahu sítě, zavedením nových služeb vyžadujících specializované zpracování NAS a potřebou vyrovnávání zatížení, aby se předešlo zahlcení uzlů. Umožněním dynamického výběru NNSF zlepšuje odolnost sítě, škálovatelnost a kvalitu služeb.

Vytvoření NNSF také podporuje síťové řezování v 5G, kde různé řezy mohou vyžadovat různé uzly NAS pro optimalizovanou správu. Umožňuje síti směrovat NAS signalizaci na uzly přizpůsobené charakteristikám řezu (např. řezy s nízkou latencí na blízké uzly). Tím se řeší omezení pevného směrování, které se nedokázalo přizpůsobit řezům nebo měnícím se síťovým podmínkám, a zajišťuje se, že zpracování NAS je v souladu s požadavky služeb a síťovými zásadami.

## Klíčové vlastnosti

- Dynamický výběr uzlů NAS na základě identity UE a síťových podmínek
- Podpora vyrovnávání zatížení mezi uzly NAS k prevenci zahlcení
- Umožňuje optimalizaci směrování NAS pro síťové řezování
- Integruje se s prvky přístupové sítě pro počáteční připojení UE
- Pro výběr používá kritéria jako geografie, ID řezu a zatížení uzlu
- Zlepšuje efektivitu signalizace a využití zdrojů v jádru sítě

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.820** (Rel-8) — 3G Home NodeB Study Report
- **TS 29.108** (Rel-19) — RANAP on E-interface for 3G MSC Relocation
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TR 38.882** (Rel-18) — Technical Report on UE Location Service
- **TS 43.130** (Rel-19) — Iur-g Interface Overview

---

📖 **Anglický originál a plná specifikace:** [NNSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/nnsf/)
