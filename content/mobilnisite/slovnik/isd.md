---
slug: "isd"
url: "/mobilnisite/slovnik/isd/"
type: "slovnik"
title: "ISD – Initialization Segment Description"
date: 2025-01-01
abbr: "ISD"
fullName: "Initialization Segment Description"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/isd/"
summary: "Metadatová struktura používaná v multimediálním streamování, zejména pro Dynamic Adaptive Streaming over HTTP (DASH). Popisuje inicializační segment mediální prezentace, který obsahuje informace potře"
---

ISD je metadatová struktura v multimediálním streamování, která popisuje inicializační segment obsahující informace potřebné k zahájení dekódování mediálního datového proudu pro adaptivní přehrávání s proměnnou přenosovou rychlostí.

## Popis

Initialization Segment Description (ISD, popis inicializačního segmentu) je základní součástí rámce MPEG-DASH (Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/)), který je široce přijímán pro doručování multimédií v sítích 3GPP. Jedná se o XML metadatový prvek, který poskytuje podrobný popis inicializačního segmentu mediální prezentace. Samotný inicializační segment je klíčový blok dat obsahující základní konfigurační informace potřebné mediálním přehrávačem klienta pro správné dekódování a vykreslení následujících mediálních segmentů. To zahrnuje inicializační data kodeku, jako jsou záznamy konfigurace dekodéru (např. pro [AVC](/mobilnisite/slovnik/avc/)/H.264 nebo [HEVC](/mobilnisite/slovnik/hevc/)/H.265), časové informace a další parametry nezbytné pro vytvoření dekódovacího kontextu před zpracováním jakýchkoli mediálních dat.

Z architektonického hlediska je ISD součástí Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)), což je hlavní playlist nebo manifest soubor v [DASH](/mobilnisite/slovnik/dash/). MPD je XML dokument popisující strukturu mediální prezentace včetně dostupných přenosových rychlostí, rozlišení, kodeků a URL segmentů. V rámci tohoto MPD se pro každý adaptační soubor (adaptation set) nebo reprezentaci (representation) typicky nachází odkaz na inicializační segment. ISD poskytuje strukturovaný způsob, jak popsat vlastnosti a umístění (často prostřednictvím URL) tohoto inicializačního segmentu. To umožňuje DASH klientovi efektivně načíst a zpracovat inicializační data před vyžádáním mediálních segmentů, čímž zajišťuje plynulý a bezchybný začátek přehrávání.

Během provozu, když DASH klient zahájí streamování, nejprve stáhne a analyzuje MPD. Nalezne ISD pro vybranou reprezentaci (např. na základě dostupné šířky pásma a možností zařízení). Klient poté načte inicializační segment podle popisu v ISD. Tento segment je zpracován pro inicializaci audio a video dekodérů. Teprve po dokončení této inicializace začne klient stahovat mediální segmenty obsahující skutečné audio a video snímky. ISD tedy funguje jako klíčový most, který zajišťuje, že klient má veškeré potřebné nastavovací informace před konzumací kontinuálních mediálních dat. Jeho role je zásadní pro podporu adaptivního streamování, kde klienti mohou dynamicky přepínat mezi různými kvalitativními reprezentacemi; každé přepnutí může vyžadovat nový inicializační segment, pokud se liší parametry kodeku, a ISD pomáhá tyto přechody zvládnout bezproblémově.

Klíčové komponenty, na které se ISD odkazuje nebo které popisuje, zahrnují URL inicializačního segmentu, jeho rozsah bajtů ve větším souboru (je-li to aplikovatelné), jeho [MIME](/mobilnisite/slovnik/mime/) typ a případně jeho délku a informace o závislostech. V pokročilých scénářích, jako je ochrana obsahu pomocí Common Encryption ([CENC](/mobilnisite/slovnik/cenc/)), může ISD také nést informace o šifrovacích klíčích a inicializačních vektorech. Přesná specifikace ISD zajišťuje interoperabilitu mezi DASH servery a klienty od různých výrobců, což je nezbytné pro globální streamovací ekosystém. Jeho integrace do specifikací 3GPP, zejména těch souvisejících se službou Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a enhanced Multimedia Broadcast Multicast Service (eMBMS), podtrhuje jeho význam při umožnění efektivního broadcastového a unicastového doručování bohatých médií přes mobilní sítě.

## K čemu slouží

ISD byl vytvořen k řešení problému efektivní a spolehlivé inicializace přehrávání médií v adaptivních HTTP streamovacích systémech. Před standardizovaným adaptivním streamováním proprietární streamovací protokoly často vkládaly inicializační data přímo do mediálního datového proudu nebo používaly složitou signalizaci, což vedlo k problémům s interoperabilitou a pomalým startem. Přechod na streamování založené na HTTP, využívající standardní webovou infrastrukturu, vyžadoval jasné oddělení mezi popisnými metadaty (MPD) a mediálními daty. ISD toto oddělení poskytuje tím, že explicitně popisuje inicializační segment, který obsahuje všechny jednorázové nastavovací informace.

Motivace vychází z potřeby robustního, klientem řízeného modelu streamování s adaptivní přenosovou rychlostí (ABR). V ABR klient autonomně vybírá nejlepší kvalitativní segment na základě síťových podmínek. Různé kvalitativní reprezentace (např. 480p vs. 1080p) však mohou používat různé profily nebo úrovně kodeků, což vyžaduje odlišná inicializační data. Bez standardizovaného způsobu, jak tato inicializační data popsat a lokalizovat, by klienti zápasili s plynulým přepínáním reprezentací, což by způsobovalo chyby přehrávání nebo zpoždění. ISD jako součást standardu DASH přijatého 3GPP poskytuje tento standardizovaný popis, umožňuje bezproblémové přepínání kvality a zajišťuje, že přehrávání může začít rychle po načtení MPD.

Historicky dřívější streamovací metody jako Real-Time Streaming Protocol (RTSP) nebo proprietární adaptivní streamovací řešení postrádaly tuto úroveň explicitního, deklarativního popisu inicializace. ISD, zavedený spolu s DASH ve 3GPP Release 11, tyto nedostatky odstranil poskytnutím jednotného, XML založeného popisu, který je snadno analyzovatelný a ukládaný do mezipaměti. Podporuje škálovatelnost pro rozsáhlé sítě pro doručování obsahu (CDN) a je nezbytný pro služby jako mobilní TV, video na vyžádání a živé streamování přes sítě 4G a 5G. Oddělením inicializačních informací od mediálních segmentů také usnadňuje pokročilé funkce jako šifrování obsahu, trikové režimy (rychlé převíjení vpřed/pozpátku) a obsah s více obdobími (multi-period), což z něj činí základní kámen moderního doručování multimédií v telekomunikacích.

## Klíčové vlastnosti

- Poskytuje standardizovaný XML popis pro inicializační segment v rámci DASH Media Presentation Description (MPD)
- Umožňuje efektivní inicializaci dekodéru na straně klienta před zahájením přehrávání mediálních segmentů
- Podporuje bezproblémové přepínání adaptivní přenosové rychlosti popisem inicializačních dat pro každou reprezentaci
- Usnadňuje ochranu obsahu tím, že nese metadata související se šifrováním (např. pro Common Encryption)
- Umožňuje specifikaci URL inicializačního segmentu a jeho rozsahu bajtů pro flexibilní hostování obsahu
- Zajišťuje interoperabilitu mezi DASH servery a klienty různých výrobců a platforem

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [MPD – Media Presentation Description](/mobilnisite/slovnik/mpd/)
- [MPEG – Moving Pictures Experts Group](/mobilnisite/slovnik/mpeg/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TS 36.839** (Rel-11) — HetNet Mobility Improvements for LTE
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study
- **TS 36.878** (Rel-13) — LTE Performance Enhancements for High Speed Scenarios
- **TR 36.976** (Rel-19) — LTE-based 5G Terrestrial Broadcast Overview
- **TS 37.840** (Rel-12) — RF & EMC Requirements for Active Antenna Systems
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TS 38.817** — 3GPP TR 38.817
- **TR 38.833** (Rel-17) — NR Demodulation Performance Enhancement
- **TR 38.858** (Rel-18) — Technical Report on Evolution of NR Duplex Operation
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [ISD na 3GPP Explorer](https://3gpp-explorer.com/glossary/isd/)
