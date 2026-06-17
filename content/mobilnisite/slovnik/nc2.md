---
slug: "nc2"
url: "/mobilnisite/slovnik/nc2/"
type: "slovnik"
title: "NC2 – Network Control mode 2"
date: 2025-01-01
abbr: "NC2"
fullName: "Network Control mode 2"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nc2/"
summary: "NC2 je síťový řídicí režim GERAN, ve kterém mobilní stanice provádí měření, ale hlásí je na základě žádostí sítě. Síť vyzývá MS k poskytnutí dat, čímž získává přímou kontrolu nad načasováním a obsahem"
---

NC2 je síťový řídicí režim GERAN, ve kterém mobilní stanice provádí měření, ale hlásí je pouze na vyžádání sítě, což umožňuje přímé síťové řízení načasování a obsahu hlášení.

## Popis

Síťový řídicí režim 2 (NC2) je doplňkový řídicí režim k [NC1](/mobilnisite/slovnik/nc1/), definovaný ve specifikacích 3GPP pro GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network. V NC2 síť ([BSC](/mobilnisite/slovnik/bsc/)) nakonfiguruje mobilní stanici parametry, které detailně určují, co má měřit, například konkrétní [ARFCN](/mobilnisite/slovnik/arfcn/) sousedních buněk a měřené veličiny. Na rozdíl od NC1 se však [MS](/mobilnisite/slovnik/ms/) nerozhoduje autonomně, kdy odeslat hlášení. Místo toho průběžně provádí měření a ukládá výsledky. Síť explicitně vyžádá hlášení o měření odesláním příkazu k vyzvání (polling) MS. Po přijetí této žádosti MS sestaví hlášení obsahující nejnovější měřená data a odešle je síti. To poskytuje síti úplnou a na vyžádání dostupnou informaci o aktuálních rádiových podmínkách, jak je vnímá mobilní stanice.

Architektonický postup zahrnuje počáteční fázi přiřazení, ve které BSC odešle zprávu s informacemi o měření ke konfiguraci MS. Následně fyzická vrstva a protokolové vrstvy MS provádějí průběžná měření. BSC pak může odeslat speciální zprávu k vyzvání, například požadavek na hlášení měření na přidruženém řídicím kanálu. MS odpoví zprávou Measurement Report obsahující data pro obsluhující buňku a seznam nakonfigurovaných sousedních buněk. Tento režim zcela svěřuje iniciativu k hlášení síti, což jí umožňuje shromažďovat data měření v konkrétních okamžicích, například těsně před potenciálním rozhodnutím o předání hovoru nebo pro diagnostiku optimalizace sítě.

Fungování NC2 je klíčové pro scénáře, kdy síť potřebuje přesný snímek rádiových podmínek bez spoléhání se na událostmi spouštěné hlášení MS. Zajišťuje, že síť obdrží komplexní data, když je potřebuje, avšak za cenu dodatečné signalizace na downlinku (vyzvání) a zaručené signalizace na uplinku (hlášení). To jej činí méně efektivním pro neustálý management mobility než NC1, ale vhodnějším pro cílený sběr dat, testování nebo situace, kdy centralizovaný algoritmus sítě vyžaduje přímé, nefiltrované vzorky měření k rozhodnutí.

## K čemu slouží

NC2 byl vyvinut, aby poskytl síti přímý přístup na vyžádání k datům měření mobilní stanice. Jeho primárním účelem je dát síťovým řadičům přesnou kontrolu nad načasováním a obsahem informací o rádiovém prostředí. Tím řeší problém potřeby kompletní sady aktuálních měření pro analytické nebo rozhodovací procesy, které se nemohou spoléhat pouze na událostmi spouštěná hlášení z režimů jako [NC1](/mobilnisite/slovnik/nc1/).

Motivace pro NC2 vychází z plánování sítě, optimalizace a specifických pokročilých algoritmů předání hovoru. Například operátor sítě může použít NC2 k diagnostice problémů s pokrytím vyzýváním konkrétních mobilů v problematické oblasti. Řeší omezení čistě autonomního hlášení [MS](/mobilnisite/slovnik/ms/), kdy síť přijímá data pouze tehdy, když je MS považuje za nezbytná, což může vést k přehlédnutí jemných trendů nebo specifických datových bodů potřebných pro činnosti ladění sítě. NC2 zajišťuje, že se síť může vždy 'zeptat' na aktuální situaci.

Historicky zavedený ve Release 10 je NC2 součástí širšího rámce pro flexibilní řízení měření v [GERAN](/mobilnisite/slovnik/geran/). Představuje síťově-centrický konec spektra řízení, což kontrastuje s autonomním NC1. Tento dvou-režimový přístup umožnil GSM/EDGE sítím podporovat širokou škálu případů užití, od vysoce efektivní rutinní mobility po detailní síťově řízenou diagnostiku, a zajistil tak, že technologie zůstala přizpůsobivá a spravovatelná po celou dobu svého vývoje.

## Klíčové vlastnosti

- Hlášení měření na základě vyzvání sítí
- Mobilní stanice provádí průběžná měření na pozadí
- Síť řídí přesné načasování generování hlášení
- Poskytuje úplné snímky rádiových podmínek na vyžádání
- Konfigurováno prostřednictvím zpráv řízení měření z BSC
- Používá se pro diagnostiku, optimalizaci a specifické scénáře předání hovoru

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [NC1 – Network Control mode 1](/mobilnisite/slovnik/nc1/)

## Definující specifikace

- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [NC2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/nc2/)
