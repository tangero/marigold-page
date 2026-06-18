---
slug: "dts"
url: "/mobilnisite/slovnik/dts/"
type: "slovnik"
title: "DTS – Data Transport Service"
date: 2026-01-01
abbr: "DTS"
fullName: "Data Transport Service"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dts/"
summary: "Data Transport Service (DTS) je základní koncept služby 3GPP zahrnující spolehlivý, efektivní a na QoS orientovaný přenos uživatelských dat a signalizace po síti. Tvoří základ všech služeb založených"
---

DTS je základní služba 3GPP pro spolehlivý, efektivní a na QoS orientovaný přenos uživatelských dat a signalizace, která poskytuje architektonický rámec pro veškerou IP komunikaci.

## Popis

Data Transport Service (DTS) v 3GPP není jediný protokol nebo uzel, ale komplexní koncept služební vrstvy, který abstrahuje koncový přenos datových paketů. Je definován v řadě specifikací, včetně požadavků na služby (řada 22.x), architektury (23.700) a především rámce Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) (29.212, 29.213, 29.214). DTS představuje schopnost sítě doručit IP pakety mezi uživatelským zařízením (UE) a paketovou datovou sítí ([PDN](/mobilnisite/slovnik/pdn/)) se specifickými charakteristikami kvality služby (QoS), pravidly účtování a vynucováním politik.

Z architektonického hlediska je DTS realizován interakcí několika funkcí jádra sítě. Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v EPC nebo Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC slouží jako kotvící body pro službu přenosu dat. Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/) v EPC) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/) v 5GC) je řídícím centrem DTS, které určuje politiky řídící tuto službu. Tyto politiky jsou vynucovány v bránových uzlech (PGW/UPF) a v rádiové přístupové síti (eNodeB/gNB) prostřednictvím funkce Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)) nebo jejích ekvivalentů. Rámec DTS definuje Service Data Flows (SDFs), což jsou agregáty IP paketů odpovídajících filtru, a váže je na QoS Flows (v 5G) nebo EPS Bearers (v 4G).

Jak to funguje, zahrnuje vícekrokový proces. Nejprve UE požádá o PDN spojení nebo PDU Session. Síť (SMF/MME) komunikuje s politikovou funkcí (PCF/PCRF) za účelem stanovení příslušných politik pro tuto session. Politiková funkce poskytuje pravidla Policy and Charging Control (PCC), která zahrnují parametry jako QoS Class Identifier (QCI/5QI), limity přenosové rychlosti, účtovací klíče a řízení přístupu (povolit/blokovat). Tato pravidla jsou instalována v uživatelských rovinových bránách a v RAN. Každý paket procházející uživatelskou rovinou je kontrolován a klasifikován do SDF. Na základě klasifikace SDF je aplikováno odpovídající PCC pravidlo, což zajišťuje, že paket obdrží předepsané QoS zacházení (priorita plánování, zpracování rozpočtu zpoždění paketů) a je zaznamenán pro účely účtování.

Role DTS je klíčová pro posun architektury 3GPP k plně IP sítím. Odděluje aplikační vrstvu (např. IMS, prohlížení webu) od základních transportních mechanismů. To umožňuje vytváření standardizovaných, sítí řízených QoS profilů pro různé služby – od her s nízkou latencí po hromadné hlášení ze senzorů IoT – na společné IP infrastruktuře. Rámec DTS zajišťuje, že transportní prostředky jsou přidělovány efektivně, spravedlivě a v souladu s politikami operátora a profily účastníků, čímž tvoří páteř zpeněžitelné služební diferenciace.

## K čemu slouží

Koncept Data Transport Service byl vytvořen, aby řešil základní výzvu řízení různorodých služeb založených na IP přes sdílenou infrastrukturu mobilní sítě. V časných mobilních datových sítích byl přenos často "best-effort" kanál s omezenou schopností rozlišovat provoz. S příchodem služeb jako VoIP, video streamování a podnikové VPN vznikla kritická potřeba standardizovaných mechanismů pro zaručení specifických úrovní výkonu (latence, kolísání, ztráta) a pro aplikaci diferencovaného účtování.

Historicky, před-3GPP IP sítě nebo raný GPRS postrádaly jednotný rámec pro řízení politik. Diferenciace služeb byla ad-hoc nebo nemožná, což vedlo ke špatnému uživatelskému zážitku u aplikací reálného času a neschopnosti vytvářet služby na různých úrovních. Rámec DTS, vykrystalizovaný kolem PCC architektury zavedené ve Release 7 a dále rozšířené, byl motivován potřebou centralizovaného, dynamického a na aplikace citlivého systému řízení politik. Vyřešil problém, jak převést požadavky služeb na vysoké úrovni (např. "toto je IMS hlasový hovor") na konkrétní akce na síťové úrovni (např. "přiřaď bearer se zaručenou přenosovou rychlostí a vysokou prioritou").

Dále DTS umožňuje síťové slicing v 5G tím, že poskytuje základní služební mechanismus pro vytváření a řízení izolovaných cest přenosu dat se specifickými charakteristikami pro různé slice. Řeší obchodní potřebu operátorů posunout se za jednoduché účtování datových balíčků k sofistikovanému služebnímu účtování a partnerským modelům (např. sponzorovaná data). V podstatě DTS existuje proto, aby vnesl řád, kontrolu a možnost zpeněžení do chaotického toku IP paketů v mobilní síti, čímž činí pokročilé, spolehlivé služby komerčně a technicky životaschopnými.

## Klíčové vlastnosti

- Abstrakce koncového přenosu IP paketů s definovatelnými charakteristikami QoS
- Centralizované řízení politik prostřednictvím PCRF/PCF určující QoS, řízení přístupu a pravidla účtování
- Dynamické vynucování politik v uživatelských rovinových bránách (PGW/UPF) a RAN uzlech
- Klasifikace provozu do Service Data Flows (SDFs) na základě paketových filtrů
- Vázání SDFs na standardizované QoS Flows (5G) nebo EPS Bearers (4G)
- Podpora služebního účtování, včetně integrace offline a online účtování

## Související pojmy

- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 22.153** (Rel-20) — Multimedia Priority Service (MPS) requirements
- **TR 22.854** (Rel-17) — Feasibility Study on Multimedia Priority Service - Phase 2
- **TR 22.953** (Rel-19) — Multimedia Priority Service Feasibility Study
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [DTS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dts/)
