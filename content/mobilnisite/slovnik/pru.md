---
slug: "pru"
url: "/mobilnisite/slovnik/pru/"
type: "slovnik"
title: "PRU – Positioning Reference Unit"
date: 2026-01-01
abbr: "PRU"
fullName: "Positioning Reference Unit"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pru/"
summary: "Síťový uzel nebo zařízení vysílající referenční signály pro přesné určování polohy koncového zařízení (UE). Jedná se o klíčovou komponentu ve vylepšené architektuře pro určování polohy podle 3GPP, kte"
---

PRU je síťový uzel nebo zařízení, které vysílá referenční signály za účelem přesného určení polohy koncového zařízení (User Equipment).

## Popis

Jednotka referenčního signálu pro určování polohy (Positioning Reference Unit – PRU) je definovaný síťový prvek v rámci architektury pro určování polohy podle 3GPP, zavedený za účelem zvýšení přesnosti a spolehlivosti lokalizace. Funguje jako pozemní vysílač referenčních signálů pro určování polohy, podobně jako základnová stanice, ale je vyhrazena nebo optimalizována pro účely lokalizace. PRU lze nasadit jako samostatné jednotky nebo je integrovat do stávající síťové infrastruktury, jako jsou gNB nebo ng-eNB. Tyto jednotky vysílají specifické downlinkové signály, jako jsou referenční signály pro určování polohy (Positioning Reference Signals – [PRS](/mobilnisite/slovnik/prs/)) nebo jiné synchronizační signály, které měří cílové UE nebo jiné síťové uzly (jako je funkce správy polohy – Location Management Function) za účelem provedení výpočtů polohy.

Provoz PRU je řízen síťovými funkcemi, jako je funkce správy polohy ([LMF](/mobilnisite/slovnik/lmf/)) v síti 5G Core. LMF může konfigurovat přenosové parametry PRU, včetně načasování signálu, frekvence a výkonu. Mezi hlavní metody určování polohy využívající PRU patří měření rozdílu času příchodu na downlinku ([DL-TDOA](/mobilnisite/slovnik/dl-tdoa/)) a metoda měření doby oběhu ([RTT](/mobilnisite/slovnik/rtt/)). V metodě DL-TDOA UE měří rozdíl času příchodu signálů z více synchronizovaných PRU (a/nebo základnových stanic) k výpočtu své polohy. U metod založených na RTT si PRU a UE vyměňují signály za účelem změření doby šíření signálu tam a zpět.

Z architektonického hlediska je PRU připojena k páteřní síti prostřednictvím rozhraní definovaných pro lokalizační služby, jako je rozhraní NLs k LMF. To umožňuje LMF řídit PRU a shromažďovat měřená data. Role PRU je klíčová v prostředích, kde je satelitní určování polohy (jako [GNSS](/mobilnisite/slovnik/gnss/)) nedostupné nebo nespolehlivé, například uvnitř budov, v městských zástavbách (urban canyons) nebo pod zemí. Díky poskytnutí husté a řízené sítě pozemních referenčních bodů PRU výrazně zvyšují dostupnost a přesnost určování polohy a splňují tak přísné požadavky záchranných služeb, průmyslového IoT a komerčních lokalizačních služeb.

## K čemu slouží

PRU bylo zavedeno, aby řešilo rostoucí poptávku po vysoce přesných a spolehlivých službách určování polohy, které nemohou být uspokojeny pouze globálními navigačními satelitními systémy ([GNSS](/mobilnisite/slovnik/gnss/)). Signály GNSS jsou často slabé nebo nedostupné uvnitř budov, v hustě zastavěných městských oblastech a v podzemních prostorách, což vytváří kritické pokrytí pro aplikace, jako je lokalizace volajícího v nouzových případech (E911/E112), sledování majetku nebo autonomní systémy. Předchozí metody určování polohy v celulárních sítích, jako je Cell-ID nebo pozorovaný rozdíl času příchodu ([OTDOA](/mobilnisite/slovnik/otdoa/)) využívající standardní základnové stanice, často postrádaly potřebnou přesnost nebo vyžadovaly husté nasazení základnových stanic, které nebylo optimalizováno pro určování polohy.

Vytvoření PRU jako dedikovaného uzlu pro určování polohy umožňuje přizpůsobenou strategii nasazení. Síťoví operátoři mohou PRU strategicky rozmístit tak, aby vyplnili mezery v pokrytí a vylepšili geometrii signálu speciálně pro účely lokalizace, nezávisle na plánu pokrytí makro sítě. Tato specializovaná architektura, standardizovaná ve verzi 3GPP Release 17 a vylepšená v následujících verzích, poskytuje škálovatelný a nákladově efektivní způsob dosažení přesnosti určování polohy na úrovni metrů nebo dokonce subměrové úrovně. Řeší problém poskytování všudypřítomné a vysoce přesné lokalizace jako nativní síťové služby, což je základním požadavkem pro vertikály 5G a vyšších generací, jako je průmyslová automatizace, rozšířená realita a veřejná bezpečnost.

## Klíčové vlastnosti

- Vysílá standardizované downlinkové referenční signály pro určování polohy (PRS) pro měření UE
- Může být konfigurována a řízena funkcí správy polohy (LMF) páteřní sítě
- Podporuje klíčové metody určování polohy, jako jsou DL-TDOA a RTT
- Umožňuje vysoce přesné určování polohy v prostředích bez přístupu k GNSS (interiéry/městská zástavba)
- Lze ji nasadit jako samostatnou jednotku nebo integrovat se stávajícími uzly RAN
- Poskytuje přesnou časovou synchronizaci, která je klíčová pro metody určování polohy založené na čase

## Související pojmy

- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [DL-TDOA – Downlink Time Difference Of Arrival](/mobilnisite/slovnik/dl-tdoa/)
- [RTT – Round Trip Time](/mobilnisite/slovnik/rtt/)

## Definující specifikace

- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.571** (Rel-19) — Control Plane LCS Procedures
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.843** (Rel-19) — Study on AI/ML for NR Air Interface

---

📖 **Anglický originál a plná specifikace:** [PRU na 3GPP Explorer](https://3gpp-explorer.com/glossary/pru/)
