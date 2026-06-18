---
slug: "nrsn"
url: "/mobilnisite/slovnik/nrsn/"
type: "slovnik"
title: "NRSN – Network Requested Support Network"
date: 2025-01-01
abbr: "NRSN"
fullName: "Network Requested Support Network"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nrsn/"
summary: "Network Requested Support Network (NRSN) je koncept jádra sítě, kdy síť vyžádá podporu od jiné sítě, například pro roaming nebo služby mezi operátory. Zahrnuje signalizaci mezi sítěmi pro zajištění sl"
---

NRSN je koncept jádra sítě, kdy síť vyžádá podporu od jiné sítě, například pro roaming, zahrnující signalizaci pro zajištění služeb jako autentizace nebo účtování.

## Popis

Network Requested Support Network (NRSN) je funkční koncept v 3GPP jádrových sítích, který umožňuje jedné síti (síti žádající) požádat o pomoc nebo služby od jiné sítě (podpůrné sítě). K tomu typicky dochází ve scénářích jako roaming mezi [PLMN](/mobilnisite/slovnik/plmn/) (Public Land Mobile Network), kdy navštívená síť potřebuje podporu od domovské sítě pro autentizaci, autorizaci a účtování účastníka. Mechanismus je implementován prostřednictvím standardizovaných rozhraní a protokolů, jako je rozhraní Gp mezi uzly GGSN (Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Nodes) v různých PLMN nebo rozhraní N9 v 5G mezi funkcemi [UPF](/mobilnisite/slovnik/upf/) (User Plane Functions). Když se uživatelské zařízení (UE) připojí nebo zahájí relaci v navštívené síti, prvky jádra navštívené sítě (např. [SGSN](/mobilnisite/slovnik/sgsn/) v GPRS nebo [AMF](/mobilnisite/slovnik/amf/) v 5G) mohou odeslat požadavek prvkům domovské sítě (např. [HLR](/mobilnisite/slovnik/hlr/)/[HSS](/mobilnisite/slovnik/hss/) nebo [AUSF](/mobilnisite/slovnik/ausf/)) pro ověření přihlašovacích údajů a získání profilu účastníka. Tento požadavek spustí proceduru NRSN, při které domovská síť poskytne potřebnou podporu, například odešle autentizační vektory nebo pravidla politik. Proces zahrnuje zabezpečenou výměnu signalizačních zpráv, často s využitím protokolů Diameter nebo HTTP/2, pro zajištění integrity a důvěrnosti dat. NRSN se také vztahuje na další podpůrné funkce, jako je zákonné odposlouchávání, koordinace služeb nouzového volání nebo vyjednávání kvality služby (QoS) mezi operátory. Je základním kamenem globální mobility, umožňujícím plynulé poskytování služeb přes administrativní hranice tím, že sítě mohou dynamicky žádat a poskytovat podporu na základě aktuálních potřeb.

## K čemu slouží

Účelem Network Requested Support Network (NRSN) je řešit výzvy interoperability a kontinuity služeb v prostředí více operátorů, zejména pro roaming a spolupráci mezi sítěmi. Před standardizací operátoři spoléhali na bilaterální dohody a proprietární metody podpory, což vedlo k neefektivitě, bezpečnostním rizikům a omezené škálovatelnosti. NRSN byl vytvořen, aby poskytl jednotný, standardizovaný rámec pro sítě k vyžádání a poskytnutí podpůrných služeb, což zajišťuje konzistentní chování napříč různými dodavateli a regiony. Řeší problémy jako autentizace účastníka v navštívených sítích, kde domovská síť musí ověřit přihlašovací údaje bez přímého zásahu uživatele, což umožňuje bezpečný globální roaming. Dále usnadňuje sdílení zdrojů, například když síť potřebuje dodatečnou kapacitu nebo specializované služby od partnerské sítě. Motivace vychází z růstu globálních mobilních služeb, které vyžadují robustní mechanismy pro komunikaci mezi PLMN pro podporu účtování, vynucování politik a dodržování regulatorních požadavků. Zavedením NRSN ve vydání 7 a jeho vývojem v následujících vydáních umožnil 3GPP efektivnější, bezpečnější a škálovatelnější operace mezi operátory, což zlepšuje uživatelský zážitek a spolehlivost sítě.

## Klíčové vlastnosti

- Umožňuje žádosti o podporu mezi PLMN pro roaming a služby
- Používá standardizovaná rozhraní jako Gp a N9 pro signalizaci
- Podporuje autentizaci, autorizaci a účtování mezi sítěmi
- Usnadňuje zabezpečenou signalizaci s protokoly jako Diameter a HTTP/2
- Rozšiřuje se na zákonné odposlouchávání a koordinaci služeb nouzového volání
- Poskytuje dynamické sdílení zdrojů a politik přes hranice operátorů

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1

---

📖 **Anglický originál a plná specifikace:** [NRSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrsn/)
