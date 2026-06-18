---
slug: "aal"
url: "/mobilnisite/slovnik/aal/"
type: "slovnik"
title: "AAL – ATM Adaptation Layer"
date: 2025-01-01
abbr: "AAL"
fullName: "ATM Adaptation Layer"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aal/"
summary: "AAL je protokolová vrstva v zásobníku protokolů ATM, která adaptuje protokoly vyšších vrstev na podkladovou vrstvu ATM. Segmentuje data do ATM buněk a znovu je skládá, přičemž poskytuje různé třídy sl"
---

AAL (ATM Adaptation Layer) je adaptační vrstva ATM, protokol, který adaptuje data z vyšších vrstev pro přenos přes ATM tím, že je segmentuje do buněk a znovu je skládá, přičemž poskytuje třídy služeb pro provoz jako je hlas a video.

## Popis

Adaptační vrstva [ATM](/mobilnisite/slovnik/atm/) (AAL) je klíčovou součástí architektury protokolu Asynchronous Transfer Mode (ATM), definovanou v řadě [ITU-T](/mobilnisite/slovnik/itu-t/) I.363 a hojně odkazovanou ve specifikacích 3GPP pro rané verze UMTS. AAL se nachází mezi vrstvou ATM a protokoly vyšších vrstev a poskytuje potřebné adaptační funkce, aby různé typy provozu byly kompatibilní s pevnou strukturou 53bajtové ATM buňky. Jejím hlavním úkolem je překlenout propast mezi spojově orientovanou, buňkově přepínanou povahou ATM a požadavky různých služeb vyšších vrstev, které mohou mít odlišné charakteristiky, jako je proměnná velikost paketů, časové požadavky a tolerance k chybám.

AAL funguje prostřednictvím podsložek segmentace a opětovného složení ([SAR](/mobilnisite/slovnik/sar/)), které rozkládají datové jednotky protokolů ([PDU](/mobilnisite/slovnik/pdu/)) vyšších vrstev na 48bajtové segmenty užitečného zatížení vhodné pro ATM buňky, přičemž přidávají potřebné hlavičky a zápatí pro rekonstrukci na přijímací straně. Vrstva je rozdělena na dvě hlavní podsložky: Konvergenční podsložka ([CS](/mobilnisite/slovnik/cs/)) a Podsložka segmentace a opětovného složení (SAR). CS zajišťuje funkce specifické pro služby, jako je obnova hodin, kompenzace kolísání zpoždění buněk a zpracování ztracených nebo chybně vložených buněk, zatímco SAR provádí vlastní segmentaci dat do užitečného zatížení buněk a jejich opětovné složení v cíli.

V sítích 3GPP, zejména v UMTS [R99](/mobilnisite/slovnik/r99/) až raných verzích LTE, byla AAL hojně využívána na rozhraních Iub, Iur a Iu pro přenos uživatelských dat a řídicí signalizace mezi síťovými prvky, jako je Node B, [RNC](/mobilnisite/slovnik/rnc/) a uzly jádra sítě. Pro různé požadavky na provoz byly specifikovány různé typy AAL: [AAL2](/mobilnisite/slovnik/aal2/) byla optimalizována pro provoz citlivý na zpoždění s proměnnou přenosovou rychlostí, jako je hlas a video v reálném čase, a poskytovala multiplexování více spojení do jediného virtuálního okruhu ATM. AAL5 byla naopak navržena pro spojově orientovaný a nespojový datový provoz a nabízela efektivní přenos pro přerušovaná data s nižší režií ve srovnání s AAL2.

Implementace AAL v sítích 3GPP zahrnovala specifické adaptace pro různá rozhraní. Například na rozhraní Iub mezi Node B a RNC se běžně používala AAL2 pro provoz v uživatelské rovině (kanály DCH), zatímco AAL5 zpracovávala signalizaci v řídicí rovině (NBAP). Specifikace 3GPP definovaly přesná mapování mezi přenosovými rádiovými kanály a spojeními AAL, přičemž parametry kvality služby byly převáděny mezi rádiovou a přenosovou doménou. To umožnilo sítím UMTS využít možnosti QoS ATM při současném podporování různorodých požadavků mobilních služeb.

S vývojem sítí 3GPP role AAL slábla s přechodem na plně IP architektury v pozdějších verzích. Během své doby nasazení však AAL poskytovala robustní mechanismus pro adaptaci provozu, který umožnil raným sítím 3G poskytovat integrované hlasové, video a datové služby přes jednotnou přenosovou infrastrukturu. Podrobné specifikace v dokumentech jako 25.414 a 29.414 zajišťovaly interoperabilitu mezi zařízeními různých výrobců a tvořily základ spolehlivého mobilního přenosu v raných nasazeních 3G.

## K čemu slouží

AAL byla vytvořena, aby vyřešila základní nesoulad mezi pevnou strukturou 53bajtové buňky sítí ATM a proměnlivou délkou paketů generovaných protokoly a aplikacemi vyšších vrstev. Před adaptačními vrstvami ATM vyžadoval přenos různorodého provozu přes buňkové sítě složitá, pro aplikaci specifická řešení, která byla neefektivní a nestandardizovaná. AAL poskytla standardizovaný přístup, který umožnil sítím ATM podporovat více tříd služeb s různými požadavky na kvalitu služeb, čímž se ATM stala vhodnou pro integrované digitální sítě (ISDN) a později pro mobilní sítě 3G.

Historický kontext důležitosti AAL v 3GPP vychází z výběru ATM jako primární přenosové technologie pro rané sítě UMTS (R99 až Rel-7). ATM nabízela deterministickou kvalitu služeb, možnosti správy provozu a prověřenou spolehlivost, což ji činilo ideální pro přenos smíšeného provozu v mobilních přenosových sítích. Protokoly rádiové přístupové sítě, jako je FP (Frame Protocol), a řídicí signalizační protokoly však vytvářely pakety různé velikosti a s různými časovými požadavky, které nebylo možné přímo mapovat na ATM buňky. AAL poskytla potřebnou adaptační vrstvu, aby bylo toto mapování efektivní a standardizované napříč zařízeními různých výrobců.

Předchozí přístupy k přenosu smíšeného provozu přes telekomunikační sítě typicky zahrnovaly oddělené sítě pro různé typy služeb (okruhově přepínané pro hlas, paketově přepínané pro data) nebo neefektivní adaptace, které plýtvaly šířkou pásma. AAL tyto limity řešila poskytnutím více typů adaptací optimalizovaných pro různé charakteristiky provozu: AAL1 pro služby s konstantní přenosovou rychlostí, AAL2 pro služby v reálném čase s proměnnou přenosovou rychlostí, AAL3/4 pro spojově orientovaná a nespojová data a AAL5 pro efektivní přenos dat. To umožnilo sítím 3GPP konsolidovat více typů provozu přes jedinou infrastrukturu ATM při zachování odpovídající kvality služeb pro každou třídu služeb.

## Klíčové vlastnosti

- Segmentace a opětovné složení paketů proměnné délky do pevně velkých ATM buněk
- Podpora více tříd služeb prostřednictvím různých typů AAL (AAL1, AAL2, AAL5)
- Mapování kvality služeb mezi protokoly vyšších vrstev a přenosem ATM
- Multiplexování více logických spojení přes jediné virtuální okruhy ATM
- Mechanismy detekce a zpracování chyb pro ztrátu a chybné vložení buněk
- Obnova hodin a časová synchronizace pro služby v reálném čase

## Související pojmy

- [ATM – Asynchronous Transfer Mode](/mobilnisite/slovnik/atm/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface
- **TS 25.432** (Rel-19) — Iub NBAP Signalling Transport Specification
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols
- **TS 29.415** (Rel-19) — Nb User Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [AAL na 3GPP Explorer](https://3gpp-explorer.com/glossary/aal/)
