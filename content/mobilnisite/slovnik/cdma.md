---
slug: "cdma"
url: "/mobilnisite/slovnik/cdma/"
type: "slovnik"
title: "CDMA – Code Division Multiple Access"
date: 2025-01-01
abbr: "CDMA"
fullName: "Code Division Multiple Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cdma/"
summary: "CDMA je metoda přístupu k rádiovému kanálu používaná v celulárních sítích 2G a 3G, kde více uživatelů současně sdílí stejné frekvenční pásmo. Každému uživateli přiřazuje unikátní ortogonální kódy pro"
---

CDMA je metoda přístupu k rádiovému kanálu pro sítě 2G a 3G, při které více uživatelů sdílí stejnou frekvenci současně díky použití unikátních ortogonálních kódů pro oddělení jejich signálů.

## Popis

Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (CDMA) je metoda vícenásobného přístupu s rozprostřeným spektrem, která je základem standardů 2G cdmaOne (IS-95) a 3G CDMA2000. Funguje na principu umožňujícím více vysílačům současně přenášet informace přes jeden komunikační kanál. Toho je dosaženo rozprostřením signálu každého uživatele přes širší šířku pásma pomocí unikátního pseudonáhodného rozprostíracího kódu. V přijímači je požadovaný signál obnoven korelací přijatého složeného signálu se stejným specifickým kódem, zatímco signály od ostatních uživatelů se jeví jako nízká úroveň šumu díky ortogonalitě nebo nízké vzájemné korelaci kódů. Tento proces je znám jako despreading (sbíhání spektra).

Z architektonického hlediska se síť založená na CDMA skládá z mobilních stanic ([MS](/mobilnisite/slovnik/ms/)), základnových převodových stanic ([BTS](/mobilnisite/slovnik/bts/)), řadičů základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) a mobilní ústředny ([MSC](/mobilnisite/slovnik/msc/)). Rádiové rozhraní je charakterizováno použitím přímé sekvence s rozprostřeným spektrem (DSSS). Mezi klíčové komponenty fyzické vrstvy patří Walshovy kódy pro kanálizaci (zajišťující ortogonalitu mezi uživateli na dopředném spoji) a dlouhé pseudonáhodné ([PN](/mobilnisite/slovnik/pn/)) sekvence pro skramblování a identifikaci uživatele. Řízení výkonu je kritický podsystém, který neustále upravuje vysílací výkon mobilní stanice, aby všechny signály dorazily k základnové stanici s téměř stejným výkonem, čímž zmírňuje problém blízký-vzdálený a maximalizuje kapacitu.

V síti je úlohou CDMA poskytnout základní rádiový spoj pro hlasové a datové služby. Její inherentní vlastnosti, jako je faktor frekvenčního opakování 1 (každá buňka používá stejnou frekvenci), měkký předávání hovoru (soft handoff, kdy mobil komunikuje s více buňkami během přechodu) a odolnost vůči vícecestnému útlumu pomocí RAKE přijímačů, přímo přispívají ke zvýšené spektrální účinnosti, kvalitě hovoru a síťové kapacitě. Tyto technické atributy z ní učinily konkurenceschopnou a robustní alternativu k převládající technologické cestě GSM/Time Division Multiple Access ([TDMA](/mobilnisite/slovnik/tdma/)) v 90. letech a na počátku 21. století.

## K čemu slouží

CDMA byla vyvinuta za účelem řešení kapacitních a kvalitativních omezení analogových systémů první generace (např. AMPS) a raných digitálních celulárních systémů, jako je GSM, které používaly [FDMA](/mobilnisite/slovnik/fdma/) a TDMA. Primární motivací bylo dosáhnout vyšší spektrální účinnosti, což umožňuje obsloužit více uživatelů ve stejném přiděleném rádiovém spektru. Předchozí přístupy přidělovaly uživatelům oddělené frekvenční výseky nebo časové sloty, což stanovovalo pevné limity kapacity a vyžadovalo pečlivé frekvenční plánování, aby se zabránilo ko-kanálovému rušení mezi buňkami.

CDMA tyto problémy vyřešila tím, že umožnila všem uživatelům obsadit celé frekvenční pásmo po celou dobu, přičemž se odlišovali pouze kódy. To poskytlo statistické zisky multiplexování, inherentní utajení díky pseudonáhodným kódům a zlepšený výkon v prostředích s vícecestným šířením. Historicky byl její vývoj poháněn vojenským výzkumem komunikací s rozprostřeným spektrem, který byl pro komerční využití adaptován společností Qualcomm. Schopnost technologie zvládat měkké kapacitní limity (kdy se kvalita postupně zhoršuje s přidáváním dalších uživatelů, namísto tvrdého blokování) a její elegantní podpora měkkého předávání hovoru byly klíčovými výhodami, které motivovaly její standardizaci a rozšířené nasazení, zejména v Severní Americe a částech Asie, což vedlo k rodině standardů cdmaOne a CDMA2000.

## Klíčové vlastnosti

- Přenos s rozprostřeným spektrem využívající pro každého uživatele unikátní pseudonáhodné kódy
- Univerzální frekvenční opakování (faktor opakování 1) napříč všemi buňkami
- Důmyslné rychlé a uzavřené smyčkové řízení výkonu pro zmírnění problému blízký-vzdálený
- Schopnost měkkého předávání hovoru (soft handoff) pro plynulou mobilitu mezi buňkami
- RAKE přijímač pro kombinaci vícecestných složek signálu a potlačení útlumu
- Statistické multiplexování umožňující flexibilní kompromis mezi kapacitou a kvalitou signálu

## Související pojmy

- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.100** (Rel-4) — UMTS Service Requirements Phase 1
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview

---

📖 **Anglický originál a plná specifikace:** [CDMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdma/)
