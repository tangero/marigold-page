---
slug: "t-sgw"
url: "/mobilnisite/slovnik/t-sgw/"
type: "slovnik"
title: "T-SGW – Transport Signalling Gateway"
date: 2025-01-01
abbr: "T-SGW"
fullName: "Transport Signalling Gateway"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/t-sgw/"
summary: "Síťová funkce v architektuře 3GPP IMS, která provádí převod signalizačních protokolů, primárně mezi IP-based SIGTRAN (např. SCTP/IP) a legacy okruhově spínanou signalizací (např. SS7 přes TDM). Umožňu"
---

T-SGW je síťová funkce v architektuře IMS, která provádí převod signalizačních protokolů mezi IP-based SIGTRAN a legacy okruhově spínanou signalizací SS7, aby umožnila spolupráci mezi IP sítěmi a tradičními telefonními systémy.

## Popis

Transport Signalling Gateway (T-SGW) je klíčová funkce pro spolupráci v rámci IP Multimedia Subsystem (IMS) a širší architektury 3GPP. Jejím primárním úkolem je fungovat jako brána signalizační roviny na transportní vrstvě, usnadňující komunikaci mezi síťovými elementy používajícími různé podkladové transportní protokoly. Nejběžnější funkcí je převod mezi transportními protokoly založenými na IP, konkrétně Stream Control Transmission Protocol ([SCTP](/mobilnisite/slovnik/sctp/)) v rámci sady SIGTRAN definované [IETF](/mobilnisite/slovnik/ietf/), a tradičním transportem okruhově spínané signalizace, jako jsou úrovně 1-3 Message Transfer Part ([MTP](/mobilnisite/slovnik/mtp/)) zásobníku protokolů [SS7](/mobilnisite/slovnik/ss7/) přenášené přes Time-Division [Multiplexing](/mobilnisite/slovnik/multiplexing/) ([TDM](/mobilnisite/slovnik/tdm/)) linky typu E1/T1. T-SGW neinterpretuje vyšší aplikační protokoly (např. [ISUP](/mobilnisite/slovnik/isup/), [MAP](/mobilnisite/slovnik/map/), CAP, BICC), které jí procházejí; pouze adaptuje jejich transportní nosič.

Architektonicky se T-SGW nachází na hranici mezi paketově spínanou sítí IMS/jádra a legacy okruhově spínanou sítí (např. PSTN, legacy PLMN). Rozhraní má s entitami jako Media Gateway Control Function (MGCF) nebo IMS Application Server na IP straně a s SS7 Signalling Points (SPs) nebo Signalling Transfer Points (STPs) na TDM straně. Na IP straně používá adaptační vrstvy SIGTRAN jako M3UA (MTP3 User Adaptation) nebo M2UA (MTP2 User Adaptation) pro přenos SS7 signalizačních zpráv přes sítě SCTP/IP. Na TDM straně ukončuje fyzickou vrstvu MTP1 a zpracovává linkové procedury MTP2. T-SGW provádí kritické funkce jako správa signalizačních linek, oprava chyb, řazení do pořadí a řízení toku odpovídající každému transportu, čímž zajišťuje spolehlivé doručování signalizačních zpráv přes heterogenní síťovou hranici.

Při provozu, když dorazí signalizační zpráva ze sítě SS7, T-SGW extrahuje užitečná data MTP3, zapouzdří je do příslušné užitečné náplně adaptační vrstvy SIGTRAN a přepošle je přes SCTP asociaci k IP-based uzlu jako je MGCF. Opačný proces probíhá pro zprávy směřující z IP do SS7. To umožňuje IP-based řídicím funkcím komunikovat s legacy ústřednami (MSCs, SSPs), aniž by tyto legacy uzly potřebovaly přímou IP konektivitu. T-SGW je často nasazována společně s Media Gateway (MGW), která zajišťuje spolupráci na uživatelské rovině, a společně tak tvoří kompletní řešení brány pro integraci okruhově spínaných sítí. Její nasazení je klíčové pro postupnou migraci ze sítí založených na TDM na plně IP sítě.

## K čemu slouží

T-SGW byla zavedena, aby vyřešila základní výzvu migrace v telekomunikacích: jak integrovat nová, plně IP jádra sítí (jako IMS) s rozsáhlou instalovanou základnou legacy okruhově spínaných sítí, které používají signalizaci SS7 přes vyhrazené TDM linky. Bez transportní brány by IP-based síťové funkce nemohly komunikovat s tradičními ústřednami, což by znemožnilo postupný a nákladově efektivní přechod na IP. T-SGW poskytuje transparentní vrstvu pro převod transportu, což umožňuje operátorům nasazovat IP-based řídicí elementy při zachování investic do stávající SS7 infrastruktury.

Historicky byly sítě SS7 budovány na hierarchii vyhrazených 64 kbps časových slotů (TDM). Vzestup IP jako univerzálního transportu vyžadoval metodu pro přenos této kritické signalizační provozu přes sdílené IP sítě se stejnou spolehlivostí. Pracovní skupina IETF SIGTRAN vyvinula pro tento účel sadu protokolů (SCTP a adaptační vrstvy). 3GPP standardizovala T-SGW jako síťovou funkci, která tuto spolupráci implementuje, poprvé podrobně popsána ve Release 4 jako součást počáteční architektury IMS a softswitch. Řešila omezení spočívající v nutnosti upgradovat každou legacy ústřednu drahými IP rozhraními nebo udržovat paralelní TDM sítě neomezeně dlouho.

Dále T-SGW umožňuje konsolidaci a zjednodušení sítě. Díky přenosu (backhaul) SS7 linek z více vzdálených ústředen k centralizované T-SGW přes IP síť mohou operátoři snížit složitost a náklady svých signalizačních sítí. Také usnadňuje zavádění nových IP-based služeb, které potřebují komunikovat s legacy účastníky, jako je telefonie založená na IMS nebo dotazy na přenos čísla. V podstatě je T-SGW mostní technologií, která byla a v mnoha sítích stále je nepostradatelná pro vývoj směrem k jednotnému IP-centric jádru sítě.

## Klíčové vlastnosti

- Převod na transportní vrstvě mezi SCTP/IP a SS7 MTP
- Podpora adaptačních vrstev SIGTRAN (M3UA, M2UA)
- Transparentnost vůči vyšším signalizačním protokolům (ISUP, MAP atd.)
- Správa signalizačních linek a monitorování jejich stavu
- Poskytuje spolehlivý transport s řízením toku a řazením do pořadí
- Umožňuje centralizovaný přenos SS7 přes IP (backhaul) z distribuovaných ústředen

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [SCTP – Stream Control Transmission Protocol](/mobilnisite/slovnik/sctp/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [T-SGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-sgw/)
