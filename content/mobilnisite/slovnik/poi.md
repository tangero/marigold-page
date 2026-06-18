---
slug: "poi"
url: "/mobilnisite/slovnik/poi/"
type: "slovnik"
title: "POI – Point Of Interconnection"
date: 2025-01-01
abbr: "POI"
fullName: "Point Of Interconnection"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/poi/"
summary: "POI (Point Of Interconnection, bod propojení) je fyzické a logické rozhraní, kde se 3GPP mobilní síť připojuje k veřejné telefonní síti (PSTN) nebo jiným externím sítím. Umožňuje interoperabilitu pro"
---

POI (Point Of Interconnection, bod propojení) je fyzické a logické rozhraní, kde se 3GPP mobilní síť připojuje k externím sítím, jako je PSTN, a umožňuje interoperabilitu pro hlasové a datové služby.

## Popis

Point Of Interconnection (POI, bod propojení) je kritické síťové rozhraní definované ve specifikacích 3GPP, které slouží jako demarkační bod mezi jádrovou sítí mobilního operátora a externími sítěmi, především veřejnou telefonní sítí ([PSTN](/mobilnisite/slovnik/pstn/)). Zahrnuje jak fyzickou konektivitu (např. kabeláž a porty), tak logické protokoly pro signalizaci a přenos médií. Z architektonického hlediska se POI typicky nachází na hranici jádrové sítě a zahrnuje síťové prvky jako Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) ve 2G/3G nebo Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) a IMS komponenty v 4G/5G. POI umožňuje výměnu hlasových hovorů, [SMS](/mobilnisite/slovnik/sms/) a dalších okruhově přepínaných služeb mezi mobilními uživateli a účastníky PSTN, čímž zajišťuje interoperabilitu napříč různými síťovými technologiemi. Mezi klíčové komponenty patří signalizační rozhraní jako [SS7](/mobilnisite/slovnik/ss7/) (Signaling System No. 7) pro navázání a ukončení hovoru a mediální brány, které převádějí mezi paketově přepínanými (např. IP v LTE/5G) a okruhově přepínanými (např. [TDM](/mobilnisite/slovnik/tdm/) v PSTN) formáty. POI funguje tak, že směruje příchozí a odchozí provoz na základě číslovacích plánů (např. E.164), přičemž signalizační protokoly zajišťují překlad adres, účtování a servisní funkce. V sítích 3GPP se POI vyvíjí s technologickými generacemi: ve 2G/3G zahrnuje přímé propojení MSC s PSTN; v 4G se integruje s IMS prostřednictvím prvků jako Breakout Gateway Control Function ([BGCF](/mobilnisite/slovnik/bgcf/)) a MGW pro VoLTE; a v 5G podporuje propojení přes 5G Core a služby simulace PSTN/[ISDN](/mobilnisite/slovnik/isdn/). POI hraje zásadní roli při zajišťování kontinuity služeb od konce ke konci, což umožňuje mobilním uživatelům komunikovat s pevnými linkami a naopak. Také podporuje regulatorní požadavky na propojení, jako je přenositelnost čísel a přístup ke službám tísňového volání. Technicky musí POI zvládat vysokou spolehlivost a nízkou latenci pro zachování kvality hovoru, s redundantními mechanismy pro prevenci výpadků služeb. Standardy jako 3GPP TS 23.271 specifikují požadavky na POI pro lokalizační služby, zatímco jiné pokrývají bezpečnostní a protokolové detaily, což zajišťuje konzistentní implementaci napříč operátory.

## K čemu slouží

POI existuje, aby řešil základní problém propojení různorodých telekomunikačních sítí a umožnil plynulou komunikaci mezi mobilními buněčnými systémy a globální infrastrukturou PSTN. Historicky, s nástupem mobilních sítí (počínaje GSM ve 2G), vznikla potřeba rozhraní s existujícími pevnými sítěmi, aby účastníci mohli volat na jakýkoli telefon na světě. Bez standardizovaného POI by operátoři čelili problémům s interoperabilitou, což by vedlo k fragmentaci služeb a zvýšeným nákladům. Motivací pro definici POI ve standardech 3GPP, počínaje Release 99, bylo stanovit jednotné technické a provozní požadavky na propojení, které zajistí spolehlivé směrování hovorů, signalizaci a účtování napříč síťovými hranicemi. Řeší omezení proprietárních rozhraní tím, že poskytuje společný rámec podporující hlasové služby, SMS a doplňkové služby, což usnadňuje konkurenci a dodržování regulatorních požadavků. Jak se sítě vyvíjely směrem k paketovým technologiím jako LTE a 5G, POI se přizpůsobilo, aby zvládalo propojení na bázi IP při zachování zpětné kompatibility s legacy PSTN, čímž řeší výzvu přechodu z okruhově přepínaných na plně IP sítě. POI také umožňuje kritické služby jako tísňová volání (např. 911, 112) tím, že poskytuje bránu k místům příjmu tísňových hovorů, a podporuje funkce zákonného odposlechu a bezpečnosti podle specifikací 3GPP. Standardizací POI 3GPP podporuje globální roaming a interoperabilitu služeb, což je klíčové pro růst telekomunikačního ekosystému a uživatelský zážitek.

## Klíčové vlastnosti

- Demarkační bod mezi mobilní jádrovou sítí a PSTN/externími sítěmi
- Podpora signalizačních protokolů jako SS7 a SIP
- Konverze médií mezi paketově přepínanými a okruhově přepínanými formáty
- Interoperabilita pro hlasové služby, SMS a tísňové volání
- Soulad s regulatorními požadavky a číslovacími plány
- Vývoj pro podporu architektur IMS a 5G jádrové sítě

## Související pojmy

- [PSTN – Public Switched Telecommunications Network](/mobilnisite/slovnik/pstn/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MGW – Media Gateway](/mobilnisite/slovnik/mgw/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.115** (Rel-19) — 3GPP TS 26115: Echo Control Requirements
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.261** (Rel-19) — Electro-acoustic specs for immersive terminals
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 43.050** (Rel-19) — GSM Transmission Planning for Speech Services

---

📖 **Anglický originál a plná specifikace:** [POI na 3GPP Explorer](https://3gpp-explorer.com/glossary/poi/)
