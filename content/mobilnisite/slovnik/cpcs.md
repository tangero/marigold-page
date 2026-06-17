---
slug: "cpcs"
url: "/mobilnisite/slovnik/cpcs/"
type: "slovnik"
title: "CPCS – Common Part Convergence Sublayer"
date: 2025-01-01
abbr: "CPCS"
fullName: "Common Part Convergence Sublayer"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cpcs/"
summary: "Common Part Convergence Sublayer (CPCS) je protokolová vrstva v rámci transportní síťové vrstvy rozhraní Iub, standardizovaná v 3GPP. Poskytuje společné datové transportní služby pro různé protokoly u"
---

CPCS je Common Part Convergence Sublayer (společná konvergenční podsložka), protokolová vrstva v rozhraní Iub, která poskytuje společné transportní služby pro protokoly uživatelské roviny mezi RNC a Node B.

## Popis

Common Part Convergence Sublayer (CPCS) je základní součástí transportní síťové vrstvy v architektuře rozhraní Iub definované 3GPP, které spojuje Radio Network Controller (RNC) a Node B v sítích UMTS. Jako součást protokolového zásobníku adaptační vrstvy [ATM](/mobilnisite/slovnik/atm/) typu 2 ([AAL2](/mobilnisite/slovnik/aal2/)) pracuje CPCS nad Service Specific Convergence Sublayer (SSCS) a pod Segmentation and Reassembly (SAR) podsložkou. Její primární funkcí je poskytnout standardizované rozhraní pro protokoly vyšších vrstev pro přístup k transportním službám AAL2, abstrahuje podrobnosti přenosu ATM buněk a zároveň zajišťuje spolehlivé doručování dat.

Architektonicky se CPCS nachází v protokolové vrstvě AAL2 definované v doporučení [ITU-T](/mobilnisite/slovnik/itu-t/) I.363.2 a adaptované 3GPP pro rozhraní mobilních sítí. Zpracovává zapouzdření uživatelských dat z různých entit SSCS do CPCS Protocol Data Units (PDU), které jsou následně předány SAR podsložce pro segmentaci do ATM buněk. Struktura CPCS PDU zahrnuje hlavičku obsahující pole indikace délky a pořadového čísla, pole datové části pro uživatelská data a zápatí s výplní a cyklickým redundantním součtem ([CRC](/mobilnisite/slovnik/crc/)) pro detekci chyb. Tento strukturovaný přístup umožňuje, aby více logických spojení (AAL2 kanálů) sdílelo jediný virtuální okruh ATM prostřednictvím statistického multiplexování.

Při provozu přijímá CPCS datové jednotky služby od entit SSCS, které byly klasifikovány podle typu služby (jako hlas, okruhově přepínaná data nebo paketově přepínaná data). Přidává potřebné informace hlavičky a zápatí CPCS, provádí indikaci délky pro vymezení hranic PDU a implementuje číslování sekvence pro zachování pořadí paketů. Mechanismus CRC v zápatí poskytuje schopnosti detekce chyb, což umožňuje identifikaci poškozených paketů a jejich případné opětovné vyslání vyššími vrstvami. CPCS také zpracovává výplň, aby zajistila, že PDU je v souladu s požadavky SAR podsložky, která segmentuje CPCS PDU do 48bajtových datových částí ATM buněk.

V architektuře sítí 3GPP hraje CPCS klíčovou roli v transportu uživatelské roviny rozhraní Iub, zejména pro vyhrazené kanály ([DCH](/mobilnisite/slovnik/dch/)) a společné kanály. Umožňuje efektivní využití šířky pásma tím, že více služeb s nízkým přenosovým tokem (jako hovory) může sdílet stejné transportní prostředky prostřednictvím multiplexování AAL2. Standardizace CPCS ve specifikacích 3GPP zajišťuje interoperabilitu mezi zařízeními různých výrobců a poskytuje konzistentní transportní mechanismus pro různé služby nosičů rádiového přístupu, od okruhově přepínaných hlasových spojení po paketově přepínaná datová spojení.

## K čemu slouží

Common Part Convergence Sublayer byla vytvořena, aby řešila potřebu efektivního přenosu více služeb s nízkým přenosovým tokem přes rozhraní založená na [ATM](/mobilnisite/slovnik/atm/) v raných sítích 3G UMTS. Před její standardizací vyžadovaly různé služby samostatná transportní spojení, což vedlo k neefektivnímu využití šířky pásma a složitému řízení sítě. CPCS jako součást protokolového zásobníku [AAL2](/mobilnisite/slovnik/aal2/) umožnila statistické multiplexování více služeb přes jediný virtuální okruh ATM, což významně zlepšilo efektivitu transportu pro hlas a další zpoždění citlivý provoz s proměnným přenosovým tokem.

Historicky byl vývoj CPCS motivován požadavky UMTS Release 99, které potřebovaly podporovat jak okruhově přepínané, tak paketově přepínané služby přes společnou transportní infrastrukturu. Tradiční adaptační vrstvy ATM jako [AAL1](/mobilnisite/slovnik/aal1/) a AAL5 byly neefektivní pro smíšené vzorce provozu očekávané v mobilních sítích – AAL1 byla optimalizována pro služby s konstantním přenosovým tokem, ale plýtvala šířkou pásma pro provoz s proměnným tokem, zatímco AAL5 poskytovala efektivní paketový transport, ale zaváděla nadměrné zpoždění pro služby v reálném čase. CPCS v rámci AAL2 poskytla optimální kompromis, nabízející nízké zpoždění pro služby v reálném čase při zachování efektivního využití šířky pásma prostřednictvím multiplexování.

Vytvoření CPCS speciálně pro sítě 3GPP řešilo omezení předchozích transportních přístupů tím, že poskytlo standardizovaný mechanismus, který dokáže zvládnout různé požadavky QoS mobilních služeb. Vyřešila problém přenosu více souběžných služeb (hlasových hovorů, videohovorů a datových relací) od různých uživatelů přes stejné fyzické rozhraní mezi RNC a Node B. Definováním společné konvergenční vrstvy zajistilo 3GPP interoperabilitu mezi výrobci a umožnilo síťovým operátorům optimalizovat jejich transportní infrastrukturu pro specifické vzorce provozu charakteristické pro mobilní sítě, kde je třeba efektivně agregovat mnoho spojení s nízkým přenosovým tokem přes vysokokapacitní páteřní spoje.

## Klíčové vlastnosti

- Poskytuje společné transportní služby pro více entit SSCS přes AAL2
- Umožňuje statistické multiplexování více služeb s nízkým přenosovým tokem na jediném virtuálním spojovacím okruhu (VCC) ATM
- Implementuje číslování sekvence pro zachování pořadí paketů
- Obsahuje detekci chyb založenou na CRC v zápatí CPCS PDU
- Podporuje PDU proměnné délky s polem indikace délky
- Zpracovává výplň pro splnění požadavků SAR podsložky

## Související pojmy

- [AAL2 – ATM Adaptation Layer type 2](/mobilnisite/slovnik/aal2/)
- [ATM – Asynchronous Transfer Mode](/mobilnisite/slovnik/atm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling

---

📖 **Anglický originál a plná specifikace:** [CPCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpcs/)
