---
slug: "plr"
url: "/mobilnisite/slovnik/plr/"
type: "slovnik"
title: "PLR – Packet Loss Ratio"
date: 2026-01-01
abbr: "PLR"
fullName: "Packet Loss Ratio"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/plr/"
summary: "Klíčový výkonnostní ukazatel, který měří podíl paketů ztracených při přenosu k celkovému počtu paketů odeslaných přes síťovou cestu během určitého časového intervalu. Je zásadní pro hodnocení kvality"
---

PLR je podíl paketů ztracených při přenosu k celkovému počtu paketů odeslaných přes síťovou cestu během určitého časového intervalu.

## Popis

Packet Loss Ratio (PLR) je kvantitativní ukazatel definovaný jako (Počet ztracených paketů) / (Počet odeslaných paketů), často vyjádřený v procentech nebo jako hodnota mezi 0 a 1. Ve specifikacích 3GPP se PLR používá jak jako klíčový výkonnostní ukazatel ([KPI](/mobilnisite/slovnik/kpi/)) pro monitorování sítě, tak jako parametr pro definování požadavků na kvalitu služeb (QoS). Měří se na různých vrstvách a rozhraních: end-to-end pro službu, přes konkrétní přenosový kanál (např. EPS bearer nebo QoS Flow) nebo přes konkrétní síťový spoj (např. rozhraní N3 v 5G). Ke ztrátám může docházet z důvodu zahlcení, chyb na rádiovém spoji, přetečení vyrovnávacích pamětí v síťových uzlech nebo selhání předávání spojení.

Z technického hlediska měření se PLR často počítá pomocí sekvenčních čísel v hlavičkách protokolu. Například v protokolu [RTP](/mobilnisite/slovnik/rtp/) používaném pro hlas a video může příjemce analyzovat sekvenční čísla přijímaných paketů, aby detekoval mezery a vypočítal ztrátu. V rádiové přístupové síti 3GPP mají nižší vrstvy, jako je Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) a Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)), vlastní mechanismy pro detekci a hlášení ztráty paketů. Vrstva PDCP, zodpovědná za kompresi hlaviček a ochranu integrity, udržuje sekvenční číslování pro uživatelská data. Čítače pro ztráty PDCP paketů jsou definovány pro měření výkonu ([PM](/mobilnisite/slovnik/pm/)) ve specifikacích jako TS 38.314 (NR) a jsou hlášeny do systému řízení. Tato měření pomáhají izolovat, zda ke ztrátám dochází na rádiovém spoji nebo v jádru sítě.

PLR je neoddělitelně spojen se správou QoS. V modelu QoS pro 5G definovaném v TS 23.501 se některé charakteristiky QoS Flow odkazují na míru ztráty paketů. Například QoS Flow s garantovaným přenosovým tokem (GFBR) pro službu Ultra-Reliable Low Latency Communication ([URLLC](/mobilnisite/slovnik/urllc/)) bude mít velmi přísnou maximální povolenou míru ztráty paketů (např. 10^-5 nebo 10^-6). Síť využívá řízení přístupu a plánování zdrojů, aby se pokusila tohoto cíle dosáhnout. Pro multimediální služby definuje 3GPP TS 26.114 výkonnostní cíle pro služby založené na IMS, kde je PLR kritickým parametrem pro hlas (VoLTE/VoNR) a videohovory. Transportní vrstva sítě ve spolupráci s technikami na aplikační vrstvě, jako je dopředná korekce chyb ([FEC](/mobilnisite/slovnik/fec/)) a opakované přenosy (např. RLC Acknowledged Mode pro data v reálném čase), pracuje na udržení PLR v přijatelných mezích pro každý typ služby.

## K čemu slouží

PLR existuje jako základní metrika, protože ztráta paketů přímo a výrazně degraduje uživatelský prožitek ([QoE](/mobilnisite/slovnik/qoe/)) u digitálních služeb, zejména těch interaktivních v reálném čase. U hlasu přes IP může i malá míra ztráty paketů (např. 1 %) způsobit slyšitelné klikání a přerušení, zatímco u streamování videa vede k zamrznutí snímků nebo blokovým artefaktům. Kvantifikace této ztráty je prvním krokem k jejímu řízení a zmírnění. Před standardizovanými QoS metrikami se výkon sítě hodnotil vágními pojmy; PLR poskytl objektivní, měřitelný cíl pro smlouvy o úrovni služeb (SLA) a optimalizaci sítě.

Motivace pro jeho přesnou definici v 3GPP vychází z přechodu na plně IP sítě od Release 5 a dále, kde tradiční hlas s přepojováním okruhů se zaručeným doručením byl nahrazen hlasem přes IP (VoIP) s přepojováním paketů. V paketových sítích je ztráta inherentní kvůli statistickému multiplexování a směrování typu best-effort. 3GPP potřebovalo definovat přijatelné prahové hodnoty ztráty pro konverzační služby, aby zajistilo, že zůstanou životaschopné přes bezdrátové IP sítě. To vedlo k zahrnutí PLR do charakteristik QoS Class Identifier (QCI) v EPS a 5QI charakteristik v 5G, což síti umožňuje zacházet s provozem různě podle jeho citlivosti na ztráty.

Historicky PLR řešil omezení spočívající v absenci standardizovaného způsobu korelace výkonu sítě s kvalitou vnímanou uživatelem. Umožňuje několik klíčových síťových funkcí: 1) Monitorování výkonu: Operátoři měří PLR k identifikaci zahlcených spojů nebo vadného zařízení. 2) Vynucování QoS: Rámec pro správu politik (PCRF/PCF) může použít měření PLR ke spuštění nápravných akcí. 3) Vývoj služeb: Vývojáři aplikací (např. pro videokonference) znají garantovanou PLR sítě a mohou podle toho navrhnout odpovídající odolnost proti chybám (jako je FEC). PLR tedy není jen měřením, ale základním kamenem celé architektury QoS v moderních mobilních sítích.

## Klíčové vlastnosti

- Kvantitativní metrika pro hodnocení spolehlivosti sítě
- Definována jako ztracené pakety děleno celkově odeslanými pakety
- Používá se v definicích QoS pro přenosové kanály (bearers) a QoS Flows
- Měřena na více protokolových vrstvách (RTP, PDCP, end-to-end)
- Kritický KPI pro výkon služeb v reálném čase (VoLTE, ViLTE)
- Spouští rozhodnutí o optimalizaci sítě a řízení přístupu

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS
- **TR 26.910** (Rel-19) — MTSI enhancements for RAN delay budget reporting
- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.936** (Rel-19) — Audio Codec Characterization Technical Report
- **TR 26.959** (Rel-19) — Enhanced VoLTE Performance Study
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation

---

📖 **Anglický originál a plná specifikace:** [PLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/plr/)
