---
slug: "ert"
url: "/mobilnisite/slovnik/ert/"
type: "slovnik"
title: "ERT – Expected Residual Time"
date: 2025-01-01
abbr: "ERT"
fullName: "Expected Residual Time"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ert/"
summary: "Prediktivní metrika používaná při multimediálním streamování, zejména u Dynamic Adaptive Streaming over HTTP (DASH), k odhadu zbývající doby přehrání mediálního obsahu v bufferu klienta. Umožňuje inte"
---

ERT je prediktivní metrika používaná při multimediálním streamování k odhadu zbývající doby přehrání média v bufferu klienta, což umožňuje adaptační logice zabránit jeho vyprázdnění a udržet plynulé přehrávání.

## Popis

Expected Residual Time (ERT) je parametr vypočítávaný na straně klienta v kontextu specifikací Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)) od 3GPP. Představuje odhad v sekundách, jak dlouho aktuálně zabufferovaná mediální data udrží přehrávání, než se buffer vyprázdní, za předpokladu konstantní rychlosti spotřeby. ERT není prostým měřením obsazenosti bufferu v bajtech; jde o časovou projekci, která zohledňuje doby přehrání mediálních segmentů již stažených a uložených v bufferu. Tento výpočet průběžně provádí adaptační engine DASH klienta.

Technický výpočet ERT zahrnuje, že klient udržuje model svého přehrávacího bufferu. Jak jsou mediální segmenty stahovány, jsou umisťovány do tohoto bufferu, přičemž každý segment má známou dobu přehrání (např. 2 sekundy, 4 sekundy). ERT je součet dob přehrání všech kompletních, přehratelných segmentů aktuálně přítomných v bufferu, mínus jakýkoli mediální čas, který již byl spotřebován ze segmentu právě přehrávaného. Pokročilé implementace mohou také zohledňovat částečně stažené segmenty nebo používat vážené průměrování pro vyhlazení odhadů. Klient používá tuto hodnotu ERT jako klíčový vstup pro svůj algoritmus adaptace přenosové rychlosti.

Role ERT je klíčová pro správu Quality of Experience ([QoE](/mobilnisite/slovnik/qoe/)) u adaptivního streamování. Primárním cílem DASH klienta je vybrat nejvhodnější reprezentaci (přenosovou rychlost/kvalitu) pro další segment ke stažení. Musí vyvážit kvalitu (vyšší přenosovou rychlost) s rizikem vyprázdnění bufferu (přehrávání se zastaví). Vysoká hodnota ERT indikuje zdravý buffer, což klientovi umožňuje potenciálně požadovat segment vyšší kvality. Nízká nebo rychle klesající hodnota ERT signalizuje bezprostřední riziko vyprázdnění bufferu, což vede klienta k proaktivnímu přepnutí na reprezentaci s nižší přenosovou rychlostí, aby byla doba stažení dalšího segmentu kratší než zbývající doba bufferu, a tím se zabránilo přerušení přehrávání.

## K čemu slouží

ERT byl zaveden k řešení zásadní výzvy v adaptivním streamování: k činění inteligentních, dopředně hledících rozhodnutí o přenosové rychlosti na základě stavu bufferu, namísto pouhé reakce na minulé nebo okamžité síťové podmínky. Jednoduché metriky jako okamžitá propustnost nebo aktuální úroveň bufferu v bajtech mohou být zavádějící a vést k oscilacím kvality nebo neočekávaným přerušením přehrávání. Například buffer může obsahovat mnoho bajtů segmentu s nízkou přenosovou rychlostí (dlouhá doba přehrání) nebo málo bajtů segmentu s vysokou přenosovou rychlostí (krátká doba přehrání) a samotný počet bajtů neodhaluje skutečnou bezpečnostní rezervu pro přehrávání.

Vytvoření ERT bylo motivováno potřebou standardizovaného, přesného prediktoru kontinuity přehrávání. Poskytuje společný jazyk a metriku pro optimalizační algoritmy [QoE](/mobilnisite/slovnik/qoe/), a to jak na straně klienta, tak pro síťově asistované streamování (např. v 5G Media Streaming). Odhadem času do vyčerpání bufferu může klient činit stabilnější a optimálnější adaptační rozhodnutí. To je obzvláště kritické v mobilním prostředí, kde může být šířka pásma sítě vysoce proměnlivá a nepředvídatelná.

Řešení problému predikce bufferu pomocí ERT umožňuje plynulejší přehrávání videa, vyšší průměrné přenosové rychlosti bez zvýšení počtu přerušení a celkově lepší uživatelský zážitek. Je to klíčový faktor pro spolehlivé doručování vysoce kvalitních streamovacích služeb přes mobilní sítě, což je primární případ užití pro 4G a 5G. Jeho specifikace v rámci standardů 3GPP zajišťuje interoperabilitu a konzistentní výkon napříč různými implementacemi zařízení a serverů.

## Klíčové vlastnosti

- Časový odhad zbývající doby přehrání v bufferu klienta
- Klíčový vstup pro adaptivní logiku přenosové rychlosti (ABR) DASH klienta
- Napomáhá předcházet událostem vyprázdnění bufferu (přerušení přehrávání)
- Umožňuje proaktivní přepínání kvality na základě budoucího stavu bufferu
- Vypočítává se z dob přehrání zabufferovaných mediálních segmentů
- Standardizovaná metrika pro reportování QoE a síťově asistované streamování

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.852** (Rel-14) — MBMS user service profiles, APIs and transport enabler study
- **TR 26.946** (Rel-19) — MBMS User Services Overview

---

📖 **Anglický originál a plná specifikace:** [ERT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ert/)
