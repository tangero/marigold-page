---
slug: "w-agf"
url: "/mobilnisite/slovnik/w-agf/"
type: "slovnik"
title: "W-AGF – Wireline Access Gateway Function"
date: 2026-01-01
abbr: "W-AGF"
fullName: "Wireline Access Gateway Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/w-agf/"
summary: "W-AGF je funkce jádra sítě 5G, která poskytuje pevný drátový přístup do systému 5G. Slouží jako brána převádějící protokoly z pevných sítí (jako DSL, PON) na protokoly jádra 5G, což umožňuje spravovat"
---

W-AGF je funkce jádra sítě 5G, která slouží jako brána převádějící protokoly pevného drátového přístupu na protokoly jádra 5G, aby umožnila připojení drátových zařízení do systému 5G.

## Popis

Funkce brány drátového přístupu (Wireline Access Gateway Function, W-AGF) je klíčová síťová funkce zavedená v systému 5G (5GS) pro integraci pevných drátových přístupových sítí, jako je Digital Subscriber Line ([DSL](/mobilnisite/slovnik/dsl/)), pasivní optické sítě ([PON](/mobilnisite/slovnik/pon/)) a sítě založené na Ethernetu, do jádra 5G. Nachází se v uživatelské i řídicí rovině a funguje jako prostředník mezi drátovým zařízením na straně zákazníka (Customer Premises Equipment, [CPE](/mobilnisite/slovnik/cpe/)) a jádrem sítě 5G (5GC). Z architektonického hlediska W-AGF ukončuje specifické přístupové protokoly drátových sítí od CPE a provádí potřebné funkce pro vzájemnou spolupráci (interworking), aby prezentovala drátový přístup jako typ přístupu 5G pro jádro. Implementuje referenční body [N2](/mobilnisite/slovnik/n2/) a N3 směrem k funkci správy přístupu a mobility (Access and Mobility Management Function, [AMF](/mobilnisite/slovnik/amf/)) a funkci uživatelské roviny (User Plane Function, [UPF](/mobilnisite/slovnik/upf/)), což jí umožňuje účastnit se standardních procedur 5G, jako je registrace, správa relací a řízení politik.

Z funkční perspektivy je W-AGF zodpovědná za autentizaci a autorizaci drátového CPE nebo koncových uživatelských zařízení za ním. Mapuje drátové relace na relace protokolové datové jednotky (Protocol Data Unit, [PDU](/mobilnisite/slovnik/pdu/)) 5G, spravuje toky kvality služeb (Quality of Service, QoS) a uplatňuje politiky přijaté od funkce řízení politik (Policy Control Function, [PCF](/mobilnisite/slovnik/pcf/)). W-AGF také zpracovává aspekty mobility a správy relací specifické pro pevnou povahu přístupu, jako je správa topologie drátové přístupové sítě a poskytování informací o poloze připojených zařízení. Podporuje procedury pro vzájemnou spolupráci 3GPP i non-3GPP, čímž zajišťuje bezproblémovou kontinuitu služeb a vynucování politik.

Role W-AGF se rozšiřuje i na oblast zabezpečení, kde napomáhá odvozování klíčů a správě bezpečnostního kontextu pro drátový spoj. Spolupracuje s funkcí bezpečnostní kotvy (Security Anchor Function, SEAF) a autentizační serverovou funkcí (Authentication Server Function, AUSF) při provádění procedur autentizace a dohody o klíčích 5G. Dále W-AGF poskytuje možnosti provozu, správy a údržby (operations, administration, and maintenance, OAM), které umožňují síťovým operátorům monitorovat a spravovat integraci drátového přístupu. Její nasazení je klíčovým kamenem pro strategie 5G Fixed Wireless Access (FWA) a konvergovaných sítí, protože umožňuje operátorům využít stávající drátovou infrastrukturu a zároveň nabízet moderní služby 5G.

## K čemu slouží

W-AGF byla vytvořena jako reakce na trend v odvětví směřující ke konvergenci sítí, konkrétně k integraci pevných a mobilních sítí pod jednotnou architekturu jádra 5G. Před jejím zavedením pevné širokopásmové sítě a mobilní sítě fungovaly převážně odděleně, s vlastními jádry sítí, systémy správy a platformami pro poskytování služeb. Toto oddělení vedlo k provozní neefektivitě, duplikaci funkcí a neschopnosti nabízet skutečně bezproblémové služby, které by mohly přecházet mezi pevným a mobilním přístupem. W-AGF tento problém řeší tím, že poskytuje standardizovanou bránu, která umožňuje, aby byla jakákoli pevná drátová přístupová síť považována za nativní typ přístupu 5G.

Historicky se o konvergenci pevných a mobilních sítí pokoušely starší technologie, ale často to zahrnovalo složité proprietární brány nebo mělo omezený rozsah. Systém 5G se svou architekturou založenou na službách a jasným oddělením přístupu od jádra poskytl ideální rámec pro standardizované řešení. W-AGF umožňuje operátorům modernizovat nabídku svých pevných sítí jejich připojením k agilnímu, cloud-nativnímu jádru 5G. To umožňuje aplikovat konzistentní politiky 5G, bezpečnostní modely a možnosti síťového řezání (network slicing) na drátové účastníky. Zásadně řeší problém fragmentace přístupu, umožňuje nové obchodní modely jako 5G FWA a usnadňuje poskytování konzistentního uživatelského zážitku napříč všemi typy přístupových sítí.

## Klíčové vlastnosti

- Vzájemná spolupráce protokolů mezi drátovými sítěmi (např. PPP, DHCP, 802.1X) a jádrem 5G (NGAP, PFCP)
- Mapování drátových relací na relace PDU 5G včetně správy toků QoS
- Podpora autentizačních a bezpečnostních procedur 5G (5G-AKA, EAP-AKA') přes drátový přístup
- Integrace s řídicí rovinou 5GC prostřednictvím rozhraní N2 k AMF
- Integrace s uživatelskou rovinou 5GC prostřednictvím rozhraní N3 k UPF
- Vynucování politik pro drátový přístup na základě pokynů od PCF

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.413** (Rel-19) — NGAP for Non-3GPP Access
- **TS 29.502** (Rel-19) — 5G System; Nsmf Service Based Interface; Stage 3
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.509** (Rel-19) — AUSF Service Based Interface Protocol
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 29.594** (Rel-19) — 5G Spending Limit Control Service Stage 3
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)

---

📖 **Anglický originál a plná specifikace:** [W-AGF na 3GPP Explorer](https://3gpp-explorer.com/glossary/w-agf/)
