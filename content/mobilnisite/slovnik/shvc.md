---
slug: "shvc"
url: "/mobilnisite/slovnik/shvc/"
type: "slovnik"
title: "SHVC – Scalable High efficiency Video Coding"
date: 2025-01-01
abbr: "SHVC"
fullName: "Scalable High efficiency Video Coding"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/shvc/"
summary: "Scalable High efficiency Video Coding (SHVC) je standard pro kompresi videa, který rozšiřuje HEVC/H.265. Kóduje video do základní vrstvy a jedné či více vylepšujících vrstev, což umožňuje přizpůsobení"
---

SHVC je standard pro kompresi videa, který rozšiřuje HEVC kódováním videa do základní vrstvy a vylepšujících vrstev, což umožňuje přizpůsobení jediného datového proudu pro různá zařízení a síťové podmínky.

## Popis

Scalable High efficiency Video Coding (SHVC) je sofistikovaná architektura pro kódování videa standardizovaná skupinou [MPEG](/mobilnisite/slovnik/mpeg/) a formálně přijatá 3GPP v dokumentu TS 26.948. Jedná se o rozšíření standardu High Efficiency Video Coding ([HEVC](/mobilnisite/slovnik/hevc/)/H.265), které zavádí možnosti škálovatelného kódování. Základním principem SHVC je vrstvené kódování. Video je zakódováno nikoli jako jediný monolitický datový proud, ale jako více vzájemně závislých vrstev: povinná základní vrstva a jedna či více volitelných vylepšujících vrstev. Základní vrstva poskytuje základní kvalitu videa při nižším rozlišení a/nebo datovém toku. Každá následující vylepšující vrstva, když je dekódována společně se základní vrstvou a případně nižšími vylepšujícími vrstvami, progresivně zlepšuje kvalitu videa, zvyšuje prostorové rozlišení (např. z [SD](/mobilnisite/slovnik/sd/) na [HD](/mobilnisite/slovnik/hd/) až na 4K), časové rozlišení (snímkovou frekvenci) nebo poměr signálu k šumu (kvalitu).

Technické fungování spoléhá na predikci mezi vrstvami. Při kódování vylepšující vrstvy může enkodér použít rekonstruované snímky z nižší vrstvy (základní nebo předchozí vylepšující) jako referenci, kromě referencí v rámci stejné vrstvy. Tato predikce výrazně zlepšuje efektivitu komprese ve srovnání se simultánním vysíláním (nezávislé kódování více verzí). Datový proud je strukturován s jasnými značkami, jako jsou identifikátory vrstev a typy jednotek síťové abstraktní vrstvy ([NAL](/mobilnisite/slovnik/nal/)), definovanými ve specifikaci HEVC, které umožňují médiím-vědomému síťovému prvku nebo klientskému přehrávači snadno extrahovat podmnožinu vrstev.

V rámci architektury multimediálních služeb 3GPP se SHVC integruje s frameworkem Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)). Popis DASH Media Presentation ([MPD](/mobilnisite/slovnik/mpd/)) může popsat obsah zakódovaný pomocí SHVC jako jedinou adaptační sadu obsahující více reprezentací, které odpovídají různým kombinacím vrstev (např. Základní, Základní+Vylepšující1, Základní+Vylepšující1+Vylepšující2). Během streamování může DASH klient dynamicky vyžadovat segmenty obsahující pouze vrstvy vhodné pro aktuální schopnosti zařízení (velikost obrazovky, výkon dekodéru) a propustnost sítě. To eliminuje potřebu ukládat a spravovat více nezávislých zakódovaných verzí stejného obsahu, snižuje složitost úložiště a doručování a zároveň zajišťuje optimální kvalitu uživatelského zážitku (QoE) v široké škále uživatelských podmínek.

## K čemu slouží

SHVC byl vyvinut k řešení rostoucí fragmentace ve videoprůmyslu, která je charakterizována širokou škálou koncových zařízení s různým rozlišením displeje, výpočetním výkonem a profily síťového připojení (od mobilního 3G po optické širokopásmové připojení). Tradiční přístup transkódování a ukládání více nezávislých verzí (simultánní vysílání) stejného obsahu pro každý cílový profil je vysoce neefektivní z hlediska úložiště a šířky pásma, neboť nevyužívá redundanci mezi různými verzemi kvality.

Primární problém, který SHVC řeší, je potřeba jediné, efektivní a flexibilní reprezentace videa, kterou lze bezproblémově přizpůsobit. Jeho vytvoření bylo motivováno explozí adaptivního streamování s proměnným datovým tokem (ABR) a potřebou kódovacího standardu nativně podporujícího škálovatelnost. Zatímco dřívější standardy jako H.264/SVC nabízely škálovatelnost, nedosáhly stejné základní efektivity jako HEVC. SHVC staví na vynikající kompresi HEVC a přidává škálovatelnost s minimální ztrátou účinnosti kódování. To umožňuje poskytovatelům obsahu a síťovým operátorům ukládat jeden vysoce efektivní škálovatelný datový proud, z něhož lze pro jakéhokoli uživatele dynamicky odvodit optimální verzi pouhým oříznutím nebo extrahováním vrstev, což dramaticky zjednodušuje přípravu obsahu, logistiku úložiště a strategie ukládání do mezipaměti doručovacích sítí pro služby pro více obrazovek.

## Klíčové vlastnosti

- Vrstvená architektura kódování se základní a vylepšující vrstvou
- Vystavěno na HEVC/H.265 pro vysokou základní efektivitu komprese
- Podporuje prostorovou, časovou a kvalitativní (SNR) škálovatelnost
- Používá predikci mezi vrstvami k minimalizaci režie datového toku
- Bezešvě se integruje s adaptivním HTTP streamováním (DASH)
- Umožňuje ukládání jediného zakódovaného souboru pro doručování heterogenním zařízením

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [MPEG – Moving Pictures Experts Group](/mobilnisite/slovnik/mpeg/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)

## Definující specifikace

- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [SHVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/shvc/)
