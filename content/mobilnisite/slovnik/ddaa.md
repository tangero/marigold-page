---
slug: "ddaa"
url: "/mobilnisite/slovnik/ddaa/"
type: "slovnik"
title: "DDAA – Direct Detect And Avoid"
date: 2025-01-01
abbr: "DDAA"
fullName: "Direct Detect And Avoid"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ddaa/"
summary: "DDAA je mechanismus 3GPP, který umožňuje uživatelskému zařízení (UE) přímo detekovat a vyhýbat se rušení od nesatelitních sítí (NTN), zejména satelitních systémů. Umožňuje UE autonomně vyhledávat a zm"
---

DDAA je mechanismus 3GPP, který umožňuje uživatelskému zařízení přímo detekovat a autonomně se vyhýbat rušení od nesatelitních sítí, jako jsou satelity, a zajišťovat tak koexistenci ve sdíleném spektru.

## Popis

Direct Detect And Avoid (DDAA) je standardizovaná funkce zavedená ve specifikaci 3GPP Release 18 pro správu rušení rádiových kmitočtů v integrovaných prostředích pozemních a nesatelitních sítí ([NTN](/mobilnisite/slovnik/ntn/)). Funguje na vrstvě radiového přístupu UE a umožňuje zařízení provádět autonomní snímání spektra za účelem identifikace potenciálního rušení od signálů NTN, jako jsou signály z družic na nízké oběžné dráze ([LEO](/mobilnisite/slovnik/leo/)) nebo stanic na vysoké nadmořské výšce ([HAPS](/mobilnisite/slovnik/haps/)). Po detekci může UE zahájit procedury vyhýbání, jako je úprava svých vysílacích parametrů nebo přechod na alternativní zdroje, aby zabránila škodlivému rušení přijímače NTN a udržela si vlastní kvalitu komunikace.

Architektura DDAA zahrnuje vylepšení fyzické vrstvy a vrstvy řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) v UE. UE je vybaveno senzorickými schopnostmi pro monitorování konkrétních kmitočtových pásem na přítomnost signálů NTN s využitím předdefinovaných detekčních prahů a vzorů specifikovaných sítí. gNodeB (gNB) konfiguruje parametry DDAA prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/), včetně okamžiků snímání, měřicích mezer a kritérií pro hlášení. UE hlásí detekční události nebo výsledky měření gNB, který pak může koordinovat přidělování zdrojů nebo rozhodnutí o předání spojení za účelem zmírnění rušení.

Klíčové součásti zahrnují senzorickou funkci DDAA, která využívá pokročilé algoritmy zpracování signálu k odlišení rušení NTN od jiných rádiových signálů, a mechanismus vyhýbání, který může zahrnovat dynamický výběr kmitočtu, řízení výkonu nebo plánování v časové doméně. Řízení rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) v UE je rozšířeno o podporu měření a rozhodnutí souvisejících s DDAA. Tato funkčnost je klíčová pro režimy sdílení spektra, jako jsou ty definované pro pásmo 3,5 GHz nebo jiná sdílená pásma, kde musí pozemní sítě chránit provoz NTN před škodlivým rušením.

Úloha DDAA v síti spočívá v umožnění efektivní koexistence bez nutnosti neustálé síťové koordinace pro každou událost rušení. Ve srovnání s centralizovanými schématy správy rušení snižuje signalizační režii a latenci. Tím, že dává UE přímé detekční schopnosti, může síť dosáhnout pružnějšího a škálovatelnějšího zmírňování rušení, což podporuje bezproblémovou integraci služeb NTN do ekosystému 5G a dále.

## K čemu slouží

DDAA bylo vytvořeno, aby řešilo rostoucí potřebu sdílení spektra mezi pozemními 5G sítěmi a vznikajícími nesatelitními sítěmi ([NTN](/mobilnisite/slovnik/ntn/)), jako jsou satelitní komunikační systémy. S rostoucí poptávkou po bezdrátové šířce pásma regulační orgány podporují sdílené využívání kmitočtových pásem pro maximalizaci spektrální účinnosti. Přijímače NTN, zejména na satelitech, jsou však vysoce citlivé na rušení od pozemních přenosů. Tradiční správa rušení se spoléhá na síťovou koordinaci, která může být pomalá, neefektivní a nedostatečná pro dynamická prostředí NTN, kde se pozice satelitů rychle mění.

Předchozí přístupy, jako jsou geografické vylučovací zóny nebo statické limity výkonu, byly příliš konzervativní a snižovaly kapacitu pozemní sítě. Vyžadovaly také rozsáhlou koordinaci prostřednictvím databází a nemohly se přizpůsobit změnám v provozu NTN v reálném čase. DDAA tyto omezení řeší tím, že umožňuje UE přímo vyhledávat signály NTN a autonomně se vyhýbat způsobení rušení. Tento dynamický přístup umožňuje agresivnější opakované využití spektra při současném zajištění ochrany služeb NTN, což je v souladu s vizí 3GPP pro integrovaný přístup a přenosovou síť ([IAB](/mobilnisite/slovnik/iab/)) a nesatelitní sítě v 5G-Advanced.

Motivace pro DDAA vychází z práce 3GPP na standardizaci NTN, kde jsou mechanismy koexistence nezbytné pro komerční nasazení. Podporuje regulační požadavky na zmírňování rušení ve sdílených pásmech, jak je identifikováno ITU a národními úřady. Tím, že poskytuje standardizovanou metodu pro přímou detekci a vyhýbání, DDAA usnadňuje globální interoperabilitu a snižuje složitost nasazení pro operátory zavádějící jak pozemní, tak nesatelitní sítě.

## Klíčové vlastnosti

- Autonomní vyhledávání signálů rušení NTN prováděné uživatelským zařízením (UE)
- Konfigurovatelné detekční prahy a vzory prostřednictvím signalizace RRC
- Podpora detekce pásmově vlastního a sousedního kanálového rušení
- Dynamické mechanismy vyhýbání včetně úpravy kmitočtových a časových zdrojů
- Snížená signalizační režie ve srovnání s centralizovanou koordinací
- Vylepšená koexistence pro sdílení spektra mezi pozemními a NTN systémy

## Definující specifikace

- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 24.577** (Rel-19) — A2X Services in 5GS
- **TS 24.578** (Rel-19) — UE policies for A2X services in 5GS

---

📖 **Anglický originál a plná specifikace:** [DDAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ddaa/)
