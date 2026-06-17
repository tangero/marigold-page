---
slug: "gummei"
url: "/mobilnisite/slovnik/gummei/"
type: "slovnik"
title: "GUMMEI – Globally Unique MME Identifier"
date: 2025-01-01
abbr: "GUMMEI"
fullName: "Globally Unique MME Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gummei/"
summary: "Globálně jednoznačný identifikátor pro entitu Mobility Management Entity (MME) v systémech EPS a 5GS. Kombinuje identitu PLMN s MME Group ID a MME Code, aby jednoznačně určil MME v celosvětovém měřítk"
---

GUMMEI je globálně jednoznačný identifikátor pro entitu Mobility Management Entity (MME), který kombinuje identitu PLMN s MME Group ID a MME Code, aby jednoznačně určil MME v celosvětovém měřítku pro směrování signalizačních zpráv.

## Popis

Globálně jednoznačný identifikátor [MME](/mobilnisite/slovnik/mme/) (GUMMEI) je složený identifikátor, který jednoznačně identifikuje konkrétní uzel Mobility Management Entity (MME) v globálním síťovém ekosystému Evolved Packet System (EPS) a 5G System (5GS). Je strukturován ze tří hlavních složek: identity Public Land Mobile Network (PLMN) ([MCC](/mobilnisite/slovnik/mcc/) a [MNC](/mobilnisite/slovnik/mnc/)), MME Group ID (MMEGI) a MME Code ([MMEC](/mobilnisite/slovnik/mmec/)). Identita PLMN identifikuje domovskou síť MME. MMEGI identifikuje skupinu MME v rámci této PLMN, často používanou pro vyrovnávání zátěže a redundanci. MMEC je kód, který jednoznačně identifikuje MME v rámci této konkrétní skupiny MME. Spojení PLMN ID + MMEGI + MMEC zaručuje globální jednoznačnost. Tato struktura je definována v technických specifikacích, jako jsou TS 23.003 a TS 36.413.

Z architektonického hlediska se GUMMEI hojně používá v signalizačních procedurách mezi síťovými entitami. Například během procedury počátečního připojení (initial attach) nebo aktualizace oblasti sledování (Tracking Area Update, TAU) potřebuje eNodeB (v LTE) nebo gNB (v 5G NR) vybrat MME pro UE. Pokud UE ve své signalizaci poskytne dříve přidělené GUMMEI (např. v Globally Unique Temporary Identity, [GUTI](/mobilnisite/slovnik/guti/)), může eNodeB použít části PLMN a MME Group ID k napomoci směrování zprávy do správného poolu MME. Síť poté použije celé GUMMEI k určení přesné MME, která drží kontext UE. GUMMEI je také přenášeno v zprávách mezi MME během předávání mezi MME (roaming mezi MME, interface S10) a mezi MME a dalšími funkcemi jádra sítě, jako je Serving Gateway (SGW) a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)).

Jeho role je klíčová pro správu mobility, správu relací a škálovatelnost sítě. Poskytnutím globálně jednoznačné adresy pro každou MME zabraňuje nejednoznačnosti v signalizačním směrování, což je zásadní v propojených sítích zahrnujících roaming. Hierarchická struktura (PLMN -> Skupina -> Uzel) podporuje efektivní síťové plánování. Operátoři mohou nasadit pooly MME (sdílející MMEGI) pro distribuci zátěže a odolnost; pokud jedna MME selže, jiná ve stejné skupině může převzít její UE, protože je známa identita na úrovni skupiny. GUMMEI je také klíčovou složkou při odvozování GUTI, dočasného identifikátoru přiděleného UE k ochraně jeho trvalé identity účastníka ([IMSI](/mobilnisite/slovnik/imsi/)). Bezpečnost a jednoznačnost GUMMEI podporuje integritu tohoto mechanismu ochrany soukromí. V 5GS je ekvivalentním konceptem pro funkci Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) identifikátor GUAMI (Globally Unique AMF ID), který následuje podobný strukturální princip, což zdůrazňuje zásadní důležitost tohoto typu identifikátoru v celulárních jádrových sítích.

## K čemu slouží

GUMMEI bylo zavedeno ve 3GPP Release 8 s Evolved Packet Core (EPC) k řešení problémů adresování a směrování vlastních ploché, plně IP architektury jádra sítě, která nahradila hierarchické okruhově přepínané jádro 2G/3G. V předchozích systémech bylo adresování uzlů často více lokalizované nebo vázané na paradigma okruhového přepínání. EPC zavedlo plošší architekturu s jasným oddělením řídicí roviny (MME) a uživatelské roviny (SGW/PGW), což vyžadovalo robustní, škálovatelný a jednoznačný způsob identifikace entit řídicí roviny globálně. Primárním problémem bylo zajistit, aby signalizační zprávy pro mobilního uživatele, potenciálně roamujícího kdekoli na světě, mohly být správně směrovány ke konkrétní MME, která aktuálně spravuje kontext mobility tohoto uživatele, a to i mezi mnoha MME nasazenými v poolech pro vysokou dostupnost.

Vytvoření GUMMEI bylo motivováno několika klíčovými požadavky: Za prvé, globální jednoznačnost, aby se předešlo konfliktům v mezinárodních roamingových scénářích. Za druhé, podpora síťových poolů a vyrovnávání zátěže, což umožňuje více MME obsluhovat společnou geografickou oblast. Složka Group ID to přímo řeší, umožňujíc směrování do poolu před výběrem konkrétního uzlu. Za třetí, efektivita signalizace; identifikátor je dostatečně kompaktní, aby mohl být zahrnut do četných zpráv bez nadměrné režie. Za čtvrté, umožnil vylepšené soukromí prostřednictvím GUTI. Díky existenci jednoznačného identifikátoru MME mohla síť přidělovat dočasné identity, které byly vysledovatelné pouze sítí držící mapování, čímž chránila IMSI uživatele před odposloucháváním. GUMMEI tyto problémy vyřešilo poskytnutím standardizovaného, strukturovaného identifikátoru, který se stal základním kamenem pro správu mobility v EPC a 5GC a usnadnil škálovatelné nasazení sítí LTE a 5G po celém světě. Bez něj by bylo řízení mobility ve velkých, distribuovaných, více-dodavatelských sítích výrazně složitější a náchylnější k chybám.

## Klíčové vlastnosti

- Globálně jednoznačný složený identifikátor pro MME
- Třídílná struktura: PLMN ID + MME Group ID (MMEGI) + MME Code (MMEC)
- Umožňuje jednoznačné směrování signalizačních zpráv NAS a S1-MME
- Základní složka pro odvození Globally Unique Temporary Identity (GUTI) pro soukromí UE
- Podporuje poolování MME a redundanci prostřednictvím složky MME Group ID
- Používá se v procedurách předávání mezi MME a přenosu kontextu

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [GUTI – Globally Unique Temporary UE Identity](/mobilnisite/slovnik/guti/)
- [GUAMI – Globally Unique AMF Identifier](/mobilnisite/slovnik/guami/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification

---

📖 **Anglický originál a plná specifikace:** [GUMMEI na 3GPP Explorer](https://3gpp-explorer.com/glossary/gummei/)
