---
slug: "sstd"
url: "/mobilnisite/slovnik/sstd/"
type: "slovnik"
title: "SSTD – SFN and Subframe Timing Difference"
date: 2025-01-01
abbr: "SSTD"
fullName: "SFN and Subframe Timing Difference"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/sstd/"
summary: "Měření hlášené uživatelským zařízením (UE) síti, které udává časový rozdíl mezi dvěma buňkami. Je klíčové pro lokalizační techniky jako je Observed Time Difference of Arrival (OTDOA) v LTE a pomáhá ur"
---

SSTD je měření časového rozdílu mezi dvěma buňkami hlášené uživatelským zařízením (UE), používané pro lokalizační techniky jako OTDOA k určení polohy UE.

## Popis

[SFN](/mobilnisite/slovnik/sfn/) and Subframe Timing Difference (SSTD) je specifické měření definované v LTE pro podporu síťových lokalizačních metod, především Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)). Kvantifikuje relativní časový rozdíl pozorovaný uživatelským zařízením (UE) mezi referenční buňkou a sousední buňkou. Tento časový rozdíl je přímým vstupem pro výpočet hyperbol používaných v multilateračních lokalizačních algoritmech. Měření je hlášeno UE do Evolved Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) prostřednictvím LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)).

Z architektonického hlediska je měření SSTD založeno na příjmu lokalizačních referenčních signálů ([PRS](/mobilnisite/slovnik/prs/)) vysílaných eNodeB. Síť konfiguruje UE prostřednictvím LPP seznamem buněk k měření, včetně referenční buňky (typicky obslužné buňky) a více sousedních buněk. Pro každou sousední buňku UE měří časový rozdíl mezi příjmem hranice podrámce od referenční buňky a hranice podrámce od sousední buňky. Výsledkem je SSTD, vyjádřený v jednotkách Ts (základní časová jednotka rovna 1/(15000*2048) sekundy). Klíčové je, že měření zahrnuje jak rozdíl čísla systémového rámce (SFN), tak časový rozdíl na úrovni podrámce, což mu umožňuje zachytit velké časové posuny přesahující více rámců, což je nezbytné pro buňky, které nejsou synchronizované nebo jsou vzdálené.

Z provozního hlediska UE provádí korelační detekci na přijatých PRS sekvencích z konfigurovaných buněk. Díky pseudonáhodné povaze PRS sekvencí, které jsou pro každou buňku jedinečné, může UE rozlišit signály z různých buněk i za podmínek nízkého poměru signálu k šumu ([SNR](/mobilnisite/slovnik/snr/)). Měřicí postup zahrnuje zarovnání lokálního časování přijímače na PRS referenční buňky a následnou korelaci s očekávanou PRS sekvencí sousední buňky, aby se našel její přesný časový posun. Nahlášená hodnota SSTD spolu se známými zeměpisnými souřadnicemi a přesným časováním eNodeB (poskytnutými E-SMLC) se používá k výpočtu polohy UE. Přesnost nahlášené polohy UE přímo závisí na přesnosti těchto měření SSTD, což z něj činí klíčový ukazatel výkonu pro lokalizační služby založené na OTDOA.

## K čemu slouží

SSTD bylo vytvořeno za účelem splnění regulatorních a komerčních požadavků na přesné určování polohy mobilních zařízení v sítích LTE. Předchozí lokalizační metody v sítích 2G/3G, jako Cell-ID a Enhanced Cell-ID, nabízely omezenou přesnost. Potřeba přesné lokalizace (např. pro tísňové služby (E911), služby založené na poloze a sledování majetku) vedla k požadavku na přesnější, síťově asistovanou metodu. Jako primární řešení bylo přijato [OTDOA](/mobilnisite/slovnik/otdoa/), ale vyžadovalo standardizované, vysoce přesné měření časových rozdílů mezi signály buněk, jak je pozoruje UE.

Měření SSTD konkrétně řeší problém kvantifikace rozdílů v době příchodu ve formátu vhodném pro multilaterační výpočty. Odstraňuje omezení jednodušších časových měření tím, že zahrnuje posun [SFN](/mobilnisite/slovnik/sfn/), což je nezbytné v asynchronních sítích nebo když časový rozdíl přesahuje délku jednoho podrámce (1 ms). Jeho zavedení ve vydání 13 bylo součástí širšího vylepšení lokalizačních schopností LTE a poskytlo základní datový bod, který umožňuje přesnost lokalizace na úrovni metrů v kombinaci s hustým nasazením buněk podporujících PRS a přesnou znalostí časování základnových stanic.

## Klíčové vlastnosti

- Definované měření pro lokalizaci OTDOA v LTE.
- Hlásí časový rozdíl mezi referenční buňkou a sousední buňkou.
- Měření zahrnuje rozdíly jak v čísle systémového rámce (SFN), tak na úrovni podrámce.
- Založeno na detekci lokalizačních referenčních signálů (PRS).
- Hlášeno UE síti prostřednictvím LTE Positioning Protocol (LPP).
- Základní vstup pro multilaterační algoritmy k výpočtu polohy UE.

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [RSTD – Reference Signal Time Difference](/mobilnisite/slovnik/rstd/)

## Definující specifikace

- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SSTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/sstd/)
