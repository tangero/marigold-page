---
slug: "roc"
url: "/mobilnisite/slovnik/roc/"
type: "slovnik"
title: "ROC – Roll-Over Counter"
date: 2025-01-01
abbr: "ROC"
fullName: "Roll-Over Counter"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/roc/"
summary: "Bezpečnostní čítač používaný v sítích 3GPP k zabránění replay útoků na šifrovaná data. Jeho hodnota se zvyšuje s každou novou šifrovací relací nebo datovým paketem, čímž zajišťuje kryptografickou svěž"
---

ROC je bezpečnostní čítač v sítích 3GPP, jehož hodnota se zvyšuje, aby zabránil replay útokům a zajistil kryptografickou svěžest pro šifrovaný uživatelský a signalizační provoz.

## Popis

Čítač přetečení (Roll-Over Counter, ROC) je základní bezpečnostní parametr v mechanismech ochrany důvěrnosti a integrity 3GPP, konkrétně používaný s algoritmy 128-EEA1 a 128-EIA1 založenými na šifře SNOW 3G. Jde o 32bitový čítač, který spolupracuje s 16bitovým sekvenčním číslem (Sequence Number, [SQN](/mobilnisite/slovnik/sqn/)) za vzniku 48bitového parametru COUNT. COUNT je hlavním vstupem pro generování kryptografického keystreamu v algoritmech EPS Encryption Algorithm ([EEA](/mobilnisite/slovnik/eea/)) a EPS Integrity Algorithm ([EIA](/mobilnisite/slovnik/eia/)). ROC je udržován samostatně pro směr uplink a downlink pro každé rádiové přenosové médium a spravuje jej síť i UE. Jeho primární úlohou je poskytovat vysoce řádovou monotónně rostoucí hodnotu, která zajišťuje, že se keystream po dlouhou dobu neopakuje, což je zásadní pro prevenci opakovaného použití keystreamu a následných kryptografických útoků.

Architektonicky je ROC uložen v bezpečnostním kontextu přístupové vrstvy v UE a v síti. Pro uplink UE zvýší hodnotu ROC, když se 16bitové SQN přetočí (tj. zacyklí z hodnoty 65535 na 0). Příjemce na síťové straně využívá přijaté SQN a lokálně udržované ROC ke zrekonstruování úplného COUNT pro dešifrování a ověření integrity. Kritickým procesem je kontrola synchronizace ROC; pokud síť přijme paket s SQN, které je výrazně nižší než očekávané (což naznačuje možný replay útok), může aktivovat příkaz security mode pro opětovnou synchronizaci nebo obnovení zabezpečení. Správa ROC je podrobně popsána v dokumentu 3GPP TS 33.246, který specifikuje zabezpečení služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), kde je manipulace s ROC klíčová pro správu klíčů vysílacích služeb.

Za provozu je hodnota ROC implicitně komunikována prostřednictvím SQN na rádiovém rozhraní, neboť v hlavičce paketu (např. v hlavičce [PDCP](/mobilnisite/slovnik/pdcp/) pro LTE/NR) je přenášeno pouze SQN. Toto řešení optimalizuje režii. Bezpečnost celého systému závisí na nevratnosti a monotónním růstu COUNT. Pokud by s ROC bylo nakládáno nesprávně – například pokud by byl nepatřičně resetován – mohlo by to vést k opětovnému použití stejného keystreamu s různým otevřeným textem, což by narušilo důvěrnost. Proto procesy pro předávání spojení, obnovení spojení a změnu přenosového média obsahují specifická pravidla pro údržbu ROC, aby byla zajištěna kontinuální bezpečnost. V MBMS je ROC také používán v souvislosti s životním cyklem MBMS Service Key ([MSK](/mobilnisite/slovnik/msk/)) a MBMS Traffic Key ([MTK](/mobilnisite/slovnik/mtk/)) k identifikaci generací klíčů a prevenci opakovaného přehrávání vysílaného obsahu.

## K čemu slouží

ROC byl zaveden, aby řešil omezení používání pouze krátkého sekvenčního čísla pro kryptografickou synchronizaci v mobilních sítích. Rané šifrovací schémata riskovala opakování keystreamu, pokud by se prostor sekvenčních čísel vyčerpal v rámci jediného bezpečnostního kontextu, což by mohlo vést k úspěšným kryptanalytickým útokům. ROC dramaticky rozšiřuje efektivní prostor čítače a zajišťuje, že kombinovaný COUNT (ROC || [SQN](/mobilnisite/slovnik/sqn/)) je dostatečně velký (48 bitů), aby se v praxi během životnosti kryptografického klíče nikdy neopakoval. To je klíčové pro dlouhodobou bezpečnost spojení, zejména u služeb s vysokou přenosovou rychlostí, kde se sekvenční čísla paketů zvyšují rychle.

Jeho vytvoření bylo motivováno potřebou robustní, dlouhodobé ochrany důvěrnosti a integrity v systémech 3GPP počínaje zavedením silnějších algoritmů ve verzi 8 pro LTE. Algoritmy založené na SNOW 3G vyžadovaly spolehlivou metodu pro generování unikátního keystreamu pro každý paket. Mechanismus ROC to zajišťuje tím, že funguje jako vysoce řádový epochový čítač. Řeší problém potenciálních replay útoků, kdy by útočník mohl znovu vložit dříve zachycené pakety; příjemce může takové opakované přehrání detekovat kontrolou rekonstruovaného COUNT vůči očekávanému oknu. ROC je jádrovou součástí plnění bezpečnostních požadavků 3GPP na dopřednou bezpečnost a odolnost proti replay útokům, které jsou základními pro ochranu soukromí uživatelů a integritu sítě.

## Klíčové vlastnosti

- 32bitový čítač rozšiřující 16bitové sekvenční číslo (SQN) do 48bitového COUNT
- Nezbytný vstup pro šifrovací (EEA1) a integritní (EIA1) algoritmy založené na SNOW 3G
- Udržován samostatně pro směr uplink a downlink pro každé rádiové přenosové médium
- Implicitně synchronizován mezi UE a sítí prostřednictvím přenášeného SQN
- Zvyšuje svou hodnotu při přetečení SQN, aby udržel monotónní nárůst
- Kritický pro prevenci opakovaného použití keystreamu a replay útoků

## Související pojmy

- [COUNT-C – Ciphering Sequence Number for Core Network](/mobilnisite/slovnik/count-c/)
- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [SQN – Sequence Number](/mobilnisite/slovnik/sqn/)

## Definující specifikace

- **TS 33.246** (Rel-19) — MBMS Security Specification

---

📖 **Anglický originál a plná specifikace:** [ROC na 3GPP Explorer](https://3gpp-explorer.com/glossary/roc/)
