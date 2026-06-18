---
slug: "tfci"
url: "/mobilnisite/slovnik/tfci/"
type: "slovnik"
title: "TFCI – Transport Format Combination Indicator"
date: 2025-01-01
abbr: "TFCI"
fullName: "Transport Format Combination Indicator"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tfci/"
summary: "Pole v kanálu DPCCH, které signalizuje konkrétní kombinaci transportních formátů (TF) používanou pro kanály DPDCH ve stejném CCTrCH. Umožňuje přijímači správně dekódovat data identifikací přesné multi"
---

TFCI je pole v kanálu DPCCH, které signalizuje kombinaci transportních formátů použitou pro kanály DPDCH, což umožňuje přijímači správně dekódovat data identifikací multiplexní a kódovací konfigurace vysílače.

## Popis

Indikátor kombinace transportních formátů (Transport Format Combination Indicator – TFCI) je klíčový řídicí prvek fyzické vrstvy v 3GPP UMTS ([UTRAN](/mobilnisite/slovnik/utran/)) a jeho evoluci. Přenáší se jako součást vyhrazeného fyzického řídicího kanálu (Dedicated Physical Control Channel – [DPCCH](/mobilnisite/slovnik/dpcch/)) v uplinku i downlinku. Jeho primární funkcí je explicitně signalizovat přijímači, která konkrétní kombinace transportních formátů (Transport Formats – TFs) je aktivní pro přidružené vyhrazené fyzické datové kanály (Dedicated Physical Data Channels – DPDCHs) v rámci stejného kódovaného složeného transportního kanálu (Coded Composite Transport Channel – CCTrCH) pro aktuální rádiový rámec (10 ms). Transportní formát definuje parametry jako velikost transportního bloku, počet bloků a schéma kanálového kódování pro jeden transportní kanál. Kombinace transportních formátů (Transport Format Combination – [TFC](/mobilnisite/slovnik/tfc/)) je platná sada [TF](/mobilnisite/slovnik/tf/), po jednom z každého transportního kanálu multiplexovaného do CCTrCH. Hodnota TFCI je binární kód, který přímo mapuje na jednu předem dohodnutou TFC ze sady kombinací transportních formátů (Transport Format Combination Set – [TFCS](/mobilnisite/slovnik/tfcs/)).

Po přijetí rádiového rámce fyzická vrstva extrahuje bity TFCI z DPCCH. Přijímač pak použije tuto hodnotu TFCI jako index k vyhledání odpovídající kombinace transportních formátů (TFC) v rámci TFCS, která byla nakonfigurována vyššími vrstvami ([RRC](/mobilnisite/slovnik/rrc/)) během nastavení nebo rekonfigurace rádiového nosiče. Toto vyhledání poskytne přijímači přesnou znalost o tom, kolik transportních bloků je přítomno pro každý transportní kanál, jaké jsou jejich velikosti a jaké kódovací schéma bylo použito. Tyto informace jsou naprosto nezbytné, aby přijímač mohl správně demultiplexovat, provést de-rate-matching a dekódovat datové bity na kanálech [DPDCH](/mobilnisite/slovnik/dpdch/). Bez TFCI by přijímač musel slepě zkoušet dekódování pomocí všech možných TFC, což je výpočetně neproveditelné.

Délka pole TFCI je konfigurovatelná (např. 0, 2, 3, 4, 5, 6, 7, 8, 9 nebo 10 bitů) v závislosti na velikosti TFCS. Délka TFCI 0 bitů znamená, že TFC je pevná a není třeba ji signalizovat dynamicky. Mapování mezi kódy TFCI a TFC je definováno sítí. V některých provozních režimech, jako je komprimovaný režim (compressed mode) pro měření, může TFCI nést dodatečné informace nebo se může měnit jeho interpretace. Spolehlivý přenos TFCI je prvořadý, protože jeho poškození by vedlo k úplnému selhání dekódování přidruženého datového rámce. Proto jsou samotné bity TFCI kódovány robustním (32,10) subkódem Reed-Mullerova kódu druhého řádu, aby byla zajištěna vysoká spolehlivost detekce.

## K čemu slouží

TFCI bylo zavedeno k vyřešení zásadního problému dynamického a proměnlivého přenosu dat v sítích UMTS založených na [WCDMA](/mobilnisite/slovnik/wcdma/). Na rozdíl od pevné struktury časových slotů v GSM podporuje UMTS vysoce flexibilní datové rychlosti, které se mohou měnit každých 10 ms rámec, aby odpovídaly okamžitým požadavkům služeb, jako je hlas, video nebo prohlížení webu. Této flexibility je dosaženo tím, že umožňuje multiplexovat více transportních kanálů s různými charakteristikami (např. signalizace a uživatelská data) dohromady (CCTrCH) a jejich individuální formáty se mohou měnit od rámce k rámci.

Bez explicitního indikátoru by přijímač neměl způsob, jak zjistit, která kombinace formátů byla pro daný rámec použita. Slepá detekce všech možných kombinací z potenciálně velké sady je výpočetně složitá a náchylná k chybám, zejména pro mobilní zařízení napájená baterií. TFCI poskytuje efektivní signalizační mechanismus s nízkou režií, který tuto nejednoznačnost okamžitě řeší. Umožňuje rychlou adaptaci fyzické vrstvy na měnící se podmínky provozu a požadavky QoS, což je zásadní pro podporu mixu spojově orientovaných a paketově orientovaných služeb, pro které byl UMTS navržen. TFCI je základním kamenem fyzické vrstvy WCDMA, který činí pokročilé funkce, jako jsou proměnlivé škálovací faktory (variable spreading factors), adaptivní vícerychlostní kodeky (adaptive multi-rate – AMR) a efektivní multiplexování různých logických kanálů, prakticky proveditelnými.

## Klíčové vlastnosti

- Explicitně signalizuje aktivní kombinaci transportních formátů (TFC) pro rádiový rámec
- Přenáší se jako součást vyhrazeného fyzického řídicího kanálu (DPCCH)
- Umožňuje správné demultiplexování a dekódování dat s proměnnou rychlostí na kanálech DPDCH
- Konfigurovatelná délka pole (0–10 bitů) na základě velikosti TFCS
- Kódováno robustním (32,10) kanálovým kódem pro vysokou spolehlivost
- Nezbytné pro podporu dynamického rate matchingu a operací v komprimovaném režimu (compressed mode)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.308** (Rel-19) — HSDPA Overall Description
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [TFCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tfci/)
