---
slug: "fmc"
url: "/mobilnisite/slovnik/fmc/"
type: "slovnik"
title: "FMC – Fixed Mobile Convergence"
date: 2025-01-01
abbr: "FMC"
fullName: "Fixed Mobile Convergence"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/fmc/"
summary: "Fixed Mobile Convergence (FMC) je servisní rámec, který integruje pevné sítě (např. širokopásmové) a mobilní sítě za účelem poskytnutí bezproblémových uživatelských zkušeností. Umožňuje konzistentní s"
---

FMC je servisní rámec, který integruje pevné a mobilní sítě za účelem poskytnutí bezproblémových uživatelských zkušeností a konzistentních služeb napříč různými přístupovými technologiemi.

## Popis

Fixed Mobile Convergence (FMC) je servisní architektura definovaná 3GPP, která sjednocuje služby pevných sítí (jako [DSL](/mobilnisite/slovnik/dsl/), optické vlákno nebo kabel) se službami mobilních sítí (jako 4G LTE nebo 5G) za účelem poskytnutí soudržné uživatelské zkušenosti. Funguje na principu abstrakce podkladových přístupových technologií prostřednictvím společných funkcí jádra sítě a servisních vrstev, což uživatelům umožňuje přistupovat k hlasovým, datovým a multimediálním službám bezproblémově bez ohledu na to, zda jsou připojeni přes pevný nebo mobilní spoj. Architektura typicky zahrnuje konvergenční body v jádru sítě, jako je IP Multimedia Subsystem (IMS), který zajišťuje řízení relací a doručování služeb napříč různorodými přístupovými sítěmi.

Klíčové součásti FMC zahrnují přístupově agnostické servisní platformy, funkce řízení politik (jako PCRF nebo [PCF](/mobilnisite/slovnik/pcf/)) a jednotné autentizační mechanismy. Například když uživatel zahájí hlasový hovor, FMC umožňuje předání mezi Wi-Fi (pevný přístup) a mobilními sítěmi bez přerušení, a to za použití technologií jako Voice over Wi-Fi (VoWiFi) nebo Single Radio Voice Call Continuity (SRVCC). Síť využívá protokoly kontinuity relací a řízení kvality služeb (QoS) k udržení úrovně služeb během přechodů. To zahrnuje koordinaci mezi pevnou širokopásmovou bránou (např. domácí bránou) a prvky mobilního jádra, jako je Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)).

V praxi FMC využívá společné databáze účastníků, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), pro ukládání uživatelských profilů a politik platných napříč pevnou i mobilní doménou. Tato integrace umožňuje funkce jako jednotné přihlašování, jednotné účtování a sjednocené zasílání zpráv. Propojením pevné a mobilní infrastruktury FMC zvyšuje využití sítě, snižuje provozní náklady díky sdíleným zdrojům a podporuje inovativní služby jako konvergované [IPTV](/mobilnisite/slovnik/iptv/) a aplikace pro chytré domácnosti. Je to základní koncept pro sítě 5G, který umožňuje scénáře, kde pevný bezdrátový přístup ([FWA](/mobilnisite/slovnik/fwa/)) doplňuje tradiční mobilní služby.

## K čemu slouží

Fixed Mobile Convergence byl vytvořen k řešení fragmentace mezi pevnými a mobilními sítěmi, které historicky fungovaly jako oddělené izolované celky s odlišnými službami, fakturačními systémy a uživatelskými zkušenostmi. Jelikož spotřebitelé požadovali flexibilnější a integrovanější komunikaci, operátoři čelili výzvám v poskytování bezproblémové mobility a kontinuity služeb. FMC tyto problémy řeší tím, že umožňuje jednotný přístup, který uživatelům dovoluje transparentně přepínat mezi sítěmi, což zvyšuje pohodlí a spokojenost zákazníků.

Motivace pro FMC vycházela z konvergence hlasových a datových služeb přes IP sítě, poháněné přijetím IMS a úpadkem technologií s přepojováním okruhů. Řeší omezení, jako je duplikace služeb, kdy operátoři udržovali oddělené infrastruktury pro pevné a mobilní sítě, což vedlo k neefektivitám a vyšším nákladům. Integrací sítí FMC snižuje kapitálové a provozní výdaje prostřednictvím sdílení zdrojů a zjednodušuje nasazování služeb. Historicky byly rané pokusy o konvergenci proprietární, ale standardizace 3GPP ve verzi Release 8 poskytla interoperabilní rámec, který podnítil široké přijetí.

FMC také řeší rostoucí poptávku po širokopásmovém připojení všude, protože pevné sítě nabízejí vysokou kapacitu, zatímco mobilní sítě poskytují mobilitu. Umožňuje operátorům přesměrovat provoz na pevné sítě (např. přes Wi-Fi), čímž ulevuje přetížení mobilních sítí. To je obzvláště relevantní s nástupem 5G, kde FMC podporuje pevný bezdrátový přístup jako náhradu za tradiční širokopásmové připojení, čímž rozšiřuje pokrytí a možnosti služeb. Nakonec FMC připravuje cestu pro plně konvergované sítě, které podporují nové případy užití, jako jsou chytrá města a průmyslový IoT.

## Klíčové vlastnosti

- Bezproblémová kontinuita služeb napříč pevným a mobilním přístupem
- Integrace s IP Multimedia Subsystem (IMS) pro jednotné řízení
- Jednotná autentizace a správa účastníků
- Řízení kvality služeb (QoS) a správa provozu založená na politikách
- Podpora předání hlasových a datových služeb (např. VoWiFi, SRVCC)
- Konvergované účtování a poskytování služeb

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.937** (Rel-13) — FMC requirements for 3GPP-WLAN service continuity
- **TS 28.620** (Rel-19) — FMC Federated Network Information Model (FNIM) UIM
- **TS 28.820** (Rel-12) — Umbrella Operation Model for Fixed Mobile Convergence
- **TS 28.821** (Rel-13) — UML Model Repertoire for FMC Management
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.103** (Rel-19) — 3GPP Management IRP Overview
- **TS 32.107** (Rel-19) — Federated Network Information Model (FNIM)
- **TS 32.828** (Rel-10) — Study on 3GPP-TMF NRM/SID Alignment
- **TS 32.832** (Rel-10) — Alarm Correlation and Root Cause Analysis Study
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study
- **TS 32.863** (Rel-13) — PM Measurement Metadata Definition

---

📖 **Anglický originál a plná specifikace:** [FMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/fmc/)
