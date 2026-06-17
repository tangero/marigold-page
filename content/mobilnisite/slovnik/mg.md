---
slug: "mg"
url: "/mobilnisite/slovnik/mg/"
type: "slovnik"
title: "MG – Measurement Gap"
date: 2025-01-01
abbr: "MG"
fullName: "Measurement Gap"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mg/"
summary: "Nakonfigurované období, během kterého uživatelské zařízení (UE) dočasně přeruší komunikaci s obsluhující buňkou, aby provedlo rádiová měření na jiných kmitočtech nebo technologiích rádiového přístupu"
---

MG (Measurement Gap) je nakonfigurované období, během kterého UE přeruší komunikaci s obsluhující buňkou za účelem provádění rádiových měření na jiných kmitočtech nebo RAT; je nezbytný pro mobilní procedury, jako je předávání spojení (handover).

## Popis

Measurement Gap (MG) je klíčový mechanismus správy mobility v 3GPP sítích, který umožňuje uživatelskému zařízení (UE) zapojenému v aktivním spojení (např. ve stavu [RRC](/mobilnisite/slovnik/rrc/)_CONNECTED) přeladit svůj rádiový přijímač z kmitočtu obsluhující buňky za účelem provedení mezifrekvenčních nebo mezitechnologických (inter-RAT) měření. Během předkonfigurovaného MG síť (např. [eNB](/mobilnisite/slovnik/enb/) v LTE nebo gNB v NR) nenaplánuje žádné přenosy směrem k UE ani od ní, čímž zajišťuje, že UE nepřijde o žádná data. UE toto klidové období využívá k naslouchání a měření kvality signálu (např. RSRP, RSRQ) sousedních buněk na různých kmitočtech nosných nebo různých RAT (např. měření LTE při připojení k NR, nebo GSM/WCDMA při připojení k LTE).

Z architektonického hlediska je Measurement Gap konfigurován sítí prostřednictvím signalizace RRC (Radio Resource Control). Mezi klíčové parametry patří vzor gapu (např. perioda opakování gapu a délka trvání gapu), které jsou standardizovány. Jsou definovány běžné vzory, jako je gap pattern #0 s periodou 40 ms a délkou trvání 6 ms, které poskytují rovnováhu mezi možností měření a přerušením datového toku. Konfigurace je odeslána ve zprávě RRCConnectionReconfiguration (nebo ekvivalentní) a zahrnuje offset gapu, který definuje, kdy nastane první gap. Plánovač sítě je tohoto vzoru vědom a vyhýbá se alokaci zdrojů pro UE během těchto oken gapů. Tato koordinace je klíčová pro zachování integrity aktivní datové relace, zatímco UE může shromažďovat potřebné informace pro případná předání spojení (handover).

Fungování zahrnuje přesné časování. Jakmile je konfigurován, UE samostatně aktivuje své gapy podle daného vzoru. Během každého gapu přeladí svůj lokální oscilátor a přijímací řetězec na cílový kmitočet, provede požadovaná měření (což může zahrnovat synchronizaci s referenčními signály nové buňky) a poté přeladí zpět na kmitočet obsluhující buňky před skončením gapu. Naměřené výsledky jsou následně nahlášeny síti ve zprávě measurement report. Síť tyto reporty využívá pro rozhodování o předání spojení. Ve složitých scénářích, jako je [EN-DC](/mobilnisite/slovnik/en-dc/) (E-UTRA-NR Dual Connectivity), se konfigurace gapů stává komplexnější, protože UE může potřebovat provádět měření pro hlavní uzel ([MN](/mobilnisite/slovnik/mn/)) nebo sekundární uzel (SN), a jsou definovány mechanismy sdílení gapů pro optimalizaci efektivity měření.

## K čemu slouží

Measurement Gapy byly zavedeny k řešení problému správy rádiových zdrojů pro UE, která jsou schopna pracovat na více kmitočtech nebo s více RAT, ale typicky disponují pouze jedním řetězcem rádiového přijímače. V raných mobilních systémech mohlo UE operovat pouze na jednom kmitočtu v daném čase. Se zavedením více pásmových telefonů a schopností práce s více RAT (2G/3G/4G) potřebovali operátoři způsob, jak může UE objevovat a měřit kvalitu alternativních buněk bez přerušení probíhajícího hovoru nebo datové relace. MG poskytuje plánované, předvídatelné přerušení, kolem kterého se síť může organizovat, což umožňuje plynulou mobilitu.

Tento koncept se stal stále kritičtějším s nasazením heterogenních sítí (HetNets), agregace nosných ([CA](/mobilnisite/slovnik/ca/)) a později nasazením 5G NR v nestandalonovém (NSA) i standalone (SA) režimu. Bez MG by UE v husté síti s vrstvami makrobuněk, malých buněk a různých RAT nebylo schopno shromáždit informace potřebné pro to, aby síť mohla provést optimální předání spojení, což by vedlo k přerušeným hovorům, špatnému uživatelskému zážitku a neefektivnímu využití síťových zdrojů. MG standardizují proces měření a zajišťují interoperabilitu mezi UE a síťovým vybavením od různých výrobců.

## Klíčové vlastnosti

- Umožňuje mezifrekvenční a mezitechnologická (inter-RAT) měření pro UE s jedním přijímačem.
- Dynamicky konfigurováno sítí prostřednictvím RRC signalizace na základě potřeb nasazení.
- Používá standardizované vzory gapů (např. délka trvání 6 ms, perioda 40/80/160 ms) pro vyvážení poměru měření a datového toku.
- Plánovač sítě je na gapy citlivý a vyhýbá se plánování přenosů pro UE během oken gapů.
- Nezbytný pro rozhodování o předání spojení (handover) v nasazeních s více vrstvami buněk a více RAT.
- Podporuje požadavky na přesnost měření a reportování definované ve specifikacích výkonu (např. 38.133).

## Definující specifikace

- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility

---

📖 **Anglický originál a plná specifikace:** [MG na 3GPP Explorer](https://3gpp-explorer.com/glossary/mg/)
