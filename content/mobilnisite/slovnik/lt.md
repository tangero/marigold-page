---
slug: "lt"
url: "/mobilnisite/slovnik/lt/"
type: "slovnik"
title: "LT – Layer Termination"
date: 2025-01-01
abbr: "LT"
fullName: "Layer Termination"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/lt/"
summary: "Layer Termination (LT, ukončení vrstvy) je funkční entita v architektuře sítě 3GPP zodpovědná za ukončení protokolových vrstev v určitých bodech. Zajišťuje správné protokolové zpracování, manipulaci s"
---

LT je funkční entita v architektuře sítě 3GPP zodpovědná za ukončení protokolových vrstev, aby zajistila správné zpracování, manipulaci a správu rozhraní pro integritu sítě a tok dat.

## Popis

Layer Termination (LT, ukončení vrstvy) je základní architektonický koncept v systémech 3GPP, který definuje body, kde jsou v síti ukončeny konkrétní protokolové vrstvy. Nejde o samostatný síťový uzel, ale o funkční schopnost integrovanou v různých síťových prvcích, jako jsou základnové stanice (eNodeB/gNB), uživatelská zařízení (UE) nebo funkce jádra sítě. Funkce LT zpracovává protokolové datové jednotky (PDU) pro danou vrstvu a provádí úkoly definované specifikacemi této vrstvy, jako je přidání/odstranění hlavičky, segmentace a znovusestavení, šifrování/dešifrování a detekce/korekce chyb. Jejím hlavním úkolem je řídit komunikaci typu peer-to-peer mezi odpovídajícími protokolovými entitami přes síťové propojení a zajistit, aby byla data správně formátována a doručena podle požadavků služeb dané vrstvy.

V praxi jsou body LT klíčové pro definici síťových rozhraní a oddělení odpovědností. Například v rádiové přístupové síti se bod ukončení vrstvy Packet Data Convergence Protocol (PDCP) liší mezi řídicí a uživatelskou rovinou, což ovlivňuje funkce jako šifrování a komprese hlaviček. V architekturách pro správu a účtování (odkazy ve specifikacích jako 32.107) pomáhá LT vymezit, kde dochází ke konkrétnímu zpracování pro přesné měření, vynucování politik a účtování. Umístění LT určuje, který síťový prvek zpracovává konkrétní protokolové funkce, což ovlivňuje latenci, bezpečnostní hranice a škálovatelnost sítě.

Z architektonického hlediska je LT úzce spojeno s vrstveným protokolovým modelem (např. PHY, [MAC](/mobilnisite/slovnik/mac/), RLC, PDCP, [RRC](/mobilnisite/slovnik/rrc/)). Bod ukončení každé vrstvy je designovou volbou, která ovlivňuje celkový výkon systému. Například centralizace ukončení RLC v centralizované jednotce ([CU](/mobilnisite/slovnik/cu/)) oproti jeho distribuci v distribuované jednotce ([DU](/mobilnisite/slovnik/du/)) v 5G ovlivňuje požadavky na přenosovou síť front-haul a latenci. Specifikace (např. 26.346, 28.620) podrobně popisují LT v kontextech, jako je multimediální služba vysílání/multicastu ([MBMS](/mobilnisite/slovnik/mbms/)) a správa, a definují, jak jsou protokoly ukotveny pro poskytování služeb a provoz sítě. Porozumění LT je nezbytné pro návrh sítě, testování interoperability a řešení problémů, protože definuje funkční hranice a předávací body mezi síťovými entitami.

## K čemu slouží

Koncept Layer Termination (ukončení vrstvy) existuje proto, aby poskytl jasnou, standardizovanou definici toho, kde v architektuře sítě 3GPP začíná a končí zpracování protokolové vrstvy. Tato jasnost je zásadní pro zajištění interoperability mezi síťovými zařízeními od různých výrobců, protože specifikuje přesné funkční odpovědnosti na každém rozhraní. Bez dobře definovaných bodů ukončení by nejednoznačnosti v protokolovém zpracování mohly vést k poškození dat, bezpečnostním slabinám nebo neúspěšným spojením. Historicky, jak se sítě vyvíjely z jednoduchých hlasových systémů na složité platformy pro multimédia založené na IP, rostla potřeba přesných architektonických definic pro zvládání rostoucí složitosti protokolového zásobníku.

LT řeší problém funkčního vymezení v více-dodavatelském, vrstveném síťovém prostředí. Umožňuje návrhářům sítí přidělovat konkrétní zpracovatelské úkoly (např. šifrování, kompresi hlaviček, opakované přenosy) tomu nejvhodnějšímu síťovému prvku – ať už v UE, RAN nebo jádru sítě – na základě úvah o latenci, bezpečnostní politice a efektivitě přenosu. Například ukončení vrstvy PDCP v gNB pro data uživatelské roviny umožňuje šifrování s nízkou latencí, zatímco její odlišné ukončení pro řídicí rovinu může optimalizovat signalizaci. V systémech správy je definice bodů LT klíčová pro přesné měření výkonu a sběr dat pro účtování, protože identifikuje místo, kde jsou generovány konkrétní události nebo počty dat.

Motivace pro standardizaci LT vychází z potřeby konzistentního referenčního modelu, který podporuje síťové řezy (network slicing), multi-konektivitu a disaggregační architektury RAN. Jak je vidět u 5G, s koncepty jako rozdělení na Centralized Unit ([CU](/mobilnisite/slovnik/cu/)) a Distributed Unit ([DU](/mobilnisite/slovnik/du/)), se umístění ukončení vrstvy (např. RLC, PDCP) stává klíčovou volitelnou možností (např. split options 2 a 6). Tato flexibilita umožňuje operátorům přizpůsobit nasazení sítí pro různé případy užití, ale vyžaduje přesné standardy, aby všechny síťové komponenty měly společné porozumění tomu, kde jsou funkce každé vrstvy prováděny. LT je tedy základním prvkem umožňujícím pokročilé síťové funkce a efektivní provoz.

## Klíčové vlastnosti

- Definuje přesné body pro ukončení zpracování protokolové vrstvy
- Umožňuje interoperabilitu standardizací funkčních hranic mezi síťovými prvky
- Podporuje flexibilní rozdělení síťové architektury (např. CU-DU v 5G NR)
- Umožňuje přesné měření výkonu a generování dat pro účtování
- Je nezbytný pro definici bezpečnostních hranic (např. kde dochází k šifrování/dešifrování)
- Je klíčový pro funkce správy a orchestrace dle specifikací správy 3GPP

## Související pojmy

- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 28.620** (Rel-19) — FMC Federated Network Information Model (FNIM) UIM
- **TS 32.107** (Rel-19) — Federated Network Information Model (FNIM)

---

📖 **Anglický originál a plná specifikace:** [LT na 3GPP Explorer](https://3gpp-explorer.com/glossary/lt/)
