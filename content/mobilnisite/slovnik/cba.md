---
slug: "cba"
url: "/mobilnisite/slovnik/cba/"
type: "slovnik"
title: "CBA – Channel-Based Audio"
date: 2025-01-01
abbr: "CBA"
fullName: "Channel-Based Audio"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cba/"
summary: "Channel-Based Audio (CBA) je standardizovaný audio formát 3GPP pro imerzivní vícekanálový přenos zvuku přes mobilní sítě. Umožňuje vysoce kvalitní prostorové audio zážitky tím, že kóduje audio jako di"
---

CBA je standardizovaný audio formát 3GPP pro imerzivní vícekanálový přenos zvuku přes mobilní sítě, který kóduje audio jako diskrétní kanály, aby umožnil vysoce kvalitní prostorové audio zážitky.

## Popis

Channel-Based Audio (CBA) je hlavní typ audio média standardizovaný v 3GPP TS 26.918, navržený pro přenos imerzivního audio obsahu, kde je zvuk reprezentován jako pevná sada audio kanálů, z nichž každý odpovídá konkrétní pozici reproduktoru v předdefinované konfiguraci. Na rozdíl od audio formátů založených na objektech, jako je MPEG-H 3D Audio, které popisují zdroje zvuku jako jednotlivé objekty s metadaty pro dynamický rendering, CBA kóduje audio jako diskrétní, předem namíchané kanály, jaké se používají v tradičních systémech surround zvuku (např. 5.1 s levým, středním, pravým, levým obklopujícím, pravým obklopujícím a nízkofrekvenčním efektovým kanálem, nebo 7.1 s dodatečnými zadními kanály). Tento přístup poskytuje přímočarou, výpočetně efektivní metodu pro doručování vysoce věrných vícekanálových audio zážitků přes mobilní sítě, zejména pro vysílání, streamování a stažená média, kde je audio mix statický a určený pro přehrávání na systémech se známým rozložením reproduktorů.

Technická implementace CBA v rámci 3GPP využívá existující rámce pro doručování médií, jako jsou protokoly Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)) a HTTP Live Streaming ([HLS](/mobilnisite/slovnik/hls/)), kde je CBA definováno jako specifický kodek nebo mediální profil. Audio obsah je zakódován pomocí podporovaných kodeků (např. Advanced Audio Coding - [AAC](/mobilnisite/slovnik/aac/) nebo Enhanced Voice Services - [EVS](/mobilnisite/slovnik/evs/) kodeky rozšířené pro vícekanálové použití) do diskrétních kanálových proudů, které jsou následně multiplexovány do mediálních kontejnerů jako [MP4](/mobilnisite/slovnik/mp4/) nebo transportní proudy. Během streamování přijímá klientské zařízení nebo mediální přehrávač tyto kanálové proudy a v závislosti na možnostech audio výstupu zařízení (např. stereo sluchátka, vícekanálové soundbary nebo domácí kina) může aplikovat algoritmy downmixingu nebo virtualizace, aby přizpůsobilo vícekanálové audio pro optimální přehrávání. Specifikace zahrnuje signalizační mechanismy v mediálních manifestech pro označení konfigurace kanálů (např. prostřednictvím atributu 'channelConfiguration' v DASH), což umožňuje klientům vybrat vhodné reprezentace a správně zvládnout rendering.

Klíčové architektonické komponenty CBA zahrnují audio enkodér, který vytváří vícekanálový bitstream; server pro balení médií a streamování, který zapouzdřuje audio do segmentů s adaptivní přenosovou rychlostí; a klientský mediální přehrávač s audio rendererem. Role CBA v ekosystému médií 5G spočívá v poskytování standardizovaného, interoperabilního formátu pro vysoce kvalitní audio služby, který doplňuje vylepšení videa jako streamování 4K/8K a virtuální realitu. Umožňuje poskytovatelům služeb nabízet imerzivní audio bez nutnosti komplexního zpracování audio založeného na objektech na všech klientských zařízeních, což jej činí vhodným pro masové aplikace jako mobilní [TV](/mobilnisite/slovnik/tv/), streamování hudby a video na vyžádání, kde je konzistentní, vysoce kvalitní audio zásadní. Tím, že je CBA součástí mediálních standardů 3GPP, zajišťuje bezproblémovou integraci s mechanismy QoS sítě, doručováním multicast/broadcast (např. přes 5G Broadcast) a end-to-end mediálními řetězci.

## K čemu slouží

Channel-Based Audio (CBA) bylo představeno v 3GPP Release 14, aby řešilo rostoucí poptávku po imerzivních audio zážitcích na mobilních zařízeních, poháněnou rozšířením vysoce kvalitního video obsahu (např. 4K, [HDR](/mobilnisite/slovnik/hdr/)) a vznikajícími službami jako virtuální realita a vylepšená mobilní TV. Před CBA byl přenos audia na mobilních zařízeních většinou omezen na stereo nebo mono formáty, které nevyužívaly možností moderních vícekanálových audio systémů v domácnostech a na špičkových mobilních zařízeních. Existující audio standardy jako AAC sice podporovaly vícekanálové kódování, ale postrádaly jednotnou, pro sítě optimalizovanou specifikaci pro streamování vícekanálového audia přes celulární sítě, což vedlo k fragmentaci a nekonzistentní implementaci napříč službami a zařízeními. CBA poskytuje standardizovaný rámec pro překlenutí této mezery a umožňuje konzistentní, vysoce věrné audio, které odpovídá vizuální kvalitě pokročilých video služeb.

Vytvoření CBA bylo motivováno potřebou podporovat vysílací a streamovací aplikace, kde je audio profesionálně namícháno pro specifická rozložení kanálů, jako ve filmové, televizní a sportovní produkci. Audio formáty založené na objektech, ačkoli flexibilní, vyžadují složitější rendering a zpracování metadat, což může být náročné na zdroje pro mobilní zařízení a nemusí být nutné pro obsah se statickými audio mixy. CBA nabízí jednodušší, efektivnější alternativu standardizací přenosu předem vyrenderovaného kanálového audia, čímž snižuje procesní režii na klientských zařízeních a zároveň zajišťuje kompatibilitu s existujícími audio produkčními postupy. To jej činí zvláště vhodným pro služby jako 5G Broadcast (FeMBMS) a over-the-top mediální streamování, kde je efektivní doručování kinematografického nebo vysílacího kvalitního audia milionům uživatelů klíčové.

Historicky omezení předchozích přístupů zahrnovala nedostatek standardizované signalizace pro vícekanálové audio v adaptivních streamovacích protokolech, což vedlo k ad-hoc implementacím a špatné interoperabilitě. CBA jako součást mediálních standardů 3GPP tyto problémy řeší definováním jasných profilů kodeků, kontejnerových formátů a streamovacích protokolů pro kanálové audio, což usnadňuje široké přijetí v odvětví. Také se sladí s vývojem sítí 5G, které poskytují vysokou přenosovou rychlost a nízkou latenci potřebnou pro imerzivní média, což operátorům umožňuje diferencovat své služby lepší audio kvalitou. Tím, že CBA řeší tyto technické a tržní potřeby, pomáhá odemknout nové zdroje příjmů pro mediální poskytovatele a zlepšuje uživatelský zážitek pro mobilní spotřebitele.

## Klíčové vlastnosti

- Standardizovaný vícekanálový audio formát pro konfigurace 5.1, 7.1 a další surround
- Integrace s adaptivními streamovacími protokoly jako DASH a HLS pro efektivní doručování
- Podpora vysoce efektivních audio kodeků včetně AAC a EVS
- Signalizace konfigurací kanálů v mediálních manifestech pro adaptaci na straně klienta
- Kompatibilita s existujícími audio produkčními a vysílacími postupy
- Optimalizace pro doručování přes mobilní sítě včetně multicast/broadcast scénářů

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP

---

📖 **Anglický originál a plná specifikace:** [CBA na 3GPP Explorer](https://3gpp-explorer.com/glossary/cba/)
