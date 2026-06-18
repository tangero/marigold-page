---
slug: "mst"
url: "/mobilnisite/slovnik/mst/"
type: "slovnik"
title: "MST – Mobile Service Transport"
date: 2025-01-01
abbr: "MST"
fullName: "Mobile Service Transport"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mst/"
summary: "MST je protokolový rámec definovaný v 3GPP pro přenos signalizace a dat specifických pro mobilní služby po IP sítích. Poskytuje standardizovaný mechanismus pro komunikaci na aplikační vrstvě mezi síťo"
---

MST je protokolový rámec 3GPP pro přenos signalizace a dat specifických pro mobilní služby po IP sítích, který umožňuje standardizovanou komunikaci na aplikační vrstvě mezi síťovými prvky.

## Popis

Mobile Service Transport (MST) je klíčový protokolový rámec specifikovaný v rámci architektury 3GPP, primárně dokumentovaný v TS 29.205. Definuje transportní mechanismy pro služební signalizaci a data a usnadňuje komunikaci mezi různými entitami aplikační vrstvy v mobilní síti. V jádru není MST jediným protokolem, ale rámcem, který využívá stávající IP transportní protokoly, přičemž často specifikuje, jak používat protokoly jako Stream Control Transmission Protocol ([SCTP](/mobilnisite/slovnik/sctp/)) nebo TCP s konkrétními úpravami pro přenos dat mobilních služeb. Zajišťuje, aby zprávy pro služby jako IP Multimedia Subsystem (IMS) nebo Customised Applications for Mobile network Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)) byly doručovány spolehlivě, ve správném pořadí a s vhodným řízením toku mezi síťovými uzly, jako jsou aplikační servery, Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Service Capability Exposure Function ([SCEF](/mobilnisite/slovnik/scef/)).

Architektura MST zahrnuje definici konkrétních protokolových zásobníků, formátů zpráv a procedur pro navazování a udržování transportních asociací. Například může specifikovat použití SCTP kvůli jeho výhodám v multi-homingu a ochraně proti flooding útokům, což je žádoucí pro kritické signalizační spoje. Rámec podrobně popisuje, jak namapovat služebně specifické aplikační protokoly (např. Diameter pro IMS) na tyto transportní vrstvy, včetně aspektů jako navázání spojení, jeho údržba a procedury ukončení. Pokrývá také zpracování chyb, mechanismy převzetí služeb při selhání a bezpečnostní hlediska na transportní vrstvě, čímž zajišťuje, že podkladový přenosový nosič je robustní a bezpečný.

Role MST je klíčová při přechodu od tradiční signalizace s přepojováním okruhů (jako [SS7](/mobilnisite/slovnik/ss7/)) k paketově přepínaným, plně IP jádrovým sítím. Poskytnutím standardizovaného transportního rámce umožňuje různým síťovým prvkům od různých dodavatelů bezproblémovou interoperabilitu na aplikační vrstvě. Tím odděluje služební logiku od podrobností podkladového síťového transportu, což podporuje flexibilitu a škálovatelnost. Například aplikační server IMS využívající MST pro transport může komunikovat s [CSCF](/mobilnisite/slovnik/cscf/) bez nutnosti spravovat složitosti samotného IP transportu, protože vrstva MST zajišťuje spolehlivost a správu relací. Tato abstrakce je zásadní pro efektivní nasazení složitých, zisk generujících služeb napříč moderními jádry LTE a 5G.

## K čemu slouží

Vytvoření Mobile Service Transport (MST) bylo motivováno celoprůmyslovým přechodem k plně IP jádrovým sítím ve standardech 3GPP, zejména se zavedením IP Multimedia Subsystem (IMS) a vývojem služeb s přepojováním paketů. Před IP transportem byla signalizace mobilních služeb silně závislá na protokolech s přepojováním okruhů, jako je [SS7](/mobilnisite/slovnik/ss7/) (Signalling System No. 7) a jeho adaptace pro mobilní sítě (např. [MAP](/mobilnisite/slovnik/map/) přes TCAP). Tyto protokoly nebyly původně navrženy pro IP sítě a představovaly výzvy z hlediska škálovatelnosti, flexibility a integrace s internetovými službami. Když operátoři začali nasazovat IMS a další IP služby, naléhavě byla potřeba standardizovaná, spolehlivá a efektivní metoda pro přenos služebně specifické signalizace po IP.

MST byl vyvinut k řešení problému interoperability a spolehlivého transportu pro signalizaci aplikační vrstvy v IP prostředí. Odstraňuje omezení předchozích ad-hoc nebo proprietárních transportních řešení tím, že poskytuje standardizovaný rámec 3GPP. To zajišťuje, že různé síťové prvky od různých dodavatelů mohou komunikovat předvídatelně a spolehlivě, což je zásadní pro rozsáhlá nasazení sítí s více dodavateli. Dále MST podporuje požadovanou kvalitu služeb pro signalizaci, která je citlivá na zpoždění a kritická pro kontinuitu služeb (např. během nastavování hovoru v IMS). Definováním transportních mechanismů, které zahrnují funkce jako spojově orientované relace, řízení toku a obnovu po chybě, poskytuje MST robustnost, kterou dříve nabízelo SS7, ale v rámci IP kontextu.

Historicky jeho zavedení v Release 9 korespondovalo s dozráním IMS a potřebou kohezivní transportní strategie pro aplikační vrstvu při nasazování sítí LTE. Řešil problém, jak přenášet protokoly jako Diameter, SIP nebo jiné služební protokoly spolehlivě mezi distribuovanými síťovými funkcemi. Bez takového standardu by operátoři čelili zvýšené složitosti a nákladům na integraci sítí s více dodavateli, což by potenciálně brzdilo rychlé nasazování nových služeb. MST tedy slouží jako základní enabler pro architekturu založenou na službách, která se později stala klíčovým prvkem 5G, a zajišťuje, že kritická signalizace pro autentizaci, účtování a služební logiku může procházet IP sítěmi se spolehlivostí na úrovni operátorských služeb.

## Klíčové vlastnosti

- Standardizovaný rámec pro přenos signalizace aplikační vrstvy po IP sítích
- Využívá spolehlivé transportní protokoly jako SCTP a TCP
- Definuje procedury pro navázání, údržbu a uvolnění asociace
- Podporuje multi-homing a převzetí služeb při selhání pro zvýšenou spolehlivost
- Poskytuje jasné mapování aplikačních protokolů (např. Diameter) na transportní vrstvu
- Zahrnuje specifikace pro zabezpečení na transportní úrovni

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SCTP – Stream Control Transmission Protocol](/mobilnisite/slovnik/sctp/)

## Definující specifikace

- **TS 29.205** (Rel-19) — BICC Protocols for Bearer-Independent CS Core Network

---

📖 **Anglický originál a plná specifikace:** [MST na 3GPP Explorer](https://3gpp-explorer.com/glossary/mst/)
