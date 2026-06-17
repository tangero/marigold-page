---
slug: "cbl"
url: "/mobilnisite/slovnik/cbl/"
type: "slovnik"
title: "CBL – Current Bucket Level"
date: 2025-01-01
abbr: "CBL"
fullName: "Current Bucket Level"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cbl/"
summary: "CBL je čítač používaný v řadiči základnové stanice (BSC) ke správě využití rádiových prostředků mobilní stanice. Sleduje objem přenesených dat, měřený v jednotkách jako kilobajty, a je klíčovým parame"
---

CBL je čítač v řadiči základnové stanice (Base Station Controller), který sleduje objem dat přenesených mobilní stanicí v kilobajtech pro účely účtování předplacených služeb v reálném čase a řízení služeb v sítích GSM/GPRS/EDGE.

## Popis

Current Bucket Level (CBL) je základní parametr související s účtováním, definovaný v architektuře základnového stanicového systému ([BSS](/mobilnisite/slovnik/bss/)) podle 3GPP, který spravuje konkrétně řadič základnové stanice ([BSC](/mobilnisite/slovnik/bsc/)). Funguje jako dekrementační čítač, který sleduje objem dat (nebo někdy u okruhově přepínaných služeb dobu trvání) spotřebovaný mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) pro konkrétní účtovací kontext, například předplacený datový balík. CBL se měří v kvantifikovatelných jednotkách, typicky kilobajtech pro paketové datové služby, a jeho hodnota představuje zbývající povolený objem před tím, než musí být spuštěna akce související s účtováním, jako je pozastavení služby nebo notifikace.

Z architektonického hlediska je CBL udržován lokálně v rámci BSC po dobu trvání datové relace nebo kontextu správy mobility. Jeho počáteční hodnota je poskytnuta účtovacím systémem jádra sítě, často prostřednictvím uzlu SGSN (Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node) za použití zpráv protokolu [BSSGP](/mobilnisite/slovnik/bssgp/) (BSS GPRS Protocol) přes rozhraní Gb. BSC je zodpovědný za snižování hodnoty CBL v reálném čase na základě skutečného objemu dat přeneseného do mobilní stanice a z ní. Toto účtování v reálném čase je kritickou funkcí, která umožňuje přesné předplacené účtování a okamžité řízení služeb bez neustálé signalizace do jádra sítě pro každý datový paket.

Role CBL je klíčová pro vynucování účtovacích politik. Jak data proudí, BSC průběžně monitoruje CBL. Když CBL dosáhne konfigurovatelné prahové hodnoty (často nula nebo nízká hranice), BSC musí provést akci podle pokynů jádra sítě. To typicky zahrnuje odeslání notifikace do SGSN (indikace 'Bucket Empty') nebo přímé omezení datového toku uživatele. SGSN pak může komunikovat s online účtovacím systémem ([OCS](/mobilnisite/slovnik/ocs/)) za účelem doplnění balíku nebo aplikace rozhodnutí politik. Tento mechanismus zajišťuje, že předplacení účastníci nemohou překročit svůj kreditní limit, a umožňuje téměř okamžité řízení služeb, což je regulační požadavek na mnoha trzích.

Klíčové komponenty interagující s CBL zahrnují BSC (který hostí a spravuje čítač), SGSN (který poskytuje počáteční hodnoty a přijímá notifikace) a podkladové protokoly GPRS tunelování a správy rádiových prostředků, které umožňují měřený přenos dat. CBL je základním kamenem funkce Advice of Charge (AoC) a možností okamžitého ukončení služeb vyžadovaných pro předplacené služby, což z něj činí nezbytný prvek pro komerční provoz mobilních sítí, zejména na trzích s vysokým podílem předplacených účastníků.

## K čemu slouží

CBL byl zaveden, aby řešil kritickou komerční potřebu spolehlivého a v reálném čase působícího řízení účtování v mobilních sítích, zejména pro předplacené modely předplatného. Před jeho standardizací bylo zavádění předplacených služeb, zejména pro data, obtížné a často se spoléhalo na méně přesné dávkové zpracování po skončení relace nebo proprietární řešení, která mohla vést k úniku výnosů nebo špatné zákaznické zkušenosti kvůli opožděnému pozastavení služby. CBL poskytuje standardizovaný, síťový mechanismus pro přesné, na relaci citlivé účtování prostředků přímo v místě jejich spotřeby ([BSC](/mobilnisite/slovnik/bsc/)).

Jeho vytvoření bylo motivováno růstem datových služeb [GPRS](/mobilnisite/slovnik/gprs/) a EDGE ve 3GPP Release 8 a novějších, kde datová spotřeba mohla rychle vyčerpat uživatelský kredit. Operátoři potřebovali způsob, jak v reálném čase vynucovat výdajové limity, aby ochránili své výnosy a dali zákazníkům kontrolu nad jejich výdaji. CBL to řeší delegováním podrobného, vysokofrekvenčního úkolu měření spotřeby na BSC, který spravuje rádiové prostředky, zatímco jádro sítě si ponechává celkovou kontrolu politik. Tato distribuovaná architektura vyvažuje signalizační zátěž a umožňuje rychlé akce.

Tato technologie řeší omezení spočívající v absenci standardizovaného čítače v reálném čase uvnitř rádiové přístupové sítě, který by byl určen pro účtování. Umožňuje složité tarifní modely, jako jsou objemové datové balíky, a je zásadní pro soulad s telekomunikačními předpisy týkajícími se ochrany spotřebitele a transparentního účtování. Poskytnutím jasné, klesající míry zbývajících prostředků tvoří technický základ pro notifikace, jako jsou upozornění 'blížící se datový limit', což zlepšuje uživatelský zážitek u předplacených služeb.

## Klíčové vlastnosti

- Dekrementační čítač v reálném čase pro objem dat nebo délku hovoru
- Spravován lokálně řadičem základnové stanice (BSC) pro řízení s nízkou latencí
- Počáteční hodnota a politiky poskytnuty jádrem sítě (SGSN/účtovací systém)
- Při překročení prahu spouští notifikace (např. Bucket Empty) do jádra sítě
- Umožňuje okamžité pozastavení nebo omezení služby, aby se zabránilo překročení výdajů
- Základní prvek pro předplacené účtování a funkci Advice of Charge (AoC)

## Související pojmy

- [BSSGP – Base Station System GPRS Protocol](/mobilnisite/slovnik/bssgp/)

## Definující specifikace

- **TS 48.018** (Rel-19) — BSS-SGSN Interface for GPRS Control

---

📖 **Anglický originál a plná specifikace:** [CBL na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbl/)
