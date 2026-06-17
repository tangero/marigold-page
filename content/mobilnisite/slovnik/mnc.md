---
slug: "mnc"
url: "/mobilnisite/slovnik/mnc/"
type: "slovnik"
title: "MNC – Mobile Network Code"
date: 2026-01-01
abbr: "MNC"
fullName: "Mobile Network Code"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mnc/"
summary: "Dvou- nebo tříciferný kód, který jednoznačně identifikuje operátora mobilní sítě v rámci země. Je klíčovou součástí mezinárodního identifikátoru mobilního účastníka (IMSI), umožňuje identifikaci účast"
---

MNC je dvou- nebo tříciferný kód, který jednoznačně identifikuje operátora mobilní sítě v rámci země a je klíčovou součástí IMSI pro identifikaci účastníka, roaming a směrování.

## Popis

Mobile Network Code (MNC) je klíčový identifikátor v systému 3GPP a tvoří část mezinárodního identifikátoru mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)). IMSI je globálně jednoznačné číslo uložené na SIM kartě účastníka a v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) operátora. Struktura IMSI je definována jako MCC-MNC-MSIN, kde [MCC](/mobilnisite/slovnik/mcc/) je Mobile Country Code, MNC je Mobile Network Code a [MSIN](/mobilnisite/slovnik/msin/) je Mobile Subscriber Identification Number. MNC konkrétně identifikuje operátora mobilní sítě (např. Vodafone, AT&T) v rámci země definované MCC. Jeho délka jsou buď dvě nebo tři číslice, jak definuje národní regulátor, a tato délka musí být konzistentní pro všechny operátory v dané zemi.

Z architektonického hlediska se MNC používá na více místech v síti. Při počátečním připojení k síti mobilní zařízení prezentuje své IMSI. Obsluhující síť (např. Visitor Location Register - VLR nebo Mobility Management Entity - [MME](/mobilnisite/slovnik/mme/)) extrahuje MCC a MNC k identifikaci domovské sítě účastníka. To spouští procedury autentizace a autorizace, kdy se obsluhující síť spojí s domovskou sítí účastníka (identifikovanou pomocí MCC+MNC) k ověření přihlašovacích údajů a načtení profilu účastníka. MNC je také zásadní pro směrování signalizace a uživatelských dat, zejména v roamingových scénářích. Když je účastník v roamingu, navštívená síť použije MNC (společně s MCC) ke směrování signalizačních zpráv do správné domovské sítě pro autorizaci služeb a účtování.

Mimo základní síťové procedury je MNC vysílán buňkami jako součást identity veřejné pozemní mobilní sítě (PLMN) (MCC+MNC). Mobilní zařízení používají tuto vysílanou informaci k identifikaci dostupných sítí pro výběr buňky, její převýběr a předávání hovoru. SIM karta zařízení obsahuje seznam preferovaných PLMN (domovských a roamingových partnerů), které jsou prioritizovány na základě kombinací MCC-MNC. To zajišťuje, že se zařízení připojí k nejvhodnější síti. Role MNC zasahuje i do oblasti správy sítě a zákonného odposlechu, kde se používá k filtrování a identifikaci provozu náležejícího konkrétním operátorům. Jeho konzistentní definice napříč všemi releasy 3GPP zajišťuje zpětnou a dopřednou kompatibilitu v prostředí s více dodavateli a operátory.

## K čemu slouží

MNC byl vytvořen, aby vyřešil základní problém jednoznačné identifikace operátora mobilní sítě v globálním měřítku. Před standardizovanými číslovacími plány by proprietární identifikační schéma znemožnilo mezinárodní roaming, protože navštívená síť by neměla způsob, jak identifikovat a směrovat dotazy do domovské sítě účastníka. MNC jako součást [IMSI](/mobilnisite/slovnik/imsi/) definovaného v éře GSM (Release 99) stanovil univerzální adresovací schéma.

Toto adresování je klíčové pro umožnění automatizovaného roamingu, účtování a poskytování služeb. Když účastník cestuje do zahraničí, navštívená síť přečte MNC z IMSI a použije jej spolu s [MCC](/mobilnisite/slovnik/mcc/) k určení domovského operátora. To umožňuje navštívené síti navázat zabezpečené signalizační spojení ke správné domovské síti (HLR/HSS) k autentizaci uživatele a načtení dat o předplatném. Bez tohoto standardizovaného kódu by nebylo možné plynulé globální pokrytí. MNC také umožňuje regulačním orgánům spravovat rádiové spektrum a licencovat operátory v zemi, přičemž každému přidělí jedinečný kód, aby se předešlo konfliktům.

## Klíčové vlastnosti

- Globálně jednoznačný identifikátor operátora v kontextu země (v kombinaci s MCC)
- Integrální součást IMSI a vysílané PLMN identity
- Používá se pro výběr sítě, směrování a autentizaci účastníka
- Délka je 2 nebo 3 číslice, standardizovaná pro danou zemi
- Zásadní pro umožnění národního a mezinárodního roamingu
- Používá se v systémech správy sítě, provizioningu a zákonného odposlechu

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [MCC – Mobile Country Code](/mobilnisite/slovnik/mcc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.235** (Rel-12) — I-WLAN Interworking Management Object
- **TS 24.305** (Rel-19) — Selective Disabling of 3GPP UE Capabilities
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.367** (Rel-19) — Home NodeB Mobility Procedures
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [MNC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mnc/)
