---
slug: "mc"
url: "/mobilnisite/slovnik/mc/"
type: "slovnik"
title: "MC – Mission Critical User Identity"
date: 2026-01-01
abbr: "MC"
fullName: "Mission Critical User Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mc/"
summary: "Jedinečný identifikátor pro uživatele a zařízení v rámci služeb 3GPP Mission Critical (MC), jako jsou MCPTT, MCVideo a MCData. Umožňuje zabezpečenou a prioritní komunikaci pro uživatele z oblasti veře"
---

MC je jedinečný identifikátor pro uživatele a zařízení v rámci služeb Mission Critical (kritické komunikace) definovaných 3GPP, který umožňuje zabezpečenou a prioritní komunikaci pro uživatele z oblasti veřejné bezpečnosti a kritické infrastruktury.

## Popis

Mission Critical User Identity (MC) je základní identifikátor v architektuře služeb Mission Critical Services definované 3GPP. Jedná se o globálně jedinečný identifikátor přiřazený uživateli (např. záchranáři) nebo funkčnímu aliasu (např. 'Hasicí vůz 5'), který je přihlášen k odběru služeb kritické komunikace. Tato identita se používá v celé aplikační vrstvě služeb pro ověřování, autorizaci, vyhledávání služeb a správu relací. Je odlišná od, ale může být asociována s, jinými síťovými identitami, jako je [IMSI](/mobilnisite/slovnik/imsi/) nebo [MSISDN](/mobilnisite/slovnik/msisdn/), což umožňuje službám kritické komunikace fungovat nezávisle na podkladové technologii přístupové sítě (např. LTE, 5G).

Identita MC je klíčovou součástí rámce služeb MC definovaného ve specifikaci 3GPP TS 23.280 a souvisejících dokumentech. Používá ji klient služby Mission Critical na uživatelském zařízení (UE) pro registraci na platformě služeb MC, která zahrnuje základní funkce, jako je server Mission Critical Push To Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Během registrace a následných požadavků na službu je identita MC ověřována proti profilu předplatného uživatele uloženému v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo v dedikované databázi služeb Mission Critical. Tím se zajišťuje, že pouze autorizovaný personál může přistupovat ke skupinám kritické komunikace, iniciovat nouzová volání nebo používat jiné prioritní funkce.

Z architektonického hlediska identita MC umožňuje klíčové vlastnosti služeb. Podporuje individuální i skupinovou komunikaci, což umožňuje adresování uživatelů přímo nebo jako součást předdefinované mluvící skupiny (talkgroup). Tato identita je také zásadní pro zabezpečení, protože tvoří základ pro vzájemné ověřování mezi UE a sítí s využitím přihlašovacích údajů uložených na UICC nebo v systému softwarových přihlašovacích údajů. Dále usnadňuje kontinuitu služeb a mobilitu; když se uživatel pohybuje mezi buňkami nebo sítěmi, identita MC umožňuje aplikační vrstvě služeb MC udržovat aktivní relace uživatele a uplatňovat konzistentní politiky, jako je přednostní přerušení a prioritní QoS, bez ohledu na polohu.

V praxi je identita MC často strukturována podle specifické konvence pojmenování, například ve formátu Uniform Resource Name ([URN](/mobilnisite/slovnik/urn/)) definovaném v 3GPP TS 23.003 (např. 'urn:uuid:...' nebo schéma specifické pro kritickou komunikaci). Tento strukturovaný formát umožňuje federaci mezi různými poskytovateli služeb nebo organizacemi veřejné bezpečnosti, což zajišťuje interoperabilitu při rozsáhlých incidentech. Správa těchto identit, včetně jejich vytváření, přiřazování a životního cyklu, je typicky zajišťována systémem správy operátora služeb kritické komunikace, který komunikuje s prvky jádra sítě za účelem provisioningu dat předplatného.

## K čemu slouží

Identita MC byla vytvořena, aby řešila specifické potřeby komunikace pro veřejnou bezpečnost a kritickou infrastrukturu v rámci komerčních 3GPP sítí. Tradiční mobilní identifikátory, jako je [MSISDN](/mobilnisite/slovnik/msisdn/) (telefonní číslo), byly navrženy pro spotřebitelské služby a postrádají granularitu, zabezpečení a funkční požadavky potřebné pro operace kritické komunikace. Byla potřeba dedikovaná identita, která by podporovala skupinovou komunikaci, vysokou prioritu, bezpečné ověřování a interoperabilitu napříč organizačními a národními hranicemi.

Před jejím standardizováním používaly proprietární systémy, jako [TETRA](/mobilnisite/slovnik/tetra/) nebo [P25](/mobilnisite/slovnik/p25/), vlastní schémata identit, což bránilo interoperabilitě s moderními IP sítěmi LTE a 5G. Zavedení služeb MC v 3GPP Release 13 vyžadovalo základní mechanismus identity, který by byl nezávislý na podkladové přístupové technologii, což umožnilo nasazení aplikací kritické komunikace přes LTE a později 5G NR. Tato identita řeší problém jedinečné a bezpečné identifikace záchranářů a jejich funkčních rolí v rámci standardizovaného a škálovatelného rámce.

Identita MC dále umožňuje realizaci klíčových požadavků služeb, jako je dynamická správa skupin, nouzové varování a inherentní zabezpečení. Poskytuje ukotvovací bod pro uplatňování QoS politik pro kritickou komunikaci, což zajišťuje, že komunikační relace pro autorizované identity obdrží potřebné síťové prostředky a prioritu, a to i během zahlcení sítě. Její vytvoření bylo motivováno celosvětovým úsilím o nahrazení nebo doplnění starších systémů pozemní mobilní rádiové komunikace (LMR) širokopásmovými řešeními, což vyžadovalo robustní a standardizovaný systém správy identit v jádru tohoto přechodu.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro uživatele a funkční aliasy
- Základ pro ověřování a autorizaci ve službách MC
- Umožňuje adresování pro individuální a skupinovou (talkgroup) komunikaci
- Podporuje kontinuitu služeb a mobilitu napříč síťovými oblastmi
- Nezávislý na podkladové technologii přístupové sítě (LTE, 5G)
- Strukturovaný formát (např. URN) pro federaci a interoperabilitu

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 22.119** (Rel-19) — Maritime Communication Service Requirements
- **TS 23.180** (Rel-19) — MC services support in IOPS mode
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.281** (Rel-20) — MCVideo Functional Architecture and Flows
- **TS 23.282** (Rel-20) — MCData Functional Architecture & Info Flows
- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.783** (Rel-18) — Technical Report on Mission Critical Services over 5GS
- **TS 23.784** (Rel-16) — Discreet Listening for Mission Critical Services
- **TS 23.790** (Rel-15) — FRMCS Gap Analysis and Architecture Enhancements
- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 24.482** (Rel-19) — Mission Critical Services Identity Management
- … a dalších 19 specifikací

---

📖 **Anglický originál a plná specifikace:** [MC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mc/)
