---
slug: "son"
url: "/mobilnisite/slovnik/son/"
type: "slovnik"
title: "SON – Self-Organizing Network"
date: 2026-01-01
abbr: "SON"
fullName: "Self-Organizing Network"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/son/"
summary: "SON automatizuje konfiguraci, optimalizaci a léčení mobilních sítí. Snižuje provozní náklady a zlepšuje síťový výkon minimalizací manuálních zásahů. To je klíčové pro řízení rostoucí složitosti modern"
---

SON je soubor automatizačních schopností pro mobilní sítě, které konfigurují, optimalizují a léčí síť za účelem snížení provozních nákladů a zlepšení výkonu minimalizací manuálních zásahů.

## Popis

Self-Organizing Network (SON) je komplexní rámec automatizačních funkcí navržených pro plánování, konfiguraci, správu, optimalizaci a léčení mobilních rádiových přístupových a jádrových sítí. Jeho architektura je distribuována napříč síťovými prvky jako [eNB](/mobilnisite/slovnik/enb/)/gNB a centralizována v Operations Support System ([OSS](/mobilnisite/slovnik/oss/)) nebo Network Management System ([NMS](/mobilnisite/slovnik/nms/)). SON funkce fungují prostřednictvím kombinace mechanismů self-configuration (automatická konfigurace), self-optimization (automatická optimalizace) a self-healing (automatické léčení). Self-configuration automatizuje počáteční nastavení nových síťových uzlů, včetně přiřazení Physical Cell ID, vytvoření tabulky sousedních vztahů (Neighbor Relation Table, [NRT](/mobilnisite/slovnik/nrt/)) a automatického stažení softwaru. Self-optimization kontinuálně monitoruje klíčové ukazatele výkonu (Key Performance Indicators, KPIs), jako jsou míra spadlých hovorů, úspěšnost předání spojení (handover) a úrovně interference, a následně upravuje parametry, jako je sklon antény (antenna tilt), handover prahové hodnoty a nastavení výkonu, pro udržení optimálního výkonu. Self-healing zahrnuje automatickou detekci, diagnostiku a kompenzaci síťových poruch, jako jsou výpadky buněk, spuštěním mechanismů jako cell breathing nebo úpravou parametrů sousedních buněk pro pokrytí zasažené oblasti.

Rámec podporuje tři hlavní architektonické paradigmaty: Centralized SON (C-SON), kde algoritmy běží v OSS/NMS; Distributed SON (D-SON), kde jsou algoritmy vestavěny do rádiových síťových uzlů (eNB/gNB) pro rychlé lokální reakce; a Hybrid SON, který kombinuje oba přístupy. Klíčové komponenty zahrnují rozhraní Network Management ([NM](/mobilnisite/slovnik/nm/)) a Domain Management ([DM](/mobilnisite/slovnik/dm/)) (Itf-N a Itf-S), Northbound Interface (NBI) pro SON aplikace třetích stran a standardizované SON funkce jako Automatic Neighbor Relation ([ANR](/mobilnisite/slovnik/anr/)), Mobility Robustness Optimization ([MRO](/mobilnisite/slovnik/mro/)), Mobility Load Balancing (MLB) a Coverage and Capacity Optimization (CCO). SON se opírá o kontinuální smyčku sběru měření, vyhodnocení výkonu, rozhodování a úpravy parametrů, často využívající politiky a prahové hodnoty definované operátorem.

V síťovém ekosystému je SON nedílnou součástí rámce 3GPP Management and Orchestration (MANO), interaguje s Network Functions Virtualization (NFV) a Software-Defined Networking (SDN) pro dynamickou orchestraci zdrojů. Jeho role se rozšířila od 4G LTE k 5G NR, kde řídí složité scénáře jako optimalizace svazků Massive MIMO, dual-connectivity a síťové segmenty (network slicing). Automatizace SON je klíčová pro umožnění zero-touch network and service management (ZSM), snížení provozních výdajů (OPEX) a zajištění konzistentní Quality of Experience (QoE) pro koncové uživatele v rostoucí hustotě a heterogenitě síťových nasazení.

## K čemu slouží

SON byl vytvořen k řešení rostoucí provozní složitosti a nákladů spojených s manuální správou sítí, jak se mobilní sítě vyvíjely od 3G k 4G a dále. Rozmnožení síťových uzlů, zejména se zavedením LTE a small cells, učinilo tradiční procesy manuálního plánování, optimalizace a řešení problémů nepřijatelně časově náročnými, náchylnými k chybám a drahými. SON automatizuje tyto opakující se a složité úlohy, umožňuje rychlejší nasazení sítě, efektivnější využití rádiových zdrojů a zlepšenou kvalitu služeb. Přímo řeší výzvu síťového zhušťování a heterogenity, kde tisíce buněk s překrývajícím se pokrytím vyžadují neustálou koordinaci pro minimalizaci interference a zajištění plynulé mobility.

Historicky byla síťová optimalizace reaktivním procesem náročným na drive-testy, prováděným týmy inženýrů. Tento přístup nemohl škálovat, aby uspokojil požadavky ploché architektury LTE a očekávanou hustotu 5G sítí. SON poskytuje proaktivní, daty řízenou a automatizovanou alternativu. Řeší kritické problémy jako suboptimální parametry handoveru způsobující spadlé hovory, nevyvážené zatížení vedoucí k přetížení některých buněk, zatímco jiné jsou málo využité, a dlouhou dobu obnovy po výpadku buňky. Vestavěním inteligence do samotné sítě umožňuje SON operátorům efektivněji spravovat 'sítě sítí', což je základním požadavkem pro dosažení vysoké spolehlivosti, nízké latence a masivní konektivity cílů 5G a budoucích 6G systémů.

## Klíčové vlastnosti

- Automatické zjišťování a správa sousedních vztahů (Automatic Neighbor Relation, ANR)
- Optimalizace robustnosti mobility (Mobility Robustness Optimization, MRO) pro minimalizaci selhání předání spojení (handover)
- Vyvažování zátěže mobility (Mobility Load Balancing, MLB) pro distribuci provozu napříč buňkami
- Optimalizace pokrytí a kapacity (Coverage and Capacity Optimization, CCO) prostřednictvím úprav parametrů antén
- Automatická konfigurace Physical Cell Identity (PCI) a Root Sequence Index (RSI)
- Funkce automatického léčení (Self-Healing) pro automatickou detekci poruch a kompenzaci

## Související pojmy

- [ANR – Automatic Neighbour Relationship](/mobilnisite/slovnik/anr/)
- [MRO – Mobility Robustness Optimisation](/mobilnisite/slovnik/mro/)
- [CCO – Capacity and Coverage Optimization](/mobilnisite/slovnik/cco/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 28.561** (Rel-20) — Management and Orchestration; Network Digital Twin
- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 28.631** (Rel-19) — Inventory Management NRM IRP Requirements
- **TR 28.841** (Rel-18) — Technical Report on IoT NTN Enhancements
- **TS 32.130** (Rel-19) — Network Sharing OAM&P Requirements
- **TS 32.521** (Rel-11) — SON Policy NRM IRP Requirements
- **TS 32.522** (Rel-11) — SON Policy NRM IRP Information Service
- **TS 32.541** (Rel-19) — SON Self-Healing Concepts and Requirements
- **TS 32.582** (Rel-19) — HNB Management Information Model for Type 1 Interface
- **TS 32.584** (Rel-19) — HNB OAM&P XML Definitions for Type 1 Interface
- **TS 32.592** (Rel-19) — HeNB OAM&P Information Model
- **TS 32.594** (Rel-19) — Data definitions for HeNB to HeMS Type 1 interface
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [SON na 3GPP Explorer](https://3gpp-explorer.com/glossary/son/)
