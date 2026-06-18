---
slug: "pfcp"
url: "/mobilnisite/slovnik/pfcp/"
type: "slovnik"
title: "PFCP – Packet Forwarding Control Protocol"
date: 2025-01-01
abbr: "PFCP"
fullName: "Packet Forwarding Control Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pfcp/"
summary: "Protokol 3GPP používaný v 5G Core a EPC k oddělení řídicí roviny od uživatelské roviny. Umožňuje řídicí rovině (SMF/CP-funkci) programovat přeposílací pravidla, QoS politiky a pokyny pro účtování do u"
---

PFCP je protokol 3GPP, který odděluje řídicí a uživatelskou rovinu a umožňuje řídicí rovině programovat do uživatelské roviny přeposílací pravidla, QoS politiky a pokyny pro účtování.

## Popis

Packet Forwarding Control Protocol (PFCP) je klíčový protokol definovaný 3GPP pro komunikaci mezi řídicí a uživatelskou rovinou v architekturách sítí Evolved Packet Core (EPC) i 5G Core (5GC). Působí přes rozhraní Sx (mezi [SGW-C](/mobilnisite/slovnik/sgw-c/)/[PGW-C](/mobilnisite/slovnik/pgw-c/) a [SGW-U](/mobilnisite/slovnik/sgw-u/)/[PGW-U](/mobilnisite/slovnik/pgw-u/)) v EPC a přes rozhraní N4 (mezi [SMF](/mobilnisite/slovnik/smf/) a [UPF](/mobilnisite/slovnik/upf/)) v 5GC. PFCP je protokol typu master-slave, kde funkce řídicí roviny (CPF), jako je Session Management Function (SMF), vystupuje jako hlavní uzel (master) a funkce uživatelské roviny (UPF), jako je UPF nebo PGW-U, vystupuje jako podřízený uzel (slave). Protokol používá mechanismus požadavek-odpověď, přičemž CPF posílá příkazy a UPF je provádí a podává zpětnou zprávu.

Hlavní funkcí PFCP je umožnit řídicí rovině vzdáleně spravovat chování uživatelské roviny, aniž by byla v datové cestě. Toho je dosaženo správou pravidel pro detekci paketů ([PDR](/mobilnisite/slovnik/pdr/)), pravidel pro přeposílání ([FAR](/mobilnisite/slovnik/far/)), pravidel pro vymáhání QoS (QER) a pravidel pro hlášení využití (URR), která jsou souhrnně označována jako PFCP asociace, relace a pravidla. PDR obsahuje informace pro porovnání paketů (např. IP hlavičky a porty) k identifikaci konkrétního toku. Každé PDR je propojeno s FAR, které určuje, co se má s odpovídajícími pakety udělat (např. přeposlat, zahodit, uložit do bufferu nebo odeslat do CPF). QER aplikují omezení rychlosti a značkování, zatímco URR spouští hlášení využití pro účtování.

Při vytvoření uživatelské relace použije SMF procedury PFCP Session Establishment k naprogramování těchto pravidel do UPF. Když dorazí datové pakety, rychlá cesta (fast-path) UPF je porovná s nainstalovanými PDR a provede odpovídající FAR a QER. To umožňuje funkce jako klasifikátor v uplinku, bod větvení, směrování provozu a vymáhání QoS přímo v uživatelské rovině. PFCP také podporuje heartbeat mechanismy pro detekci živosti uzlů a procedury hlášení relací, kde může UPF informovat CPF o událostech, jako je dosažení prahů využití nebo detekce začátku/konce toku provozu. Toto jasné oddělení, umožněné protokolem PFCP, je základem architektury Control and User Plane Separation (CUPS).

## K čemu slouží

PFCP byl vytvořen k umožnění architektury Control and User Plane Separation (CUPS), což je významný vývoj v návrhu jádra sítě. Tradiční síťové prvky jako SGW a PGW byly monolitické, kombinující řídicí signalizaci i přeposílání dat v jednom fyzickém nebo logickém uzlu. Toto těsné propojení omezovalo škálovatelnost, protože zdroje řídicí a uživatelské roviny musely být škálovány společně, a bránilo flexibilnímu nasazení, protože datová rovina nemohla být distribuována nezávisle, aby byla blíže uživatelům.

Vývoj PFCP přímo řešil tato omezení. Definováním standardního protokolu umožnil oddělení řídicí roviny (odpovědné za signalizaci, politiky a správu relací) od uživatelské roviny (odpovědné za vysokorychlostní přeposílání paketů). To umožňuje nezávislé škálování zdrojů řídicí a uživatelské roviny. Operátoři sítí mohou nasadit centralizované řídicí funkce pro efektivitu a zároveň distribuovat bezstavové funkce uživatelské roviny (UPF) k okraji sítě pro služby s nízkou latencí. PFCP poskytuje přesný jazyk, kterým může řídicí rovina dynamicky 'programovat' přeposílací chování uživatelské roviny, což je zásadní pro podporu síťového řezání (network slicing), vytváření služeb na vyžádání a efektivní správu provozu v moderních 5G a pokročilých 4G sítích.

## Klíčové vlastnosti

- Umožňuje architekturu Control and User Plane Separation (CUPS)
- Definuje procedury pro správu asociace, vytvoření, změnu a zrušení relace
- Používá systém založený na pravidlech (PDR, FAR, QER, URR) k programování chování uživatelské roviny
- Podporuje hlášení na úrovni uzlu a relace pro monitorování a účtování
- Poskytuje heartbeat mechanismus pro detekci živosti uzlu a selhání
- Protokol nezávislý na podkladové transportní vrstvě (může používat SCTP nebo UDP)

## Definující specifikace

- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TR 29.820** (Rel-17) — Study on PFCP Best Practice
- **TS 29.866** (Rel-19) — IMS Disaster Prevention & Restoration Enhancement

---

📖 **Anglický originál a plná specifikace:** [PFCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pfcp/)
