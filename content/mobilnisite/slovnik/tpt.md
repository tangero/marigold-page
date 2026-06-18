---
slug: "tpt"
url: "/mobilnisite/slovnik/tpt/"
type: "slovnik"
title: "TPT – TDO Parameters Table"
date: 2025-01-01
abbr: "TPT"
fullName: "TDO Parameters Table"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tpt/"
summary: "Standardizovaná tabulka definující parametry pro měření časového rozdílu příjmu (Time Difference of Observation – TDO), primárně používaná pro služby určování polohy. Zajišťuje konzistentní konfigurac"
---

TPT je standardizovaná tabulka definující parametry pro měření časového rozdílu příjmu (Time Difference of Observation) za účelem zajištění konzistentní konfigurace a reportování pro přesné určování polohy v systémech 3GPP.

## Popis

Tabulka parametrů [TDO](/mobilnisite/slovnik/tdo/) (TPT) je klíčová datová struktura definovaná v rámci specifikací 3GPP, konkrétně v TS 26.953, která spadá pod oblast služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a služeb určování polohy. Jejím hlavním účelem je standardizovat soubor parametrů spojených s měřením časového rozdílu příjmu (TDO). TDO je základní metoda pro určení polohy uživatelského zařízení (UE) výpočtem rozdílu v čase příchodu signálů z více geograficky oddělených vysílacích bodů, jako jsou evolved NodeBs (eNBs) nebo gNBs. TPT poskytuje jednotný rámec, který definuje konkrétní parametry, jejich formáty, rozsahy a interpretace, jež musí být použity, když síť vyžaduje od UE měření TDO nebo když UE takové měření reportuje zpět síti. Tato standardizace je zásadní pro interoperabilitu, neboť zajišťuje, že různí výrobci síťových zařízení a UE mají společný výklad naměřených dat, čímž předchází chybným interpretacím a umožňuje přesné výpočty polohy.

Z architektonického hlediska není TPT samostatným síťovým prvkem, ale logickou tabulkou zabudovanou do polohových protokolů a signalizačních zpráv. Je odkazována a využívána polohovými servery, jako je Enhanced Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)), v závislosti na generaci 3GPP (LTE nebo 5G). Když je zahájena polohová služba, síť (prostřednictvím polohového serveru) zahrne relevantní parametry z TPT do polohové požadavkové zprávy odeslané UE. Tyto parametry instruují UE, jak přesně provést měření TDO – například specifikují, které referenční signály měřit (např. Positioning Reference Signals – [PRS](/mobilnisite/slovnik/prs/)), časové okno, požadovanou přesnost měření a kritéria pro reportování. UE následně provede měření na základě této konfigurace.

Po dokončení měření UE vytvoří report. Tento report strukturováním naměřených dat vychází z definic parametrů v TPT. Reportované informace typicky zahrnují naměřené hodnoty časového rozdílu, identity měřených buněk nebo vysílacích bodů a přidruženou metriku kvality (jako odhad chyby). Polohový server přijme tento standardizovaný report a použije hodnoty TDO spolu se známými zeměpisnými souřadnicemi vysílacích bodů k výpočtu polohy UE pomocí multilateračních algoritmů. Role TPT tedy spočívá v tom, že slouží jako závazný slovník a smlouva pro polohování založené na TDO, řídíc celý životní cyklus měření od žádosti po report. Její existence abstrahuje složitost měření na rádiovém rozhraní, což umožňuje spolehlivou funkci protokolů pro určování polohy na vyšších vrstvách napříč různými hardwarovými implementacemi.

## K čemu slouží

Tabulka parametrů [TDO](/mobilnisite/slovnik/tdo/) byla zavedena, aby vyřešila problém nekonzistentních a na výrobce specifických implementací polohových měření založených na čase. Před její standardizací mohli různí výrobci síťových zařízení a UE používat proprietární sady parametrů, formáty nebo interpretace pro měření TDO. Tento nedostatek jednotnosti vytvářel významné problémy s interoperabilitou, což ztěžovalo síti využívající zařízení od jednoho výrobce přesně lokalizovat UE od jiného výrobce. Také komplikovalo vývoj služeb založených na poloze ([LBS](/mobilnisite/slovnik/lbs/)) a regulatorních služeb, jako je určení polohy volajícího v nouzových případech (např. E911 v USA), které vyžadují spolehlivé a standardizované metody určování polohy napříč všemi nasazenými zařízeními a sítěmi.

Její vytvoření bylo motivováno rostoucím významem přesného určování polohy v rámci celulárních sítí, zejména s nasazením LTE (Long Term Evolution). S rozšiřováním datových služeb rostly i aplikace vyžadující povědomí o poloze, od navigace a geo-fencing až po optimalizaci sítě a veřejnou bezpečnost. 3GPP uznalo, že pro techniky založené na TDO, jako je Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)), aby byly robustní primární metodou určování polohy, je nezbytná společná a jednoznačná parametrizace. TPT byla tedy zavedena, aby poskytla tuto společnou půdu, a zajistila tak, že všechny strany v procesu určování polohy – síť, polohový server a UE – hovoří stejným technickým jazykem. Tím přímo řeší omezení ad-hoc přístupů tím, že zaručuje konzistenci měření, zlepšuje přesnost určování polohy a umožňuje škálovatelné nasazení pokročilých polohových služeb v globálních sítích.

## Klíčové vlastnosti

- Standardizuje definice parametrů pro žádosti o měření TDO a reporty
- Zajišťuje interoperabilitu mezi síťovým vybavením a UE od různých výrobců
- Definuje formáty a rozsahy hodnot pro časová měření a odhady kvality
- Podporuje konfiguraci měřicích referencí, jako jsou Positioning Reference Signals (PRS)
- Umožňuje přesný výpočet polohy UE pomocí multilaterace na polohovém serveru
- Usnadňuje splnění regulatorních požadavků na určování polohy pro nouzové služby

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [TPT na 3GPP Explorer](https://3gpp-explorer.com/glossary/tpt/)
