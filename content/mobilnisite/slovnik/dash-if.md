---
slug: "dash-if"
url: "/mobilnisite/slovnik/dash-if/"
type: "slovnik"
title: "DASH-IF – DASH Industry Forum"
date: 2025-01-01
abbr: "DASH-IF"
fullName: "DASH Industry Forum"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dash-if/"
summary: "DASH-IF je průmyslové konsorcium, které vyvíjí a propaguje standard MPEG-DASH pro adaptivní streamování s proměnnou datovou rychlostí přes HTTP. Poskytuje pokyny, testovací vektory a referenční softwa"
---

DASH-IF je průmyslové konsorcium, které vyvíjí a propaguje standard MPEG-DASH, přičemž poskytuje pokyny a nástroje pro zajištění interoperability adaptivního streamování v sítích 3GPP.

## Popis

[DASH](/mobilnisite/slovnik/dash/) Industry Forum (DASH-IF) je nezávislé průmyslové konsorcium, nikoli protokol definovaný 3GPP, avšak jeho práce je v rámci specifikací 3GPP odkazována a přijímána, zejména pro služby doručování médií. 3GPP TS 26.949 odkazuje na implementační pokyny DASH-IF, aby zajistil konzistentní a interoperabilní aplikaci standardu MPEG-DASH (Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/)) v ekosystému 3GPP. MPEG-DASH je mezinárodní standard ([ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 23009) pro adaptivní streamování s proměnnou datovou rychlostí, který umožňuje klientovi dynamicky vybírat a přepínat mezi různými mediálními segmenty kódovanými v různých datových rychlostech a rozlišeních na základě aktuálních síťových podmínek a možností zařízení.

Architektonicky DASH funguje nad standardními HTTP webovými servery, což jej činí vysoce škálovatelným a přátelským k firewallům. Ústřední součástí je Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)), manifestní soubor [XML](/mobilnisite/slovnik/xml/), který popisuje strukturu mediální prezentace, včetně dostupných adaptačních sad (např. video, audio, titulky), reprezentací (různých kvalitativních verzí) a [URL](/mobilnisite/slovnik/url/) segmentů. Klient nejprve získá MPD a poté na základě své adaptivní logiky žádá jednotlivé mediální segmenty (typicky v kontejnerech ISO Base Media File Format nebo [MPEG-2](/mobilnisite/slovnik/mpeg-2/) TS). Tento přístup řízený klientem přesouvá inteligenci na okraj sítě, čímž snižuje zatížení sítě a zdrojových serverů.

V rámci sítě 3GPP spočívá role DASH-IF v poskytování konkrétních implementačních profilů a bodů interoperability (IOP), které specifikují, jak používat DASH pro konkrétní servisní scénáře, jako je živé, na vyžádání nebo streamování s nízkou latencí. Tyto pokyny pokrývají aspekty jako omezení kodeků, šifrování pro DRM (Digital Rights Management) pomocí Common Encryption (CENC), signalizaci vkládání reklam a reportování metrik. Odkazováním na IOP DASH-IF zajišťuje 3GPP, že mediální servery, nástroje pro přípravu obsahu a klienti přehrávačů od různých dodavatelů mohou bezproblémově spolupracovat, což je klíčové pro komerční mobilní video služby jako LTE Broadcast (eMBMS) a 5G Media Streaming.

Integrace zahrnuje architektury 3GPP Packet Switched Streaming (PSS) a Multimedia Broadcast/Multicast Service (MBMS). Streamovací klient, často aplikace na uživatelském zařízení (UE), používá protokoly HTTP/HTTPS přes IP připojení k paketové datové síti (PDN) pro komunikaci s mediálním serverem podporujícím DASH. Pro vysílání/multicastové doručování přes eMBMS může BM-SC (Broadcast Multicast Service Centre) doručovat DASH segmenty přes vysílací nosič a DASH MPD poskytuje potřebná metadata pro klienty, aby k tomuto vysílacímu proudu získali přístup. Práce DASH-IF zajišťuje, že jsou tyto složité mechanismy doručování standardizovány a interoperabilní.

## K čemu slouží

DASH-IF bylo vytvořeno za účelem řešení fragmentace na raném trhu adaptivního streamování, který ovládala proprietární řešení jako Apple HLS, Microsoft Smooth Streaming a Adobe HDS. Tyto nekompatibilní formáty nutily poskytovatele obsahu kódovat a ukládat více verzí svých médií, což zvyšovalo složitost a náklady. Standard MPEG-DASH, vyvinutý skupinou MPEG, poskytl jednotný mezinárodní standard, ale jako abstraktní specifikace připouštěl mnoho implementačních možností, což hrozilo opětovným vytvořením problému interoperability, který měl řešit.

Účelem DASH Industry Forum je překlenout tuto mezeru vytvářením konkrétních implementačních pokynů a podporou přijetí jediného interoperabilního profilu MPEG-DASH. Poskytováním testovacích vektorů, referenčního softwaru (jako je DASH-IF Reference Player) a certifikačních programů umožňuje DASH-IF dodavatelům vytvářet produkty, které vzájemně spolupracují přímo po vybalení. Pro 3GPP, které standardizuje systémy mobilní telekomunikace, představuje odkazování na pokyny DASH-IF v TS 26.949 stabilní, průmyslově ověřený základ pro služby doručování médií. To umožňuje 3GPP soustředit se na optimalizace specifické pro síť (jako QoS, mobilita a integrace vysílání), aniž by muselo znovu vynalézat základní streamovací technologii, a tím urychlit nasazení kvalitních video služeb přes sítě 4G a 5G.

## Klíčové vlastnosti

- Definuje interoperabilní implementační profily (IOP) pro MPEG-DASH
- Poskytuje pokyny pro integraci Common Encryption (CENC) se systémy DRM
- Specifikuje metadata a signalizaci pro vkládání reklam a zprávy o událostech
- Podporuje scénáře streamování na vyžádání i živého streamování s nízkou latencí
- Zahrnuje konformní a referenční software pro testování dodavateli
- Umožňuje efektivní využití HTTP cache a infrastruktur CDN

## Definující specifikace

- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [DASH-IF na 3GPP Explorer](https://3gpp-explorer.com/glossary/dash-if/)
