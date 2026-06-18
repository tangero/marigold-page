---
slug: "utran"
url: "/mobilnisite/slovnik/utran/"
type: "slovnik"
title: "UTRAN – Universal Terrestrial Radio Access Network"
date: 2025-01-01
abbr: "UTRAN"
fullName: "Universal Terrestrial Radio Access Network"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/utran/"
summary: "Architektura rádiové přístupové sítě pro 3G UMTS, skládající se z základnových stanic Node B a radiových síťových řadičů (RNC). Je zodpovědná za všechny funkce související s rádiovým přístupem, včetně"
---

UTRAN je Universal Terrestrial Radio Access Network pro 3G UMTS, který se skládá z Node B a RNC a zajišťuje všechny funkce související s rádiovým přístupem a propojuje uživatelské zařízení s jádrovou sítí.

## Popis

Universal Terrestrial Radio Access Network (UTRAN) je souhrnný termín pro síťovou infrastrukturu, která poskytuje rádiové přístupové schopnosti pro uživatelská zařízení (UE) v síti 3G UMTS. Je to jeden z klíčových podsystémů definovaných 3GPP, vedle jádrové sítě (CN) a uživatelského zařízení (UE). Hlavními komponentami UTRAN jsou Node B (základnová stanice) a Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)). Tyto prvky spolupracují na správě rádiového rozhraní ([UTRA](/mobilnisite/slovnik/utra/)) a usnadňují připojení mobilních uživatelů ke službám jádrové sítě.

Z architektonického hlediska je UTRAN strukturován kolem konceptu řídicích bodů. RNC je řídicí síťový prvek pro jeden nebo více Node B. Hostuje kritickou vrstvu protokolu Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a je zodpovědný za centralizovaná rozhodnutí správy rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)), včetně řízení přístupu, plánování paketů, řízení předávání hovorů a nastavení řízení výkonu. Node B je zodpovědný za zpracování fyzické vrstvy rozhraní UTRA: modulaci/demodulaci, kódování/dekódování, rozprostření/despreading a vysílání/příjem rádiových signálů prostřednictvím svých buněk. Rozhraní mezi RNC a Node B se nazývá rozhraní Iub, které je otevřené a standardizované, aby umožnilo interoperabilitu mezi různými dodavateli. Pro komunikaci mezi RNC (např. při předávání mezi RNC) se používá rozhraní Iur. Celý UTRAN se připojuje k jádrové síti prostřednictvím rozhraní Iu, které je logicky rozděleno na Iu-CS pro okruhově přepínané domény ([MSC](/mobilnisite/slovnik/msc/)) a Iu-PS pro paketově přepínané domény ([SGSN](/mobilnisite/slovnik/sgsn/)).

UTRAN funguje tak, že mezi UE a CN vytváří a udržuje rádiové přístupové přenosové cesty ([RAB](/mobilnisite/slovnik/rab/)). Když chce UE komunikovat, RNC na žádost CN nastaví potřebné rádiové prostředky napříč zapojenými Node B a nakonfiguruje RRC spojení UE. Spravuje mobilitu pomocí procedur, jako je výběr/převýběr buňky, měkké předání (charakteristický rys [WCDMA](/mobilnisite/slovnik/wcdma/), kdy je UE připojeno k více buňkám současně) a tvrdé předání. UTRAN také zajišťuje bezpečnostní funkce, jako je šifrování a ochrana integrity na rádiovém rozhraní. Jeho úlohou je abstrahovat složitost rádiového spoje od jádrové sítě a poskytovat jí spolehlivou přenosovou službu pro uživatelská data a signalizaci, přičemž efektivně využívá omezené rádiové spektrum pomocí pokročilých technik RRM.

## K čemu slouží

UTRAN byl vytvořen, aby poskytl síťovou architekturu nezbytnou pro realizaci schopností nového rádiového rozhraní UTRA pro 3G UMTS. Jeho účelem bylo překročit jednodušší subsystém základnových stanic (BSS) 2G GSM, který se skládal z přenosových stanic BTS a řadičů základnových stanic (BSC). Nová architektura byla potřebná k podpoře složitější správy rádiových prostředků vyžadované technologií WCDMA, jako je měkké předání a rychlé řízení výkonu, a k umožnění vyšších přenosových rychlostí a nových paketově přepínaných služeb.

Řešil několik klíčových problémů předchozích architektur. Oddělení řídicí inteligence (RNC) od jednotky pro rádiový přenos/příjem (Node B) umožnilo centralizovanější a efektivnější správu prostředků napříč více buňkami. Zavedení otevřených rozhraní Iub a Iur podpořilo konkurenci dodavatelů a flexibilitu při nasazování sítí. Nejvýznamnější je, že UTRAN byl navržen tak, aby současně podporoval jak tradiční okruhově přepínané hlasové služby, tak nové paketově přepínané datové služby s odpovídajícím řízením kvality služeb (QoS), což byl základní požadavek pro 3G vizi multimediální komunikace.

Historický kontext představuje vývoj od GSM. Zatímco BSS GSM bylo optimalizováno pro hlas, UTRAN byl koncipován koncem 90. let jako součást iniciativy IMT-2000 k vytvoření sítě schopné přenášet širokopásmová data. Poskytl základní rámec, který umožnil operátorům globálně nasazovat sítě UMTS. Architektura UTRAN se osvědčila jako robustní a rozšiřitelná, podporovala zásadní evoluční upgrady, jako je High-Speed Packet Access (HSPA), bez zásadních změn. Po více než desetiletí sloužila jako dominantní 3G RAN a vytvořila kritický most mezi 2G a plošší, plně IP architekturou 4G LTE (E-UTRAN).

## Klíčové vlastnosti

- Dvouuzlová architektura skládající se z Node B (základnová stanice) a Radio Network Controller (RNC)
- Otevřená, standardizovaná rozhraní: Iub (RNC-Node B), Iur (RNC-RNC) a Iu (RNC-jádrová síť)
- Centralizovaná správa rádiových prostředků (RRM) prováděná RNC
- Nativní podpora měkkého předání a měkčího předání (vlastnost WCDMA)
- Současná správa okruhově přepínaných (CS) a paketově přepínaných (PS) přenosových cest
- Zodpovědnost za šifrování a ochranu integrity na rádiovém rozhraní

## Související pojmy

- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [UTRA – Universal Terrestrial Radio Access](/mobilnisite/slovnik/utra/)

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.100** (Rel-4) — UMTS Service Requirements Phase 1
- **TS 22.240** (Rel-19) — 3GPP Generic User Profile Requirements
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.034** (Rel-19) — HSCSD Stage 2 Service Description
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- … a dalších 175 specifikací

---

📖 **Anglický originál a plná specifikace:** [UTRAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/utran/)
