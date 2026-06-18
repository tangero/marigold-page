---
slug: "pich"
url: "/mobilnisite/slovnik/pich/"
type: "slovnik"
title: "PICH – Paging Indication Channel"
date: 2025-01-01
abbr: "PICH"
fullName: "Paging Indication Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pich/"
summary: "Downlinkový fyzický kanál v UMTS (WCDMA) používaný k efektivnímu upozornění uživatelského zařízení (UE) na příchozí pagingové zprávy. Nese Paging Indicators (PI), které upozorňují UE v idle nebo conne"
---

PICH je downlinkový fyzický kanál v UMTS, který přenáší Paging Indicators (indikátory volání) k upozornění uživatelského zařízení (UE) na příchozí pagingové zprávy, čímž umožňuje úsporu energie tím, že je navádí ke čtení Paging Channel.

## Popis

Paging Indication Channel (PICH) je pevně daný downlinkový fyzický kanál definovaný v rozhraní UMTS (Universal Mobile Telecommunications System) [WCDMA](/mobilnisite/slovnik/wcdma/), poprvý specifikovaný ve 3GPP Release 99. Je to vyhrazený řídicí kanál, jehož jediným účelem je přenášet Paging Indicators ([PI](/mobilnisite/slovnik/pi/)). Tyto indikátory jsou krátké signály, které informují konkrétní uživatelské zařízení (UE) nebo skupinu UE, že pro ně je určena pagingová zpráva na přidruženém Secondary Common Control Physical Channel ([S-CCPCH](/mobilnisite/slovnik/s-ccpch/)), který nese transportní kanál Paging Channel ([PCH](/mobilnisite/slovnik/pch-text-pch/)). PICH je vždy svázán s konkrétním S-CCPCH.

Architektonicky je PICH vysílán Node B (základnovou stanicí) na downlinku. Sám nenese data ani zprávy vyšších vrstev. Místo toho používá sekvenci binárních symbolů (Paging Indicators), které jsou rozprostřeny specifickým kanalizačním kódem a zakódovány primárním scrambling kódem buňky. Rámcová struktura PICH je synchronizována s 10ms rádiovým rámcem. V rámci tohoto rámce je určitý počet bitů (např. 288 bitů pro spreading faktor 256) alokován pro přenos více Paging Indicators. Každý PI je krátký, opakovaný bitový vzor. Přítomnost nebo nepřítomnost specifického PI vzoru na předem určené pozici říká UE, zda potřebuje dekódovat [PCH](/mobilnisite/slovnik/pch/) v odpovídajícím rámci.

Princip fungování je klíčový pro mechanismus úspory energie UE zvaný Discontinuous Reception ([DRX](/mobilnisite/slovnik/drx/)). Místo neustálého monitorování vysokokapacitního PCH pro možné pagingové zprávy – což by vybíjelo baterii – se UE probouzí pouze v konkrétních, předem definovaných pagingových okamžicích. V těchto okamžicích se UE nejprve naladí na PICH a zkontroluje svůj přiřazený Paging Indicator. PI pro UE je určen vzorcem používajícím jeho International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)) a další systémové parametry. Pokud UE detekuje svůj PI nastavený na '1' (což indikuje volání), pokračuje v dekódování přidruženého S-CCPCH, aby přijala celou pagingovou zprávu na PCH. Pokud je PI '0', může se UE okamžitě vrátit do spánkového stavu a šetřit tak energii.

Klíčové komponenty zahrnují algoritmus mapování PI, časový vztah mezi rámcem PICH a rámcem PCH (PICH je vysílán s pevným předstihem před odpovídajícím blokem PCH) a parametry DRX cyklu vysílané v systémové informaci. Role PICH je kritická pro síťově iniciované nastavení hovoru, doručování [SMS](/mobilnisite/slovnik/sms/) a další procedury správy mobility, jako jsou aktualizace lokální oblasti. Efektivně spravuje rádiové zdroje tím, že se vyhýbá zbytečnému dekódování PCH pro všechna UE, a výrazně snižuje spotřebu energie UE, což je zásadní požadavek pro mobilní zařízení. Jeho specifikace jsou podrobně popsány v 3GPP TS 25.211 (fyzické kanály), TS 25.213 (spreading a modulace), TS 25.133 (požadavky) a dalších.

## K čemu slouží

PICH byl vytvořen, aby vyřešil kritický problém spotřeby baterie UE v idle módu v sítích UMTS WCDMA. V dřívějších celulárních systémech mohly být pagingové mechanismy méně efektivní a vyžadovaly, aby UE naslouchala pagingovým kanálům častěji. PICH umožňuje vysoce efektivní schéma nespojitého příjmu (DRX). Použitím jednoduchého indikačního kanálu s nízkou režií mohou UE rychle zjistit, zda je třeba zpracovat úplnou pagingovou zprávu, což jim umožňuje trávit většinu času v nízkopříkonovém spánkovém stavu.

Jeho zavedení v UMTS Release 99 bylo motivováno potřebou lepší energetické účinnosti pro podporu delší výdrže baterie očekávané u 3G telefonů, zejména když začaly podporovat více 'vždy zapnutých' aplikací. PICH řeší omezení, kdy UE musí nepřetržitě dekódovat pagingový kanál vyšší vrstvy. Odděluje funkci upozornění (PICH) od funkce přenosu zpráv (PCH), čímž optimalizuje jak využití energie, tak využití downlinkových kódových zdrojů.

Historický kontext zahrnuje jeho návrh jako součást struktury společných kanálů fyzické vrstvy WCDMA. Poskytuje škálovatelný způsob volání více UE bez nutnosti věnovat významné kódové nebo výkonové zdroje samotnému procesu upozornění. PICH řeší výzvu efektivního řízení volání pro velkou populaci idle UE v buňce, což je zásadní pro správu mobility a doručování hovorů. Je klíčovým prvkem pro procedury idle módu UE, přímo ovlivňujícím výdrž ve standby režimu a celkový uživatelský zážitek.

## Klíčové vlastnosti

- Pevně daný downlinkový fyzický kanál přenášející binární Paging Indicators (PI)
- Umožňuje úsporu energie UE prostřednictvím nespojitého příjmu (DRX)
- Vždy asociován s konkrétním S-CCPCH nesoucím Paging Channel (PCH)
- UE-specifický PI odvozený z IMSI pro cílená pagingová upozornění
- Jednoduchá detekce umožňuje UE rychle se rozhodnout, zda číst PCH, nebo se vrátit do spánku
- Rámcová struktura synchronizovaná s 10ms rádiovým rámcem a specifický časový posun vůči PCH

## Související pojmy

- [PCH – Paging Channel](/mobilnisite/slovnik/pch/)
- [DRX – Discontinuous Reception](/mobilnisite/slovnik/drx/)
- [S-CCPCH – Secondary Common Control Physical Channel](/mobilnisite/slovnik/s-ccpch/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.367** (Rel-19) — Home NodeB Mobility Procedures
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [PICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pich/)
