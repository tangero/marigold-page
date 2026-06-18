---
slug: "sl-rstd"
url: "/mobilnisite/slovnik/sl-rstd/"
type: "slovnik"
title: "SL-RSTD – Sidelink Reference Signal Time Difference"
date: 2025-01-01
abbr: "SL-RSTD"
fullName: "Sidelink Reference Signal Time Difference"
category: "Physical Layer"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/sl-rstd/"
summary: "Měření časového rozdílu příjmu mezi referenčními signály postranního spoje ze dvou různých UE nebo mezi signálem postranního spoje a signálem sestupného spoje. Používá se pro relativní určování polohy"
---

SL-RSTD je měření časového rozdílu příjmu mezi referenčními signály postranního spoje (sidelink) ze dvou různých UE nebo mezi signálem postranního spoje a signálem sestupného spoje (downlink). Používá se pro relativní určování polohy a časovou synchronizaci.

## Popis

SL-RSTD je přesné měření časového rozdílu definované pro účely určování polohy v kontextech NR a vyvinutého postranního spoje (sidelink). Měří rozdíl v čase příjmu (ToA) specifických referenčních signálů pro určování polohy (např. Positioning Reference Signals for Sidelink, [SL-PRS](/mobilnisite/slovnik/sl-prs/)) vysílaných ze dvou různých zdrojových UE, jak je pozorováno jedinou přijímající UE. Alternativně může měřit rozdíl mezi časem příjmu signálu postranního spoje od jednoho UE a signálu sestupného spoje od gNB. Měření se provádí korelací známé sekvence SL-PRS s přijímaným signálem za účelem odhadu přesného časování každé cesty. Výsledek se typicky hlásí v jednotkách času (např. nanosekundy nebo vzorky Ts). Toto měření je základním vstupem pro techniky určování polohy založené na pozorovaném časovém rozdílu příjmu ([OTDOA](/mobilnisite/slovnik/otdoa/)) a další metody multilaterace v architekturách určování polohy s asistencí postranního spoje. Například ve scénáři, kdy cílové UE potřebuje určit svou polohu, může měřit SL-RSTD mezi signály SL-PRS přijímanými od více sousedních kotvících UE (jejichž polohy jsou známé). Každé měření SL-RSTD definuje hyperbolickou linii polohy; průsečík více takových hyperbol odhadne polohu cílového UE. Architektura zahrnuje funkci správy polohy ([LMF](/mobilnisite/slovnik/lmf/)), která konfiguruje prostředky SL-PRS pro kotvící UE a měřicí mezery pro cílové UE. Cílové UE provádí měření a hlásí hodnoty SL-RSTD LMF prostřednictvím obslužného gNB a základní sítě (pomocí LTE Positioning Protocol, [LPP](/mobilnisite/slovnik/lpp/)). LMF následně vypočítá polohu. Přesnost SL-RSTD je klíčová a závisí na faktorech, jako je šířka pásma signálu, interference a podmínky vícecestného šíření. Vylepšení v pozdějších verzích se zaměřují na zlepšení přesnosti měření, snížení latence a podporu nových případů užití, jako je relativní určování polohy mezi vozidly pro prevenci kolizí.

## K čemu slouží

SL-RSTD byl zaveden, aby umožnil přesné určování polohy založené na komunikaci mezi zařízeními (device-to-device), a řešil tak omezení tradičních metod založených na síti (např. Uu-based [OTDOA](/mobilnisite/slovnik/otdoa/)) a na [GNSS](/mobilnisite/slovnik/gnss/) v náročných prostředích. Zatímco GNSS poskytuje dobrou přesnost venku, selhává uvnitř budov, v městských kaňonech nebo pod hustým porostem. Určování polohy založené na síti může být nepřesné, pokud je špatná přímá viditelnost na základnové stanice nebo je nízká hustota buněk. Určování polohy pomocí postranního spoje, umožněné SL-RSTD, využívá potenciálně hustší a bližší síť spojů mezi UE. Řeší problém relativního určování polohy mezi vozidly nebo chodci pro bezpečnostní aplikace (např. znalost přesné vzdálenosti a orientace mezi dvěma vozidly) a absolutního určování polohy v oblastech bez pokrytí GNSS využitím jiných UE jako kotvících bodů. Vznik SL-RSTD byl motivován přísnými požadavky na určování polohy pro pokročilé [V2X](/mobilnisite/slovnik/v2x/) (např. přesnost na úrovni jízdního pruhu pro autonomní řízení), průmyslový IoT (sledování aktiv uvnitř továren) a veřejnou bezpečnost (lokalizace záchranářů uvnitř budov). Poskytuje standardizovanou, měřitelnou veličinu, kterou lze integrovat do celkového rámce 3GPP pro určování polohy, což umožňuje hybridní určování polohy kombinující měření z rozhraní Uu, postranního spoje a senzorů pro robustní a přesné služby určování polohy.

## Klíčové vlastnosti

- Měří časový rozdíl příjmu mezi referenčními signály pro určování polohy na postranním spoji (SL-PRS)
- Základní prvek pro OTDOA s asistencí postranního spoje a další metody multilaterace pro určování polohy
- Podporuje jak absolutní určování polohy (s využitím kotvících UE), tak relativní určování polohy mezi UE
- Integrováno s protokolem 3GPP LPP pro hlášení na lokální server (LMF)
- Umožňuje vysoce přesné určování polohy v prostředích bez GNSS, jako jsou vnitřní prostory nebo městské kaňony
- Kritické pro bezpečnostní aplikace V2X vyžadující přesnost na úrovni jízdního pruhu a nízkou latenci

## Související pojmy

- [SL-PRS – Sidelink Positioning Reference Signals](/mobilnisite/slovnik/sl-prs/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [SL-RSTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-rstd/)
