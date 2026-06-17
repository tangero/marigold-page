---
slug: "ffs"
url: "/mobilnisite/slovnik/ffs/"
type: "slovnik"
title: "FFS – For Further Specification"
date: 2025-01-01
abbr: "FFS"
fullName: "For Further Specification"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ffs/"
summary: "Zápis používaný v technických specifikacích 3GPP k označení, že konkrétní technický detail, parametr nebo chování ještě není dokončeno a bude definováno v budoucí verzi specifikace nebo v samostatném"
---

FFS je zápis v dokumentaci 3GPP, který označuje, že technický detail ještě není dokončen a bude definován později.

## Popis

For Further Specification (FFS) je základní administrativní a procedurální zápis v technických specifikacích (TS) a technických zprávách (TR) 3GPP. Není to síťová funkce, protokol nebo rozhraní, ale značka používaná autory specifikací. Když pracovní skupina narazí na technický aspekt, který vyžaduje další studium, čeká na zpětnou vazbu z implementace nebo je závislý na rozhodnutí jiné skupiny, označí jej jako FFS. Tím explicitně signalizuje, že současný text je neúplný a detail je záměrně ponechán otevřený.

Používání FFS se řídí pravidly pro tvorbu specifikací 3GPP. Obvykle se aplikuje na parametry, procedury, pole zpráv, algoritmy nebo dokonce celé funkční popisy. Přítomnost FFS vytváří otevřený problém nebo "zástupný symbol", který musí být vyřešen, než může specifikace dosáhnout stabilního, implementovatelného stavu. Vyřešení položky FFS zahrnuje technickou diskusi, vytváření konsenzu v příslušné pracovní skupině a nakonec dohodu na konkrétním textu, který nahradí značku FFS. Tento text je pak začleněn do pozdější verze stejné specifikace nebo v některých případech do jiné, odkazované specifikace.

Z architektonické a implementační perspektivy má FFS významný dopad. Výrobci zařízení a operátoři sítí čtoucí specifikaci musí identifikovat všechny značky FFS, aby pochopili mezery a rizika v technologii. FFS u kritického parametru může oddálit vývoj produktu nebo vést k prozatímním proprietárním řešením. Proces řešení položek FFS je jádrem iterativního pracovního postupu standardizace, který zajišťuje, že specifikace dospějí z vysokoúrovňových rámců k detailním, jednoznačným plánům pro interoperabilní zařízení. Jeho použití pokrývá všechny domény 3GPP, od radiového přístupu (např. specifikace řady 36) po core síť (řada 29) a bezpečnost (řada 33), jak naznačuje jeho výskyt v desítkách specifikačních dokumentů napříč releasy.

## K čemu slouží

FFS existuje, aby umožnil pragatický a paralelní vývoj složitých telekomunikačních standardů. Specifikace 3GPP vytváří více pracovních skupin současně, pokrývajících různé části systému (rádio, core, protokoly, testování). Není možné dokončit každý drobný detail v jediném kroku. FFS poskytuje formální mechanismus pro pokrok celkového rámce specifikace, přičemž uznává a sleduje nevyřešené technické body.

Tím se řeší problém uváznutí specifikace. Bez FFS by práce na široké části specifikace zcela zastavila, dokud by nebyla dohodnuta každá drobnost, což by drasticky zpomalilo pokrok. Použitím FFS mohou skupiny zachytit architektonické dohody a většinu toku procedury, přičemž konkrétní hodnoty nebo algoritmické detaily ponechají pro pozdější vyřešení na základě výsledků simulací, implementačních zkušeností nebo sladění s jinými skupinami. Přímo řeší výzvu řízení vzájemné závislosti mezi různými částmi rozsáhlého, systémového standardu. Historicky byl tento zápis nezbytný od prvních releasů 3GPP (R99) dále, což umožnilo rychlý vývoj základních specifikací, jako je protokol [RRC](/mobilnisite/slovnik/rrc/) (25.331), přičemž určité parametry byly ponechány pro pozdější doladění.

## Klíčové vlastnosti

- Zástupný symbol v textu specifikace 3GPP označující nedefinované detaily
- Používá se ke správě otevřených problémů a sledování nevyřešených technických bodů
- Umožňuje paralelní vývoj částí specifikace bez plného konsenzu na všech detailech
- Musí být vyřešeno předtím, než je specifikace považována za stabilní a implementovatelnou
- Aplikuje se na parametry, procedury, formáty zpráv a algoritmy
- Dokumentováno ve stovkách specifikací 3GPP ze všech domén

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TS 22.057** (Rel-19) — Mobile Execution Environment (MExE) Stage 1
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 22.112** (Rel-8) — USAT Gateway System Specification
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.240** (Rel-19) — 3GPP Generic User Profile (GUP) Architecture
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements
- **TS 25.153** (Rel-19) — LCR TDD Repeater RF Requirements & Testing
- … a dalších 48 specifikací

---

📖 **Anglický originál a plná specifikace:** [FFS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ffs/)
