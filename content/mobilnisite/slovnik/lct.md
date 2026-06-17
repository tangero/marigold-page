---
slug: "lct"
url: "/mobilnisite/slovnik/lct/"
type: "slovnik"
title: "LCT – Layered Coding Transport"
date: 2025-01-01
abbr: "LCT"
fullName: "Layered Coding Transport"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lct/"
summary: "Layered Coding Transport je mechanismus pro přenos médií podle 3GPP pro streamovací služby, který využívá vrstvené kódování videa (např. SVC) v kombinaci s přenosem souborů přes FLUTE/ALC. Umožňuje ef"
---

LCT je mechanismus pro přenos médií podle 3GPP pro streamování, který využívá vrstvené kódování videa a protokoly pro přenos souborů k umožnění efektivního adaptivního streamování a spolehlivé multicastové nebo broadcastové distribuce.

## Popis

Layered Coding Transport je standardizovaný mechanismus 3GPP pro přenos médií, zejména videa, přes broadcastové/multicastové a unicastové sítě. Je navržen pro práci s vrstvenými video kodeky, nejvýznamněji Scalable Video Coding (SVC), což je rozšíření standardu H.264/[AVC](/mobilnisite/slovnik/avc/). Základním principem LCT je přenášet různé vrstvy škálovatelného video datového toku jako samostatné logické kanály nebo přenosové relace. Základní vrstva, obsahující nezbytné video informace, je vysílána nezávisle na jedné nebo více zlepšujících vrstvách, které přidávají prostorové rozlišení (velikost), časové rozlišení (snímkovou frekvenci) nebo kvalitu (poměr signálu k šumu). Toto oddělení umožňuje přijímačům přihlásit se k odběru a dekódovat pouze ty vrstvy, které jsou schopny úspěšně přijmout a zpracovat, na základě faktorů jako dostupná rádiová šířka pásma, schopnosti zařízení a úroveň předplatného.

Z pohledu přenosu LCT typicky využívá protokol File Delivery over Unidirectional Transport ([FLUTE](/mobilnisite/slovnik/flute/)), který je sám postaven na sadě protokolů Asynchronous Layered Coding ([ALC](/mobilnisite/slovnik/alc/)). FLUTE/ALC zajišťuje spolehlivý přenos souborů přes IP multicast. V LCT je každá video vrstva (základní nebo zlepšující) zabalena jako samostatná relace přenosu souborů FLUTE. Tyto relace jsou oznamovány prostřednictvím souboru Session Description Protocol (SDP) nebo Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) v kontextu Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)). Klientské zařízení přijme oznámení, identifikuje dostupné vrstvy a jim odpovídající přenosové relace (identifikované specifickými Transport Session Identifiers - TSI) a připojí se k multicastovým skupinám nebo naváže unicastová spojení potřebná k přijetí vybraných vrstev.

Architektura zahrnuje několik klíčových komponent: Broadcast Multicast Service Centre ([BM-SC](/mobilnisite/slovnik/bm-sc/)) v síti, který funguje jako zdroj a kontroler pro relace FLUTE; LTE/5G broadcastové entity jako eMBMS (evolved Multimedia Broadcast Multicast Service) nebo 5G [MBS](/mobilnisite/slovnik/mbs/) (Multicast Broadcast Service) pro distribuci; a klientské zařízení s mediálním přehrávačem a přijímačem FLUTE/ALC. Klient provádí logiku adaptivního streamování sledováním podmínek příjmu (např. míra ztráty paketů, síla signálu) a dynamickým přidáváním nebo odebíráním relací zlepšujících vrstev. Pokud je zlepšující vrstva ztracena kvůli špatnému příjmu, základní vrstva může být stále dekódována, což poskytuje nižší kvalitu, ale nepřerušený video zážitek – klíčovou vlastnost pro robustní mobilní broadcast. LCT je tedy hybridním přístupem, který kombinuje efektivnost multicastu pro rozsáhlou distribuci s flexibilitou adaptace řízené klientem.

## K čemu slouží

Layered Coding Transport byl vyvinut pro řešení výzev spojených s efektivním poskytováním služeb streamování videa vysoké kvality přes mobilní sítě, zejména v broadcastových/multicastových scénářích jako je mobilní TV. Tradiční unicastové streamování je pro oblíbené živé události neefektivní, protože duplikuje stejný datový tok každému uživateli, čímž spotřebovává nadměrné síťové zdroje. Broadcast/multicast (např. MBMS) řeší problém efektivity, ale tradičně dodával jediný datový tok s pevnou kvalitou, což bylo nevhodné pro různorodé a proměnlivé podmínky příjmu mobilních uživatelů.

LCT byl vytvořen ke kombinaci spektrální efektivity broadcastu s přizpůsobivostí unicastového streamování. Jeho primárním účelem je umožnit adaptivní streamování řízené kvalitou uživatelského zážitku (QoE) přes broadcastové kanály. Rozdělením videa na nezávislé vrstvy umožňuje jedinému broadcastovému přenosu obsloužit uživatele s různými schopnostmi zařízení (např. chytré telefony vs. tablety) a různými rádiovými podmínkami (např. na okraji buňky vs. v jejím středu). Uživatelé se špatnou kvalitou signálu mohou dekódovat pouze robustní základní vrstvu, zatímco uživatelé s výborným příjmem mohou přidat zlepšující vrstvy pro vysoké rozlišení. Tím se maximalizuje pokrytí služby a spokojenost uživatelů. Dále LCT usnadňuje členění služeb, kdy operátoři mohou nabízet základní (pouze základní vrstva) a prémiová (základní + zlepšující vrstvy) předplatná přes stejnou broadcastovou infrastrukturu. Byl to základní technologie pro služby založené na eMBMS a ovlivnil pozdější standardy adaptivního streamování jako DASH, kde se koncept vrstev vyvinul do reprezentací segmentovaných přes HTTP.

## Klíčové vlastnosti

- Využívá Scalable Video Coding (SVC) k vytvoření základní vrstvy a jedné či více zlepšujících vrstev
- Každou video vrstvu přenáší jako samostatnou relaci přenosu souborů FLUTE/ALC
- Umožňuje adaptivní streamování řízené klientem prostřednictvím selektivního připojování k relacím vrstev
- Poskytuje postupnou degradaci: ztráta zlepšujících vrstev nezpůsobí přerušení přehrávání základní vrstvy
- Efektivně podporuje broadcastovou/multicastovou distribuci prostřednictvím eMBMS/5G MBS
- Usnadňuje členění služeb a diferencovanou kvalitu uživatelského zážitku

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.852** (Rel-14) — MBMS user service profiles, APIs and transport enabler study
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TR 26.947** (Rel-19) — FEC Evaluation for MBMS Enhancement

---

📖 **Anglický originál a plná specifikace:** [LCT na 3GPP Explorer](https://3gpp-explorer.com/glossary/lct/)
