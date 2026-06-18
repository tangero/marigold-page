---
slug: "scg"
url: "/mobilnisite/slovnik/scg/"
type: "slovnik"
title: "SCG – Secondary Cell Group"
date: 2026-01-01
abbr: "SCG"
fullName: "Secondary Cell Group"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/scg/"
summary: "Skupina sekundárních buněk v konfiguracích dual connectivity (DC), spravovaná sekundárním uzlem (např. gNB v NR), která poskytuje uživatelskému zařízení dodatečné rádiové prostředky. Funguje společně"
---

SCG je skupina sekundárních buněk spravovaná sekundárním uzlem v dual connectivity, která spolu s hlavní skupinou buněk poskytuje uživatelskému zařízení dodatečné rádiové prostředky.

## Popis

Sekundární skupina buněk (SCG) je základním konceptem v architekturách dual connectivity ([DC](/mobilnisite/slovnik/dc/)) a multi-connectivity od 3GPP, zavedeným od Release 12. Ve scénáři DC je uživatelské zařízení (UE) současně připojeno ke dvěma uzlům: k hlavnímu uzlu ([MN](/mobilnisite/slovnik/mn/)) spravujícímu hlavní skupinu buněk ([MCG](/mobilnisite/slovnik/mcg/)) a k sekundárnímu uzlu ([SN](/mobilnisite/slovnik/sn/)) spravujícímu SCG. SCG se skládá z jedné nebo více sekundárních buněk (SCell) poskytovaných SN, které mohou být stejné nebo jiné rádiové přístupové technologie ([RAT](/mobilnisite/slovnik/rat/)) než MCG – například LTE MCG s NR SCG v [EN-DC](/mobilnisite/slovnik/en-dc/) (E-UTRA-NR Dual Connectivity). SCG přidává další rádiové prostředky, čímž zvyšuje celkovou šířku pásma a zlepšuje datovou propustnost, spolehlivost a robustnost mobility.

Architektonicky je SCG řízena SN, která spravuje radioresource management ([RRM](/mobilnisite/slovnik/rrm/)) pro své buňky, včetně plánování, konfigurace rozdělení bearerů a mobility v rámci SCG. MN si ponechává kontrolu nad MCG a koordinuje celkové připojení UE, spravuje signalizaci jako [RRC](/mobilnisite/slovnik/rrc/) spojení a handover. Datové toky mohou být rozděleny v různých bodech: bearery mohou být ukončeny na MN (MCG bearery), na SN (SCG bearery) nebo rozděleny mezi oběma (split bearery). SCG využívá pro koordinaci s MCG rozhraní jako X2 (mezi eNB v LTE) nebo Xn (mezi gNB v NR). Klíčové procedury zahrnují přidání, modifikaci a uvolnění SCG, které jsou spouštěny na základě měřicích reportů a síťových politik pro optimalizaci výkonu.

SCG funguje s konkrétními aspekty fyzické a protokolové vrstvy: SCell v rámci SCG mohou být dynamicky aktivovány/deaktivovány pro úsporu energie a podporují principy carrier aggregation (CA). V SCG založených na NR jsou uplatnitelné funkce jako části šířky pásma (BWP) a flexibilní numerologie. SCG zlepšuje výkon sítě tím, že umožňuje vyrovnávání zátěže, snižuje doby přerušení během handoverů a podporuje náročné use case jako enhanced mobile broadband (eMBB). Je nedílnou součástí nasazení 5G non-standalone (NSA), kde LTE slouží jako kotva pro řízení, zatímco NR SCG poskytuje vysokorychlostní data. S vývojem multi-connectivity se koncept SCG rozšiřuje na scénáře s více RAT a tvoří základ pro pokročilé agregační techniky v 5G-Advanced a dalších verzích.

## K čemu slouží

SCG byla vytvořena, aby řešila rostoucí poptávku po vyšších datových rychlostech a spolehlivějších spojeních, kterou nemohla plně uspokojit single connectivity nebo carrier aggregation v rámci jednoho uzlu. Před Release 12 spoléhal LTE Advanced na carrier aggregation (CA) v rámci jediného eNB, což bylo omezeno dostupným spektrem a možnostmi lokality. Dual connectivity s SCG umožňuje agregaci prostředků z geograficky oddělených základnových stanic, čímž zvyšuje celkovou šířku pásma a poskytuje zisky z makro-diverzity. Toto vyřešilo problémy jako degradace výkonu na okraji buňky a kapacitní úzká místa, zejména v heterogenních sítích s malými buňkami.

S přechodem na 5G se SCG stala klíčovou pro plynulou migraci, protože umožňuje vzájemnou spolupráci LTE-NR v non-standalone režimu. Umožnila operátorům využít stávající LTE infrastrukturu pro pokrytí a řízení a zároveň přidat NR SCG pro vylepšené datové schopnosti, čímž řešila výzvu nasazení 5G bez kompletní výměny jádra sítě. SCG také podporuje kontinuitu služeb a ultra-spolehlivou komunikaci s nízkou latencí (URLLC) tím, že umožňuje redundantní cesty. Její vývoj byl motivován potřebou flexibilních a efektivních řešení multi-connectivity pro podporu různých 5G use case a vývoje sítě.

## Klíčové vlastnosti

- Poskytuje dodatečné rádiové prostředky prostřednictvím sekundárních buněk spravovaných sekundárním uzlem.
- Umožňuje dual connectivity napříč stejnými nebo různými RAT (např. LTE a NR).
- Podporuje typy bearerů: MCG bearery, SCG bearery a split bearery.
- Umožňuje dynamickou aktivaci/deaktivaci SCell pro energetickou účinnost.
- Zlepšuje datovou propustnost, spolehlivost a mobilitu prostřednictvím multi-connectivity.
- Integruje se s carrier aggregation a pokročilými funkcemi NR, jako jsou části šířky pásma (BWP).

## Související pojmy

- [EN-DC – E-UTRA NR Dual Connectivity with MCG using E-UTRA and SCG using NR](/mobilnisite/slovnik/en-dc/)

## Definující specifikace

- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.825** (Rel-16) — Security for 5G URLLC Services
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.410** (Rel-19) — S1 Interface: General Aspects and Principles
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- … a dalších 27 specifikací

---

📖 **Anglický originál a plná specifikace:** [SCG na 3GPP Explorer](https://3gpp-explorer.com/glossary/scg/)
