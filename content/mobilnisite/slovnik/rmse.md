---
slug: "rmse"
url: "/mobilnisite/slovnik/rmse/"
type: "slovnik"
title: "RMSE – Root Mean Square Error"
date: 2025-01-01
abbr: "RMSE"
fullName: "Root Mean Square Error"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/rmse/"
summary: "Root Mean Square Error (RMSE, střední kvadratická chyba) je statistická metrika používaná ve specifikacích 3GPP ke kvantifikaci přesnosti měření nebo predikcí, zejména při hodnocení výkonu a testování"
---

RMSE je statistická metrika používaná v rámci 3GPP pro kvantifikaci přesnosti měření nebo predikce. Je vypočtena jako druhá odmocnina z průměru druhých mocnin rozdílů mezi pozorovanými a predikovanými hodnotami.

## Popis

Root Mean Square Error (RMSE, střední kvadratická chyba) je základní statistická metrika používaná v technických specifikacích 3GPP pro hodnocení výkonu a ověřování shody. Slouží jako kvantitativní míra rozdílů mezi hodnotami predikovanými modelem nebo systémem a hodnotami skutečně pozorovanými. Výpočet zahrnuje odmocnění z průměru druhých mocnin těchto chyb, což v důsledku operace umocňování penalizuje větší chyby silněji než menší. Tato vlastnost činí RMSE obzvláště citlivou na odlehlé hodnoty a poskytuje tak robustní ukazatel celkové přesnosti tam, kde jsou velké chyby nežádoucí.

V kontextu 3GPP je RMSE specifikována v dokumentech jako TS 26.921 (pro hodnocení kvality řeči a videa) a TS 32.862 (pro řízení a měření výkonu). Její použití pokrývá různé domény, včetně hodnocení výkonu kodeků, přesnosti odhadu kanálu, algoritmů pro určování polohy a predikce síťových parametrů. Například při testování kvality řeči může být RMSE použita pro porovnání výstupu testovaného kodeku s referenčním signálem, čímž kvantifikuje zavedené zkreslení. Podobně při řízení radiových zdrojů může posoudit chybu při predikci informací o stavu kanálu nebo poloze uživatele.

Matematické vyjádření RMSE pro sadu n predikcí (ŷ_i) a odpovídajících pozorovaných hodnot (y_i) je: RMSE = √[ Σ(ŷ_i - y_i)² / n ]. Výsledná hodnota je ve stejných jednotkách jako původní data, což usnadňuje intuitivní interpretaci. Nižší hodnota RMSE indikuje lepší shodu mezi predikovanými a pozorovanými hodnotami. V rámci testovacích procedur 3GPP jsou často definovány specifické prahové hodnoty RMSE jako výkonnostní požadavky, které musí zařízení nebo algoritmy splnit, aby byla zajištěna interoperabilita a konzistentní kvalita služeb v celé síti.

## K čemu slouží

Zařazení RMSE do specifikací 3GPP odpovídá potřebě standardizované, objektivní a kvantifikovatelné metody pro hodnocení výkonu a přesnosti různých telekomunikačních systémů a komponent. Před touto standardizací mohlo být hodnocení výkonu subjektivní nebo založené na nekonzistentních metrikách, což ztěžovalo porovnání výsledků od různých dodavatelů nebo testovacích laboratoří. RMSE poskytuje společný matematický rámec, který je v technice a statistice široce chápán, a zajišťuje tak ověřitelnost a srovnatelnost výkonnostních tvrzení.

Její účel je zvláště kritický v oblastech jako měření kvality uživatelského prožitku ([QoE](/mobilnisite/slovnik/qoe/)) pro multimediální služby a validace složitých algoritmů používaných v rádiových přístupových sítích. Například s vývojem sítí k podpoře pokročilých služeb, jako je vysokokvalitní hlas (VoLTE) nebo streamování videa, se stalo zásadním přesně kvantifikovat percepční kvalitu. RMSE, když je aplikována na percepční modely nebo porovnání signálů, nabízí reprodukovatelnou metriku, která koreluje s uživatelským prožitkem. Dále, v oblasti řízení sítí a funkcí samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)), je přesná predikce chování sítě klíčová. RMSE umožňuje operátorům posoudit účinnost těchto prediktivních algoritmů, čímž zajišťuje stabilitu sítě a efektivní využití zdrojů.

## Klíčové vlastnosti

- Standardizovaná statistická metrika pro hodnocení přesnosti
- Citlivost na velké chyby díky umocňování rozdílů
- Výsledek je ve stejných jednotkách jako měřená data
- Používá se při testování výkonu a ověřování shody
- Specifikována v technických specifikacích 3GPP pro reprodukovatelné testování
- Aplikovatelná napříč více doménami včetně hodnocení kodeků a určování polohy

## Související pojmy

- [KQI – Key Quality Indicators](/mobilnisite/slovnik/kqi/)
- [MOS – Mean Opinion Score](/mobilnisite/slovnik/mos/)
- [MSE – Mobility Speed Estimation](/mobilnisite/slovnik/mse/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)

## Definující specifikace

- **TR 26.921** (Rel-19) — UE Performance in Ambient Noise
- **TS 32.862** (Rel-14) — Service KQI Standardization Study

---

📖 **Anglický originál a plná specifikace:** [RMSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/rmse/)
