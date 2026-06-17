---
slug: "msc-s"
url: "/mobilnisite/slovnik/msc-s/"
type: "slovnik"
title: "MSC-S – Mobile Switching Centre Server"
date: 2025-01-01
abbr: "MSC-S"
fullName: "Mobile Switching Centre Server"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/msc-s/"
summary: "Řídicí rovinný prvek v architektuře sítě 3GPP All-IP, který odděluje funkce řízení hovoru a přepojování. Zpracovává signalizaci pro služby s přepojováním okruhů a spolupracuje s Media Gateway (MGW) pr"
---

MSC-S je řídicí rovinný prvek v síti 3GPP All-IP, který zpracovává signalizaci pro služby s přepojováním okruhů, odděluje řízení hovoru od přepojování a spolupracuje s Media Gateway pro přenos přenosových kanálů.

## Popis

Mobile Switching Centre Server (MSC-S) je prvek jádra sítě zavedený jako součást architektury 3GPP All-IP a IP Multimedia Subsystem (IMS). Představuje vývoj tradičního monolitického [MSC](/mobilnisite/slovnik/msc/) oddělením funkcí řízení hovoru (signalizace) od funkcí přepojování médií (přenosových kanálů). MSC-S je zodpovědný za veškerou signalizaci řízení hovoru a správy mobility pro služby s přepojováním okruhů, jako jsou hlasové hovory a data s přepojováním okruhů. Komunikuje s uživatelským zařízením (UE) a dalšími síťovými uzly pomocí signalizačních protokolů, jako je [BSSAP](/mobilnisite/slovnik/bssap/) přes rozhraní A pro přístup 2G, RANAP přes rozhraní Iu-CS pro přístup 3G a [ISUP](/mobilnisite/slovnik/isup/)/BICC pro propojení s jinými sítěmi.

Architektonicky MSC-S spolupracuje s Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) pod kontrolou funkce Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) nebo přímo přes rozhraní Mc pomocí protokolů jako H.248 (Megaco). MSC-S dává pokyny MGW k vytváření, úpravám a uvolňování mediálních spojení (přenosových kanálů) pro uživatelský provoz, který je přenášen přes IP nebo [ATM](/mobilnisite/slovnik/atm/) sítě namísto tradičních TDM okruhů. Toto oddělení umožňuje nasazení MSC-S jako softwarové entity na standardních serverech, což zvyšuje škálovatelnost a flexibilitu. MSC-S také obsahuje funkci VLR pro správu dat navštěvujících účastníků, provádění autentizace a zpracování aktualizací polohy.

Při provozu MSC-S zpracovává požadavky na sestavení hovoru, provádí analýzu čísel a směrování, spravuje předávání hovoru (včetně přesunu SRNS v UMTS) a realizuje doplňkové služby. Rozhraní s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo [HLR](/mobilnisite/slovnik/hlr/) pro data účastníka. Pro tísňová volání může obsahovat specifické směrovací funkce. MSC-S podporuje jak starší služby s přepojováním okruhů, tak umožňuje konvergenci směrem k IP sítím, čímž slouží jako most během přechodu z TDM na jádrové sítě typu all-IP.

## K čemu slouží

MSC-S byl vytvořen, aby řešil omezení tradičního monolitického MSC, které kombinovalo řídicí a přepojovací funkce v jedné, často proprietární, hardwarové platformě. Tato architektura byla nepružná, nákladná na škálování a bránila zavádění nových služeb. Přechod k sítím All-IP vyžadoval oddělení funkcí, aby bylo možné využít IP přenos a standardní výpočetní platformy.

Jeho vývoj byl motivován potřebou modernizace sítě, snížení provozních nákladů a umožnění inovací služeb. Oddělením řídicí roviny (MSC-S) od mediální roviny (MGW) mohli operátoři každou z nich škálovat a inovovat nezávisle, nasazovat služby rychleji a přejít z TDM na paketové páteřní sítě. MSC-S je klíčovým prvkem strategie vývoje jádra sítě 3GPP, usnadňuje konvergenci pevných a mobilních sítí a připravuje cestu pro multimediální služby založené na IMS.

## Klíčové vlastnosti

- Signalizace řízení hovoru a správy mobility pro služby s přepojováním okruhů
- Oddělení řídicí a uživatelské roviny, rozhraní s Media Gateway přes H.248
- Podpora signalizace pro rozhraní A (2G) a Iu-CS (3G)
- Integrovaná funkce Visitor Location Register (VLR)
- Umožňuje vývoj sítě směrem k architektuře All-IP
- Podpora řízení předávání hovoru a přesunu SRNS pro UMTS

## Související pojmy

- [MGW – Media Gateway](/mobilnisite/slovnik/mgw/)

## Definující specifikace

- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TR 23.977** (Rel-19) — Bandwidth/Resource Savings & Speech Quality Requirements
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TS 32.407** (Rel-19) — PM; CN CS Domain; UMTS/GSM measurements

---

📖 **Anglický originál a plná specifikace:** [MSC-S na 3GPP Explorer](https://3gpp-explorer.com/glossary/msc-s/)
