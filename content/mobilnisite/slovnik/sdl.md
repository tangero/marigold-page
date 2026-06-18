---
slug: "sdl"
url: "/mobilnisite/slovnik/sdl/"
type: "slovnik"
title: "SDL – Specification and Description Language"
date: 2025-01-01
abbr: "SDL"
fullName: "Specification and Description Language"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sdl/"
summary: "Formální, grafický jazyk standardizovaný ITU-T (řada Z.100) pro specifikaci složitých, událostmi řízených, reálného času a distribuovaných systémů. V rámci specifikací 3GPP se používá k jednoznačně př"
---

SDL je formální, grafický jazyk standardizovaný ITU-T pro specifikaci složitých, událostmi řízených systémů, používaný v 3GPP k definici protokolů a stavových automatů s jednoznačnou přesností.

## Popis

Specification and Description Language (SDL) je formální, objektově orientovaný, grafický modelovací jazyk standardizovaný Mezinárodní telekomunikační unií ([ITU-T](/mobilnisite/slovnik/itu-t/)) v řadě Z.100. V kontextu standardizace 3GPP se SDL používá k poskytnutí rigorózních, jednoznačných specifikací komunikačních protokolů, systémových procedur a chování stavových automatů. Jeho primární role spočívá v definici dynamického chování systémů se zaměřením na posloupnost událostí, výměnu zpráv a stavové přechody, které nastávají v reakci na podněty. Tento formální přístup odstraňuje nejednoznačnosti vlastní textu v přirozeném jazyce, čímž snižuje riziko chybného výkladu a implementačních chyb napříč různými dodavateli zařízení a síťovými operátory.

SDL modeluje systém jako sadu souběžných procesů, které komunikují asynchronně prostřednictvím signálů. Jazyk používá hierarchickou strukturu, počínaje blokovým diagramem systému, který definuje celkový systém a jeho komunikační kanály. Tento systém je rozložen na bloky, které jsou dále upřesněny na procesy. Každý proces je definován pomocí rozšířených konečných automatů (EFSM), reprezentovaných SDL diagramy procesů. Tyto diagramy se skládají ze stavů, vstupů (spouštěcí signály), výstupů (odeslané signály), úloh (interní akce), rozhodnutí a procedur. Jazyk podporuje datové typy, proměnné, časovače a vytváření nových instancí signálů, což umožňuje specifikaci složitých interakcí reálného času, které se vyskytují v telekomunikačních protokolech.

V technických specifikacích 3GPP (TS) jsou SDL diagramy často poskytovány jako normativní přílohy doplňující textové popisy protokolů. Například SDL je hojně používáno ve specifikacích signalizačních protokolů vrstvy 3 jak v jádru sítě (Core Network), tak v rádiové přístupové síti (Radio Access Network), jako jsou procedury Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) a Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Schopnost jazyka přesně definovat časovače, formáty zpráv a podmíněné chování je klíčová pro testování interoperability a certifikaci shody. Poskytnutím vizuálního a formálního modelu slouží SDL jako klíčový nástroj pro protokolové inženýry, vývojáře testů a systémové architekty k pochopení, implementaci a ověření správného fungování systémů 3GPP.

## K čemu slouží

Primárním účelem SDL v rámci 3GPP je dosažení jednoznačné a přesné specifikace složitých, reaktivních systémů. Telekomunikační protokoly zahrnují složité posloupnosti zpráv, časovačů a stavově závislého chování. Popis těchto aspektů pouze v přirozeném jazyce může vést k mnohoznačnému výkladu, což způsobuje problémy s interoperabilitou mezi zařízeními od různých výrobců. SDL tento problém řeší poskytnutím formálního grafického zápisu, který definuje chování s matematickou přesností, a zajišťuje, že všichni implementátoři odvozují ze specifikace stejný logický model.

Historicky, jak se mobilní systémy vyvíjely od 2G přes 3G (UMTS) dále, složitost protokolů dramaticky vzrostla. Zavedení paketově orientovaných domén, sofistikovaného řízení mobility a mechanismů kvality služeb vyžadovalo robustnější metodiku specifikace. SDL, jako standard [ITU-T](/mobilnisite/slovnik/itu-t/) již používaný v jiných telekomunikačních oblastech, bylo přijato, aby přineslo tuto přesnost do 3GPP. Řeší problém nejednoznačnosti specifikace, který je hlavní příčinou chyb a zpoždění při nasazování více-dodavatelských sítí.

Navíc modely SDL nejsou pouze dokumentací; lze je použít pro simulaci, validaci a dokonce jako základ pro automatické generování testů. To umožňuje standardizačním orgánům a výrobcům zařízení ověřit logickou konzistenci specifikace protokolu před jejím dokončením a vyvinout komplexní testovací sady. Účel SDL se tedy rozšiřuje nad rámec statické specifikace a aktivně přispívá ke zlepšení kvality, spolehlivosti a zkrácení doby uvedení na trh u produktů vyhovujících 3GPP.

## Klíčové vlastnosti

- Formální grafický zápis založený na rozšířených konečných automatech (EFSM)
- Podpora souběžných procesů komunikujících prostřednictvím asynchronních signálů
- Hierarchická dekompozice systému (System, Block, Process)
- Integrované datové modelování s abstraktními datovými typy a proměnnými
- Explicitní modelování časovačů, časových limitů a omezení reálného času
- Možnost generovat spustitelný kód nebo simulační modely ze specifikací

## Související pojmy

- [ITU-T – International Telecommunication Union Telecommunication Standardization Sector](/mobilnisite/slovnik/itu-t/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.801** (Rel-19) — 3GPP Specification Drafting Rules
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 36.113** (Rel-19) — EMC Requirements for E-UTRA Base Stations
- **TS 36.761** (Rel-15) — Extended-Band 12 Study Report
- **TS 36.858** (Rel-14) — LTE 2.6 GHz SDL Band Technical Report
- **TS 36.895** (Rel-13) — 700 SDL Band for LTE Carrier Aggregation
- **TS 37.814** (Rel-12) — L-band Supplemental Downlink for UTRA/E-UTRA
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.113** (Rel-19) — NR Base Station EMC Specification
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [SDL na 3GPP Explorer](https://3gpp-explorer.com/glossary/sdl/)
