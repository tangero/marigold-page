---
slug: "ncr"
url: "/mobilnisite/slovnik/ncr/"
type: "slovnik"
title: "NCR – Network Status Continuous Report Request"
date: 2026-01-01
abbr: "NCR"
fullName: "Network Status Continuous Report Request"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ncr/"
summary: "Funkce správy sítě, která vyžaduje průběžné hlášení informací o stavu sítě od uživatelského zařízení (UE). Umožňuje sledování rádiových podmínek, mobilních událostí a metrik výkonu v reálném čase. Tat"
---

NCR je požadavek správy sítě na průběžné hlášení informací o stavu sítě od uživatelského zařízení, který umožňuje sledování v reálném čase pro optimalizaci a řešení problémů.

## Popis

Network Status Continuous Report Request (NCR, požadavek na průběžné hlášení stavu sítě) je mechanismus správy sítě zavedený ve specifikaci 3GPP Release 13, který umožňuje síti vyžádat si od uživatelského zařízení (UE) průběžné hlášení různých parametrů stavu. Funguje v rámci řídicí roviny, typicky je iniciován systémem správy sítě nebo entitami pro provoz, správu a údržbu (OAM). NCR umožňuje sběr dat v reálném čase o rádiových podmínkách, mobilních událostech a výkonu UE, která jsou přenášena do sítě k analýze. Tato funkce je součástí širších rámců samoorganizujících se sítí (SON) a minimalizace jízdních testů ([MDT](/mobilnisite/slovnik/mdt/)) a jejím cílem je automatizace optimalizace sítě a snížení provozních nákladů.

Z architektonického hlediska NCR zahrnuje interakce mezi systémem OAM, rádiovou přístupovou sítí (RAN) a UE. Síť odešle zprávu s požadavkem NCR na UE, ve které specifikuje parametry k hlášení, jako je přijatý výkon referenčního signálu (RSRP), přijatá kvalita referenčního signálu (RSRQ), identity buněk a časové informace. UE následně tyto parametry průběžně monitoruje a odesílá hlášení zpět do sítě v definovaných intervalech nebo při spouštěcích událostech. Hlášení jsou agregována a zpracovávána systémy správy sítě za účelem získání přehledu o výkonu sítě, problémech s pokrytím a interferenčních vzorcích.

Fungování NCR zahrnuje několik kroků: nejprve síť nakonfiguruje UE pomocí kritérií pro hlášení prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) nebo řídicích protokolů. UE přejde do režimu průběžného hlášení a shromažďuje data na základě těchto kritérií. Hlášení jsou formátována podle určených šablon a přenášena pomocí zavedených signalizačních kanálů, často využívají stávající mechanismy hlášení měření, ale s rozšířenou kontinuitou. Síť tato data používá pro účely jako optimalizace pokrytí, ladění parametrů předávání spojení a identifikace selhání rádiového spoje. NCR podporuje jak režim hlášení s ukládáním do logu, tak okamžité hlášení, v závislosti na požadavcích sítě.

Klíčové komponenty zahrnují konfigurační parametry NCR, spouštěče hlášení a datové struktury pro zapouzdření informací o stavu. Mechanismus se integruje se stávajícími postupy měření a hlášení v LTE a NR a rozšiřuje je o průběžné monitorování iniciované sítí. Hraje klíčovou roli při umožnění proaktivní správy sítě, což operátorům umožňuje detekovat a řešit problémy dříve, než ovlivní uživatele. Poskytnutím standardizovaného způsobu sběru dat na straně UE zvyšuje NCR efektivitu procesů optimalizace sítě.

## K čemu slouží

NCR bylo vytvořeno, aby řešilo potřebu sledování stavu sítě v reálném čase a průběžně z perspektivy UE, což tradiční jízdní testy a periodické hlášení nemohly plně uspokojit. Předchozí přístupy, jako manuální jízdní testy, byly nákladné, časově náročné a poskytovaly pouze momentková data. NCR umožňuje automatizovaný a průběžný sběr dat, čímž řeší problémy související s dynamickými síťovými podmínkami a sporadickými problémy, které by přerušovaná měření mohla minout. Podporuje vývoj směrem k samooptymalizujícím sítím tím, že poskytuje bohatou datovou sadu pro analýzy a automatizaci.

Historický kontext zahrnuje snahu o SON a [MDT](/mobilnisite/slovnik/mdt/) v rámci 3GPP, jejichž cílem bylo snížit provozní náklady a zlepšit výkon sítě. NCR navazuje na dřívější funkce MDT tím, že umožňuje průběžné hlášení iniciované sítí, namísto spoléhání se pouze na měření spouštěná UE nebo ukládaná do logu. Tím řeší omezení předchozích metod, které často měly mezery v pokrytí dat nebo vyžadovaly spolupráci UE pouze během specifických událostí. NCR zajišťuje, že operátoři mají stabilní proud informací pro průběžnou optimalizaci.

Motivace pro NCR zahrnuje rostoucí složitost sítí s hustým nasazením a heterogenním prostředím, kde je průběžné monitorování nezbytné pro udržení kvality služeb. Řeší výzvy při detekci přechodných problémů, optimalizaci parametrů mobility a zlepšování uživatelského zážitku v reálném čase. Integrací s řídicími systémi usnadňuje NCR rozhodování založené na datech a podporuje pokročilé případy užití, jako je prediktivní údržba a optimalizace sítě založená na umělé inteligenci.

## Klíčové vlastnosti

- Umožňuje průběžné hlášení stavu iniciované sítí od UE
- Podporuje hlášení RSRP, RSRQ, identifikátorů buněk a mobilních událostí
- Integruje se s rámci MDT a SON pro automatizaci
- Poskytuje jak okamžité, tak režimy hlášení s ukládáním do logu
- Konfigurovatelné prostřednictvím signalizace RRC pro flexibilní sběr parametrů
- Zlepšuje sledování sítě v reálném čase a řešení problémů

## Související pojmy

- [MDT – Minimization of Drive Tests](/mobilnisite/slovnik/mdt/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 28.313** (Rel-20) — Management and orchestration; SON for 5G networks
- **TS 28.658** (Rel-19) — E-UTRAN NRM IRP Information Service
- **TR 28.841** (Rel-18) — Technical Report on IoT NTN Enhancements
- **TS 29.153** (Rel-19) — Ns Reference Point Protocol between SCEF and RCAF
- **TS 32.511** (Rel-19) — ANR Management Concepts & Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.114** (Rel-19) — EMC Requirements for NR Repeaters and NCR
- **TS 38.115** (Rel-19) — NR Repeater RF Conformance Testing Part 1
- **TS 38.201** (Rel-19) — NR Physical Layer General Description
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [NCR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ncr/)
