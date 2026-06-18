---
slug: "tsctsf"
url: "/mobilnisite/slovnik/tsctsf/"
type: "slovnik"
title: "TSCTSF – Time Sensitive Communication and Time Synchronization Function"
date: 2026-01-01
abbr: "TSCTSF"
fullName: "Time Sensitive Communication and Time Synchronization Function"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tsctsf/"
summary: "Funkce jádra sítě 5G zavedená ve specifikaci 3GPP Release 17 pro podporu deterministické, nízkolatenční a vysoce spolehlivé komunikace s přesnou časovou synchronizací. Umožňuje průmyslové IoT, řízení"
---

TSCTSF je funkce jádra sítě 5G, která poskytuje deterministickou, nízkolatenční a spolehlivou komunikaci s přesnou synchronizací času pro podporu průmyslového IoT a dalších časově citlivých aplikací.

## Popis

Funkce pro časově citlivou komunikaci a synchronizaci času (TSCTSF) je klíčovou síťovou funkcí jádra sítě 5G, standardizovanou od specifikace 3GPP Release 17. Je centrální architektonickou entitou navrženou k umožnění schopností časově citlivého sítí ([TSN](/mobilnisite/slovnik/tsn/)) a přesné distribuce času v systémech 5G. TSCTSF se nachází v řídicí rovině jádra 5G a spolupracuje s dalšími funkcemi jádra, jako je funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)), funkce zpřístupnění sítě ([NEF](/mobilnisite/slovnik/nef/)) a funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)), aby orchestrovala služby deterministické komunikace end-to-end.

Architektonické má TSCTSF několik klíčových rolí. Za prvé funguje jako most mezi systémem 5G a externí sítí TSN (nebo aplikací podporující TSN), často reprezentovanou TSN překladačem nebo centralizovaným síťovým řadičem ([CNC](/mobilnisite/slovnik/cnc/)). Výměňuje konfiguraci a požadavky specifické pro TSN, jako jsou seznamy řízení bran pro plánovaný provoz a informace o synchronizaci času, prostřednictvím NEF nebo přímých rozhraní. Za druhé je TSCTSF zodpovědná za správu a konfiguraci systému 5G jako virtuálního mostu TSN. To zahrnuje překlad požadavků TSN na parametry a politiky QoS specifické pro 5G, které poskytuje PCF a následně funkci správy relací ([SMF](/mobilnisite/slovnik/smf/)) a UPF. Pro synchronizaci času se TSCTSF podílí na distribuci přesného časování z hlavního zdroje času (který může být uvnitř nebo vně sítě 5G) k uživatelským zařízením (UE) a UPF, což zajišťuje, že všechny uzly na komunikační cestě jsou zarovnány ke společnému časovému referenčnímu bodu, často s využitím profilu [IEEE](/mobilnisite/slovnik/ieee/) 802.1AS (gPTP).

Z provozního hlediska TSCTSF pracuje ve spojení s rámcem QoS systému 5G k vytváření vyhrazených toků QoS se zaručenou (GFBR) a maximální ([MFBR](/mobilnisite/slovnik/mfbr/)) přenosovou rychlostí toku spolu s přísným prioritním plánováním pro splnění požadavků na latenci a spolehlivost. Konfiguruje UPF tak, aby fungovala jako mluvčí/posluchač a most TSN, implementuje tvarování provozu (např. řízení bran na bázi front podle IEEE 802.1Qbv) na rozhraní N6 směrem k datové síti. TSCTSF také podporuje mechanismy pro redundanci a bezproblémovou redundanci definované v IEEE 802.1CB (replikace a eliminace rámců pro spolehlivost) koordinací více cest přes UPF. Její rozhraní, jako je Ntsctsf, jsou definována pro interakci založenou na službách uvnitř jádra 5G, což umožňuje ostatním síťovým funkcím žádat o služby časově citlivé komunikace.

## K čemu slouží

Vytvoření TSCTSF bylo motivováno požadavkem průmyslového sektoru používat 5G jako jednotnou komunikační páteř pro kritické aplikace, jako je automatizace továren, řízení pohybu a monitorování procesů. Tyto aplikace mají přísné požadavky na deterministickou latenci (často submilisekundovou), ultra vysokou spolehlivost (až 99,9999 %) a přesnou synchronizaci (s přesností na mikrosekundy), které tradiční best-effort mobilní sítě nemohly garantovat. Předchozí vydání specifikací 3GPP se zaměřovala na vylepšené mobilní širokopásmové připojení (eMBB) a ultra spolehlivou nízkolatenční komunikaci (URLLC), ale postrádala konkrétní podporu pro paradigma plánování a synchronizace standardizovaná v sadě IEEE TSN.

TSCTSF konkrétně řeší problém integrace systémů 5G do průmyslových sítí podporujících TSN. Před jejím zavedením neexistoval standardizovaný způsob, jak by se síť 5G mohla jevit jako virtuální deterministický most v doméně TSN, ani jak by se mohla účastnit centralizovaného konfiguračního modelu TSN. TSCTSF tuto mezeru překlenuje a umožňuje, aby bylo 5G spravováno jako součást větší sítě řízené TSN. Řeší výzvu překladu konceptů časově citlivého tvarování a plánovaného provozu TSN na proveditelné konfigurace QoS a uživatelské roviny v 5G, což umožňuje deterministické toky end-to-end, které bezproblémově procházejí jak drátovými segmenty TSN, tak bezdrátovými segmenty 5G. To umožňuje konvergenci sítí operační technologie (OT) a informační technologie (IT) na jedné infrastruktuře 5G.

## Klíčové vlastnosti

- Orchestruje konfiguraci systému 5G pro fungování jako virtuální most TSN
- Překládá požadavky aplikací TSN (např. seznamy řízení bran) do politik QoS v 5G
- Spravuje distribuci přesné časové synchronizace (např. gPTP) napříč uživatelskými zařízeními (UE) a UPF v 5G
- Podporuje tvarování provozu TSN (IEEE 802.1Qbv) a plánovaný provoz na rozhraní N6
- Umožňuje ultra spolehlivou komunikaci prostřednictvím koordinace pro replikaci a eliminaci rámců (IEEE 802.1CB)
- Poskytuje rozhraní založená na službách (Ntsctsf) pro interakci s PCF, NEF a AF

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.539** (Rel-19) — NW-TT Protocol Aspects
- **TR 28.839** (Rel-18) — Technical Report
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.521** (Rel-19) — 5G Binding Support Management Service Stage 3
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 29.534** (Rel-19) — 5G Access & Mobility Policy Authorization Service
- **TS 29.564** (Rel-19) — Nupf Service Based Interface Protocol
- **TS 29.565** (Rel-19) — Time Synchronization Function Services
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [TSCTSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/tsctsf/)
