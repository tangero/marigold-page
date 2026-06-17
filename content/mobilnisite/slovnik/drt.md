---
slug: "drt"
url: "/mobilnisite/slovnik/drt/"
type: "slovnik"
title: "DRT – Delay Reference Time"
date: 2025-01-01
abbr: "DRT"
fullName: "Delay Reference Time"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/drt/"
summary: "Časovací parametr používaný při správě rozhraní Iur mezi RNC v sítích UMTS. Definuje referenční bod pro měření a kompenzaci přenosových zpoždění v transportní síti, aby byla zajištěna přesná synchroni"
---

DRT (Delay Reference Time) je časovací parametr používaný na rozhraní UMTS Iur k definování referenčního bodu pro měření a kompenzaci přenosových zpoždění, aby bylo zajištěno přesné synchronizace procedur, jako je předávání spojení (handover).

## Popis

Delay Reference Time (DRT) je klíčový časovací parametr definovaný ve specifikacích 3GPP pro rozhraní Iur, které spojuje dva řadiče rádiové sítě (RNC) v pozemní rádiové přístupové síti UMTS (UTRAN). Jeho primární funkcí je vytvořit společný časový referenční bod mezi RNC pro přesné měření a správu proměnlivých přenosových zpoždění, která jsou vlastní transportní síti je spojující. To je nezbytné pro časově citlivé koordinační funkce.

Z architektonického hlediska je DRT vyjednáván a nastaven během zřizování logického spojení Iur mezi obsluhujícím RNC (SRNC) a driftovým RNC ([DRNC](/mobilnisite/slovnik/drnc/)). Tento parametr definuje konkrétní časový bod použitý jako základní linie. Oba RNC používají tuto referenci k časovému značkování zpráv a měření skutečného zpoždění transportní sítě pro rámce uživatelských dat a řídicí signalizaci. Naměřená variace zpoždění je následně kompenzována v procedurách, které vyžadují přesné časové sladění, jako je makro-diverzitní kombinování (kdy jsou stejná uživatelská data přijímána prostřednictvím dvou NodeB řízených různými RNC) a mezibuněčné tvrdé předání spojení (inter-RNC hard handover).

Mechanismus funguje tak, že do rámcových protokolů vkládá časové informace. Jeden RNC (typicky SRNC) odešle řídicí rámec označený svým aktuálním časem vzhledem k dohodnutému DRT. Přijímající RNC porovná toto časové razítko se svými vlastními hodinami (také sladěnými s DRT) a vypočítá jednosměrné zpoždění. Toto vypočtené zpoždění je pak použito k úpravě vyrovnávací paměti a plánování. Mezi klíčové komponenty patří samotná hodnota DRT, procedury časového přizpůsobení v rámcových protokolech Iur (jako je [DCH](/mobilnisite/slovnik/dch/) Frame Protocol) a související řídicí signalizace. Jeho role spočívá v abstrakci kolísání latence (jitteru) podkladové transportní sítě, čímž poskytuje algoritmům správy rádiových prostředků RNC stabilnější a předvídatelnější časové prostředí.

## K čemu slouží

DRT byl zaveden, aby vyřešil kritický problém variability zpoždění transportní sítě v architekturách UMTS s více RNC. V raném UMTS vyžadovaly funkce jako měkké předání spojení (makro-diverzita) mezi NodeB patřícími k různým RNC extrémně těsnou synchronizaci datových proudů uživatele, aby mohly být správně kombinovány. Transportní síť (např. IP nebo [ATM](/mobilnisite/slovnik/atm/)) mezi RNC zaváděla nepředvídatelná a proměnná zpoždění, která mohla vážně zhoršit výkon kombinování nebo způsobit selhání předání spojení, pokud s nimi nebylo počítáno.

Jeho vytvoření bylo motivováno potřebou, aby pokročilé rádiové funkce spolehlivě fungovaly přes neideální přenosové spoje (backhaul). Předchozí přístupy, které předpokládaly pevné nebo zanedbatelné zpoždění mezi RNC, byly nedostatečné. DRT poskytuje standardizovanou metodu pro vytvoření společné časové základny a měření skutečných zpoždění, což umožňuje dynamickou kompenzaci. To umožnilo operátorům nasazovat UTRAN flexibilnějším a distribuovaným způsobem, aniž by byli omezeni ultranízkolatencí a vyhrazenými spoji mezi všemi RNC. V podstatě oddělil výkon rádiové části od nedokonalostí transportní sítě, čímž zvýšil spolehlivost sítě a kvalitu služeb během událostí mobility.

## Klíčové vlastnosti

- Vytváří společný časový referenční bod mezi dvěma RNC přes rozhraní Iur
- Umožňuje přesné měření proměnlivého zpoždění transportní sítě
- Podporuje kompenzaci zpoždění pro makro-diverzitní kombinování při mezibuněčném měkkém předání spojení (inter-RNC soft handover)
- Klíčový pro synchronizaci při provádění mezibuněčného tvrdého předání spojení (inter-RNC hard handover)
- Implementován v rámci řídicích procedur rámcového protokolu Iur
- Zlepšuje výkon UTRAN přes neideální přenosové sítě (backhaul)

## Definující specifikace

- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols

---

📖 **Anglický originál a plná specifikace:** [DRT na 3GPP Explorer](https://3gpp-explorer.com/glossary/drt/)
