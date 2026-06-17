---
slug: "asme"
url: "/mobilnisite/slovnik/asme/"
type: "slovnik"
title: "ASME – Access Security Management Entity"
date: 2025-01-01
abbr: "ASME"
fullName: "Access Security Management Entity"
category: "Security"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/asme/"
summary: "Access Security Management Entity (ASME, entita pro správu přístupové bezpečnosti) je logická funkce v sítích 3GPP zodpovědná za správu bezpečnostních klíčů pro uživatelské zařízení (UE) během procedu"
---

ASME je logická funkce v sítích 3GPP zodpovědná za správu bezpečnostních klíčů pro uživatelské zařízení během autentizace a za odvozování přístupově specifických klíčů používaných pro zabezpečení komunikace.

## Popis

Access Security Management Entity (ASME) je klíčová logická bezpečnostní funkce definovaná v architektuře 3GPP, primárně specifikovaná v řadě 3GPP TS 33.401 pro Evolved Packet System (EPS) a přenesená do systémů 5G. Není to samostatný fyzický uzel, ale funkční role, která může být implementována v rámci síťové entity. V LTE/EPC tuto roli plní Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)). V 5G Core (5GC) je odpovídající funkce integrována do Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)). Základní činnost ASME začíná, když se uživatelské zařízení (UE) pokouší připojit k síti. Entita obslužné sítě (MME nebo AMF), vystupující jako ASME, požádá o autentizační vektory z Authentication Centre (AuC) domovské sítě prostřednictvím Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) v EPS nebo Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) a Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) v 5GS. Tyto vektory obsahují kryptografické klíče a parametry, včetně hlavního relakového klíče (K_ASME v EPS, odvozeného z [CK](/mobilnisite/slovnik/ck/)/[IK](/mobilnisite/slovnik/ik/); nebo KAUSF v 5GS, odvozeného z CK'/IK').

Po přijetí těchto autentizačních vektorů ASME provádí klíčovou funkci odvozování a správy klíčů. Používá přijatý hlavní klíč k odvození hierarchie následných klíčů specifických pro přístupovou síť. Například v EPS ASME (MME) odvozuje klíč K_[eNB](/mobilnisite/slovnik/enb/) z K_ASME. Tento K_eNB je pak předán evolved NodeB (eNB) k zabezpečení rozhraní rádiového rozhraní. ASME zajišťuje, že dlouhodobý klíčový materiál domovské sítě není nikdy vystaven mimo domovskou doménu; s rádiovým přístupovým uzlem obslužné sítě jsou sdíleny pouze odvozené, přístupově specifické klíče. Tato architektura vynucuje oddělení klíčů, což znamená, že klíče použité v jedné přístupové síti (např. LTE) nemohou být přímo znovu použity v jiné (např. 5G NR nebo ne-3GPP přístupu), čímž se zvyšuje celková bezpečnost systému.

Povinnosti ASME sahají za rámec počátečního odvozování klíčů. Spravuje hierarchii klíčů během událostí mobility, jako je předávání spojení. Když se UE přesouvá mezi základnovými stanicemi, ASME může spustit odvozování klíčů pro nové základnové stanice (např. odvození nového K_eNB* pro cílové eNB při předávání spojení v LTE) na základě stávajících klíčů a nových parametrů, aby byla zachována dopředná a zpětná bezpečnost. Dále ASME zvládá správu bezpečnostního kontextu, ukládá bezpečnostní kontext spojený s UE během jeho připojené relace. Tento kontext zahrnuje hlavní klíč (K_ASME), identifikátory sady klíčů a přidružené bezpečnostní algoritmy. Pokud je třeba bezpečnostní kontext navázat pro ne-3GPP přístup (jako je důvěryhodná WLAN), ASME také hraje roli při usnadnění přenosu potřebného klíčového materiálu příslušným síťovým funkcím (např. Trusted WLAN Access Gateway v EPS).

V 5G jsou principy funkce ASME zachovány, ale vylepšeny v rámci servisně orientované architektury. AMF, vystupující jako ASME, komunikuje s AUSF/UDM pro primární autentizaci a přijímá kotvící klíč (KAUSF). AMF následně odvozuje následný klíč K_AMF, který plní podobnou roli jako K_ASME. Z K_AMF jsou odvozeny klíče pro přístupovou síť (K_gNB) a pro ochranu signalizace NAS. Systém 5G zavádí vylepšené oddělení klíčů, explicitně odděluje klíče pro různé síťové řezy a typy služeb. Funkce ASME, ztělesněná v AMF, je klíčová pro vynucování těchto zásad oddělení a zajišťuje, že bezpečnost jednoho řezu neohrozí jiný. Její činnost je zásadní pro bezpečnostní architekturu 3GPP, neboť poskytuje bezpečný most mezi důvěryhodnou kotvou domovské sítě a proměnlivým prostředím přístupové sítě.

## K čemu slouží

ASME byla představena ve 3GPP Release 8 s Evolved Packet System (LTE/EPC) za účelem řešení kritických bezpečnostních nedostatků v předchozích architekturách 3GPP a zavedení robustního, škálovatelného bezpečnostního rámce pro sítě typu all-IP. V systémech před Release 8, jako je UMTS, byla správa bezpečnostních klíčů těsněji provázána mezi jádrovou sítí a radiovým síťovým řadičem (RNC). Přechod k plošší architektuře v LTE, kde eNB přímo zpracovává bezpečnost na rádiovém rozhraní, vytvořil nový model hrozeb: eNB se nachází v potenciálně méně důvěryhodné doméně (přístupová síť) ve srovnání s jádrem. Primárním účelem ASME je vyřešit tento problém důvěryhodnosti tím, že funguje jako bezpečnostní mediátor. Zajišťuje, že dlouhodobý klíč účastníka, uložený pouze v domovské síti, není nikdy sdílen s uzly přístupové sítě. Místo toho ASME odvozuje krátkodobé, přístupově specifické klíče, čímž omezuje dopad potenciálního kompromitování v rádiové přístupové síti.

Dalším klíčovým problémem, který ASME řeší, je umožnění bezpečné mobility a interoperability napříč heterogenními přístupovými sítěmi. Jak se sítě vyvíjely a zahrnovaly ne-3GPP přístup (jako WiFi) a později 5G New Radio, byl potřebný mechanismus pro zajištění konzistentní autentizace a dohody o klíčích při zachování oddělení klíčů mezi různými přístupovými technologiemi. ASME poskytuje tento centralizovaný bod pro správu klíčů. Přijímá jedinou sadu přihlašovacích údajů z domovské sítě a je zodpovědná za odvození příslušných klíčů pro jakoukoli přístupovou technologii, kterou UE používá, ať už jde o LTE, 5G NR nebo důvěryhodnou WLAN. Tento návrh zajišťuje budoucí odolnost bezpečnostní architektury, umožňuje integraci nových typů přístupu bez nutnosti přepracování základního autentizačního procesu s domovskou sítí.

Dále ASME usnadňuje lepší efektivitu sítě a správu bezpečnostního kontextu. Centralizací odvozování a distribuce přístupových klíčů zjednodušuje procedury předávání spojení. Během předávání spojení může ASME efektivně vypočítat nové klíče pro cílovou buňku bez nutnosti znovu autentizovat s domovskou sítí, čímž snižuje latenci a signalizační zátěž. Vytvoření K_ASME (nebo K_AMF v 5G) jako klíče střední úrovně v hierarchii také umožňuje nezávislé obnovování klíčů a aktualizace kryptografických algoritmů na přístupovém spoji bez ovlivnění spojení s jádrem k domovské síti. Tento vrstvený přístup ke správě klíčů, řízený ASME, je základním konceptem, který umožňuje pokročilé bezpečnostní funkce vyžadované pro moderní mobilní broadband, massive IoT a síťové řezy v 5G a dalších generacích.

## Klíčové vlastnosti

- Centralizované odvozování přístupově specifických klíčů (např. K_eNB, K_gNB) z hlavních klíčů domovské sítě
- Vynucování oddělení klíčů mezi různými technologiemi přístupové sítě a síťovými řezy
- Správa hierarchie bezpečnostních klíčů během počátečního připojení a procedur předávání spojení
- Funguje jako bezpečnostní zprostředkovatel mezi důvěryhodnou domovskou sítí a méně důvěryhodnou přístupovou sítí
- Ukládá a spravuje bezpečnostní kontext UE, včetně identifikátorů sady klíčů a kryptografických algoritmů
- Usnadňuje autentizaci a dohodu o klíčích pro ne-3GPP přístupové sítě (např. důvěryhodná WLAN)

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 33.401** (Rel-19) — EPS Security Architecture

---

📖 **Anglický originál a plná specifikace:** [ASME na 3GPP Explorer](https://3gpp-explorer.com/glossary/asme/)
