---
slug: "p-cscf"
url: "/mobilnisite/slovnik/p-cscf/"
type: "slovnik"
title: "P-CSCF – Proxy Call Session Control Function"
date: 2026-01-01
abbr: "P-CSCF"
fullName: "Proxy Call Session Control Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/p-cscf/"
summary: "Proxy Call Session Control Function (P-CSCF) je prvním kontaktním bodem pro uživatelské zařízení (UE) v rámci IMS (IP Multimedia Subsystem). Funguje jako SIP proxy, přeposílá SIP zprávy mezi UE a jádr"
---

P-CSCF je prvním kontaktním bodem IMS pro uživatelské zařízení (UE), který funguje jako SIP proxy přeposílající zprávy a vynucující politiky pro navázání, správu a ukončení multimediálních relací.

## Popis

Proxy Call Session Control Function (P-CSCF) je základním uzlem v architektuře IP Multimedia Subsystem (IMS), jak je definována 3GPP, která poskytuje multimediální služby přes IP sítě. Je první IMS entitou, se kterou uživatelské zařízení (UE) komunikuje po získání IP konektivity, typicky přes LTE nebo 5G přístup. Funkčně P-CSCF pracuje jako proxy a uživatelský agent pro protokol Session Initiation Protocol (SIP), ale její role sahá daleko za pouhé směrování zpráv. Nachází se v domovské síti uživatele nebo ve visited síti a slouží jako zabezpečená brána pro veškerou signalizaci SIP mezi UE a zbytkem jádra IMS, které zahrnuje Interrogating-CSCF ([I-CSCF](/mobilnisite/slovnik/i-cscf/)) a Serving-CSCF (S-CSCF).

Z protokolového hlediska P-CSCF zpracovává celý životní cyklus SIP dialogů. Když UE zahájí registraci SIP nebo požadavek na relaci (jako hlasové nebo video volání), odešle SIP zprávu na zjištěnou adresu P-CSCF. P-CSCF ověří formát zprávy, uplatní síťové politiky – například zkontroluje, zda je požadovaná služba povolena – a poté směruje požadavek k příslušnému [I-CSCF](/mobilnisite/slovnik/icscf/) nebo S-CSCF na základě profilu uživatele a domény. Zásadně také udržuje bezpečnostní asociaci s UE pomocí [IPsec](/mobilnisite/slovnik/ipsec/) nebo TLS, čímž zajišťuje integritu a důvěrnost signalizace SIP. Provádí také kompresi SIP zpráv (SigComp) pro optimalizaci přenosu přes bezdrátové spoje a spravuje směrování nouzových relací.

Klíčovou architektonickou odpovědností P-CSCF je její interakce s rámcem Policy and Charging Control (PCC). Funguje jako Policy and Charging Enforcement Function (PCEF) pro mediální rovinu IMS nebo komunikuje se samostatným PCEF (jako je PGW v 4G nebo [UPF](/mobilnisite/slovnik/upf/) v 5G). Během navazování relace P-CSCF extrahuje mediální parametry (např. typy kodeků, IP adresy, porty) z SIP Session Description Protocol (SDP) a komunikuje je s funkcí Policy and Charging Rules Function (PCRF) přes rozhraní Rx. To umožňuje síti autorizovat příslušné prostředky Quality of Service (QoS) (např. vyhrazené nosiče pro VoLTE) a uplatnit tarifní pravidla před zahájením mediálního toku. P-CSCF také generuje záznamy o účtování ([CDR](/mobilnisite/slovnik/cdr/)) pro offline billing. Její nasazení může být v moderních cloud-nativních implementacích sloučeno s jinými funkcemi, ale její logická role jako vstupního bodu UE a vynucovatele politik zůstává konstantní napříč 4G a 5G.

## K čemu slouží

P-CSCF byla vytvořena jako součást architektury IMS, poprvé standardizované v 3GPP Release 5, aby umožnila poskytování bohatých, real-time multimediálních služeb přes paketově přepínané IP sítě. Před IMS se s hlasem a SMS vypořádávaly sítě s přepojováním okruhů, zatímco paketově přepínané sítě jako [GPRS](/mobilnisite/slovnik/gprs/) byly primárně pro best-effort data. IMS mělo za cíl tyto světy sloučit tím, že nabídne hlas, video a zasílání zpráv přes IP s úrovní spolehlivosti, zabezpečení a účtování na úrovni operátorských služeb. P-CSCF řeší problém bezpečného připojení milionů potenciálně mobilních UE k tomuto komplexnímu servisnímu jádru tím, že funguje jako důvěryhodný zprostředkovatel, který chrání vnitřní IMS síť před přímou expozicí přístupové síti.

Historicky by bez vyhrazené proxy funkce na okraji sítě bylo řízení signalizace SIP od různorodých UE napříč různými typy přístupu (např. LTE, Wi-Fi) chaotické a nejisté. P-CSCF poskytuje standardizovaný první kontaktní bod, který zvládá přístupově specifické adaptace, jako je překlad IP adres a komprese signalizace. Také jednotně vynucuje síťové politiky, čímž brání neoprávněnému používání služeb a zajišťuje, že mediální toky získají potřebnou QoS. To bylo obzvláště klíčové pro zavedení Voice over LTE (VoLTE), kde P-CSCF zajišťuje, že hlasové pakety jsou upřednostňovány prostřednictvím systému EPS nosičů.

Vývoj směrem k 5G a network slicing dále podtrhuje význam P-CSCF. V 5G Core (5GC) zůstává P-CSCF klíčovou součástí pro telefonii založenou na IMS (VoNR) a multimediální služby. Komunikuje s 5G Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) přes rozhraní N5, což je analogické rozhraní Rx s PCRF v 4G, za účelem orchestrace QoS s ohledem na relaci. Její návrh umožňuje operátorům nasazovat IMS nezávisle na podkladové přístupové technologii, což chrání investice do budoucnosti a umožňuje bezproblémovou kontinuitu služeb, jak se sítě vyvíjejí z 4G na 5G a dále.

## Klíčové vlastnosti

- Funguje jako první SIP proxy a zabezpečený vstupní bod pro UE do sítě IMS.
- Vytváří a udržuje bezpečnostní asociace IPsec nebo TLS s UE pro ochranu signalizace.
- Komunikuje s PCRF/PCF přes Rx/N5 za účelem autorizace prostředků QoS na základě mediálních parametrů SDP.
- Provádí kompresi SIP zpráv (SigComp) pro optimalizaci signalizace přes rádiová rozhraní.
- Směruje SIP zprávy k příslušnému I-CSCF nebo S-CSCF a zajišťuje priorizaci nouzových relací.
- Generuje záznamy o účtování (CDR) pro fakturaci IMS relací.

## Související pojmy

- [I-CSCF – Interrogating-Call Session Control Function](/mobilnisite/slovnik/i-cscf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TS 23.849** (Rel-11) — Study on IMS Roaming Media Optimization
- **TS 23.894** (Rel-10) — IMS Local Breakout & Optimal Media Routing Study
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- … a dalších 51 specifikací

---

📖 **Anglický originál a plná specifikace:** [P-CSCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/p-cscf/)
