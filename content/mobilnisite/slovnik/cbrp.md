---
slug: "cbrp"
url: "/mobilnisite/slovnik/cbrp/"
type: "slovnik"
title: "CBRP – CBR Packet transmission"
date: 2025-01-01
abbr: "CBRP"
fullName: "CBR Packet transmission"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cbrp/"
summary: "CBR Packet transmission (přenos paketů s konstantním datovým tokem) je servisní funkce definovaná ve specifikaci 3GPP TS 26.937 pro službu Multimedia Broadcast/Multicast Service (MBMS). Umožňuje přeno"
---

CBRP je funkce služby Multimedia Broadcast/Multicast Service (MBMS) pro přenos mediálních paketů s konstantním datovým tokem (Constant Bit Rate) přes přenosové kanály MBMS, která zajišťuje předvídatelné doručování dat pro streamovací aplikace, jako je mobilní televize.

## Popis

[CBR](/mobilnisite/slovnik/cbr/) Packet transmission je specifický provozní režim v rámci architektury služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) definované 3GPP. Řídí způsob, jakým je mediální obsah s konstantním datovým tokem (CBR) paketizován a plánován pro přenos přes přenosové kanály MBMS. Architektura zahrnuje vrstvu MBMS Bearer Service, která využívá podkladové zdroje rádiového přístupu a jádra sítě k doručování dat z Broadcast Multicast-Service Centre ([BM-SC](/mobilnisite/slovnik/bm-sc/)) k více uživatelským zařízením (UE). Funkce CBRP je implementována v protokolech servisní vrstvy a zajišťuje, že charakteristika konstantního toku zdrojového média je zachována napříč přenosovou sítí.

Technicky CBRP funguje tak, že definuje pravidla pro tvorbu paketů a časování přenosu v souladu se zdrojovým CBR mediálním proudem. BM-SC nebo vyhrazená aplikační funkce generuje mediální pakety konstantní rychlostí. Tyto pakety jsou pak předány službě MBMS bearer service k doručení. Procesy plánování a kódování pro opravu chyb ([FEC](/mobilnisite/slovnik/fec/)) jsou konfigurovány tak, aby respektovaly tento konstantní tok, a zabraňovaly tak nárazům, které by na straně přijímače mohly způsobit podtečení nebo přetečení vyrovnávací paměti. Protokol zajišťuje, že interval příchodu paketů na UE přibližně odpovídá původnímu generačnímu intervalu, čímž udržuje plynulý zážitek ze streamovaných služeb.

Klíčové komponenty umožňující CBRP zahrnují službu MBMS Bearer Service s jejími přidruženými funkcemi plánování a aplikační protokoly specifikované pro doručování médií, jako jsou ty založené na sadě protokolů [FLUTE](/mobilnisite/slovnik/flute/)/[ALC](/mobilnisite/slovnik/alc/). BM-SC hraje centrální roli v přizpůsobení zdrojové rychlosti a označování paketů podle CBR profilu. V rádiové přístupové síti eNodeB (v LTE) nebo gNB (v NR) plánuje přenos těchto paketů na skupinovém kanálu pro přenos dat ([MTCH](/mobilnisite/slovnik/mtch/)) s ohledem na požadavek CBR a další omezení správy rádiových zdrojů.

Její úlohou v síti je poskytovat transportní mechanismus s garantovanou kvalitou pro vysílací/skupinový obsah v reálném čase nebo pro streamování. Zaručením předvídatelného a stabilního toku paketů CBRP podporuje aplikace, jako je živé vysílání audio/video, kde jsou důležité konzistentní datový tok a nízký jitter. Spolupracuje s mechanismy QoS, aby bylo zajištěno, že přenosovému kanálu MBMS jsou přiděleny dostatečné a stabilní zdroje pro udržení deklarovaného konstantního datového toku, a tvoří tak základní služební prvek pro hromadné šíření médií v celulárních sítích.

## K čemu slouží

[CBR](/mobilnisite/slovnik/cbr/) Packet transmission byl zaveden, aby řešil specifické požadavky streamovacích vysílacích a skupinových služeb v sítích 3GPP. Před jeho standardizací MBMS primárně podporovala služby doručování souborů (stahování) nebo streamování s proměnným datovým tokem (VBR), což mohlo vést k nekonzistentní kvalitě a problémům se správou vyrovnávací paměti přijímače. Potřeba spolehlivého, televiznímu zážitku podobného prostředí v mobilních sítích si vyžádala standardizovanou metodu pro zpracování mediálních toků s konstantní rychlostí, které jsou typické pro profesionálně kódovaný živý obsah.

Vznik CBRP byl motivován komerčním tlakem na služby Mobilní televize a živého vysílání událostí přes celulární sítě. Tyto služby vyžadují předvídatelnou šířku pásma a časování, aby všichni uživatelé přijímali synchronizovaný vysoce kvalitní stream bez zamrznutí nebo přeskočení. CBRP řeší problém efektivního mapování kontinuálního mediálního zdroje na paketově spínaný skupinový/vysílací přenosový kanál při zachování jeho časových charakteristik. Poskytuje smlouvu mezi servisní vrstvou a transportní vrstvou, což umožňuje rezervaci síťových zdrojů a optimální plánování na základě známého, konstantního datového toku.

Historicky vysílací služby, jako je Digital Video Broadcasting (DVB), používaly přenos s konstantní rychlostí. MBMS od 3GPP si kladlo za cíl nabídnout konkurenceschopnou alternativu založenou na celulárních sítích, což vyžadovalo analogické schopnosti. CBRP tuto mezeru zaplnil definováním způsobu adaptace těchto tradičních vysílacích paradigmat na IP-based, sdílený model zdrojů sítí 3G/4G/5G. Řeší omezení prostého best-effort doručování paketů zavedením profilu přenosu s ohledem na službu, čímž zajišťuje, že jsou inherentní vlastnosti média kódovaného v CBR zachovány end-to-end, což je klíčové pro přijetí služby masovým trhem.

## Klíčové vlastnosti

- Standardizovaná paketizace a plánování pro mediální toky s konstantním datovým tokem (CBR) přes MBMS
- Umožňuje předvídatelnou spotřebu šířky pásma a rezervaci zdrojů pro vysílací přenosové kanály
- Podporuje doručování s nízkým jitterem, které je nezbytné pro aplikace streamování v reálném čase, jako je mobilní televize
- Integruje se s mechanismy QoS pro MBMS, aby garantovala trvalé doručování deklarovaného datového toku
- Definuje procedury aplikační vrstvy kompatibilní s doručováním obsahu založeným na FLUTE/ALC
- Usnadňuje správu vyrovnávací paměti přijímače tím, že poskytuje stabilní, předvídatelný tok paketů

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)
- [MTCH – MBMS point-to-multipoint Traffic Channel](/mobilnisite/slovnik/mtch/)

## Definující specifikace

- **TR 26.937** (Rel-19) — 3GPP PSS Characterization

---

📖 **Anglický originál a plná specifikace:** [CBRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbrp/)
