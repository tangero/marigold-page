---
slug: "sgw-u"
url: "/mobilnisite/slovnik/sgw-u/"
type: "slovnik"
title: "SGW-U – Serving Gateway User plane function"
date: 2025-01-01
abbr: "SGW-U"
fullName: "Serving Gateway User plane function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sgw-u/"
summary: "SGW-U je uživatelská rovina brány Serving Gateway, odpovědná za vlastní přeposílání, směrování a vynucování QoS paketů uživatelských dat. Je řízena funkcí SGW-C pomocí protokolu PFCP, což umožňuje fle"
---

SGW-U je uživatelská rovina brány Serving Gateway, která podléhá řízení SGW-C a přeposílá, směruje a vynucuje QoS pro pakety uživatelských dat.

## Popis

Funkce uživatelské roviny brány Serving Gateway (SGW-U) je přeposílací engine, který vznikl rozdělením tradiční brány Serving Gateway. Zavedena s oddělením řídicí a uživatelské roviny (CUPS) zpracovává SGW-U veškeré zpracování roviny dat pro uživatelský provoz v Evolved Packet Core (EPC). Jejím hlavním úkolem je sloužit jako mobilní kotva pro uživatelskou rovinu při předávání spojení mezi eNodeB v rámci LTE a směrovat a přeposílat provoz mezi rádiovou přístupovou sítí (RAN) a bránou Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)). Funguje pod přímým velením své přidružené funkce řídicí roviny, [SGW-C](/mobilnisite/slovnik/sgw-c/), a to pomocí Packet Forwarding Control Protocol ([PFCP](/mobilnisite/slovnik/pfcp/)) přes referenční bod Sxa.

Funkčně provádí SGW-U kontrolu paketů, jejich klasifikaci a vynucovací akce na základě pravidel nainstalovaných SGW-C. Tato pravidla jsou předávána prostřednictvím zpráv PFCP a zahrnují Pravidla pro detekci paketů (PDRs), Pravidla pro akce přeposílání (FARs) a Pravidla pro vynucování QoS (QERs). [PDR](/mobilnisite/slovnik/pdr/) definuje, jak identifikovat tok paketů (pomocí parametrů jako zdrojová/cílová IP adresa, port a identifikátory koncových bodů tunelu [GTP](/mobilnisite/slovnik/gtp/)). Jakmile paket odpovídá PDR, přidružené [FAR](/mobilnisite/slovnik/far/) určuje akci, například přeposlání paketu do konkrétního tunelu dalšího směru (např. směrem k eNodeB nebo [PGW-U](/mobilnisite/slovnik/pgw-u/)), jeho uložení do vyrovnávací paměti nebo jeho zahození. QERs umožňují SGW-U uplatňovat řízení rychlosti, značkování a plánování, aby byla zajištěna dohodnutá kvalita služby (QoS). SGW-U je také odpovědná za zapouzdřování a rozbalování uživatelských IP paketů v tunelech [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol (GTP-U), které ji spojují s eNodeB (S1-U) a s PGW-U (S5/S8-U).

Z architektonického hlediska umožňuje toto oddělení implementovat SGW-U jako vysoce výkonný, odlehčený uzel pro zpracování paketů, často s využitím hardwarové akcelerace. Může být nasazena distribuovaným způsobem, mnohem blíže k RAN než centralizované datové centrum. Tato distribuce je klíčová pro snížení latence, což prospívá aplikacím jako mobilní hry, autonomní vozidla a rozšířená realita. Ve scénářích spolupráce se sítí 5G může být SGW-U umístěna společně nebo propojena s funkcí uživatelské roviny 5G (UPF), aby usnadnila plynulé předávání uživatelské roviny mezi přístupem 4G a 5G. Její specifikace pokrývají architekturu (23.214), správu (28.708, 32.867), protokol PFCP (29.244) a bezpečnostní požadavky (33.127).

## K čemu slouží

SGW-U byla vyvinuta za účelem překonání nepružnosti integrované SGW platformy. V tradičních nasazeních EPC byla uživatelská rovina SGW pevně svázána s její řídicí rovinou, což bránilo nezávislé optimalizaci a škálování. Toto propojení bylo nevhodné pro nové trendy, jako je virtualizace síťových funkcí (NFV) a potřeba výpočetního výkonu s nízkou latencí na okraji sítě. Škálování propustnosti uživatelské roviny vyžadovalo pořizování celých nových instancí SGW, včetně redundantních prostředků řídicí roviny, což vedlo k neefektivním kapitálovým výdajům.

Vytvoření SGW-U, dokončené ve verzi 3GPP Release 14 jako součást CUPS, bylo motivováno snahou o agilnější, cloud-nativní síťovou architekturu. Vytěžením uživatelské roviny do samostatné funkce mohou operátoři nasazovat odlehčené, bezstavové instance SGW-U pomocí běžně dostupného hardwaru nebo virtualizovaných platforem na optimálních místech v topologii sítě. To umožňuje odklonění provozu na okraji sítě pro místní služby a snižuje náklady na backhaul. Programovatelnost SGW-U prostřednictvím PFCP také otevírá dveře principům softwarově definovaného sítění (SDN) v mobilním jádře sítě, což umožňuje dynamičtější směrování provozu a řetězení služeb. Toto oddělení bylo přímým předchůdcem nativního oddělení řídicí a uživatelské roviny, které vidíme u SMF a UPF v jádru 5G sítě, a potvrdilo tento koncept pro sítě příští generace.

## Klíčové vlastnosti

- Vysokovýkonné přeposílání paketů a GTP-U tunelování
- Vynucuje politiky QoS (omezování rychlosti, značkování) pomocí QERs
- Provádí akce zpracování paketů (přeposlat, zahodit, uložit do vyrovnávací paměti) pomocí FARs
- Identifikuje uživatelské toky na základě PDRs přijatých od SGW-C
- Slouží jako kotva uživatelské roviny pro předávání spojení v rámci LTE
- Podporuje distribuované nasazení na okraji sítě pro nízkou latenci

## Související pojmy

- [SGW-C – Serving Gateway Control plane function](/mobilnisite/slovnik/sgw-c/)
- [PFCP – Packet Forwarding Control Protocol](/mobilnisite/slovnik/pfcp/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)

## Definující specifikace

- **TS 23.214** (Rel-19) — Control and User Plane Separation for EPC
- **TS 28.708** (Rel-19) — EPC NRM Integration Reference Point Information Service
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.844** (Rel-14) — Control and User Plane Separation for EPC Nodes
- **TS 32.867** (Rel-15) — Management Impacts of EPC CUPS
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [SGW-U na 3GPP Explorer](https://3gpp-explorer.com/glossary/sgw-u/)
