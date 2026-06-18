---
slug: "sgw-c"
url: "/mobilnisite/slovnik/sgw-c/"
type: "slovnik"
title: "SGW-C – Serving Gateway Control plane function"
date: 2025-01-01
abbr: "SGW-C"
fullName: "Serving Gateway Control plane function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sgw-c/"
summary: "SGW-C je řídicí (control plane) komponenta Serving Gateway (SGW) v architektuře 5G a rozvinuté 4G. Zpracovává správu relací, kotvení mobility a vynucování pravidel pro relace uživatelských dat, čímž o"
---

SGW-C je řídicí (control plane) komponenta Serving Gateway, která zpracovává správu relací, kotvení mobility a vynucování pravidel, oddělující řídicí logiku od přeposílání paketů.

## Popis

Funkce řídicí roviny Serving Gateway (SGW-C) je kritická síťová funkce zavedená jako součást architektury oddělení řídicí a uživatelské roviny (CUPS) pro Evolved Packet Core (EPC) a jeho vývoj směrem k 5G. Představuje rozdělení monolitického Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) na samostatné entity řídicí a uživatelské roviny. SGW-C je zodpovědná za veškerou řídicí logiku spojenou se správou uživatelských relací. To zahrnuje zpracování signalizace od Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo funkce Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), jako jsou požadavky na zřízení, změnu a ukončení relace. Spravuje kotvící bod mobility pro předání mezi eNodeB v rámci LTE a funguje jako lokální kotva mobility pro 3GPP přístup, když se uživatelské zařízení (UE) pohybuje mezi eNodeB. SGW-C také komunikuje s funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) za účelem vynucení pravidel kvality služeb (QoS) a tarifních pravidel pro každou datovou relaci.

Z architektonického hlediska SGW-C komunikuje s odpovídající funkcí uživatelské roviny, [SGW-U](/mobilnisite/slovnik/sgw-u/), pomocí protokolu Packet Forwarding Control Protocol ([PFCP](/mobilnisite/slovnik/pfcp/)) definovaného v 3GPP TS 29.244. Tento protokol umožňuje SGW-C dávat pokyny SGW-U, jak zacházet s pakety uživatelské roviny. Například SGW-C odesílá SGW-U požadavky PFCP na zřízení/změnu/zrušení relace, aby vytvořila, aktualizovala nebo odstranila pravidla pro detekci paketů ([PDR](/mobilnisite/slovnik/pdr/)), pravidla pro akce přeposílání (FAR), pravidla pro vynucení QoS (QER) a pravidla pro hlášení využití (URR). Toto oddělení umožňuje centrální nasazení SGW-C pro efektivní řízení, zatímco instance SGW-U mohou být distribuovány k okraji sítě za účelem snížení latence uživatelského provozu.

V kontextu 5G je SGW-C součástí funkce pro propojení mezi 5G Core (5GC) a EPC, zejména ve scénářích nasazení non-standalone (NSA). Funguje ve spojení s User Plane Function (UPF) a Session Management Function (SMF). Úlohou SGW-C je zachovat kontinuitu pro 4G relace při přechodu sítí na 5G, což zajišťuje plynulou mobilitu a služby. Její fungování je podrobně popsáno v řadě specifikací, včetně architektury (23.214), správy (28.708, 32.867), protokolů (29.244) a zabezpečení (33.127).

## K čemu slouží

SGW-C byla vytvořena, aby řešila omezení tradiční, integrované Serving Gateway v 4G sítích. Monolitický SGW kombinoval funkce řídicí i uživatelské roviny v jednom síťovém prvku, což vedlo k neefektivitám při škálování. Škálování pro zvýšenou řídicí signalizaci (např. při hromadném připojování zařízení) vyžadovalo škálovat celý prvek včetně nákladných prostředků pro zpracování paketů uživatelské roviny. Naopak škálování pro propustnost uživatelské roviny (např. při náhlém nárůstu streamování videa) si rovněž vynutilo škálování kapacity řídicí roviny, což vedlo k nákladově neefektivním a rigidním nasazením.

Zavedení SGW-C jako součásti architektury CUPS standardizované v 3GPP Release 14 bylo motivováno potřebou větší flexibility, škálovatelnosti a inovací sítě. Oddělením řídicí roviny mohou operátoři centralizovat a sdružovat prostředky SGW-C ve velkých datových centrech pro efektivní správu a zpracování signalizace. Toto oddělení umožňuje nezávislé škálování prostředků řídicí a uživatelské roviny na základě skutečných požadavků sítě. Také usnadňuje nasazení funkcí uživatelské roviny (SGW-U) na distribuovaných místech blíže k rádiové přístupové síti, což je klíčový požadavek pro aplikace s nízkou latencí a edge computing. Tento architektonický posun byl základním krokem směrem k plně cloud-nativní, službami řízené architektuře 5G Core sítě.

## Klíčové vlastnosti

- Řídicí logika pro správu relací založených na GTP
- Kotvení mobility pro předání mezi eNodeB v LTE
- Rozhraní PFCP (N4/Sxa) pro řízení SGW-U
- Rozhraní k MME (S11) a PGW-C/SAEGW-C (S5/S8-C)
- Schopnosti funkce Policy and Charging Enforcement Function (PCEF) pro QoS
- Podpora propojení s 5GC pro mobilitu mezi 4G a 5G

## Související pojmy

- [SGW-U – Serving Gateway User plane function](/mobilnisite/slovnik/sgw-u/)
- [PFCP – Packet Forwarding Control Protocol](/mobilnisite/slovnik/pfcp/)
- [SGW – Signalling Gateway](/mobilnisite/slovnik/sgw/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 23.214** (Rel-19) — Control and User Plane Separation for EPC
- **TS 28.708** (Rel-19) — EPC NRM Integration Reference Point Information Service
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.844** (Rel-14) — Control and User Plane Separation for EPC Nodes
- **TS 32.867** (Rel-15) — Management Impacts of EPC CUPS
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [SGW-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/sgw-c/)
