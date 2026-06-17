---
slug: "cim"
url: "/mobilnisite/slovnik/cim/"
type: "slovnik"
title: "CIM – Common Information Model"
date: 2025-01-01
abbr: "CIM"
fullName: "Common Information Model"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/cim/"
summary: "CIM (Common Information Model) je dodavatelem neutrální, objektově orientovaný informační model pro popis a správu IT a síťových prostředků. V rámci 3GPP umožňuje standardizovanou výměnu řídicích dat"
---

CIM (Common Information Model) je dodavatelem neutrální, objektově orientovaný model pro popis IT a síťových prostředků, který umožňuje standardizovanou výměnu řídicích dat v systémech 3GPP za účelem zajištění interoperability v prostředí více dodavatelů.

## Popis

Common Information Model (CIM) je komplexní, na schématech založený informační model původně vyvinutý Distributed Management Task Force ([DMTF](/mobilnisite/slovnik/dmtf/)). Poskytuje konzistentní definici a strukturu pro popis a reprezentaci spravovaných prostředků, jako jsou počítačové systémy, sítě, aplikace a služby, jednotným, objektově orientovaným způsobem. V 3GPP je CIM využíván v rámci specifikací správy k usnadnění standardizovaného datového modelování pro telekomunikační síťové prvky, což umožňuje bezproblémovou výměnu informací mezi systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)), systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)) a síťovými funkcemi. Model používá třídy, vlastnosti, asociace a metody k abstrakci reálných entit, což umožňuje přesné sémantické definice nezávislé na konkrétních implementacích nebo platformách.

Architektonicky je CIM strukturován na základní model (Core Model) a společné modely (Common Models). Základní model definuje základní koncepty použitelné ve všech doménách, jako jsou systémy, služby a závislosti. Společné modely rozšiřují základní model pro řešení konkrétních domén; v kontextech 3GPP to zahrnuje modely pro výkon sítě, správu poruch, správu konfigurace a zajištění služeb. Model je typicky vyjádřen v Unified Modeling Language (UML) a může být serializován do XML pro výměnu dat prostřednictvím protokolů jako CIM-XML přes [HTTP](/mobilnisite/slovnik/http/) nebo WBEM (Web-Based Enterprise Management). To umožňuje řídicím aplikacím standardizovaným způsobem zjišťovat, přistupovat k nim a manipulovat se spravovanými objekty bez ohledu na podkladový hardware nebo software.

V rámci řídicích rámců 3GPP hraje CIM klíčovou roli v rozhraních, jako je Itf-N (Interface-Northbound) a specifikacích řídicích služeb. Poskytuje schéma pro data správy výkonu (PM), alarmy správy poruch ([FM](/mobilnisite/slovnik/fm/)) a parametry správy konfigurace ([CM](/mobilnisite/slovnik/cm/)), což zajišťuje, že data z různorodých síťových prvků – jako základnové stanice, uzly jádra sítě nebo virtualizované síťové funkce – mohou být konzistentně interpretována. Mezi klíčové komponenty patří třídy spravovaných objektů (např. CIM_ManagedElement pro obecné prostředky), asociace (např. CIM_Dependency pro modelování vztahů) a kvalifikátory pro přidávání metadat. Použitím CIM dosahuje 3GPP interoperability v sítích více dodavatelů, zjednodušuje integraci nových technologií a podporuje automatizované operace, jako je provisioning, monitorování a odstraňování problémů.

Implementace CIM v 3GPP zahrnuje mapování síťově specifických konceptů – jako jsou 5G síťové řezy, QoS toky nebo kontexty UE – do tříd a vlastností CIM. Toto mapování je podrobně popsáno v technických specifikacích, jako jsou 32.622 a 32.642, které definují, jak je modelována telekomunikační řídicí informace. Například gNodeB může být reprezentován jako podtřída CIM_ComputerSystem s vlastnostmi pro identifikátory buněk a provozní stavy. Řídicí systémy používají tyto modely ke sběru metrik, nastavování konfigurací a přijímání notifikací, což umožňuje správu služeb end-to-end. Rozšiřitelnost CIM umožňuje 3GPP začleňovat nové funkce napříč vydáními, jako je síťové krájení nebo edge computing, bez narušení stávajících řídicích rozhraní.

## K čemu slouží

CIM byl vytvořen k řešení výzev správy heterogenních [IT](/mobilnisite/slovnik/it/) a síťových prostředí, kde proprietární datové modely vedly k problémům s interoperabilitou, vysokým integračním nákladům a provozní neefektivitě. Před CIM každý dodavatel často používal jedinečná schémata pro reprezentaci spravovaných prostředků, což ztěžovalo řídicím systémům agregaci dat, automatizaci procesů nebo podporu sítí více dodavatelů. [DMTF](/mobilnisite/slovnik/dmtf/) vyvinulo CIM jako otevřený standard, aby poskytlo společný jazyk pro popis prostředků, což umožňuje konzistentní správu napříč různorodými systémy. V telekomunikacích 3GPP přijalo CIM ke standardizaci řídicích rozhraní, zejména když se sítě vyvíjely směrem k více softwarově definovaným a virtualizovaným komponentám, což vyžadovalo agilní, interoperabilní řídicí řešení.

Primární problém, který CIM řeší v sítích 3GPP, je absence jednotného informačního modelu pro výměnu řídicích dat. Bez něj se operátoři potýkali s izolovanými řídicími systémy, manuálním překladem dat a omezenými možnostmi automatizace, zejména ve složitých nasazeních zahrnujících více dodavatelů nebo cloud-nativní síťové funkce. CIM poskytuje dodavatelem neutrální základ, který umožňuje síťovým prvkům – ať už od tradičních dodavatelů hardwaru nebo nových softwarových poskytovatelů – vystavovat řídicí data v konzistentním formátu. To podporuje klíčové cíle 3GPP, jako je snížení provozních nákladů (OPEX), umožnění plug-and-play integrace a usnadnění pokročilých řídicích funkcí, jako jsou samoorganizující se sítě (SON) a automatizace v uzavřené smyčce.

Historicky motivace pro integraci CIM do 3GPP vycházela z potřeby sladit se se širšími postupy správy IT a podpořit konvergenci mezi telekomunikační a IT doménami. Jak sítě přijímaly technologie založené na IP a později virtualizaci (např. NFV), použití zavedeného standardu jako CIM umožnilo 3GPP využít stávající nástroje a odborné znalosti. Řeší omezení předchozích ad-hoc přístupů tím, že poskytuje škálovatelný, rozšiřitelný model, který se může vyvíjet spolu se síťovými technologiemi, od 3G přes 5G a dále. Standardizací na CIM zajišťuje 3GPP, že se řídicí systémy mohou přizpůsobit novým službám, jako je síťové krájení nebo IoT, aniž by vyžadovaly kompletní přepracování řídicích rozhraní.

## Klíčové vlastnosti

- Dodavatelem neutrální, objektově orientované schéma pro reprezentaci prostředků
- Rozšiřitelné základní a společné modely podporující telekomunikačně specifické domény
- Standardizovaná výměna dat prostřednictvím protokolů CIM-XML a WBEM
- Interoperabilita napříč síťovými prvky a řídicími systémy více dodavatelů
- Podpora modelování dat pro správu výkonu, poruch a konfigurace
- Integrace s řídicími rozhraními 3GPP, jako je Itf-N, pro automatizované operace

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 28.708** (Rel-19) — EPC NRM Integration Reference Point Information Service
- **TS 29.198** (Rel-9) — OSA API Overview Specification
- **TS 32.622** (Rel-11) — Generic Network Resources IRP NRM
- **TS 32.642** (Rel-11) — UTRAN Network Resource Model for Configuration Management
- **TS 32.652** (Rel-12) — GERAN Network Resources NRM for Configuration Management
- **TS 32.692** (Rel-11) — Inventory Management NRM IRP Specification
- **TS 32.712** (Rel-11) — Transport Network Interface NRM for CM
- **TS 32.742** (Rel-11) — STN NRM for Configuration Management
- **TS 32.752** (Rel-11) — EPC NRM IRP Information Service
- **TR 37.829** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [CIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/cim/)
