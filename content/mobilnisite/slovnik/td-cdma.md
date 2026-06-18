---
slug: "td-cdma"
url: "/mobilnisite/slovnik/td-cdma/"
type: "slovnik"
title: "TD-CDMA – Time Division - Code Division Multiple Access"
date: 2025-01-01
abbr: "TD-CDMA"
fullName: "Time Division - Code Division Multiple Access"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/td-cdma/"
summary: "Hybridní schéma mnohonásobného přístupu kombinující časový mnohonásobný přístup (TDMA) a kódový mnohonásobný přístup (CDMA). Bylo použito v režimu UTRA TDD standardu 3GPP, kde jsou uživatelské signály"
---

TD-CDMA je hybridní schéma mnohonásobného přístupu, používané v režimu UTRA TDD standardu 3GPP, kde jsou uživatelské signály odděleny jak časovými sloty, tak rozprostíracími kódy, čímž kombinuje TDMA a CDMA.

## Popis

TD-CDMA je konkrétní implementace režimu [UTRA](/mobilnisite/slovnik/utra/) (Universal Terrestrial Radio Access) s časovým duplexem ([TDD](/mobilnisite/slovnik/tdd/)), standardizovaná organizací 3GPP. Jedná se o hybridní technologii mnohonásobného přístupu, která spojuje vlastnosti [TDMA](/mobilnisite/slovnik/tdma/) a [CDMA](/mobilnisite/slovnik/cdma/). V systému TD-CDMA je rádiový zdroj rozdělen ve dvou dimenzích: čas a kód. Časová osa je rozdělena na opakující se rámce, z nichž každý je rozdělen na pevný počet časových slotů (např. 15 slotů na 10ms rámec v běžné konfiguraci). V rámci každého časového slotu může vysílat více uživatelů současně, což je komponenta CDMA. Tato simultánní vysílání jsou oddělena použitím různých ortogonálních nebo kvaziortogonálních rozprostíracích kódů. Datové symboly každého uživatele jsou násobeny (rozprostřeny) vysokorychlostním, uživatelsky specifickým rozprostíracím kódem, čímž se zvyšuje šířka pásma signálu. Přijímač použije stejný kód k desprezování a obnovení zamýšleného uživatelského signálu, zatímco signály od ostatních uživatelů (s jinými kódy) se jeví jako šum. Aspekt TDD znamená, že stejná nosná frekvence je použita pro uplink i downlink, přičemž pro každý směr jsou alokovány různé časové sloty, což umožňuje asymetrický provoz a flexibilní využití spektra. Fyzická vrstva používá na přijímací straně techniky společné detekce ke zmírnění interference mezi více uživateli ve stejném časovém slotu, což je klíčová technická výzva. TD-CDMA bylo navrženo pro provoz v nepárových kmitočtových pásmech, což jej činilo atraktivním pro operátory, kteří neměli párové spektrum pro tradiční [WCDMA](/mobilnisite/slovnik/wcdma/) [FDD](/mobilnisite/slovnik/fdd/). Jeho rámcová struktura umožňuje dynamické přidělování kanálů a podporuje proměnné datové rychlosti přiřazením více časových slotů a/nebo více kódů jednomu uživateli.

## K čemu slouží

TD-CDMA bylo vyvinuto za účelem poskytnutí řešení pro mobilní komunikaci 3. generace pro nepárové alokace spektra, což je scénář, který nebyl efektivně řešen párovým spektrem režimu [WCDMA](/mobilnisite/slovnik/wcdma/) [FDD](/mobilnisite/slovnik/fdd/). Jeho vytvoření vyřešilo problém asymetrie spektra, což umožnilo operátorům nasadit služby 3G v kmitočtových pásmech, kde nebyly k dispozici stejné párové bloky pro uplink/downlink. To bylo zvláště cenné pro nové hráče nebo regulátory se specifickou spektrální politikou. Hybridní přístup TDMA/CDMA si kladl za cíl kombinovat flexibilitu a kapacitu CDMA s jednoduchostí plánování a potenciálem koordinace interference TDMA. Historicky bylo součástí širší rodiny standardů IMT-2000, přičemž TD-CDMA (v rámci UTRA TDD) a úzce související TD-SCDMA (z Číny) představovaly TDD větev 3G. Řešilo omezení čistých TDMA systémů (omezená kapacita) a čistých CDMA systémů (složitá regulace výkonu a dýchání buňky) v určitých scénářích nasazení. Technologie byla motivována snahou o efektivní podporu asymetrického internetového provozu (kde je zátěž downlinku typicky vyšší) a potenciálně nižší náklady na infrastrukturu díky nižším požadavkům na duplexery v provozu TDD.

## Klíčové vlastnosti

- Hybridní mnohonásobný přístup kombinující časové sloty TDMA a rozprostírací kódy CDMA
- Časový duplex (TDD) na jedné nosné frekvenci
- Provoz v nepárových kmitočtových pásmech
- Podpora asymetrického uplink/downlink provozu prostřednictvím flexibilní alokace slotů
- Použití přijímačů se společnou detekcí pro potlačení interference uvnitř buňky
- Dynamické přidělování kanálů (DCA) pro efektivní správu zdrojů

## Související pojmy

- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [TD-SCDMA – Time Division Synchronous Code Division Multiple Access](/mobilnisite/slovnik/td-scdma/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)
- [UTRA – Universal Terrestrial Radio Access](/mobilnisite/slovnik/utra/)
- [Multiple Access](/mobilnisite/slovnik/multiple-access/)

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.100** (Rel-4) — UMTS Service Requirements Phase 1

---

📖 **Anglický originál a plná specifikace:** [TD-CDMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/td-cdma/)
