---
slug: "u-lsadf"
url: "/mobilnisite/slovnik/u-lsadf/"
type: "slovnik"
title: "U-LSADF – UTRAN Location System Assistance Data Function"
date: 2025-01-01
abbr: "U-LSADF"
fullName: "UTRAN Location System Assistance Data Function"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/u-lsadf/"
summary: "Funkce UTRAN, která poskytuje uživatelskému zařízení (UE) asistenční data pro zlepšení přesnosti a rychlosti určování polohy. Dodává informace jako GPS satelitní almanachy, seznamy sousedních buněk ne"
---

U-LSADF je funkce UTRAN, která poskytuje asistenční data pro určování polohy, jako jsou satelitní almanachy nebo časové reference buněk, uživatelskému zařízení (UE) za účelem zlepšení přesnosti a rychlosti určení polohy.

## Popis

U-LSADF ([UTRAN](/mobilnisite/slovnik/utran/) Location System Assistance Data Function) je logická funkce v rámci UTRAN, která typicky sídlí v řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)). Je zodpovědná za generování, správu a doručování asistenčních dat mobilnímu terminálu (UE) pro podporu určování polohy. Asistenční data zahrnují informace, které uživatelskému zařízení pomáhají provádět měření polohy rychleji nebo přesněji.

Během provozu, když je vyžádána lokalizační služba, může základnová síť instruovat UTRAN, aby poskytl asistenční data. U-LSADF shromažďuje relevantní data na základě použité metody určování polohy. Pro Assisted [GPS](/mobilnisite/slovnik/gps/) ([A-GPS](/mobilnisite/slovnik/a-gps/)) to může zahrnovat efemeridy GPS satelitů, data almanachu, přibližnou polohu a časové korekce. Pro [OTDOA](/mobilnisite/slovnik/otdoa/) (Observed Time Difference of Arrival) může poskytnout informace o seznamu sousedních buněk a přesné časové reference. Tato data jsou formátována a odeslána uživatelskému zařízení prostřednictvím přenosové funkce [U-LIRF](/mobilnisite/slovnik/u-lirf/) za použití zpráv [RRC](/mobilnisite/slovnik/rrc/).

Funkce často získává nezpracovaná asistenční data z externích systémů (jako jsou referenční sítě GPS) nebo z interních dat sítě (jako je konfigurace buněk). Z architektonického hlediska je úzce propojena s U-LIRF; U-LSADF připravuje asistenční data a U-LIRF zajišťuje jejich přenos. Mezi klíčové komponenty patří databáze nebo rozhraní pro externí zdroje asistenčních dat, algoritmy pro přizpůsobení dat přibližné poloze uživatelského zařízení a protokoly pro zabalení dat. Její role je klíčová pro metody určování polohy s podporou sítě, protože snižuje spotřebu baterie uživatelského zařízení a zlepšuje dobu a přesnost získání polohy.

## K čemu slouží

U-LSADF byla zavedena za účelem zlepšení výkonu lokalizačních služeb v sítích UMTS, zejména pro metody jako Assisted [GPS](/mobilnisite/slovnik/gps/). Samostatný GPS v mobilních zařízeních mohl trpět dlouhou dobou do prvního určení polohy (TTFF) a špatnou přesností v interiéru. Poskytnutí asistenčních dat ze sítě tyto problémy zmírňuje.

Řešila problém, jak může rádiová přístupová síť aktivně přispět ke zlepšení určování polohy uživatelského zařízení. Dodáním satelitních dat a časových nápověd mohla GPS přijímač uživatelského zařízení začít pracovat rychleji a lépe fungovat v náročných prostředích. Pro jiné metody, jako je OTDOA, poskytnutí informací o sousedních buňkách umožnilo uživatelskému zařízení provádět přesná časová měření. Vytvoření specializované funkce zajistilo standardizované a efektivní doručování těchto asistenčních dat.

Historicky se objevila ve vydání 12 spolu s U-LIRF jako součást vylepšení určování polohy v UTRAN. Reagovala na rostoucí poptávku po přesných a rychlých lokalizačních službách pro tísňová volání (E911), komerční aplikace a optimalizaci sítě. Formalizovala roli sítě v poskytování pomocných informací, což je koncept přenesený do architektur určování polohy v LTE a 5G.

## Klíčové vlastnosti

- Generuje a spravuje asistenční data pro určování polohy
- Podporuje A-GPS poskytováním satelitních efemerid/almanachů
- Podporuje OTDOA poskytováním dat o sousedních buňkách a časových údajů
- Přizpůsobuje asistenční data na základě přibližné polohy uživatelského zařízení (UE)
- Spolupracuje s U-LIRF při doručování dat uživatelskému zařízení
- Může mít rozhraní k externím zdrojům asistenčních dat (např. referenční sítě GPS)

## Související pojmy

- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [U-LIRF – UTRAN Location Information Relay Function](/mobilnisite/slovnik/u-lirf/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [U-LSADF na 3GPP Explorer](https://3gpp-explorer.com/glossary/u-lsadf/)
