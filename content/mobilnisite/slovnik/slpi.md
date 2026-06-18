---
slug: "slpi"
url: "/mobilnisite/slovnik/slpi/"
type: "slovnik"
title: "SLPI – Service Logic Program Instance"
date: 2025-01-01
abbr: "SLPI"
fullName: "Service Logic Program Instance"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/slpi/"
summary: "Běhová instance programu servisní logiky (Service Logic Program, SLP) v architektuře CAMEL (Customised Applications for Mobile network Enhanced Logic). Vykonává servisní logiku pro služby s přidanou h"
---

SLPI je běhová instance programu servisní logiky (Service Logic Program) v architektuře CAMEL, která vykonává servisní logiku pro konkrétní relaci účastníka a umožňuje tak služby s přidanou hodnotou, jako je předplacené volání nebo přesměrování hovorů.

## Popis

Instance programu servisní logiky (Service Logic Program Instance, SLPI) je základním konceptem v architektuře [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile network Enhanced Logic) standardizované 3GPP, což je standard inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) pro mobilní sítě. SLPI je konkrétní, aktivní instance programu servisní logiky ([SLP](/mobilnisite/slovnik/slp/)), která je vytvořena pro obsluhu konkrétní servisní relace účastníka. Když účastník aktivuje službu založenou na CAMEL (např. uskuteční předplacený hovor), CAMEL Service Environment ([CSE](/mobilnisite/slovnik/cse/)) v síti pro tuto relaci vytvoří SLPI. Tato instance obsahuje informace o běhovém stavu a vykonává servisní logiku definovanou v SLP, což je v podstatě softwarový program řídící chování služby. SLPI komunikuje s hlavními entitami mobilní sítě, jako je [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre) nebo [SGSN](/mobilnisite/slovnik/sgsn/) (Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node), prostřednictvím zpráv protokolu CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)). Činí rozhodnutí na základě servisní logiky, například kontroluje stav účtu, uplatňuje zákaz hovorů nebo upravuje směrování hovoru. SLPI zůstává aktivní po dobu trvání servisní relace, zpracovává události jako přijetí hovoru, ukončení spojení nebo změnu polohy, a je ukončena po dokončení relace. Současně může existovat více instancí SLPI pro různé účastníky nebo i pro různé relace stejného účastníka. Tento model umožňuje škálovatelné, na účastníka specifické vykonávání komplexní servisní logiky bez nutnosti úprav jádrových síťových ústředen, naplňující tak princip IN oddělení řízení služeb od přepojování.

## K čemu slouží

Koncept SLPI byl vytvořen jako součást standardu CAMEL za účelem umožnění nasazení operátorsky specifických služeb s přidanou hodnotou standardizovaným a na dodavateli nezávislým způsobem napříč sítěmi GSM a později UMTS. Před koncepty CAMEL a IN byly pokročilé služby typicky pevně zakódovány v síťových ústřednách (MSC), což jejich vytváření, úpravy a rychlé nasazování velmi ztěžovalo. To brzdilo inovace a vedlo k závislosti na konkrétním dodavateli. CAMEL zavedl architekturu řízení služeb, kde servisní logika sídlí v samostatném uzlu (CSE), a SLPI je dynamický vykonávací mechanismus této logiky pro každou relaci účastníka. Tím se řeší problém poskytování služeb v reálném čase a personalizovaných služeb, jako je předplacené účtování, virtuální privátní sítě (VPN) a filtrování hovorů. SLPI umožňuje síti udržovat stav relace, komunikovat s externími databázemi (např. s fakturačním systémem) a řídit hovor/relaci na základě vlastní logiky. Její vytvoření bylo motivováno potřebou konkurenční diferenciace služeb, kratší doby uvedení nových služeb na trh a podpory pokročilých funkcí, jako je bezproblémový roaming služeb. Abstrahuje vykonávání služeb od podkladové síťové hardwarové vrstvy a poskytuje tak operátorům flexibilní a výkonnou platformu.

## Klíčové vlastnosti

- Běhová instance programu servisní logiky (SLP) pro konkrétní relaci účastníka
- Udržuje stav relace a vykonává servisní logiku CAMEL
- Komunikuje s hlavními síťovými uzly (MSC, SGSN) prostřednictvím protokolu CAP
- Umožňuje řízení v reálném čase pro služby jako předplacené volání, řízení hovorů a VPN
- Vytvářena a spravována prostředím CAMEL Service Environment (CSE)
- Poskytuje standardizovaný model pro vykonávání služeb inteligentní sítě v mobilních sítích

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification

---

📖 **Anglický originál a plná specifikace:** [SLPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/slpi/)
