---
slug: "pgw-c"
url: "/mobilnisite/slovnik/pgw-c/"
type: "slovnik"
title: "PGW-C – PDN Gateway Control plane function"
date: 2025-01-01
abbr: "PGW-C"
fullName: "PDN Gateway Control plane function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pgw-c/"
summary: "Řídicí rovina brány PDN v jádru sítě 5G. Zajišťuje správu relací, vynucování politik a řízení účtování pro relace uživatelských dat. Je klíčovým prvkem architektury oddělení řídicí a uživatelské rovin"
---

PGW-C je řídicí rovina brány PDN v jádru sítě 5G, která v rámci architektury CUPS zajišťuje správu relací, vynucování politik a řízení účtování.

## Popis

PGW-C (řídicí rovina brány [PDN](/mobilnisite/slovnik/pdn/)) je funkce jádra sítě zavedená jako součást architektury oddělení řídicí a uživatelské roviny (CUPS) ve specifikaci 3GPP Release 14. Představuje oddělení tradiční brány [P-GW](/mobilnisite/slovnik/p-gw/) (Packet Data Network Gateway) na samostatné entity řídicí roviny (PGW-C) a uživatelské roviny ([PGW-U](/mobilnisite/slovnik/pgw-u/)). Toto oddělení umožňuje nezávislé škálování, nasazení a vývoj funkcí řídicí a uživatelské roviny. PGW-C je zodpovědná za inteligenci a signalizační aspekty brány.

Z architektonického hlediska rozhraní PGW-C komunikuje s několika dalšími funkcemi jádra sítě. Komunikuje s funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) přes rozhraní Gx, aby přijímala pravidla pro politiky a účtování ([PCC](/mobilnisite/slovnik/pcc/)). Interaguje s Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) přes rozhraní Gy pro online řízení kreditu a s Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)) přes rozhraní Gz pro generování záznamů o účtovacích datech ([CDR](/mobilnisite/slovnik/cdr/)) pro offline účtování. Pro správu relací se připojuje k řídicí rovině Serving Gateway (SGW-C) a k Mobility Management Entity (MME) v Evolved Packet Core (EPC).

Její hlavní operační role zahrnuje správu připojení k paketové datové síti (PDN) pro uživatelské zařízení (UE). Když se UE připojí k síti a požádá o PDN připojení, PGW-C je zodpovědná za zřízení, modifikaci a ukončení relace. Přiděluje IP adresu UE (nebo tento úkol deleguje na PGW-U), vynucuje politiky QoS na základě PPC pravidel od PCRF a spravuje účtování na základě datového toku služby uživatele. Také zpracovává události mobility, jako jsou předání spojení mezi různými přístupovými technologiemi (např. z LTE na Wi-Fi), a zajišťuje kontinuitu relace.

PGW-C spolupracuje s PGW-U prostřednictvím standardizovaného řídicího protokolu definovaného ve specifikacích 3GPP, jako je TS 29.244 (PFCP - Packet Forwarding Control Protocol). PGW-C používá PFCP k instruování PGW-U, jak zacházet s provozem v uživatelské rovině. To zahrnuje instalaci, modifikaci nebo mazání pravidel pro detekci paketů (PDR), pravidel pro přeposílání (FAR), pravidel pro vynucování QoS (QER) a pravidel pro hlášení využití (URR). Tento vztah typu master-slave umožňuje PGW-C centrálně řídit více, potenciálně distribuovaných, instancí PGW-U, což umožňuje flexibilní a efektivní směrování a zpracování provozu.

## K čemu slouží

PGW-C byla vytvořena, aby řešila omezení monolitické architektury P-GW používané v dřívějších vydáních 3GPP. V tradičním EPC byla P-GW jediný síťový uzel kombinující funkce řídicí i uživatelské roviny. Tento monolitický design představoval několik výzev, včetně neefektivního škálování (celý uzel musel být škálován, i když byla potřeba pouze kapacita uživatelské roviny), omezené flexibility nasazení (funkce řídicí a uživatelské roviny musely být umístěny společně) a brzdil inovace (aktualizace jedné roviny mohly ovlivnit druhou).

Hlavní motivací pro její vytvoření byl celoprůmyslový posun směrem k virtualizaci síťových funkcí (NFV) a softwarově definovaným sítím (SDN), které vyžadují disagregované, softwarové komponenty, které lze nasadit nezávisle. Architektura oddělení řídicí a uživatelské roviny (CUPS), formalizovaná ve vydání 14, byla odpovědí 3GPP. Rozdělením P-GW na PGW-C a PGW-U získali operátoři schopnost škálovat řídicí rovinu (která zpracovává signalizaci a politiky) a uživatelskou rovinu (která zpracovává datové pakety s vysokou propustností) nezávisle na základě vzorců provozu. Například funkce uživatelské roviny mohou být nasazeny na okraji sítě pro služby s nízkou latencí, zatímco funkce řídicí roviny mohou zůstat centralizované pro efektivní správu.

Toto oddělení také připravilo cestu pro architekturu jádra sítě 5G (5GC), kde Session Management Function (SMF) a User Plane Function (UPF) jsou přímými konceptuálními nástupci PGW-C a PGW-U. Zavedení PGW-C umožnilo plynulejší vývoj z EPC na 5GC, umožnilo časné přijetí principů cloud-nativních a distribuovaných architektur v rámci sítě 4G, čímž se vyřešily problémy škálovatelnosti, flexibility a nákladové efektivity tváří v tvář exponenciálně rostoucímu mobilnímu datovému provozu.

## Klíčové vlastnosti

- Správa relací: Zajišťuje zřízení, modifikaci a ukončení PDN připojení pro UE.
- Vynucování politik: Aplikuje kontroly QoS a řízení přístupu na základě dynamických pravidel přijatých od PCRF.
- Řízení účtování: Komunikuje s online (OCS) a offline (OFCS) systémy účtování pro účtování využití služeb.
- Správa IP adres: Přiděluje nebo spravuje přidělování IP adres uživatelskému zařízení.
- Řídicí protokol (master): Působí jako řídicí entita pro jednu nebo více instancí PGW-U za použití protokolu PFCP.
- Podpora mobility: Spravuje kontinuitu relace během předání spojení mezi různými přístupovými technologiemi (např. z LTE na non-3GPP).

## Související pojmy

- [PGW-U – PDN Gateway User plane function](/mobilnisite/slovnik/pgw-u/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [P-GW – Packet Data Network Gateway](/mobilnisite/slovnik/p-gw/)
- [PFCP – Packet Forwarding Control Protocol](/mobilnisite/slovnik/pfcp/)

## Definující specifikace

- **TS 23.214** (Rel-19) — Control and User Plane Separation for EPC
- **TS 28.708** (Rel-19) — EPC NRM Integration Reference Point Information Service
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 29.844** (Rel-14) — Control and User Plane Separation for EPC Nodes
- **TS 32.867** (Rel-15) — Management Impacts of EPC CUPS
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [PGW-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/pgw-c/)
