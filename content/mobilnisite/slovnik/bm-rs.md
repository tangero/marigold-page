---
slug: "bm-rs"
url: "/mobilnisite/slovnik/bm-rs/"
type: "slovnik"
title: "BM-RS – Beam Management Reference Signal"
date: 2025-01-01
abbr: "BM-RS"
fullName: "Beam Management Reference Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bm-rs/"
summary: "BM-RS je sada referenčních signálů v 5G NR používaná pro procedury správy paprsků, včetně měření, hlášení a zpřesňování paprsků. Umožňuje efektivní beamforming a sledování paprsků, což je klíčové pro"
---

BM-RS je sada referenčních signálů v 5G NR používaná pro procedury správy paprsků, jako je měření, hlášení a zpřesňování, za účelem efektivního beamformingu a sledování paprsků.

## Popis

Beam Management Reference Signals (BM-RS) jsou specializované signály fyzické vrstvy definované v 5G New Radio (NR) pro podporu operací založených na paprscích, což je obzvláště klíčové pro pásma milimetrových vln (mmWave), kde je směrový beamforming nezbytný pro překonání vysokého útlumu na dráze. Tyto signály jsou vysílány jak gNodeB (gNB), tak uživatelským zařízením (UE), aby usnadnily různé procedury správy paprsků, které zahrnují počáteční zachycení paprsku, měření paprsku, hlášení o paprsku a jeho zpřesňování. BM-RS funguje v rámci struktury fyzické vrstvy NR, konkrétně v rámci struktury downlinkových a uplinkových kanálů, a je navržen tak, aby byl konfigurovatelný z hlediska časově-frekvenčních zdrojů, periodicity a prostorových parametrů pro přizpůsobení různým scénářům nasazení a podmínkám mobility.

Architektura BM-RS zahrnuje více typů referenčních signálů, které plní odlišné funkce v rámci správy paprsků. Patří mezi ně Channel State Information Reference Signals ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) pro měření a hlášení o paprsku, stejně jako Synchronization Signal Blocks (SSB), které mohou být také použity pro účely správy paprsků. gNB konfiguruje zdroje BM-RS prostřednictvím signalizace vyšší vrstvy ([RRC](/mobilnisite/slovnik/rrc/)), specifikuje parametry jako mapování zdrojů, předpoklady kvazi-kolokace ([QCL](/mobilnisite/slovnik/qcl/)) a asociaci s konkrétními stavy Transmission Configuration Indicator ([TCI](/mobilnisite/slovnik/tci/)). Během provozu UE měří kvalitu přijatých instancí BM-RS (např. pomocí metrik jako Reference Signal Received Power ([RSRP](/mobilnisite/slovnik/rsrp/)) nebo Signal-to-Interference-plus-Noise Ratio ([SINR](/mobilnisite/slovnik/sinr/))) a tato měření hlásí gNB, který pak tyto informace použije k výběru optimálních paprsků pro přenos a příjem dat.

Klíčové součásti implementace BM-RS zahrnují beamformingové obvody na straně vysílače i přijímače, stavový stroj správy paprsků definovaný v protokolech vrstvy 2 a související mechanismy měření a hlášení. Signály jsou typicky vysílány pomocí analogových nebo hybridních beamformingových technik, kde je fáze více anténních prvků nastavena tak, aby vytvořila směrové paprsky. Zdroje BM-RS mohou být konfigurovány jako periodické, semi-perzistentní nebo aperiodické, což poskytuje flexibilitu pro různé případy užití. Signály podporují jak široké paprsky pro počáteční přístup, tak užší paprsky pro zpřesněný přenos dat, což umožňuje hierarchický přístup ke správě paprsků, který vyvažuje pokrytí a spektrální účinnost.

V síťové architektuře hraje BM-RS zásadní roli při udržování kvality rádiového spoje, zejména v nasazeních na vysokých frekvencích, kde je zarovnání paprsků kritické. Umožňuje gNB sledovat pohyb UE a podle toho upravovat paprsky, čímž předchází výpadkům spojení a zajišťuje konzistentní propustnost. Signály také podporují vícepaprskové operace, kde může být více paprsků současně spravováno pro různá UE nebo pro účely diverzity. Prostřednictvím standardizovaných procedur měření a hlášení poskytuje BM-RS nezbytné informace pro přepínání paprsků, obnovu paprsků a jejich zpřesňování, čímž tvoří základ spolehlivé komunikace v milimetrových vlnách v 5G systémech.

## K čemu slouží

BM-RS byl vytvořen k řešení základních výzev komunikace založené na paprscích v 5G NR, zejména pro spektrum milimetrových vln, kde jsou tradiční všesměrové nebo sektorizované přístupy nedostatečné. Před 5G systémy LTE primárně pracovaly na nižších frekvencích s širšími oblastmi pokrytí, což vyžadovalo méně agresivní beamforming. Přechod na mmWave frekvence (nad 24 GHz) v 5G přinesl závažná omezení šíření včetně vysokého útlumu na dráze, atmosférické absorpce a citlivosti na překážky, což si vyžádalo použití směrových paprsků ke koncentraci energie a prodloužení efektivního dosahu. Bez vyhrazených referenčních signálů pro správu paprsků by udržování zarovnání mezi vysílacími a přijímacími paprsky bylo neefektivní a nespolehlivé, což by vedlo k častým výpadkům spojení a zhoršenému uživatelskému zážitku.

Historický kontext vývoje BM-RS vychází z práce 3GPP na NR v Release 15, kde byla operace zaměřená na paprsky identifikována jako klíčový faktor umožňující komunikaci v mmWave. Předchozí buněčné systémy postrádaly standardizované mechanismy pro dynamickou správu paprsků a spoléhaly se místo toho na pevné sektorové antény nebo omezené techniky adaptivních anténních polí. BM-RS poskytuje standardizovaný rámec, který umožňuje síťovému vybavení od různých výrobců efektivně spolupracovat a zároveň podporuje pokročilé funkce jako sledování paprsků, obnova po selhání paprsku a koordinace více paprsků. Tato standardizace byla zásadní pro zajištění konzistentního výkonu napříč nasazeními a umožnění globálního roamingu v 5G sítích.

BM-RS řeší několik kritických problémů v systémech založených na paprscích: umožňuje efektivní počáteční spárování paprsků během náhodného přístupu, podporuje kontinuální zpřesňování paprsků při pohybu UE nebo změně podmínek kanálu, usnadňuje procedury detekce a obnovy selhání paprsku a poskytuje referenční měření pro rozhodnutí o výběru a přepínání paprsků. Řešením těchto výzev činí BM-RS komunikaci v mmWave prakticky životaschopnou pro aplikace mobilního širokopásmového přístupu, čímž odemyká mnohagigabitové datové rychlosti slibované 5G, a zároveň udržuje spolehlivé připojení i v náročných podmínkách šíření.

## Klíčové vlastnosti

- Podporuje měření paprsků pro downlinkový i uplinkový směr
- Umožňuje hlášení o paprsku pomocí metrik jako RSRP a SINR
- Konfigurovatelné jako periodické, semi-perzistentní nebo aperiodické zdroje
- Asociované se stavy Transmission Configuration Indicator (TCI) pro indikaci paprsku
- Podporuje předpoklady kvazi-kolokace (QCL) pro modelování vztahů mezi paprsky
- Integruje se s mechanismy detekce a obnovy selhání paprsku

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification

---

📖 **Anglický originál a plná specifikace:** [BM-RS na 3GPP Explorer](https://3gpp-explorer.com/glossary/bm-rs/)
