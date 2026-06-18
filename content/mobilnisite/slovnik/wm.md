---
slug: "wm"
url: "/mobilnisite/slovnik/wm/"
type: "slovnik"
title: "WM – WaterMark or WaterMarking"
date: 2025-01-01
abbr: "WM"
fullName: "WaterMark or WaterMarking"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wm/"
summary: "WaterMarking (WM) v kontextu 3GPP označuje techniky pro vkládání nepostřehnutelných identifikačních dat do mediálních proudů, primárně pro sledování obsahu a správu autorských práv ve službě Multimedi"
---

WM je technika pro vkládání nepostřehnutelných identifikačních dat do mediálních proudů za účelem sledování obsahu a správy autorských práv ve službě Multimedia Broadcast/Multicast Service.

## Popis

WaterMarking (WM), v kontextu 3GPP definovaném v TS 26.953, je bezpečnostní a správní technologie práv aplikovaná na multimediální obsah doručovaný přes mobilní sítě, konkrétně prostřednictvím služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a její pokročilé formy Enhanced MBMS (eMBMS). Zahrnuje proces nepostřehnutelného vložení jedinečného, robustního identifikátoru – vodoznaku – do audio, video nebo audiovizuální podstaty mediálního proudu. Tento identifikátor je navržen tak, aby přečkal standardní zpracovatelské operace, jako je překódování, komprese a analogově-digitální konverze, což umožňuje jeho detekci a extrakci i poté, co byl obsah redistribuován nebo zaznamenán.

Architektura vodoznaku v MBMS zahrnuje několik klíčových komponent. Na vysílací straně Vkladač vodoznaku (Watermark Embedder), který může být součástí Broadcast-Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) nebo samostatné entity pro přípravu obsahu, vloží datovou část vodoznaku (payload) do média podle specifického algoritmu. Datová část může obsahovat informace jako ID obsahu, ID relace, ID služby nebo dokonce informace specifické pro příjemce (fingerprinting). Obsah s vodoznakem je následně zakódován, multiplexován a vysílán přes přenosový kanál MBMS. Na přijímací straně může kompatibilní uživatelské zařízení (UE) s podporou detekce vodoznaku tento vodoznak extrahovat. Pro forenzní sledování může specializované detekční zařízení analyzovat zachycený obsah a získat vodoznak, čímž identifikuje zdroj úniku nebo neoprávněné kopie.

Technický princip závisí na algoritmu, ale typicky využívá psychoakustické nebo psychovizuální modely k úpravě mediálního signálu způsobem, který je pod prahem lidského vnímání (nepostřehnutelný), ale statisticky detekovatelný. Pro audio to může zahrnovat úpravu fázových vztahů ve specifických frekvenčních pásmech; pro video to mohou být nepatrné úpravy hodnot jasu ve vybraných snímcích nebo blocích. Specifikace 3GPP standardizuje požadavky, formáty datové části a signalizaci pro systémy vodoznaku, aby zajistila interoperabilitu, přičemž implementátorům ponechává flexibilitu ve volbě konkrétní vodoznakové technologie. Jejím úkolem je poskytnout trvalý, neoddělitelný spoj mezi obsahem a jeho distribučními metadaty, což umožňuje poskytovatelům obsahu monitorovat využití, prokázat vlastnictví a odradit od pirátství ve vysílacích a multicastových scénářích.

## K čemu slouží

WaterMarking byl do standardů 3GPP zaveden, aby řešil jedinečné výzvy ochrany obsahu spojené s vysílacími a multicastovými modely doručování, jako je [MBMS](/mobilnisite/slovnik/mbms/). Na rozdíl od unicastu, kde je obsah doručován jednotlivému odběrateli se známou identitou, multicast/broadcast inherentně doručuje stejný obsah potenciálně milionům anonymních zařízení. Tradiční šifrování Digital Rights Management ([DRM](/mobilnisite/slovnik/drm/)) zabezpečuje přenos, ale nechrání obsah poté, co je dešifrován a přehrán na kompatibilním zařízení, kde může být znovu zaznamenán a redistribuován (tzv. „analogová díra“ nebo problém redistribuce).

Účelem vodoznaku je poskytnout forenzní sledovací mechanismus, který přečká toto nové nahrávání. Řeší problém identifikace zdroje obsahu a trasování „zrádce“ ve scénářích, kde samotné šifrování nestačí. Pokud je vysílání s vodoznakem nelegálně zaznamenáno a sdíleno, lze vložený identifikátor extrahovat a určit konkrétní vysílací službu, čas nebo dokonce geografickou oblast úniku. Tato schopnost je klíčová pro vlastníky obsahu (např. filmová studia, sportovní ligy) pro ochranu jejich duševního vlastnictví při využití MBMS pro prémiové služby, jako jsou živé sportovní přenosy nebo uvedení filmů. Jeho vznik byl motivován komerčními požadavky, aby se MBMS stalo životaschopnou platformou pro obsah s vysokou hodnotou přidáním robustní vrstvy bezpečnosti po dešifrování, čímž se umožní nové obchodní modely a splní licenční požadavky poskytovatelů obsahu.

## Klíčové vlastnosti

- Vkládá nepostřehnutelné, robustní identifikátory přímo do audio/video podstaty média
- Podporuje forenzní sledování a trasování „zrádců“ pro vysílací/multicastový obsah
- Datová část může nést informace o obsahu, relaci, službě nebo informace specifické pro příjemce
- Navrženo tak, aby přečkalo překódování, kompresi a analogové nové nahrávání
- Standardizováno pro použití v architekturách doručování MBMS/eMBMS (TS 26.953)
- Doplňuje šifrování založené na DRM tím, že poskytuje bezpečnost po dešifrování

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)

## Definující specifikace

- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [WM na 3GPP Explorer](https://3gpp-explorer.com/glossary/wm/)
