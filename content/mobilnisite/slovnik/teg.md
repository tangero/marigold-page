---
slug: "teg"
url: "/mobilnisite/slovnik/teg/"
type: "slovnik"
title: "TEG – Timing Error Group"
date: 2025-01-01
abbr: "TEG"
fullName: "Timing Error Group"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/teg/"
summary: "Timing Error Group (TEG) je logická skupina uživatelských zařízení (UE), která sdílejí podobné časové charakteristiky nebo synchronizační chyby vůči síti. TEG byl zaváděn pro pokročilé lokalizování a"
---

TEG je logická skupina uživatelských zařízení (UE), která sdílejí podobné časové chyby, což umožňuje síti efektivně řídit a kompenzovat nepřesnosti na úrovni skupiny pro pokročilé lokalizování a služby citlivé na časování.

## Popis

Timing Error Group (TEG) je koncept zaváděný ve 3GPP Release 17, primárně v specifikacích pro lokalizování a řízení radiofrekvenčních zdrojů (např. TS 37.355, 38.331, 38.305). Označuje skupinu UE, které síť – konkrétně Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) nebo gNB – identifikuje jako zařízení s korelovanými nebo podobnými časovými chybami. Tyto chyby vznikají z faktorů jako společný drift hodin, sdílené charakteristiky prostředí přenosu (např. pobyt ve stejné indoor oblasti s podobným multipath) nebo obsluha ze stejného synchronizačního zdroje s známým offsetem. TEG není fyzická entita, ale logická asociace udržovaná v síti pro optimalizaci lokalizačních procedur a alokace zdrojů pro služby závislé na časování.

Architektonicky koncept TEG zahrnuje několik síťových funkcí. LMF jako centrální lokalizační kontrolér může definovat TEG na základě reportů lokalizačních měření (např. měření Reference Signal Time Difference ([RSTD](/mobilnisite/slovnik/rstd/)) pro [OTDOA](/mobilnisite/slovnik/otdoa/)) nebo požadavků na asistenční data od UE. gNB může být také zapojen do řízení TEG pro řízení radiofrekvenčních zdrojů, obzvláště pro sidelink lokalizování, kde UE měří přímo mezi sebou. Klíčové komponenty zahrnují lokalizační protokoly ([LPP](/mobilnisite/slovnik/lpp/), NRPPa), které mohou přenášet identifikátory TEG a související informace o chybách, schopnosti UE, které indikují podporu procedur na základě TEG, a síťové algoritmy, které klastrují UE do skupin na základě statistické analýzy jejich časových měření.

Jak funguje: Síť nejprve identifikuje UE vhodné pro skupinování, často během periodických lokalizačních session nebo při počátečním přístupu. Například, více senzorů v fabrice může reportovat časové měření s konstantní odchylkou kvůli sdílenému neideálnímu zdroji hodin. LMF přidělí tyto UE do TEG a přidělí TEG ID. Následně, namísto samostatného řešení časové chyby každého UE, může síť aplikovat korekce na úrovni skupiny. Ve výpočtech lokalizace může LMF kompenzovat společnou chybu uvnitř TEG, což zlepšuje absolutní přesnost všech členů. Pro sidelink lokalizování mohou být UE ve stejné TEG konfigurovány se specifickými zdroji nebo jim mohou být nastaveny upravené časové očekávání pro zlepšení přesnosti relativní lokalizace mezi nimi. Tento skupinový přístup snižuje signalizační overhead a výpočetní zátěž ve srovnání s řešením chyb pro každé UE samostatně.

## K čemu slouží

TEG byl vytvořen v Release 17 pro řešení problémů spojených s poskytováním vysoké přesnosti lokalizování a časové synchronizace pro nové 5G use cases, obzvláště průmyslový IoT, komunikaci vozidlo-s-okolím ([V2X](/mobilnisite/slovnik/v2x/)) a rozšířené sidelink služby. Předchozí releases řešily časové chyby pro každé UE samostatně, což bylo neefektivní a méně přesné ve scénářích, kde více zařízení má podobné časové poruchy kvůli sdíleným faktorům prostředí nebo omezením hardwaru. Pro husté deploymenty, jako fabrikové senzory nebo vozidlové platoony, samostatné odhadování a kompenzace chyb vedlo k nadměrné signalizaci a suboptimálnímu výkonu lokalizování.

Motivace pro TEG vychází z potřeb škálovatelných a přesných lokalizačních mechanismů v 5G-Advanced. Skupinováním UE s korelovanými chybami může síť dosáhnout několika benefitů: snižuje množství asistenčních dat a reportů měření potřebných, protože společná komponenta chyby může být komunikována jednou pro skupinu; zlepšuje přesnost lokalizování tím, že umožňuje kompenzaci skupinových odchylek na straně síť; a umožňuje pokročilé funkce jako kooperativní lokalizování, kde UE uvnitř skupiny pomáhají kalibrovat mezi sebou. TEG specificky řeší problémy v sidelink lokalizování (např. pro V2X), kde relativní časování mezi UE je kritické, a ve scénářích s omezenou dostupností [GNSS](/mobilnisite/slovnik/gnss/), kde UE musí záviset na časování z buněčné sítě, které může mít nepřesnosti na úrovni skupiny. Tento koncept podporuje evoluce směrem více autonomních a efektivních lokalizačních architektur potřebných pro mission-critical a komerční aplikace.

## Klíčové vlastnosti

- Logické skupinování UE s korelovanými časovými chybami pro efektivní řízení síti
- Podporuje zvýšenou přesnost lokalizování pomocí kompenzace chyb na úrovni skupiny
- Snižuje signalizační overhead v lokalizačních protokolech (LPP/NRPPa) pro husté deploymenty UE
- Umožňuje optimalizovanou alokaci zdrojů a konfiguraci pro sidelink lokalizování
- Podporuje kooperativní lokalizační techniky mezi členy skupiny
- Identifikován pomocí TEG ID řízeného LMF nebo gNB

## Související pojmy

- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.455** (Rel-19) — NR Positioning Protocol A (NRPPa)
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [TEG na 3GPP Explorer](https://3gpp-explorer.com/glossary/teg/)
