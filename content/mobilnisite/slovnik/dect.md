---
slug: "dect"
url: "/mobilnisite/slovnik/dect/"
type: "slovnik"
title: "DECT – Digital Enhanced Cordless Telecommunications"
date: 2026-01-01
abbr: "DECT"
fullName: "Digital Enhanced Cordless Telecommunications"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dect/"
summary: "DECT je standardizovaná digitální rádiová technologie pro bezšňůrovou hlasovou a datovou komunikaci, původně vyvinutá pro domácí a firemní bezšňůrové telefony. V rámci 3GPP byla integrována, aby umožn"
---

DECT je standardizovaná digitální rádiová technologie pro bezšňůrovou hlasovou a datovou komunikaci, původně určená pro bezšňůrové telefony, která byla integrována do 3GPP pro konvergenci pevných a mobilních sítí a jako alternativní rádiová přístupová technologie.

## Popis

DECT je rádiová technologie založená na přístupu s časovým dělením (TDMA) a duplexu s časovým dělením (TDD), která primárně pracuje v kmitočtovém pásmu 1880-1900 MHz v Evropě a v podobných pásmech po celém světě. Architektura systému se skládá z pevných částí (Fixed Parts - [FP](/mobilnisite/slovnik/fp/)), což jsou základnové stanice připojené k síti, a přenosných částí (Portable Parts - PP), což jsou mobilní telefony nebo terminály. Rozhraní využívá strukturu multiframe s rámci o délce 10 ms rozdělenými na 24 časových slotů, přičemž 12 slotů je přiděleno pro přenosy ve směru dolní (downlink, FP k PP) a 12 pro přenosy ve směru horní (uplink, PP k FP), což umožňuje plně duplexní komunikaci.

Na fyzické vrstvě DECT používá modulaci s Gaussovským frekvenčním klíčováním (GFSK) s roztečí kanálů 1,728 MHz, což v jeho standardním pásmu poskytuje 10 rádiových kmitočtových kanálů. Systém podporuje dynamický výběr a přidělování kanálů, kdy přenosné části průběžně skenují nejlepší dostupný kanál, minimalizují tak rušení a umožňují efektivní opakované využití kmitočtů. Každý časový slot může přenášet 32 kbps hlasových dat pomocí adaptivní diferenciální pulzně kódové modulace ([ADPCM](/mobilnisite/slovnik/adpcm/)) nebo paketová data pro služby jako fax, modemová komunikace a omezený přístup k internetu.

Protokolový zásobník zahrnuje fyzickou vrstvu (PHY), vrstvu řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)), vrstvu řízení datového spoje ([DLC](/mobilnisite/slovnik/dlc/)) a síťovou vrstvu (NWK). Vrstva MAC se zabývá přidělováním kanálů, multiplexováním a šifrováním, zatímco vrstva DLC řídí opravu chyb a řízení toku. Síťová vrstva poskytuje řízení hovoru, správu mobility a doplňkové služby. DECT podporuje jak okruhově přepínané hlasové služby, tak paketově orientované datové služby prostřednictvím svých profilů pro spolupráci, což umožňuje integraci s různými sítěmi včetně PSTN, [ISDN](/mobilnisite/slovnik/isdn/) a IP sítí.

V kontextu 3GPP byl DECT standardizován jako alternativní rádiová přístupová technologie, aby umožnil konvergenci pevných a mobilních sítí, což dovoluje systémům DECT propojovat se s mobilními sítěmi. Tato integrace byla specifikována prostřednictvím profilu pro spolupráci DECT/UMTS (DECT/UP) a pozdějších vylepšení pro interoperabilitu se službami založenými na IMS. Technologie poskytuje místní pokrytí s typickými dosahy 50-300 metrů uvnitř budov a až několik kilometrů venku s vhodnými anténními systémy, což ji činí vhodnou pro rezidenční, podnikové a veřejné přístupové aplikace.

## K čemu slouží

DECT byl původně vyvinut koncem 80. a začátkem 90. let 20. století jako evropský standard pro nahrazení analogových bezšňůrových telefonních systémů, které trpěly špatnou kvalitou hlasu, omezenou kapacitou a bezpečnostními slabinami. Cílem technologie bylo poskytnout digitální kvalitu hlasové komunikace se zvýšenou bezpečností prostřednictvím šifrování, lepší spektrální účinností díky digitální modulaci a podporou vyšších hustot uživatelů v domácím a firemním prostředí. Na rozdíl od mobilních systémů navržených pro pokrytí široké oblasti byl DECT optimalizován pro bezšňůrovou komunikaci v místní oblasti s plynulým předáváním hovoru mezi základnovými stanicemi v rámci areálu.

Integrace DECT do standardů 3GPP počínaje Release 4 řešila rostoucí potřebu konvergence pevných a mobilních sítí, což umožnilo uživatelům plynule přecházet mezi mobilními sítěmi a bezšňůrovými systémy. To bylo zvláště cenné v podnikovém prostředí, kde zaměstnanci mohli používat jediný telefon pro mobilní hovory mimo budovu i pro hovory založené na DECT uvnitř kancelářských prostor, což snižovalo náklady a zlepšovalo uživatelský zážitek. Standardizace také umožnila DECT vyvíjet se nad rámec jednoduchých hlasových služeb a podporovat datové aplikace a připojení k internetu.

Poskytnutím standardizované, interoperabilní bezšňůrové technologie DECT vyřešil problém proprietárních bezšňůrových systémů, které spolu nemohly komunikovat a měly omezenou funkčnost. Efektivní využití nelicencovaného spektra (ve většině regionů), nízká spotřeba energie a podpora šifrování hlasu učinily tuto technologii atraktivní pro spotřebitelské i podnikové aplikace. Její integrace do 3GPP umožnila telekomunikačním operátorům nabízet konvergované služby a poskytla výrobcům jasnou cestu migrace pro vývoj bezšňůrové technologie souběžně s mobilními systémy.

## Klíčové vlastnosti

- Rádiový přístup TDMA/TDD s 24 časovými sloty na 10 ms rámec
- Dynamický výběr a přidělování kanálů pro vyhýbání se rušení
- Modulace GFSK s roztečí kanálů 1,728 MHz
- Podpora okruhově přepínaných hlasových služeb (32 kbps ADPCM) a paketových datových služeb
- Šifrování a autentizace pro zabezpečenou komunikaci
- Plynulé předávání hovoru mezi základnovými stanicemi v rámci místních pokrytí

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework

---

📖 **Anglický originál a plná specifikace:** [DECT na 3GPP Explorer](https://3gpp-explorer.com/glossary/dect/)
