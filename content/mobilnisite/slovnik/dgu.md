---
slug: "dgu"
url: "/mobilnisite/slovnik/dgu/"
type: "slovnik"
title: "DGU – Digital Gathering Unit"
date: 2025-01-01
abbr: "DGU"
fullName: "Digital Gathering Unit"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/dgu/"
summary: "Síťová komponenta správy, která sbírá, agreguje a zpracovává data o výkonu z různých síťových prvků. Umožňuje centralizovaný sběr dat pro analýzu, optimalizaci a zajištění kvality služeb v sítích 3GPP"
---

DGU je síťová komponenta správy, která sbírá, agreguje a zpracovává data o výkonu z různých síťových prvků pro centralizovanou analýzu a zajištění kvality služeb v sítích 3GPP.

## Popis

Digital Gathering Unit (DGU) je standardizovaná funkce síťového managementu definovaná ve specifikacích 3GPP pro sběr a zpracování dat o výkonu (PM). Funguje v rámci řídicí roviny, typicky jako součást funkce Network Data Analytics Function (NWDAF) nebo specializovaného systému pro sběr dat. DGU komunikuje přes standardizovaná rozhraní s různými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) a síťovými prvky ([NE](/mobilnisite/slovnik/ne/)) napříč systémem 5G – včetně jádra sítě (5GC), rádiové přístupové sítě (NG-RAN) a potenciálně i uživatelských zařízení (UE) – za účelem sběru nezpracovaných dat o výkonu. Jejím hlavním úkolem je sloužit jako centralizovaný bod agregace dat, který normalizuje heterogenní datové toky do konzistentního formátu vhodného pro následnou analýzu, reportování a optimalizaci sítě.

Z architektonického hlediska je DGU definována v rámci frameworku 3GPP Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)), konkrétně v doménách Network Management ([NM](/mobilnisite/slovnik/nm/)) a Element Management ([EM](/mobilnisite/slovnik/em/)). Implementuje severovýchodní rozhraní Itf-N (dle specifikace TS 28.622) pro komunikaci s vyššími systémy správy, jako je Network Manager (NM) nebo Operations Support System ([OSS](/mobilnisite/slovnik/oss/)). Na jihozápadní straně využívá standardizovaná rozhraní pro připojení k síťovým funkcím (NF) a síťovým prvkům (NE) a sbírá data pomocí protokolů jako File Transfer Protocol ([FTP](/mobilnisite/slovnik/ftp/)), Hypertext Transfer Protocol ([HTTP](/mobilnisite/slovnik/http/)) nebo specializovaných protokolů pro streamování. Vnitřní zpracování v DGU zahrnuje validaci dat, zarovnání časových značek, agregaci (např. sčítání čítačů, výpočet průměrů za časová okna) a formátování podle datových modelů pro PM dle 3GPP (např. TS 28.552).

Klíčové součásti implementace DGU zahrnují engine pro sběr dat, který zajišťuje komunikaci s datovými zdroji specifickou pro daný protokol; jednotku pro zpracování dat, která provádí agregaci, filtrování a normalizaci; správce úložiště pro dočasné ukládání nezpracovaných a zpracovaných dat; a obslužný modul rozhraní pro severovýchodní komunikaci. DGU hraje klíčovou roli v umožnění datově řízených síťových operací tím, že poskytuje čistá, agregovaná PM data analytickým funkcím. To podporuje případy užití, jako je monitorování výkonu sítě, detekce chyb, plánování kapacity a automatizovaná optimalizace. Centralizací a standardizací sběru dat DGU snižuje složitost pro jednotlivé síťové funkce a zajišťuje konzistenci dat používaných pro celosíťovou analýzu a rozhodování.

## K čemu slouží

DGU byla vytvořena, aby řešila výzvy spojené se sběrem a správou dat o výkonu v stále složitějších a heterogenních sítích 5G. Před její standardizací se operátoři spoléhali na proprietární nebo dodavatelsky specifické systémy sběru dat, což vedlo k fragmentovaným datovým formátům, nekonzistentním intervalům sběru a složitým integračním snahám. To ztěžovalo provádění komplexní síťové analýzy, korelaci problémů s výkonem napříč doménami a implementaci automatizované optimalizace ve velkém měřítku. DGU poskytuje standardizovaný přístup ke sběru PM dat, který umožňuje interoperabilitu mezi více dodavateli a zjednodušuje datové toky pro analytické funkce.

Historicky, jak se sítě vyvíjely ze 4G na 5G se zavedením síťových řezů, edge computingu a massive IoT, objem a různorodost dat o výkonu exponenciálně rostly. Tradiční metody sběru nedokázaly efektivně zvládnout toto měřítko ani poskytnout přístup k datům s nízkou latencí potřebnou pro analýzu v reálném čase. Specifikace DGU ve verzi 15 (Release 15) byla motivována potřebou škálovatelného, standardizovaného rámce pro sběr dat, který by mohl podporovat pokročilou analýzu vyžadovanou pro automatizaci sítí 5G, včetně operací v uzavřené smyčce a optimalizace založené na AI/ML.

DGU řeší několik konkrétních problémů: odstraňuje datové sila poskytnutím centralizovaného sběrného bodu, snižuje síťovou zátěž inteligentní agregací, zajišťuje konzistenci dat pomocí standardizovaných formátů a umožňuje dostupnost dat v reálném čase pro analytické funkce. Tím, že řeší tato omezení, DGU usnadňuje implementaci sofistikovaných aplikací pro správu sítě, které jsou závislé na komplexních, kvalitních datech o výkonu z celé síťové infrastruktury.

## Klíčové vlastnosti

- Standardizovaný sběr dat o výkonu z více síťových domén
- Schopnosti agregace a zpracování dat (filtrování, normalizace, zarovnání časových značek)
- Podpora více protokolů pro sběr (FTP, HTTP, streamování)
- Integrace s rozhraními správy 3GPP (Itf-N) pro severovýchodní komunikaci
- Škálovatelná architektura podporující příjem dat ve vysokém objemu
- Dočasné ukládání dat do bufferu a správa úložiště

## Definující specifikace

- **TS 28.304** (Rel-19) — PEE Parameters Control & Monitoring Requirements
- **TS 28.305** (Rel-19) — PEE Control & Monitoring IRP Information Service
- **TR 32.972** (Rel-19) — Energy Efficiency Study for 5G Networks

---

📖 **Anglický originál a plná specifikace:** [DGU na 3GPP Explorer](https://3gpp-explorer.com/glossary/dgu/)
