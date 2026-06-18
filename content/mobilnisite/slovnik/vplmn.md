---
slug: "vplmn"
url: "/mobilnisite/slovnik/vplmn/"
type: "slovnik"
title: "VPLMN – Visited Public Land Mobile Network"
date: 2025-01-01
abbr: "VPLMN"
fullName: "Visited Public Land Mobile Network"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vplmn/"
summary: "VPLMN je mobilní síť, ve které se účastník aktuálně nachází v roamingu a která je odlišná od jeho domovské PLMN (HPLMN). Poskytuje přístup k rádiovému rozhraní a služby jádra sítě navštěvujícímu uživa"
---

VPLMN je mobilní síť, ve které se účastník aktuálně nachází v roamingu a která poskytuje přístup k rádiovému rozhraní a služby jádra sítě navštěvujícímu uživateli, a je odlišná od jeho domovské sítě.

## Popis

Visited Public Land Mobile Network (VPLMN) je základním konceptem v mobilním roamingu. Označuje síť provozovanou mobilním operátorem (navštíveným operátorem) v geografické oblasti, kde se aktuálně nachází uživatelské zařízení (UE) účastníka a přijímá služby, ale ke které účastník nemá primární předplatné. Předplatné účastníka je vedeno u samostatné domovské [PLMN](/mobilnisite/slovnik/plmn/) ([HPLMN](/mobilnisite/slovnik/hplmn/)). Když je UE zapnuto nebo přesune se do pokrytí VPLMN, provede výběr sítě, často s preferencí VPLMN na základě roamingových dohod.

Z architektonického hlediska se VPLMN skládá z vlastní kompletní sady síťových prvků: uzlů přístupové rádiové sítě (RAN), jako jsou gNB nebo [eNB](/mobilnisite/slovnik/enb/), a funkcí jádra sítě, jako je funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5G, nebo entita správy mobility ([MME](/mobilnisite/slovnik/mme/)) v 4G a Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)). Klíčové je, že pro roamingového účastníka jádro sítě VPLMN komunikuje s HPLMN účastníka. Toto propojení probíhá primárně přes roamingová rozhraní (např. rozhraní N9/N16 mezi funkcemi uživatelské roviny VPLMN a HPLMN nebo rozhraní S8/S6a v 4G). VPLMN zajišťuje místní správu rádiových zdrojů, správu mobility ve své oblasti a poskytuje připojení k paketové datové síti, ale pro autentizaci, autorizaci účastníka a data profilu se spoléhá na HPLMN prostřednictvím Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)).

Během provozu, když se roamingové UE připojí k VPLMN, prvky jádra sítě VPLMN identifikují HPLMN účastníka z International Mobile Subscriber Identity (IMSI). VPLMN poté směruje autentizační signalizaci do autentizačního centra HPLMN. Po úspěšné autentizaci HPLMN poskytne VPLMN profil účastníka včetně povolených služeb a parametrů QoS. Funkce správy relace VPLMN následně pro UE zřídí datovou relaci. Data uživatelské roviny mohou být směrována lokálně v zemi VPLMN (Local Breakout) nebo zpět do HPLMN (Home Routed) v závislosti na roamingové dohodě a službě.

Úlohou VPLMN je rozšířit pokrytí služeb pro účastníky mimo pokrytí jejich domovské sítě a umožnit tak globální mobilitu. Je odpovědná za poskytování služeb – hlasu, dat a SMS – roamingovému uživateli v reálném čase. VPLMN také provádí účtování, generuje záznamy o volání (CDR), které jsou vyúčtovány s HPLMN. Vztah je upraven komerčními roamingovými dohodami a technickými standardy (jako jsou ty od GSM Association), které zajišťují interoperabilitu, zabezpečení a konzistentní kvalitu služeb pro roamingové účastníky.

## K čemu slouží

Koncept VPLMN existuje proto, aby umožnil bezproblémové mobilní služby napříč různými síťovými operátory a zeměmi, což je základem globálního roamingu. Bez něj by mobilní telefon fungoval pouze v pokrytí svého domovského síťového operátora, což by výrazně omezilo mobilitu. Problém, který řeší, je poskytování nepřetržité služby účastníkovi, když cestuje mimo licencované geografické území své HPLMN.

Historicky šlo o klíčovou inovaci GSM (2G) oproti dřívějším celulárním systémům. Architektura čistě odděluje 'domovskou' síť, která vlastní vztah se zákazníkem a předplatné, od 'navštívené' sítě, která poskytuje fyzickou infrastrukturu. Toto oddělení umožňuje škálovatelný roaming. HPLMN nemusí budovat infrastrukturu všude a VPLMN může generovat příjmy obsluhou návštěvníků. Standardizovaná rozhraní (definovaná 3GPP a GSMA) zajišťují, že účastník z jakékoli kompatibilní HPLMN může využívat služeb na jakékoli kompatibilní VPLMN.

VPLMN řeší omezení monolitických síťových architektur tím, že umožňuje konkurenci a spolupráci. Umožňuje stovkám operátorů po celém světě se vzájemně propojit a vytvořit globální služební strukturu. Pro účastníka zajišťuje transparentnost – jeho telefon v zahraničí 'prostě funguje'. Pro operátory vytváří obchodní model sdílení výnosů. Vývoj od 2G do 5G tento model zdokonalil, zavedl koncepty jako S8HR (Home Routed roaming) a LBO (Local Breakout) pro data a řízení roamingu pro optimalizaci výběru sítě, ale základní dichotomie HPLMN/VPLMN zůstává ústřední pro všechny specifikace mobility a roamingu 3GPP.

## Klíčové vlastnosti

- Poskytuje přístup k rádiovému rozhraní a konektivitu jádra sítě roamingovým účastníkům.
- Propojuje se s HPLMN prostřednictvím standardizovaných roamingových rozhraní (např. S8, N9, N32).
- Provádí místní správu mobility a správu relace pro navštěvující UE.
- Spoléhá na HPLMN pro autentizaci účastníka, autorizaci a získání profilu.
- Generuje záznamy pro účtování roamingového využití pro vyúčtování s HPLMN.
- Podporuje architektury uživatelské roviny typu home-routed i local breakout pro datový provoz.

## Související pojmy

- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [GSMA – Global System for Mobile communications Association](/mobilnisite/slovnik/gsma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 23.849** (Rel-11) — Study on IMS Roaming Media Optimization
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TR 28.840** (Rel-18) — Technical Report
- … a dalších 17 specifikací

---

📖 **Anglický originál a plná specifikace:** [VPLMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/vplmn/)
