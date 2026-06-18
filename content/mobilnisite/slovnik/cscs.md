---
slug: "cscs"
url: "/mobilnisite/slovnik/cscs/"
type: "slovnik"
title: "CSCS – Common Supported Codec Set"
date: 2025-01-01
abbr: "CSCS"
fullName: "Common Supported Codec Set"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cscs/"
summary: "CSCS je standardizovaný seznam audio a video kodeků, které síťový operátor podporuje pro multimediální služby. Umožňuje efektivní vyjednávání kodeků mezi sítěmi a zařízeními, čímž zajišťuje interopera"
---

CSCS je standardizovaný seznam audio a video kodeků, které podporuje síťový operátor, aby umožnil efektivní vyjednávání kodeků a zajistil interoperabilitu pro multimediální služby, jako jsou hlasové a video hovory.

## Popis

Common Supported Codec Set (CSCS, společná sada podporovaných kodeků) je základním konceptem v sítích 3GPP pro správu interoperability multimediálních kodeků. Je definován jako standardizovaný, operátorsky specifický seznam audio a video kodeků, které síť podporuje pro služby jako Voice over LTE (VoLTE), Voice over NR (VoNR) a videotelefonie. CSCS není samostatnou entitou, ale konceptem implementovaným v síťových prvcích a postupech, který zajišťuje, že při navázání multimediální relace mohou jak počáteční a koncová síť, tak i uživatelské zařízení (UE) dohodnout společný kodek pro mediální stream.

Z architektonického hlediska je koncept CSCS integrován v jádrové síti IP Multimedia Subsystem (IMS). Mezi klíčové síťové prvky patří Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), který slouží jako první kontaktní bod pro UE, a Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)), který zajišťuje řízení relace. Informace o CSCS jsou typicky konfigurovány síťovým operátorem v těchto uzlech IMS. Během navazování relace, například pomocí požadavku [SIP](/mobilnisite/slovnik/sip/) INVITE, UE zahrne svůj seznam podporovaných kodeků v nabídce Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)). Síť (např. P-CSCF) pak může porovnat kodeky nabízené UE vůči své nakonfigurované CSCS. Na základě místní politiky může síť seznam kodeků v SDP přefiltrovat nebo změnit jejich pořadí před jeho přeposláním k cíli, čímž zajistí, že jsou vyjednávány pouze vzájemně podporované a operátorem schválené kodeky.

Hlavní úlohou CSCS je fungovat jako mechanismus prosazování politiky a interoperability. Zabrání vyjednání kodeků, které síť nepodporuje, nedokáže transkódovat nebo považuje z hlediska kvality nebo zdrojů za suboptimální. Například operátor může nakonfigurovat svou CSCS tak, aby upřednostňovala kodek [AMR-WB](/mobilnisite/slovnik/amr-wb/) (Adaptive Multi-Rate Wideband) pro hlas ve vysoké kvalitě, a zajistila tak, že je preferovanou volbou oproti úzkopásmovým alternativám, pokud je podporován oběma koncovými body. CSCS také hraje klíčovou roli v scénářích mezi operátory. Když hovor prochází více sítěmi, každá síť uplatňuje svou vlastní politiku CSCS. Výběr kodeku od konce ke konci se pak stává průnikem schopností počátečního UE, CSCS počáteční sítě, CSCS koncové sítě a schopností koncového UE.

Technicky je CSCS definován ve specifikaci 3GPP TS 28.062, která spadá pod specifikace Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)). Toto umístění zdůrazňuje, že konfigurace CSCS je činností správy. Specifikace poskytuje rámec a požadavky na to, jak je tato sada definována a spravována, což zajišťuje její konzistentní implementaci napříč zařízeními různých výrobců. Samotné vyjednávání kodeků probíhá dynamicky během výměny SIP/SDP, ale CSCS poskytuje statické politické zázemí, které toto vyjednávání řídí, čímž činí mediální relace předvídatelnými, efektivními a sladěnými s provozní strategií operátora.

## K čemu slouží

CSCS byl vytvořen, aby řešil základní výzvy interoperability a správy kvality v paketově přepínaných multimediálních službách, které se staly kritickými se zavedením IMS a LTE. Před standardizovanými plně-IP sítěmi používala přepojovaná hlasová služba omezenou, dobře definovanou sadu kodeků (jako [AMR](/mobilnisite/slovnik/amr/)). Přechod na IP-bázi multimédií v IMS přinesl širokou škálu možných audio a video kodeků od různých standardizačních organizací (3GPP, [ITU](/mobilnisite/slovnik/itu/), IETF). Bez řízeného přístupu mohly koncové body vyjednat kodeky, které síť neuměla podporovat, což vedlo k selhání hovorů, nebo suboptimální kodeky, které degradovaly uživatelský zážitek. Absence společné reference také komplikovala roamingové a propojovací dohody mezi operátory.

Jádrem problému, který CSCS řeší, je nesoulad mezi schopnostmi koncového bodu a schopnostmi sítě. UE může podporovat desítky kodeků, ale síťový operátor potřebuje zajistit kvalitu služeb, efektivně spravovat zdroje pro transkódování a udržovat konzistentní zážitek z vlastní značky. CSCS poskytuje operátorovi centralizovaný kontrolní bod politiky pro výběr kodeků. Zajišťuje, že síť souhlasí pouze s mediálními relacemi používajícími kodeky, které je připravena zpracovat, ať už nativně nebo prostřednictvím dostupných mediálních bran. Tím se zabrání scénářům, kdy je hovor navázán s kodekem, který síť nedokáže zpracovat, což by vedlo k jednosměrnému audiu nebo úplnému selhání média.

Dále CSCS umožňuje strategickou diferenciaci služeb. Definováním preferovaného pořadí kodeků v rámci sady mohou operátoři směrovat relace k vyšší kvalitě kodeků, jako je EVS (Enhanced Voice Services) nebo AMR-WB, a tím podporovat hlas ve vysoké kvalitě jako tržní vlastnost. Také zajišťuje budoucí kompatibilitu sítě; když jsou vyvíjeny nové, efektivnější kodeky jako EVS, mohou je operátoři přidat do své CSCS a postupně vyřazovat starší, čímž řídí přechod kontrolovaným způsobem. CSCS v podstatě mění vyjednávání kodeků z nekontrolovaného procesu řízeného koncovými body na síťově řízenou politiku, což je nezbytné pro spolehlivé, kvalitní komerční multimediální služby.

## Klíčové vlastnosti

- Standardizovaná politika kodeků definovaná operátorem
- Umožňuje síťově řízené vyjednávání kodeků během navazování IMS relace
- Zajišťuje interoperabilitu mezi UE a síťovými mediálními zdroji
- Podporuje správu kvality služeb prostřednictvím upřednostňování kvalitních kodeků
- Usnadňuje roamingové a propojovací dohody mezi operátory
- Poskytuje rámec pro řízený vývoj a zavádění nových kodeků

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [SDP – Service Discovery Protocol](/mobilnisite/slovnik/sdp/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)

## Definující specifikace

- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [CSCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cscs/)
