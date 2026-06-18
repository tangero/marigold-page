---
slug: "ipe"
url: "/mobilnisite/slovnik/ipe/"
type: "slovnik"
title: "IPE – In Path Equipment"
date: 2025-01-01
abbr: "IPE"
fullName: "In Path Equipment"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ipe/"
summary: "In Path Equipment (IPE) označuje síťové prvky, například sondy nebo monitorovací systémy, které jsou fyzicky nebo logicky vloženy do cesty pro přenos dat za účelem analýzy, měření nebo modifikace prov"
---

IPE (In Path Equipment) je síťový prvek, například sonda nebo monitorovací systém, který je vložen do datové cesty za účelem analýzy, měření nebo modifikace provozu v uživatelské rovině v reálném čase.

## Popis

In Path Equipment (IPE) je termín používaný ve specifikacích správy 3GPP, zejména v rámci rámců pro správu výkonu ([PM](/mobilnisite/slovnik/pm/)) a správu poruch ([FM](/mobilnisite/slovnik/fm/)). Popisuje jakýkoli fyzický nebo logický síťový prvek, který se nachází přímo v aktivní cestě pro přenos dat (uživatelská rovina) mezi dvěma koncovými body komunikace. Na rozdíl od nástrojů mimo cestu (out-of-path), které analyzují kopírovaný provoz, IPE přímo zpracovává živý tok provozu. Mezi běžné příklady patří systémy hluboké inspekce paketů (DPI), mediační funkce pro zákonné odposlechy ([LI](/mobilnisite/slovnik/li/)), uzly pro optimalizaci provozu (např. optimalizátory TCP), sondy pro měření výkonu a některé bezpečnostní brány.

Z architektonického hlediska lze IPE nasadit různými způsoby: jako fyzické zařízení vložené mezi dva síťové porty (bump-in-the-wire), jako virtuální funkci integrovanou do síťového uzlu jako [PGW](/mobilnisite/slovnik/pgw/) nebo [UPF](/mobilnisite/slovnik/upf/), nebo jako logickou funkci na směrovači, která přesměrovává specifické toky ke zpracování. Jeho klíčovou charakteristikou je, že se nachází v kritické cestě pro doručování dat, což znamená, že jakékoli zpoždění, selhání nebo omezení výkonu způsobené IPE přímo ovlivňuje kvalitu služby uživatele. Proto je vysoká dostupnost a nízká latence klíčovými aspekty návrhu IPE.

IPE funguje tak, že zachytává pakety s rychlostí linky, aplikuje sadu konfigurovaných pravidel nebo analýz a následně přeposílá pakety (potenciálně upravené) směrem k jejich cíli. Například IPE založené na DPI může klasifikovat provoz, aplikovat značky QoS nebo blokovat škodlivé toky. IPE pro měření výkonu může označovat pakety časovými značkami pro měření jednostranného zpoždění nebo rozkmitu. Rozhraní pro správu IPE, definovaná např. ve specifikaci 28.062, umožňují síťovým operátorům tyto funkce konfigurovat, sbírat měření a monitorovat stav samotného IPE.

V kontextu samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)) a funkce pro analýzu síťových dat ([NWDAF](/mobilnisite/slovnik/nwdaf/)) 3GPP mohou být data sesbíraná IPE klíčovým vstupem. Měření propustnosti, ztrátovosti paketů a doby odezvy aplikací provedená přímo v datové cestě poskytují nejpřesnější pohled na skutečný uživatelský prožitek. Správa IPE vyžaduje pečlivou rovnováhu mezi získáním přehledu/kontroly a minimalizací rizika, že se IPE stane síťovým úzkým hrdlem nebo jediným bodem selhání.

## K čemu slouží

Koncept In Path Equipment byl standardizován, aby řešil rostoucí potřebu reálného a přesného monitorování a řízení stále složitějšího a rychlejšího mobilního datového provozu. Jak se sítě vyvíjely z jednoduchých hlasových okruhů na komplexní platformy IP služeb, monitorování mimo datovou cestu (např. dotazy [SNMP](/mobilnisite/slovnik/snmp/), analýza logů) se stalo nedostatečným pro pochopení skutečného výkonu služeb a vynucování podrobných politik.

IPE existuje pro řešení problémů souvisejících se zajištěním služeb, zabezpečením a optimalizací provozu. Umožňuje operátorům přímo v datové cestě měřit klíčové ukazatele výkonu (KPI), jako je latence uživatelské roviny a propustnost, což je nezbytné pro ověřování SLA a odstraňování problémů. Pro zabezpečení umožňuje IPE detekci a zmírnění útoků v reálném čase. Z obchodního hlediska IPE umožňuje pokročilé směrování provozu, rodičovské kontroly a účtování specifické pro aplikace.

Před zavedením formálních standardů správy pro IPE bylo nasazování takových zařízení závislé na dodavateli a často narušovalo integraci celkové správy sítě. Definice 3GPP poskytují společný rámec pro modelování, konfiguraci a monitorování těchto zařízení, což zajišťuje, že mohou být spravována jako nedílné součásti sítě, a nikoli jako izolované, neřízené 'černé skříňky'. To bylo obzvláště důležité s virtualizací síťových funkcí (NFV), která vyžadovala standardizovaný způsob vkládání a správy virtuálních funkcí IPE v datových cestách definovaných softwarem.

## Klíčové vlastnosti

- Nachází se přímo v aktivní cestě pro přenos dat uživatelské roviny
- Schopné reálné analýzy, modifikace nebo měření paketů
- Může implementovat funkce jako hluboká inspekce paketů (DPI) a optimalizace provozu
- Kritické pro přesné měření uživatelského prožitku a zajištění služeb
- Vyžaduje návrh s vysokou dostupností, aby se předešlo jeho roli jediného bodu selhání
- Spravováno pomocí standardizovaných rozhraní (např. definovaných v 3GPP 28.062) pro konfiguraci a sběr dat

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [IPE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipe/)
