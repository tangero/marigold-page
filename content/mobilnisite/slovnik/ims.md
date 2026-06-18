---
slug: "ims"
url: "/mobilnisite/slovnik/ims/"
type: "slovnik"
title: "IMS – IP Multimedia Subsystem"
date: 2026-01-01
abbr: "IMS"
fullName: "IP Multimedia Subsystem"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ims/"
summary: "Standardizovaný architektonický rámec definovaný 3GPP pro poskytování multimediálních služeb založených na protokolu IP (hlas, video, zasílání zpráv) přes mobilní a pevné sítě. Poskytuje funkce řízení"
---

IMS je standardizovaný architektonický rámec pro poskytování multimediálních služeb založených na protokolu IP přes sítě, který poskytuje funkce řízení služeb, autentizace a účtování nezávisle na přístupové technologii.

## Popis

IP Multimedia Subsystem (IMS) je základní, na přístupu nezávislá podsystémová síť jádra v architektuře 3GPP. Nejde o jeden uzel, ale o kompletní rámec logických funkcí a referenčních bodů navržený k navazování, úpravám a ukončování multimediálních relací s použitím protokolu Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) jako primárního signalizačního protokolu. IMS odděluje poskytování služeb od podkladové transportní vrstvy (např. GSM, UMTS, LTE, 5G NR, WiFi, pevný broadband), což umožňuje konvergenci a konzistentní uživatelský zážitek napříč různými přístupovými sítěmi. Jeho architektura je organizována do tří hlavních vrstev: Transportní vrstva (poskytující IP konektivitu), Řídící vrstva (samotné jádro IMS) a Aplikační/Servisní vrstva.

Jádro řídicí vrstvy IMS tvoří Call Session Control Functions (CSCFs): Proxy-CSCF ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) a Interrogating-CSCF ([I-CSCF](/mobilnisite/slovnik/i-cscf/)). P-CSCF je prvním kontaktním bodem pro uživatelské zařízení (UE), zajišťuje přeposílání SIP zpráv, zabezpečení a vynucování pravidel. I-CSCF funguje jako vstupní bod do sítě operátora, vybírá vhodný S-CSCF a skrývá topologii sítě. S-CSCF je centrálním mozkem; provádí registraci uživatele, směrování relací a komunikuje s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro autentizaci a načítání uživatelského profilu. Mezi další klíčové funkce patří HSS (hlavní databáze účastníků), Breakout Gateway Control Function ([BGCF](/mobilnisite/slovnik/bgcf/)) pro směrování do komutovaných sítí a Media Resource Functions ([MRF](/mobilnisite/slovnik/mrf/)) pro konferenční hovory a tóny.

Relace začíná registrací UE. UE objeví P-CSCF a poté odešle požadavek SIP REGISTER. S-CSCF autentizuje uživatele (pomocí přihlašovacích údajů z HSS) prostřednictvím protokolu IMS Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)). Po registraci může UE iniciovat relaci (např. VoLTE hovor) odesláním SIP INVITE. S-CSCF směruje požadavek na základě initial Filter Criteria (iFC) stažených z HSS, což může spustit služby na Application Servers (AS). IMS také integruje řízení pravidel a účtování prostřednictvím rozhraní Rx k Policy and Charging Rules Function (PCRF), čímž zajišťuje odpovídající Quality of Service (QoS) a účtování pro mediální toky. Samotná média typicky proudí přímo mezi koncovými body (UE) přes IP s použitím protokolů jako RTP, pod kontrolou navázanou SIP signalizací.

## K čemu slouží

IMS bylo koncipováno k řešení omezení tradičních mobilních sítí, které byly postaveny na komutované technologii optimalizované primárně pro hlas. S růstem internetu vzrostla poptávka po integrovaných datových a multimediálních službách (jako je videohovor, instant messaging a presence). Pokusy o nabídnutí těchto služeb před érou IMS byly často vertikálními 'silosy' – proprietárními, závislými na přístupu a obtížně integrovatelnými, což vedlo ke špatnému uživatelskému zážitku a vysokým nákladům operátorů na vývoj a údržbu.

Primární motivací pro IMS bylo vytvoření horizontální, standardizované platformy pro poskytování služeb. Jeho založení na protokolech Internet Engineering Task Force (IETF), jako jsou SIP a Diameter, umožnilo 3GPP využít internetové technologie a zároveň přidat nezbytné schopnosti pro telekomunikační služby carrier-grade: robustní zabezpečení, garantovanou kvalitu služeb, zákonný odposlech a sofistikované modely účtování (předplacené, postpaid, událostní). To umožnilo operátorům rychle nasazovat a kombinovat služby (hlas, video, text, přenos souborů) do bohatých komunikačních sad a konkurovat tak internetovým hráčům typu Over-The-Top (OTT).

Navíc bylo IMS od svého vzniku v 3GPP Release 5 navrženo jako na přístupu nezávislé. Toto budoucí zabezpečení architektury umožnilo sloužit nejen 3G UMTS, ale i následným technologiím jako LTE (kde se stalo základem pro VoLTE), 5G (pro Voice over New Radio), WiFi (přes VoWiFi) a pevným sítím (vedoucím k Fixed-Mobile Convergence). Vyřešilo problém fragmentace služeb, což umožnilo uživateli mít stejné telefonní číslo, identitu a servisní funkce bez ohledu na to, zda je připojen přes mobilní síť, firemní WiFi nebo domácí broadband. IMS se tak stalo základním kamenem pro vývoj mobilních sítí směrem k All-IP sítím a umožnilo vyřazení starších komutovaných jader.

## Klíčové vlastnosti

- Na přístupu nezávislá architektura podporující 3G, 4G, 5G, WiFi a pevný broadband
- Řízení relací založené na SIP pro navazování multimediální komunikace
- IMS AKA pro silnou vzájemnou autentizaci a zabezpečení
- Oddělená servisní vrstva umožňující rychlý vývoj a integraci nových aplikací
- Integrované řízení pravidel a účtování (PCC) pro dynamickou QoS a fakturaci
- Podpora roamingu a interoperability mezi sítěmi různých operátorů

## Související pojmy

- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TS 22.240** (Rel-19) — 3GPP Generic User Profile Requirements
- **TS 22.250** (Rel-19) — IMS Group Management Requirements
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.340** (Rel-19) — IMS Messaging Stage 1 Requirements
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 22.519** (Rel-19) — NGN Business Communication Requirements
- **TR 22.940** (Rel-19) — IMS Messaging Requirements Analysis
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- … a dalších 168 specifikací

---

📖 **Anglický originál a plná specifikace:** [IMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ims/)
