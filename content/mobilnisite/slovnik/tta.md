---
slug: "tta"
url: "/mobilnisite/slovnik/tta/"
type: "slovnik"
title: "TTA – Time To Alert"
date: 2025-01-01
abbr: "TTA"
fullName: "Time To Alert"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tta/"
summary: "TTA je klíčový ukazatel výkonnosti (KPI) definovaný v 3GPP pro polohově závislé nouzové služby. Stanovuje maximální přípustný čas, který má síť na určení a nahlášení polohy zařízení iniciujícího nouzo"
---

TTA (Time To Alert) je maximální přípustný čas, který má síť na určení a nahlášení polohy zařízení po zahájení nouzového volání, jak je definováno 3GPP pro polohově závislé nouzové služby.

## Popis

Time To Alert (TTA) je standardizovaná metrika výkonnosti definovaná v rámci specifikací 3GPP, konkrétně v technické specifikaci (TS) 38.305 pro NG-RAN. Kvantifikuje včasnost poskytnutí polohových informací pro uživatelské zařízení (UE), které zahájilo nouzovou relaci. TTA se měří od okamžiku, kdy síť obdrží indikaci o zřízení nouzové relace (např. od funkce [AMF](/mobilnisite/slovnik/amf/) v jádru sítě), až do okamžiku, kdy je odhad polohy tohoto UE doručen žadateli, typicky funkci [LRF](/mobilnisite/slovnik/lrf/) nebo centru [GMLC](/mobilnisite/slovnik/gmlc/). Tato latence typu end-to-end je klíčovým parametrem pro regulatorní shodu, například s direktivami Evropského kodexu elektronických komunikací (EECC), které ukládají konkrétní požadavky na přesnost a časování určení polohy nouzového volajícího.

Požadavek TTA ovlivňuje celý řetězec určování polohy v systému 5G. Když je detekováno nouzové volání, obsluhující AMF spustí žádost o polohu směrem k funkci [LMF](/mobilnisite/slovnik/lmf/). LMF následně koordinuje s UE a NG-RAN (sestávajícím z gNB) získání polohovacích měření. Tato měření mohou být založena na různých metodách, jako je [OTDOA](/mobilnisite/slovnik/otdoa/), [UTDOA](/mobilnisite/slovnik/utdoa/) nebo [A-GNSS](/mobilnisite/slovnik/a-gnss/). Volba metody ovlivňuje dosažitelné TTA, protože některé techniky (např. cell-ID) poskytují rychlou, ale hrubou polohu, zatímco jiné (např. A-GNSS) jsou přesnější, ale mohou trvat déle, zejména v interiéru. Síť musí vybrat a provést polohovací proceduru, která splňuje omezení TTA a zároveň dosahuje požadované přesnosti určení polohy.

Architektonicky není TTA samostatný protokol, ale výkonnostní hranice, která řídí interakci mezi síťovými funkcemi. Mezi klíčové komponenty podílející se na splnění TTA patří AMF (pro kontext relace a mobility), LMF (centrální uzel pro koordinaci a výpočet polohy), gNB (pro poskytování radiových měření a případně funkci [LMU](/mobilnisite/slovnik/lmu/)) a UE (které může podporovat různé polohovací schopnosti). LMF je zodpovědná za výběr vhodné polohovací metody a řízení signalizační výměny pro sběr měření v časovém okně TTA. Selhání v doručení odhadu polohy ve stanoveném TTA může spustit záložní procedury nebo vést k nahlášení méně přesné, ale včasné polohy (např. ID obsluhující buňky), aby nouzové služby obdržely alespoň nějaké použitelné informace.

## K čemu slouží

Hlavním účelem definice Time To Alert (TTA) je stanovit standardizovaný, měřitelný výkonnostní cíl pro určení polohy nouzového volajícího v mobilních sítích. To bylo motivováno přísnými regulatorními požadavky po celém světě, zejména po zavedení nařízení jako FCC E911 v USA a EU E112, která vyžadují, aby mobilní operátoři poskytovali přesné polohové informace pro nouzová volání, aby umožnili rychlejší a efektivnější zásah záchranných složek. Před formální definicí v 3GPP bylo časování určení polohy často závislé na konkrétní implementaci nebo bilaterální dohodě, což vedlo k nekonzistencím a potenciálním zpožděním v nouzových službách.

TTA řeší kritickou potřebu předvídatelnosti a spolehlivosti v nouzových scénářích. Stanovením jasného maximálního časového limitu zajišťuje, že centra tísňového volání (PSAP) obdrží polohová data v známém časovém rámci, což jim umožní vyslat pomoc bez zbytečného odkladu. To je obzvláště důležité v situacích, kdy volající není schopen verbálně komunikovat svou polohu. Formalizace TTA v rámci specifikací 3GPP poskytuje společný etalon pro výrobce síťového vybavení, čipsetů a mobilní operátory k návrhu, testování a nasazení systémů, které jsou interoperabilní a shodné s právními povinnostmi.

Zavedení TTA, zvláště zdůrazňované od 3GPP Release 17 dále, navíc koresponduje s vývojem směrem k nouzovým službám založeným na 5G (5G-ES). Protože 5G umožňuje nové use case a podporuje širší škálu zařízení (IoT senzory pro automatizovaná nouzová upozornění), je existence robustní a standardizované metriky časování polohy ještě důležitější. Zajišťuje, že pokročilé schopnosti 5G, jako je síťové slice pro nouzové služby a podpora vertikální polohy (osa z), jsou podloženy garantovanými výkonnostními parametry pro časově kritické aplikace.

## Klíčové vlastnosti

- Definuje maximální přípustnou latenci pro doručení odhadu polohy UE po zahájení nouzové relace.
- Měří se end-to-end od síťového spouštěče po doručení polohy žadateli (např. LRF/GMLC).
- Řídí výkon různých polohovacích metod (např. OTDOA, A-GNSS, cell-ID).
- Klíčová pro shodu s regulatorními nařízeními pro nouzové služby (E911, E112).
- Ovlivňuje rozhodnutí o síťové architektuře a výběr polohovací procedury funkcí LMF.
- Podporuje architektury polohových služeb jak po řídicí, tak po uživatelské rovině.

## Definující specifikace

- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [TTA na 3GPP Explorer](https://3gpp-explorer.com/glossary/tta/)
