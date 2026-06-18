---
slug: "dcqr"
url: "/mobilnisite/slovnik/dcqr/"
type: "slovnik"
title: "DCQR – Downlink Channel Quality Report"
date: 2025-01-01
abbr: "DCQR"
fullName: "Downlink Channel Quality Report"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dcqr/"
summary: "Mechanismus v LTE a 5G NR, při kterém UE hlásí síti měření kvality downlinkového kanálu. Umožňuje eNB/gNB provádět efektivní adaptaci spoje a plánování prostředků tím, že poskytuje zpětnou vazbu o rád"
---

DCQR je mechanismus v LTE a 5G NR, při kterém UE (uživatelské zařízení) hlásí síti měření kvality downlinkového kanálu, aby umožnil efektivní adaptaci spoje a plánování prostředků.

## Popis

Downlink Channel Quality Report (DCQR, zpráva o kvalitě downlinkového kanálu) je základní mechanismus zpětné vazby definovaný ve specifikacích 3GPP, primárně v rámci protokolu vrstvy Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) (TS 36.321). Funguje v rámci frameworku řídicí signalizace v uplinku, kde User Equipment (UE) periodicky nebo aperiodicky měří kvalitu downlinkového rádiového kanálu a předává tuto informaci obsluhující základnové stanici ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR). Zpráva typicky kvantifikuje kvalitu kanálu pomocí metrik jako Channel Quality Indicator ([CQI](/mobilnisite/slovnik/cqi/)), který představuje nejvyšší modulační a kódové schéma ([MCS](/mobilnisite/slovnik/mcs/)), které může UE při současných podmínkách kanálu podporovat s předdefinovanou mírou chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)). Toto měření je odvozeno z referenčních signálů, jako je Cell-Specific Reference Signal ([CRS](/mobilnisite/slovnik/crs/)) v LTE nebo Channel State Information Reference Signal ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) v 5G NR.

Architektura pro DCQR zahrnuje komponenty na straně UE i na straně sítě. Na straně UE fyzická vrstva provádí odhad a měření kanálu, které jsou následně zpracovány vyššími vrstvami za účelem generování indexu CQI mapovaného na předdefinovanou tabulku. Vrstva MAC zabalí toto CQI spolu s další potenciální zpětnou vazbou, jako je Precoding Matrix Indicator ([PMI](/mobilnisite/slovnik/pmi/)) a Rank Indicator (RI) pro MIMO operace, do MAC Control Element (CE) nebo využije pro přenos fyzické vrstvy uplinkových řídicích kanálů (např. PUCCH nebo PUSCH). Na straně sítě, konkrétně plánovač uvnitř eNB/gNB, tyto zprávy přijímá a interpretuje. Plánovač používá DCQR k dynamickému výběru vhodných parametrů přenosu pro downlink, včetně modulačního schématu (např. QPSK, 16QAM, 64QAM, 256QAM), kódové rychlosti, přidělení zdrojových bloků a MIMO precodingu. Tento proces, známý jako adaptace spoje, zajišťuje, že datové přenosy odpovídají okamžité kvalitě kanálu, maximalizují datové rychlosti za dobrých podmínek a zajišťují robustnost za špatných podmínek.

Role DCQR v síti je klíčová pro správu rádiových prostředků a poskytování Quality of Service (QoS). Tím, že poskytuje včasné a přesné informace o stavu kanálu (CSI), umožňuje síti optimalizovat spektrální účinnost a kapacitu buňky. Například ve scénářích s vysokou mobilitou nebo útlumem umožňují časté aktualizace DCQR plánovači rychle se přizpůsobit měnícím se podmínkám, čímž se zabrání nadměrným retransmisím a sníží se latence. Dále DCQR podporuje pokročilé funkce jako agregace nosných, kde mohou být poskytovány samostatné zprávy pro každou komponentní nosnou, a koordinované operace multipoint (CoMP), kde je uvažována kvalita kanálu z více vysílacích bodů. Hlášení může být konfigurováno sítí jako širokopásmové (pokrývající celou šířku pásma systému) nebo subpásmové (pro specifické frekvenční oddíly), což nabízí kompromis mezi režií hlášení a granularitou informací o kanálu.

## K čemu slouží

DCQR existuje, aby řešil základní výzvu časově proměnlivého a frekvenčně selektivního útlumu v bezdrátových kanálech, který vážně ovlivňuje spolehlivost a účinnost downlinkového přenosu. Bez přesné zpětné vazby o kvalitě kanálu by síť musela používat konzervativní, pevná modulační a kódová schémata, což by vedlo k nevyužití šířky pásma za dobrých podmínek nebo k vysokým chybovostem za špatných podmínek. Primární problém, který řeší, je umožnění adaptivní modulace a kódování (AMC), což je klíčová technika v moderních buněčných systémech (od HSPA dále), která dynamicky upravuje parametry přenosu na základě podmínek kanálu v reálném čase. To maximalizuje propustnost a spektrální účinnost při zachování cílové míry chybovosti, což je nezbytné pro podporu různorodých služeb s různými požadavky na QoS, od hlasových hovorů po vysokorychlostní data.

Historicky dřívější buněčné systémy jako GSM používaly pevná kódová schémata, která byla neefektivní. Zavedení hlášení kvality kanálu ve standardech 3GPP, vyvíjející se z CQI v HSDPA (3G) k sofistikovanějším mechanismům DCQR v LTE a 5G NR, bylo motivováno potřebou vyšších datových rychlostí a lepšího využití prostředků v systémech založených na OFDMA. V LTE a NR se kvalita kanálu může výrazně měnit napříč frekvenčními subnosnými a v čase kvůli vícecestnému šíření a interferenci. DCQR poskytuje nezbytnou zpětnou vazbu k využití těchto variací prostřednictvím frekvenčně selektivního plánování, kdy jsou prostředky přidělovány UE na jejich nejlepší subpásma. Tím se řeší omezení slepých nebo polostatických přístupů k plánování, které se nemohou rychle přizpůsobit dynamice kanálu, čímž se zlepšuje výkon na okraji buňky a celková kapacita systému.

## Klíčové vlastnosti

- Umožňuje dynamickou adaptaci spoje hlášením Channel Quality Indicator (CQI)
- Podporuje jak periodické, tak aperiodické hlášení spouštěné sítí
- Usnadňuje frekvenčně selektivní plánování prostřednictvím subpásmových CQI zpráv
- Integruje se s MIMO operacemi volitelným zahrnutím zpětné vazby PMI a RI
- Pro uplinkový přenos využívá MAC Control Elements nebo kanály fyzické vrstvy
- Konfigurovatelná granularita hlášení (širokopásmová nebo subpásmová) pro vyvážení režie a přesnosti

## Související pojmy

- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)
- [PMI – Precoding Matrix Indicator](/mobilnisite/slovnik/pmi/)

## Definující specifikace

- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [DCQR na 3GPP Explorer](https://3gpp-explorer.com/glossary/dcqr/)
