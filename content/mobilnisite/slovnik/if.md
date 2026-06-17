---
slug: "if"
url: "/mobilnisite/slovnik/if/"
type: "slovnik"
title: "IF – Intermediate Frequency"
date: 2026-01-01
abbr: "IF"
fullName: "Intermediate Frequency"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/if/"
summary: "Kmitočet, na který je nosná frekvence přeložena jako mezistupeň při přenosu nebo příjmu v rádiových systémech. Zjednodušuje návrh filtrů a zesilovačů a zlepšuje selektivitu a výkon jak v základnových"
---

IF (mezifrekvence) je mezilehlý kmitočet, na který je nosná přeložena za účelem zjednodušení návrhu filtrů a zesilovačů, čímž se zlepšuje selektivita a výkon v rádiovém přenosu a příjmu.

## Popis

Mezifrekvence (Intermediate Frequency, IF) je klíčový koncept v superhetrodynních rádiových přijímačích a vysílačích, což je dominantní architektura používaná v moderních bezdrátových komunikačních systémech, včetně buněčných sítí definovaných 3GPP, jako jsou LTE a 5G NR. V přijímači je příchozí vysokofrekvenční (RF) signál z antény nejprve zesílen šumově nízkým zesilovačem ([LNA](/mobilnisite/slovnik/lna/)) a poté smíchán se signálem z lokálního oscilátoru ([LO](/mobilnisite/slovnik/lo/)). Tento proces míšení, nazývaný frekvenční konverze nebo heterodynění, vytváří součtové a rozdílové frekvence. Rozdílová frekvence je vybrána jako IF. Toto přeložení dolů posune vysokou, proměnnou nosnou RF frekvenci na pevnou, nižší IF.

Tato pevná IF je klíčová, protože umožňuje použití vysoce výkonných, stabilních a selektivních filtrů a zesilovačů optimalizovaných pro jedinou frekvenci. Výběr kanálu (naladění na konkrétní nosnou) je primárně dosažen změnou frekvence lokálního oscilátoru, což mění RF frekvenci, která je přeložena na pevnou IF. IF signál je poté výrazně zesílen a filtrován, aby se odstranilo sousední kanálové rušení a šum. Toto filtrování je mnohem účinnější a ekonomičtější na pevné, nižší IF než na původní vysoké RF. Po zpracování na IF je signál často podruhé přeložen dolů na základní pásmo pro analogově-digitální převod a další digitální zpracování signálu ([DSP](/mobilnisite/slovnik/dsp/)).

Ve vysílačích je proces obrácený. Signál základního pásma nebo nízké IF je přeložen nahoru na konečnou nosnou RF frekvenci, často s využitím jednoho nebo více mezifrekvenčních stupňů. To umožňuje účinné zesílení výkonu na pevné IF před konečným přeložením nahoru na RF, což může zlepšit linearitu a účinnost. Použití IF stupňů je zásadní pro dosažení přísných požadavků na výkon dle standardů 3GPP pro citlivost, selektivitu, dynamický rozsah a spektrální čistotu v rádiových částech uživatelských zařízení (UE) i základnových stanic (gNB/[eNB](/mobilnisite/slovnik/enb/)).

## K čemu slouží

Účelem mezifrekvenčního stupně je řešit základní praktické problémy v návrhu rádiových zařízení. Přímé zesílení a filtrování na velmi vysokých RF frekvencích (např. několik GHz pro 5G) je extrémně náročné. Komponenty jako filtry a vysokoziskové zesilovače jsou na těchto frekvencích obtížně navrhovatelné, jsou méně selektivní, mají vyšší šum a jsou dražší. Architektura superhetrodynu s IF stupněm byla historicky vynalezena, aby překonala špatnou selektivitu a citlivost raných přijímačů s laděným RF (TRF).

Převodem signálu na pevnou, nižší IF tento návrh umožňuje, aby hlavní část zesílení a nejkritičtější filtrování (jako je filtr pro výběr kanálu) byly prováděny za optimálních, stabilních podmínek. Tato architektura řeší omezení spočívající v nutnosti ladit více vysokofrekvenčních stupňů současně. Poskytuje vynikající potlačení zrcadlového kmitočtu, selektivitu vůči sousedním kanálům a celkovou citlivost přijímače. V kontextu 3GPP je to nezbytné pro splnění přísných požadavků na blokování, selektivitu a citlivost definovaných v RF konformačních specifikacích (např. TS 38.101 pro NR), které zajišťují, že zařízení mohou spolehlivě fungovat v přeplněném rádiovém prostředí s mnoha rušivými signály.

## Klíčové vlastnosti

- Umožňuje fixně-frekvenční, vysoce selektivní filtrování pro výběr kanálu
- Zjednodušuje návrh vysokoziskových, šumově nízkých zesilovačů
- Zlepšuje celkovou citlivost přijímače a dynamický rozsah
- Usnadňuje potlačení zrcadlového kmitočtu v superhetrodynních přijímačích
- Umožňuje nákladově efektivní a stabilní návrh rádiového hardwaru
- Používá se v uplinkových i downlinkových drahách základnových stanic a UE

## Definující specifikace

- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TR 37.880** (Rel-17) — High-power UE for fixed-wireless/vehicle use
- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR
- **TS 38.774** (Rel-19) — Rel-19 LP-WUS/WUR RF Requirements TR
- **TR 38.803** (Rel-14) — Study on Coexistence and RF Feasibility for 5G NR
- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [IF na 3GPP Explorer](https://3gpp-explorer.com/glossary/if/)
