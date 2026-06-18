---
slug: "nni"
url: "/mobilnisite/slovnik/nni/"
type: "slovnik"
title: "NNI – Network to Network Interfaces"
date: 2025-01-01
abbr: "NNI"
fullName: "Network to Network Interfaces"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nni/"
summary: "NNI označuje standardizovaná rozhraní mezi různými sítěmi nebo síťovými prvky v systémech 3GPP. Umožňují interoperabilitu, signalizaci a výměnu dat přes síťové hranice, což je klíčové pro provoz ve ví"
---

NNI je standardizované rozhraní mezi různými sítěmi nebo síťovými prvky v systémech 3GPP, které umožňuje interoperabilitu, signalizaci a výměnu dat přes síťové hranice.

## Popis

Rozhraní mezi sítěmi (Network to Network Interfaces, NNI) jsou standardizovaná rozhraní definovaná 3GPP, která usnadňují komunikaci mezi odlišnými sítěmi nebo mezi různými síťovými prvky v prostředí více sítí. Tato rozhraní jsou klíčová pro zajištění interoperability, signalizace a výměny dat přes síťové hranice, například mezi dvěma operátory mobilních sítí, mezi páteřní sítí a externí sítí nebo mezi různými administrativními doménami. Specifikace NNI pokrývají protokoly, formáty zpráv a procedury pro zajištění bezproblémové interakce.

V architektuře 3GPP jsou rozhraní NNI implementována napříč různými doménami, včetně rozhraní páteřní sítě (např. mezi [MME](/mobilnisite/slovnik/mme/) v různých sítích), roamovacích rozhraní (např. pro komunikaci mezi operátory) a rozhraní s externími sítěmi, jako jsou IP sítě nebo jiní poskytovatelé služeb. Příklady zahrnují rozhraní pro správu mobility, navázání relace, přenos účtovacích dat a výměnu bezpečnostního kontextu. Často využívají protokoly jako Diameter, [GTP](/mobilnisite/slovnik/gtp/) nebo [SIP](/mobilnisite/slovnik/sip/), upravené pro scénáře mezi sítěmi.

Provoz NNI zahrnuje standardizovanou výměnu zpráv mezi síťovými entitami. Například při roamingu mezi sítěmi umožňuje NNI domovské síti autentizovat uživatele navštěvujícího cizí síť, přenášet data účastníka a zpracovávat fakturační informace. Mezi klíčové komponenty patří koncové body rozhraní (např. síťové brány nebo hraniční kontroléry), protokolový zásobník (definující transportní, relační a aplikační vrstvu) a sada zpráv (včetně požadavků, odpovědí a chybových kódů). Tato rozhraní zajišťují, že sítě mohou spolupracovat bez nutnosti proprietárních úprav, což podporuje globální mobilitu a kontinuitu služeb.

NNI hrají zásadní roli při umožňování funkcí, jako je mezinárodní roaming, poskytování služeb mezi operátory a federace sítí. Poskytují technický základ pro sdílení zdrojů, koordinaci politik a zajištění bezproblémového uživatelského zážitku napříč administrativními hranicemi. Standardizací NNI zajišťuje 3GPP, že se mobilní operátoři po celém světě mohou spolehlivě propojovat, čímž podporuje soudržný globální telekomunikační ekosystém.

## K čemu slouží

Rozhraní NNI byla vytvořena k řešení problému interoperability mezi různými sítěmi a síťovými prvky v mobilní telekomunikaci. Jak se mobilní sítě vyvíjely z izolovaných systémů na propojenou globální infrastrukturu, potřeba standardizovaných rozhraní se stala klíčovou pro umožnění roamingu, služeb ve více sítích a efektivního sdílení zdrojů. Bez NNI by každé propojení sítí vyžadovalo vlastní, proprietární řešení, což by vedlo ke složitosti, vysokým nákladům a omezené škálovatelnosti.

Historicky měly rané mobilní sítě omezené možnosti propojení mezi sítěmi, ale s růstem globálního roamingu a služeb více operátorů zavedla 3GPP specifikace NNI od verze [R99](/mobilnisite/slovnik/r99/). Tato rozhraní řeší omezení, jako jsou nekompatibilní signalizační protokoly, odlišné účtovací mechanismy a bezpečnostní mezery mezi sítěmi. Poskytují společný rámec pro sítě k výměně uživatelských dat, správě relací, zpracování fakturace a vynucování bezpečnostních politik přes hranice.

Motivace pro vývoj NNI zahrnuje podporu mezinárodní mobility, umožnění poskytovatelům služeb nabízet bezproblémový zážitek napříč sítěmi a usnadnění optimalizace síťových zdrojů (např. sdílení infrastruktury). Definováním NNI umožňuje 3GPP operátorům efektivně se propojovat, snižovat bariéry nasazení a podporovat konkurenci a inovace na telekomunikačním trhu. Jsou nezbytné pro moderní mobilní ekosystém, kde uživatelé očekávají nepřerušenou službu bez ohledu na síť nebo polohu.

## Klíčové vlastnosti

- Standardizovaná rozhraní pro komunikaci mezi sítěmi
- Podpora protokolů jako Diameter, GTP a SIP
- Umožňují roaming, správu relací a účtování napříč sítěmi
- Definují formáty zpráv a procedury pro interoperabilitu
- Usnadňují výměnu bezpečnostního kontextu mezi sítěmi
- Umožňují sdílení zdrojů a koordinaci politik napříč administrativními doménami

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 23.889** (Rel-10) — Local Call Local Switch Core Network Impact Study
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.930** (Rel-19) — WebRTC Enhancements for Immersive RTC over 5G
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [NNI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nni/)
