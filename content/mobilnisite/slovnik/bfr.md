---
slug: "bfr"
url: "/mobilnisite/slovnik/bfr/"
type: "slovnik"
title: "BFR – Beam Failure Recovery"
date: 2025-01-01
abbr: "BFR"
fullName: "Beam Failure Recovery"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bfr/"
summary: "Beam Failure Recovery (BFR) je mechanismus v 5G NR, který umožňuje uživatelskému zařízení (UE) detekovat selhání svého obslužného paprsku a rychle obnovit spolehlivé spojení pomocí nového paprsku. Je"
---

BFR je mechanismus 5G NR, při kterém UE detekuje selhání svého obslužného paprsku a rychle obnoví spolehlivé spojení pomocí nového paprsku, čímž zajišťuje nepřetržitou mobilitu a vysoké přenosové rychlosti.

## Popis

Beam Failure Recovery (BFR) je kritický postup na fyzické vrstvě ([PHY](/mobilnisite/slovnik/phy/)) a vrstvě [MAC](/mobilnisite/slovnik/mac/) definovaný pro 5G New Radio (NR), zejména pro provoz ve frekvenčním rozsahu 2 (FR2), který zahrnuje pásma milimetrových vln (mmWave). V těchto vysokofrekvenčních spektrech komunikace závisí na vysoce směrových paprskových přenosech mezi gNodeB (gNB) a uživatelským zařízením (UE) kvůli překonání vysoké útlumové ztráty. Tyto úzké paprsky jsou však náchylné k náhlým překážkám (např. osobou, vozidlem nebo budovou), což vede k rychlé degradaci kvality signálu označované jako selhání paprsku. Procedura BFR je mechanismus iniciovaný UE pro detekci tohoto selhání a obnovení spojení bez nutnosti úplného selhání rádiového spoje ([RLF](/mobilnisite/slovnik/rlf/)) a následného [RRC](/mobilnisite/slovnik/rrc/) přestavění, což je mnohem pomalejší a více rušivý proces.

Architektura BFR zahrnuje fáze monitorování, detekce a obnovy koordinované mezi fyzickou vrstvou (PHY) UE, vrstvou řízení přístupu k médiu (MAC) a gNB. gNB nakonfiguruje UE sadou referenčních signálů pro správu paprsků, primárně referenčními signály pro informace o stavu kanálu ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) a/nebo bloky synchronizačních signálů (SSB). UE kontinuálně monitoruje kvalitu svého aktuálně aktivního obslužného paprsku pomocí těchto referenčních signálů. Procedura je spuštěna, když kvalita paprsku, měřená jako přijímaný výkon referenčního signálu ([RSRP](/mobilnisite/slovnik/rsrp/)) nebo podobná metrika, poklesne pod nastavenou prahovou hodnotu po určitý počet po sobě jdoucích měření. Toto představuje detekci selhání paprsku.

Po detekci selhání UE zahájí fázi žádosti o obnovu. gNB předkonfiguruje UE sadou kandidátních paprsků, což jsou alternativní paprsky (identifikované specifickými zdroji CSI-RS nebo SSB), které může UE měřit. UE vybere vhodný nový paprsek z těchto kandidátů a odešle gNB žádost o obnovu paprsku (BFRQ). Tato žádost je odeslána pomocí vyhrazeného preambule na fyzickém náhodném přístupovém kanálu ([PRACH](/mobilnisite/slovnik/prach/)), známé jako prostředek pro náhodný přístup bez kolizí ([CFRA](/mobilnisite/slovnik/cfra/)), který je jednoznačně asociován s vybraným kandidátním paprskem. Tato asociace umožňuje gNB identifikovat, který nový paprsek UE navrhuje pro obnovu po přijetí preambule.

Závěrečnou fází je odpověď gNB a dokončení obnovy. Po přijetí preambule BFRQ gNB potvrdí její přijetí zprávou odpovědi na náhodný přístup (RAR) na fyzickém downlinkovém řídicím kanálu (PDCCH). Klíčové je, že tato odpověď je přenášena pomocí nového paprsku identifikovaného žádostí UE, čímž gNB potvrzuje přijetí přepnutí paprsku. Následně normální komunikace pokračuje na novém paprsku. Celá procedura BFR je navržena tak, aby byla provedena v řádu desítek milisekund, což zajišťuje minimální dopad na uživatelský zážitek a zachovává vysokou spolehlivost a nízkou latenci požadovanou pro služby 5G.

## K čemu slouží

BFR byl zaveden, aby řešil základní výzvu využití mmWave a vysokofrekvenčního spektra v 5G NR: inherentní křehkost směrových komunikačních spojů. Před 5G fungovaly buněčné systémy primárně v pásmech pod 6 GHz, kde jsou signály více všesměrové a méně náchylné k úplnému, okamžitému přerušení. V těchto systémech bylo obnovení spojení řešeno na vyšší vrstvě pomocí procedur selhání rádiového spoje (RLF), které zahrnují komplexní RRC přestavění, převýběr buňky nebo předání spojení – procesy, které mohou trvat stovky milisekund až sekundy. Tato latence je nepřijatelná pro scénáře použití ultra-spolehlivé nízkolatenční komunikace (URLLC) a rozšířeného mobilního širokopásmového přístupu (eMBB) plánované pro 5G.

Motivace pro vytvoření BFR vycházela z poznání, že v paprskově orientovaných nasazeních mmWave je přerušení spojení často lokálním problémem paprsku, nikoliv úplným selháním buňky. Obslužná buňka (gNB) pravděpodobně disponuje dalšími použitelnými paprsky pro obsluhu UE. Účelem BFR je poskytnout rychlý mechanismus obnovy na nižší vrstvě, který zachází se selháním paprsku jako s lokalizovanou událostí. Řeší problém přerušení služby způsobeného dočasnými překážkami tím, že umožňuje rychlé přepnutí paprsku, analogické 'předání spojení na úrovni paprsku', bez zapojení jádra sítě nebo složitých protokolů vyšších vrstev. To přímo zvyšuje robustnost mobility, uživatelský přenosový výkon a celkovou spolehlivost sítě v hustých městských a vnitřních prostředích, kde jsou překážky časté.

Historicky 4G LTE nemělo ekvivalentní proceduru, protože nepoužívalo formování paprsku tak intenzivně jako 5G NR v mmWave. Správa paprsků v LTE, kde existovala, byla méně dynamická. BFR představuje posun paradigmatu k agilnější a odolnější architektuře rádiové přístupové sítě (RAN), který bere v potaz realitu fyzické vrstvy vysokofrekvenční komunikace. Řeší omezení předchozího přístupu 'vše nebo nic' při obnově RLF zavedením granulárního, na paprsek specifického procesu obnovy, který je nezbytný pro naplnění výkonnostních slibů 5G.

## Klíčové vlastnosti

- Rychlá detekce degradace kvality paprskového spoje pomocí nakonfigurovaných referenčních signálů (CSI-RS/SSB)
- Procedura obnovy iniciovaná UE pro minimalizaci latence ve srovnání s obnovou řízenou sítí
- Použití preambulí pro náhodný přístup bez kolizí (CFRA) pro efektivní přenos žádosti o obnovu paprsku (BFRQ)
- Výběr kandidátního paprsku UE z množiny nakonfigurované gNB
- Odpověď gNB a potvrzení přepnutí paprsku pomocí paprskově specifické odpovědi na náhodný přístup (RAR)
- Integrace s celkovým rámcem správy paprsků pro zachování plynulého spojení

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 37.816** (Rel-16) — RAN-centric Data Collection & Utilization Study
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz

---

📖 **Anglický originál a plná specifikace:** [BFR na 3GPP Explorer](https://3gpp-explorer.com/glossary/bfr/)
