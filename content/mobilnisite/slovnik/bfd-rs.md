---
slug: "bfd-rs"
url: "/mobilnisite/slovnik/bfd-rs/"
type: "slovnik"
title: "BFD-RS – BFD Reference Signal"
date: 2025-01-01
abbr: "BFD-RS"
fullName: "BFD Reference Signal"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bfd-rs/"
summary: "BFD-RS je vyhrazený referenční signál používaný pro detekci selhání paprsku (Beam Failure Detection) v 5G NR. Umožňuje uživatelským zařízením (UE) sledovat kvalitu paprsku a detekovat jeho selhání měř"
---

BFD-RS je vyhrazený referenční signál používaný v 5G NR pro detekci selhání paprsku (Beam Failure Detection), který umožňuje uživatelským zařízením (UE) sledovat kvalitu paprsku a detekovat selhání měřením specifických BFD-RS zdrojů.

## Popis

BFD-RS (Beam Failure Detection Reference Signal) je specializovaný referenční signál definovaný v 5G New Radio (NR) pro účely detekce selhání paprsku v komunikačních systémech využívajících beamforming. Na rozdíl od všeobecných referenčních signálů, jako jsou [CSI-RS](/mobilnisite/slovnik/csi-rs/) nebo SSB, je BFD-RS specificky konfigurován pro sledování kvality kandidátních paprsků, které by potenciálně mohly nahradit selhávající služební paprsek. Signál je vysílán gNB na specifických časově-frekvenčních zdrojích nakonfigurovaných prostřednictvím [RRC](/mobilnisite/slovnik/rrc/) signalizace, což umožňuje UE provádět periodická měření bez nutnosti přenosu dat na těchto paprscích.

Z architektonického hlediska BFD-RS funguje v rámci frameworku správy paprsků fyzické vrstvy 5G NR. gNB nakonfiguruje pro UE jeden nebo více BFD-RS zdrojů, z nichž každý odpovídá kandidátnímu paprsku. Tyto zdroje zahrnují specifické [OFDM](/mobilnisite/slovnik/ofdm/) symboly, subnosné a informace o periodicitě. UE nepřetržitě monitoruje tyto nakonfigurované BFD-RS zdroje při zachování primárního spojení na služebním paprsku. Proces monitorování zahrnuje měření výkonu přijímaného referenčního signálu ([RSRP](/mobilnisite/slovnik/rsrp/)) nebo poměru signálu k šumu a interferenci ([SINR](/mobilnisite/slovnik/sinr/)) na každém BFD-RS zdroji a porovnání těchto měření s nastavenými prahy.

Mechanismus detekce selhání paprsku funguje prostřednictvím vícekrokového procesu. Nejprve UE monitoruje kvalitu služebního paprsku pomocí nakonfigurovaných BFD-RS zdrojů nebo jiných referenčních signálů. Když kvalita služebního paprsku klesne pod nastavenou prahovou hodnotu (Q_out), UE spustí časovač detekce selhání paprsku a začne vyhodnocovat kandidátní paprsky pomocí jejich příslušných BFD-RS zdrojů. Pokud UE identifikuje kandidátní paprsek s kvalitou nad prahovou hodnotou pro obnovu (Q_in) před vypršením časovače, může zahájit procedury obnovy po selhání paprsku. Pokud není nalezen vhodný kandidát, UE deklaruje selhání paprsku a může spustit procedury selhání rádiového spoje.

Klíčové součásti systému BFD-RS zahrnují konfiguraci BFD-RS zdrojů (určující časově-frekvenční zdroje, periodicitu a informace o kvazi-ko-lokaci), prahy detekce selhání paprsku (Q_out a Q_in), časovač detekce selhání paprsku a logiku identifikace kandidátních paprsků. BFD-RS zdroje jsou typicky konfigurovány tak, aby byly kvazi-ko-lokovány s řídicími a datovými kanály odpovídajících kandidátních paprsků, což zajišťuje, že měření na BFD-RS přesně odrážejí kvalitu těchto paprsků pro účely skutečné komunikace.

V širší síťové architektuře hraje BFD-RS klíčovou roli při udržování spolehlivosti spoje v nasazeních na vysokých frekvencích, kde je beamforming nezbytný. Poskytnutím vyhrazených měřicích zdrojů pro kandidátní paprsky umožňuje BFD-RS rychlejší a spolehlivější obnovu po selhání paprsku ve srovnání se systémy, které se při událostech selhání spoléhají na skenování všech možných paprsků. Tím se snižuje doba přerušení služby a zlepšuje se celková spolehlivost systému, zejména v náročných rádiových prostředích s vysokou mobilitou nebo scénáři zastínění.

## K čemu slouží

BFD-RS byl vytvořen, aby řešil specifické výzvy správy paprsků v 5G systémech využívajících milimetrové vlny (mmWave), kde je směrový beamforming nezbytný kvůli vysokému útlumu na trase a náchylnosti k zastínění. V tradičních buňkových systémech pracujících na nižších frekvencích bylo pro udržení spolehlivého spojení dostačující všesměrové nebo širokopaprskové vysílání. Systémy mmWave však vyžadují úzké, směrové paprsky pro dosažení adekvátního rozpočtu spoje, což je činí zranitelnými vůči náhlým selháním paprsku způsobeným mobilitou, rotací nebo změnami prostředí.

Předchozí přístupy k udržování spoje, jako je monitorování rádiového spoje v LTE, byly navrženy pro širší pokrytí a pomalejší změny kanálu. Tyto systémy používaly pro monitorování buňkově specifické referenční signály ([CRS](/mobilnisite/slovnik/crs/)), ale postrádaly granularitu a rychlost potřebnou pro detekci selhání na úrovni paprsku v 5G. Bez vyhrazených signálů pro monitorování paprsků by UE musela neustále skenovat alternativní paprsky nebo čekat na úplné selhání spoje před zahájením obnovy, což by vedlo k nepřijatelným dobám přerušení služby pro aplikace citlivé na latenci.

Zavedení BFD-RS ve 3GPP Release 15 tyto limity specificky řešilo poskytnutím standardizovaného mechanismu pro proaktivní monitorování kvality paprsku. Umožňuje UE udržovat 'seznam sledovaných' kandidátních paprsků při aktivním používání služebního paprsku, což dramaticky snižuje čas potřebný k přepnutí na alternativní paprsek, když ten současný selže. To bylo obzvláště důležité pro podporu případů užití, jako je rozšířená mobilní širokopásmová komunikace (eMBB) a ultra-spolehlivá nízkolatenční komunikace ([URLLC](/mobilnisite/slovnik/urllc/)) v 5G, kde by i krátké přerušení spojení mohlo zhoršit uživatelský zážitek nebo porušit smlouvy o úrovni služeb.

## Klíčové vlastnosti

- Konfigurace vyhrazeného referenčního signálu prostřednictvím RRC signalizace
- Podpora současného monitorování více kandidátních paprsků
- Nastavitelné prahy detekce selhání paprsku (Q_out a Q_in)
- Flexibilní přidělení časově-frekvenčních zdrojů pro BFD-RS
- Asociace kvazi-ko-lokace s kanály kandidátních paprsků
- Integrace s procedurami obnovy po selhání paprsku

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification

---

📖 **Anglický originál a plná specifikace:** [BFD-RS na 3GPP Explorer](https://3gpp-explorer.com/glossary/bfd-rs/)
