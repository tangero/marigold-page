---
slug: "cs-ibcf"
url: "/mobilnisite/slovnik/cs-ibcf/"
type: "slovnik"
title: "CS-IBCF – Circuit Switched domain - Interconnection Border Control Function"
date: 2025-01-01
abbr: "CS-IBCF"
fullName: "Circuit Switched domain - Interconnection Border Control Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cs-ibcf/"
summary: "CS-IBCF je funkční entita v rámci IP Multimedia Subsystem (IMS), která poskytuje hraniční řídicí funkci pro propojení mezi sítí IMS a externími sítěmi s přepojováním okruhů (CS), jako jsou legacy sítě"
---

CS-IBCF je hraniční řídicí funkce IMS, která zajišťuje protokolovou interoperabilitu, skrytí topologie a zabezpečení pro propojení mezi sítí IMS a externími sítěmi s přepojováním okruhů, jako je PSTN/PLMN.

## Popis

CS-IBCF (Circuit Switched domain - Interconnection Border Control Function) je kritická komponenta v architektuře IMS (IP Multimedia Subsystem) definované 3GPP. Nachází se na hranici mezi sítí IMS a externími sítěmi s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)), jako je Public Switched Telephone Network (PSTN) nebo legacy Public Land Mobile Networks (PLMN). Jejím hlavním úkolem je fungovat jako brána a kontrolní bod pro veškerý signalizační provoz procházející mezi těmito dvěma odlišnými síťovými doménami. Architektonicky je CS-IBCF součástí rodiny IMS Interconnection Border Control Function ([IBCF](/mobilnisite/slovnik/ibcf/)), která dále zahrnuje TrGW (Transition Gateway) pro zpracování médií a samotnou IBCF pro IP-IP propojení. CS-IBCF se konkrétně zaměřuje na rozhraní CS domény a často komunikuje s funkcí Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)), která řídí mediální brány ([MGW](/mobilnisite/slovnik/mgw/)) provádějící konverzi mezi IP médii v IMS a médii založenými na TDM/CS.

Operačně CS-IBCF funguje tak, že zachycuje a zpracovává signalizační zprávy SIP (Session Initiation Protocol), které jsou určeny do CS sítí nebo z nich pocházejí. Když uživatel IMS iniciuje hovor na číslo v PSTN, je SIP INVITE směrován na CS-IBCF. CS-IBCF provádí několik klíčových funkcí: může fungovat jako SIP Back-to-Back User Agent ([B2BUA](/mobilnisite/slovnik/b2bua/)), který ukončí SIP dialog z IMS strany a vytvoří nový SIP dialog směrem k MGCF. Tento model B2BUA umožňuje skrytí topologie, kdy je vnitřní topologie sítě IMS a adresy uzlů skryty před externí CS sítí. Také umožňuje adaptaci protokolů, protože CS-IBCF může překládat mezi různými profily SIP nebo začleňovat informace potřebné pro interoperabilitu se signalizací [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part), kterou zpracovává MGCF.

Mezi klíčové součásti funkcionality CS-IBCF patří vynucování zabezpečení, kdy může aplikovat filtrační politiky, ověřovat příchozí požadavky a chránit před škodlivým provozem z CS domény. Dále poskytuje korelaci účtování tím, že asociuje identifikátory účtování mezi doménami IMS a CS, což je zásadní pro fakturaci. CS-IBCF také spravuje překlad síťových adres a portů a může řídit využití zdrojů. Jeho role je definována v 3GPP TS 29.235, která specifikuje SIP profil a procedury pro toto rozhraní. Centralizací těchto hraničních řídicích funkcí CS-IBCF zjednodušuje síťovou architekturu, zvyšuje zabezpečení a zajišťuje spolehlivou interoperabilitu služeb, čímž tvoří základní kámen migrace z legacy CS sítí na plně IP sítě IMS.

## K čemu slouží

CS-IBCF byla vytvořena, aby řešila základní výzvu propojení nové generace plně IP sítí IMS s rozsáhlou instalovanou základnou legacy telefonních sítí s přepojováním okruhů. Před IMS byly mobilní a pevné sítě převážně založeny na [CS](/mobilnisite/slovnik/cs/) a používaly protokoly jako ISUP pro řízení hovorů. Zavedení IMS se signalizací založenou na SIP a médii založenými na IP vytvořilo nesoulad v protokolech a architektuře. Jednoduché brány mohly zvládnout konverzi médií, ale na signalizační hranici byla potřeba inteligentní řídicí funkce pro správu zabezpečení, skrytí síťové topologie a zajištění správné interoperability služeb.

Hlavní problémy, které CS-IBCF řeší, jsou bezpečnostní zranitelnosti z přímé expozice základních prvků IMS, složitost správy propojení mezi operátory a nedostatek kontroly nad procesem interoperability. Bez CS-IBCF by IMS S-CSCF (Serving Call Session Control Function) musela komunikovat přímo s MGCF v doméně jiného operátora, čímž by odhalila svou IP adresu a schopnosti. CS-IBCF funguje jako zabezpečený demarkační bod, implementuje skrytí topologie pro ochranu vnitřní sítě. Také centralizuje logiku interoperability, čímž zjednodušuje přidávání nových partnerských propojení a zajišťuje konzistentní vynucování politik pro veškerý provoz směřující do CS sítí. Její vytvoření bylo motivováno postupným přechodem odvětví na plně IP sítě, který vyžadoval stabilní, standardizovanou hraniční funkci schopnou usnadnit toto období koexistence, což operátorům umožňuje nasadit IMS při zachování konektivity ke globální PSTN.

## Klíčové vlastnosti

- Funguje jako SIP Back-to-Back User Agent (B2BUA) pro signalizaci mezi doménami IMS a CS
- Poskytuje skrytí topologie, aby vnitřní struktura sítě IMS zůstala skryta před externími CS sítěmi
- Vynucuje bezpečnostní politiky včetně filtrování a ověřování příchozí signalizace z CS domény
- Umožňuje adaptaci protokolů a interoperabilitu mezi SIP a legacy CS signalizací (např. směrem k ISUP přes MGCF)
- Podporuje korelaci účtování správou identifikátorů účtování na hranici IMS-CS
- Centralizuje řízení pro CS propojení, čímž zjednodušuje správu sítě a vynucování politik

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [MGW – Media Gateway](/mobilnisite/slovnik/mgw/)

## Definující specifikace

- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking

---

📖 **Anglický originál a plná specifikace:** [CS-IBCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/cs-ibcf/)
