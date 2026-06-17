---
slug: "mgrp"
url: "/mobilnisite/slovnik/mgrp/"
type: "slovnik"
title: "MGRP – Measurement Gap Repetition Period"
date: 2025-01-01
abbr: "MGRP"
fullName: "Measurement Gap Repetition Period"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mgrp/"
summary: "Konfigurovatelný parametr periodicity, který definuje, jak často přijímá UE měřicí mezery od sítě. Tyto mezery jsou krátké pauzy v přenosu dat, které umožňují rádiovému přijímači UE naladit se na jiné"
---

MGRP je konfigurovatelný parametr periodicity, který definuje, jak často přijímá UE měřicí mezery. Tyto mezery jsou krátké pauzy v přenosu dat, které umožňují UE naladit se na jiné frekvence za účelem měření mobility.

## Popis

Measurement Gap Repetition Period (MGRP) je základní parametr v řízení rádiových zdrojů v LTE a NR, který řídí plánování měřicích mezer. Měřicí mezera je nakonfigurované období (typicky 6 ms v LTE), během kterého není User Equipment (UE) plánováno pro vysílání nebo příjem na své servisní buňce. To umožňuje jedinému řetězci rádiového přijímače UE dočasně přeladit na jinou nosnou frekvenci nebo dokonce na jinou Radio Access Technology (RAT) za účelem provedení měření kvality signálu (např. RSRP, RSRQ, SINR) na sousedních buňkách. MGRP definuje časový interval mezi začátky po sobě jdoucích měřicích mezer.

Z pohledu sítě konfiguruje MGRP gNB (v NR) nebo [eNB](/mobilnisite/slovnik/enb/) (v LTE) prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) jako součást měřicí konfigurace (MeasConfig). Běžné standardizované hodnoty jsou 20 ms, 40 ms, 80 ms nebo 160 ms. Volba MGRP představuje kompromis. Kratší perioda (např. 20 ms) poskytuje častější příležitosti k měření, což vede k rychlejší a potenciálně přesnější detekci lepší buňky, což je klíčové pro scénáře s vysokou mobilitou. Zároveň však zavádí častější přerušení toku uživatelských dat, což může snížit propustnost. Delší perioda (např. 160 ms) minimalizuje narušení, ale zvyšuje zpoždění měření a riziko pozdního předání spojení.

MGRP funguje ve spojení s parametrem délky měřicí mezery (MGL). Síť tyto mezery synchronizuje s aktivitou UE, aby se zajistilo, že nebudou zmeškána kritická systémová informace nebo pagingové zprávy. Konfigurace je specifická pro UE a může být přizpůsobena na základě stavu mobility UE, scénáře nasazení (intra-frekvenční, inter-frekvenční nebo inter-RAT) a požadovaného výkonu měření. Při agregaci nosných s více komponentními nosnými, pokud je sekundární buňka na jiné frekvenci, může UE také potřebovat mezery k jejímu měření, což ovlivňuje nastavení MGRP. Správná konfigurace MGRP je tedy klíčovým aspektem optimalizace rádiové mobility a přímo ovlivňuje úspěšnost předání spojení, míru ztráty hovoru a kontinuitu datové služby vnímanou uživatelem.

## K čemu slouží

Koncept MGRP byl vytvořen, aby vyřešil výzvu provádění inter-frekvenčních a inter-RAT měření s UE, které typicky mají jediný řetězec rádiového přijímače schopný naslouchat pouze jedné nosné frekvenci najednou. V raných celulárních systémech bez tohoto konceptu nemohlo UE měřit jiné frekvence bez přerušení probíhajícího hovoru nebo datové relace. Zavedení konfigurovaných měřicích mezer poskytlo řízený, předvídatelný mechanismus, kterým síť instruuje UE, kdy může bezpečně provést tato měření.

Řeší tak omezení "slepého" nebo autonomního přístupu UE k měření, který by mohl vést k nepředvídatelným přerušením služby. Tím, že síť konfiguruje vzor mezer (pomocí MGRP a MGL), si zachovává kontrolu nad plánováním. To umožňuje síti optimalizovat kompromis mezi latencí/přesností měření a efektivitou přenosu dat na základě její znalosti nasazení a kontextu UE. Standardizace konkrétních hodnot MGRP zajišťuje interoperabilitu mezi síťovými prvky a UE od různých výrobců a poskytuje konzistentní rámec pro správu mobility napříč sítěmi LTE a 5G NR.

## Klíčové vlastnosti

- Konfigurovatelná periodicita (např. 20, 40, 80, 160 ms) nastavená sítí prostřednictvím signalizace RRC
- Definuje čas mezi po sobě jdoucími výskyty měřicí mezery pro UE
- Umožňuje UE provádět inter-frekvenční a inter-RAT měření kvality signálu
- Zahrnuje základní kompromis mezi latencí měření a narušením propustnosti dat
- Součást měřicí konfigurace specifické pro UE (MeasConfig)
- Funguje ve spojení s parametrem délky měřicí mezery (MGL)

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 36.894** (Rel-13) — Study on LTE Measurement Gap Enhancement
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification

---

📖 **Anglický originál a plná specifikace:** [MGRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mgrp/)
