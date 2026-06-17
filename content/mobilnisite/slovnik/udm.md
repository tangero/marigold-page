---
slug: "udm"
url: "/mobilnisite/slovnik/udm/"
type: "slovnik"
title: "UDM – Unified Data Management"
date: 2026-01-01
abbr: "UDM"
fullName: "Unified Data Management"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/udm/"
summary: "Funkce jádra sítě v servisně orientované architektuře (SBA) 5G, která spravuje data účastníků, identity a autentizační přihlašovací údaje. Je centrálním úložištěm uživatelských profilů, generuje auten"
---

UDM je funkce jádra sítě, která spravuje data účastníků, identity a autentizační přihlašovací údaje a slouží jako centrální úložiště uživatelských profilů v servisně orientované architektuře 5G.

## Popis

Funkce Unified Data Management (UDM) je klíčovou součástí jádra 5G sítě (5GC) založeného na servisně orientované architektuře (SBA). Slouží jako centralizované úložiště a správní bod pro data související s účastníky. UDM je zodpovědná za ukládání a správu dlouhodobých informací o předplatném, včetně uživatelských identit, bezpečnostních přihlašovacích údajů, servisních profilů a dat souvisejících s politikami. Komunikuje s ostatními síťovými funkcemi prostřednictvím standardizovaných servisně orientovaných rozhraní, primárně za použití [HTTP](/mobilnisite/slovnik/http/)/2 s kódováním [JSON](/mobilnisite/slovnik/json/) nebo [CBOR](/mobilnisite/slovnik/cbor/). Primární role UDM zahrnují zpracování autentizačních přihlašovacích údajů, správu uživatelských identifikátorů, autorizaci přístupu a správu dat předplatného.

Architektonicky je UDM softwarová síťová funkce, kterou lze nasadit v cloudových prostředích. Často pracuje ve spojení s Unified Data Repository (UDR), které poskytuje skutečné trvalé úložiště pro data účastníků. UDM obsahuje aplikační logiku pro zpracování a správu těchto dat, zatímco UDR funguje jako databáze. Klíčové vnitřní komponenty zahrnují Authentication Credential Repository and Processing Function ([ARPF](/mobilnisite/slovnik/arpf/)), která ukládá dlouhodobé klíče a spouští autentizační algoritmy, a logiku správy dat předplatného. UDM zpřístupňuje své schopnosti jako služby ostatním [NF](/mobilnisite/slovnik/nf/), například Nudm_UEAuthentication pro autentizaci, Nudm_SubscriberDataManagement pro data předplatného a Nudm_EventExposure pro sledování událostí účastníků.

Jak funguje: Když se uživatelské zařízení (UE) pokouší zaregistrovat v 5G síti, obrátí se Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) na UDM. ARPF v UDM vygeneruje autentizační vektory (pomocí procedur 5G Authentication and Key Agreement (5G-AKA) nebo EAP-AKA') a poskytne je AMF prostřednictvím [AUSF](/mobilnisite/slovnik/ausf/). Pro zřízení relace si Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) načte uživatelská data předplatného a profil politik z UDM, aby určila povolené služby, parametry QoS a pravidla účtování. UDM také spravuje vazbu mezi trvalým identifikátorem předplatitele (SUPI) a dočasným identifikátorem (SUCI) používaným pro soukromí a sleduje obsluhující AMF pro každého účastníka, aby správně směrovala signalizační zprávy.

Její role je klíčová pro síťovou bezpečnost, personalizaci služeb a správu mobility. Centralizací dat účastníků UDM umožňuje konzistentní vynucování politik v celé síti, podporuje plynulou mobilitu a kontinuitu relací a poskytuje jediný zdroj pravdy pro uživatelské profily. To je nezbytné pro pokročilé funkce 5G, jako je síťové dělení (network slicing), kde UDM poskytuje předplatitelské informace pro výběr síťového řezu. Její servisně orientovaný design navíc umožňuje flexibilní integraci, škálovatelnost a podporu nových služeb, čímž vytváří základ pro správu účastníků v éře 5G.

## K čemu slouží

UDM bylo vytvořeno, aby řešilo omezení zastaralé správy dat účastníků v sítích před 5G, která byla roztříštěná mezi různé síťové elementy. V 4G EPC spravovaly funkce jako Home Subscriber Server (HSS) uživatelské profily a autentizaci, ale architektura byla uzlově orientovaná a méně flexibilní. Rozmach různorodých služeb 5G, IoT a síťového dělení vyžadoval agilnější, škálovatelnější a sjednocený přístup ke správě dat.

Primární problém, který UDM řeší, je centralizace a standardizace zpracování dat účastníků. Konsoliduje funkce dříve rozprostřené mezi HSS, Home Location Register (HLR) a další entity do jediné, cloud-nativní síťové funkce. Toto sjednocení zjednodušuje provoz, snižuje duplikaci dat a poskytuje konzistentní pohled na účastníka všem ostatním funkcím jádra sítě. Jeho vytvoření bylo motivováno přechodem na servisně orientovanou architekturu (SBA), která vyžaduje, aby síťové funkce zpřístupňovaly své schopnosti jako znovupoužitelné služby.

Historicky se UDM vyvinulo z konceptů HSS/HLR, ale se zásadním architektonickým přepracováním. Umožňuje dynamickou správu předplatného, aktualizace politik v reálném čase a efektivní podporu masivního množství IoT zařízení. Oddělením aplikační logiky (UDM) od úložiště (UDR) umožňuje nezávislé škálování a využívá moderní principy cloudu a softwarově definovaných sítí. Tím řeší potřebu více programovatelného, automatizovaného a na služby zaměřeného jádra sítě, které je schopné podporovat širokou škálu případů užití předpokládaných pro 5G a další generace.

## Klíčové vlastnosti

- Centralizované úložiště a správa pro 3GPP data účastníků
- Generuje autentizační vektory a spravuje bezpečnostní přihlašovací údaje prostřednictvím ARPF
- Ukládá profily předplatného včetně dat o službách, politikách a výběru síťového řezu
- Poskytuje servisně orientovaná rozhraní (např. Nudm) ostatním síťovým funkcím 5GC
- Spravuje vazbu mezi trvalou (SUPI) a utajenou (SUCI) identitou účastníka
- Podporuje síťové dělení (network slicing) poskytováním předplatitelských informací specifických pro síťový řez

## Související pojmy

- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.540** (Rel-19) — 5G Service Based SMS Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.732** (Rel-16) — User Data Interworking, Coexistence, Migration Study
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.973** (Rel-19) — Separate HSS/UDM Deployment Scenarios & Solutions
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.540** (Rel-20) — 5G Network Resource Model (NRM) Management
- **TS 28.561** (Rel-20) — Management and Orchestration; Network Digital Twin
- … a dalších 46 specifikací

---

📖 **Anglický originál a plná specifikace:** [UDM na 3GPP Explorer](https://3gpp-explorer.com/glossary/udm/)
