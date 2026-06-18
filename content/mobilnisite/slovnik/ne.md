---
slug: "ne"
url: "/mobilnisite/slovnik/ne/"
type: "slovnik"
title: "NE – Network Element"
date: 2026-01-01
abbr: "NE"
fullName: "Network Element"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ne/"
summary: "Základní spravovatelná logická nebo fyzická entita v telekomunikační síti, například základnová stanice, přepínač nebo směrovač. Je základní jednotkou správy sítě, která zpřístupňuje rozhraní pro sprá"
---

NE (síťový prvek) je základní spravovatelná logická nebo fyzická entita v telekomunikační síti, například základnová stanice nebo směrovač, která slouží jako základní jednotka správy sítě.

## Popis

Síťový prvek (NE) je základním konceptem správy sítí 3GPP a představuje jakoukoli samostatnou, spravovatelnou entitu, která tvoří část telekomunikační sítě. NE může být fyzické zařízení (jako eNodeB, gNB, [MME](/mobilnisite/slovnik/mme/) nebo [SGW](/mobilnisite/slovnik/sgw/)), virtualizovaná síťová funkce ([VNF](/mobilnisite/slovnik/vnf/)), softwarová komponenta nebo dokonce logické seskupení zdrojů. Z pohledu správy je NE charakterizováno schopností být spravováno prostřednictvím standardizovaného rozhraní, typicky rozhraní Itf-N nebo jiných rozhraní pro správu definovaných v architektuře 3GPP Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)). Každé NE obsahuje spravované objekty, které reprezentují jeho zdroje, schopnosti a aktuální stav.

Architektura správy sítě je postavena kolem NE. Jsou spravovány systémy vyšší úrovně, jako jsou systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)), systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)) nebo orchestrační systémy. NE implementuje agenta správy, který komunikuje s těmito manažery pomocí protokolů jako [SNMP](/mobilnisite/slovnik/snmp/), NETCONF/YANG nebo protokolů založených na [CORBA](/mobilnisite/slovnik/corba/) dle specifikací 3GPP. Rozhraní pro správu umožňuje provádění základních operací FCAPS: správu poruch (reportování alarmů, oznámení událostí), správu konfigurace (zřizování, aktualizace softwaru), účtování (sběr dat o využití), správu výkonu (reportování čítačů a měření) a správu zabezpečení (řízení přístupu, auditní záznamy).

Vnitřní fungování NE se liší podle jeho funkce, ale z pohledu správy udržuje bázi informací pro správu (MIB) nebo ekvivalentní informační model, který definuje všechny spravovatelné atributy. Například gNB jako NE by zpřístupňovalo spravované objekty pro své buňky, konfigurace antén, připojená UE, stav hardwaru a verze softwaru. Úlohou NE je poskytnout normalizovaný pohled na svou vnitřní složitost vrstvě správy, abstrahující výrobcem specifické detaily prostřednictvím standardizovaných informačních modelů. Tato abstrakce je klíčová pro interoperabilitu více dodavatelů a automatizované síťové operace. V moderních virtualizovaných sítích může být NE cloud-nativní síťová funkce (CNF) běžící v kontejneru, jejíž rozhraní pro správu zpřístupňuje kromě tradičních telekomunikačních funkcí také parametry životního cyklu a elasticity.

## K čemu slouží

Koncept síťového prvku byl formalizován, aby řešil výzvu správy stále složitějších telekomunikačních sítí s více dodavateli. V raných sítích byla správa často proprietární a specifická pro zařízení, což činilo rozsáhlou integrovanou správu sítě téměř nemožnou. Koncept NE vytváří společnou abstraktní vrstvu, definující jakoukoli síťovou komponentu jako spravovatelnou entitu se standardní sadou rozhraní a chování. Tím řeší problém heterogenity poskytnutím jednotného modelu, pomocí kterého mohou manažery komunikovat s různorodým hardwarem a softwarem od různých dodavatelů.

Jeho vznik byl motivován potřebou škálovatelné správy poruch, konfigurace a výkonu. Tím, že se každá významná síťová komponenta považuje za NE s definovaným rozhraním pro správu, mohli operátoři budovat centralizované systémy podpory provozu (OSS), které automatizují úlohy napříč celou sítí. Historicky se to vyvinulo z jednoduchých manažerů prvků komunikujících s jednotlivými zařízeními až k sofistikovaným NMS spravujícím tisíce NE. NE je atomární jednotkou automatizace správy; bez tohoto standardizovaného konceptu by uzavřená smyčka automatizace, samoorganizující se sítě (SON) a správa založená na záměru byly nepraktické. Tvoří základ všech specifikací správy 3GPP a umožňuje vizi síťových komponent typu plug-and-play a zjednodušených operací.

## Klíčové vlastnosti

- Představuje logickou nebo fyzickou spravovatelnou entitu v síti
- Zpřístupňuje standardizované rozhraní pro správu (např. Itf-N) pro operace FCAPS
- Obsahuje bázi informací pro správu (MIB) definující jeho spravované objekty
- Může být fyzický síťový uzel, virtualizovaná síťová funkce (VNF) nebo softwarová komponenta
- Generuje a reportuje poruchy, měření výkonu a události
- Přijímá a provádí konfigurační příkazy ze systémů správy

## Související pojmy

- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 28.301** (Rel-19) — LSA Controller IRP Requirements
- **TS 28.311** (Rel-19) — Policy Management for 4G Networks
- **TS 28.314** (Rel-20) — Management and Orchestration - Plug and Connect
- **TS 28.624** (Rel-19) — State Management Data Definition IRP Requirements
- **TS 28.625** (Rel-19) — State Management Data Definition IRP Information Service
- **TS 28.626** (Rel-19) — State Management Data Definition IRP Solution Set
- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- **TS 28.632** (Rel-19) — Inventory Management NRM Integration Reference Point
- **TS 28.655** (Rel-19) — GERAN NRM IRP Information Service
- **TS 28.662** (Rel-19) — Generic RAN Network Resource Model (NRM) IRP IS
- **TS 28.680** (Rel-19) — WLAN Management Concepts and Requirements
- **TS 28.681** (Rel-19) — WLAN Management NRM IRP Requirements
- **TS 28.701** (Rel-19) — Core Network NRM IRP Requirements
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- … a dalších 145 specifikací

---

📖 **Anglický originál a plná specifikace:** [NE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ne/)
