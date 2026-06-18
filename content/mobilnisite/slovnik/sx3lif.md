---
slug: "sx3lif"
url: "/mobilnisite/slovnik/sx3lif/"
type: "slovnik"
title: "SX3LIF – Split X3 LI Interworking Function"
date: 2025-01-01
abbr: "SX3LIF"
fullName: "Split X3 LI Interworking Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sx3lif/"
summary: "Funkční entita, která umožňuje zákonné odposlechy (LI) v sítích s rozdělenou architekturou, konkrétně mezi řídicí rovinou (CP) a uživatelskou rovinou (UP). Funguje jako zprostředkovatel, který shromaž"
---

SX3LIF je funkční entita, která umožňuje zákonné odposlechy v sítích s rozdělenou architekturou tím, že shromažďuje a koreluje informace z řídicí a uživatelské roviny pro doručení orgánům činným v trestním řízení.

## Popis

Funkce pro spolupráci zákonných odposlechů v rozdělené architektuře X3 (SX3LIF) je standardizovaná síťová funkce zavedená pro podporu zákonných odposlechů ([LI](/mobilnisite/slovnik/li/)) v moderních architekturách 3GPP, kde jsou řídicí a uživatelská rovina odděleny, jako je například 5G Core (5GC) s architekturou založenou na službách ([SBA](/mobilnisite/slovnik/sba/)). Jejím hlavním úkolem je fungovat jako mediační a doručovací funkce, která komunikuje jak s funkcemi řídicí roviny ([CP](/mobilnisite/slovnik/cp/)), tak s funkcemi uživatelské roviny ([UP](/mobilnisite/slovnik/up/)), aby získávala informace související s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) a obsah komunikace ([CC](/mobilnisite/slovnik/cc/)). SX3LIF je definována v technických specifikacích, jako je 29.244 (pro protokol) a 33.107 (pro celkovou architekturu a požadavky LI). V podstatě implementuje rozhraní X3 v kontextu rozdělené architektury.

Z architektonického hlediska se SX3LIF nachází v doméně síťového operátora, komunikuje na jedné straně s funkcemi CP (jako je [SMF](/mobilnisite/slovnik/smf/) nebo [AMF](/mobilnisite/slovnik/amf/)) a funkcemi UP (jako je UPF) a na druhé straně s monitorovacím zařízením orgánů činných v trestním řízení (LEMF). Přijímá spouštěče odposlechů a data prostřednictvím interních rozhraní (např. od SMF přes rozhraní založené na službách nebo od UPF přes rozhraní N4). SX3LIF je zodpovědná za korelaci IRI (metadat o komunikaci, jako jsou identity, čas a umístění) přijatých z CP s odpovídajícím CC (skutečným hlasovým, datovým nebo signalizačním obsahem) přijatým z UP. Tato korelace je klíčová pro poskytnutí kompletního záznamu odposlechu LEMF.

Provozně, po aktivaci příkazu k zákonnému odposlechu pro cílovou identitu, je příslušná funkce CP nakonfigurována tak, aby hlásila IRI do SX3LIF. Současně SX3LIF instruuje příslušnou funkci UP, aby duplikovala a přeposílala uživatelský provoz cíle (CC). SX3LIF poté tento kombinovaný informace naformátuje, zabalí a zašifruje podle standardizovaných formátů (jako jsou standardy ETSI) a bezpečně je doručí přes standardizované rozhraní X3 jednomu nebo více LEMF. Zpracovává administrativní funkce, jako je správa více současných odposlechů, udržování zabezpečených asociací a zajištění spolehlivého doručení zachycených dat se zachováním pořadí, a to vše při zachování utajení aktu odposlechu.

## K čemu slouží

SX3LIF byla vytvořena, aby řešila specifické výzvy implementace zákonných odposlechů v sítích nové generace, které využívají oddělení řídicí a uživatelské roviny (CUPS). Tradiční monolitické síťové architektury měly integrované schopnosti LI, ale oddělení CP a UP v architekturách, jako je 5GC a vyvinuté EPC, vytvořilo technickou mezeru. V rozdělené architektuře jsou IRI a CC generovány a dostupné v různých logických uzlech (CPF a UPF), což vyžaduje specializovanou funkci pro shromažďování, korelaci a doručení těchto oddělených informací.

Její zavedení ve verzi 14 bylo motivováno požadavky regulatorní shody, které ukládají síťovým operátorům povinnost poskytovat schopnosti LI bez ohledu na podkladovou síťovou architekturu. SX3LIF řeší problém, jak efektivně a standardně zprostředkovávat komunikaci mezi novými, disagregovanými síťovými funkcemi a stávajícími standardizovanými rozhraními pro předání LI (jako je X3). Zajišťuje, že orgány činné v trestním řízení nadále dostávají konzistentní, korelovaný proud dat z odposlechů, aniž by musely rozumět vnitřnímu rozdělení sítě operátora, čímž budoucně zajišťuje schopnosti LI pro cloudové a softwarově definované sítě.

## Klíčové vlastnosti

- Koreluje informace související s odposlechem (IRI) z řídicí roviny s obsahem komunikace (CC) z uživatelské roviny
- Implementuje standardizované rozhraní X3 směrem k orgánům činným v trestním řízení
- Podporuje aktivaci a správu odposlechů v architektuře CUPS (oddělení řídicí a uživatelské roviny)
- Zpracovává zabezpečené, spolehlivé a na pořadí citlivé doručení zachycených dat
- Spolupracuje jak se síťovými funkcemi založenými na službách (např. SMF), tak s funkcemi pro přeposílání paketů (např. UPF)
- Spravuje více souběžných odposlechů a s nimi spojené administrativní funkce

## Související pojmy

- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)
- [CC – Component Carrier](/mobilnisite/slovnik/cc/)

## Definující specifikace

- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions

---

📖 **Anglický originál a plná specifikace:** [SX3LIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/sx3lif/)
