---
slug: "he"
url: "/mobilnisite/slovnik/he/"
type: "slovnik"
title: "HE – Home Environment"
date: 2025-01-01
abbr: "HE"
fullName: "Home Environment"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/he/"
summary: "Domácí prostředí (Home Environment) je administrativní doména poskytovatele služeb uživatele, která spravuje jeho předplatné, služební profily a autentizaci. Jde o základní koncept pro personalizaci s"
---

HE je administrativní doména poskytovatele služeb uživatele, která spravuje jeho předplatné, služební profily a autentizaci za účelem konzistentní a personalizované služby napříč navštívenými sítěmi.

## Popis

Domácí prostředí (HE) je klíčový architektonický a administrativní koncept v sítích 3GPP, který představuje doménu domácího poskytovatele služeb nebo síťového operátora uživatele. Nejde o jedinou fyzickou entitu, ale o logickou doménu zahrnující systémy a datové úložiště, které definují identitu účastníka, práva z předplatného a možnosti služeb. HE je zodpovědné za uložení hlavní kopie služebního profilu uživatele, který zahrnuje předplacené služby, parametry kvality služby (QoS) a autentizační údaje. Tento profil je klíčový pro řízení služeb a personalizaci, neboť zajišťuje, že uživatelé mají přístup ke svým předplaceným službám i při roamování mimo pokrytí své domácí sítě.

Architektonicky HE komunikuje s navštívenou sítí (VN) nebo obslužnou sítí (Serving Network), kde se uživatel aktuálně nachází. Mezi klíčové funkční komponenty v HE patří Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), který slouží jako centrální databáze informací o účastnících, a různé aplikační servery poskytující nadstandardní služby. Když se uživatel připojí k navštívené síti, entity obslužné sítě (jako [MSC](/mobilnisite/slovnik/msc/), SGSN nebo [MME](/mobilnisite/slovnik/mme/)) komunikují s HSS/HLR v HE, aby uživatele autentizovaly a stáhly relevantní data o předplatném. Tento proces, řízený protokoly jako [MAP](/mobilnisite/slovnik/map/) (pro 2G/3G) nebo Diameter (pro 4G/5G), zajišťuje, že autorizace služeb a účtování jsou správně zpracovávány domácím operátorem.

Role HE přesahuje základní správu předplatného a zahrnuje také pokročilou služební logiku a její provádění. Pro služby jako IMS (IP Multimedia Subsystem) HE zahrnuje S-CSCF (Serving-Call Session Control Function) přiřazený uživateli, který sídlí v domácí síti a provádí služební profil uživatele. To zajišťuje, že služební logika, jako jsou pravidla pro přesměrování hovorů nebo informace o stavu, je konzistentně aplikována bez ohledu na polohu uživatele. Oddělení mezi domácím a obslužným prostředím je zásadní pro roamingovou architekturu 3GPP, neboť umožňuje interoperabilitu mezi sítěmi různých operátorů při zachování kontroly domácího operátora nad poskytováním služeb, zabezpečením a účtováním.

## K čemu slouží

Koncept domácího prostředí byl zaveden, aby formalizoval oddělení mezi domácím poskytovatelem služeb účastníka a sítí, která aktuálně poskytuje rádiový přístup a konektivitu. Toto oddělení je nezbytné pro umožnění bezproblémového národního a mezinárodního roamingu. Před takovými standardizovanými architekturami byli účastníci často vázáni na infrastrukturu jediného síťového operátora s omezenou možností používat služby mimo jeho pokrytí. Model HE to řeší definováním jasné administrativní hranice a standardizovaných rozhraní (jako rozhraní C/D pro přístup k [HLR](/mobilnisite/slovnik/hlr/)), která umožňují navštívené síti bezpečně dotazovat domácí síť na data a autorizaci účastníka.

Dále je HE klíčové pro personalizaci a inovace služeb. Umožňuje domácímu operátorovi vyvíjet a řídit pokročilé služby (jako multimediální telefonie nebo zasílání zpráv), které jsou uživateli doručovány konzistentně, ať už je doma nebo roamuje. Tento obchodní model motivuje operátory k investicím do služebních platforem. HE také řeší kritické požadavky na zabezpečení centralizací autentizačních funkcí. Dlouhodobý tajný klíč (Ki) používaný pro generování autentizačních vektorů je uložen pouze v zabezpečené doméně HE (v AuC, což je součást [HSS](/mobilnisite/slovnik/hss/)/HLR) a nikdy není přenášen do navštívené sítě. Tento návrh zabraňuje expozici přihlašovacích údajů a tvoří základ pro vzájemnou autentizaci mezi uživatelem a sítí.

## Klíčové vlastnosti

- Centralizované úložiště hlavních profilů účastníků a servisních dat
- Autentizace a autorizace účastníků pro přístup k síti a službám
- Umožňuje bezproblémové poskytování služeb a personalizaci během roamingu
- Hostí klíčové funkce řízení služeb, jako je IMS S-CSCF
- Poskytuje kotvící bod pro generování záznamů o účtování a poplatcích
- Udržuje zabezpečení tím, že uchovává autentizační údaje (AuC) v rámci domácí domény

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.127** (Rel-9) — Open Service Access (OSA) Requirements
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 29.198** (Rel-9) — OSA API Overview Specification
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 32.141** (Rel-19) — Subscription Management (SuM) Architecture
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.401** (Rel-19) — EPS Security Architecture
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [HE na 3GPP Explorer](https://3gpp-explorer.com/glossary/he/)
