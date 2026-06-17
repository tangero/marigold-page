---
slug: "cpb"
url: "/mobilnisite/slovnik/cpb/"
type: "slovnik"
title: "CPB – Coding Picture Buffer"
date: 2025-01-01
abbr: "CPB"
fullName: "Coding Picture Buffer"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cpb/"
summary: "Coding Picture Buffer (CPB) je model vyrovnávací paměti na straně dekodéru používaný ve video kodecích pro řízení časování a ukládání komprimovaných video dat během přenosu. Zajišťuje plynulé přehrává"
---

CPB je model vyrovnávací paměti na straně dekodéru ve video kodecích, který řídí časování a ukládání komprimovaných dat do vyrovnávací paměti, aby zajistil plynulé přehrávání kompenzací síťových zpoždění a kolísání přenosové rychlosti.

## Popis

Coding Picture Buffer (CPB) je konceptuální model vyrovnávací paměti definovaný ve standardech pro video kódování, jako jsou ty odkazované ve specifikacích 3GPP, například H.264/[AVC](/mobilnisite/slovnik/avc/) a H.265/[HEVC](/mobilnisite/slovnik/hevc/). Nachází se na straně video dekodéru a slouží k simulaci uložení a časování zakódovaných obrazových dat přijatých přes síť před jejich dekódováním a zobrazením. CPB funguje tak, že přijímá komprimované video datové toky, které mohou přicházet s proměnným zpožděním v důsledku síťových podmínek, a dočasně je ukládá, aby zajistil konstantní přísun dat pro dekodér. Tento mechanismus vyrovnávací paměti pomáhá vyhladit chvění (jitter) a variaci zpoždění paketů, které jsou běžné v bezdrátových a mobilních sítích, a tím umožňuje nepřerušované přehrávání.

Z architektonického hlediska je CPB součástí modelu Hypothetical Reference Decoder ([HRD](/mobilnisite/slovnik/hrd/)), který poskytuje standardizovaný rámec pro ověřování konformace datového toku a zajištění interoperability mezi kodéry a dekodéry. Mezi klíčové komponenty patří velikost CPB, která definuje maximální kapacitu vyrovnávací paměti v bitech, a čas vyjmutí snímků, který určuje, kdy jsou uložená data extrahována pro dekódování na základě časových informací vložených v datovém toku. Činnost CPB je řízena parametry, jako je počáteční zpoždění vyjmutí z CPB a přenosová rychlost, které jsou signalizovány ve video datovém toku pro synchronizaci chování kodéru a dekodéru. To zajišťuje, že dekodér může správně interpretovat časování snímků a předcházet podtečení vyrovnávací paměti (kdy se vyrovnávací paměť vyprázdní, což způsobí zastavení přehrávání) nebo jejímu přetečení (kdy jsou data ztracena kvůli nedostatečné kapacitě).

V systémech 3GPP je CPB nedílnou součástí multimediálních služeb, jako je streamování a videotelefonie, jak je specifikováno v technických specifikacích, například 26.119 a 26.140. Interaguje se síťovými protokoly a mechanismy kvality služeb (QoS), aby se přizpůsobil dynamickým síťovým podmínkám, jako jsou ty v sítích LTE a 5G. Například při přechodech mezi buňkami nebo při zahlcení pomáhá CPB udržovat kontinuitu videa tím, že předem ukládá do vyrovnávací paměti další data. Jeho role sahá až k umožnění funkcí, jako je adaptivní streamování s proměnnou přenosovou rychlostí, kde kodér upravuje kvalitu videa na základě stavu CPB a síťové zpětné vazby, čímž optimalizuje využití prostředků a uživatelský zážitek. Poskytnutím předvídatelného modelu vyrovnávací paměti CPB usnadňuje efektivní doručování videa přes nespolehlivé kanály, což z něj činí základní kámen spolehlivých multimediálních aplikací v mobilním prostředí.

## K čemu slouží

Coding Picture Buffer (CPB) byl zaveden, aby řešil výzvy při přenosu videa přes paketově spínané sítě, zejména v mobilních systémech, kde jsou běžné proměnlivá latence a kolísání šířky pásma. Před jeho standardizací často trpělo video streamování problémy s přehráváním, jako je zamrzávání nebo přeskakování, kvůli nekonzistentním časům příchodu dat, protože rané kodeky postrádaly robustní mechanismy správy vyrovnávací paměti. CPB tento problém řeší tím, že poskytuje standardizovaný model vyrovnávací paměti, který zajišťuje, že dekodéry dokážou zvládnout variace způsobené sítí, čímž zlepšuje spolehlivost videa a kvalitu uživatelského zážitku (QoS).

Historicky, jak se 3GPP vyvíjelo od Rel-11 dále, rostla poptávka po vysoce kvalitních video službách přes sítě LTE a později 5G, což si vyžádalo sofistikovanější nástroje pro video kódování. Zavedení CPB bylo motivováno potřebou podporovat pokročilé kodeky jako H.265/[HEVC](/mobilnisite/slovnik/hevc/) a později Versatile Video Coding (VVC), které nabízejí vyšší kompresi, ale vyžadují přesné řízení časování. Definováním parametrů CPB ve specifikacích, jako jsou 26.346 a 26.906, umožnilo 3GPP interoperabilní doručování videa napříč různými zařízeními a sítěmi, čímž řešilo omezení ad-hoc přístupů k vyrovnávací paměti, které vedly k problémům s kompatibilitou a suboptimálním výkonem.

CPB dále usnadňuje efektivní využití síťových prostředků tím, že umožňuje dynamickou adaptaci na měnící se podmínky. V mobilním prostředí, kde jsou rádiové prostředky vzácné a sdílené, pomáhá CPB předcházet nadměrnému naplnění nebo vyprázdnění vyrovnávací paměti, optimalizuje propustnost a snižuje ztrátu paketů. To je obzvláště důležité pro služby v reálném čase, jako je videokonferencing a živé streamování, kde jsou nízká latence a plynulé přehrávání kritické. Standardizací CPB zajistilo 3GPP, že video aplikace mohou využívat vylepšení sítě, jako jsou identifikátory třídy QoS a správa přenosových cest, což v konečném důsledku podpořilo rozšíření multimediálních služeb v moderní telekomunikaci.

## Klíčové vlastnosti

- Standardizovaný model vyrovnávací paměti pro řízení časování video dekodéru
- Nedílná součást Hypothetical Reference Decoder (HRD) pro testování konformace
- Podporuje kompenzaci proměnné přenosové rychlosti a síťového zpoždění pro prevenci problémů s přehráváním
- Umožňuje adaptivní streamování s proměnnou přenosovou rychlostí interakcí s řízením rychlosti kodéru
- Definuje parametry jako velikost CPB a zpoždění vyjmutí pro zajištění interoperability
- Usnadňuje plynulé doručování videa v mobilních sítích s chvěním (jitter) a ztrátou paketů

## Definující specifikace

- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [CPB na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpb/)
