---
slug: "upt"
url: "/mobilnisite/slovnik/upt/"
type: "slovnik"
title: "UPT – Universal Personal Telecommunications"
date: 2025-01-01
abbr: "UPT"
fullName: "Universal Personal Telecommunications"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/upt/"
summary: "Standardizovaná sada schopností služeb umožňujících osobní mobilitu a personalizaci služeb napříč různými sítěmi a koncovými zařízeními. Umožňuje uživatelům přistupovat k telekomunikačním službám na z"
---

UPT je standardizovaná sada schopností umožňujících osobní mobilitu a přístup ke službám napříč sítěmi za použití osobního identifikátoru, čímž odděluje služby od konkrétní linky nebo zařízení.

## Popis

Universal Personal Telecommunications (UPT) je komplexní servisní rámec standardizovaný [ITU-T](/mobilnisite/slovnik/itu-t/) a přijatý 3GPP. Jeho základním principem je osobní mobilita, která umožňuje účastníkovi iniciovat a přijímat telekomunikační služby na jakémkoli koncovém zařízení, na jakémkoli místě a napříč více sítěmi, za použití jedinečného, na síti nezávislého osobního UPT čísla. Architektura odděluje identitu uživatele (UPT číslo) od síťové adresy konkrétního koncového zařízení. Toto je řízeno pomocí UPT servisního profilu uloženého v síťové databázi, který obsahuje uživatelské preference, odběry služeb a směrovací informace.

Operačně, pro příchozí hovor, síť dotazuje UPT servisní řídicí funkci (často integrovanou v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo v dedikovaném servisním řídicím bodě) pomocí vytočeného UPT čísla. Tato funkce načte profil uživatele, který může obsahovat pravidla pro doručení hovoru na základě času, identity volajícího nebo stavu registrace koncového zařízení. Následně přeloží UPT číslo na směrovatelnou síťovou adresu (jako je Mobile Station International Subscriber Directory Number ([MSISDN](/mobilnisite/slovnik/msisdn/)) nebo IP adresa) pro koncové zařízení, kde je uživatel aktuálně registrován. Pro odchozí hovory se UPT uživatel autentizuje (často pomocí osobního identifikačního čísla - [PIN](/mobilnisite/slovnik/pin/)) na koncovém zařízení, což následně umožní, aby byly hovory účtovány na jeho UPT účet, nikoli na linku daného zařízení.

UPT zahrnuje několik klíčových síťových komponent: UPT číslo jako globální identifikátor, autentizační mechanismy, databáze servisních profilů a flexibilní logiku pro zpracování hovorů. Využívá koncepty Inteligentní sítě (Intelligent Network - [IN](/mobilnisite/slovnik/in/)), přičemž servisní logika je prováděna v síťových uzlech oddělených od základních funkcí přepojování hovorů. V systémech 3GPP byly schopnosti UPT integrovány do servisní architektury jádra sítí GSM/UMTS/LTE/5G, což ovlivnilo návrh správy mobility a zpracování účastnických dat. Je předchůdcem moderních konceptů, jako jsou služby Virtual Private Network ([VPN](/mobilnisite/slovnik/vpn/)) a uživatelsky orientovaná mobilita, a klade základy pro servisní vrstvu nezávislou na přístupové technologii.

## K čemu slouží

UPT bylo koncipováno za účelem překonání zásadního omezení tradiční telefonie, kde byla služba vázána na konkrétní fyzickou přístupovou linku nebo koncové zařízení. To omezovalo mobilitu uživatele a nutilo jednotlivce spravovat více kontaktních čísel pro domácí, kancelářské a mobilní telefony. Hnacím vizí byla 'osobní dostupnost' (personal communicability) – dosažení na osobu, nikoli na místo nebo zařízení. Cílem bylo poskytnout univerzální, celoživotní telekomunikační identitu.

Její vytvoření řešilo několik klíčových problémů: množení čísel pro jednoho uživatele, neschopnost zachovat konzistentní identitu při stěhování nebo změně poskytovatele služeb a složitost správy pravidel přesměrování hovorů napříč více zařízeními. Zavedením osobního identifikátoru a servisního profilu je UPT vyřešilo oddělením identity od umístění. To umožnilo pokročilé funkce, jako je dosažitelnost na jedno číslo, personalizované třídění příchozích hovorů a konzistentní účtování napříč různými sítěmi. Zatímco konkrétní služba UPT, jak byla nabízena v raných sítích GSM, se vyvinula, její základní principy přímo ovlivnily vývoj následných funkcí mobility a personalizace v celulárních sítích, včetně integrace konceptů konvergence pevné a mobilní sítě.

## Klíčové vlastnosti

- Osobní mobilita využívající jediné, na síti nezávislé UPT číslo pro celý život.
- Personalizace služeb prostřednictvím uživatelem definovaného servisního profilu řídícího zpracování hovorů.
- Autentizační mechanismy (např. PIN) pro autorizaci použití služby z jakéhokoli koncového zařízení.
- Integrace s architekturami Inteligentní sítě (Intelligent Network - IN) pro flexibilní řízení služeb.
- Podpora pro třídění příchozích hovorů, časově závislé směrování a zpracování specifické pro volajícího.
- Oddělení identity účastníka od identity koncového zařízení a síťové adresy.

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 36.863** (Rel-12) — CRS Interference Mitigation for Homogeneous Networks
- **TS 38.843** (Rel-19) — Study on AI/ML for NR Air Interface
- **TR 38.858** (Rel-18) — Technical Report on Evolution of NR Duplex Operation
- **TR 38.864** (Rel-18) — Technical Report on Network Energy Savings for NR

---

📖 **Anglický originál a plná specifikace:** [UPT na 3GPP Explorer](https://3gpp-explorer.com/glossary/upt/)
