---
slug: "mtp1"
url: "/mobilnisite/slovnik/mtp1/"
type: "slovnik"
title: "MTP1 – Message Transfer Part layer 1"
date: 2025-01-01
abbr: "MTP1"
fullName: "Message Transfer Part layer 1"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mtp1/"
summary: "MTP1 je fyzická vrstva signalizačního protokolového zásobníku SS7, odpovědná za elektrický a fyzický přenos signalizačních zpráv po digitálním spoji. Definuje fyzické rozhraní, linkové kódování a sync"
---

MTP1 je fyzická vrstva signalizačního protokolového zásobníku SS7, odpovědná za elektrický a fyzický přenos signalizačních zpráv po digitálním spoji.

## Popis

Message Transfer Part layer 1 (MTP1) tvoří nejnižší vrstvu protokolové sady [SS7](/mobilnisite/slovnik/ss7/), jak je standardizována [ITU-T](/mobilnisite/slovnik/itu-t/) a přijata ve specifikacích 3GPP pro signalizaci v legacy okruhově přepínaných jádrových sítích. Odpovídá fyzické vrstvě (vrstvě 1) modelu [OSI](/mobilnisite/slovnik/osi/). MTP1 je odpovědná za fyzikální a elektrické charakteristiky signalizačního datového spoje. Definuje hardwarové rozhraní, přenosové médium (typicky digitální časový úsek E1/T1 o rychlosti 64 kbit/s nebo rozhraní V.35), linkové kódování (např. HDB3 pro E1) a bitovou synchronizaci (synchronizaci taktovacího kmitočtu). Jejím hlavním úkolem je přenášet surový, nestrukturovaný bitový tok přes fyzické spojení mezi dvěma signalizačními body, jako je spojení mezi [MSC](/mobilnisite/slovnik/msc/) a MSC nebo mezi MSC a [HLR](/mobilnisite/slovnik/hlr/).

Z architektonického hlediska poskytuje MTP1 službu vrstvě [MTP2](/mobilnisite/slovnik/mtp2/) ([MTP](/mobilnisite/slovnik/mtp/) Layer 2) tím, že nabízí transparentní digitální kanál. Nevykonává žádnou detekci chyb, jejich opravu ani rámování; to jsou úkoly MTP2. Tato vrstva je implementována v hardwaru, často jako součást vyhrazeného signalizačního terminálu nebo kanálu v rámci [PCM](/mobilnisite/slovnik/pcm/) multiplexoru. V typickém rámci E1 o rychlosti 2,048 Mbit/s je pro signalizační spoj SS7 vyhrazen konkrétní časový úsek (např. úsek 16) a MTP1 zajišťuje vysílání a příjem bitů v tomto přiděleném kanálu.

Její role v síti je naprosto zásadní. Integrita a dostupnost fyzického spoje přímo určují spolehlivost celé signalizační sítě. Zatímco vyšší vrstvy řídí složité směrování a aplikační logiku, MTP1 zajišťuje existenci základní konektivity. Poruchy na této vrstvě, jako je přerušení kabelu nebo ztráta synchronizace, spouštějí okamžité alarmy a způsobí, že je příslušný signalizační spoj označen jako nedostupný, což nutí MTP3 přesměrovat signalizační provoz na alternativní cesty. V systémech 3GPP je MTP1 zmiňována v souvislosti s podporou legacy signalizace MAP, CAP a BSSAP přes tradiční rozhraní založená na TDM, zejména v raných vydáních GSM a UMTS před rozšířeným nasazením IP alternativ typu SIGTRAN.

## K čemu slouží

MTP1 existuje za účelem poskytnutí základní fyzické konektivity pro signalizaci mimo přenosový pásmo v telekomunikačních sítích, konkrétně v rámci architektury SS7. Před zavedením SS7 byla signalizace často v přenosovém pásmu (používala stejný kanál jako hovor), což bylo neefektivní, pomalé pro sestavování hovorů a mělo omezené možnosti. Vytvoření samostatné, vyhrazené signalizační sítě si vyžádalo standardizovanou fyzickou vrstvu, aby byla zajištěna interoperabilita mezi zařízeními od různých výrobců. MTP1 řeší problém fyzického propojení signalizačních bodů (uzlů sítě) spolehlivým a standardizovaným způsobem.

Historický kontext je zakořeněn v digitalizaci telefonních sítí v 70. a 80. letech 20. století. ITU-T definovala protokolový zásobník SS7 pro umožnění pokročilých telefonních služeb, jako je bezplatné volání, přesměrování hovorů a roaming. MTP1 byla nezbytná pro specifikaci 'drátu', po kterém by tyto signalizační zprávy putovaly. Řešila omezení spočívající v neexistenci společného fyzického rozhraní pro signalizační zařízení, a zajišťovala tak, že ústředna od jednoho výrobce se mohla připojit k databázi od jiného výrobce pomocí standardního spoje E1 nebo T1.

Její účel zasahuje i do oblasti 3GPP, protože rané jádrové sítě 2G GSM a 3G UMTS byly pro veškerou signalizaci nesouvisející s rádiovým rozhraním (správa mobility, řízení hovorů, SMS) silně závislé na SS7. Specifikace 3GPP začlenily MTP1, aby zaručily, že jádrové síťové prvky (MSC, HLR, VLR atd.) mohou být vzájemně propojeny pomocí globálně nasazené a prověřené signalizační infrastruktury SS7, což poskytlo stabilní základ pro počáteční zavádění mobilních sítí před přechodem na IP.

## Klíčové vlastnosti

- Definuje fyzické přenosové médium (např. časový úsek E1/T1 o rychlosti 64 kbit/s)
- Specifikuje elektrické charakteristiky a konektorová rozhraní
- Implementuje schémata linkového kódování, jako je HDB3 pro E1 nebo B8ZS pro T1
- Poskytuje bitovou synchronizaci a obnovu synchronizace taktovacího kmitočtu
- Nabízí službu transparentního bitového toku pro vyšší vrstvu (MTP2)
- Spouští indikace poruchy fyzického spoje pro vyšší vrstvy správy sítě

## Související pojmy

- [MTP2 – Message Transfer Part layer 2](/mobilnisite/slovnik/mtp2/)
- [MTP3 – Message Transfer Part layer 3](/mobilnisite/slovnik/mtp3/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)

## Definující specifikace

- **TS 29.202** (Rel-19) — SS7 Signalling Transport Protocol Architectures
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [MTP1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtp1/)
