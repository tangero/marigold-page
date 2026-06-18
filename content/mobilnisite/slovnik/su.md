---
slug: "su"
url: "/mobilnisite/slovnik/su/"
type: "slovnik"
title: "SU – Spectrum Utilization"
date: 2025-01-01
abbr: "SU"
fullName: "Spectrum Utilization"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/su/"
summary: "Metrika výkonu a optimalizační cíl pro vyhodnocení, jak efektivně rádiová přístupová síť využívá své přidělené frekvenční spektrum. Zahrnuje techniky jako je agregace nosných, sdílení spektra a dynami"
---

SU je metrika výkonu a optimalizační cíl sloužící k vyhodnocení, jak efektivně rádiová síť využívá přidělený frekvenční spektrum k maximalizaci datové propustnosti a uživatelské kapacity.

## Popis

Využití spektra (SU) v 3GPP odkazuje na metodologie, metriky a funkce navržené k maximalizaci efektivity a účinnosti využití přiděleného rádiového frekčního spektra. Nejde o jeden protokol, ale o široký koncept hodnocený pomocí klíčových ukazatelů výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako je spektrální účinnost (bity/s/Hz), využití šířky pásma a propustnost na jednotku šířky pásma. Architektura pro SU pokrývá celou RAN a zahrnuje techniky fyzické vrstvy, plánování řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a algoritmy správy rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)) v gNB (5G) nebo [eNB](/mobilnisite/slovnik/enb/) (4G).

Jak to funguje, zahrnuje vícevrstvý přístup. Na fyzické vrstvě pokročilé modulace (např. 256QAM, 1024QAM) a kódovací schémata zabalí více bitů na symbol. Víceanténní technologie jako [MIMO](/mobilnisite/slovnik/mimo/) a beamforming zvyšují počet prostorových vrstev, čímž efektivně násobí datový tok ve stejném pásmu. Agregace nosných ([CA](/mobilnisite/slovnik/ca/)) kombinuje více komponentních nosných ([CC](/mobilnisite/slovnik/cc/)) napříč souvislými nebo nesouvislými pásmy za účelem vytvoření širšího virtuálního kanálu, což přímo zvyšuje špičkové uživatelské datové rychlosti. V časové doméně dynamické plánování ve vrstvě MAC zajišťuje, že rádiové prostředky (bloky zdrojů) jsou přidělovány uživatelům s nejlepšími okamžitými podmínkami kanálu (proporcionálně spravedlivé plánování), a maximalizuje tak propustnost buňky.

Klíčové komponenty umožňující vysoké SU zahrnují koncepty systému přístupu ke spektru ([SAS](/mobilnisite/slovnik/sas/)) pro sdílené spektrum (např. CBRS), licencovaný přístup s podporou (LAA), který využívá nelicencovaná pásma k doplnění licencovaných nosných, a dynamické sdílení spektra (DSS), které umožňuje koexistenci 4G a 5G na stejné nosné. Dále funkce jako adaptace části šířky pásma (BWP) v 5G NR umožňují uživatelskému zařízení (UE) pracovat pouze s částí celkové šířky pásma buňky, čímž šetří energii a umožňují efektivnější multiplexování různorodých zařízení. Síťové segmenty (network slicing) také přispívají k SU tím, že zajišťují logické rozdělení spektrálních prostředků a jejich garance pro konkrétní typy služeb (např. massive IoT vs. enhanced mobile broadband).

## K čemu slouží

Využití spektra jako zaměřený koncept získalo na významu kvůli rostoucímu nedostatku a ceně nového rádiového spektra. S exponenciálním růstem mobilního datového provozu potřebovali operátoři vytěžit maximální hodnotu ze svých stávajících licencovaných pásem a najít inovativní způsoby přístupu k novému spektru (sdílenému, nelicencovanému). Účelem optimalizace SU je dosáhnout vyšší kapacity sítě, lepších uživatelských datových rychlostí a podpory více připojených zařízení bez nutnosti proporcionálně získávat větší šířku pásma, což je často politicky a ekonomicky náročné.

Řeší omezení statického přidělování spektra a jednoduchých přístupových schémat. Rané buněčné systémy měly pevně přiřazené kanály a méně efektivní modulaci. Vývoj řízený SU zavedl adaptivní techniky reagující na reálné zatížení sítě a podmínky kanálu. Například agregace nosných vyřešila problém fragmentovaných spektrálních držeb operátorů tím, že jim umožnila kombinovat různorodá pásma. Dynamické sdílení spektra je přímým řešením problému migrace z 4G na 5G, neboť umožňuje efektivní opětovné využití stávajícího LTE spektra pro nasazení NR bez potřeby vyhrazené, čisté nosné.

Motivace je zásadně ekonomická a technická: snížit náklady na přenesený bit a splnit rostoucí výkonnostní cíle nových vydání 3GPP. Jak se sítě vyvíjely z hlasově orientovaných na platformy širokopásmových dat, stala se spektrální účinnost primární metrikou technologického pokroku. Funkce SU jsou klíčové pro dosažení cílů 5G, jako jsou víceGbps špičkové rychlosti a masivní hustota připojení, v rámci praktických spektrálních omezení.

## Klíčové vlastnosti

- Zahrnuje spektrální účinnost (bity/s/Hz) jako klíčový KPI
- Umožněno agregací nosných napříč více kmitočtovými pásmy
- Využívá pokročilé anténní systémy (MIMO, beamforming) pro prostorový multiplex
- Používá dynamické plánování a adaptaci spojení pro zisk z více uživatelů
- Podporuje techniky sdílení spektra (DSS, LAA, CBRS)
- Využívá adaptaci šířky pásma (např. části šířky pásma v 5G) pro efektivitu

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TR 38.820** (Rel-16) — NR; 7-24 GHz Frequency Range Study
- **TR 38.838** (Rel-17) — Study on XR Evaluations for NR

---

📖 **Anglický originál a plná specifikace:** [SU na 3GPP Explorer](https://3gpp-explorer.com/glossary/su/)
