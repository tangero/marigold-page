---
slug: "mme"
url: "/mobilnisite/slovnik/mme/"
type: "slovnik"
title: "MME – NPC MME Network Product Class"
date: 2026-01-01
abbr: "MME"
fullName: "NPC MME Network Product Class"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mme/"
summary: "Klasifikace v rámci standardů 3GPP pro entity pro správu mobility (MME) založená na jejich produktových schopnostech a kapacitě. Definuje výkonnostní měřítka a soubory funkcí, což umožňuje síťovým ope"
---

MME je třída síťového produktu podle 3GPP, která kategorizuje entity pro správu mobility (Mobility Management Entities) podle jejich výkonnostních měřítek, souborů funkcí a kapacity za účelem konzistentního hodnocení a pořizování operátory.

## Popis

[NPC](/mobilnisite/slovnik/npc/) MME (třída síťového produktu pro entitu pro správu mobility) je podrobná specifikace v rámci 3GPP, která kategorizuje implementace MME podle standardizované sady výkonnostních a schopnostních kritérií. Samotná MME je uzel jádra sítě v Evolved Packet Core (EPC) pro LTE a v 5G Core (5GC), kde se vyvinula ve funkci pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)). Rámec NPC se však zaměřuje na definici toho, co tvoří konkrétní 'třídu' produktu MME z hlediska jeho kapacity zvládat účastníky, relace, signalizační transakce a podporované funkce.

Z architektonického hlediska definice NPC nemění standardní rozhraní nebo protokoly MME, ale poskytují důkladnou metodologii testování a klasifikace. Třída MME je určena jejím výkonem proti měřítkům definovaným ve specifikacích jako TS 36.413 (S1-AP) a TS 29.272 (S6a). Mezi klíčové metriky patří maximální podporovaný počet připojených účastníků, pokusy o volání v hodině špičky (BHCA), připojení k paketové datové síti (PDN), aktualizace oblasti sledování (TAU) za sekundu a míry předávání hovoru. Klasifikace také vyžaduje podporu konkrétních funkcí 3GPP, jako jsou služby tísňového volání, zákonné odposlechy a různé procedury správy mobility a relací.

Jak to funguje: dodavatelé navrhují svůj hardware nebo software MME tak, aby cílově odpovídal konkrétní NPC (např. třídě s vysokou kapacitou). Poté provedou testy shody a zatížení, často s odkazem na testovací sady ve specifikacích jako TS 36.523, aby ověřili, že produkt splňuje všechny požadavky pro danou třídu. To poskytuje síťovým operátorům možnost přímého srovnání při vydávání výzev k podání nabídky (RFP). NPC zajišťuje, že MME inzerovaná jako určitá třída poskytne garantovanou úroveň výkonu a funkčnosti, což je klíčové pro dimenzování sítě, plánování kapacity a zajištění smluv o úrovni služeb (SLA). Její role je tedy standardizační a zajišťující kvalitu na trhu síťového vybavení, čímž zaručuje interoperabilitu a předvídatelný výkon napříč různými implementacemi dodavatelů.

## K čemu slouží

Účelem definování tříd síťových produktů ([NPC](/mobilnisite/slovnik/npc/)) pro MME bylo přinést do procesu pořizování telekomunikačního vybavení jasnost, spravedlnost a spolehlivost. Před takovou klasifikací mohli dodavatelé používat proprietární nebo nestandardní metriky k popisu kapacity svých uzlů MME, což operátorům ztěžovalo přímé srovnání. To vedlo k rizikům poddimenzování (pokud produkt nepodával očekávaný výkon) nebo neefektivních kapitálových výdajů (pokud byly pořizovány předimenzované produkty).

Vytvoření MME NPC, s kořeny v dřívější práci na třídách síťových produktů pro jiné uzly, bylo motivováno komerčním nasazením LTE (EPS) počínaje 3GPP Release 8. Jako zcela nové, plně IP jádro sítě potřebovali operátoři jistotu, že kritický signalizační uzel (MME) od jakéhokoli dodavatele zvládne předpokládaný růst počtu účastníků a signalizační zátěž. Rámec NPC to vyřešil poskytnutím společného jazyka a důkladné sady měřítek definovaných samotným standardizačním orgánem.

Řeší základní problém vázanosti na dodavatele a nejednoznačnosti výkonu. Standardizací výkonnostních tříd podporuje konkurenční prostředí s více dodavateli, protože operátoři mohou s jistotou v jejich vzájemném fungování a kapacitě kombinovat uzly od různých dodavatelů. Dále napomáhá vývoji sítí, protože definice NPC jsou aktualizovány napříč releasy, aby zahrnovaly nové funkce (např. podporu VoLTE, zařízení IoT, předchůdce síťového řezání), čímž zajišťují, že produktové klasifikace zůstávají relevantní pro současné požadavky služeb. Je to klíčový faktor pro předvídatelné škálování sítě a nákladově efektivní vývoj ze sítí 4G na 5G.

## Klíčové vlastnosti

- Standardizované metriky kapacity (např. připojení uživatelé, BHCA, souběžná připojení PDN)
- Definovaná výkonnostní měřítka pro signalizační procedury (Attach, TAU, Handover)
- Povinná podpora základní sady funkcí a protokolů 3GPP
- Úrovně klasifikace (např. malé, střední, velké nasazení) pro různé scénáře nasazení
- Odkaz na metodiky testování shody a zatížení pro ověření
- Vývoj definic tříd pro začlenění funkcí z nových releasů 3GPP

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.839** (Rel-12) — Fixed-Mobile Convergence Architecture Study
- **TS 23.857** (Rel-11) — EPC Node Failure & Restoration Study
- **TS 23.896** (Rel-12) — Policy & Charging Control for Fixed Broadband Convergence
- **TS 24.161** (Rel-19) — Network-Based IP Flow Mobility (NBIFOM)
- **TS 24.171** (Rel-19) — NAS Protocol for LCS in E-UTRAN
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- … a dalších 70 specifikací

---

📖 **Anglický originál a plná specifikace:** [MME na 3GPP Explorer](https://3gpp-explorer.com/glossary/mme/)
