---
slug: "cp"
url: "/mobilnisite/slovnik/cp/"
type: "slovnik"
title: "CP – Control Plane"
date: 2026-01-01
abbr: "CP"
fullName: "Control Plane"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cp/"
summary: "Řídicí rovina (Control Plane, CP) je síťová vrstva odpovědná za signalizaci, správu relací, mobilitu a řízení politik. Zajišťuje navázání, udržování a ukončení spojení, čímž odděluje signalizaci od př"
---

CP (řídicí rovina) je síťová vrstva odpovědná za signalizaci, správu relací, mobilitu a řízení politik, která zajišťuje navázání, udržování a ukončení spojení.

## Popis

Řídicí rovina (Control Plane, CP) v systémech 3GPP představuje soubor funkcí a protokolů odpovědných za signalizaci potřebnou k navázání, správě a ukončení komunikačních relací a spojení pro uživatelské zařízení (UE). Funguje odděleně od uživatelské roviny (User Plane, UP), která zpracovává samotný přenos uživatelských dat. Toto oddělení funkcí, známé jako Control and User Plane Separation (CUPS), je klíčovým architektonickým principem, který zvyšuje flexibilitu a škálovatelnost sítě a umožňuje nezávislý vývoj síťových funkcí. CP je odpovědná za kritické procedury včetně autentizace, registrace, navazování relací, správy mobility (předávání spojení, aktualizace oblasti sledování), řízení politik a účtování a správu spojení.

Z architektonického hlediska se CP skládá z různých síťových funkcí (NFs), které v 5G vzájemně komunikují prostřednictvím standardizovaných rozhraní založených na službách (SBIs), nebo prostřednictvím referenčních bodů v dřívějších generacích. Mezi klíčové funkce CP v 5G Core (5GC) patří Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)). V Evolved Packet Core (EPC) jsou ekvivalentními funkcemi Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a Policy and Charging Rules Function (PCRF). Tyto funkce si vyměňují signalizační zprávy pomocí protokolů jako [NGAP](/mobilnisite/slovnik/ngap/), [NAS](/mobilnisite/slovnik/nas/) a HTTP/2, aby orchestrovaly síťové zdroje a služby pro UE.

CP funguje tak, že zpracovává signalizační zprávy iniciované UE nebo jinými síťovými funkcemi. Například během počáteční registrace odešle UE registrační požadavek prostřednictvím Radio Access Network (RAN) do AMF. AMF následně komunikuje s UDM za účelem autentizace a získání profilu účastníka a se SMF pro případné navázání PDU relace. CP činí rozhodnutí na základě politik účastníka, stavu sítě a požadavků služeb a následně dává pokyn funkcím uživatelské roviny (např. UPF, SGW-U/PGW-U), aby nastavily příslušné datové cesty. Tato orchestrace zajišťuje efektivní tok uživatelských dat při zachování zabezpečení, kvality služeb (QoS) a podpory mobility.

Její role je klíčová pro automatizaci sítě, síťové řezy (slicing) a poskytování služeb. Centralizací řídicí logiky umožňuje CP dynamickou rekonfiguraci sítě, efektivní přidělování zdrojů napříč síťovými řezy a implementaci pokročilých služeb, jako je správa IoT zařízení s podporou sítě nebo edge computing. Návrh CP umožňuje cloud-nativní implementaci, podporuje bezstavové síťové funkce, škálovatelnost a odolnost prostřednictvím redundance a vyvažování zátěže, což je nezbytné pro moderní softwarově definované mobilní sítě.

## K čemu slouží

Řídicí rovina existuje proto, aby zvládla složitost provozu mobilních sítí oddělením signalizační logiky od přeposílání dat. Toto oddělení řeší omezení monolitických síťových architektur, kde bylo řízení a zpracování dat těsně propojeno, což vedlo k problémům se škálovatelností, neefektivnímu využití zdrojů a nepružnosti při zavádění nových služeb. Rozdělení na CP/UP umožňuje každé rovině škálovat nezávisle podle poptávky; například UP lze škálovat pro zvládnutí nárazů v datovém provozu, zatímco CP se škáluje podle počtu připojených zařízení a signalizační zátěže.

Historicky, jak se sítě vyvíjely od přepojování okruhů k paketovým IP architekturám (GPRS, UMTS, LTE), stala se potřeba robustního a flexibilního řídicího mechanismu klíčovou pro podporu trvalého připojení, pokročilé QoS a různorodých služeb. Vytvoření vyhrazené řídicí roviny standardizovalo signalizační procedury pro mobilitu, správu relací a zabezpečení napříč různými přístupovými technologiemi (např. 3G, 4G, 5G-NR, ne-3GPP WLAN), což umožnilo plynulou mobilitu a kontinuitu služeb. Vyřešila tak problém neefektivních proprietárních řídicích mechanismů, které bránily interoperabilitě a rychlému nasazení služeb.

Navíc je CP hybatelem klíčových technologických pokroků, jako jsou síťové řezy (Network Slicing) a edge computing v 5G. Poskytuje orchestrační vrstvu, která může na sdílené fyzické infrastruktuře vytvářet, spravovat a ukončovat izolované síťové řezy se specifickými charakteristikami. Centralizací řízení politik a relací umožňuje CP operátorům nabízet diferencované služby, implementovat sofistikované modely účtování a dynamicky přizpůsobovat chování sítě požadavkům aplikací, což s dřívějšími, rigidnějšími architektonickými přístupy nebylo možné.

## Klíčové vlastnosti

- Orchestruje procedury navázání, změny a uvolnění relací
- Spravuje mobilitu UE, včetně předávání spojení a aktualizací registrační oblasti
- Vynucuje autentizaci, autorizaci a řízení politik účastníka
- Podporuje Control and User Plane Separation (CUPS) pro nezávislé škálování
- Umožňuje síťové řezy (network slicing) prostřednictvím vyhrazeného výběru řezu a správy zdrojů
- Poskytuje rozhraní pro interakci s funkcemi uživatelské roviny a dalšími síťovými funkcemi jádra

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.714** (Rel-14) — Study on CP-UP separation in EPC
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 23.868** (Rel-9) — Study on IMS Emergency Calls
- **TS 24.167** (Rel-19) — 3GPP IMS Management Object Specification
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling
- **TR 26.930** (Rel-19) — WebRTC Enhancements for Immersive RTC over 5G
- … a dalších 71 specifikací

---

📖 **Anglický originál a plná specifikace:** [CP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cp/)
