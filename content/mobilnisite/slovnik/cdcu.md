---
slug: "cdcu"
url: "/mobilnisite/slovnik/cdcu/"
type: "slovnik"
title: "CDCU – Constrained Dual-Carrier Uplink"
date: 2025-01-01
abbr: "CDCU"
fullName: "Constrained Dual-Carrier Uplink"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cdcu/"
summary: "CDCU je funkce GERAN (GSM/EDGE Radio Access Network) zavedená ve 3GPP Release 8. Umožňuje mobilní stanici vysílat současně na dvou nosných v uplinku, avšak s omezeními výkonu a modulačních schémat pou"
---

CDCU je funkce GERAN, která umožňuje mobilní stanici vysílat současně na dvou nosných v uplinku, s omezeními výkonu a modulace pro druhou nosnou za účelem zvýšení přenosových rychlostí v uplinku.

## Popis

Constrained Dual-Carrier Uplink (CDCU) je klíčové vylepšení v rámci vývojové cesty [GERAN](/mobilnisite/slovnik/geran/) (GSM [EDGE](/mobilnisite/slovnik/edge/) Radio Access Network) definované ve specifikacích 3GPP. Navazuje na základní koncept Dual-Carrier ([DC](/mobilnisite/slovnik/dc/)) operace, která umožňuje mobilní stanici využívat dvě samostatné rádiové kmitočtové nosné pro vysílání a příjem ke zvýšení špičkových přenosových rychlostí. CDCU se konkrétně zabývá směrem uplink a umožňuje zařízení vysílat současně na dvou nosných v uplinku. Na rozdíl od idealizované implementace duální nosné však CDCU zavádí specifická provozní omezení. Tato omezení jsou primárně zavedena pro řízení zvýšeného poměru špičkového a průměrného výkonu ([PAPR](/mobilnisite/slovnik/papr/)) a pro omezení celkové spotřeby energie a tepelného výkonu v mobilním zařízení, což jsou klíčové konstrukční faktory pro mobilní terminály.

Technická operace CDCU zahrnuje přidělení dvou časových slotů v uplinku mobilní stanici, každého na jiném kmitočtu nosné. Síť toto přidělení řídí pomocí zpráv pro alokaci kanálů. Hlavní omezení stanovuje, že při provozu v režimu CDCU musí mobilní stanice na sekundární nosné v uplinku používat modulační schéma nižšího řádu (konkrétně Gaussian Minimum Shift Keying - [GMSK](/mobilnisite/slovnik/gmsk/)). Primární nosná může stále používat modulace vyššího řádu, jako je [8-PSK](/mobilnisite/slovnik/8-psk/) nebo 16-QAM, jak je podporováno standardem EDGE Evolution. Dále je celkový výstupní výkon řízen napříč oběma nosnými, aby nedocházelo k překročení možností výkonového zesilovače zařízení a aby byla dodržena regulační spektrální maska. Toho je dosaženo pomocí algoritmů řízení výkonu, které mohou snížit výkon na jedné nebo obou nosných ve srovnání s provozem na jedné nosné.

Z architektonického hlediska je funkce CDCU rozdělena mezi mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) a podsystém základnové stanice ([BSS](/mobilnisite/slovnik/bss/)). MS musí implementovat druhý vysílací řetězec schopný simultánního provozu spolu s nezbytným zpracováním digitálních signálů a logikou řízení výkonu pro dodržení omezení. BSS, který se skládá z základnové přenosové stanice (BTS) a řadiče základnových stanic (BSC), zajišťuje alokaci zdrojů pro duální nosnou, adaptaci spojení a příjem dvou souběžných uplinkových datových proudů. Receivery BTS musí být schopny demodulovat potenciálně odlišná modulační schéma na dvou nosných. Úlohou CDCU je poskytnout významný krok ve zvýšení propustnosti v uplinku v rámci frameworku EDGE, čímž se zlepšuje symetrie datového kanálu a uživatelský komfort pro aplikace jako nahrávání videa, a zároveň je zajištěno, že funkce zůstane realizovatelná v zařízeních pro koncové uživatele bez nadměrných nákladů nebo vysoké spotřeby baterie.

## K čemu slouží

CDCU bylo vyvinuto pro řešení rostoucí poptávky po vyšších rychlostech mobilních dat, zejména ve směru uplink, v rámci rozšířené infrastruktury sítí GSM/EDGE. Před jeho zavedením byly sítě EDGE zásadně omezeny na provoz s jednou nosnou v uplinku, což vytvářelo asymetrii, kdy downlink mohl být vylepšen funkcemi jako Downlink Dual Carrier (DDC), ale uplink zůstal úzkým hrdlem. Tato asymetrie bránila aplikacím vyžadujícím značnou šířku pásma v uplinku, jako je videokonferencing, nahrávání velkých souborů a sdílení obsahu v reálném čase.

Vytvoření CDCU bylo motivováno potřebou vývoje stávajících sítí GERAN nákladově efektivním způsobem při respektování praktických omezení mobilních terminálů. Plnohodnotný, neomezený duální nosný uplink by vyžadoval, aby mobilní zařízení vysílala s vysokým výkonem na dvou nosných současně, což by vedlo k nepřijatelným požadavkům na výkonové zesilovače, zvýšené spotřebě baterie, generování tepla a v konečném důsledku vyšším nákladům a rozměrům zařízení. Omezený přístup CDCU – omezení modulace na sekundární nosné a řízení celkového výkonu – byl záměrným technickým kompromisem. Poskytl podstatnou část teoretického výkonnostního zisku duální nosné (efektivně zdvojnásobil kapacitu časového slotu v uplinku), přičemž udržel složitost implementace a energetické nároky v mezích současného návrhu terminálů. To umožnilo síťovým operátorům zvýšit kapacitu uplinku prostřednictvím softwarové aktualizace BSS a s novými terminály, aniž by vyžadovali kompletní přestavbu sítě, a tím prodloužit konkurenceschopnou životnost sítí GSM/EDGE tváří v tvář se vyvíjejícím technologiím 3G a 4G.

## Klíčové vlastnosti

- Simultánní vysílání na dvou kmitočtech nosných v uplinku
- Povinné použití modulace GMSK na sekundární nosné v uplinku
- Řízený celkový výstupní výkon pro dodržení omezení zařízení
- Vylepšení pro sítě EDGE Evolution (EGPRS2)
- Řízeno BSS prostřednictvím signalizace alokace kanálu
- Zvyšuje špičkové přenosové rychlosti v uplinku a spektrální účinnost

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [GMSK – Gaussian Minimum Shift Keying](/mobilnisite/slovnik/gmsk/)

## Definující specifikace

- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [CDCU na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdcu/)
