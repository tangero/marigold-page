---
slug: "vvc"
url: "/mobilnisite/slovnik/vvc/"
type: "slovnik"
title: "VVC – Versatile Video Coding"
date: 2025-01-01
abbr: "VVC"
fullName: "Versatile Video Coding"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vvc/"
summary: "Vysoce účinný standard pro kompresi videa vyvinutý společně skupinami MPEG a ITU-T (jako H.266). 3GPP přijalo VVC pro doručování médií přes systémy 5G, což umožňuje video v ultra vysokém rozlišení (4K"
---

VVC je vysoce účinný standard pro kompresi videa přijatý 3GPP pro doručování médií v 5G, který umožňuje ultra vysoké rozlišení a imerzivní video s přibližně o 50 % lepší kompresí než jeho předchůdce, HEVC.

## Popis

Versatile Video Coding (VVC), standardizovaný jako H.266 skupinou [ITU-T](/mobilnisite/slovnik/itu-t/) a MPEG-I Part 3 ([ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 23090-3), je nejnovější generace video kodeku začleněná do specifikací 3GPP pro multimediální služby. Jeho hlavní funkcí je komprimovat digitální video s výrazně vyšší účinností než předchozí standardy, jako je High Efficiency Video Coding ([HEVC](/mobilnisite/slovnik/hevc/)/H.265) a Advanced Video Coding ([AVC](/mobilnisite/slovnik/avc/)/H.264). 3GPP standardizovalo použití VVC pro doručování médií přes sítě 5G, definující profily, úrovně a přenosové formáty ve specifikacích jako 26.927 a 26.928, aby zajistilo interoperabilitu mezi servery, sítěmi a uživatelskými zařízeními (UE).

Architektonicky VVC vychází z hybridního blokového kódovacího modelu, ale zavádí řadu pokročilých nástrojů, které přispívají k jeho účinnosti. Základní jednotkou je kódovací stromová jednotka ([CTU](/mobilnisite/slovnik/ctu/)), která může být rozdělena pomocí sofistikované více-typové stromové struktury umožňující binární, ternární a kvadrantové dělení, což umožňuje mnohem přesnější adaptaci na obsah videa. Mezi klíčové technické komponenty patří vylepšená intra predikce s 93 směrovými režimy (ve srovnání s 33 v HEVC), afinní pohybová predikce pro komplexní netranslační pohyb, adaptivní smyčkové filtry (ALF) pro redukci artefaktů a rafinace pohybových vektorů na straně dekodéru. Pro imerzivní média zavádí VVC specifické nástroje pro 360stupňové video, jako je ekvirektangulární projekce a regionální balení. Kodek funguje tak, že rozdělí video sekvenci na řezy a dlaždice pro paralelní zpracování, aplikuje prostorovou (intra) a časovou (inter) predikci, transformuje reziduální data a aplikuje entropické kódování ([CABAC](/mobilnisite/slovnik/cabac/)).

V rámci ekosystému 3GPP je VVC integrováno do služby Multimedia Broadcast and Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a Packet Switched Streaming Service (PSS). Jeho úlohou je umožnit doručování náročných video aplikací přes 5G New Radio (NR) s efektivním využitím šířky pásma. To je klíčové pro služby jako vysílání 4K/8K, rozšířená realita (AR), virtuální realita (VR) a cloudové hraní, kde jsou vysoké rozlišení, vysoká snímková frekvence a nízká latence prvořadé. Specifikace 3GPP definují, jak jsou VVC bitové toky paketizovány pro přenos přes RTP/IP nebo MPEG-2 TS, a jak manifesty Dynamic Adaptive Streaming over HTTP (DASH) signalizují možnosti VVC. Síťový rámec Quality of Service (QoS) může být aplikován na VVC mediální toky, aby zajistil potřebný datový tok a výkon při ztrátě paketů, což z něj činí základní enabler pro rozšířenou mobilní širokopásmovou službu (eMBB) a kategorii služeb masivního internetu věcí (mIoT), které zahrnují bohatá média.

## K čemu slouží

VVC bylo vytvořeno, aby řešilo exponenciální růst video provozu, který dominuje mobilním sítím, a vznik nových, datově náročných video formátů. Jeho předchůdce, HEVC, byl sice účinný, ale čelil licenčním komplikacím a dosahoval svých kompresních limitů pro aplikace příští generace, jako je rozlišení 8K (až 7680x4320 pixelů), video s vysokým dynamickým rozsahem (HDR) a imerzivní 360stupňový obsah. Streamování takového obsahu pomocí HEVC by spotřebovávalo nepřijatelné množství vzácného bezdrátového spektra, zvyšovalo náklady a zhoršovalo výkon sítě pro všechny uživatele.

Motivace pro standardizaci VVC v rámci 3GPP, počínaje Release 16, byla připravit sítě 5G na mediální prostředí 20. let 21. století a dále. 5G slibuje vícegigabitové datové rychlosti a ultra nízkou latenci, ale bez odpovídajícího skoku v kompresní účinnosti by tyto schopnosti byly promrhány pouhým přenosem režie. Přibližné 50% snížení datového toku VVC při stejné vizuální kvalitě jako HEVC přímo znamená obsloužení dvojnásobku uživatelů kvalitním videem nebo umožnění dříve nepraktických služeb, jako je živé vysílání 8K do mobilních zařízení. Dále, standardizací jeho použití, 3GPP zajišťuje konzistentní, interoperabilní mediální vrstvu napříč globálními nasazeními 5G, čímž se vyhýbá fragmentaci a podporuje široké přijetí poskytovateli zařízení a služeb.

## Klíčové vlastnosti

- Přibližně o 50 % lepší kompresní účinnost než HEVC při stejné kvalitě videa
- Podpora ultra vysokého rozlišení videa až do 8K a výše
- Pokročilé dělicí struktury (více-typový strom) pro přesnou segmentaci bloků
- Vylepšené predikční nástroje včetně afinního pohybu a 93 intra predikčních režimů
- Specifické kódovací nástroje pro 360stupňová všesměrová imerzivní videa
- Podpora obsahu s vysokým dynamickým rozsahem (HDR) a širokým barevným gamutem (WCG)

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [AVC – Assured Voice Communication](/mobilnisite/slovnik/avc/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [VVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/vvc/)
