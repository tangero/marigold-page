---
slug: "dsm-cc"
url: "/mobilnisite/slovnik/dsm-cc/"
type: "slovnik"
title: "DSM-CC – Digital Storage Media – Command and Control"
date: 2025-01-01
abbr: "DSM-CC"
fullName: "Digital Storage Media – Command and Control"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dsm-cc/"
summary: "DSM-CC je sada protokolů standardizovaná organizací 3GPP pro řízení a správu přenosu multimediálního obsahu po sítích. Umožňuje interaktivní služby, video na vyžádání a datové vysílání tím, že poskytu"
---

DSM-CC je sada protokolů standardizovaná organizací 3GPP pro řízení a správu přenosu multimediálního obsahu po sítích, která umožňuje interaktivní služby a vysílání prostřednictvím správy relací a signalizace.

## Popis

Digital Storage Media – Command and Control (DSM-CC) je komplexní sada protokolů původně definovaná standardy [MPEG](/mobilnisite/slovnik/mpeg/) a převzatá organizací 3GPP pro poskytování multimediálních služeb. Funguje jako aplikační rámec, který usnadňuje správu multimediálních relací, streamování obsahu a interaktivní služby v telekomunikačních sítích. Architektura je rozdělena do několika funkčních oblastí, včetně rozhraní User-to-User (U-U), User-to-Network (U-N) a Network-to-Network (N-N), přičemž každé z nich řeší specifické signalizační a řídicí úlohy. Mezi klíčové komponenty patří protokol DSM-CC User-Network pro navazování relací a rezervaci zdrojů, protokol DSM-CC Download pro spolehlivé doručování datových karuselů a souborů a DSM-CC Object Carousel pro vysílání datových objektů více klientům. V kontextu 3GPP je primárně specifikován v dokumentu TS 26.953 pro multimediální vysílací/multicastové služby ([MBMS](/mobilnisite/slovnik/mbms/)) a další streamovací aplikace.

DSM-CC funguje tak, že mezi klientem (např. uživatelským zařízením, UE) a síťovým serverem vytváří řídicí kanál, což umožňuje vyjednávání parametrů relace, přidělování šířky pásma a popis obsahu. Pro interaktivní služby podporuje příkazy jako přehrát, pozastavit a přejít, což umožňuje funkce videa na vyžádání (VoD). Ve vysílacích scénářích spravuje karuselový přenos datových modulů a zajišťuje, že klienti mohou k souborům nebo streamům přistupovat kdykoli díky opakovanému cyklování obsahu. Zásobník protokolů typicky běží nad IP nebo [MPEG-2](/mobilnisite/slovnik/mpeg-2/) transportními proudy a integruje se s dalšími prvky 3GPP, jako je [BM-SC](/mobilnisite/slovnik/bm-sc/) (Broadcast Multicast Service Centre) pro doručování MBMS. Jeho úlohou je abstrahovat složitost řízení médií a poskytnout standardizovaný způsob, jak mohou aplikace vyžadovat a spravovat multimediální zdroje napříč heterogenními sítěmi.

Robustnost této technologie vychází z podpory jak spojově orientovaných, tak nespojových operací, což vyhovuje modelům doručování v reálném čase (streamování) i stahování. Zahrnuje mechanismy pro synchronizaci, obnovu po chybě a správu zdrojů, čímž zajišťuje kvalitu služeb (QoS) pro koncové uživatele. V systémech 3GPP se DSM-CC často používá spolu s protokoly jako [FLUTE](/mobilnisite/slovnik/flute/) (File Delivery over Unidirectional Transport) a RTP (Real-time Transport Protocol) k vytváření kompletních platforem pro multimediální služby. Jeho přijetí umožňuje operátorům zavádět pokročilé služby, jako je mobilní TV, softwarové aktualizace přes vysílání a interaktivní reklama, což z něj činí základní kámen multimediálně bohatých aplikací ve vyvíjejících se sítích, jako jsou LTE a 5G.

## K čemu slouží

DSM-CC byl vytvořen, aby řešil potřebu standardizovaného řízení a správy služeb digitálních médií napříč různými přenosovými sítěmi, včetně vysílacích, kabelových a mobilních systémů. Před jeho přijetím dominovaly v poskytování multimediálních služeb proprietární řešení, což vedlo k problémům s interoperabilitou, omezené škálovatelnosti a vysokým nákladům pro poskytovatele služeb. Tato sada protokolů poskytuje jednotný rámec, který umožňuje interaktivní služby a služby na vyžádání, a řeší problémy související s řízením relací, přidělováním zdrojů a distribucí obsahu v síťovém prostředí.

V historickém kontextu 3GPP byl DSM-CC představen ve verzi Release 13 pro vylepšení multimediálních schopností, zejména pro [MBMS](/mobilnisite/slovnik/mbms/) a pokročilé vysílací služby. Zaplnil mezeru tím, že nabídl dobře definovaný mechanismus příkazů a řízení, který se integruje s existujícími architekturami 3GPP a umožňuje operátorům využívat standardy založené na [MPEG](/mobilnisite/slovnik/mpeg/) pro efektivní doručování médií. Motivací byl rostoucí poptávka po video a datových službách na mobilních zařízeních, která vyžadovala spolehlivé, škálovatelné a interaktivní řídicí protokoly schopné pracovat přes IP a vysílací kanály.

Standardizací DSM-CC chtěla organizace 3GPP usnadnit nasazení služeb, jako je mobilní TV, streamování videa a stahování souborů, bez nutnosti znovuvynalézat řídicí protokoly. Řeší omezení dřívějších ad-hoc přístupů tím, že poskytuje zpracování chyb, synchronizaci a kompatibilitu s dalšími standardy [IETF](/mobilnisite/slovnik/ietf/) a MPEG. To zajišťuje, že sítě mohou podporovat širokou škálu multimediálních aplikací při zachování výkonu a uživatelského zážitku, a tím nakonec podporuje konvergenci vysílacích a telekomunikačních služeb.

## Klíčové vlastnosti

- Podporuje signalizaci User-to-Network (U-N) pro navazování relací a řízení zdrojů
- Umožňuje interaktivní příkazy (např. přehrát, pozastavit, přejít) pro služby videa na vyžádání
- Poskytuje protokoly Download a Object Carousel pro spolehlivé vysílání souborů a dat
- Integruje se s MPEG-2 transportními proudy a IP sítěmi pro flexibilní doručování
- Obsahuje mechanismy pro obnovu po chybě a synchronizaci pro robustní přehrávání médií
- Usnadňuje správu multimediálních služeb v systémech MBMS a dalších vysílacích systémech 3GPP

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)
- [MPEG-2 – Moving Picture Experts Group Transport Stream](/mobilnisite/slovnik/mpeg-2/)

## Definující specifikace

- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [DSM-CC na 3GPP Explorer](https://3gpp-explorer.com/glossary/dsm-cc/)
