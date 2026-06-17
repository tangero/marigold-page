---
slug: "mr"
url: "/mobilnisite/slovnik/mr/"
type: "slovnik"
title: "MR – Medium Range Base Station"
date: 2025-01-01
abbr: "MR"
fullName: "Medium Range Base Station"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mr/"
summary: "Základnová stanice středního dosahu (MR) je typ základnové stanice definovaný ve standardech 3GPP pro mobilní sítě, která typicky pokrývá středně velkou geografickou oblast. Je klíčovou součástí rádio"
---

MR je typ základnové stanice definovaný ve standardech 3GPP, který pokrývá středně velkou geografickou oblast a poskytuje bezdrátové připojení uživatelským zařízením jako součást rádiové přístupové sítě.

## Popis

Základnová stanice středního dosahu (MR) je standardizovaný síťový prvek v architektuře rádiové přístupové sítě (RAN) 3GPP. Funguje jako přijímací a vysílací stanice, která komunikuje s uživatelským zařízením (UE) přes rozhraní vzduchem a spravuje řízení rádiových zdrojů, plánování a navazování spojení. Základnová stanice MR je charakterizována svým středním dosahem, který se nachází mezi lokálními (např. femtobuňky) a rozlehlými (např. makrobuňky) nasazeními, což ji činí vhodnou pro předměstské, venkovské nebo specializované scénáře pokrytí. Její technické specifikace zahrnují charakteristiky vysílače a přijímače, jako je výstupní výkon, kmitočtová pásma, modulační schémata a požadavky na velikost chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)), které jsou podrobně popsány v četných technických specifikacích (TS) 3GPP, aby byl zajištěn konzistentní výkon a minimální interference.

Architektonicky je základnová stanice MR propojena s jádrem sítě přes backhaulové spoje a podporuje jak řídicí, tak uživatelskou rovinu. V kontextu LTE a 5G NR může být implementována jako [eNB](/mobilnisite/slovnik/enb/) ([E-UTRAN](/mobilnisite/slovnik/e-utran/) Node B) nebo gNB (Next Generation Node B) v souladu s funkčními rozděleními definovanými 3GPP. Mezi klíčové vnitřní komponenty patří základnová jednotka ([BBU](/mobilnisite/slovnik/bbu/)) pro digitální zpracování signálu a dálková rádiová jednotka (RRU) pro vysílání a příjem vysokofrekvenčního signálu, ačkoli implementace se mohou lišit. MR podporuje více technologií rádiového přístupu (RAT), jak je specifikováno, včetně LTE a NR, a musí splňovat přísné požadavky na emise ve spektru, parazitní emise a citlivost přijímače, aby byla zachována kvalita sítě.

Její role v síti je klíčová pro poskytování spolehlivého bezdrátového přístupu a umožňuje služby jako hlas přes LTE (VoLTE), mobilní širokopásmový přístup a připojení pro IoT. Základnová stanice MR provádí kritické postupy RAN, jako je vyhledávání a výběr buňky, náhodný přístup, předávání hovoru a formování svazku (v 5G). Podporuje také pokročilé funkce, jako je agregace nosných, [MIMO](/mobilnisite/slovnik/mimo/) (Multiple-Input Multiple-Output) a duální konektivita, v závislosti na vydání 3GPP. Správa a provoz jsou usnadněny prostřednictvím rozhraní, jako je rozhraní X2 (pro komunikaci mezi eNB v LTE) nebo rozhraní Xn (pro komunikaci mezi gNB v 5G), což zajišťuje koordinovanou mobilitu a vyvažování zátěže v celé síti.

## K čemu slouží

Základnová stanice středního dosahu (MR) byla zavedena, aby uspokojila potřebu standardizované kategorie základnové stanice se specifickým dosahem, která vyplňuje mezeru mezi malými a makro buňkami v nasazeních mobilních sítí. Před její standardizací se síťoví operátoři spoléhali na proprietární nebo méně definované typy základnových stanic, což vedlo k problémům s interoperabilitou a nekonzistentním výkonem. Definováním MR ve specifikacích 3GPP umožňuje výrobcům vyvíjet kompatibilní zařízení, která lze bezproblémově integrovat do vícevýrobcových sítí, a zajistit tak spolehlivé poskytování služeb v prostředích se středním dosahem, jako jsou městečka, dálnice nebo průmyslové oblasti.

Historicky, jak se mobilní sítě vyvíjely od 2G do 5G, rostla rozmanitost scénářů nasazení, což vyžadovalo základnové stanice s přizpůsobenými charakteristikami pro různé hustoty a geografické podmínky. Specifikace MR řeší problémy související s mezerami v pokrytí, optimalizací kapacity a nákladově efektivním rozšiřováním sítě. Poskytuje vyvážené řešení tam, kde by makrobuňky mohly být předimenzované a malé buňky nedostatečné, čímž optimalizuje kapitálové a provozní výdaje. Vytvoření MR bylo motivováno snahou odvětví o granulárnější a flexibilnější architektury RAN, které podporují rostoucí poptávku po mobilních datech a vznik nových případů užití, jako je pevný bezdrátový přístup.

Dále základnové stanice MR hrají klíčovou roli při plnění regulatorních požadavků na využití spektra a elektromagnetickou kompatibilitu. Dodržováním standardizovaných technických parametrů pomáhají předcházet interferencím s jinými rádiovými systémy a zajišťují efektivní využití licencovaných kmitočtových pásem. Tato standardizace také usnadňuje globální roaming a certifikaci zařízení, což přispívá ke škálovatelnosti a spolehlivosti moderních mobilních sítí.

## Klíčové vlastnosti

- Střední geografický dosah pokrytí, typicky mezi malými a makro buňkami
- Soulad se specifikacemi 3GPP pro výkon vysílače a přijímače
- Podpora více technologií rádiového přístupu (např. LTE, NR)
- Rozhraní s jádrem sítě a dalšími základnovými stanicemi (např. X2, Xn)
- Pokročilé rádiové schopnosti jako MIMO a agregace nosných
- Správa prostřednictvím standardizovaných postupů provozu a údržby

## Související pojmy

- [eNB – Evolved Node B](/mobilnisite/slovnik/enb/)

## Definující specifikace

- **TS 22.156** (Rel-19) — Mobile Metaverse Services
- **TR 22.978** (Rel-19) — Feasibility of All-IP Network (AIPN) in 3GPP
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 26.506** (Rel-19) — Real-Time Media Communication Architecture for 5G
- **TR 26.812** (Rel-18) — Technical Report
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 29.079** (Rel-19) — Optimal Media Routeing (OMR) Procedures
- **TS 33.849** (Rel-14) — 3GPP Privacy Principles and Guidelines
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.755** (Rel-15) — US 600 MHz LTE Band 71 Technical Report
- … a dalších 30 specifikací

---

📖 **Anglický originál a plná specifikace:** [MR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mr/)
