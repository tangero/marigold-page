---
slug: "vlr"
url: "/mobilnisite/slovnik/vlr/"
type: "slovnik"
title: "VLR – Visitor Location Register"
date: 2026-01-01
abbr: "VLR"
fullName: "Visitor Location Register"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vlr/"
summary: "Databáze v jádru sítě, která ukládá údaje o mobilních účastnících, kteří právě roamují v oblasti obsluhované konkrétním Mobile Switching Center (MSC). Umožňuje směrování hovorů, autentizaci a poskytov"
---

VLR je databáze v jádru sítě, která dočasně ukládá údaje o účastníkovi z jeho domovského HLR, aby umožnila směrování hovorů, autentizaci a poskytování služeb, zatímco účastník roamuje v oblasti konkrétního MSC.

## Popis

Visitor Location Register (VLR) je základní databáze v okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) doméně mobilní sítě 2G/3G. Vždy je umístěna společně s konkrétním Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a slouží mu. Když mobilní účastník vstoupí do geografické oblasti řízené MSC, příslušný VLR požádá domovský Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) účastníka o kopii jeho profilu služeb. Tento profil obsahuje klíčové informace, jako je International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), přihlášené služby (např. přesměrování hovorů nebo zákazy) a autentizační parametry. VLR tato data uchovává po dobu přítomnosti účastníka ve své oblasti, což umožňuje MSC zpracovávat sestavování hovorů, doplňkové služby a správu mobility (např. aktualizace polohy) bez nutnosti dotazovat se na vzdálený HLR při každé transakci, čímž se snižuje signalizační zatížení a latence.

Z architektonického hlediska tvoří dvojice VLR-MSC primární uzel služeb pro okruhově spínaný hlas a [SMS](/mobilnisite/slovnik/sms/). VLR komunikuje s HLR prostřednictvím protokolu [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) po signalizační síti [SS7](/mobilnisite/slovnik/ss7/). Komunikuje také s dalšími MSC/VLR při procedurách předávání hovoru a s Authentication Center (AuC) za účelem získání bezpečnostních trojic ([RAND](/mobilnisite/slovnik/rand/), SRES, Kc) pro autentizaci a šifrování účastníka. VLR přiřazuje účastníkovi dočasný identifikátor Temporary Mobile Subscriber Identity (TMSI) pro zvýšení soukromí, který na rozhraní rádiové komunikace maskuje jeho trvalé IMSI.

Jeho role je klíčová pro mobilitu. Sleduje přesnou polohu účastníka ve své oblasti, typicky na úrovni lokální oblasti (Location Area, LA). Když se účastník přesune, VLR aktualizuje HLR o nové poloze a může také informovat předchozí VLR, aby vymazal svůj dočasný záznam. Pro příchozí hovory nebo SMS se Gateway MSC (GMSC) dotazuje HLR na směrovací informace. HLR se následně dotazuje aktuálního VLR na Mobile Station Roaming Number (MSRN), což je dočasné číslo používané k směrování hovoru na obsluhující MSC. VLR tedy funguje jako místní kotva a správce relace pro navštěvující účastníky, což umožňuje plynulé roamování a kontinuitu služeb napříč hranicemi sítí.

## K čemu slouží

VLR byl vytvořen, aby vyřešil základní problém umožnění mobility a roamování účastníků v celulárních sítích. V raných mobilních systémech by centrální databáze byla zahlcena dotazy na každý pokus o hovor nebo aktualizaci polohy od každého účastníka v síti bez ohledu na jeho polohu. Architektura VLR decentralizuje správu údajů o účastnících zavedením hierarchické struktury s trvalou domovskou databází (HLR) a dočasnými návštěvnickými databázemi (VLR). Tento návrh dramaticky snižuje signalizační provoz v jádru sítě a zkracuje dobu sestavení hovoru.

K jeho vytvoření vedla potřeba efektivního využití síťových zdrojů a škálovatelného růstu počtu účastníků. Díky lokálnímu ukládání dat o účastníkovi v místě poskytování služby (oblast MSC) síť minimalizuje dálkovou signalizaci k HLR, který může být pro roamující účastníky v jiné zemi. Toto lokální ukládání do mezipaměti je zásadní pro poskytování služeb v reálném čase, jako jsou hlasové hovory. Dále VLR umožňuje implementaci procedur založených na poloze (např. vyvolání účastníka pouze v jeho aktuální lokální oblasti) a přiřazování dočasných identit (TMSI), což zvyšuje soukromí účastníka tím, že brání sledování trvalého IMSI na rádiovém rozhraní.

Před konceptem rozdělení VLR/HLR jednodušší architektury nemohly efektivně škálovat pro podporu celostátního nebo mezinárodního roamingu. VLR, jak byl definován od GSM, se stal základním kamenem pro správu navštěvujících účastníků. Tento koncept byl tak úspěšný, že ovlivnil pozdější architektury jádra sítě, a to i když se síť vyvíjela směrem k IP systémům v pozdějších vydáních 3GPP.

## Klíčové vlastnosti

- Dočasné ukládání profilů roamujících účastníků načtených z HLR
- Umístění společně s konkrétním MSC a vyhrazená služba pro něj
- Přiřazení a správa dočasných identit účastníka (TMSI) pro zachování soukromí
- Správa lokálních oblastí a zpracování procedur aktualizace polohy
- Poskytování roamovacích čísel (MSRN) pro směrování příchozích hovorů
- Zpracovává autentizaci a šifrování prostřednictvím rozhraní s AuC

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [TMSI – Temporary Mobile Subscriber Identifier](/mobilnisite/slovnik/tmsi/)
- [AUC – Authentication Centre](/mobilnisite/slovnik/auc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TR 26.944** (Rel-19) — QoE, ESQoS and SQoS metrics for 3G multimedia services
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 29.198** (Rel-9) — OSA API Overview Specification
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [VLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/vlr/)
