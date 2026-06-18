---
slug: "pcp"
url: "/mobilnisite/slovnik/pcp/"
type: "slovnik"
title: "PCP – Priority Code Point"
date: 2025-01-01
abbr: "PCP"
fullName: "Priority Code Point"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pcp/"
summary: "Pole v rámcích Ethernet používané k označení úrovně priority provozu pro zpracování QoS. V systémech 5G se používá na rozhraní N6 mezi UPF a datovou sítí k sladění prioritizace přenosu na bázi Etherne"
---

PCP je pole Priority Code Point v rámcích Ethernet používané na rozhraní N6 v 5G sítích pro označení priority provozu a sladění přenosu po Ethernetu s toky QoS v 5G za účelem konzistentní kvality služeb.

## Popis

Priority Code Point (PCP) je 3bitové pole uvnitř [VLAN](/mobilnisite/slovnik/vlan/) tagu ([IEEE](/mobilnisite/slovnik/ieee/) 802.1Q) hlavičky rámce Ethernet. Používá se k označení úrovně priority rámce, což umožňuje diferenciaci kvality služeb (QoS) na vrstvě 2. Hodnota PCP se mapuje na různé úrovně priority, které často odpovídají třídám provozu, jako je Background, Best Effort, Excellent Effort, Critical Applications, Video, Voice a Network Control. Ethernetové přepínače tuto hodnotu PCP používají pro rozhodování o přeposílání, včetně výběru fronty a precedence zahození paketů, což je klíčové pro správu zahlcení a zajištění nízké latence pro prioritní provoz.

V kontextu systémů 3GPP 5G získává PCP specifický význam na rozhraní N6, které spojuje User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) s datovou sítí ([DN](/mobilnisite/slovnik/dn/)). Jádrová síť 5G spravuje QoS prostřednictvím toků QoS, z nichž každý má identifikátor [5QI](/mobilnisite/slovnik/5qi/) (5G QoS Identifier), který definuje charakteristiky jako priorita, rozpočet zpoždění paketů a míra chyb. Když jsou pakety uživatelské roviny odesílány přes rozhraní N6, které je často založené na Ethernetu, je nutné mapování mezi parametry toku QoS v 5G a značkami QoS na vrstvě 2 používanými v přenosové síti. Pole PCP je jedním z mechanismů pro přenos této informace o prioritě.

UPF je zodpovědná za označení pole PCP v odchozích rámcích Ethernetu na základě politiky QoS spojené s tokem QoS daného paketu. Tím se zajišťuje, že přenosová síť mezi UPF a DN (např. internetovou bránou nebo podnikovou sítí) respektuje úrovně priority stanovené jádrem 5G. Toto sladění je zásadní pro end-to-end QoS, neboť zabraňuje tomu, aby se přenosový segment stal úzkým hrdlem, které degraduje kvalitu služeb garantovanou 5G rádiovou a jádrovou sítí.

## K čemu slouží

PCP existuje jako standardizovaný mechanismus na linkové vrstvě pro prioritizaci provozu v sítích Ethernet, jak je definováno standardem [IEEE](/mobilnisite/slovnik/ieee/) 802.1Q. Jeho účelem je umožnit přepínačům rozlišovat provoz a aplikovat odpovídající chování při řazení do front a plánování bez nutnosti hluboké kontroly paketů. To je základní pro budování konvergovaných sítí, které přenášejí mix provozu citlivého na latenci (např. hlas, hry) a hromadného provozu.

V 5G je explicitní motivací pro odkazování na PCP v technických specifikacích, jako je TS 29.244 (protokol [UPF](/mobilnisite/slovnik/upf/)), zajistit bezproblémovou integraci QoS mezi jádrem 5G a externími sítěmi. 5G zavádí sofistikované, na tocích založené modely QoS. Pouhé spoléhání se na značky [DSCP](/mobilnisite/slovnik/dscp/) na IP vrstvě nemusí být dostačující, pokud je podkladový přenos spravován na vrstvě 2. PCP poskytuje přímý způsob, jak přenést prioritu toku QoS 5G na ethernetovou infrastrukturu, a řeší tak problém transparentnosti QoS napříč administrativními a technologickými doménami. Řeší omezení spočívající v existenci mezery v QoS mezi podrobnou kontrolou systému 5G a potenciálně jednoduššími mechanismy priority přenosu připojené datové sítě.

## Klíčové vlastnosti

- 3bitové pole v tagu VLAN IEEE 802.1Q pro prioritu rámce
- Definuje osm úrovní priority (0-7) pro označení třídy provozu
- Používáno ethernetovými přepínači pro výběr fronty a správu zahlcení
- V 5G je mapováno z parametrů toku QoS 5G (např. 5QI, ARP)
- Aplikováno UPF na rozhraní N6 směrem k datové síti
- Umožňuje konzistenci end-to-end QoS napříč rádiovým, jádrovým a přenosovým segmentem

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report

---

📖 **Anglický originál a plná specifikace:** [PCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcp/)
