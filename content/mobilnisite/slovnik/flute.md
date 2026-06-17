---
slug: "flute"
url: "/mobilnisite/slovnik/flute/"
type: "slovnik"
title: "FLUTE – File Delivery over Unidirectional Transport"
date: 2025-01-01
abbr: "FLUTE"
fullName: "File Delivery over Unidirectional Transport"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/flute/"
summary: "File Delivery over Unidirectional Transport (FLUTE) je protokol pro efektivní doručování souborů a dat velkému počtu příjemců přes jednosměrné, vysílací (broadcast) nebo skupinové (multicast) sítě. Je"
---

FLUTE je protokol pro efektivní doručování souborů a dat mnoha příjemcům přes jednosměrné, vysílací (broadcast) nebo skupinové (multicast) sítě, který umožňuje škálovatelné šíření obsahu pro služby jako 3GPP MBMS.

## Popis

File Delivery over Unidirectional Transport (FLUTE) je aplikační protokol standardizovaný v rámci [IETF](/mobilnisite/slovnik/ietf/) a přijatý konsorciem 3GPP pro vysílací/skupinové (broadcast/multicast) doručování souborů. Funguje nad sadou protokolů Asynchronous Layered Coding ([ALC](/mobilnisite/slovnik/alc/)), která sama využívá stavební blok Layered Coding Transport ([LCT](/mobilnisite/slovnik/lct/)) a řízení zahlcení. FLUTE je navržen pro scénáře distribuce typu jeden–mnoho, kde je zpětná vazba od příjemců k odesílateli nepraktická nebo nemožná kvůli jednosměrné povaze přenosu (např. terestriální rozhlasové vysílání). Jeho primární funkcí je spolehlivě doručit jeden nebo více souborů, případně kolekci datových objektů, potenciálně milionům příjemců současně.

Z architektonického hlediska v kontextu 3GPP [MBMS](/mobilnisite/slovnik/mbms/)/eMBMS běží FLUTE mezi Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) a uživatelským zařízením (UE). BM-SC funguje jako odesílatel FLUTE, zatímco UE hostuje příjemce FLUTE. FLUTE zabalí soubory do zdrojových bloků, které jsou následně zakódovány pomocí schémat dopředné korekce chyb ([FEC](/mobilnisite/slovnik/fec/)), jako jsou Raptor nebo RaptorQ, specifikovaných v 3GPP. Toto FEC kódování generuje opravné symboly, které jsou vysílány spolu s původními zdrojovými symboly. To umožňuje příjemcům obnovit ztracené pakety bez nutnosti žádat o opakovaný přenos, což je klíčové pro vysílání, kde zpětné kanály nejsou dostupné nebo jsou neefektivní. FLUTE používá File Delivery Table ([FDT](/mobilnisite/slovnik/fdt/)) k popisu doručovaných souborů, včetně atributů jako typ obsahu, velikost a URI. Samotná FDT je doručována jako FLUTE objekt, čímž poskytuje příjemcům manifest relace.

FLUTE funguje tak, že naváže relaci identifikovanou Transport Session Identifier (TSI). V rámci této relace je každému souboru přidělen Transport Object Identifier (TOI). Odesílatel vysílá zdrojové a opravné symboly pro každý TOI v datových paketech. Příjemce tyto pakety přijímá, shromažďuje symboly a použije FEC dekodér k rekonstrukci původního souboru, jakmile je přijato dostatečné množství symbolů, bez ohledu na to, které konkrétní symboly dorazily. Protokol podporuje doručování na bázi kolotoče (carousel), kde je obsah opakován cyklicky, což umožňuje příjemcům, kteří se připojí pozdě, stále získat všechny soubory. FLUTE je nezávislý na podkladovém transportu; v 3GPP typicky běží nad UDP/IP, které je přenášeno přes eMBMS přenosový kanál prostřednictvím vysílacího rozhraní LTE nebo 5G. Tato kombinace poskytuje efektivní kanál pro hromadné šíření obsahu, odlehčuje provoz v jednobodové (unicast) páteřní síti a umožňuje služby jako systémy veřejného varování, bezdrátové aktualizace (over-the-air) nebo lineární televizní vysílání do mobilních zařízení.

## K čemu slouží

FLUTE byl vyvinut k řešení zásadní výzvy škálovatelného a spolehlivého šíření souborů přes vysílací (broadcast) sítě. Tradiční protokoly pro přenos souborů, jako [FTP](/mobilnisite/slovnik/ftp/) nebo HTTP/TCP, spoléhají na potvrzení a opakované přenosy, což vytváří problém zpětnovazební exploze při obsluze milionů uživatelů současně – to je nemožné v čistě vysílacích scénářích, jako je televizní nebo rozhlasový přenos. Před FLUTE a MBMS neměli mobilní operátoři efektivní způsob, jak odeslat stejný velký soubor (např. aktualizaci OS) všem účastníkům bez ochromení jejich jednobodových (unicast) sítí.

Vytvoření protokolu bylo motivováno potřebou jednosměrné, spolehlivé metody doručování obsahu pro nově vznikající vysílací služby. Řeší omezení jednoduchého, nespolehlivého skupinového vysílání (multicast) začleněním vestavěného FEC, které poskytuje spolehlivost bez zpětné vazby. To byl posun paradigmatu. FLUTE také zavedl strukturovaný způsob popisu a doručování více souborů v rámci jedné relace, což bylo zásadní pro komplexní obsah, jako je webová stránka s více komponentami nebo video s přidruženými metadaty. Jeho přijetí konsorciem 3GPP pro MBMS umožnilo řadu vysílacích služeb, které by jinak byly neproveditelné, a proměnilo mobilní síť z čistě bodového systému na hybridní, schopný efektivní komunikace typu bod–mnoho bodů. To je klíčové pro případy použití vyžadující simultánní doručení, jako jsou nouzová varování, kde musí každé zařízení v oblasti informaci obdržet okamžitě a spolehlivě.

## Klíčové vlastnosti

- Spolehlivé doručování souborů pomocí dopředné korekce chyb (FEC) na aplikační vrstvě
- Podpora doručování více souborů v rámci jedné relace
- Použití tabulky doručování souborů (FDT) pro popis relace
- Přenos na bázi kolotoče (carousel) pro možnost připojení příjemců s opožděním
- Nezávislost protokolu na transportu nižší vrstvy (funguje nad UDP)
- Standardizace pro použití v ekosystémech 3GPP MBMS a eMBMS

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [ALC – Asynchronous Layered Coding](/mobilnisite/slovnik/alc/)

## Definující specifikace

- **TS 23.792** (Rel-16) — MBMS API for Mission Critical Services
- **TS 26.142** (Rel-19) — 3GPP TS 26.142: Dynamic and Interactive Multimedia Scenes (DIMS)
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.827** (Rel-12) — IMS-based Streaming & Download Delivery Enhancements
- **TS 26.848** (Rel-12) — Enhanced MBMS for DASH over broadcast/unicast
- **TS 26.849** (Rel-12) — MBMS Operation on Demand (MooD)
- **TS 26.850** (Rel-16) — Massive File Delivery for IoT Devices
- **TS 26.851** (Rel-11) — Enhancements to Multimedia (EMM) for PSS, MMS, MBMS
- **TS 26.852** (Rel-14) — MBMS user service profiles, APIs and transport enabler study
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [FLUTE na 3GPP Explorer](https://3gpp-explorer.com/glossary/flute/)
