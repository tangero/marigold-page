---
slug: "pgw-u"
url: "/mobilnisite/slovnik/pgw-u/"
type: "slovnik"
title: "PGW-U – PDN Gateway User plane function"
date: 2026-01-01
abbr: "PGW-U"
fullName: "PDN Gateway User plane function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pgw-u/"
summary: "Uživatelská rovina brány PDN v síti 5G Core. Provádí přeposílání, inspekci, ukládání do vyrovnávací paměti a vynucování QoS pro uživatelský datový provoz. Je kotvícím bodem pro přenos dat v architektu"
---

PGW-U je uživatelská rovina brány PDN (Packet Data Network Gateway) v sítích 5G Core, která provádí přeposílání, inspekci, ukládání do vyrovnávací paměti a vynucování QoS (Quality of Service) paketů a slouží jako kotvící bod pro přenos dat.

## Popis

PGW-U ([PDN](/mobilnisite/slovnik/pdn/) Gateway User plane function) je komponenta datové roviny vzniklé oddělením od tradiční [P-GW](/mobilnisite/slovnik/p-gw/) (Packet Data Network Gateway) podle architektury oddělení řídicí a uživatelské roviny (CUPS, Control and User Plane Separation) definované konsorciem 3GPP počínaje Release 14. Je zodpovědná za skutečné přeposílání a zpracování paketů uživatelských dat mezi uživatelským zařízením (UE, User Equipment) a externími paketovými datovými sítěmi (PDN, Packet Data Network), jako je internet nebo síť IMS. Zatímco [PGW-C](/mobilnisite/slovnik/pgw-c/) (PDN Gateway Control plane function) zpracovává signalizaci a inteligenci, PGW-U zajišťuje vysokopropustnou a na latenci citlivou datovou cestu.

Architektonicky se PGW-U nachází na cestě uživatelské roviny mezi funkcí uživatelské roviny Serving Gateway ([SGW-U](/mobilnisite/slovnik/sgw-u/)) a externí sítí. Rozhraní se SGW-U zajišťuje přes rozhraní S5/S8-U (pomocí tunelů [GTP-U](/mobilnisite/slovnik/gtp-u/)) a k externí PDN se připojuje přes rozhraní SGi. Její nejdůležitější vztah je s její řídicí funkcí PGW-C, se kterou komunikuje pomocí protokolu [PFCP](/mobilnisite/slovnik/pfcp/) (Packet Forwarding Control Protocol) definovaného v TS 29.244. PGW-C funguje jako řídicí prvek (master), který posílá řídicí příkazy, zatímco PGW-U funguje jako vykonavatel (slave), který tyto příkazy provádí na provozu uživatelské roviny.

Její činnost je řízena pravidly. PGW-C instaluje v PGW-U pravidla prostřednictvím PFCP relací. Tato pravidla zahrnují [PDR](/mobilnisite/slovnik/pdr/) (Packet Detection Rules), které identifikují, na které pakety uživatelské roviny se má působit, na základě kritérií, jako jsou identifikátory koncových bodů tunelů ([TEID](/mobilnisite/slovnik/teid/), Tunnel Endpoint Identifier), IP adresy a čísla portů. Pro pakety odpovídající PDR aplikuje PGW-U odpovídající FAR (Forwarding Action Rules), které určují akce, jako je přeposlání paketu do konkrétního tunelu (např. směrem k SGW-U nebo externí síti), jeho zahození nebo uložení do vyrovnávací paměti. Aplikuje také QER (QoS Enforcement Rules) pro označení paketů pomocí DSCP (DiffServ Code Point), vynucení limitů přenosové rychlosti pro uplink/downlink a přiřazení identifikace QoS toku.

PGW-U vykonává několik klíčových funkcí uživatelské roviny. Slouží jako kotvící bod pro mobilitu, což znamená, že IP adresa UE je zde ukotvena, což zajišťuje kontinuitu relace, když se uživatel pohybuje a mění se přístupový bod sítě (např. SGW-U). Provádí inspekci paketů a vynucení tarifních politik počítáním paketů/bajtů na služební datový tok podle pokynů URR (Usage Reporting Rules) a odesílá hlášení o využití PGW-C pro účely účtování. Také zajišťuje zákonné odposlechy duplikací paketů podle požadavků. Oddělená povaha PGW-U umožňuje její implementaci jako vysoce výkonné funkce, potenciálně s hardwarovou akcelerací, kterou lze nasadit na distribuovaných místech, například na okraji sítě, aby se snížila latence pro aplikace, jako je rozšířená realita nebo autonomní vozidla.

## K čemu slouží

PGW-U byla vytvořena za účelem řešení problémů se škálovatelností a nedostatečnou flexibilitou nasazení, které byly vlastní monolitickému návrhu P-GW v sítích EPC před Release 14. V tradiční architektuře byly uživatelská a řídicí rovina těsně integrovány v rámci jediného fyzického nebo virtuálního síťového zařízení. Toto propojení znamenalo, že škálování pro zvládnutí většího objemu datového provozu uživatelské roviny vyžadovalo škálování celého uzlu včetně prostředků řídicí roviny, což bylo neefektivní a nákladné. Také vynucovalo centralizovaný model nasazení, který operátorům bránil umístit funkce přenosu dat blíže uživatelům za účelem zlepšení výkonu.

Hnací silou jejího vývoje byl průmyslový trend směrem k virtualizaci sítí, cloud-nativnímu návrhu a potřeba podpory různorodých služeb s nízkou latencí očekávaných u 5G. Architektura CUPS, která toto oddělení formalizovala, byla přímou odpovědí. Vytvořením samostatné PGW-U získali operátoři možnost nezávisle a masivně škálovat datovou rovinu pomocí běžného hardwaru nebo specializovaných akcelerátorů datové roviny. Také umožnila distribuované nasazení, což umožňuje umístit funkce uživatelské roviny do centrálních ústředen, agregačních míst základnových stanic nebo přímo do základnové stanice (jako u Mobile Edge Computing), což radikálně snižuje dobu odezvy pro aplikace kritické na latenci.

Toto oddělení navíc odpovídá principům SDN (Software-Defined Networking), kde je řídicí logika (PGW-C) centralizovaná a programovatelná, zatímco přeposílací elementy (PGW-U) jsou jednoduché a distribuované. Tento model zjednodušuje správu sítě, umožňuje rychlejší zavádění nových služeb a snižuje provozní náklady. Koncept PGW-U se přímo vyvinul ve funkci uživatelské roviny (UPF, User Plane Function) v síti 5G Core, čímž se stal klíčovým architektonickým mezníkem. Vyřešil problémy monolitického škálování, nedostatku flexibility nasazení a nemožnosti optimalizovat současně efektivitu signalizace řídicí roviny a propustnost/nízkou latenci uživatelské roviny, což byly významná omezení pro zvládání exponenciálního růstu a vyvíjejících se požadavků mobilního širokopásmového provozu.

## Klíčové vlastnosti

- Přeposílání a směrování paketů: Kotví uživatelské relace a směruje IP pakety mezi přístupovou sítí (přes SGW-U) a externími PDN.
- Zpracování založené na pravidlech: Provádí pravidla pro detekci paketů, přeposílání, vynucování QoS a hlášení využití, která nainstalovala PGW-C prostřednictvím PFCP.
- Vynucování QoS: Aplikuje politiky QoS označováním paketů (DSCP), vynucováním garantovaných a maximálních přenosových rychlostí a správou QoS toků.
- Hlášení využití: Sleduje a počítá uživatelský provoz na služební datový tok a hlásí využití PGW-C pro účely účtování.
- Kotva mobility: Slouží jako stabilní IP kotvící bod pro PDN připojení UE během událostí mobility a zajišťuje kontinuitu relace.
- Podpora zákonného odposlechu: Umí duplikovat a zrcadlit provoz uživatelské roviny podle požadavků pro účely zákonného odposlechu.

## Související pojmy

- [PGW-C – PDN Gateway Control plane function](/mobilnisite/slovnik/pgw-c/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [P-GW – Packet Data Network Gateway](/mobilnisite/slovnik/p-gw/)
- [PFCP – Packet Forwarding Control Protocol](/mobilnisite/slovnik/pfcp/)

## Definující specifikace

- **TS 23.214** (Rel-19) — Control and User Plane Separation for EPC
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 28.708** (Rel-19) — EPC NRM Integration Reference Point Information Service
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 29.844** (Rel-14) — Control and User Plane Separation for EPC Nodes
- **TS 32.867** (Rel-15) — Management Impacts of EPC CUPS
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [PGW-U na 3GPP Explorer](https://3gpp-explorer.com/glossary/pgw-u/)
