---
slug: "slss"
url: "/mobilnisite/slovnik/slss/"
type: "slovnik"
title: "SLSS – Sidelink Synchronisation Signal"
date: 2025-01-01
abbr: "SLSS"
fullName: "Sidelink Synchronisation Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/slss/"
summary: "Signál fyzické vrstvy používaný pro synchronizaci v komunikacích typu zařízení-zařízení (D2D) a Vozidlo-s-vším (V2X) přes postranní spoj (sidelink). Umožňuje uživatelským zařízením (UE) sladit své čas"
---

SLSS je signál fyzické vrstvy používaný pro synchronizaci v komunikacích typu zařízení-zařízení (D2D) a V2X přes postranní spoj (sidelink), který umožňuje uživatelským zařízením sladit svůj časování a kmitočet pro přímou komunikaci.

## Popis

Sidelink Synchronisation Signal (SLSS) je klíčový signál fyzické vrstvy definovaný v 3GPP pro služby komunikace na krátkou vzdálenost ([ProSe](/mobilnisite/slovnik/prose/)) a sidelink komunikaci, což je přímý rádiový spoj mezi uživatelskými zařízeními (UE). Skládá se ze dvou hlavních složek: Primárního sidelink synchronizačního signálu ([PSSS](/mobilnisite/slovnik/psss/)) a Sekundárního sidelink synchronizačního signálu ([SSSS](/mobilnisite/slovnik/ssss/)). Tyto signály vysílá UE fungující jako synchronizační zdroj, často označované jako SyncRef UE. Hlavní funkcí SLSS je poskytnout časovou a kmitočtovou synchronizaci pro další UE (synchronizační následovníky) v dosahu, aby mohla správně přijímat a dekódovat následné řídicí a datové kanály sidelink.

Z architektonického hlediska může být přenos SLSS řízen sítí nebo autonomní. V pokrytí může [eNB](/mobilnisite/slovnik/enb/)/gNB nařídit UE vysílat SLSS a poskytnout potřebnou synchronizační konfiguraci. Mimo pokrytí se mohou UE autonomně stát synchronizačními zdroji na základě předdefinovaných pravidel a vytvářet tak synchronizační řetězec. SLSS nese identitu sidelink synchronizace (SLSS ID), která udává typ synchronizačního zdroje (např. ze sítě, z jiného UE v pokrytí nebo z nezávislého UE). Přijímající UE provádí korelační detekci PSSS a SSSS, aby dosáhla synchronizace symbolů, časování rádiových rámců a korekce kmitočtového posunu.

Jak to funguje: UE prohledává vyhrazené fondy prostředků, aby našlo SLSS. Po detekci odvodí časový referenční signál a upraví svůj vnitřní hodinový signál. Tato synchronizovaná časová základna je zásadní, protože sidelink komunikace využívá duplexování s časovým dělením ([TDD](/mobilnisite/slovnik/tdd/)) s konkrétními podrámci vyhrazenými pro řízení a data. Bez společné časové reference by se přenosy kolidovaly a přijímače by nevěděly, kdy mají naslouchat. SLSS také usnadňuje objevování synchronizačních zdrojů a pomáhá udržovat stabilní synchronizační hierarchii v dynamických prostředích, jako jsou vozidlové sítě, kde se UE pohybují vysokou rychlostí. Jeho role je základní pro spolehlivou přímou komunikaci v aplikacích veřejné bezpečnosti, [V2X](/mobilnisite/slovnik/v2x/) a komerčního [D2D](/mobilnisite/slovnik/d2d/).

## K čemu slouží

SLSS byl zaveden, aby vyřešil základní výzvu navázání a udržení synchronizace v decentralizované, přímé komunikaci mezi zařízeními. Před jeho specifikací byla synchronizace v LTE výhradně mezi UE a základnovou stanicí ([eNB](/mobilnisite/slovnik/enb/)). Pro přímou sidelink komunikaci, zejména pro scénáře mimo pokrytí, jako jsou operace veřejné bezpečnosti nebo vozidla jedoucí v koloně, byl vyžadován nový synchronizační mechanismus nezávislý na síťové infrastruktuře.

K jeho vytvoření vedla práce 3GPP na službách komunikace na krátkou vzdálenost (ProSe) počínaje Release 12 a později na V2X v Release 14. Omezení spočívající pouze v závislosti na GNSS pro časování (např. nedostupnost v interiéru, cena, spotřeba energie) si vyžádala synchronizační signál založený na buněčné síti. SLSS umožňuje vytváření lokálních synchronizačních klastrů a zajišťuje, že všechna vysílající UE v oblasti jsou časově sladěna, což minimalizuje interference a umožňuje efektivní využití sdílených prostředků. Řeší problém chaotických, nesynchronizovaných přenosů, které by vedly ke špatné spolehlivosti a kapacitě v kritických scénářích přímé komunikace.

## Klíčové vlastnosti

- Skládá se z Primárního (PSSS) a Sekundárního (SSSS) sidelink synchronizačního signálu
- Poskytuje časovou a kmitočtovou synchronizaci pro UE používající sidelink
- Může být vysílán z UE v pokrytí, mimo pokrytí nebo na základě GNSS
- Nese Identitu sidelink synchronizace (SLSS ID) udávající typ zdroje
- Umožňuje vytváření synchronizačních hierarchií a řetězců
- Nezbytný pro správnou funkci řídicích (PSCCH) a sdílených (PSSCH) kanálů sidelink

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SLSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/slss/)
