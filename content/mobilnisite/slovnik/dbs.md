---
slug: "dbs"
url: "/mobilnisite/slovnik/dbs/"
type: "slovnik"
title: "DBS – Downlink level B Modulation and Coding Scheme"
date: 2025-01-01
abbr: "DBS"
fullName: "Downlink level B Modulation and Coding Scheme"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dbs/"
summary: "DBS je specifická konfigurace modulačního a kódového schématu (MCS) definovaná pro downlinkové přenosy ve standardech 3GPP, primárně pro GSM/EDGE Evolution. Představuje konkrétní kombinaci typu modula"
---

DBS je specifická konfigurace modulačního a kódového schématu pro downlink v 3GPP GSM/EDGE Evolution, optimalizující spektrální účinnost a spolehlivost spoje pro plánování sítě a adaptaci spojů.

## Popis

Downlink level B Modulation and Coding Scheme (DBS) je technická specifikace v rámci vývojového rámce GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Spadá pod širší koncept Link Adaptation, kde síť dynamicky vybírá nejvhodnější [MCS](/mobilnisite/slovnik/mcs/) na základě měření kvality rádiového kanálu v reálném čase (např. poměr Carrier-to-Interference, [C/I](/mobilnisite/slovnik/c-i/)), aby maximalizovala datovou propustnost při zachování přijatelné míry chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)). DBS je jeden diskrétní bod v spektru dostupných MCS, z nichž každý je definován specifickým modulačním formátem (jako [GMSK](/mobilnisite/slovnik/gmsk/) nebo 8PSK) a rychlostí kódování pro dopřednou korekci chyb ([FEC](/mobilnisite/slovnik/fec/)).

Architektonicky je DBS implementována na fyzické vrstvě základnové stanice ([BTS](/mobilnisite/slovnik/bts/)) a mobilní stanice. Vysílač BTS aplikuje specifickou modulaci (mapování bitů na symboly) a kanálové kódování (přidání redundantních bitů) podle definice DBS. Odpovídající přijímač v mobilní stanici musí být schopen demodulovat a dekódovat signál formátovaný tímto schématem. Výběr DBS oproti jiným MCS, jako je DAS nebo DACS, je řízen protokoly vyšších vrstev na základě hlášení o kvalitě kanálu od mobilního zařízení.

Klíčové komponenty podílející se na fungování DBS zahrnují kanálový kodér, který aplikuje konvoluční nebo turbokódování při specifikované rychlosti; modulátor, který mapuje zakódované bity na zvolenou konstelaci; a ekvalizér na straně přijímače pro potlačení intersymbolového rušení. Jeho výkon je důsledně charakterizován ve specifikacích 3GPP (jako TS 45.005) pomocí parametrů, jako je požadovaný C/I pro cílový BLER, a jeho teoretická maximální bitová rychlost. Tyto výkonnostní tabulky jsou nezbytné pro algoritmy správy rádiových prostředků.

Úloha DBS v síti spočívá v poskytování spolehlivého datového kanálu pro paketově přepínané služby (přes EGPRS), když podmínky na kanálu odpovídají jejímu specifickému pracovnímu bodu. Přispívá k celkové spektrální účinnosti systému GERAN. Díky dobře definované sadě MCS včetně DBS může systém provádět jemně odstupňované adaptace, přepínat na robustnější (ale pomalejší) schéma jako DAS při špatných podmínkách, nebo na schéma vyššího řádu jako DACS při výborných podmínkách, přičemž DBS slouží jako mezilehlá možnost.

## K čemu slouží

DBS byla zavedena jako součást kontinuálního vývoje GSM směrem k Enhanced Data rates for GSM Evolution (EDGE) a dále, konkrétně ve vydání 10. Primární motivací bylo upřesnit sadu dostupných modulačních a kódových schémat, aby lépe odpovídala vývojovým možnostem hardwaru a optimalizovala výkon pro nově vznikající mobilní datové služby. Před takovým upřesněním mohla být sada MCS suboptimální, což zanechávalo mezery v křivce kompromisu mezi výkonem a robustností, což vedlo buď k neefektivnímu využití spektra, nebo k nadbytečným retransmisím.

Vytvoření DBS řešilo potřebu standardizovaných, dobře charakterizovaných pracovních bodů, na které by se mohli výrobci zařízení a provozovatelé sítí spolehnout pro předvídatelný výkon. Definováním specifických 'úrovní', jako je úroveň B, zajišťuje 3GPP interoperabilitu mezi základnovými stanicemi a koncovými zařízeními různých výrobců. Řeší problém, jak efektivně přenášet rostoucí objemy dat v rámci původního GSM spektra, tím, že poskytuje pečlivě zvolenou kombinaci modulace a kódování, která nabízí dobrou rovnováhu mezi datovou rychlostí a požadovanou kvalitou signálu.

Historicky, jak se poptávka uživatelů přesouvala od hlasu k datům, se původní GSM modulace GMSK a základní kódování staly nedostatečnými. EDGE zavedlo modulaci 8PSK a nová kódová schémata. DBS představuje následný krok v tomto vývoji, součást procesu zhušťování sady dostupných MCS, což umožňuje algoritmu adaptace spojů činit přesnější volby, a tím vytěžit maximální propustnost z dostupných rádiových prostředků a zlepšit uživatelský zážitek z datových aplikací.

## Klíčové vlastnosti

- Definována jako specifická kombinace typu modulace a rychlosti kanálového kódování
- Součást sady MCS pro EGPRS pro downlinkové přenosy
- Charakterizována požadovaným výkonem poměru Carrier-to-Interference (C/I) pro cílový BLER
- Používána síťově řízenými algoritmy Link Adaptation
- Umožňuje dynamický kompromis mezi datovou propustností a robustností přenosu
- Standardizována pro zajištění interoperability mezi různými výrobci v sítích GERAN

## Související pojmy

- [MCS – Modulation and Coding Schemes](/mobilnisite/slovnik/mcs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [EGPRS – Enhanced GPRS](/mobilnisite/slovnik/egprs/)

## Definující specifikace

- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 45.860** (Rel-11) — Precoded EGPRS2 Downlink Study

---

📖 **Anglický originál a plná specifikace:** [DBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dbs/)
