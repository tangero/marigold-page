---
slug: "licf"
url: "/mobilnisite/slovnik/licf/"
type: "slovnik"
title: "LICF – Lawful Interception Control Function"
date: 2025-01-01
abbr: "LICF"
fullName: "Lawful Interception Control Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/licf/"
summary: "Hlavní síťová funkce 5G odpovědná za správu, autorizaci a aktivaci příkazů k zákonnému odposlechu (LI). Slouží jako centrální administrativní řídicí bod, který přijímá soudní příkazy k odposlechu od o"
---

LICF je hlavní síťová funkce 5G, která spravuje, autorizuje a aktivuje příkazy k zákonnému odposlechu od orgánů činných v trestním řízení a orchestruje odposlech v celé síti.

## Popis

Lawful Interception Control Function (LICF) je standardizovaná funkce jádra sítě 5G definovaná v rámci specifikace 3GPP Security Assurance Specification ([SCAS](/mobilnisite/slovnik/scas/)). Slouží jako hlavní řídicí prvek pro všechny činnosti zákonného odposlechu v rámci samostatné ([SA](/mobilnisite/slovnik/sa/)) sítě 5G. LICF se nachází v administrativní doméně operátora a komunikuje se zařízením pro monitorování orgánů činných v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)) prostřednictvím standardizovaného předávacího rozhraní ([HI](/mobilnisite/slovnik/hi/)). Jejím primárním úkolem je ověřit a autorizovat žádosti o odposlech, zvalidovat jejich zákonný rozsah (např. identitu cíle, obsah odposlechu, dobu trvání) a následně zřídit příkaz k odposlechu pro příslušné odposlouchávající síťové funkce.

Z architektonického hlediska LICF komunikuje s ostatními funkcemi jádra 5G prostřednictvím rozhraní založených na službách. Po přijetí platného soudního příkazu LICF identifikuje, které síťové funkce (NFs) se podílejí na relacích cílového účastníka – například Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) pro události řídicí roviny, Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) pro data relace a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) pro vlastní obsah komunikace. LICF zasílá těmto NFs aktivační příkazy a instruuje je, aby začaly shromažďovat a duplikovat stanovené informace související s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) a obsah komunikace (CC).

Funkce spravuje celý životní cyklus odposlechu, včetně aktivace, změny, deaktivace a dotazů na stav. Zajišťuje, že odposlech je prováděn přesně v autorizovaném rozsahu a nedochází k nadměrnému shromažďování dat. LICF také zajišťuje zabezpečené doručení odposlechnutých dat k mediační funkci (MF), která je naformátuje podle standardů ETSI před přenosem do LEMF. Tento centralizovaný řídicí model zjednodušuje provádění bezpečnostních auditů, logování a podávání zpráv o souladu pro síťové operátory, protože všechny příkazy k odposlechu procházejí jedinou zabezpečenou funkcí.

## K čemu slouží

LICF byla zavedena v 5G jako reakce na architektonický posun od monolitických síťových prvků předchozích generací (2G/3G/4G) k cloud-nativní, na službách založené architektuře (SBA). V legacy systémech byla funkce LI vestavěna do jednotlivých síťových uzlů (jako MSC, SGSN nebo MME), což vedlo ke složitému distribuovanému zřizování a nekonzistentním bezpečnostním kontrolám. Tento decentralizovaný přístup ztěžoval zajištění jednotného prosazování politik a udržení zabezpečené auditní stopy v celé síti.

Vytvoření LICF poskytuje centralizovanou, standardizovanou řídicí rovinu pro LI, která je nezávislá na podkladových síťových funkcích. Tím se řeší klíčové problémy: nabízí jediný zabezpečený vstupní bod pro žádosti orgánů činných v trestním řízení, zjednodušuje implementaci LI ve virtualizované a řezané síti a zvyšuje celkové zabezpečení systému odposlechu jako takového. Oddělením řídicí logiky od odposlouchávajících entit umožňuje LICF agilnější nasazení v cloudových jádrech 5G a zajišťuje, že schopnosti LI se mohou vyvíjet nezávisle na ostatních síťových službách, a to vše při splnění přísných zákonných a regulačních požadavků na soulad po celém světě.

## Klíčové vlastnosti

- Centralizovaná autorizace a aktivace soudních příkazů k odposlechu
- Rozhraní založené na službách (např. Nlicf) pro komunikaci s NFs jádra 5G
- Správa životního cyklu (aktivace, změna, deaktivace, dotaz) příkazů k odposlechu
- Identifikace cíle a mapování na obsluhující síťové funkce
- Zabezpečené rozhraní (HI2) k zařízení pro monitorování orgánů činných v trestním řízení (LEMF)
- Integrace s mediační funkcí 5G pro standardizované doručování dat

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)

## Definující specifikace

- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [LICF na 3GPP Explorer](https://3gpp-explorer.com/glossary/licf/)
