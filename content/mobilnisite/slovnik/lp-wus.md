---
slug: "lp-wus"
url: "/mobilnisite/slovnik/lp-wus/"
type: "slovnik"
title: "LP-WUS – Low Power Wake Up Signal"
date: 2025-01-01
abbr: "LP-WUS"
fullName: "Low Power Wake Up Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lp-wus/"
summary: "Signál fyzické vrstvy vysílaný gNB za účelem aktivace hlavního přijímače uživatelského zařízení (UE) prostřednictvím jeho LP-WUR. Zavedený v 3GPP Release 18 využívá jednoduchou modulaci pro minimaliza"
---

LP-WUS je signál fyzické vrstvy zavedený v Release 18, který gNB vysílá, aby prostřednictvím přijímače s nízkou spotřebou (low-power wake-up receiver) aktivoval hlavní přijímač uživatelského zařízení (UE). Používá jednoduchou modulaci, aby šetřil životnost baterie v zařízeních IoT a RedCap.

## Popis

Low Power Wake Up Signal (LP-WUS) je signál fyzické vrstvy definovaný v 3GPP Release 18 pro New Radio (NR), navržený tak, aby jej s minimální energetickou náročností detekoval přijímač pro nízkopříkonové buzení ([LP-WUR](/mobilnisite/slovnik/lp-wur/)) uživatelského zařízení (UE). Vysílá jej gNB, aby upozornil konkrétní UE nebo skupiny UE na nutnost aktivace jejich hlavních rádiových transceiverů pro následnou komunikaci, jako je stránkování, přenos dat nebo aktualizace sítě. LP-WUS používá jednoduché modulační schémata, například klíčování zapnutí/vypnutí (on-off keying) nebo binární fázovou modulaci (binary phase-shift keying) při nízkých přenosových rychlostech, aby zajistil spolehlivou detekci nízkonákladovým obvodem LP-WUR. Signál nese základní informace, jako je identita UE nebo skupinové ID, což umožňuje cílené buzení bez falešných aktivací, a je konfigurován pomocí síťových parametrů pro optimalizaci úspor energie a latence.

Z architektonického hlediska je LP-WUS integrován do rámce fyzické vrstvy NR a je specifikován v několika dokumentech 3GPP včetně TS 38.211 pro fyzické kanály a TS 38.331 pro protokoly [RRC](/mobilnisite/slovnik/rrc/). Funguje v časové a frekvenční doméně, často je mapován na specifické zdrojové elementy v rámci okamžiku signálu buzení (wake-up signal occasion), který je gNB plánován periodicky nebo na vyžádání. Mezi klíčové komponenty patří generování sekvence pro odolnost signálu, řízení výkonu pro optimalizaci pokrytí a signalizační mechanismy pro konfiguraci specifickou pro UE. gNB rozhoduje o vysílání LP-WUS na základě faktorů, jako jsou čekající downlinková data, cykly stránkování nebo procedury iniciované sítí, a koordinuje jej s dalšími funkcemi pro nízkou spotřebu, jako je [LP-SS](/mobilnisite/slovnik/lp-ss/), pro synchronizované operace. Na straně UE přijímač LP-WUR nepřetržitě monitoruje přítomnost LP-WUS, k jeho identifikaci používá korelační techniky a po úspěšné detekci vyvolá přerušení (wake-up interrupt) pro hlavní přijímač.

Během provozu LP-WUS umožňuje efektivní proceduru buzení: když gNB potřebuje komunikovat s nečinným (dormant) UE, vysílá LP-WUS přizpůsobený konfiguraci tohoto UE. LP-WUR UE, který spotřebovává mikrowatty energie, tento signál detekuje a ověří jej vůči uloženým parametrům. Pokud dojde ke shodě, LP-WUR aktivuje hlavní přijímač UE a protokoly vyšších vrstev, což umožní UE přijímat stránkovací zprávy, aktualizace systémových informací nebo datové přenosy. Tento proces snižuje potřebu, aby se hlavní přijímač periodicky probouzel (jako u tradičního [DRX](/mobilnisite/slovnik/drx/)), a významně tak snižuje celkovou spotřebu energie. LP-WUS je podrobně popsán ve specifikacích jako TS 38.774 a 38.869, které pokrývají jeho výkonnostní požadavky a integraci s síťovým slicingem a službami IoT, což z něj činí klíčový prvek pro energeticky efektivní 5G sítě.

## K čemu slouží

LP-WUS byl vytvořen jako doplněk k [LP-WUR](/mobilnisite/slovnik/lp-wur/) pro řešení problémů s energetickou účinností v 5G NR, zejména pro zařízení internetu věcí (IoT) a zařízení se sníženou schopností (RedCap), která vyžadují životnost baterie v řádu desetiletí. Před Release 18 NR spoléhalo na stránkovací mechanismy prostřednictvím hlavního přijímače, což nutilo UE se pravidelně probouzet během cyklů nespojitého příjmu ([DRX](/mobilnisite/slovnik/drx/)) a spotřebovávat energii i v případě, že žádná komunikace nečekala. Tento přístup byl pro většinu času nečinná zařízení neefektivní, což vedlo ke zkrácení životnosti baterie a omezovalo škálovatelnost masivních nasazení IoT v NR sítích.

Motivace pro LP-WUS vychází z potřeby síťově iniciovaného spouštěče, který může s minimální režií oslovit nečinná UE, a byla inspirována technologiemi rádiového buzení v jiných bezdrátových standardech. Řeší problém 'slepého' probouzení tím, že poskytuje cílený signál, který aktivuje UE pouze v případě potřeby, a snižuje tak energii spotřebovanou při naslouchání v nečinnosti (idle listening). Historicky nabízely podobné funkce LTE-M a NB-IoT, ale nebyly nativní součástí NR; LP-WUS integruje tyto koncepty do 5G a umožňuje bezproblémovou podporu vertikál s nízkou spotřebou. Tím, že umožňuje UE hluboce spát, dokud nejsou vyvolána pomocí LP-WUS, usnadňuje aplikace jako senzory pro chytrá města, sledovače majetku nebo zdravotní monitory ve formě nositelných zařízení, kde jsou okamžitá dosažitelnost a ultra nízká spotřeba energie klíčové, a rozšiřuje tak použitelnost NR pro udržitelné a nákladově efektivní ekosystémy IoT.

## Klíčové vlastnosti

- Jednoduchá modulace pro nízkopříkonovou detekci přijímačem LP-WUR
- Vysíláno gNB za účelem aktivace hlavního přijímače UE
- Nese identifikaci UE nebo skupiny pro cílené buzení
- Konfigurovatelné prostřednictvím signalizace RRC pro optimalizaci sítě
- Snižuje spotřebu energie UE minimalizací používání hlavního přijímače
- Integruje se s fyzickou vrstvou NR a procedurami stránkování

## Související pojmy

- [LP-WUR – Low Power Wake Up Receiver](/mobilnisite/slovnik/lp-wur/)
- [LP-SS – Low Power Synchronization Signal](/mobilnisite/slovnik/lp-ss/)

## Definující specifikace

- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.410** (Rel-19) — NG Interface Introduction for NG-RAN to 5GC
- **TS 38.420** (Rel-19) — Introduction to Xn interface specifications
- **TS 38.470** (Rel-19) — F1 Interface Introduction
- **TS 38.774** (Rel-19) — Rel-19 LP-WUS/WUR RF Requirements TR
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [LP-WUS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lp-wus/)
