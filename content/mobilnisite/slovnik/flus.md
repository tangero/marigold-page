---
slug: "flus"
url: "/mobilnisite/slovnik/flus/"
type: "slovnik"
title: "FLUS – Framework for Live Uplink Streaming"
date: 2025-01-01
abbr: "FLUS"
fullName: "Framework for Live Uplink Streaming"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/flus/"
summary: "Framework for Live Uplink Streaming (FLUS) je služební enabler 3GPP, který standardizuje přenos živých médií (audio/video) z uživatelského zařízení do síťové aplikace nebo poskytovatele obsahu. Poskyt"
---

FLUS je služební enabler 3GPP, který standardizuje přenos živých médií (uplink) z uživatelského zařízení do síťové aplikace a poskytuje mechanismy pro řízení relace, ingestování dat a správu kvality.

## Popis

Framework for Live Uplink Streaming (FLUS) je komplexní soubor specifikací 3GPP navržený k usnadnění efektivního, spolehlivého a kvalitního živého streamování médií z uživatelského zařízení (UE) na vzdálený mediální server. Definuje architekturu klient-server, kde UE funguje jako zdroj médií (FLUS Client) a síťová aplikační funkce jako příjemce médií (FLUS Server). Tento framework zahrnuje protokoly a procedury pro vyjednávání relace, adaptaci přenosu médií a síťovou expozici za účelem optimalizace streamování v proměnných podmínkách mobilního rádiového rozhraní.

Z architektonického hlediska FLUS interaguje s několika komponentami 5G systému. FLUS Client sídlí na UE, zatímco FLUS Server je typicky součástí aplikační funkce ([AF](/mobilnisite/slovnik/af/)) v 5G Core. Framework využívá Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) nebo přímo rozhraní s Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) k vyžádání specifického QoS zacházení pro uplinkový mediální tok. To umožňuje službě FLUS požádat o zřízení vyhrazeného QoS toku se zaručeným přenosovým tokem, prioritou a charakteristikami ztrátovosti vhodnými pro přenos videa v reálném čase. Mezi klíčové procedury patří zjišťování schopností, kde si UE a server vyměňují informace o podporovaných kodecích a funkcích FLUS; navázání relace, kde jsou vyjednány parametry streamování; a řízení médií, které může zahrnovat příkazy ze serveru ke klientovi k úpravě datového toku, rozlišení nebo jiných kódovacích parametrů na základě zpětné vazby ze sítě.

FLUS funguje tak, že mezi FLUS klientem a serverem naváže řídicí spojení (např. přes [HTTP](/mobilnisite/slovnik/http/)/2) pro správu relace. Samotná média jsou následně přenášena přes datový tok v uživatelské rovině, typicky pomocí [RTP](/mobilnisite/slovnik/rtp/) přes [UDP](/mobilnisite/slovnik/udp/)/IP. Základní inovací FLUS je jeho integrace s možnostmi 5G sítě. FLUS Server může vyvolat 5G síťová [API](/mobilnisite/slovnik/api/), aby získal analytické údaje o rádiových podmínkách UE (např. očekávaná propustnost, latence), a může následně ovlivnit zacházení sítě s mediálním tokem prostřednictvím QoS řízení politik. Dále FLUS definuje efektivní protokoly pro ingestování médií vhodné pro živé streamování, podporující mechanismy jako vkládání časované metadat, synchronizaci a redundanci pro zvýšení odolnosti proti ztrátě paketů. Tento end-to-edge framework zajišťuje optimalizaci živého video přenosu od snímače kamery přes rádiovou přístupovou síť až po síť pro doručování obsahu, což umožňuje vysílání živých přenosů z mobilních zařízení ve vysílací kvalitě.

## K čemu slouží

FLUS byl vytvořen k uspokojení rostoucí poptávky trhu po kvalitním a spolehlivém živém streamování videa z mobilních zařízení, což je služba popularizovaná platformami sociálních médií a tvůrci obsahu. Před FLUS používaly aplikace pro živé streamování proprietární řešení typu over-the-top ([OTT](/mobilnisite/slovnik/ott/)), která nebyla integrována s mobilní sítí. Tato řešení se potýkala s nepředvídatelnými podmínkami mobilní sítě, což vedlo ke špatné kvalitě videa, bufferingu a přerušovaným přenosům. Nemohla využívat síťovou inteligenci ani žádat o prioritní prostředky, což mělo za následek podprůměrný uživatelský zážitek, zejména v přeplněných oblastech nebo na okraji buňky.

Hlavním problémem, který FLUS řeší, je absence standardizace a síťového povědomí pro uplinkové streamování. Vytvořením standardizovaného frameworku umožňuje interoperabilitu mezi zařízeními, sítěmi a aplikačními servery od různých dodavatelů. Co je důležitější, umožňuje streamovací aplikaci komunikovat své požadavky 5G síti, což umožňuje síťově asistovanou optimalizaci kvality. Tím se řeší klíčová omezení: 1) Neefektivní reaktivní adaptace, kdy aplikace reaguje pouze na pozorovanou kongesci, často příliš pozdě. 2) Neschopnost garantovat prostředky, což vede k soupeření s jiným provozem na pozadí. 3) Nedostatek rádiové analytiky pro proaktivní úpravu kódovacích parametrů. FLUS poskytuje rozhraní pro síťovou asistenci aplikaci, čímž připravuje cestu pro deterministicky kvalitní živé vysílání, což je kritické pro profesionální případy užití, jako je zpravodajství, produkce živých sportovních přenosů nebo komunikace pro veřejnou bezpečnost.

## Klíčové vlastnosti

- Standardizovaný protokol mezi UE a serverem pro řízení relace živého streamování
- Těsná integrace s 5G síťovými API pro QoS a analytiku
- Podpora dynamické adaptace médií na základě síťových podmínek
- Efektivní protokoly pro ingestování médií s podporou časované metadat
- Mechanismy pro redundanci a odolnost proti chybám
- Zjišťování a vyjednávání mediálních kodeků a možností streamování

## Související pojmy

- [5GS – 5G System](/mobilnisite/slovnik/5gs/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [AF – Authentication Framework](/mobilnisite/slovnik/af/)

## Definující specifikace

- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 26.238** (Rel-19) — Framework for Live Uplink Streaming (FLUS)
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TR 26.862** (Rel-17) — Immersive Teleconferencing & Telepresence for Remote Terminals
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.939** (Rel-19) — Framework for Live Uplink Streaming (FLUS)
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3

---

📖 **Anglický originál a plná specifikace:** [FLUS na 3GPP Explorer](https://3gpp-explorer.com/glossary/flus/)
