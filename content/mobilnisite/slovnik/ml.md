---
slug: "ml"
url: "/mobilnisite/slovnik/ml/"
type: "slovnik"
title: "ML – Maximum Likelihood"
date: 2026-01-01
abbr: "ML"
fullName: "Maximum Likelihood"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ml/"
summary: "Základní statistická metoda odhadu hojně používaná v 3GPP pro zpracování signálu, odhad kanálu, dekódování a určování polohy. Identifikuje hodnoty parametrů, které maximalizují pravděpodobnost pozorov"
---

ML je základní statistická metoda odhadu používaná v 3GPP k optimalizaci výkonu přijímače tím, že identifikuje hodnoty parametrů maximalizující pravděpodobnost pozorování přijímaného signálu.

## Popis

Maximum Likelihood (ML) je princip a metoda statistického odhadu používaná v celé řadě specifikací 3GPP k optimalizaci úloh zpracování signálu v bezdrátových komunikačních systémech. V podstatě, při daném statistickém modelu a pozorovaných datech (např. přijímaný rádiový signál zkreslený šumem), odhad ML najde hodnoty parametrů (např. vysílaný symbol, koeficienty kanálu, poloha uživatele), pro které jsou pozorovaná data nejpravděpodobnější. Matematicky maximalizuje tzv. věrohodnostní funkci, což je pravděpodobnost pozorovaných dat při daných parametrech. V digitálních komunikacích to často znamená minimalizaci vzdálenostní metriky mezi přijatým signálem a všemi možnými vyslanými signály, což z ní činí optimální detektor v přítomnosti aditivního bílého Gaussovského šumu ([AWGN](/mobilnisite/slovnik/awgn/)).

Ve fyzické vrstvě rádiových přístupových technologií 3GPP (LTE, NR) se algoritmy ML používají v několika klíčových oblastech. Pro odhad kanálu lze techniky ML využít k odhadu komplexních zesílení rádiového kanálu z referenčních signálů, což poskytuje přesnější obraz o tom, jak byl signál během šíření zkreslen, ve srovnání s jednoduššími metodami, jako jsou nejmenší čtverce (Least Squares). Při detekci [MIMO](/mobilnisite/slovnik/mimo/) (Multiple-Input Multiple-Output) je detekce ML (nebo její aproximace jako ML-MIMO) optimální metodou pro oddělení prostorově multiplexovaných datových proudů na straně přijímače, ačkoliv její složitost roste exponenciálně s počtem proudů. Pro dekódování se Viterbiho algoritmus – což je implementace ML detekce sekvence – používá pro konvoluční kódy, zatímco principy ML jsou základem dekódování dalších kanálových kódů.

Mimo fyzickou vrstvu je odhad ML klíčový pro metody určování polohy v 3GPP. Pro určování polohy metodou [OTDOA](/mobilnisite/slovnik/otdoa/) (Observed Time Difference of Arrival) v LTE a NR měří UE časové rozdíly příchodu signálu z více základnových stanic. Odhad ML lze použít k výpočtu polohy UE z těchto zašuměných měření, což poskytuje vyšší přesnost než linearizované metody, zejména v podmínkách bez přímé viditelnosti. Podobně při určování polohy založeném na úhlech s využitím massive MIMO pomáhá odhad ML určit úhel příchodu (AoA) nebo úhel odchodu (AoD).

Implementace ML v síťových zařízeních a UE s sebou nese značnou výpočetní složitost, zejména pro systémy s vysokomodulačními řády nebo rozsáhlým MIMO. Proto specifikace 3GPP často odkazují na ML jako na výkonnostní etalon, zatímco praktické implementace mohou používat suboptimální, ale méně složité aproximace (jako [MMSE](/mobilnisite/slovnik/mmse/) pro detekci MIMO). Úlohou ML v síti je posouvat hranice výkonu – zvyšovat přenosové rychlosti, zlepšovat pokrytí, zvyšovat přesnost určování polohy a umožňovat efektivnější využití spektra – tím, že poskytuje teoretické optimum, vůči kterému se měří a zlepšují reálné algoritmy.

## K čemu slouží

Odhad metodou maximální věrohodnosti byl začleněn do standardů 3GPP jako základní matematický nástroj pro dosažení optimálního nebo téměř optimálního výkonu v různých úlohách zpracování signálu, které jsou vlastní digitální bezdrátové komunikaci. Rané celulární systémy používaly jednodušší, méně optimální odhady a detektory kvůli omezenému výpočetnímu výkonu. Nicméně s rostoucími nároky na přenosovou rychlost a s nasazením složitějších technik, jako je [MIMO](/mobilnisite/slovnik/mimo/) a modulace vyšších řádů, se výkonnostní mezera mezi jednoduchými metodami a teoretickým optimem (často ML) stala limitujícím faktorem pro kapacitu sítě a uživatelský zážitek.

Přijetí technik založených na ML v rámci 3GPP bylo motivováno potřebou tyto limity překonat. Například v MIMO-OFDM systémech zavedených v LTE trpěly lineární detektory, jako je Zero-Forcing, zesílením šumu, zejména v špatně podmíněných kanálech. Detekce ML nabídla výrazně lepší výkon z hlediska chybovosti (bit-error-rate), což umožnilo plné využití prostorového multiplexního zisku slibovaného MIMO teorií. Podobně pro pokročilé požadavky na určování polohy vyžadované pro služby tísňového volání a komerční služby založené na poloze byly tradiční geometrické metody v mnohacestném prostředí nedostatečné. Odhad ML poskytl robustní statistický rámec pro zpracování měřicího šumu a chyb způsobených nepřímou viditelností, čímž zlepšil přesnost lokalizace.

ML navíc slouží jako společný etalon ve výkonnostních požadavcích a testování shody 3GPP. Testy výkonu přijímače (např. pro referenční citlivost) často předpokládají ideální ML přijímač pro definování teoretického limitu, což zajišťuje, že reálné implementace dosahují výkonu blízkého této hranici. Standardizací použití principů ML ve specifikacích pro odhad kanálu, detekci, dekódování a určování polohy zajišťuje 3GPP, že zařízení od různých výrobců jsou navržena tak, aby splňovala vysoký a konzistentní výkonnostní standard, což pohání neustálé zlepšování efektivity a schopností bezdrátových technologií.

## Klíčové vlastnosti

- Poskytuje statisticky optimální odhad/detekci v přítomnosti Gaussovského šumu
- Používá se jako výkonnostní etalon pro přijímače v testování shody dle 3GPP
- Aplikuje se při detekci MIMO k oddělení prostorově multiplexovaných datových proudů
- Zvyšuje přesnost odhadu kanálu z referenčních signálů (např. DMRS, SRS)
- Základní pro algoritmy vysokopřesného určování polohy (OTDOA, AoA/AoD)
- Je základem optimálních dekódovacích algoritmů pro různé kanálové kódy (např. Viterbiho algoritmus)

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TR 22.874** (Rel-18) — Technical Report
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.560** (Rel-19) — AIML Enablement (AIMLE) Services Stage 3 Protocol
- **TR 26.812** (Rel-18) — Technical Report
- **TS 26.847** (Rel-19) — AI/ML Evaluation in 5G Media Services
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- **TS 28.104** (Rel-19) — Management Data Analytics (MDA)
- **TS 28.105** (Rel-19) — AI/ML Management for 5GS
- **TS 28.561** (Rel-20) — Management and Orchestration; Network Digital Twin
- **TR 28.809** (Rel-17) — Enhancement of Management Data Analytics (MDA) Study
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [ML na 3GPP Explorer](https://3gpp-explorer.com/glossary/ml/)
