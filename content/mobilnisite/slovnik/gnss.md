---
slug: "gnss"
url: "/mobilnisite/slovnik/gnss/"
type: "slovnik"
title: "GNSS – Global Navigation Satellite System"
date: 2026-01-01
abbr: "GNSS"
fullName: "Global Navigation Satellite System"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gnss/"
summary: "GNSS označuje satelitní konstelace poskytující globální služby určování polohy, navigace a času, jako jsou GPS, Galileo, GLONASS a BeiDou. Ve standardech 3GPP umožňuje služby založené na poloze, lokal"
---

GNSS je systém satelitních konstelací, který poskytuje uživatelským zařízením globální služby určování polohy, navigace a času, což umožňuje služby založené na poloze, lokalizaci volajícího v nouzových případech a síťově asistované určování polohy v mobilních sítích.

## Popis

Globální navigační satelitní systém (GNSS) je obecný termín zahrnující všechny satelitní systémy pro určování polohy, včetně [GPS](/mobilnisite/slovnik/gps/) (USA), Galileo (EU), [GLONASS](/mobilnisite/slovnik/glonass/) (Rusko) a BeiDou (Čína). Ve specifikacích 3GPP je GNSS integrován jako klíčová metoda pro stanovení geografické polohy uživatelského zařízení (UE). Architektura zahrnuje UE obsahující GNSS přijímač schopný zpracovávat signály z jedné nebo více satelitních konstelací. Síť může tento proces asistovat prostřednictvím řídicích nebo uživatelských protokolů pro určování polohy, jako je LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) nebo Secure User Plane Location ([SUPL](/mobilnisite/slovnik/supl/)), poskytováním pomocných dat, jako jsou efemeridy, almanach a přibližná poloha, aby se snížil čas do prvního určení polohy ([TTFF](/mobilnisite/slovnik/ttff/)) UE a zlepšila se přesnost.

Základní fungování spočívá v tom, že UE měří čas příchodu signálů z více viditelných satelitů. Výpočtem doby šíření signálu a znalostí poloh satelitů (z dekódovaných nebo sítí poskytnutých navigačních zpráv) může UE vypočítat svou vlastní trojrozměrnou polohu a přesný čas pomocí trilaterace. Mezi klíčové komponenty patří samotné satelitní konstelace, GNSS přijímač a anténa UE a síťové prvky, jako je Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5GC nebo Enhanced Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v EPS, které spravují relaci určování polohy a výpočty.

Určování polohy pomocí GNSS v 3GPP podporuje více režimů: samostatný (UE funguje nezávisle pouze pomocí satelitních signálů), asistovaný UE (UE odesílá měření síti pro výpočet polohy) a na UE založený (UE vypočítává svou vlastní polohu, případně s využitím síťových pomocných dat). Jeho role je klíčová pro nouzové služby (např. E911/E112), služby založené na poloze, zákonný odposlech, optimalizaci sítě (např. pro správu mobility) a různé IoT aplikace vyžadující sledování majetku. Specifikace podrobně popisují požadavky na výkon (přesnost, citlivost), testování a integraci s technologiemi radiového přístupu od UMTS po 5G NR.

## K čemu slouží

Primárním účelem integrace GNSS do standardů 3GPP je poskytnout spolehlivou, globálně dostupnou metodu pro určení polohy UE. Tím se řeší regulatorní požadavky na lokalizaci volajícího v nouzových případech (např. [FCC](/mobilnisite/slovnik/fcc/) E911 v USA, E112 v EU), které vyžadují, aby mobilní sítě poskytovaly přesnou polohovou informaci pro nouzová volání. Také umožňuje rozsáhlý ekosystém komerčních služeb založených na poloze (LBS), jako je navigace, správa vozového parku a aplikace využívající polohu, což vytváří nové zdroje příjmů pro operátory.

Historicky měly metody určování polohy založené pouze na buňkách, jako je Cell-ID, Enhanced Cell-ID a Observed Time Difference of Arrival (OTDOA), omezení v přesnosti, zejména ve venkovských oblastech nebo oblastech s řídkým pokrytím buněk. GNSS poskytuje lepší venkovní přesnost, často až na několik metrů, a tuto mezeru zaplňuje. Jeho zařazení počínaje 3GPP Release 7 formalizovalo podporu pro asistovaný GNSS (A-GNSS), který využívá síť k doručování pomocných dat do UE, což ve srovnání se samostatným provozem GNSS výrazně zlepšuje počáteční výkon (TTFF), citlivost (umožňuje určení polohy i při slabších signálech) a výdrž baterie UE.

Motivace přesahovala rámec compliance a služeb až k optimalizaci sítě a novým případům užití. Přesná poloha napomáhá při správě rádiových zdrojů, rozhodování o předávání hovorů a plánování sítě. Pro pozdější technologie jako V2X a IoT jsou přesné načasování a určování polohy založené na GNSS zásadní. Vývoj směrem k podpoře více konstelací (multi-GNSS) a hybridního určování polohy (kombinace GNSS s pozemskými signály) v následujících vydáních byl hnut potřebou zlepšit dostupnost, odolnost v městských kaňonech a ještě vyšší přesnost pro pokročilé aplikace, jako je autonomní řízení a průmyslová automatizace.

## Klíčové vlastnosti

- Podpora více satelitních konstelací (GPS, Galileo, GLONASS, BeiDou)
- Síťově asistovaný provoz (A-GNSS) pro zlepšení času do prvního určení polohy (TTFF) a citlivosti
- Více režimů určování polohy: Samostatný, asistovaný UE a na UE založený
- Integrace s 3GPP řídicími (LPP) a uživatelskými (SUPL) protokoly pro určování polohy
- Specifikace požadavků na výkon (např. přesnost, citlivost) pro testování shody
- Podpora hybridního určování polohy kombinujícího GNSS s pozemskými měřeními (např. OTDOA, WLAN)

## Související pojmy

- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TR 22.867** (Rel-18) — Study on 5G Smart Energy and Infrastructure
- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 22.989** (Rel-20) — FRMCS Analysis and Requirements
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TR 23.744** (Rel-17) — Location Enhancements for Mission Critical Services
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.215** (Rel-19) — UTRA FDD Measurement Definitions
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- … a dalších 46 specifikací

---

📖 **Anglický originál a plná specifikace:** [GNSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/gnss/)
