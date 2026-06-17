---
slug: "nmr"
url: "/mobilnisite/slovnik/nmr/"
type: "slovnik"
title: "NMR – Network Measurement Results"
date: 2025-01-01
abbr: "NMR"
fullName: "Network Measurement Results"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nmr/"
summary: "Standardizovaná sada výkonnostních a rádiových měření shromažďovaných od uživatelského zařízení (UE) a síťových prvků. Poskytuje klíčová data pro optimalizaci sítě, řešení problémů a zajištění kvality"
---

NMR je standardizovaná sada výkonnostních a rádiových měření shromažďovaných od uživatelského zařízení a sítě, která poskytuje klíčová data pro optimalizaci, řešení problémů a zajištění kvality služeb.

## Popis

Výsledky síťových měření (NMR) představují komplexní datovou sadu definovanou ve specifikacích 3GPP, která zachycuje výkon a provozní stav rádiové přístupové sítě a uživatelského zařízení. Mechanismus sběru zahrnuje UE, které je schopné provádět různá měření na obsluhující a sousední buňky, a samotnou síťovou infrastrukturu, která může shromažďovat data o rádiových podmínkách, zatížení provozem a míře chyb. Tato měření jsou typicky hlášena systému správy sítě prostřednictvím signalizace řídicí roviny, často spouštěna síťovými požadavky nebo nakonfigurovanými kritérii hlášení, jako jsou prahové hodnoty událostí nebo periodické časovače.

Klíčové složky dat NMR zahrnují úroveň přijímaného referenčního signálu (RSRP), kvalitu přijímaného referenčního signálu (RSRQ), poměr signálu k šumu a interferenci (SINR), časový předstih a identifikační informace buňky pro obsluhující i sousední buňky. Dále mohou zahrnovat výkonnostní metriky, jako jsou míry blokových chyb, úspěšnost předávání hovoru a statistiky přerušení hovorů. Architektura pro zpracování NMR zahrnuje rádiovou přístupovou síť (RAN), která data shromažďuje a může je předzpracovat, a páteřní síť, která je předává do operačních a podpůrných systémů ([OSS](/mobilnisite/slovnik/oss/)) k analýze.

V síťovém ekosystému slouží NMR jako základní nezpracovaná data pro mnoho automatizovaných a manuálních optimalizačních procesů. Síťoví inženýři a algoritmy samoorganizujících se sítí (SON) tato data využívají k provádění úloh, jako je optimalizace robustnosti mobility ([MRO](/mobilnisite/slovnik/mro/)), optimalizace pokrytí a kapacity ([CCO](/mobilnisite/slovnik/cco/)) a vyrovnávání zatížení. Analýzou trendů a anomálií v NMR mohou operátoři identifikovat díry v pokrytí, problémy s interferencí a kapacitní úzká místa, což vede k cíleným úpravám sítě, jako je sklon antény, změny nastavení výkonu nebo plánování nových lokalit buněk.

## K čemu slouží

Primárním účelem NMR je poskytnout objektivní, standardizovaný a podrobný pohled na výkon rádiové sítě z perspektivy sítě i koncového uživatele. Před jeho formální standardizací se operátoři spoléhali na nesourodá, výrobcem specifická měření a testy z vozidel, které byly nákladné, neprobíhaly v reálném čase a poskytovaly omezené prostorové a časové pokrytí. NMR tento problém řeší tím, že umožňuje nepřetržitý sběr dat asistovaný UE napříč celou základnou účastníků, což nabízí mnohem bohatší a ekonomičtější datovou sadu pro síťovou analýzu.

Jeho vytvoření bylo motivováno rostoucí složitostí mobilních sítí a potřebou efektivnějších provozních postupů. Jak se sítě vyvíjely od 2G přes 3G a dále, manuální optimalizace se stala neudržitelnou. NMR poskytuje nezbytnou telemetrii potřebnou pro automatizaci úloh správy sítě, což je základním kamenem moderních operačních podpůrných systémů ([OSS](/mobilnisite/slovnik/oss/)) a samoorganizujících se sítí (SON). Řeší kritický problém udržování a zlepšování kvality uživatelského zážitku (QoE) v dynamickém rádiovém prostředí tím, že dodává data nezbytná pro proaktivní a reaktivní ladění sítě.

Historicky formalizace NMR v Release 6 korespondovala s úsilím průmyslu směrem k více daty řízeným síťovým operacím a počátečním konceptům SON. Stanovila společný jazyk pro hlášení měření, čímž zajistila interoperabilitu mezi vícevýrobcovými UE a síťovými zařízeními, což je klíčové pro rozsáhlá, heterogenní nasazení sítí.

## Klíčové vlastnosti

- Standardizované hlášení rádiových měření z UE (např. RSRP, RSRQ)
- Podpora měření na obsluhující buňce a více sousedních buňkách
- Konfigurovatelné spouštěče hlášení (událostní, periodické)
- Sběr výkonnostních metrik, jako je úspěšnost a neúspěšnost předání hovoru
- Data využívaná funkcemi samoorganizujících se sítí (SON)
- Základ pro optimalizaci sítě a správu poruch

## Související pojmy

- [MRO – Mobility Robustness Optimisation](/mobilnisite/slovnik/mro/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [NMR na 3GPP Explorer](https://3gpp-explorer.com/glossary/nmr/)
