---
slug: "mcc"
url: "/mobilnisite/slovnik/mcc/"
type: "slovnik"
title: "MCC – Mobile Country Code"
date: 2026-01-01
abbr: "MCC"
fullName: "Mobile Country Code"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mcc/"
summary: "Mobile Country Code (MCC) je trojmístný číselný kód, který jednoznačně identifikuje domovskou zemi účastníka mobilní sítě. Je první částí International Mobile Subscriber Identity (IMSI) a je zásadní p"
---

MCC je trojmístný číselný kód, který jednoznačně identifikuje domovskou zemi mobilního účastníka a tvoří první část IMSI pro mezinárodní roaming a identifikaci sítě.

## Popis

Mobile Country Code (MCC) je klíčový, standardizovaný identifikátor v rámci globálního telekomunikačního číslovacího plánu definovaného Mezinárodní telekomunikační unií ([ITU](/mobilnisite/slovnik/itu/)) a přijatého organizací 3GPP. Skládá se ze tří desítkových číslic (např. 310 pro Spojené státy, 262 pro Německo) a slouží jako primární zeměpisný identifikátor pro mobilního účastníka. MCC je trvale zakódován v [SIM](/mobilnisite/slovnik/sim/) kartě účastníka jako úvodní segment 15místného International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), který má formát MCC-MNC-MSIN. Tato struktura zajišťuje, že každý mobilní účastník na světě má globálně jedinečný identifikátor.

Z architektonického hlediska se MCC používá na prakticky všech vrstvách mobilní sítě, od rozhraní rádiového přístupu po páteřní síť. Když se mobilní zařízení zapne nebo vstoupí do nové oblasti, skenuje dostupné sítě a čte vysílané systémové informace, které zahrnují MCC a Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)) každé sítě. Zařízení používá toto MCC k určení, zda se nachází ve své domovské zemi (MCC odpovídá MCC na SIM kartě), nebo v navštívené zemi (MCC se liší). Tento počáteční krok je klíčový pro procedury výběru sítě a roamingu. Uvnitř páteřní sítě, konkrétně v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), je MCC klíčovým atributem používaným ke správnému směrování signalizačních zpráv a aplikaci odpovídajících profilů a politik účastníka.

MCC spolupracuje s Mobile Network Code (MNC) a společně tvoří [PLMN](/mobilnisite/slovnik/plmn/) ID (Public Land Mobile Network Identity), které jednoznačně identifikuje konkrétní síť operátora v rámci země. Síťové elementy jako Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), Serving GPRS Support Node (SGSN) a Mobility Management Entity (MME) používají PLMN ID (a tedy i MCC) pro funkce jako autentizace, registrace, předávání hovorů mezi buňkami (handover) a účtování. Při mezinárodním roamingu, když se účastník pokusí zaregistrovat v navštívené síti (VPLMN), použije VPLMN MCC z IMSI účastníka k identifikaci domovské země a následně dotazuje příslušnou signalizační síť mezi operátory (jako SS7 nebo Diameter-based IPX), aby kontaktovala domovskou síť (HPLMN) pro autentizaci a autorizaci služeb.

Jeho role je zásadní pro interoperabilitu a globální dosah mobilních komunikací. Umožňuje bezproblémovou mobilitu přes hranice tím, že poskytuje standardizovaný způsob, jak sítě identifikují zemi původu účastníka. To je nezbytné pro směrování hovorů a datových relací, aplikaci roamingových dohod, výpočet poplatků a zajištění zákonného odposlechu a nouzových služeb (např. určení správného centra tísňového volání na základě kódu země). MCC je statický, administrativně přidělený kód, který tvoří základ správy identity účastníka ve všech generacích mobilních sítí, od GSM po 5G.

## K čemu slouží

MCC byl vytvořen, aby vyřešil základní problém jednoznačné identifikace mobilních účastníků v globálním měřítku, což je předpoklad pro mezinárodní roaming. V počátcích buněčných sítí, které byly převážně národními systémy, nebyly schémata identifikace účastníků globálně koordinována. To by znemožnilo komunikaci a mobilitu přes hranice, protože navštívená síť by neměla způsob, jak identifikovat domovskou síť účastníka, aby získala autentizační data a informace pro účtování.

Primární motivací bylo vytvořit celosvětový číslovací plán, který by umožňoval jednoznačnou identifikaci země registrace účastníka. Tím byla řešena kritická potřeba interoperability mezi různými národními sítěmi provozovanými různými operátory. ITU v doporučení E.212 definovala strukturu IMSI a přidělila rozsahy MCC jednotlivým zemím. 3GPP tento standard přijala, čímž zajistila, že každá SIM karta vyrobená kdekoli na světě obsahuje globálně jedinečné IMSI začínající MCC.

Historicky bylo jeho zavedení spolu se systémem GSM (od verze R99 výše) klíčovým faktorem pro 'globální' charakter Global System for Mobile Communications. Vyřešilo omezení čistě národních číslovacích plánů a umožnilo automatizované, zabezpečené zacházení s roamingovými účastníky. Bez MCC by byla nezvladatelná složitá síť bilaterálních roamingových dohod, která je základem dnešní mobilní zkušenosti. MCC zůstává základním kamenem mobilní identity a podporuje vše od základního hlasového roamingu po sofistikované modely směrování provozu přes domovskou síť používané v datovém roamingu 4G a 5G.

## Klíčové vlastnosti

- Třímístný kód jednoznačně přidělený zemi nebo geografické oblasti
- První složka 15místného International Mobile Subscriber Identity (IMSI)
- V kombinaci s MNC tvoří jedinečnou PLMN Identity (PLMN-ID)
- Základní prvek pro procedury mezinárodního roamingu a výběru sítě
- Používá se globálně ve všech generacích buněčných sítí (GSM, UMTS, LTE, 5G)
- Administrativně přidělován a spravován organizací ITU

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [MNC – Mobile Network Code](/mobilnisite/slovnik/mnc/)
- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 24.103** (Rel-19) — Telepresence Protocol for IMS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.235** (Rel-12) — I-WLAN Interworking Management Object
- **TS 24.305** (Rel-19) — Selective Disabling of 3GPP UE Capabilities
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.367** (Rel-19) — Home NodeB Mobility Procedures
- … a dalších 18 specifikací

---

📖 **Anglický originál a plná specifikace:** [MCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcc/)
