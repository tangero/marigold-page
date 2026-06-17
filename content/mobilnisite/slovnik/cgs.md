---
slug: "cgs"
url: "/mobilnisite/slovnik/cgs/"
type: "slovnik"
title: "CGS – Coarse Grain Scalability"
date: 2025-01-01
abbr: "CGS"
fullName: "Coarse Grain Scalability"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cgs/"
summary: "CGS je funkce škálovatelnosti při kódování videa umožňující efektivní adaptaci video streamů na proměnlivé síťové podmínky a možnosti zařízení. Umožňuje vylepšit základní vrstvu o další kvalitativní v"
---

CGS je funkce škálovatelnosti při kódování videa, která umožňuje efektivní adaptaci datového toku vylepšením základní vrstvy o kvalitativní vrstvy pro flexibilní úpravy datového toku a rozlišení.

## Popis

Coarse Grain Scalability (CGS) je vrstvená technika kódování videa standardizovaná v rámci architektury 3GPP Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), primárně specifikovaná v TS 26.904. Funguje tak, že strukturová video stream do více vrstev: povinné základní vrstvy a jedné či více vylepšujících vrstev. Základní vrstva poskytuje video základní kvality při nižším datovém toku, zatímco každá následná vylepšující vrstva při přidání přírůstkově zlepšuje kvalitu videa, rozlišení nebo snímkovou frekvenci. Tento vrstvený přístup je základním principem škálovatelného kódování videa (SVC), profilu standardu H.264/[AVC](/mobilnisite/slovnik/avc/), kde CGS představuje jednu z metod pro dosažení prostorové nebo kvalitativní škálovatelnosti.

Z architektonického hlediska je CGS implementována ve video enkodéru a dekodéru. Enkodér vytváří datový tok, ve kterém vylepšující vrstvy přímo závisí na základní vrstvě nebo nižších vylepšujících vrstvách, nikoli však na všech předchozích datech, což zjednodušuje proces dekódování. V síti lze během přenosu vrstvy selektivně přidávat nebo vypouštět na základě aktuálních síťových podmínek, možností zařízení nebo úrovně předplatného uživatele. Například v přetížené buňce může síťový prvek, jako je broadcast multicast service center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), vysílat pouze základní vrstvu, aby zajistil základní kontinuitu služby, zatímco v dobře zásobené oblasti může přidat vylepšující vrstvy pro doručení obsahu ve vysokém rozlišení.

Mezi klíčové součásti patří SVC enkodér, který generuje CGS vrstvy; transportní mechanismy, které tyto vrstvy paketizují a doručují, často s využitím RTP/UDP/IP; a klientský dekodér, který rekonstruuje video z přijatých vrstev. BM-SC hraje klíčovou roli v řízení distribuce, případně provádí filtrování vrstev nebo transkódování. Úkolem CGS je poskytnout robustní, přizpůsobivý mechanismus pro doručování videa, zejména pro broadcastové a multicastové služby, kde jediný stream musí obsloužit různorodé přijímače zažívající rozdílné kanálové podmínky.

Z technického pohledu CGS funguje aplikací offsetů kvantizačního parametru (QP) mezi vrstvami. Základní vrstva je zakódována s určitým QP a vylepšující vrstvy jsou kódovány s jemnější kvantizací (menší QP), čímž přidávají detail. To se liší od Medium Grain Scalability ([MGS](/mobilnisite/slovnik/mgs/)), která nabízí jemnější kvalitativní úpravy pomocí kódování bitových rovin. CGS vrstvy jsou typicky větší a poskytují hrubší kroky ve zlepšení kvality, což je efektivní pro scénáře, kde jsou variace v přenosové kapacitě významné, ale ne extrémně jemnozrnné. Pro dekódování je nutná přítomnost všech nižších vrstev; vylepšující vrstvu nelze dekódovat bez její podkladové základní vrstvy, což zajišťuje integritu závislostí.

Při provozu systému CGS umožňuje dynamickou adaptaci bez nutnosti úplného překódování. Síťové uzly mohou zkrátit datový tok vyřazením paketů vylepšující vrstvy, čímž okamžitě sníží datový tok. To je zásadní pro MBMS, jako je evolved Multimedia Broadcast Multicast Service (eMBMS), kde pomáhá řídit alokaci rádiových prostředků mezi více uživateli. Díky podpoře proměnlivých úrovní kvality CGS zlepšuje uživatelský zážitek, efektivitu sítě a flexibilitu služeb a tvoří tak základní technologii pro adaptivní streamování v mobilním prostředí.

## K čemu slouží

CGS byla vyvinuta k řešení výzev spojených s doručováním video obsahu přes mobilní sítě, které se vyznačují heterogenními zařízeními a kolísající přenosovou kapacitou. Před škálovatelným kódováním videa video streamování často používalo jednovrstvé kodeky jako H.264/[AVC](/mobilnisite/slovnik/avc/), které vyžadovaly samostatná kódování (transkódování) pro různé úrovně kvality nebo síťové podmínky. Tento přístup byl neefektivní, zvyšoval náklady na úložiště, výpočetní režii a latenci, zejména pro broadcastové služby, kde bylo nutné současně spravovat více variant datového toku. CGS jako součást SVC představila elegantnější řešení tím, že umožnila dynamickou adaptaci jediného zakódovaného streamu, čímž snížila složitost a zlepšila škálovatelnost.

Primární motivací pro CGS byl růst spotřeby mobilního videa a potřeba efektivních multicastových/broadcastových služeb v sítích 3GPP. Ve verzi Release 10, s vylepšeními [MBMS](/mobilnisite/slovnik/mbms/) a zavedením eMBMS v LTE, vzrostla poptávka po kódování videa, které by mohlo plynule akomodovat různé možnosti přijímačů – od smartphonů s vysokým rozlišením displeje po jednodušší zařízení s omezeným výpočetním výkonem – a různorodé síťové podmínky, jako jsou uživatelé na okraji buňky versus v jejím středu. CGS poskytla standardizovanou metodu, jak toho dosáhnout, což umožnilo operátorům optimalizovat využití přenosové kapacity při zachování kvality služby.

Řešením těchto problémů CGS usnadnila nasazení služeb jako mobilní TV, živé streamování a aktualizace softwaru přes multicast. Odstranila omezení předchozích neškálovatelných přístupů tím, že umožnila plynulé snížení kvality při špatných signálových podmínkách a vylepšení kvality při dobrých podmínkách, a to vše z jediného zdrojového streamu. To nejen zlepšilo uživatelský zážitek, ale také snížilo provozní náklady pro síťové operátory, čímž učinilo doručování videa udržitelnějším a flexibilnějším v se vyvíjejícím ekosystému 3GPP.

## Klíčové vlastnosti

- Vrstvené kódování videa se základní a vylepšující vrstvou
- Podpora adaptací kvalitativní a prostorové škálovatelnosti
- Dynamická úprava datového toku přidáním/vypuštěním vrstev
- Efektivní jednoproudové kódování pro více úrovní kvality
- Kompatibilita s architekturami 3GPP MBMS a eMBMS
- Zjednodušená struktura závislostí pro dekódování ve srovnání s jemnozrnnou škálovatelností

## Definující specifikace

- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS

---

📖 **Anglický originál a plná specifikace:** [CGS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cgs/)
