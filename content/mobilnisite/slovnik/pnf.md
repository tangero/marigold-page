---
slug: "pnf"
url: "/mobilnisite/slovnik/pnf/"
type: "slovnik"
title: "PNF – Physical Network Function"
date: 2026-01-01
abbr: "PNF"
fullName: "Physical Network Function"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/pnf/"
summary: "Tradiční, vyhrazená síťová funkce realizovaná jako hardwarové zařízení, například fyzický router, firewall nebo entita pro správu mobility. Je v protikladu k virtualizovaným síťovým funkcím (VNF) a je"
---

PNF je tradiční, vyhrazená síťová funkce realizovaná jako hardwarové zařízení, například fyzický router nebo firewall, což je v protikladu k virtualizovaným softwarovým protějškům.

## Popis

Fyzická síťová funkce (Physical Network Function, PNF) označuje síťovou funkci implementovanou jako vyhrazené proprietární hardwarové zařízení s těsně svázaným softwarem. Na rozdíl od svého virtualizovaného protějšku ([VNF](/mobilnisite/slovnik/vnf/)) je software PNF neoddělitelně spojen s konkrétním fyzickým hardwarem, na kterém běží. Příklady PNF v mobilní síti zahrnují tradiční jednotky základního pásma ([BBU](/mobilnisite/slovnik/bbu/)), fyzické routery, hardwarové firewally, zařízení pro hlubokou kontrolu paketů (DPI) a legacy uzly jádra sítě, jako jsou entity pro správu mobility ([MME](/mobilnisite/slovnik/mme/)) nebo servisní brány ([S-GW](/mobilnisite/slovnik/s-gw/)), implementované jako samostatné fyzické boxy. PNF je samostatná entita s vlastními výpočetními, úložnými a síťovými prostředky, často od jediného dodavatele, a je spravována jako monolitická jednotka.

Architektonicky PNF komunikuje se zbytkem sítě prostřednictvím standardních fyzických nebo logických rozhraní (např. S1, [N2](/mobilnisite/slovnik/n2/), N3, N6). Její vnitřní správa a životní cyklus jsou však pro externí orchestrátor neprůhledné. Systém správy komunikuje s PNF prostřednictvím dodavatelsky specifického rozhraní nebo standardizovaného rozhraní pro správu PNF (PNFM), které poskytuje fasádu pro základní správu FCAPS (poruchy, konfigurace, účtování, výkon, bezpečnost). PNF abstrahuje svou vnitřní složitost a prezentuje se jako spravovatelná entita, ale nevystavuje podrobné prostředky, jako jsou virtuální [CPU](/mobilnisite/slovnik/cpu/) nebo paměť, pro orchestraci.

V kontextu moderních síťových architektur, jako je 5G a virtualizace síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)), představuje PNF legacy nebo specializovanou komponentu v převážně virtualizovaném prostředí. Její role je klíčová pro integraci stávající infrastruktury, nasazení funkcí, kde je vyžadováno hardwarové zrychlení nebo fyzická bezpečnost, nebo pro případy, kdy virtualizace ještě není technicky nebo ekonomicky proveditelná. Správa hybridních sítí, skládajících se z PNF i VNF/[CNF](/mobilnisite/slovnik/cnf/) (cloud-nativních síťových funkcí), je ústřední výzvou, kterou řeší rámce jako ETSI NFV, které definují deskriptory a manažery PNF pro začlenění těchto fyzických prvků do softwarově řízeného paradigmatu orchestrace a správy.

## K čemu slouží

PNF představují tradiční paradigma nasazení telekomunikačních sítí, kde byla každá funkce dodávána jako integrované hardwarové a softwarové zařízení od dodavatele. Účelem tohoto modelu bylo poskytnout vysoce výkonné, spolehlivé a často operátorské síťové vybavení optimalizované pro specifické úkoly, jako je směrování, přepínání nebo signalizace. Tato zařízení byla navržena s redundancí, specializovanými ASIC a operačními systémy reálného času, aby splňovala přísné požadavky telekomunikačních sítí na dostupnost a latenci.

Koncept PNF získal obnovenou formální definici s příchodem principů NFV a cloud-nativního přístupu kolem 3GPP Release 15. Když se sítě začaly virtualizovat, bylo nutné formálně rozlišit mezi novými softwarovými VNF a stávající instalovanou základnou fyzických zařízení. Koncept PNF byl definován, aby řešil problém správy hybridní sítě během přechodu. Umožňuje, aby byly legacy a specializovaný hardware reprezentovány a spravovány v rámci stejných rámců orchestrace a správy (jako je NFV-MANO) jako jejich virtualizované protějšky.

Tato formalizace řeší kritickou integrační výzvu. Bez abstrakce PNF by byli síťoví operátoři nuceni spravovat virtualizované a fyzické domény prostřednictvím zcela oddělených systémů, což by zvyšovalo provozní složitost a náklady. Definováním PNF jako spravovatelných entit s deskriptory a standardními rozhraními umožnily 3GPP a ETSI NFV jednotný přístup k poskytování služeb, správě poruch a monitorování výkonu napříč heterogenními síťovými infrastrukturami, čímž chránily stávající investice při migraci k softwarově definované budoucnosti.

## Klíčové vlastnosti

- Implementována jako vyhrazené, dodavatelsky specifické hardwarové zařízení s integrovaným softwarem.
- Poskytuje síťovou funkcionalitu s těsně svázaným hardwarem a softwarem, což nabízí vysoký výkon a spolehlivost.
- Spravována jako monolitická entita prostřednictvím dodavatelsky specifických rozhraní nebo standardizovaného rozhraní pro správu PNF (PNFM).
- Reprezentuje stávající legacy infrastrukturu nebo funkce vyžadující specializovaný hardware (např. rádiové jednotky, kryptografický hardware).
- Integrována do rámců NFV prostřednictvím deskriptoru PNF (PNFD) pro správu životního cyklu společně s VNF.
- Prezentuje se orchestrátorům sítě jako black-box abstrakce, která skrývá vnitřní podrobnosti o prostředcích.

## Související pojmy

- [VNF – Virtualized Network Function](/mobilnisite/slovnik/vnf/)
- [CNF – Conjunctive Normal Form](/mobilnisite/slovnik/cnf/)
- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)
- [PNM – Personal Network Management](/mobilnisite/slovnik/pnm/)

## Definující specifikace

- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.310** (Rel-19) — Energy Efficiency Management for 5G Networks
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 28.890** (Rel-16) — ONAP-3GPP 5G Management Compatibility Study
- **TR 32.972** (Rel-19) — Energy Efficiency Study for 5G Networks
- **TR 33.848** (Rel-18) — Technical Report on Virtualisation Security

---

📖 **Anglický originál a plná specifikace:** [PNF na 3GPP Explorer](https://3gpp-explorer.com/glossary/pnf/)
