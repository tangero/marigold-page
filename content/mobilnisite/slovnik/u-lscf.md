---
slug: "u-lscf"
url: "/mobilnisite/slovnik/u-lscf/"
type: "slovnik"
title: "U-LSCF – UTRAN Location System Control Function"
date: 2025-01-01
abbr: "U-LSCF"
fullName: "UTRAN Location System Control Function"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/u-lscf/"
summary: "U-LSCF je řídicí funkce v rámci UTRAN, která spravuje lokalizační služby pro uživatelské zařízení. Koordinuje požadavky na určení polohy, komunikuje s jednotkami pro měření polohy a vypočítává zeměpis"
---

U-LSCF je řídicí funkce v UTRAN, která spravuje lokalizační služby koordinací požadavků na určení polohy, spoluprací s měřicími jednotkami a výpočtem zeměpisné polohy uživatelského zařízení.

## Popis

[UTRAN](/mobilnisite/slovnik/utran/) Location System Control Function (U-LSCF) je klíčová logická entita v architektuře UTRAN odpovědná za řízení a správu procedur určování polohy uživatelského zařízení (UE). Funguje jako součást sady funkcí lokalizačních služeb ([LCS](/mobilnisite/slovnik/lcs/)) definovaných 3GPP. U-LSCF působí jako centrální koordinátor pro jakýkoli požadavek na polohu, rozhraním komunikuje jak s jádrem sítě (CN) přes rozhraní Iupc, tak s komponentami rádiové přístupové sítě (RAN). Když je iniciován požadavek na polohu – ať už ze sítě, od samotného UE, nebo od externího klienta – U-LSCF požadavek přijme a určí vhodnou metodu určení polohy, jako je Cell-ID, [OTDOA](/mobilnisite/slovnik/otdoa/) nebo [U-TDOA](/mobilnisite/slovnik/u-tdoa/), na základě požadované kvality služeb (QoS), schopností UE a stavu sítě.

Architektura U-LSCF je navržena pro integraci v rámci řadiče rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v typickém nasazení UTRAN. Její činnost zahrnuje několik klíčových kroků. Nejprve ověří a autorizuje požadavek na polohu. Poté vydá příkazy příslušným Node B a v případě potřeby jednotkám pro měření polohy ([LMU](/mobilnisite/slovnik/lmu/)), aby provedly požadovaná rádiová měření, jako je časový předstih nebo naměřený časový rozdíl příchodu. U-LSCF shromažďuje tyto surové měřicí reporty z RAN. Pomocí těchto měření a známých zeměpisných souřadnic stanovišť buněk provede U-LSCF výpočet polohy pro odhad zeměpisné šířky a délky UE. Nakonec výsledek naformátuje a doručí odhad polohy zpět žadateli, přičemž zajišťuje soulad s předpisy o ochraně soukromí a bezpečnosti.

Role U-LSCF je klíčová pro oddělení řídicí roviny lokalizačních služeb od uživatelské roviny. Spravuje signalizaci pro relace určování polohy, řeší chybové stavy a může podporovat více souběžných požadavků na polohu. Také komunikuje s funkcí UTRAN Location System Operations Function ([U-LSOF](/mobilnisite/slovnik/u-lsof/)) pro provozní aspekty, jako je správa výkonnosti. Díky centralizaci řídicí logiky umožňuje U-LSCF efektivní využití zdrojů v RAN, zajišťuje konzistentní implementaci 3GPP lokalizačních protokolů a poskytuje standardizované rozhraní pro jádro sítě pro vyžádání polohy UE bez nutnosti detailní znalosti rádiové přístupové technologie.

## K čemu slouží

U-LSCF byla vytvořena za účelem standardizace a centralizace řízení funkcionality určování polohy v rámci [UTRAN](/mobilnisite/slovnik/utran/), rádiové přístupové sítě 3G. Před její specifikací byly lokalizační služby často implementovány pomocí proprietárních, dodavatelům specifických řešení, kterým chyběla interoperabilita a konzistentní výkon. Tlak regulačních požadavků, jako je Enhanced 911 (E911) ve Spojených státech a podobné povinnosti lokalizace tísňových volajících po celém světě, si vyžádal spolehlivou, na síti založenou schopnost určování polohy, která by mohla fungovat napříč různým síťovým zařízením od různých výrobců.

Její zavedení vyřešilo problém fragmentovaného řízení lokalizačních služeb poskytnutím dobře definované funkční entity v rámci RNC. To umožnilo centru Gateway Mobile Location Centre (GMLC) v jádru sítě vydávat standardizované požadavky na polohu bez nutnosti starat se o konkrétní rádiová měření nebo výpočty. U-LSCF abstrahuje složitosti rádiového rozhraní a vybírá optimální metodu určení polohy (např. přepnutí na přesnější, ale náročnější metodu jako U-TDOA, pouze když je to potřeba) na základě požadované přesnosti. Tento návrh řeší omezení dřívějších ad-hoc implementací tím, že zajišťuje škálovatelnost, spravovatelnost a schopnost zavádět nové techniky určování polohy v pozdějších vydáních 3GPP bez zásadních architektonických změn.

## Klíčové vlastnosti

- Centralizované řízení a správa procedur určování polohy založených na UTRAN
- Podpora více metod určování polohy definovaných 3GPP včetně Cell-ID, OTDOA a U-TDOA
- Rozhraní s jádrem sítě přes referenční bod Iupc pro požadavek na polohu a její doručení
- Koordinace rádiových měření z Node B a vyhrazených jednotek pro měření polohy (LMU)
- Provádění výpočtu polohy pomocí shromážděných dat z rádiových měření
- Zpracování autorizace, ochrany soukromí a správy chyb pro lokalizační relace

## Související pojmy

- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [U-LSCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/u-lscf/)
