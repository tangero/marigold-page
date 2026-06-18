---
slug: "ss-sinr"
url: "/mobilnisite/slovnik/ss-sinr/"
type: "slovnik"
title: "SS-SINR – SS Signal-to-Interference-plus-Noise Ratio"
date: 2025-01-01
abbr: "SS-SINR"
fullName: "SS Signal-to-Interference-plus-Noise Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ss-sinr/"
summary: "SS-SINR je měření v 5G NR, které odhaduje poměr signálu k interferenci a šumu (SINR) konkrétně pro synchronizační signál. Poskytuje přímý odhad potenciální spektrální účinnosti spoje porovnáním výkonu"
---

SS-SINR je měření v 5G NR, které odhaduje poměr signálu k interferenci a šumu (SINR) konkrétně pro synchronizační signál za účelem posouzení potenciální spektrální účinnosti spoje.

## Popis

SS-SINR ([SS](/mobilnisite/slovnik/ss/) Signal-to-Interference-plus-Noise Ratio) je pokročilé měření na fyzické vrstvě v 5G NR, které poskytuje přímý odhad kvality kanálu pro synchronizační signál. Je definován jako poměr přijatého výkonu požadovaného SS (konkrétně [SSS](/mobilnisite/slovnik/sss/)) k přijatému výkonu interference a šumu. Na rozdíl od [SS-RSRQ](/mobilnisite/slovnik/ss-rsrq/), což je poměr výkonu signálu k celkovému přijatému výkonu, se SS-SINR snaží izolovat a odhadnout složku interference a šumu přímoji, ačkoli přesná metoda výpočtu může být specifická pro implementaci. V praxi UE odhaduje výkon požadovaného SS signálu (podobně jako [SS-RSRP](/mobilnisite/slovnik/ss-rsrp/)) a výkon interference a šumu přítomného v kanálu, typicky měřením zbytkového výkonu v přenosových prvcích ([RE](/mobilnisite/slovnik/re/)), které nenesou požadovaný signál, nebo využitím známých struktur signálu.

Architektonická implementace měření SS-SINR je složitější než u SS-RSRP nebo SS-RSRQ. Příjemce UE musí používat pokročilé techniky zpracování signálu. Po synchronizaci se SSB má UE znalost vysílané sekvence SSS. Tuto znalost může využít k odhadu kanálu pro přenosové prvky (RE) SSS. Z těchto prvků je odhadnut výkon požadovaného signálu. Pro odhad interference a šumu může UE měřit výkon v prázdných přenosových prvcích (RE) uvnitř SSB nebo v sousedních symbolech/pásmech, nebo může použít algoritmy odhadu interference, které od celkového přijatého signálu odečtou rekonstruovaný požadovaný signál. Poměr těchto dvou odhadů dává SS-SINR, který je obvykle hlášen v dB.

Role SS-SINR v síti 5G je klíčová pro vysoce výkonnou adaptaci spoje a pokročilé [RRM](/mobilnisite/slovnik/rrm/). Poskytuje přesnější prediktor dosažitelného schématu modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)) a tedy potenciální propustnosti na fyzickém downlinkovém sdíleném kanálu ([PDSCH](/mobilnisite/slovnik/pdsch/)). Zatímco SS-RSRP a SS-RSRQ postačují pro základní mobilitu, SS-SINR je zásadní pro jemně odstupňované řízení svazku, zejména v nasazeních na milimetrových vlnách (FR2). gNodeB může použít nahlášená měření SS-SINR pro různé SSB (svazky) k výběru optimálního spoje dvojice svazků s nejvyšší kvalitou, nikoli pouze s nejsilnějším výkonem. Dále je SS-SINR klíčovým vstupem pro výběr vrstev MIMO a algoritmy adaptace pořadí (rank). Pomáhá síti rozhodnout, kolik prostorových vrstev lze k UE úspěšně přenést. Pro funkce jako koordinované vícebodové přenosy/příjem (CoMP) jsou přesné odhady SINR z více vysílacích bodů nezbytné pro rozhodování, zda použít sdružený přenos nebo dynamický výběr bodu.

## K čemu slouží

SS-SINR byl zaveden ve 3GPP Release 15, aby splnil potřebu přesnějšího ukazatele kvality kanálu (CQI) pro spoj založený na synchronizačním signálu v 5G NR. Zatímco SS-RSRQ poskytuje metriku kvality, je svou podstatou omezená, protože její jmenovatel (RSSI) zahrnuje i výkon samotného požadovaného signálu. SS-SINR byl vytvořen, aby nabízel čistší odhad podmínek interference a šumu, což je přímější vstup pro algoritmy adaptace spoje, které tradičně používají mapovací tabulky SINR na CQI. Motivace vycházela ze zvýšených výkonnostních požadavků 5G, jako je ultra-spolehlivá komunikace s nízkou latencí (URLLC) a vylepšené mobilní širokopásmové připojení (eMBB), které vyžadují velmi přesné informace o stavu kanálu.

Tato technologie řeší problém suboptimální alokace zdrojů, ke které může dojít při použití pouze metrik založených na výkonu nebo RSSI. Ve scénářích s výraznou mezibuněčnou interferencí nebo v podmínkách omezených šumem poskytuje SS-SINR věrnější obraz robustnosti spoje. Například dvě buňky mohou mít stejný SS-RSRP, ale jedna může mít mnohem nižší interferenci, což vede k vyššímu SS-SINR a tím i podpoře vyššího řádu MCS. Poskytnutím této informace umožňuje SS-SINR síti maximalizovat spektrální účinnost a propustnost pro uživatele. Odstraňuje omezení předchozích metrik oddělením odhadu interference od měření celkového výkonu, což umožňuje inteligentnější rozhodování o beamformingu, MIMO a plánování. To bylo zvláště kritické pro úspěch beam-centric designu 5G ve vysokých pásmech, kde je pro překonání vysokého útlumu na dráze a dynamického stínění nezbytné přesné zarovnání svazku a posouzení jeho kvality.

## Klíčové vlastnosti

- Přímý odhad SINR pro synchronizační signál (SSS)
- Poskytuje klíčový vstup pro adaptaci spoje a odhad CQI
- Klíčový pro pokročilé řízení a výběr svazku v pásmu FR2
- Podporuje adaptaci pořadí (rank) MIMO a rozhodování o výběru vrstev
- Používá se ve schématech koordinovaného vícebodového přenosu/příjmu (CoMP)
- Metodika měření může být specifická pro implementaci, ale dodržuje výkonnostní požadavky 3GPP

## Související pojmy

- [SS-RSRP – Synchronization Signal based Reference Signal Received Power](/mobilnisite/slovnik/ss-rsrp/)
- [SS-RSRQ – Synchronization Signal Reference Signal Received Quality](/mobilnisite/slovnik/ss-rsrq/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement

---

📖 **Anglický originál a plná specifikace:** [SS-SINR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ss-sinr/)
