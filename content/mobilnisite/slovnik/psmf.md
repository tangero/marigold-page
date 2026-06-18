---
slug: "psmf"
url: "/mobilnisite/slovnik/psmf/"
type: "slovnik"
title: "PSMF – Positioning Signal Measurement Function"
date: 2025-01-01
abbr: "PSMF"
fullName: "Positioning Signal Measurement Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/psmf/"
summary: "Síťová funkce zodpovědná za měření rádiových signálů z uživatelského zařízení (UE) za účelem určení jeho geografické polohy. Zpracovává měření jako časový předstih, sílu signálu a úhel příchodu. Je kl"
---

PSMF je síťová funkce, která měří rádiové signály z uživatelského zařízení (UE) za účelem určení jeho polohy zpracováním údajů o časování, síle a úhlu pro síťové určování polohy.

## Popis

Funkce měření polohovacích signálů (PSMF) je logická entita v síťové architektuře 3GPP, konkrétně součást infrastruktury pro síťové určování polohy. Jejím hlavním úkolem je shromažďovat a zpracovávat měření rádiových signálů týkající se cílového uživatelského zařízení (UE) z jednoho nebo více síťových uzlů, jako jsou základnové stanice (NodeB, [eNB](/mobilnisite/slovnik/enb/), gNB) nebo jednotky pro měření polohy ([LMU](/mobilnisite/slovnik/lmu/)). Tato nezpracovaná měření tvoří základ pro výpočet geografické polohy UE. PSMF typicky neprovádí samotný konečný výpočet polohy; místo toho poskytuje zpracovaná měřicí data funkci pro určení polohy ([PDF](/mobilnisite/slovnik/pdf/)) nebo platformě pro určování polohy v zabezpečené uživatelské rovině ([SUPL](/mobilnisite/slovnik/supl/) [SLP](/mobilnisite/slovnik/slp/)).

Z architektonického hlediska může být PSMF integrována v řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS, v základnové stanici v LTE a NR, nebo může existovat jako samostatný uzel. Funguje tak, že koordinuje s přístupovou rádiovou sítí, aby instruovala konkrétní buňky, aby prováděly měření signálů z cílového UE. Tato měření zahrnují, mimo jiné, pozorovaný časový rozdíl příchodu ([OTDOA](/mobilnisite/slovnik/otdoa/)) v LTE/NR, kde měří časový rozdíl přijatých pilotních signálů z více buněk; časový rozdíl příchodu v uplinku ([UTDOA](/mobilnisite/slovnik/utdoa/)), kde měří čas příchodu uplinkového signálu UE na více LMU; a metody rozšířeného identifikátoru buňky (E-CID), které kombinují identitu buňky, časový předstih a přijatou sílu signálu. PSMF spravuje měřicí relaci, zajišťuje, že měření jsou provedena současně nebo v požadovaném časovém okně pro přesnost, a může provádět počáteční filtrování nebo hodnocení kvality dat.

Klíčové součásti funkčnosti PSMF zahrnují měřicí kontrolér, který vyžaduje a sdružuje měření z distribuovaných bodů; měřicí databázi, která může ukládat kalibrační nebo referenční signálová data (např. pozice základnových stanic a jejich časové charakteristiky); a obslužné rutiny rozhraní pro protokoly jako LPP (LTE Positioning Protocol) nebo LPPa (LTE Positioning Protocol A) pro komunikaci s UE a dalšími síťovými prvky. Její role je klíčová pro oddělení sběru měření, který je těsně spojen s rádiovou technologií a topologií sítě, od algoritmu výpočtu polohy, který může být obecnější. Tato abstrakce umožňuje zavádění nových metod určování polohy a vylepšení bez nutnosti přepracování celé architektury služeb polohy.

## K čemu slouží

PSMF byla vytvořena pro umožnění přesného, síťového určování polohy za účelem splnění regulatorních, komerčních a bezpečnostních požadavků. Hlavním hybatelem byla (a zůstává) podpora určení polohy tísňových volajících, vyžadovaná předpisy v mnoha zemích (např. E911 v USA). Síťové metody jsou nezbytné, když si UE samo nemůže určit svou polohu (např. nemá funkci GPS) nebo mu to není umožněno (např. nastavení ochrany soukromí nebo scénář zákonného odposlechu). PSMF poskytuje síti nezávislou schopnost lokalizovat zařízení.

Historicky měly rané buněčné systémy velmi hrubé možnosti určení polohy, v podstatě omezené na identitu obsluhující buňky. S nástupem služeb založených na poloze (LBS), jako je navigace, sledování vozového parku a geografické ohraničení, vzrostla poptávka po vyšší přesnosti. PSMF, zavedená v éře UMTS, formalizovala roli sítě při provádění sofistikovaných měření signálů. Řešila omezení čistě UE-bazovaných metod (jako A-GPS), které nemusely být dostupné uvnitř budov nebo mohly vybíjet baterii, a hybridních metod tím, že poskytla spolehlivou, síťově řízenou alternativu. Také řešila problém lokalizace starších nebo jednodušších zařízení, kterým chybí pokročilý polohovací hardware.

Vývoj PSMF byl motivován neustálou potřebou vyšší přesnosti, nižší latence a podpory nových případů užití. Od základních časových měření v UMTS se vyvinula tak, aby podporovala OTDOA s polohovacími referenčními signály v LTE, a nyní zahrnuje měření napříč více RAT (Radio Access Technology) a techniky určování polohy v NR, jako je měření doby oběhu (RTT) s více buňkami. Její vývoj je úzce spojen s rozšiřováním aplikací kritických na polohu, včetně sledování majetku v IoT, komunikace vozidel (V2X) a průmyslové automatizace, kde přesná a spolehlivá lokalizace zařízení je základním předpokladem služeb.

## Klíčové vlastnosti

- Koordinuje měření rádiových signálů z více síťových bodů pro cílové UE
- Podporuje více metod určování polohy (např. OTDOA, UTDOA, E-CID)
- Komunikuje přes rozhraní se základnovými stanicemi a jednotkami pro měření polohy (LMU) za účelem sběru dat
- Může provádět počáteční zpracování a hodnocení kvality nezpracovaných měření
- Poskytuje měřicí data funkci pro určení polohy (PDF) nebo platformě SUPL
- Spravuje měřicí relace, včetně časování a alokace prostředků

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [E-CID – Enhanced Cell-ID](/mobilnisite/slovnik/e-cid/)
- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [PSMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/psmf/)
