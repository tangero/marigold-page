---
slug: "nef"
url: "/mobilnisite/slovnik/nef/"
type: "slovnik"
title: "NEF – Network Exposure Function"
date: 2026-01-01
abbr: "NEF"
fullName: "Network Exposure Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nef/"
summary: "Funkce zpřístupnění sítě (NEF) je funkce jádra sítě 5G, která bezpečně zpřístupňuje síťové schopnosti a události autorizovaným aplikacím a poskytovatelům služeb třetích stran. Působí jako řízená brána"
infografika: "/assets/slovnik/nef.svg"
infografikaAlt: "Schéma architektury 5G sítě se zvýrazněním NEF"
---

NEF je funkce jádra sítě 5G, která bezpečně zpřístupňuje síťové schopnosti a události autorizovaným třetím stranám a funguje jako řízená brána mezi externími API a interními protokoly 3GPP.

## Popis

Funkce zpřístupnění sítě (NEF) je ústřední komponenta v architektuře založené na službách ([SBA](/mobilnisite/slovnik/sba/)) jádra 5G (5GC). Slouží jako standardizovaný, bezpečný a řízený politikami vstupní bod pro externí aplikační funkce ([AF](/mobilnisite/slovnik/af/)) k interakci se sítí 3GPP. Architektonicky je NEF síťová funkce ([NF](/mobilnisite/slovnik/nf/)), která komunikuje s ostatními funkcemi jádra (jako je funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)), jednotná správa dat ([UDM](/mobilnisite/slovnik/udm/)) a síťová úložná funkce ([NRF](/mobilnisite/slovnik/nrf/))) prostřednictvím standardizovaných rozhraní založených na službách (např. Nnef). Její primární role je zprostředkovat mezi externími aplikačními protokoly mimo 3GPP (typicky RESTful [API](/mobilnisite/slovnik/api/) založená na [HTTP](/mobilnisite/slovnik/http/)/JSON) a interními rozhraními založenými na službách specifickými pro 3GPP (např. používající JSON přes HTTP/2). To zahrnuje překlad API, konverzi protokolů a zajištění, že externí požadavky jsou řádně autorizovány, autentizovány a v souladu se síťovými politikami.

Funkčně NEF poskytuje dvě hlavní schopnosti: zpřístupnění a ukládání. Pro zpřístupnění nabízí rozhraní API směrem k aplikacím (northbound API, často definované v 3GPP TS 29.522), které umožňuje AF žádat o síťové služby, jako je ovlivnění směrování provozu (např. pomocí pomocných informací pro výběr síťového řezu (NSSAI)), odběr síťových událostí (jako změna polohy UE, stav připojení nebo selhání komunikace) a přístup k síťovým analýzám. NEF ověřuje tyto požadavky proti profilům účastníků a síťovým politikám vynucovaným PCF. Pro ukládání může NEF bezpečně ukládat strukturovaná data přijatá od AF jako „aplikační data“ v jednotném datovém úložišti (UDR) pro pozdější použití jinými síťovými funkcemi, čímž funguje jako brána pro strukturovaná data.

Interně NEF funguje tak, že přijme požadavek API od AF, autentizuje a autorizuje AF (často ve spolupráci s úložnou funkcí sítě (NRF) a proxy pro ochranu hrany zabezpečení (SEPP)) a poté přeloží tento požadavek do příslušné operace rozhraní založeného na službách směrem k příslušné interní NF. Například požadavek AF na monitorování stavu dosažitelnosti UE by NEF přeložila do požadavku na odběr u funkce správy přístupu a mobility (AMF). NEF pak funguje jako proxy, která přeposílá relevantní oznámení od AMF zpět k AF. Tato abstrakce chrání interní síť 3GPP před přímým externím přístupem, poskytuje vrstvu zabezpečení, stability a řízení a zároveň umožňuje bohaté možnosti služeb.

## K čemu slouží

NEF byla vytvořena, aby řešila zásadní výzvu „uzavřených zahrad“ (walled garden) sítí předchozích generací (2G/3G/4G), kde byly síťové schopnosti z velké části nepřístupné externím subjektům, což brzdilo inovace a diferenciaci služeb. V 4G EPC bylo omezené zpřístupnění poskytováno prostřednictvím funkce zpřístupnění schopností služeb (SCEF), ale bylo často složité a ne plně standardizované pro všechny schopnosti. Vize 5G, která umožňuje vertikální odvětví (např. automobilový průmysl, IoT, výroba) a nové obchodní modely, vyžadovala robustnější, škálovatelnější a programovatelnější rámec pro zpřístupnění.

Jejím primárním účelem je řešit problém bezpečného a řízeného otevření sítě. Umožňuje mobilním síťovým operátorům (MNO) zpeněžit jejich síťová aktiva tím, že nabízejí schopnosti jako řízení QoS, lokalizační služby a informace o stavu sítě podnikovým partnerům a vývojářům třetích stran prostřednictvím dobře definovaných API. To umožňuje vytváření služeb na míru, jako je vylepšené mobilní širokopásmové připojení se zaručenými přenosovými rychlostmi pro poskytovatele videa, komunikace s nízkou latencí pro cloudové hraní nebo spolehlivé řezy sítě pro průmyslové IoT. Dále NEF řeší obavy o zabezpečení a soukromí tím, že centralizuje všechny externí interakce a zajišťuje, že zpřístupnění je řízeno politikami definovanými operátorem, souhlasem uživatele (kde je to aplikovatelné) a regulačními požadavky, čímž zabraňuje neoprávněnému přístupu k citlivým síťovým datům a řídicím funkcím.

## Klíčové vlastnosti

- Bezpečné rozhraní API směrem k aplikacím (northbound API, např. N33) pro aplikační funkce (AF) třetích stran
- Překlad protokolů mezi externími RESTful API a interními rozhraními 3GPP založenými na službách
- Vynucování politik a autorizace pro externí požadavky API prostřednictvím interakce s PCF
- Správa odběru a oznámení pro síťové události (např. poloha UE, stav připojení)
- Schopnost ukládání strukturovaných dat, funguje jako frontend k jednotnému datovému úložišti (UDR)
- Zpřístupnění síťových schopností včetně ovlivnění provozu, řízení QoS a síťových analýz

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.482** (Rel-20) — AIML Enablement Service Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.764** (Rel-17) — Study on V2X Application Layer Enhancements
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.542** (Rel-19) — SEAL Notification Management Protocol
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- … a dalších 72 specifikací

---

📖 **Anglický originál a plná specifikace:** [NEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/nef/)
