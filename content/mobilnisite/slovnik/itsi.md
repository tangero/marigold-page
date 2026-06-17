---
slug: "itsi"
url: "/mobilnisite/slovnik/itsi/"
type: "slovnik"
title: "ITSI – Individual TETRA Subscriber Identity"
date: 2026-01-01
abbr: "ITSI"
fullName: "Individual TETRA Subscriber Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/itsi/"
summary: "Jedinečný identifikátor účastníka (uživatele nebo zařízení) v síti TETRA (Terrestrial Trunked Radio). Jedná se o klíčovou identitu používanou pro autentizaci, správu mobility a směrování hovorů v syst"
---

ITSI je jedinečný identifikátor účastníka v síti TETRA, používaný pro autentizaci, správu mobility a směrování hovorů v těchto profesionálních a bezpečnostních systémech.

## Popis

Individual TETRA Subscriber Identity (ITSI) je základní, globálně jedinečný identifikátor přidělený každému koncovému zařízení (Terminal Equipment, TE) nebo mobilní stanici (Mobile Station, [MS](/mobilnisite/slovnik/ms/)) v síti Terrestrial Trunked Radio (TETRA). Je primárním klíčem pro správu účastníka, obdobně jako [IMSI](/mobilnisite/slovnik/imsi/) ve veřejných celulárních sítích. ITSI je trvale uložen v SIM kartě účastníka (TETRA Subscriber Identity Module, TSIM) a síť jej používá k identifikaci a autentizaci účastníka během procedur připojení, aktualizace polohy a sestavování hovorů. Je nezbytný pro všechny funkce správy mobility, což umožňuje domácí databázi (Home Database, HDB) a navštívené databázi (Visited Database, VDB) sledovat stav účastníka a jeho lokalizační oblast.

Z architektonického hlediska se ITSI používá na mnoha rozhraních a v síťových prvcích systému TETRA. Při počátečním přístupu k síti představuje MS své ITSI přepínací a řídicí infrastruktuře (Switching and Management Infrastructure, SwMI). SwMI, konkrétně Autentizační centrum (Authentication Centre, AuC) a domácí databáze, použije ITSI k získání autentizačních údajů a profilu služeb účastníka. Identita je strukturována tak, aby nesla konkrétní informace: zahrnuje mobilní kód země (Mobile Country Code, [MCC](/mobilnisite/slovnik/mcc/)), mobilní kód sítě (Mobile Network Code, [MNC](/mobilnisite/slovnik/mnc/)) identifikující operátora TETRA sítě a jedinečné číslo účastníka. Tato struktura umožňuje mezinárodní roaming mezi TETRA sítěmi. Všechny signalizační zprávy týkající se registrace, zabezpečení a mobility účastníka jsou korelovány pomocí ITSI.

Klíčové komponenty, které s ITSI interagují, zahrnují mobilní stanici, TETRA SIM, základnovou stanici, řídicí uzly SwMI a různé databáze (HDB, VDB). Jeho role je klíčová pro zabezpečení; ITSI je primárním vstupem pro proces autentizace a dohody o klíči v TETRA (TETRA authentication and key agreement, TAKA), který generuje sezení klíčů pro šifrování hlasového a datového provozu. Dále, pro skupinovou komunikaci – která je charakteristickým znakem TETRA – síť používá ITSI jednotlivých členů ke správě skupinové příslušnosti a dispečerských hovorů. Identita zůstává aktivní po dobu trvání vztahu účastníka se sítí a je ústřední pro účtování, zákonné odposlechy a veškerou logiku služeb specifických pro účastníka.

## K čemu slouží

ITSI byl vytvořen jako součást standardu TETRA (vyvinutého [ETSI](/mobilnisite/slovnik/etsi/)) za účelem poskytnutí robustní, bezpečné a škálovatelné metody pro identifikaci účastníků v systémech profesionální mobilní rádiové komunikace (Professional Mobile Radio, PMR). Před standardizovanými trunkovanými systémy, jako je TETRA, mnoho soukromých mobilních rádiových systémů používalo jednoduché, nejedinečné identifikátory nebo identifikátory flotil, které byly nedostatečné pro rozsáhlé, bezpečné a interoperabilní sítě. Omezení těchto přístupů zahrnovala nedostatek inherentní ochrany proti klonování, nepodporu národního nebo mezinárodního roamingu a těžkopádnou správu jednotlivých účastníků ve velkých organizacích. Koncepce TETRA pro veřejnou bezpečnost a kritickou komunikaci vyžadovala jedinečnou, proti manipulaci odolnou identitu.

Motivace pro ITSI vycházela z potřeby integrovat správu účastníků podobnou celulárním sítím do trunkovaného rádiového systému optimalizovaného pro kritickou hlasovou a datovou komunikaci. Řeší problém jedinečné identifikace každého uživatelského zařízení napříč potenciálně propojenými sítěmi provozovanými různými operátory, což umožňuje funkce jako bezpečná autentizace, individuální účtování a podrobné protokolování hovorů pro účely odpovědnosti. Jeho vytvoření bylo hnáno požadavkem na systém, který by mohl podporovat desítky tisíc uživatelů – jako jsou policie, hasiči a záchranná služba – se zaručeným přístupem a zabezpečením, kde je identita komunikujícího stejně důležitá jako samotná komunikace. ITSI tvoří základ, na kterém jsou bezpečně vybudovány a spravovány pokročilé funkce TETRA, jako je skupinový hovor, tísňový hovor a přímý režim provozu.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro účastníka TETRA
- Bezpečně uložen v TETRA SIM (TSIM)
- Používán jako primární klíč pro autentizaci účastníka a generování šifrovacích klíčů
- Umožňuje správu mobility jednotlivého účastníka a roaming
- Strukturován s MCC a MNC pro mezinárodní provoz
- Základní pro sestavování individuálních hovorů a správu členství ve skupinách

## Definující specifikace

- **TS 23.282** (Rel-20) — MCData Functional Architecture & Info Flows
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems

---

📖 **Anglický originál a plná specifikace:** [ITSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/itsi/)
