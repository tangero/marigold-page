---
slug: "sib"
url: "/mobilnisite/slovnik/sib/"
type: "slovnik"
title: "SIB – System Information Block"
date: 2026-01-01
abbr: "SIB"
fullName: "System Information Block"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sib/"
summary: "Bloky systémových informací (SIB) jsou vysílací zprávy šířené sítí, které poskytují základní konfigurační a provozní parametry všem uživatelským zařízením (UE) v buňce. Obsahují klíčové informace pro"
---

SIB je vysílací zpráva obsahující základní konfigurační a provozní parametry (např. pro výběr buňky a řízení přístupu), která umožňuje uživatelským zařízením (UE) připojit se k mobilní síti a komunikovat s ní.

## Popis

Bloky systémových informací (SIB) jsou základním prvkem rozhraní buněčného rádiového přístupu, definovaným ve vrstvě protokolu řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)). Pravidelně je vysílá stanice gNB v 5G NR nebo [eNB](/mobilnisite/slovnik/enb/) v 4G LTE přes vysílací řídicí kanál ([BCCH](/mobilnisite/slovnik/bcch/)). Systémové informace jsou logicky strukturovány do hlavního bloku informací ([MIB](/mobilnisite/slovnik/mib/)) a více SIBů, z nichž každý je identifikován typovým číslem (např. [SIB1](/mobilnisite/slovnik/sib1/), SIB2). MIB obsahuje nejkritičtější parametry pro počáteční přístup k buňce, jako je šířka pásma systému a číslo systémového rámce, a přímo nařizuje vysílání SIB1. SIB1 následně poskytuje informace související s přístupem k buňce a plánovací informace pro ostatní SIBy.

Vysílání SIBů se řídí specifickým plánem definovaným parametry periodicita a délka okna, což zajišťuje, že UE vědí, kdy mají naslouchat. SIBy se obvykle vysílají pomocí robustního modulačního a kódovacího schématu, aby bylo zajištěno spolehlivé přijetí i na okraji buňky. Obsah každého typu SIB je standardizován a zahrnuje parametry pro výběr a převýběr buňky (např. minimální požadovaná úroveň příjmu, priority převýběru buňky), konfiguraci náhodného přístupu, konfigurace společných kanálů, seznamy sousedních buněk a identitu veřejné pozemní mobilní sítě ([PLMN](/mobilnisite/slovnik/plmn/)). V 5G také SIBy přenášejí informace pro síťové segmentování (network slicing), blokování přístupu a další pokročilé funkce.

Procedura UE zahrnuje nejprve získání MIB a SIB1 po synchronizaci s buňkou. Na základě plánovacích informací v SIB1 pak UE získá další potřebné SIBy. UE si musí tyto systémové informace uložit a znovu je získat při oznámení změny (prostřednictvím pagingu nebo přímé indikace v 5G) nebo při vstupu do nové buňky. Architektura je decentralizovaná, přičemž každá buňka vysílá svou vlastní sadu SIBů. Tento vysílací mechanismus je klíčový pro efektivitu sítě, neboť se vyhýbá nutnosti vyhrazené signalizace pro každé UE pro společná konfigurační data, čímž šetří rádiové prostředky a umožňuje rychlý výběr buňky a vstup do sítě.

## K čemu slouží

Hlavním účelem SIBů je poskytnout standardizovaný a efektivní vysílací mechanismus pro doručování základních a společných konfiguračních informací sítě všem uživatelským zařízením v pokrytí buňky. Než může UE navázat vyhrazené spojení pro datové nebo hlasové služby, musí nejprve porozumět tomu, jak komunikovat se sítí – to zahrnuje znalost toho, jak k síti přistupovat, jaké prostředky jsou k dispozici a jaká jsou pravidla provozu. SIBy tento problém řeší tím, že tyto povinné informace konsolidují do naplánovaných, periodicky vysílaných bloků.

Historicky, jak se buněčné sítě vyvíjely od 2G GSM přes 3G UMTS dále, množství a složitost systémových informací výrazně vzrostly. Rané systémy měly jednodušší vysílací struktury, ale zavedení paketových služeb, více kmitočtových pásem, agregace nosných a složitých scénářů mobility si vyžádalo strukturovanější a rozšiřitelnější přístup. Rámec SIB, formalizovaný v 3GPP, tuto strukturu poskytuje. Umožňuje kategorizaci informací (různé typy SIB pro různé účely) a jasný plánovací mechanismus, který je efektivnější než vysílání všech informací v jednom velkém, zřídka přenášeném bloku.

Tento přístup řeší klíčová omezení: minimalizuje spotřebu energie UE tím, že umožňuje UE spát a probouzet se pouze pro naplánované přenosy SIBů, zajišťuje spolehlivé získání prostřednictvím opakování a robustního kódování a poskytuje škálovatelný rámec pro zavádění nových parametrů pro nové funkce v pozdějších vydáních 3GPP bez narušení zpětné kompatibility. Bez SIBů by každé UE vyžadovalo rozsáhlou vyhrazenou signalizaci pro počáteční nastavení, což by vytvořilo obrovskou signalizační režii a oddálilo vstup do sítě, zejména v prostředích s vysokou hustotou UE.

## Klíčové vlastnosti

- Vysílací přenos na logickém kanálu BCCH
- Strukturováno do více typů (SIB1, SIB2 atd.) pro organizované doručování informací
- Naplánovaný přenos s definovanou periodicitou a časovými okny
- Obsahuje parametry pro výběr buňky, převýběr a řízení přístupu
- Poskytuje společné konfigurace fyzické vrstvy a kanálů
- Zahrnuje informace o sousedních buňkách pro mobilitu

## Související pojmy

- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)
- [SIB1 – System Information Block Type 1](/mobilnisite/slovnik/sib1/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [SIB na 3GPP Explorer](https://3gpp-explorer.com/glossary/sib/)
