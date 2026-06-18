---
slug: "pg"
url: "/mobilnisite/slovnik/pg/"
type: "slovnik"
title: "PG – Processing Gain"
date: 2025-01-01
abbr: "PG"
fullName: "Processing Gain"
category: "Physical Layer"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pg/"
summary: "Processing Gain (zisk zpracování) je základním parametrem v komunikacích se šířeným spektrem, zejména ve WCDMA. Kvantifikuje poměr šířky rozprostřeného pásma k původní informační šířce pásma a poskytu"
---

PG (Processing Gain, zisk zpracování) je v systému WCDMA poměr šířky rozprostřeného pásma k původní informační šířce pásma a poskytuje míru odolnosti vůči rušení a robustnosti signálu pro výpočet rozpočtu spoje v sítích 3G UMTS.

## Popis

Processing Gain (PG, zisk zpracování) je klíčovým konceptem v systémech Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([CDMA](/mobilnisite/slovnik/cdma/)) a Wideband CDMA ([WCDMA](/mobilnisite/slovnik/wcdma/)), které tvoří základ 3G UMTS. Je definován jako poměr šířky pásma rozprostřeného signálu (rychlost čipů) k původní šířce pásma informačního signálu (bitová rychlost), často vyjádřený v decibelech jako PG (dB) = 10 * log10 (Rychlost čipů / Bitová rychlost). V režimu [UTRA](/mobilnisite/slovnik/utra/) [FDD](/mobilnisite/slovnik/fdd/) podle 3GPP je rychlost čipů pevně nastavena na 3,84 Mcps. Proto je zisk zpracování nepřímo úměrný datové rychlosti uživatele; vyšší datové rychlosti vedou k nižšímu zisku zpracování a naopak. Tento parametr přímo ovlivňuje požadovaný poměr signálu k rušení na přijímači pro úspěšnou demodulaci.

Primární mechanismus za ziskem zpracování je rozprostření datového signálu uživatele pomocí pseudonáhodného kódu s vysokou rychlostí. Toto rozprostření distribuuje energii signálu přes mnohem širší pásmo, než je původní informační šířka pásma. Na přijímači je stejný kód použit k 'složení' signálu zpět do jeho původní šířky pásma. Klíčové je, že jakékoli rušení nebo šum, které nekoreluje s tímto konkrétním rozprostíracím kódem, zůstává rozprostřeno po širokém pásmu. Operace složení tedy koncentruje výkon požadovaného signálu, zatímco výkon rušení zůstává rozprostřen, čímž efektivně zvyšuje poměr signálu k rušení ([SIR](/mobilnisite/slovnik/sir/)) pro detektor. Hodnota zisku zpracování kvantifikuje toto zlepšení SIR dosažené procesem rozprostření a složení.

V plánování sítí a řízení rádiových zdrojů je zisk zpracování klíčovým vstupem pro výpočty rozpočtu spoje. Určuje požadovaný Eb/N0 (poměr energie na bit k spektrální hustotě výkonu šumu) pro danou kvalitu služby, což následně ovlivňuje pokrytí buňky a kapacitu. Při pevné rychlosti čipů mají služby s nižší bitovou rychlostí (jako hlas) vysoký zisk zpracování, což je činí robustnějšími a umožňuje provoz ve větší vzdálenosti od základnové stanice nebo v horších podmínkách signálu. Vysokorychlostní datové služby s vyšší bitovou rychlostí a následně nižším ziskem zpracování vyžadují lepší podmínky signálu a typicky mají menší oblast pokrytí. Koncept je nedílnou součástí algoritmů řízení výkonu ve WCDMA, protože cílový SIR pro spojení je nastavován na základě požadované kvality služby a jejího inherentního zisku zpracování.

## K čemu slouží

Processing Gain (zisk zpracování) existuje jako základní konstrukční princip, který umožňuje spolehlivou komunikaci ve sdíleném spektru za vysoké úrovně rušení, což je charakteristickým rysem systémů [CDMA](/mobilnisite/slovnik/cdma/). Před CDMA používaly buněčné systémy jako GSM Time Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (TDMA) a Frequency Division Multiple Access (FDMA), které primárně oddělovaly uživatele v časových a frekvenčních slotech. Tyto systémy byly omezeny ve schopnosti zvládat rušení uvnitř stejné buňky a byly citlivé na frekvenční plánování. CDMA a koncept zisku zpracování byly zavedeny, aby umožnily všem uživatelům vysílat současně přes celé dostupné pásmo s využitím jedinečných kódů pro oddělení.

Problém, který řeší, je víceuživatelské rušení. V systému CDMA se více signálů překrývá v čase a frekvenci. Bez zisku zpracování by to vedlo k nepoužitelné úrovni šumu. Operace rozprostření, kvantifikovaná PG, poskytuje matematickou 'výhodu', která umožňuje přijímači izolovat požadovaný signál z celkového rušení. To umožňuje funkce jako měkká kapacita (postupné zhoršování s přidáváním uživatelů), frekvenční využití jedna (každá buňka používá stejnou frekvenci) a inherentní odolnost vůči úzkopásmovému rušení a vícestupňovému útlumu díky širokému pásmu. Jeho vznik byl motivován potřebou vyšší spektrální účinnosti, lepší kvality hovoru a plynulejšího přechodu k vyšším datovým rychlostem v rámci jednotného rádiového rozhraní, jak bylo zamýšleno pro sítě 3G v rámci standardu IMT-2000.

## Klíčové vlastnosti

- Definován jako poměr rychlosti čipů k informační bitové rychlosti (PG = Rychlost čipů / Bitová rychlost).
- Poskytuje kvantitativní míru schopnosti potlačení rušení v systémech se šířeným spektrem.
- Nepřímo úměrný uživatelské datové rychlosti při pevné rychlosti čipů.
- Kritický parametr pro analýzu rozpočtu spoje a plánování pokrytí v sítích WCDMA.
- Umožňuje RAKE přijímači oddělit vícecestné složky a koherentně je zkombinovat.
- Základní pro mechanismus řízení výkonu, určuje cílový poměr signálu k rušení (SIR).

## Související pojmy

- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification

---

📖 **Anglický originál a plná specifikace:** [PG na 3GPP Explorer](https://3gpp-explorer.com/glossary/pg/)
