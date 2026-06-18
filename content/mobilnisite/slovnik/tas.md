---
slug: "tas"
url: "/mobilnisite/slovnik/tas/"
type: "slovnik"
title: "TAS – Telephony Application Server"
date: 2025-01-01
abbr: "TAS"
fullName: "Telephony Application Server"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tas/"
summary: "Aplikační server v IP Multimedia Subsystem (IMS), který poskytuje telefonní služby, jako je přesměrování hovorů, hlasová schránka a doplňkové služby. Umožňuje poskytování tradičních telefonních funkcí"
---

TAS (Telephony Application Server) je aplikační server pro telefonii v IMS, který poskytuje tradiční telefonní služby, jako je přesměrování hovorů a hlasová schránka, přes IP sítě, a tvoří jádro VoLTE a hlasových služeb založených na IMS.

## Popis

Telephony Application Server (TAS) je klíčová funkční entita v architektuře IP Multimedia Subsystem (IMS) podle 3GPP, zodpovědná za hostování a provádění logiky telefonních služeb. Funguje jako aplikační server ([AS](/mobilnisite/slovnik/as/)), který komunikuje s jádrem IMS – konkrétně s Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) přes rozhraní IMS Service Control ([ISC](/mobilnisite/slovnik/isc/)) – a poskytuje hodnotově přidané telefonní služby. Když uživatel zahájí nebo přijme hovorovou relaci, S-CSCF vyvolá příslušnou servisní logiku na TAS na základě uživatelových initial Filter Criteria (iFC) definovaných v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). TAS následně ovlivňuje průběh hovoru a aplikuje funkce jako přesměrování hovoru, zákaz, hlasová schránka, čekání hovoru nebo konferenční hovor.

Architektonicky je TAS softwarový server, který implementuje servisní logiku pro telefonní aplikace definovanou standardy 3GPP. Komunikuje pomocí [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) přes rozhraní ISC. TAS může manipulovat se zprávami SIP (INVITE, BYE atd.), generovat nové SIP transakce a komunikovat s dalšími síťovými elementy, jako jsou Media Resource Functions ([MRF](/mobilnisite/slovnik/mrf/)), pro přehrávání hlášení nebo správu konferenčních můstků. V moderních nasazeních, zejména pro VoLTE, je TAS často implementován jako virtualizovaná síťová funkce ([VNF](/mobilnisite/slovnik/vnf/)) běžící na cloudové infrastruktuře, což poskytuje škálovatelnost a flexibilitu. Udržuje informace o stavu služby pro aktivní relace a může komunikovat s databázemi účastníků pro získání uživatelských profilů a nastavení služeb.

Role TAS je zásadní pro umožnění pokročilých telefonních služeb v plně IP síti. Odděluje servisní logiku od základních funkcí řízení hovoru a přenosu v jádru IMS, což umožňuje operátorům vyvíjet, nasazovat a aktualizovat služby nezávisle. Například ve VoLTE hovoru může TAS poskytovat bezproblémový překlad čísel, implementovat funkce pro obchodní komunikaci nebo se integrovat s webovými službami pro obohacené volání. Jeho fungování je specifikováno v řadě technických specifikací 3GPP pokrývajících požadavky, architekturu a protokoly služeb IMS.

## K čemu slouží

TAS byl zaveden spolu s IP Multimedia Subsystem (IMS) ve 3GPP Release 5/6, aby vyřešil výzvu poskytování tradičních telefonních služeb s přepojováním okruhů přes paketové IP sítě. Jak se mobilní sítě vyvíjely směrem k plně IP architekturám s LTE, vznikla potřeba nahradit legacy Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a jeho servisní logiku IP ekvivalentem. TAS tuto funkcionalitu poskytuje, což umožňuje operátorům nabízet známé telefonní funkce (jako ty definované v GSM) přes IMS, a tím podporovat Voice over LTE (VoLTE) a zajišťovat kontinuitu služeb a funkční paritu s hlasovými službami s přepojováním okruhů v 2G/3G.

Jeho vytvoření bylo motivováno snahou průmyslu konvergovat pevné a mobilní služby na společné IP jádro. TAS umožňuje centralizované a efektivní nasazení telefonních aplikací, které mohou obsluhovat jak mobilní, tak pevné účastníky. Řeší omezení dřívějších přístupů, kdy byly telefonní služby těsně svázány s konkrétním přepojovacím hardwarem, což je činilo nákladnými a pomalými na aktualizace. Standardizací TAS v rámci IMS umožnilo 3GPP vznik živého ekosystému aplikačních serverů, podporujícího inovace v telefonních službách při zachování interoperability mezi IMS jádry různých výrobců a uživatelskými zařízeními.

## Klíčové vlastnosti

- Hostuje a provádí servisní logiku telefonních služeb pro IMS/VoLTE
- Komunikuje s S-CSCF přes standardizované rozhraní ISC
- Poskytuje doplňkové služby (např. přesměrování hovoru, zákaz, čekání)
- Podporuje vyvolání služby na základě initial Filter Criteria (iFC)
- Může komunikovat s Media Resource Functions pro hlášení/konference
- Umožňuje rychlé nasazení a aktualizace služeb nezávisle na jádru sítě

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 23.719** (Rel-14) — Study on Service Domain Centralization (SeDoC)
- **TS 23.845** (Rel-10) — UDC Evolution Study
- **TS 23.883** (Rel-9) — IMS Centralized Services Supplementary Data Management
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony
- **TR 29.935** (Rel-19) — HSS Reference Data Model for Ud Interface
- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- **TS 38.561** (Rel-19) — UE Conformance for TRP/TRS FR1
- **TR 38.834** (Rel-17) — NR FR1 TRP/TRS Test Methodology
- **TS 38.870** (Rel-19) — Enhanced OTA Test Methods for NR FR1 TRP/TRS

---

📖 **Anglický originál a plná specifikace:** [TAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tas/)
