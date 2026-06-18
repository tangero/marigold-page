---
slug: "scte"
url: "/mobilnisite/slovnik/scte/"
type: "slovnik"
title: "SCTE – Society of Cable Telecommunications Engineers"
date: 2025-01-01
abbr: "SCTE"
fullName: "Society of Cable Telecommunications Engineers"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/scte/"
summary: "SCTE je organizace pro vývoj standardů v odvětví kabelových telekomunikací, odkazovaná v 3GPP v souvislosti s propojováním a doručováním médií. Poskytuje specifikace pro doručování obsahu po kabelovýc"
---

SCTE je standardizační organizace pro kabelové telekomunikace, odkazovaná v 3GPP pro specifikace doručování obsahu po kabelových sítích, aby byla zajištěna kompatibilita s mobilním streamováním médií a vysílacími službami.

## Popis

Society of Cable Telecommunications Engineers (SCTE) je externí standardizační orgán, nikoli interní protokol nebo architektura 3GPP. V rámci specifikací 3GPP jsou standardy SCTE odkazovány především pro definici formátů médií, transportních mechanismů a signalizačních protokolů používaných v kabelové televizi a širokopásmových sítích. To je zvláště relevantní pro službu Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a služby streamování médií 3GPP, kde je pro konvergované mediální zážitky vyžadováno propojení s kabelovými systémy doručování. Tyto odkazy zajišťují, že obsah zakódovaný a zabalený podle standardů SCTE může být bezproblémově doručen a zobrazen na zařízeních podporujících 3GPP.

Technická role SCTE v 3GPP je z velké části zprostředkována normativními odkazy ve specifikacích jako TS 26.804 (Media handling for IMS messaging) a TS 26.949 (Study on 5G Media Streaming ([5GMS](/mobilnisite/slovnik/5gms/)) architecture). Tyto specifikace mohou odkazovat na standardy SCTE pro konkrétní formáty zapouzdření médií (např. SCTE 35 pro vkládání digitálních programových značek) nebo transportní protokoly používané v adaptivním streamování s proměnným datovým tokem po kabelu. Bod integrace se typicky nachází na aplikační vrstvě, kde klient 3GPP (např. 5GMS Application Function) může potřebovat parsovat metadata nebo časovací signály definované SCTE, které jsou vloženy do mediálních streamů.

Z architektonické perspektivy standardy SCTE ovlivňují návrh vrstvy pro doručování médií v systémech 3GPP. Například v 5G Media Streaming může příprava obsahu nebo Media Session Handler potřebovat podporovat SCTE-214 ([DASH](/mobilnisite/slovnik/dash/) over [MPEG-2](/mobilnisite/slovnik/mpeg-2/) TS) nebo podobné profily, aby byla zajištěna vysílací časová přesnost a možnosti vkládání reklam. Klíčovými součástmi jsou kodéry médií, baliče a klientské mediální přehrávače v ekosystému 3GPP, které musí být kompatibilní jak s 3GPP, tak s příslušnými technickými doporučeními SCTE, aby byla zaručena interoperabilita v hybridních scénářích vysílání a širokopásmového přenosu.

Její role spočívá v poskytování mostu mezi tradičním kabelovým vysílacím průmyslem a světem mobilního širokopásmového přenosu založeného na IP, který definuje 3GPP. Začleněním odkazů na SCTE 3GPP zajišťuje, že poskytovatelé služeb mohou nasazovat mediální služby, které fungují napříč pevnými kabelovými a mobilními sítěmi, aniž by vyžadovaly proprietární překladové vrstvy. To je klíčové pro dosažení úspor z rozsahu při produkci obsahu a pro umožnění pokročilých funkcí, jako je cílená reklama nebo synchronizované zážitky na druhém obrazovce.

## K čemu slouží

Účelem odkazování na standardy SCTE v rámci 3GPP je usnadnit konvergenci mezi mobilními telekomunikacemi a ekosystémy pro doručování médií po kabelu/vysíláním. Historicky se kabelové a mobilní sítě vyvíjely odděleně s odlišnými standardy pro kódování videa, transport a signalizaci. S rostoucí poptávkou spotřebitelů po bezproblémových mediálních zážitcích napříč zařízeními a sítěmi potřebovalo 3GPP zajistit, aby jeho rámce pro doručování médií (jako [MBMS](/mobilnisite/slovnik/mbms/) a později [5GMS](/mobilnisite/slovnik/5gms/)) mohly spolupracovat se zavedenou a výkonnou kabelovou infrastrukturou.

Tím se řeší problém fragmentace médií a umožňuje se poskytovatelům služeb používat společnou sadu nástrojů pro přípravu obsahu a formátů jak pro kabelovou [TV](/mobilnisite/slovnik/tv/), tak pro mobilní doručování typu over-the-top ([OTT](/mobilnisite/slovnik/ott/)). Bez takových odkazů by operátoři potřebovali nákladné a složité systémy pro překódování a přebalování, aby mohli doručovat stejný obsah po různých sítích. Motivace vychází z průmyslového trendu směrem ke konvergenci založené na IP, kde může být jediný mediální asset efektivně doručován prostřednictvím více přístupových technologií a využívat tak přednosti každé z nich (např. vysílací efektivitu kabelu a personalizaci unicastu v 5G).

## Klíčové vlastnosti

- Poskytuje standardizované formáty zapouzdření médií pro kabel/vysílání
- Definuje signalizaci pro vkládání reklam a programové značky (např. SCTE 35)
- Specifikuje transportní protokoly pro MPEG-DASH přes MPEG-2 Transport Stream
- Umožňuje časovou synchronizaci mezi vysílacími a širokopásmovými streamy
- Podporuje signalizaci pro nouzová upozornění a hodnocení obsahu
- Usnadňuje servisní architektury hybridního vysílání a širokopásmového přenosu (podobné HbbTV)

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [SCTE na 3GPP Explorer](https://3gpp-explorer.com/glossary/scte/)
