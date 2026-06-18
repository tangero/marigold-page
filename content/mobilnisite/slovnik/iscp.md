---
slug: "iscp"
url: "/mobilnisite/slovnik/iscp/"
type: "slovnik"
title: "ISCP – Interference on Signal Code Power"
date: 2025-01-01
abbr: "ISCP"
fullName: "Interference on Signal Code Power"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/iscp/"
summary: "Interference on Signal Code Power (ISCP, rušení na výkonu signálového kódu) je klíčové rádiové měření v UMTS (WCDMA), které kvantifikuje celkovou přijatou hustotu výkonu v šířce pásma kanálu, s výjimk"
---

ISCP je měření v rádiovém rozhraní UMTS, které kvantifikuje celkovou přijatou hustotu výkonu interference a šumu v kanálu, s výjimkou signálu obsluhované buňky; používá se pro výpočet SIR a rozhodování o řízení výkonu.

## Popis

Interference on Signal Code Power (ISCP, rušení na výkonu signálového kódu) je základní rádiové měření definované ve specifikacích 3GPP pro systémy UMTS/[WCDMA](/mobilnisite/slovnik/wcdma/). Jedná se o měření spektrální hustoty výkonu (vyjádřené v dBm/3,84 MHz) přijatého širokopásmového výkonu v rámci šířky pásma odpovídající čipové rychlosti 3,84 MHz, po descramblování pomocí scrambling kódu obsluhující buňky, ale před despreidingem pomocí kanalizačního kódu konkrétního fyzického kanálu. V podstatě ISCP představuje výkon interference pozorovaný v signálové cestě konkrétní buňky, zahrnující šum a interferenci z jiných buněk, od jiných uživatelů ve stejné buňce (intrabuněčná interference) a z externích zdrojů.

Technicky ISCP měří uživatelské zařízení (UE) na downlinku a Node B na uplinku. Pro downlink UE měří ISCP na společném pilotním kanálu ([CPICH](/mobilnisite/slovnik/cpich/)) nebo jiných vyhrazených fyzických kanálech. Proces měření zahrnuje naladění na frekvenci, aplikaci scrambling kódu buňky k izolaci jejího signálového prostoru a následné měření výkonu přijatého signálu před aplikací ortogonálního kanalizačního kódu. Protože kanalizační kódy jsou ortogonální, výkon nezarovnaný s požadovaným kódem se jeví jako interference. Tato naměřená hodnota je ISCP. Je to kritický vstup pro výpočet poměru signálu k interferenci ([SIR](/mobilnisite/slovnik/sir/)), kde SIR = [RSCP](/mobilnisite/slovnik/rscp/) / ISCP (s odpovídajícím škálováním jednotek). RSCP (Received Signal Code Power) je výkon požadovaného signálu.

Z architektonického hlediska jsou měření ISCP hlášena UE do [UTRAN](/mobilnisite/slovnik/utran/) (Universal Terrestrial Radio Access Network) prostřednictvím zpráv Measurement Report jako součást protokolu Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Tyto reporty využívají algoritmy správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) sítě. Mezi klíčové funkce RRM, které spoléhají na ISCP, patří rychlé řízení výkonu, řízení předávání spojení a řízení přístupu. Pro vnitřní smyčku řízení výkonu na uplinku Node B průběžně měří SIR (pomocí přijatého výkonu signálu a ISCP) UE a odesílá příkazy řízení vysílacího výkonu ([TPC](/mobilnisite/slovnik/tpc/)), aby udržel cílový SIR, což přímo potlačuje útlum a interferenci.

Jeho role je ústřední pro povahu WCDMA omezenou interferencí. Na rozdíl od GSM, které je omezeno šumem, je kapacita UMTS primárně limitována interferencí. Přesné měření ISCP umožňuje síti dynamicky vyhodnocovat prostředí interference. Pro rozhodování o předání spojení UE hlásí ISCP (často jako součást měření kvality, jako je Ec/No, což je RSCP/ISCP) pro sousední buňky spolu s RSCP. To pomáhá síti vybrat cílovou buňku nejen na základě síly signálu, ale i kvality signálu vzhledem k místní interferenci. ISCP poskytuje pohled v reálném čase na 'znečištění' v rádiovém prostředí, což síti umožňuje činit inteligentní rozhodnutí pro zachování kvality hovoru a maximalizaci systémové kapacity.

## K čemu slouží

ISCP bylo zavedeno jako základní měření pro UMTS/WCDMA k řešení zásadní výzvy řízení sítě, kde všichni uživatelé sdílejí stejné frekvenční pásmo a jsou odděleni kódy. V takovém systému s mnohonásobným přístupem s kódovým dělením (CDMA) je signál každého uživatele interferencí pro všechny ostatní uživatele. Tradiční měření síly signálu (jako RSSI v GSM) byla nedostatečná, protože nerozlišovala mezi výkonem požadovaného signálu a rušivým výkonem ve stejném kanálu. Hlavní problém, který ISCP řeší, je poskytnutí kvantifikovatelného měření této úrovně interference, což je nezbytné pro řízení výkonu a stabilitu systému.

Historický kontext představuje přechod od systémů TDMA/FDMA (jako GSM) k širokopásmovému CDMA pro 3G. V GSM se kapacita přidávala novými frekvencemi nebo časovými sloty. Ve WCDMA je kapacita měkkým zdrojem omezeným celkovou interferencí. Pokud interference příliš vzroste, všechny spojení se zhorší. Proto bylo nutné přesné a rychlé měření interference (ISCP) k implementaci rychlé uzavřené smyčky řízení výkonu, která je charakteristickým znakem WCDMA. Toto řízení výkonu zajišťuje, že každé UE vysílá minimálním nezbytným výkonem pro udržení spojení, čímž minimalizuje svůj příspěvek k celkové interferenci vnímané ostatními – koncept známý jako průměrování interference.

Vznik ISCP byl motivován potřebou měření, které přímo vstupuje do výpočtu SIR, což je klíčová metrika pro kvalitu spoje v CDMA systému. Odstranilo omezení spočívající v absenci přímého měření interference pro systémy se sdílenou šířkou pásma. Tím, že poskytuje složku interference, umožňuje ISCP síti provádět přesná předání spojení k buňkám s lepšími podmínkami poměru signálu k interferenci, nejen se silnějšími signály, čímž se zlepšuje míra ztráty hovorů a celkový výkon sítě v prostředích s vysokou interferencí, jako jsou okraje buněk nebo husté městské oblasti. Je to základní metrika pro RRM, která umožňuje efektivní fungování systémů WCDMA.

## Klíčové vlastnosti

- Měří spektrální hustotu výkonu interference v rámci šířky pásma WCDMA kanálu
- Klíčová složka pro výpočet poměru signálu k interferenci (SIR)
- Používá se pro algoritmy rychlého řízení výkonu ve vnitřní a vnější smyčce
- Hlášeno UE do UTRAN pro rozhodování o předání spojení a správě zdrojů
- Rozlišuje interferenci od výkonu požadovaného signálu (RSCP)
- Základní měření pro systémy CDMA omezené interferencí

## Související pojmy

- [RSCP – Reference Signal Carrier Phase](/mobilnisite/slovnik/rscp/)
- [SIR – Signal-to-Interference Ratio](/mobilnisite/slovnik/sir/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.215** (Rel-19) — UTRA FDD Measurement Definitions
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.865** (Rel-10) — Distributed Antenna Enhancements for TDD
- **TS 25.866** (Rel-9) — 1.28Mcps TDD Home NodeB Study Report
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 32.405** (Rel-19) — UTRAN Performance Measurements Specification
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview

---

📖 **Anglický originál a plná specifikace:** [ISCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/iscp/)
