---
slug: "cbrs"
url: "/mobilnisite/slovnik/cbrs/"
type: "slovnik"
title: "CBRS – Citizens Broadband Radio Service"
date: 2024-01-01
abbr: "CBRS"
fullName: "Citizens Broadband Radio Service"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cbrs/"
summary: "CBRS je rámec pro sdílení spektra v pásmu 3,5 GHz (3550-3700 MHz) ve Spojených státech, který umožňuje dynamický přístup pro komerční sítě LTE/5G a původní uživatele. Zavádí třívrstvý model sdílení s"
---

CBRS je americký rámec pro sdílení spektra v pásmu 3,5 GHz, který využívá třívrstvý model a systém pro přístup ke spektru (SAS) k zajištění dynamické koexistence komerčních sítí LTE/5G a původních uživatelů.

## Popis

Citizens Broadband Radio Service (CBRS) je standardizovaný rámec pro sdílený přístup ke spektru v pásmu 3,5 GHz, konkrétně 3550-3700 MHz ve Spojených státech. Je definován organizací 3GPP pro integraci se systémy LTE (od verze 14) a 5G NR, což umožňuje komerčním mobilním operátorům, podnikům a dalším subjektům nasazovat služby v tomto pásmu vedle původních federálních a satelitních uživatelů. Klíčovou inovací je třívrstvý hierarchický model přístupu řízený automatizovaným systémem pro přístup ke spektru ([SAS](/mobilnisite/slovnik/sas/)), který dynamicky přiděluje spektrum, aby zabránil interferencím a maximalizoval efektivitu.

Z architektonického hlediska CBRS zahrnuje několik klíčových komponent: SAS, což je cloudová databáze a koordinační engine; senzory systému pro monitorování prostředí ([ESC](/mobilnisite/slovnik/esc/)), které detekují signály původních radarů (primárně námořnictva USA); a zařízení CBRS (CBSD), což jsou základnové stanice (eNodeB pro LTE, gNB pro 5G NR) a koncová uživatelská zařízení. SAS ověřuje a autorizuje CBSD, přiřazuje provozní parametry jako frekvenci a výkon a zajišťuje ochranu uživatelů vyšších úrovní. CBSD se musí zaregistrovat u SAS a před vysíláním požádat o přidělení spektra; průběžně hlásí svůj stav a přijímají aktualizace, aby se přizpůsobily měnícím se podmínkám.

Provozně jsou tři úrovně: Přístup původních uživatelů (Tier 1), který zahrnuje federální uživatele a pevné satelitní stanice, mají prioritu a jsou chráněni před interferencí; Přístup s prioritní licencí (PAL, Tier 2), udělovaný aukcí pro 10MHz kanály s obnovitelnými licencemi, poskytující ochranu před interferencí od nižších úrovní; a Obecně autorizovaný přístup ([GAA](/mobilnisite/slovnik/gaa/), Tier 3), který je licencován na základě pravidla a umožňuje otevřený přístup ke zbývajícímu spektru na principu „kdo dřív přijde“, ale bez ochrany před interferencí. SAS tyto úrovně vynucuje výpočtem map interferencí a úpravou parametrů CBSD v reálném čase, přičemž využívá vstupy ESC pro detekci původních uživatelů v pobřežních oblastech.

V síti 3GPP je CBRS integrován do rádiové přístupové sítě (RAN) prostřednictvím specifikací jako TS 36.744 a TS 38.873, které definují protokoly pro komunikaci CBSD-SAS, mechanismy sdílení spektra a koexistenci s rozhraními LTE a NR. Podporuje jak provoz s frekvenčním dělením ([FDD](/mobilnisite/slovnik/fdd/)), tak s časovým dělením ([TDD](/mobilnisite/slovnik/tdd/)) s konkrétními konfiguracemi kanálů a výkonovými limity. CBRS umožňuje flexibilní scénáře nasazení, jako jsou privátní průmyslové sítě, řešení neutrálních hostitelů pro areály a zhušťování mobilní sítě, tím, že poskytuje nákladově efektivní přístup ke spektru středního pásma s příznivými charakteristikami šíření.

## K čemu slouží

CBRS byl vytvořen, aby řešil nedostatek a nevyužitost spektra zavedením dynamického modelu sdílení, který umožňuje koexistenci více uživatelů v pásmu 3,5 GHz. Historicky bylo toto pásmo vyhrazeno původním federálním a satelitním uživatelům, což vedlo k neefektivnímu využití v mnoha geografických oblastech. Americká Federální komunikační komise ([FCC](/mobilnisite/slovnik/fcc/)) iniciovala CBRS, aby toto spektrum zpřístupnila pro komerční bezdrátové služby, podpořila inovace a konkurenci bez vytlačení původních uživatelů. Tím se řeší problém exkluzivního licencování, které může být nákladné a omezovat přístup, prostřednictvím flexibilnějšího, tržně řízeného přístupu.

Motivace vychází z rostoucí poptávky po bezdrátové kapacitě poháněné 5G, IoT a podnikovými aplikacemi, spolu s potřebou dostupného spektra pro nové účastníky a privátní sítě. Předchozí přístupy spoléhaly na statické alokace nebo exkluzivní licence, což bránilo rychlému nasazení a efektivnímu využití. CBRS zavádí regulační a technický rámec, který vyvažuje ochranu původních uživatelů s příležitostmi pro různé uživatele, a podporuje nasazení sítí LTE a 5G ve scénářích jako chytré továrny, kampusy a venkovský širokopásmový přístup.

Standardizací CBRS v 3GPP je zajištěna interoperabilita a globální relevance, což umožňuje výrobcům zařízení a operátorům vyvíjet kompatibilní řešení. Řeší omezení tradičního řízení spektra využitím koordinace založené na databázi ([SAS](/mobilnisite/slovnik/sas/)) a senzingu ([ESC](/mobilnisite/slovnik/esc/)), což umožňuje adaptaci v reálném čase a snižuje rizika interferencí. To vedlo k novým obchodním modelům, jako je neutrální hostitelství a spektrum jako služba, což zvyšuje flexibilitu sítí a snižuje vstupní bariéry na telekomunikačním trhu.

## Klíčové vlastnosti

- Třívrstvý model sdílení spektra (původní uživatelé, PAL, GAA) s přístupem založeným na prioritě
- Systém pro přístup ke spektru (SAS) pro centrální koordinaci a správu interferencí
- Schopnost monitorování prostředí (ESC) pro detekci a ochranu signálů původních radarů
- Podpora nasazení LTE a 5G NR ve sdíleném pásmu 3,5 GHz
- Dynamické přiřazování frekvence a výkonu pro CBSD na základě aktuálních podmínek
- Obecně autorizovaný přístup (GAA) licencovaný na základě pravidla, umožňující otevřené a flexibilní využití

## Definující specifikace

- **TS 36.744** (Rel-14) — CBRS 3.5GHz Band Specification for US
- **TS 36.755** (Rel-15) — US 600 MHz LTE Band 71 Technical Report
- **TS 36.790** (Rel-15) — LAA/eLAA for CBRS 3.5GHz Band in US
- **TS 38.873** (Rel-16) — NR Band n48 Technical Report
- **TR 38.892** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [CBRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbrs/)
