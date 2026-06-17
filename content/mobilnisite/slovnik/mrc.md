---
slug: "mrc"
url: "/mobilnisite/slovnik/mrc/"
type: "slovnik"
title: "MRC – Maximal Ratio Combining"
date: 2025-01-01
abbr: "MRC"
fullName: "Maximal Ratio Combining"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mrc/"
summary: "Základní technika zpracování signálu používaná v systémech s přijímací diverzitou pro optimální kombinaci více přijatých kopií signálu. Maximalizuje přijímaný poměr signálu k šumu (SNR) koherentním se"
---

MRC je technika diverzity přijímače, která optimálně kombinuje více kopií signálu jejich sečtením s váhami úměrnými jejich individuálním SNR, čímž maximalizuje celkový přijímaný poměr signálu k šumu.

## Popis

Maximal Ratio Combining (MRC) je optimální technika kombinování diverzity používaná v přijímačích bezdrátové komunikace vybavených více anténami nebo přijímacími větvemi. Jejím základním principem je zpracování více nezávisle útlumem postižených kopií stejného vysílaného signálu za účelem vytvoření jediného, vylepšeného signálu s co nejvyšším možným poměrem signálu k šumu (SNR). Každá přijatá kopie signálu, typicky z jiného anténního prvku nebo dráhy, prochází jedinečnými podmínkami kanálu charakterizovanými komplexním koeficientem kanálu (amplituda a fázový posun) a aditivním šumem. MRC funguje tak, že nejprve na každou větev aplikuje fázovou korekci, aby signály koherentně zarovnala a eliminovala destruktivní interference způsobenou náhodnými fázovými posuny zavedenými kanálem.

Po fázovém zarovnání MRC aplikuje na každou větev váhový faktor před jejich sečtením. Optimální váha pro každou větev je úměrná komplexně sdružené hodnotě jejího koeficientu kanálu a nepřímo úměrná výkonu šumu na této větvi. V praxi pro systém s N přijímacími anténami, pokud má i-tá větev zesílení kanálu h_i a rozptyl šumu σ_i², je kombinovaný signál y_MRC = Σ (h_i* / σ_i²) * y_i, kde y_i je přijatý signál na větvi i a * označuje komplexně sdruženou hodnotu. Tento váhový systém zajišťuje, že větve se silnějšími signály (vyšší SNR) přispívají více k výslednému kombinovanému signálu, zatímco šumové větve jsou potlačeny. Výsledné kombinované SNR je součtem SNR ze všech jednotlivých větví, což poskytuje teoretické N-násobné zvýšení SNR pro N nekorelovaných větví v prostředí s Rayleighovým útlumem.

MRC je implementována v rámci řetězce základního pásma fyzické vrstvy přijímače. Vyžaduje přesný odhad kanálu pro každou diverzitní větev, aby bylo možné vypočítat správné kombinační váhy. Zatímco poskytuje maximální možné zesílení SNR, vyžaduje úplnou znalost informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) na straně přijímače a předpokládá, že šum mezi větvemi je nekorelovaný. MRC je klíčovým prvkem pro přijímací diverzitu v technologiích od 2G do 5G, zlepšuje pokrytí, snižuje míru bitových chyb a zvyšuje celkovou odolnost spoje, zejména v prostředí s útlumem. Tvoří teoretický etalon, vůči kterému se porovnávají jiné kombinační techniky, jako je Equal Gain Combining (EGC) nebo Selection Combining (SC).

## K čemu slouží

MRC byla vyvinuta pro potlačení škodlivých účinků vícecestného útlumu, což je základní výzva v bezdrátové komunikaci, kde signály dorazí k přijímači po více drahách, což způsobuje konstruktivní a destruktivní interferenci vedoucí k rychlým výkyvům síly signálu (útlum). Jednoduché přijímače s jedinou anténou jsou vysoce náchylné k hlubokým útlumům, což způsobuje přerušení hovorů nebo vysoké chybovosti. Diverzitní techniky využívající více antén poskytují několik nezávisle útlumem postižených kopií signálu, takže je nepravděpodobné, že by všechny kopie byly současně v hlubokém útlumu. MRC existuje proto, aby toto diverzitu využívala matematicky nejoptimálnějším způsobem.

Před MRC nebo současně s ní byly používány jednodušší techniky, jako je Selection Combining (výběr nejsilnější větve) nebo Equal Gain Combining (fázové zarovnání a sčítání se stejnými vahami). Tyto techniky jsou však suboptimální. Selection Combinig nevyužívá energii ze všech větví a Equal Gain Combining nezohledňuje rozdílná SNR větví. MRC tento problém řeší tím, že poskytuje teoreticky optimální lineární kombinační systém, který maximalizuje výstupní SNR, a tím plně využívá výkonnostní přínos dostupných diverzitních větví. Její motivace je zakořeněna v teorii informace a snaze o spolehlivou komunikaci přes nespolehlivé kanály. Je základním kamenem moderního návrhu přijímačů, umožňuje schémata modulace vyššího řádu a zlepšenou spektrální účinnost vytvořením stabilnějšího a kvalitnějšího přijímaného signálu, což je nezbytné pro dosažení vysokých přenosových rychlostí požadovaných současnými standardy mobilního širokopásmového přenosu.

## Klíčové vlastnosti

- Poskytuje teoreticky optimální výstupní SNR pro danou sadu diverzitních větví
- Vyžaduje přesný odhad informace o stavu kanálu (CSI) pro každou přijímací větev
- Kombinuje signály aplikací komplexních vah úměrných komplexně sdružené hodnotě kanálu a nepřímo úměrných výkonu šumu
- Dosahuje kombinovaného SNR rovného součtu SNR ze všech jednotlivých větví
- Vyžaduje fázové zarovnání signálů pro zajištění konstruktivního sčítání
- Tvoří základ pro pokročilejší techniky příjmu MIMO, jako je kombinování MMSE

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 36.867** (Rel-13) — LTE DL 4 Rx Antenna Port Study TR
- **TR 38.872** (Rel-18) — Technical Report on Sub-1GHz NR Band Combinations
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [MRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mrc/)
