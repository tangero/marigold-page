---
slug: "dtd"
url: "/mobilnisite/slovnik/dtd/"
type: "slovnik"
title: "DTD – Document Type Definition"
date: 2025-01-01
abbr: "DTD"
fullName: "Document Type Definition"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/dtd/"
summary: "V 3GPP je DTD soubor definice XML schématu, který formálně popisuje strukturu, elementy a atributy XML dokumentů používaných pro výměnu dat na rozhraních správy sítě. Zajišťuje, že konfigurační, chybo"
---

DTD je soubor definice XML schématu, který formálně popisuje strukturu, elementy a atributy XML dokumentů používaných pro standardizovanou výměnu dat mezi síťovými prvky (Network Elements) a systémy pro podporu provozu (Operations Support Systems) v rámci správy sítí 3GPP.

## Popis

Ve standardech 3GPP, zejména těch souvisejících se správou sítě (např. specifikace řady 32 a 28), je Document Type Definition (DTD) schématovací jazyk používaný k definování povolených stavebních bloků dokumentu Extensible Markup Language ([XML](/mobilnisite/slovnik/xml/)). Specifikuje strukturu dokumentu pomocí seznamu platných elementů a atributů. V kontextu správy 3GPP se XML dokumenty používají jako datový formát pro informační modely a pro výměnu řídicích informací přes rozhraní jako je Itf-N (Interface-Northbound) nebo v rámci frameworku Integration Reference Point ([IRP](/mobilnisite/slovnik/irp/)). Tyto dokumenty mohou reprezentovat spravované objekty (Managed Objects), notifikace, konfigurační data, výkonnostní měření nebo hlášení poruch.

Z architektonického hlediska jsou DTD součástí specifikací Solution Set ([SS](/mobilnisite/slovnik/ss/)), které implementují abstraktní informační modely definované v IRP 3GPP. IRP definuje, *jaké* informace je třeba spravovat (např. hlášení alarmů pro základnovou stanici). Odpovídající SS, který zahrnuje soubory DTD, definuje, *jak* jsou tyto informace konkrétně reprezentovány v XML pro přenos. Soubor DTD (s příponou .dtd) deklaruje elementy jako `<AlarmInformation>` a specifikuje, že musí obsahovat podřízené elementy `<probableCause>` a `<perceivedSeverity>` a může mít atributy jako `distinguishedName`. Tím poskytuje formální gramatiku, které se musí dodržovat jak na straně producenta (např. správce síťového prvku), tak konzumenta (např. systém správy sítě) XML dat, čímž zajišťuje syntaktickou interoperabilitu.

Proces fungování DTD při výměně dat správy zahrnuje několik kroků. Nejprve specifikace řídicího rozhraní vyžaduje použití konkrétní sady DTD. Když řídicí systém potřebuje získat konfiguraci ze síťového prvku, může odeslat požadavek založený na XML strukturovaný podle DTD pro 'Get'. Síťový prvek odpoví XML dokumentem platným vůči DTD pro 'Response', obsahujícím skutečná konfigurační data strukturovaná podle odpovídajících DTD pro 'Managed Object'. Před zpracováním dat může přijímací systém ověřit příchozí XML dokument vůči odkazovanému DTD, aby zajistil, že je správně formován a odpovídá očekávané struktuře. Toto ověření je účinným nástrojem pro ladění a zajištění robustní komunikace mezi systémy od různých výrobců.

Zatímco DTD je jedna z metod pro definování struktury XML, specifikace správy 3GPP také přijaly XML Schema Definition ([XSD](/mobilnisite/slovnik/xsd/)), což je výkonnější a výraznější schématovací jazyk. XSD podporuje datové typy, jmenné prostory a složitější omezení. V mnoha pozdějších vydáních 3GPP specifikace poskytují jak DTD, tak XSD definice pro stejný informační model, aby podpořily starší i moderní systémy. Role DTD je tedy klíčovým umožňovatelem standardizované, na souborech založené výměny informací v síťové správě. Operátorům umožňuje automatizovat sběr a provisioning obrovského množství síťových dat tím, že poskytuje striktní, dohodnutý formát, který software může spolehlivě parsovat a generovat, což je nezbytné pro provoz rozsáhlých, heterogenních mobilních sítí.

## K čemu slouží

Použití DTD ve standardech správy 3GPP řeší kritický problém interoperability v síťové správě s více výrobci. Na počátku 21. století, kdy sítě rostly a stávaly se složitějšími s vybavením od mnoha dodavatelů, se proprietární formáty řídicích dat staly hlavní překážkou efektivního provozu. Účelem standardizace DTD bylo definovat společný, jednoznačný jazyk pro reprezentaci řídicích informací, umožňující systémům správy sítě ([NMS](/mobilnisite/slovnik/nms/)) od jednoho výrobce efektivně komunikovat se síťovými prvky (NEs) nebo systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)) od jiného.

Jejich vytvoření bylo motivováno posunem odvětví k datově centrickým, automatizovaným systémům pro podporu provozu ([OSS](/mobilnisite/slovnik/oss/)). Ruční konfigurace a správa založená na [CLI](/mobilnisite/slovnik/cli/) byly pro rozsáhlá nasazení 3G neudržitelné. 3GPP ve spolupráci s TeleManagement Forum (TMF) přijalo XML jako lingua franca pro řídicí data díky jeho flexibilitě a čitelnosti pro člověka. Samotné XML je však pouze syntaxe; bez striktní definice povoleného obsahu by mohl každý výrobce vytvářet platná, ale nekompatibilní XML. DTD (a později XSD) poskytla potřebnou sémantickou definici, čímž proměnila XML v robustní formát pro výměnu dat. Vyřešila problém 'jak vypadá platná alarmová zpráva?' způsobem, který lze strojově zpracovat.

Historicky byly DTD základní technologií pro implementaci frameworku IRP 3GPP. Umožnily první vlnu standardizovaných northbound rozhraní (Itf-N) pro správu chyb, konfigurace, výkonu a zabezpečení. Zatímco novější specifikace často dávají přednost XSD díky jeho bohatší sadě funkcí, DTD zůstávají specifikovány kvůli zpětné kompatibilitě a v kontextech, kde je jejich jednoduchost výhodou. Hlavní účel zůstává: zajistit, aby řídicí data vyměňovaná přes standardizovaná rozhraní byla předvídatelná, ověřitelná a nakonec použitelná přijímacím systémem, což je předpokladem pro automatizovanou korekci chyb, optimalizaci výkonu a zajištění služeb v moderních telekomunikačních sítích.

## Klíčové vlastnosti

- Definuje platnou strukturu, elementy a atributy XML dokumentů pro správu 3GPP
- Umožňuje syntaktické ověření XML dat vyměňovaných přes řídicí rozhraní (např. Itf-N)
- Implementuje konkrétní Solution Sets pro abstraktní informační modely Integration Reference Point (IRP)
- Deklaruje pořadí elementů, jejich výskyt a modely datového obsahu (PCDATA, elementy)
- Je odkazováno v XML dokumentech pomocí deklarace DOCTYPE
- Usnadňuje interoperabilitu více výrobců při výměně dat síťové správy

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 28.606** (Rel-12) — CN and non-3GPP interworking NRM IRP Solution Sets
- **TS 28.616** (Rel-19) — EPC and non-3GPP access NRM IRP SS definitions
- **TS 28.626** (Rel-19) — State Management Data Definition IRP Solution Set
- **TS 28.629** (Rel-19) — SON Policy NRM IRP Solution Set Definitions
- **TS 28.633** (Rel-19) — Inventory Management NRM IRP Solution Set definitions
- **TS 28.653** (Rel-19) — UTRAN NRM IRP Solution Set Definition
- **TS 28.656** (Rel-19) — GERAN NRM IRP Solution Set Definitions
- **TS 28.659** (Rel-19) — E-UTRAN NRM IRP Solution Set Definitions
- **TS 28.663** (Rel-19) — Generic RAN NRM IRP Solution Set Definitions
- **TS 28.673** (Rel-19) — HNS NRM IRP Solution Set Definitions
- **TS 28.676** (Rel-19) — HeNS NRM IRP Solution Set Definitions
- **TS 28.703** (Rel-19) — Core Network NRM IRP Solution Set Definitions
- **TS 28.706** (Rel-19) — IMS NRM IRP Solution Set definitions
- **TS 28.709** (Rel-19) — EPC NRM IRP Solution Set Definitions
- … a dalších 50 specifikací

---

📖 **Anglický originál a plná specifikace:** [DTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtd/)
