---
slug: "dce"
url: "/mobilnisite/slovnik/dce/"
type: "slovnik"
title: "DCE – Data Circuit-terminating Equipment"
date: 2025-01-01
abbr: "DCE"
fullName: "Data Circuit-terminating Equipment"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dce/"
summary: "DCE je síťové rozhraní, které ukončuje datový okruh a zajišťuje fyzické připojení a převod signálu mezi datovým koncovým zařízením (DTE) a telekomunikační sítí. Je nezbytné pro navázání spolehlivé bod"
---

DCE je síťové rozhraní, které ukončuje datový okruh a zajišťuje fyzické připojení a převod signálu mezi datovým koncovým zařízením (DTE) a telekomunikační sítí.

## Popis

Data Circuit-terminating Equipment (DCE) je funkční jednotka definovaná v rámci specifikací 3GPP, která navazuje, udržuje a ukončuje spojení na síťovém segmentu. Funguje na fyzické vrstvě (vrstva 1) a často i na spojové vrstvě (vrstva 2) referenčního modelu [OSI](/mobilnisite/slovnik/osi/). DCE poskytuje fyzické rozhraní, taktování a převod signálu nezbytný pro to, aby zařízení typu Data Terminal Equipment ([DTE](/mobilnisite/slovnik/dte/)), jako je směrovač nebo terminál, mohlo komunikovat prostřednictvím telekomunikačního okruhu. Slouží jako zprostředkovatel, který přizpůsobuje signály z DTE formátu a elektrickým charakteristikám vyžadovaným přenosovým médiem, například pronajatým vedením nebo okruhově přepínanou síťovou cestou.

V typickém kontextu 3GPP, zejména v dřívějších verzích, je funkčnost DCE spojena s rozhraními pro okruhově přepínané datové služby a určitá propojení s pevnými sítěmi. Například v rámci jádra sítě jsou charakteristiky DCE relevantní pro rozhraní spojující síťové entity s externími datovými sítěmi nebo se starší přenosovou technikou. DCE zajišťuje řádkové kódování, synchronizaci a může provádět postupy detekce a opravy chyb na fyzické vrstvě, aby zajistilo integritu přenášených bitů na spoji. Často je implementováno jako modem, jednotka kanálové služby (CSU) nebo jako integrovaná funkce v síťové přepojovací technice.

Role DCE je definována v protikladu k zařízení Data Terminal Equipment (DTE). DTE je koncové uživatelské zařízení, které data generuje nebo spotřebovává, zatímco DCE je komunikační zařízení, které DTE umožňuje přístup na linku. Jejich interakce se řídí standardizovanými fyzickými rozhraními, jako jsou doporučení řady V nebo řady X od [ITU-T](/mobilnisite/slovnik/itu-t/), která specifikují typy konektorů, přiřazení pinů, elektrické signály a řídicí procedury. V rámci systémové architektury 3GPP specifikace jako TS 48.014 podrobně popisují požadavky na DCE v kontextu rozhraní BSS-MSC pro okruhově přepínaná data, čímž zajišťují interoperabilitu mezi zařízeními mobilní sítě a systémy přenosu po pevných linkách.

Ačkoli jeho význam poklesl s přechodem na paketově přepínané, plně IP sítě v pozdějších verzích 3GPP, koncept DCE zůstává základním prvkem pro pochopení konektivity na fyzické vrstvě a demarkačního bodu mezi zařízeními na straně zákazníka a sítí poskytovatele služeb. Jeho principy podmiňují spolehlivý přenos datových bitů, což je předpokladem pro všechny protokoly a služby vyšších vrstev, a to i v moderních architekturách.

## K čemu slouží

Účelem DCE je poskytnout standardizovanou a spolehlivou metodu pro připojení koncového uživatelského datového koncového zařízení k telekomunikační síti. Řeší základní problém nekompatibility signálů; zařízení [DTE](/mobilnisite/slovnik/dte/) vytváří digitální signály vhodné pro komunikaci na krátkou vzdálenost, ale tyto signály nejsou vhodné pro přenos na velké vzdálenosti po pronajatých vedeních nebo okruhově přepínaných sítích, které mohou používat odlišné úrovně napětí, kódovací schémata nebo vyžadují specifické taktování. DCE funguje jako adaptér, který provádí nezbytný převod signálu, jeho regeneraci a synchronizaci, aby byla data z DTE přenositelná přes fyzickou infrastrukturu sítě.

Historicky byl model DCE/DTE klíčový v éře vyhrazených okruhově přepínaných datových sítí a raných služeb digitálních pronajatých linek. Před rozšířením IP sítí se datová komunikace často opírala o navázání fyzického, koncový-koncový okruhu po dobu trvání relace. DCE poskytovalo jasný demarkační bod, který definoval hranici odpovědnosti zákazníka (DTE) a odpovědnosti síťového operátora (DCE a okruh za ním). Tento model umožnil interoperabilitu mezi zařízeními od různých výrobců díky striktní definici elektrických a procedurálních charakteristik na tomto rozhraní.

Ve vývoji 3GPP byla funkčnost DCE začleněna pro podporu spolupráce s existujícími pevnými datovými sítěmi (jako jsou datové služby PSTN/[ISDN](/mobilnisite/slovnik/isdn/)) a pro přenos okruhově přepínaných uživatelských dat v rámci jádra mobilní sítě. Řešila omezení mobilních zařízení, která nejsou nativně vybavena pro přímé řízení dálkových přenosových linek. Zavedením požadavků na DCE ve standardech jako TS 48.014 zajistilo 3GPP, že síťové prvky mobilní sítě (fungující jako DTE nebo se k němu připojující) mohou spolehlivě komunikovat s přenosovou technikou různých síťových poskytovatelů, což usnadnilo globální roaming a propojení páteřní sítě.

## Klíčové vlastnosti

- Ukončení fyzické vrstvy a převod signálu
- Poskytuje síťové taktování a synchronizaci pro DTE
- Implementuje řádkové kódování a regeneraci signálu
- Definuje síťový demarkační bod pro datový okruh
- Podporuje standardizovaná fyzická rozhraní (např. V.35, X.21)
- Umožňuje konektivitu pro okruhově přepínané datové služby

## Související pojmy

- [DTE – Data Terminal Equipment](/mobilnisite/slovnik/dte/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 48.014** (Rel-19) — Gb Interface Physical Layer Specification

---

📖 **Anglický originál a plná specifikace:** [DCE na 3GPP Explorer](https://3gpp-explorer.com/glossary/dce/)
