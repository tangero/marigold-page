---
slug: "denm"
url: "/mobilnisite/slovnik/denm/"
type: "slovnik"
title: "DENM – Decentralized Environmental Notification Message"
date: 2026-01-01
abbr: "DENM"
fullName: "Decentralized Environmental Notification Message"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/denm/"
summary: "Standardizovaná zpráva V2X používaná v buňkovém V2X (C-V2X) založeném na 3GPP pro vysílání časově citlivých bezpečnostních a dopravních informací přímo mezi vozidly a silniční infrastrukturou. Umožňuj"
---

DENM je standardizovaná zpráva typu V2X pro vysílání časově citlivých bezpečnostních a dopravních informací přímo mezi vozidly a silniční infrastrukturou v systémech C-V2X.

## Popis

Decentralized Environmental Notification Message (DENM) je základním typem zprávy definovaným 3GPP pro komunikaci Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/)), konkrétně v rámci buňkového V2X (C-V2X). Funguje primárně v decentralizovaném režimu (rozhraní PC5) C-V2X, což umožňuje uživatelským zařízením (UE), jako jsou vozidla a zařízení silniční infrastruktury ([RSU](/mobilnisite/slovnik/rsu/)), vysílat a přijímat zprávy o bezpečnostních událostech přímo přes sidelink. Tato přímá komunikace je klíčová pro dosažení velmi nízké latence (až 100 ms) vyžadované pro kooperativní povědomí a předcházení kolizím.

Z architektonického hlediska jsou generování a šíření DENM řízeny aplikační vrstvou V2X v UE za využití služeb poskytovaných podřízeným protokolovým zásobníkem 3GPP, včetně řídicí funkce V2X. DENM je spuštěna detekcí nebo předpovědí relevantní události (např. prudké brzdění, detekce překážky). Zpráva obsahuje strukturovanou sadu informačních prvků ([IE](/mobilnisite/slovnik/ie/)) vyžadovaných specifikacemi 3GPP. Mezi klíčové IE patří typ události (např. nehoda, kluzká vozovka), přesná poloha (zeměpisná délka, šířka, elipsa spolehlivosti), čas detekce, doba relevance události a volitelné podrobnosti, jako je závažnost a příčina. Zdrojové UE přiřadí každé instanci DENM jedinečný ActionID (složený z ID zdrojové stanice a čísla sekvence) pro sledování.

Po vygenerování je DENM předána protokolovým zásobníkem k přenosu přes referenční bod PC5 pomocí přidělených rádiových zdrojů (buď autonomní plánování režimu 4, nebo síťově plánované režimu 3). Strategie šíření je řízena událostmi a může být opakovaná; zdrojové UE může vysílat DENM vícekrát v rámci definované geografické oblasti (oblast relevance) a po stanovenou dobu, aby zajistilo spolehlivý příjem všemi zasaženými UE v okolí. Přijímající UE zpracují DENM, ověří její relevanci na základě polohy a obsahu a informace předají řidiči nebo je použijí v systémech automatizovaného řízení. To vytváří decentralizované povědomí o jízdním prostředí v reálném čase.

DENM hraje základní roli v ekosystému V2X 3GPP tím, že umožňuje zásadní bezpečnostní služby. Doplňuje periodickou zprávu Cooperative Awareness Message ([CAM](/mobilnisite/slovnik/cam/)), která poskytuje rutinní stavové informace, tím, že poskytuje varování spouštěná událostmi. Návrh protokolu zajišťuje, že zprávy jsou samostatné, geograficky vymezené a mohou být šířeny i při absenci pokrytí mobilní sítí (pomocí PC5 režimu 4), což je zásadní pro robustnost aplikací zajišťujících bezpečnost života.

## K čemu slouží

DENM byla vytvořena k řešení kritické potřeby okamžitého a spolehlivého šíření časově citlivých varování před hrozbami v vozidlových sítích, což je požadavek, který tradiční buňková komunikace (závislá na síťové infrastruktuře a směrování v jádru sítě) nemohla splnit kvůli inherentní latenci a možným jediným bodům selhání. Před standardizací [V2X](/mobilnisite/slovnik/v2x/) byly bezpečnostní systémy omezeny na palubní senzory (radar, kamery) s dosahem na přímou viditelnost, což vytvářelo 'mrtvý úhel' pro hrozby mimo přímou viditelnost. Motivace vychází z globálních iniciativ pro bezpečnost silničního provozu, které usilují o snížení nehod pomocí kooperativních inteligentních dopravních systémů (C-ITS).

Historický kontext zahrnuje sbližování automobilového a telekomunikačního průmyslu, které vedlo k vývoji standardů pro vyhrazenou krátkodosahovou komunikaci (DSRC) a později k integraci V2X do ekosystému 3GPP počínaje vydáním 14. DENM, formalizovaná ve vydání 15, konkrétně řeší problém událostmi řízeného, decentralizovaného oznamování. Překonává omezení zpráv závislých na infrastruktuře tím, že umožňuje přímou komunikaci UE-UE, což zajišťuje doručení varování i v odlehlých oblastech nebo při přetížení/přerušení sítě. To je prvořadé pro pokročilé asistenční systémy řidiče (ADAS) a vývoj směrem k automatizovanému řízení, kde rozhodování vozidla musí být informováno událostmi v reálném čase za hranicemi jeho bezprostředního senzorického dosahu.

Navíc DENM poskytuje standardizovaný, interoperabilní formát zprávy. Před její specifikací hrozila proprietární řešení fragmentací, která by znemožnila vozidlům různých výrobců rozumět vzájemným varováním. Definováním společné sady informačních prvků a procedur ve standardech 3GPP zajišťuje DENM globální interoperabilitu, takže jakékoli kompatibilní vozidlo nebo zařízení silniční infrastruktury může generovat a interpretovat kritické bezpečnostní informace, čímž maximalizuje efektivitu a bezpečnostní přínosy sítě V2X.

## Klíčové vlastnosti

- Generování řízené událostí pro okamžité varování před hrozbami
- Přímé vysílání přes PC5 sidelink pro komunikaci s velmi nízkou latencí
- Obsahuje strukturovaná data včetně typu události, polohy GPS a časové známky
- Podporuje geografické vymezení pomocí definované oblasti relevance pro cílené šíření
- Jedinečný ActionID pro identifikaci a sledování zprávy
- Funguje v síťově asistovaném (režim 3) i autonomním (režim 4) režimu přidělování zdrojů

## Související pojmy

- [CAM – Cooperative Awareness Message](/mobilnisite/slovnik/cam/)

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR

---

📖 **Anglický originál a plná specifikace:** [DENM na 3GPP Explorer](https://3gpp-explorer.com/glossary/denm/)
