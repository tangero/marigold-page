---
slug: "smtc"
url: "/mobilnisite/slovnik/smtc/"
type: "slovnik"
title: "SMTC – SS/PBCH Block Measurement Timing Configuration"
date: 2025-01-01
abbr: "SMTC"
fullName: "SS/PBCH Block Measurement Timing Configuration"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/smtc/"
summary: "Konfigurace poskytovaná sítí UE, která definuje periodická okna (SMTC příležitosti), během nichž má UE provádět měření na blocích synchronizačního signálu/fyzického vysílacího kanálu (SS/PBCH). Je klí"
---

SMTC je konfigurace poskytovaná sítí, která definuje periodická okna, během nichž UE provádí měření SS/PBCH bloků pro měření buňky, mobilitu a správu paprsků.

## Popis

[SS](/mobilnisite/slovnik/ss/)/[PBCH](/mobilnisite/slovnik/pbch/) Block Measurement Timing Configuration (SMTC) je klíčový koncept v 5G New Radio (NR) pro řízení měření UE. V NR, zejména s širokou šířkou pásma a beamformingem, je neustálé monitorování všech možných SS/PBCH bloků (SSB) z obslužných a sousedních buněk pro UE energeticky náročné. SMTC to řeší definováním periodického časového okna, známého jako SMTC okno nebo příležitost. Síť konfiguruje UE parametry SMTC prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/), primárně v rámci informačního elementu MeasObjectNR. Tyto parametry zahrnují periodicitu (např. 5, 10, 20, 40, 80, 160 ms), dobu trvání (délku) měřicího okna (typicky 1–5 ms) a časový posun. UE je povinna provádět měření založená na SSB (jako Reference Signal Received Power ([RSRP](/mobilnisite/slovnik/rsrp/)) a Reference Signal Received Quality ([RSRQ](/mobilnisite/slovnik/rsrq/))) pouze během těchto nakonfigurovaných SMTC oken. Síť sladí vysílání SSB z buněk (jak obslužných, tak sousedních) s těmito SMTC okny. Toto sladění je koordinováno mezi gNB, často prostřednictvím rozhraní Xn, aby bylo zajištěno, že SSB, které má UE měřit, jsou skutečně vysílána v rámci jejího SMTC okna. Pro měření na stejném kmitočtu je typicky konfigurováno jediné SMTC. Pro měření na různých kmitočtech lze pro každý kmitočet nakonfigurovat samostatné SMTC. V pásmu FR2 (mmWave), kde je správa paprsků klíčová, je SMTC úzce propojeno s rámcem měření správy rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)) založeným na SSB, což umožňuje UE měřit paprsky vysílané v různých prostorových směrech během okna. Tato konfigurace zajišťuje přesnost měření a zároveň umožňuje přijímači UE spát během období mimo okna, což výrazně zlepšuje výdrž baterie.

## K čemu slouží

SMTC bylo zavedeno ve specifikaci 3GPP Release 15 jako součást základní specifikace 5G NR, aby vyřešilo klíčové výzvy nové technologie rádiového přístupu. NR pracuje s mnohem širší šířkou pásma a využívá massive [MIMO](/mobilnisite/slovnik/mimo/)/beamforming, což vede ke složitějšímu prostředí měření buněk a paprsků. Bez koordinovaného schématu načasování měření by UE musela neustále monitorovat signály, což by způsobovalo nadměrnou spotřebu energie, což je v rozporu s cíli 5G pro vylepšené mobilní širokopásmové připojení a efektivitu IoT. Navíc v systémech [TDD](/mobilnisite/slovnik/tdd/) a s vysíláním pomocí přepínání paprsků nejsou SSB vysílána nepřetržitě. SMTC poskytuje předvídatelný, síťově řízený plán pro měření. Řeší problém neefektivity měření tím, že umožňuje síti informovat UE přesně, kdy má hledat SSB, a sladit tak aktivitu UE se vzorci vysílání sítě. To byl významný vývoj oproti přístupu k měření v LTE, který byl více kontinuální, a motivovala jej potřeba sofistikovaných technik úspory energie (často označovaných jako koncepty 'wake-up signálu' nebo 'discontinuous reception' rozšířené na měřicí cykly) a požadavek na podporu spolehlivé mobility a správy paprsků v hustých, na paprsky zaměřených nasazeních 5G.

## Klíčové vlastnosti

- Definuje periodická měřicí okna pro měření SS/PBCH bloků (SSB)
- Konfigurovatelná periodicita, doba trvání a posun prostřednictvím signalizace RRC
- Umožňuje výraznou úsporu energie UE tím, že umožňuje přijímači spát mimo SMTC okna
- Podporuje konfigurace pro měření na stejném i různých kmitočtech
- Klíčové pro přesná měření RRM (RSRP/RSRQ) v prostředí NR s beamformingem
- Síť koordinuje načasování vysílání SSB s SMTC okny UE pro platnost měření

## Související pojmy

- [RRM – Radio Resource Management](/mobilnisite/slovnik/rrm/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.831** (Rel-16) — UE RF Requirements for FR2 Enhancements

---

📖 **Anglický originál a plná specifikace:** [SMTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/smtc/)
