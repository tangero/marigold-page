---
slug: "iut"
url: "/mobilnisite/slovnik/iut/"
type: "slovnik"
title: "IUT – Implementation Under Test"
date: 2025-01-01
abbr: "IUT"
fullName: "Implementation Under Test"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/iut/"
summary: "IUT označuje konkrétní implementaci standardu 3GPP, která je předmětem testování za účelem ověření shody a interoperability. Jde o klíčový koncept v testování shody a výkonu, který zajišťuje, že síťov"
---

IUT (Implementace podrobená testování) je konkrétní implementace standardu 3GPP, která prochází testováním za účelem ověření shody a interoperability při testování shody a výkonu.

## Popis

Implementation Under Test (IUT) je termín používaný v procesech testování a certifikace 3GPP k označení konkrétní implementace standardizovaného protokolu, rozhraní nebo funkčnosti, která je podrobována testům. Definován v různých specifikacích, jako jsou TS 21.905, TS 23.237 a TS 38.523, IUT představuje entitu – ať už hardwarovou, softwarovou nebo jejich kombinaci – která je hodnocena, aby byla zajištěna její shoda se standardy 3GPP. Funguje v rámci testovací architektury, která typicky zahrnuje testovací systémy, simulátory a měřicí nástroje, jež interagují s IUT za účelem ověření jejího chování vůči předdefinovaným testovacím případům. IUT může být síťový prvek (např. základnová stanice, uzel jádra sítě), uživatelské zařízení (např. smartphone, IoT modul) nebo podsystém implementující specifické protokoly, jako je [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum) nebo [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control). Z hlediska fungování je IUT izolována v řízeném testovacím prostředí, kde testovací zařízení vysílá podněty (např. signalizační zprávy, datové pakety) a pozoruje odpovědi IUT. Tento proces kontroluje shodu s technickými specifikacemi 3GPP a pokrývá aspekty, jako je správnost protokolů, výkonnostní metriky, bezpečnostní funkce a interoperabilita s jinými implementacemi. Klíčovými součástmi tohoto rámce jsou Testovací systém (který generuje testovací scénáře), Bod řízení a pozorování (PCO) pro monitorování interakcí a referenční implementace nebo simulátory, které emulují partnerské entity. Role IUT v síťovém ekosystému je klíčová pro zajištění toho, aby nasazené zařízení fungovalo spolehlivě a interoperabilně v prostředí více dodavatelů, a snižovala tak riziko selhání sítě nebo zhoršení služeb. Testovací fáze zahrnující IUT sahají od testování shody (ověřování dodržování standardů) přes testování výkonu (hodnocení propustnosti, latence) až po testování interoperability (zajištění kompatibility se zařízeními jiných výrobců). V průběhu vydání standardů 3GPP se koncept IUT rozšířil o nové technologie, jako jsou LTE, 5G NR a síťové segmenty (network slicing), přičemž testovací specifikace byly aktualizovány, aby pokryly pokročilé funkce, jako je agregace nosných, massive [MIMO](/mobilnisite/slovnik/mimo/) a ultra-spolehlivá komunikace s nízkou latencí (URLLC). Důkladné testování IUT je základem kvality a stability mobilních sítí, podporuje zavádění inovativních služeb při zachování zpětné kompatibility.

## K čemu slouží

Koncept IUT existuje, aby poskytl standardizovaný rámec pro testování implementací specifikací 3GPP, a řešil tak kritickou potřebu shody a interoperability v mobilních sítích více dodavatelů. Byl motivován složitostí mobilních standardů a rizikem odlišných implementací, které by mohly vést k selhání sítě, bezpečnostním narušením nebo špatné uživatelské zkušenosti. Historicky, jak se mobilní sítě vyvíjely od 2G přes 3G a dále, rozšíření výrobců zařízení a poskytovatelů služeb vyžadovalo důkladné testování, aby bylo zajištěno, že všechny komponenty spolupracují bez problémů bez ohledu na výrobce. Omezení předchozích ad-hoc testovacích přístupů zahrnovala nekonzistentní testovací metodologie a nedostatečné pokrytí, což mohlo vést ke zpožděním nasazení nebo nákladným problémům v provozu. Rámec IUT tyto problémy řeší definováním jasných testovacích postupů a kritérií, což umožňuje výrobcům ověřit své produkty před uvedením na trh a operátorům ověřit zařízení během nákupu. Podporuje globální charakter mobilních komunikací tím, že usnadňuje certifikační programy (např. [GCF](/mobilnisite/slovnik/gcf/), PTCRB), které se při udělování schválení pro zařízení a síťové prvky spoléhají na testování IUT. Vytvoření konceptu IUT v rámci 3GPP, s kořeny v dřívějších standardizačních snahách, bylo hnací silou požadavku průmyslu na spolehlivost a kvalitu, což zajišťuje, že inovace jako vysokorychlostní přenos dat, připojení IoT a síťové segmenty mohou být s důvěrou nasazovány v heterogenních prostředích.

## Klíčové vlastnosti

- Označuje implementaci testovanou na shodu se standardy 3GPP
- Pokryta v několika specifikacích (např. TS 21.905, TS 38.523)
- Používá se při testování shody, výkonu a interoperability
- Podporuje testování síťových prvků, zařízení a protokolů
- Umožňuje validaci v řízených testovacích prostředích se simulátory
- Klíčová pro interoperabilitu více dodavatelů a certifikaci

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 23.831** (Rel-10) — Enhancements to IMS Service Continuity
- **TS 23.838** (Rel-9) — IMS Service Continuity and Inter-UE Transfer Enhancements
- **TS 26.237** (Rel-19) — IMS for PSS and MBMS Control
- **TS 26.851** (Rel-11) — Enhancements to Multimedia (EMM) for PSS, MMS, MBMS
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 31.122** (Rel-18) — USIM Conformance Test Specification
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TS 51.010** (Rel-19) — SIM Application Toolkit Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [IUT na 3GPP Explorer](https://3gpp-explorer.com/glossary/iut/)
