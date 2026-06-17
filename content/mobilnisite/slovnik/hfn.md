---
slug: "hfn"
url: "/mobilnisite/slovnik/hfn/"
type: "slovnik"
title: "HFN – Hyper Frame Number"
date: 2025-01-01
abbr: "HFN"
fullName: "Hyper Frame Number"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hfn/"
summary: "Hyper Frame Number (HFN) je čítač používaný v protokolech 3GPP k rozšíření rozsahu sekvenčních čísel, zejména pro šifrování a ochranu integrity. Spolupracuje s kratšími sekvenčními čísly (SN) a vytvář"
---

HFN je čítač používaný v protokolech 3GPP k rozšíření rozsahu sekvenčních čísel pro šifrování a ochranu integrity, který tvoří delší parametr COUNT pro zajištění kryptografické synchronizace a prevenci replay útoků.

## Popis

Hyper Frame Number (HFN) je klíčová součást bezpečnostních a protokolových mechanismů 3GPP, která funguje jako vyšší část čítače používaného k generování kryptografických klíčů a zajištění čerstvosti dat. Používá se spolu s kratším sekvenčním číslem (SN) k vytvoření delší, složené hodnoty COUNT. Například v LTE a NR má parametr COUNT používaný v algoritmech šifrování a ochrany integrity typicky délku 32 bitů a skládá se z 20- až 25bitového HFN a 7- až 12bitového SN v závislosti na rádiovém beareru a konkrétním protokolu. SN se zvyšuje s každou protokolovou datovou jednotkou (PDU) a po dosažení své maximální hodnoty přeteče, načež se HFN zvýší o jedničku, čímž se efektivně rozšíří rozsah čítače na biliony rámců a zabrání se opětovnému použití stejné hodnoty COUNT v praktickém časovém horizontu.

Z architektonického hlediska je HFN nezávisle udržován jak odesílatelem, tak příjemcem (např. UE a základnovou stanicí nebo UE a jádrem sítě) pro každý rádiový bearer nebo signalizační spojení. Synchronizace HFN je zásadní; obvykle se inicializuje během procedur navázání spojení nebo předání a následně se aktualizuje na základě přetečení SN. Specifikace 3GPP definují přesná pravidla pro správu HFN, aby se předešlo desynchronizaci, která by mohla vést k selhání dešifrování nebo neshodám kontrol integrity. Ve scénářích, jako jsou předání, může být HFN přenesen nebo přepočítán, aby byla zachována kontinuita. HFN se také používá v jiných kontextech, například v Packet Data Convergence Protocol (PDCP) pro číslování sekvencí a v některých případech pro časové zarovnání.

Role HFN je zásadní pro bezpečnost a spolehlivost mobilních sítí. Poskytnutím obrovského prostoru čítače zajišťuje, že stejný šifrovací klíčový proud není znovu použit, což je nezbytné pro prevenci kryptografických útoků, jako je opakované použití klíčového proudu. Také podporuje ochranu integrity tím, že poskytuje vstup pro parametry čerstvosti. Správa HFN je těsně integrována s procedurami mobility, včetně předání a obnovení spojení, aby bylo zajištěno bezproblémové pokračování zabezpečení. Její implementace je transparentní pro vyšší vrstvy, ale je životně důležitá pro podpůrný bezpečnostní rámec, který chrání uživatelská data a signalizaci napříč generacemi 3GPP od UMTS po 5G NR.

## K čemu slouží

Hyper Frame Number byl zaveden, aby řešil omezení konečných prostorů sekvenčních čísel v kryptografických protokolech. Rané mobilní systémy používaly pro šifrování pouze sekvenční čísla, ale s rostoucím objemem dat mohla tato sekvenční čísla přetéct příliš rychle, což vedlo k opětovnému použití kryptografických klíčových proudů – což je závažná bezpečnostní slabina. HFN rozšiřuje efektivní délku čítače a zajišťuje, že kombinovaná hodnota COUNT (HFN || SN) se během životnosti bezpečnostního klíče neopakuje, čímž udržuje kryptografickou sílu a zabraňuje replay útokům.

Historicky se tento koncept vyvinul ze šifrovacích mechanismů GSM a byl formálně integrován do standardů 3GPP počínaje UMTS (Release 4), aby poskytl robustní zabezpečení pro nové paketově orientované domény. Motivací bylo podporovat dlouhodobé relace a vysoké přenosové rychlosti bez kompromisů v zabezpečení. Bez HFN by bylo nutné časté obnovování klíčů, což by zvyšovalo signalizační režii a potenciálně narušovalo služby. HFN umožňuje efektivní dlouhodobou bezpečnostní synchronizaci, která je zvláště kritická pro služby typu „always-on“ a IoT zařízení s dlouhou výdrží baterie. Řeší problém správy zabezpečené komunikace po potenciálně roky trvající provoz zařízení bez opakování klíče, což je základním požadavkem moderních mobilních sítí.

## Klíčové vlastnosti

- Rozšiřuje rozsah sekvenčních čísel, aby zabránil opakování kryptografického čítače
- Tvoří vyšší část parametru COUNT pro šifrování a ochranu integrity
- Synchronizován mezi odesílatelem a příjemcem pro udržení bezpečnostního kontextu
- Zvyšuje se při přetečení přidruženého sekvenčního čísla (SN)
- Spravován během událostí mobility, jako jsou předání a obnovení spojení
- Nedílná součást PDCP a bezpečnostních protokolů napříč generacemi 3GPP

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 38.323** (Rel-19) — Packet Data Convergence Protocol (PDCP)
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [HFN na 3GPP Explorer](https://3gpp-explorer.com/glossary/hfn/)
