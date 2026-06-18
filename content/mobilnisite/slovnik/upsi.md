---
slug: "upsi"
url: "/mobilnisite/slovnik/upsi/"
type: "slovnik"
title: "UPSI – UE Policy Section Identifier"
date: 2025-01-01
abbr: "UPSI"
fullName: "UE Policy Section Identifier"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/upsi/"
summary: "Jedinečný identifikátor pro konkrétní sekci politiky v rámci politiky UE doručené sítí. Umožňuje UE spravovat, ukládat a aplikovat různé sady síťových politik, například pro výběr sítě nebo výběr tras"
---

UPSI je jedinečný identifikátor pro konkrétní sekci politiky v rámci politiky UE, který umožňuje UE spravovat, ukládat a aplikovat různé sady síťových politik pro dynamické řízení.

## Popis

UE Policy Section Identifier (UPSI) je klíčová součást rámce pro řízení politik (Policy Control Framework) 3GPP, konkrétně definovaná pro 5G systém (5GS). Funguje jako jedinečná značka nebo klíč, který identifikuje samostatný, ucelený blok pravidel politiky – známý jako sekce politiky UE (UE Policy Section) – který je poskytován uživatelskému zařízení (UE) funkcí pro řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) sítě. Samotná politika UE je komplexní dokument, který může obsahovat více takových sekcí, z nichž každá je identifikována vlastním UPSI. Tyto sekce se mohou týkat různých domén politik, jako je politika pro vyhledávání a výběr přístupové sítě ([ANDSP](/mobilnisite/slovnik/andsp/)) pro výběr mezi 3GPP a ne-3GPP přístupem, nebo politika pro výběr trasy UE ([URSP](/mobilnisite/slovnik/ursp/)) pro určení, jak je směrován provoz aplikací (např. ke konkrétnímu názvu datové sítě ([DNN](/mobilnisite/slovnik/dnn/)) nebo síťovému řezu). UE tyto sekce politik ukládá lokálně a každou asociuje s jejím UPSI.

Z architektonického hlediska je UPSI generováno a spravováno PCF. Když PCF určí, že UE vyžaduje novou nebo aktualizovanou politiku, sestaví kontejner politiky UE, který obsahuje jednu nebo více sekcí politiky UE, z nichž každá je označena UPSI. Tento kontejner je následně doručen do UE prostřednictvím funkce pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) pomocí transportního mechanismu N1 [NAS](/mobilnisite/slovnik/nas/). Specifikace 24.501 podrobně popisuje signalizační procedury NAS pro toto doručení. PCF může také spravovat životní cyklus těchto sekcí politik prostřednictvím služby Npcf_UEPolicyControl, definované v 29.525, což mu umožňuje poskytovat, aktualizovat nebo mazat konkrétní sekce identifikované jejich UPSI.

Úlohou UPSI je umožnit efektivní a granulární správu politik. Namísto opětovného přenosu celého dokumentu politiky UE při každé změně může síť cílit na jednotlivé sekce. UE používá UPSI k identifikaci, kterou uloženou sekci politiky má použít pro daný kontext. Například když UE potřebuje vybrat přístupovou síť, vyhledá sekci ANDSP pomocí jejího specifického UPSI. Tento modulární přístup snižuje signalizační režii, šetří úložný prostor UE umožněním selektivních aktualizací a poskytuje síti jemně odstupňovanou kontrolu nad chováním UE. Správa těchto identifikátorů a jim přiřazených sekcí je dále podporována službami, jako je funkce síťového repozitáře ([NRF](/mobilnisite/slovnik/nrf/)) pro vyhledávání, jak je uvedeno ve specifikacích 29.513 a 29.519.

## K čemu slouží

UPSI bylo zavedeno v 5G (Release 15) k řešení omezení monolitické správy politik v předchozích generacích, jako je 4G EPS. V EPS byly informace o politice, jako je [ANDSP](/mobilnisite/slovnik/andsp/), doručovány jako jediný, nedělitelný celek. Jakákoli změna, bez ohledu na velikost, vyžadovala opětovné odeslání celé politiky, což vedlo k neefektivnímu využití rádiových zdrojů a zpracování v UE. Protože 5G přineslo složitější domény politik (zejména URSP pro sofistikované směrování provozu a výběr síťových řezů), potřeba modulárního, granulárního řízení politik se stala prvořadou.

Vytvoření UPSI umožňuje datově řízenou, službami založenou architekturu politik v souladu se základními principy 5G. Řeší problém škálovatelné distribuce politik v síti podporující rozmanité případy užití, od rozšířeného mobilního širokopásmového připojení po masivní IoT a ultra-spolehlivou komunikaci s nízkou latencí. Každý případ užití nebo tenant (prostřednictvím síťového řezání) může vyžadovat odlišnou sadu pravidel. UPSI umožňuje PCF sestavit přizpůsobenou politiku z diskrétních, znovupoužitelných sekcí a aktualizovat pouze části, které se mění. To je nezbytné pro podporu dynamických síťových podmínek, služeb specifických pro účastníka a efektivní správu zdrojů UE, což tvoří základní prvek pro automatizovanou správu sítě a služeb.

## Klíčové vlastnosti

- Jednoznačně identifikuje samostatnou sekci politiky UE (např. ANDSP, URSP).
- Umožňuje PCF granulární poskytování, modifikaci a mazání sekcí politik.
- Snižuje signalizační režii tím, že umožňuje cílené aktualizace namísto úplné výměny politiky.
- Podporuje ukládání a správu životního cyklu více sekcí politik v rámci UE.
- Integruje se s architekturou 5G založenou na službách prostřednictvím služby Npcf_UEPolicyControl.
- Usnadňuje efektivní aplikaci politik; UE používá UPSI k načtení správné sekce pro rozhodování.

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.519** (Rel-19) — UDR Usage for Policy & Exposure Data
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3

---

📖 **Anglický originál a plná specifikace:** [UPSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/upsi/)
