---
slug: "xr"
url: "/mobilnisite/slovnik/xr/"
type: "slovnik"
title: "XR – AS Augmented/Virtual Reality Application Server"
date: 2026-01-01
abbr: "XR"
fullName: "AS Augmented/Virtual Reality Application Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/xr/"
summary: "Aplikační server (AS) v sítích 3GPP speciálně navržený pro podporu služeb rozšířené reality (AR) a virtuální reality (VR). Spravuje doručování XR obsahu, řízení relací a adaptaci kvality, aby splnil v"
---

XR je aplikační server (Application Server) v sítích 3GPP navržený pro podporu služeb rozšířené a virtuální reality (AR/VR) tím, že spravuje doručování obsahu, řízení relací a adaptaci kvality pro imerzivní aplikace přes 5G.

## Popis

[AS](/mobilnisite/slovnik/as/) Augmented/Virtual Reality Application Server (XR AS) je síťová funkce v rámci servisně orientované architektury 5G, která usnadňuje doručování a správu aplikací rozšířené reality (Extended Reality, XR), zahrnující rozšířenou realitu ([AR](/mobilnisite/slovnik/ar/)), virtuální realitu ([VR](/mobilnisite/slovnik/vr/)) a smíšenou realitu ([MR](/mobilnisite/slovnik/mr/)). Funguje jako aplikační server, který často komunikuje s 5G Core (5GC) přes [NEF](/mobilnisite/slovnik/nef/) (Network Exposure Function) nebo přímo s [UPF](/mobilnisite/slovnik/upf/) (User Plane Function), aby ovlivnil zpracování provozu. XR AS je zodpovědný za zpracování XR obsahu, správu uživatelských relací a zajištění optimalizace síťových prostředků pro náročné požadavky imerzivních zážitků.

Architektonicky se XR AS integruje s 5G síťovými funkcemi, aby umožnil funkce jako edge computing, síťové řezy (network slicing) a vynucování kvality služeb (QoS). Může být umístěn v síti operátora nebo na okraji sítě, blízko uživatelů, pro snížení latence. Mezi klíčové komponenty patří mediální procesory pro kódování/dekódování XR proudů, správci relací pro obsluhu uživatelských připojení a analytické nástroje pro sledování výkonnostních metrik, jako je snímková frekvence a latence pohyb-foton. Server komunikuje s zařízeními pomocí protokolů jako [RTP](/mobilnisite/slovnik/rtp/)/[RTCP](/mobilnisite/slovnik/rtcp/) pro přenos médií a HTTP/2 pro řídicí signalizaci, často využívajíc API definovaná 3GPP pro interakci se sítí.

Při provozu XR AS přijímá obsah od poskytovatelů XR, přizpůsobuje jej na základě možností zařízení a síťových podmínek a streamuje jej do uživatelského zařízení (UE). Spolupracuje se sítí 5G při žádostech o specifické QoS toky, zajišťuje vysokou přenosovou kapacitu a nízkou latenci pomocí mechanismů jako Guaranteed Bit Rate (GBR) a úrovně priority. Pro interaktivní XR server zpracovává uplink data ze senzorů (např. sledování polohy hlavy) a podle toho upravuje downlink proud, čímž minimalizuje nevolnost z pohybu. Podporuje také funkce jako rozdělené vykreslování (split rendering), kde jsou výpočetně náročné úlohy přesunuty na okraj sítě, čímž se snižuje zátěž zařízení.

Role XR AS je podrobně popsána v technických specifikacích, jako jsou 3GPP TS 26.928 a 22.261, které definují požadavky na XR služby přes 5G. Slouží jako centrální bod pro aplikační logiku, řeší aspekty jako uživatelská autentizace, licence k obsahu a adaptivní streamování s proměnným datovým tokem. Koordinací se síťovými funkcemi umožňuje dynamické přidělování prostředků, což je klíčové pro udržení imerze při pohybu uživatelů nebo změně síťových podmínek. To činí z XR AS klíčový prvek pro naplnění vize 5G pro kritické aplikace nad rámec tradičního mobilního širokopásmového připojení.

## K čemu slouží

XR AS byl vyvinut, aby řešil jedinečné výzvy spojené s doručováním imerzivních AR/VR zážitků přes mobilní sítě, které se objevily jako klíčové případy užití pro 5G. Před jeho zavedením byly sítě optimalizovány pro streamování videa a prohlížení webu, postrádaly však nízkou latenci, vysokou spolehlivost a asymetrické profily přenosové kapacity vyžadované pro interaktivní XR. To vedlo ke špatným uživatelským zážitkům, jako je zpoždění a dezorientace, což omezovalo přijetí XR na bezdrátových zařízeních.

Jeho vytvoření bylo motivováno potřebou standardizovaného aplikačního serveru s přístupem k síťovým informacím, který by mohl propojit poskytovatele XR obsahu a možnosti 5G. Dřívější přístupy spoléhaly na obecné servery bez hluboké integrace se sítí, což vedlo k neefektivnímu využití prostředků a neschopnosti garantovat výkon. XR AS to řeší využitím funkcí 5G, jako jsou síťové řezy a edge computing, což umožňuje přizpůsobené zacházení s XR provozem. Operátorům umožňuje nabízet XR jako diferencovanou službu, která splňuje požadavky odvětví, jako jsou hry, školení a vzdálená asistence.

Historicky začal 3GPP studovat XR ve verzi 16 (Release 16), když rozpoznal jeho potenciál pohánět adopci 5G. XR AS ztělesňuje toto úsilí a poskytuje rámec pro správu kompletního doručování služby. Odstraňuje omezení řešení typu over-the-top tím, že umožňuje optimalizace s asistencí sítě, jako je prediktivní QoS a kontextově citlivé streamování. To zajišťuje, že XR aplikace mohou efektivně škálovat při zachování kvality, čímž podporují růst metavesmíru a dalších imerzivních technologií v éře 5G.

## Klíčové vlastnosti

- Spravuje zřizování, řízení a ukončování XR relací
- Integruje se s 5G Core pro dynamické QoS a síťové řezy (network slicing)
- Podporuje edge computing pro snížení latence u interaktivního XR
- Umožňuje adaptivní streamování s proměnným datovým tokem na základě stavu zařízení a sítě
- Zpracovává data ze senzorů pro úpravu obsahu v reálném čase
- Umožňuje rozdělené vykreslování (split rendering) přesunutím výpočtů do sítě

## Související pojmy

- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.873** (Rel-18) — Technical Report on IMS Multimedia Telephony Service Enhancements
- **TR 26.812** (Rel-18) — Technical Report
- **TS 26.854** (Rel-19) — Study on Haptics in 5G Media Services
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 33.790** (Rel-19) — Security for Next-Gen Real-Time Communication Phase 2
- **TR 38.835** (Rel-18) — Technical Report on XR Enhancements for NR
- **TR 38.838** (Rel-17) — Study on XR Evaluations for NR
- **TR 38.864** (Rel-18) — Technical Report on Network Energy Savings for NR
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR
- **TR 38.890** (Rel-17) — NR QoE Management and Optimization

---

📖 **Anglický originál a plná specifikace:** [XR na 3GPP Explorer](https://3gpp-explorer.com/glossary/xr/)
