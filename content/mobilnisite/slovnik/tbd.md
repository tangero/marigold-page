---
slug: "tbd"
url: "/mobilnisite/slovnik/tbd/"
type: "slovnik"
title: "TBD – To Be Determined"
date: 2025-01-01
abbr: "TBD"
fullName: "To Be Determined"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/tbd/"
summary: "Zástupný termín používaný ve specifikacích 3GPP k označení, že konkrétní parametr, procedura nebo koncept ještě není dokončen a bude definován v pozdější verzi nebo specifikaci. Je klíčový pro řízení"
---

TBD je zástupný termín ve specifikacích 3GPP označující, že parametr, procedura nebo koncept ještě není dokončen a bude definován později.

## Popis

V kontextu standardizace 3GPP je 'To Be Determined' (TBD) formální zástupná notace používaná v technických specifikacích (TS) a technických zprávách (TR). Značí, že konkrétní technický aspekt – například hodnota parametru, detail algoritmu, pole zprávy nebo i celá funkční procedura – nebyl v době publikace dané verze dokumentu dohodnut nebo plně specifikován. Použití TBD je klíčovým nástrojem projektového řízení v rámci procesu vývoje standardů, který umožňuje pracovním skupinám posouvat celkovou architekturu a rámec funkce, aniž by je blokovaly nevyřešené technické debaty nebo závislosti na jiných pracovních položkách.

Tato notace je systematicky aplikována napříč různými řadami specifikací. Například v protokolových specifikacích (např. řady 24, 25, 36, 38) se může TBD objevit v tabulce informačních prvků, což značí, že kódový bod nebo délka jsou neuzavřené. V požadavcích na služby (řada 22) nebo popisech architektury (řada 23) může označovat, že konkrétní schopnost služby nebo chování síťové funkce je předmětem studie. Vyřešení TBD je klíčovým výstupem pro následující vydání nebo aktualizace specifikací, což je často dokumentováno v žádostech o změnu ([CR](/mobilnisite/slovnik/cr/)), které nahradí text TBD finálním technickým obsahem.

Životní cyklus položky TBD se řídí pravidly číslování a verzování specifikací 3GPP. Specifikace obsahující TBD je publikována s vědomím, že tyto otevřené položky budou uzavřeny, typicky předtím, než specifikace dosáhne stabilního, implementovatelného stavu (např. na konci vydání Release). Proces řešení zahrnuje technické diskuze, simulace a vytváření konsenzu v rámci příslušné Skupiny pro technické specifikace ([TSG](/mobilnisite/slovnik/tsg/)) nebo Pracovní skupiny ([WG](/mobilnisite/slovnik/wg/)). Po vyřešení je specifikace aktualizována a značka TBD odstraněna, což poskytuje jasnost výrobcům zařízení a síťovým operátorům pro implementaci.

## K čemu slouží

Primárním účelem zástupného označení TBD je umožnit paralelní a inkrementální vývoj složitých telekomunikačních standardů. Standardy 3GPP zahrnují tisíce stran napříč stovkami specifikací, které vyvíjí stovky společností. Je nepraktické dokončit každý drobný detail současně. Mechanismus TBD umožňuje specifikovat různé části systému nezávisle a různým tempem. Například pracovní skupiny pro rádiový přístupový síť (RAN) mohou definovat novou strukturu fyzické vrstvy kanálu, zatímco označí určité parametry řízení vyšších vrstev jako TBD, které mohou být později doplněny skupinami pro jádro sítě ([CT](/mobilnisite/slovnik/ct/)) nebo aspekty služeb a systémů ([SA](/mobilnisite/slovnik/sa/)) na základě celkových systémových požadavků.

Historicky by bez takového mechanismu standardizace riskovala významná zpoždění nebo publikaci nekonzistentních specifikací. TBD poskytuje strukturovaný způsob řízení nejistot a závislostí. Explicitně signalizuje čtenářům specifikace – inženýrům, výzkumníkům a implementátorům – které části jsou stabilní a které se mohou změnit, čímž zabraňuje předčasné implementaci založené na předpokladech. To je obzvláště důležité pro perspektivní funkce studované v raných vydáních (např. ve fázi Study Item), kde se zkoumá proveditelnost před začátkem normativní práce a mnoho aspektů je záměrně ponecháno jako TBD, dokud není proveditelnost potvrzena.

## Klíčové vlastnosti

- Zástupný symbol pro nevyřešené technické parametry
- Umožňuje paralelní vývoj napříč různými pracovními skupinami
- Řídí závislosti mezi moduly specifikací
- Formální notace v rámci struktury dokumentů 3GPP
- Signalizuje implementátorům nedokončený obsah
- Řešeno formálním procesem žádosti o změnu (Change Request – CR)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 28.808** (Rel-17) — 5G satellite integration management study
- **TS 32.582** (Rel-19) — HNB Management Information Model for Type 1 Interface
- **TS 32.584** (Rel-19) — HNB OAM&P XML Definitions for Type 1 Interface
- **TS 32.592** (Rel-19) — HeNB OAM&P Information Model
- **TS 32.821** (Rel-9) — SON OAM Architecture for Home NodeB
- **TS 36.106** (Rel-19) — E-UTRA FDD Repeater RF Requirements
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [TBD na 3GPP Explorer](https://3gpp-explorer.com/glossary/tbd/)
