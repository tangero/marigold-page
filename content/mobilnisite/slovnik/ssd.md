---
slug: "ssd"
url: "/mobilnisite/slovnik/ssd/"
type: "slovnik"
title: "SSD – Source Statistics Descriptor"
date: 2025-01-01
abbr: "SSD"
fullName: "Source Statistics Descriptor"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ssd/"
summary: "Parametr v 5G QoS charakterizující provozní profil datového toku, například jeho překmit nebo pravidelnost. Pomáhá síti optimalizovat přidělování prostředků, plánování a řízení přístupu za účelem zvýš"
---

SSD je parametr QoS v 5G, který charakterizuje provozní profil datového toku, například jeho překmit (burstiness), aby pomohl síti optimalizovat přidělování prostředků, plánování a řízení přístupu.

## Popis

Source Statistics Descriptor (SSD) je parametr kvality služeb (QoS) zavedený ve specifikaci 3GPP Release 15 jako součást 5G systému (5GS). Používá se v rámci QoS profilu [PDU](/mobilnisite/slovnik/pdu/) (Protocol Data Unit) session nebo QoS toku k popisu statistických charakteristik zdroje provozu. Konkrétně SSD udává, zda je provoz generovaný zdrojem ve svém profilu spíše 'přerušovaný' (bursty) nebo 'pravidelný'. Tato informace umožňuje 5G síti – konkrétně rádiové přístupové síti (RAN) a funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) – činit inteligentnější rozhodnutí ohledně rezervace prostředků, plánování paketů a řízení přístupu.

SSD je definován sadou diskrétních hodnot, jako například 'speech' nebo 'unknown'. Hodnota 'speech' typicky implikuje předvídatelný, pravidelný provozní profil se známými charakteristikami, jako jsou období mluvení a ticha, jaké se vyskytují u služeb VoIP (Voice over IP). Hodnota 'unknown' značí, že provozní profil neodpovídá předdefinovanému statistickému modelu nebo není specifikován. SSD je přenášen prostřednictvím 5G QoS identifikátoru ([5QI](/mobilnisite/slovnik/5qi/)) a přidružených QoS parametrů ze základnové sítě (např. od funkce Policy Control Function, [PCF](/mobilnisite/slovnik/pcf/)) do RAN (gNB) během zřizování nebo modifikace QoS toku. gNB pak může tento deskriptor použít spolu s dalšími parametry, jako je Guaranteed Flow Bit Rate (GFBR) a Maximum Flow Bit Rate ([MFBR](/mobilnisite/slovnik/mfbr/)), k optimalizaci svého plánovače.

V provozu, když SSD udává hodnotu 'speech', může gNB aplikovat plánovací algoritmy, které berou v úvahu periodickou povahu a nízké požadavky na latenci hlasového provozu, což může umožnit efektivnější multiplexování uživatelů a snížení plýtvání prostředky ve srovnání s jeho zacházením jako s generickým nepředvídatelným provozem. To vede ke zlepšení spektrální účinnosti a celkové QoS pro aplikace citlivé na zpoždění. SSD je součástí rozšířeného QoS rámce 5G, navrženého pro podporu širokého spektra služeb od rozšířené mobilní širokopásmové komunikace (eMBB) až po ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)), a to umožněním detailnější charakterizace provozu.

## K čemu slouží

SSD byl v 5G zaveden, aby řešil omezení dřívějších QoS mechanismů, které se primárně spoléhaly na agregované parametry šířky pásma (jako Guaranteed Bit Rate) bez zohlednění časového rozložení provozu. V 4G LTE byla QoS do značné míry definována hodnotami [QCI](/mobilnisite/slovnik/qci/) (QoS Class Identifier), které udávaly prioritu, rozpočet zpoždění paketu a míru chybovosti paketů, ale explicitně nepopisovaly statistiku zdroje. To mohlo vést k neefektivnímu přidělování rádiových prostředků; například rezervace špičkové šířky pásma pro hlasový tok nepřetržitě, dokonce i během období ticha, plýtvá prostředky.

SSD to řeší tím, že poskytuje dodatečnou informaci o statistické povaze provozu, což umožňuje RAN efektivněji provádět 'statistický multiplex'. U služeb jako VoIP, kde je provoz vysoce předvídatelný se střídajícími se aktivními a tichými fázemi, umožňuje znalost SSD síti dynamicky přidělovat prostředky, přičemž plnou kapacitu přiřazuje pouze během období mluvení. Toto zlepšuje kapacitu a efektivitu sítě, což je klíčové pro cíle 5G podporovat masivní počty zařízení a rozmanité požadavky služeb. Umožňuje přesnější řízení přístupu a plánování, zajišťující optimální využití prostředků při současném splnění přísných cílů pro latenci a spolehlivost služeb, jako je hlas nebo průmyslový IoT.

## Klíčové vlastnosti

- Parametr QoS popisující statistické charakteristiky (např. překmit) zdroje provozu
- Definován hodnotami jako 'speech' pro předvídatelné profily nebo 'unknown' pro nespecifikovaný provoz
- Používá se gNB k optimalizaci plánování paketů a přidělování rádiových prostředků
- Umožňuje zisky ze statistického multiplexu díky dynamickému přiřazování prostředků na základě provozního profilu
- Přenášen jako součást QoS profilu z 5GC do RAN během zřizování QoS toku
- Zvyšuje efektivitu pro služby citlivé na zpoždění, jako je VoIP, snížením plýtvání prostředky během období ticha

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [GBR – Generic Binaural Renderer](/mobilnisite/slovnik/gbr/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping

---

📖 **Anglický originál a plná specifikace:** [SSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssd/)
