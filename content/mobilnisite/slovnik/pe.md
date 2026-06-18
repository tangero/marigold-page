---
slug: "pe"
url: "/mobilnisite/slovnik/pe/"
type: "slovnik"
title: "PE – Positioning Error"
date: 2025-01-01
abbr: "PE"
fullName: "Positioning Error"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pe/"
summary: "Positioning Error (PE) je metrika přesnosti pro polohové služby v sítích 3GPP. Představuje rozdíl mezi odhadem polohy poskytnutým sítí a skutečnou geografickou polohou uživatelského zařízení (UE) a je"
---

PE je metrika přesnosti představující rozdíl mezi odhadem polohy poskytnutým sítí a skutečnou geografickou polohou uživatelského zařízení (UE).

## Popis

Positioning Error (PE) je základním výkonnostním metrikem pro všechny polohové služby definované v 3GPP specifikacích. Kvantifikuje přesnost určení polohy, typicky vyjádřenou jako vodorovná nebo svislá chyba vzdálenosti (např. v metrech). Tato chyba je rozdílem mezi odhadnutými souřadnicemi polohy (zeměpisná šířka, délka, nadmořská výška) a skutečnou polohou UE. PE je často charakterizována statisticky, například 95. percentilem chyby nebo pravděpodobnou kruhovou chybou (CEP). Výpočet zahrnuje komplexní zpracování signálu a geometrické kalkulace založené na měřeních z různých zdrojů, jako je Globální navigační satelitní systém ([GNSS](/mobilnisite/slovnik/gnss/)), buněčné základnové stanice (gNBs/eNBs) a senzory.

Architektonicky zahrnuje určování polohy v 3GPP několik síťových funkcí. Klíčovou složkou je funkce správy polohy ([LMF](/mobilnisite/slovnik/lmf/)), která sídlí v jádru sítě 5G (definováno v TS 23.273). LMF koordinuje relaci určování polohy, volí vhodnou metodu (např. Assisted GNSS, Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)), Uplink Time Difference of Arrival ([UTDOA](/mobilnisite/slovnik/utdoa/)) nebo Enhanced Cell ID) a vypočítává konečný odhad polohy a s ním související PE. UE a rádiová přístupová síť (RAN) poskytují prostřednictvím funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) LMF nezbytná měřicí data (např. časová měření, síly signálu). V RAN specifikace jako 38.857 definují přesnou signalizaci a procedury pro podporu těchto měření.

Výpočet PE závisí na použité metodě určování polohy. U metod založených na GNSS je PE ovlivněna geometrií satelitů (Dilution of Precision), mnohocestným šířením signálu a atmosférickými podmínkami. U síťových metod, jako je OTDOA, závisí PE na hustotě a geometrii základnových stanic, přesnosti časových měření a chybách synchronizace. LMF často používá hybridní metody a filtrační algoritmy (např. Kalmanovy filtry) ke spojení více zdrojů dat a zlepšení přesnosti, přičemž odhaduje oblast spolehlivosti (elipsa chyby). Úkolem PE je poskytnout ukazatel spolehlivosti určení polohy, což je kritické pro aplikace s právními nebo bezpečnostními důsledky, jako jsou tísňová volání typu E911 nebo zákonný odposlech.

## K čemu slouží

Positioning Error existuje, aby poskytl standardizovanou, kvantifikovatelnou míru přesnosti polohové služby, což je zásadní pro regulační, komerční a bezpečnostní aplikace. Hlavním impulzem byly regulační požadavky na lokalizaci tísňových volajících (např. E112 v Evropě, E911 v USA), které vyžadují, aby mobilní sítě poskytly polohu volajícího v rámci stanovené přesnosti (např. 50 metrů pro určité procento hovorů). Bez standardizované metriky PE by nebylo možné ověřit shodu nebo porovnávat výkon různých nasazení sítí a technologií.

Historicky poskytovaly rané buněčné sítě velmi hrubou lokalizaci (pouze Cell ID), což vedlo k velkým, nepředvídatelným chybám. Evoluce přes 3G a 4G přinesla pokročilejší techniky, jako je [OTDOA](/mobilnisite/slovnik/otdoa/) a Assisted-GPS, což vyžadovalo přesný způsob vykazování jejich přesnosti. Standardizace PE v rámci 3GPP (od verze Rel-8 výše) vyřešila problém interoperability a měření výkonnosti. Umožnila vytvoření specifikací úrovně služeb pro služby založené na poloze, podpořila inovace ve vysoce přesném určování polohy pro případy použití IoT a automobilového průmyslu a dala síťovým operátorům možnost optimalizovat svou infrastrukturu (např. nasazením více small cells nebo vylepšením synchronizace) za účelem snížení PE.

## Klíčové vlastnosti

- Základní metrika přesnosti pro všechny metody určování polohy 3GPP (A-GNSS, OTDOA, ECID atd.)
- Definována a spravována funkcí správy polohy (LMF) v jádru sítě
- Hlásena jako vodorovná a/nebo svislá přesnost, často s uvedením úrovně spolehlivosti
- Kritická pro splnění regulatorních požadavků (např. na lokalizaci pro záchranné služby)
- Ovlivněna nasazením sítě, podmínkami šíření signálu a přesností měření
- Používá se k výběru optimální metody určování polohy pro daný požadavek na přesnost

## Související pojmy

- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TR 38.857** (Rel-17) — Study on NR Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [PE na 3GPP Explorer](https://3gpp-explorer.com/glossary/pe/)
