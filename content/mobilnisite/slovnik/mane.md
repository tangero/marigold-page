---
slug: "mane"
url: "/mobilnisite/slovnik/mane/"
type: "slovnik"
title: "MANE – Media Aware Network Element"
date: 2025-01-01
abbr: "MANE"
fullName: "Media Aware Network Element"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mane/"
summary: "Síťový prvek, který optimalizuje doručování multimédií tím, že je schopen rozpoznávat kódovaný mediální obsah a síťové podmínky. Umožňuje inteligentní adaptaci mediálních toků, například videa, pro zl"
---

MANE je síťový prvek, který optimalizuje doručování multimédií tím, že je schopen rozpoznávat kódovaná média a síťové podmínky, aby inteligentně přizpůsoboval datové toky za účelem zlepšení kvality uživatelského zážitku a efektivity sítě.

## Popis

Media Aware Network Element (MANE) je funkční entita v architektuře 3GPP navržená pro vylepšení doručování multimediálních služeb, zejména streamování videa. Funguje tak, že zkoumá a rozumí struktuře a sémantice kódovaných mediálních paketů, například těch používajících kodeky H.264/[AVC](/mobilnisite/slovnik/avc/) nebo H.265/[HEVC](/mobilnisite/slovnik/hevc/). Na rozdíl od tradičních síťových uzlů, které zacházejí se všemi datovými pakety stejně, může MANE parsovat hlavičky a metadata specifická pro média, což mu umožňuje činit inteligentní rozhodnutí o prioritizaci paketů, selektivním zahazování a adaptaci přenosové rychlosti na základě důležitosti jednotlivých snímků nebo síťových řezů. Tato schopnost hluboké kontroly paketů je klíčová pro správu šířky pásma a zajištění plynulého uživatelského zážitku, zvláště při přetížení nebo proměnlivých rádiových podmínkách.

Z architektonického hlediska lze MANE nasadit na různých místech sítě, například na okraji rádiové přístupové sítě (RAN) nebo uvnitř core sítě. Rozhraní s dalšími síťovými funkcemi, jako je Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) a Traffic Detection Function ([TDF](/mobilnisite/slovnik/tdf/)), aby uplatňoval řízení založené na politikách. MANE využívá Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) a jeho řídicí protokol [RTCP](/mobilnisite/slovnik/rtcp/) ke sledování síťových podmínek, jako je ztráta paketů, chvění (jitter) a dostupná šířka pásma. Na základě této zpětné vazby a své mediální povědomosti může provádět transkódování, změnu přenosové rychlosti nebo selektivní přeposílání paketů. Například může během přetížení upřednostnit I-snímky (intrakódované snímky nezbytné pro dekódování) před P- nebo B-snímky (prediktivní snímky), aby zabránil úplnému zamrznutí videa.

Klíčové komponenty MANE zahrnují mediální parser, engine politik, modul adaptace přenosové rychlosti a reportovací rozhraní. Mediální parser dekóduje syntaxi mediálního toku k identifikaci typů snímků, vrstev škálovatelnosti (ve škálovatelném kódování videa) a závislostních vztahů. Engine politik aplikuje pravidla definovaná operátorem pro správu kvality služeb (QoS) a kvality uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)). Adaptační modul provádí akce, jako je zahazování rozšiřujících vrstev ve vrstveném kódování nebo konverze mezi různými reprezentacemi přenosové rychlosti v [HTTP](/mobilnisite/slovnik/http/) Adaptive Streaming (HAS). Jeho role je klíčová pro umožnění efektivního využití síťových zdrojů při zachování přijatelné kvality médií, což je v souladu s širšími cíli 3GPP pro optimalizaci multimediálních služeb a podporu síťových řezů pro aplikace náročné na média.

## K čemu slouží

MANE byl zaveden k řešení výzev spojených s doručováním kvalitního videa a multimediálních služeb přes mobilní sítě, které jsou z podstaty omezené šířkou pásma a podléhají proměnlivým podmínkám. Před zavedením MANE sítě zacházely s video provozem jako s monolitním datovým tokem a uplatňovaly jednotné QoS politiky, které nedokázaly rozlišit mezi kritickými a nekritickými částmi video toku. To často vedlo k neefektivnímu využití šířky pásma a špatnému uživatelskému zážitku během síťového přetížení, jako je buffering nebo výrazné zhoršení kvality. Rozšíření služeb streamování videa, jako je mobilní TV, videokonference a obsah na vyžádání, vytvořilo naléhavou potřebu inteligentnější správy provozu.

Vytvoření MANE bylo motivováno snahou optimalizovat efektivitu sítě a zlepšit kvalitu uživatelského zážitku (QoE) pro koncové uživatele. Díky schopnosti rozpoznávat média může síť činit informovaná rozhodnutí, například selektivně zahazovat méně důležité video pakety během přetížení, čímž zachová základní vizuální kvalitu a zabrání úplnému zastavení přehrávání. Tento přístup je mnohem lepší než prosté zahazování paketů, které by mohlo poškodit celý datový tok. Dále MANE podporuje vývoj směrem k adaptivnímu streamování a síťovým řezům, což operátorům umožňuje nabízet diferencované služby se zaručeným výkonem pro prémiový obsah. Představuje posun od sítí fungujících jako "bitové potrubí" k infrastrukturám schopným rozpoznávat služby, což umožňuje monetizaci vylepšeného doručování multimédií.

## Klíčové vlastnosti

- Hluboká kontrola paketů kódovaných mediálních toků (např. H.264, H.265)
- Selektivní zahazování paketů na základě důležitosti snímků (I-, P-, B-snímky)
- Podpora Scalable Video Coding (SVC) a HTTP Adaptive Streaming (HAS)
- Integrace s řízením politik (PCRF) pro vynucování QoS
- Adaptace v reálném čase využívající zpětnovazební mechanismy RTP/RTCP
- Schopnosti transkódování a adaptace přenosové rychlosti

## Související pojmy

- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [MANE na 3GPP Explorer](https://3gpp-explorer.com/glossary/mane/)
