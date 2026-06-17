---
slug: "fdr"
url: "/mobilnisite/slovnik/fdr/"
type: "slovnik"
title: "FDR – False transmit format Detection Ratio"
date: 2026-01-01
abbr: "FDR"
fullName: "False transmit format Detection Ratio"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fdr/"
summary: "Metrika výkonu v uplinku WCDMA a NR, která měří schopnost přijímače správně identifikovat kombinaci transportního formátu (TFC) z pole TFCI. Kvantifikuje pravděpodobnost nesprávného dekódování TFCI př"
---

FDR je metrika výkonu, která kvantifikuje pravděpodobnost, že přijímač nesprávně dekóduje identifikátor kombinace transportního formátu (TFCI) při přenosu dat v uplinku.

## Popis

False transmit format Detection Ratio (FDR) je klíčový ukazatel výkonu definovaný ve specifikacích 3GPP pro uplink systémů WCDMA (UTRA) a New Radio (NR). Konkrétně měří spolehlivost procesu dekódování indikátoru kombinace transportního formátu (TFCI) na straně přijímače Node B (pro UMTS) nebo gNB (pro NR). V těchto systémech je datový kanál (např. Dedicated Physical Data Channel ([DPDCH](/mobilnisite/slovnik/dpdch/)) v UMTS, Physical Uplink Shared Channel (PUSCH) v NR) multiplexován s řídicími informacemi. TFCI, přenášený na řídicím kanálu (např. Dedicated Physical Control Channel ([DPCCH](/mobilnisite/slovnik/dpcch/)) v UMTS), informuje přijímač o velikosti transportního bloku, modulaci a kódovacím schématu použitého pro současný datový přenos. FDR je definován jako poměr počtu případů, kdy přijímač nesprávně dekóduje TFCI (při skutečné přítomnosti datového bloku), k celkovému počtu přenesených datových bloků. Nízká hodnota FDR je nezbytná pro to, aby přijímač správně interpretoval a demoduloval přenášená data.

Technický proces zahrnuje provedení dekódovací operace přijímačem na přijatých symbolech TFCI, které jsou typicky chráněny kanálovým kódem. Kvůli rušení kanálu, jako je šum, interference a útlum, mohou dekódované bity TFCI obsahovat chyby. Přijímač porovná dekódované TFCI se sadou platných TFC definovaných pro dané spojení. Pokud dekódované TFCI neodpovídá žádnému platnému formátu, je prohlášeno za vymazání. Pokud však nesprávně odpovídá *jinému* platnému formátu, jedná se o falešnou detekci. Metrika FDR zachycuje tyto škodlivé události, kdy přijímač pokračuje v demodulaci a dekódování datové části pomocí nesprávných parametrů, což téměř jistě vede ke zkaženému datovému bloku, který musí vyšší vrstvy (jako vrstva RLC) detekovat a vyžádat si jeho opakovaný přenos, čímž se zvyšuje latence a snižuje propustnost.

FDR je kritický parametr pro návrh systému a správu rádiových prostředků. Ovlivňuje návrh kódovacího schématu TFCI (např. použití (32,10) subkódu Reed-Mullerova kódu druhého řádu v UMTS) a přidělení výkonu mezi pole TFCI a datové pole. Výrobci síťových zařízení používají požadavky na FDR, specifikované v konformačních testovacích specifikacích jako 25.101 a 38.769, k návrhu odolných přijímačů. Během provozu lze naměřené FDR (nebo jeho protějšek, poměr vymazání TFCI) použít jako vstup pro algoritmy vnitřní smyčky řízení výkonu. Pokud je FDR příliš vysoké, síť může přikázat UE zvýšit vysílací výkon řídicího kanálu nesoucího TFCI, aby se zlepšila spolehlivost dekódování, a tím byla zachována integrita uplinkového datového přenosu. FDR se tedy nachází na průsečíku výkonu fyzické vrstvy, adaptace spojení a celkové efektivity systému.

## K čemu slouží

FDR bylo zavedeno za účelem formální specifikace a testování spolehlivosti dekódování řídicích informací v systémech založených na [CDMA](/mobilnisite/slovnik/cdma/), počínaje UMTS WCDMA. Při přenosu paketových dat s proměnnou rychlostí musí být přijímač informován o přesném přenosovém formátu použitém pro každý blok, aby jej mohl správně demodulovat a dekódovat. Tuto zásadní informaci nese TFCI. Nediagnostikovaná chyba v TFCI (falešná detekce) je katastrofální, protože způsobí, že přijímač zpracovává data na základě nesprávných předpokladů, což vede k nediagnostikovaným chybám na fyzické vrstvě nebo k nepotřebným retransmisím na vyšších vrstvách. Před jeho formální definicí nebyl výkon této kritické funkce jednotně kvantifikován, což ztěžovalo testování interoperability a stanovení minimálních požadavků na výkon.

Zavedení metriky FDR reagovalo na potřebu standardizovaného způsobu zajištění odolnosti přijímačů napříč zařízeními různých výrobců. Umožňuje síťovým operátorům mít důvěru v to, že základnové stanice od různých výrobců budou spolehlivě fungovat za specifických podmínek kanálu, jak to vyžadují konformační testy 3GPP. Dále poskytuje jasný cíl pro návrháře přijímačů, což pohání inovace v dekódovacích algoritmech (jako je dekódování s maximální věrohodností pro TFCI) a mechanismech detekce chyb. Ve vývoji směrem k LTE a NR, kde jsou řídicí informace přenášeny různými mechanismy (např. Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)) v [PDCCH](/mobilnisite/slovnik/pdcch/)), zůstává základní princip stejný: potřeba spolehlivě dekódovat přidělení prostředků a indikátory formátu. Zatímco termín 'FDR' je specifický pro TFCI v uplinku WCDMA/NR, koncept měření míry falešných detekcí pro kritické řídicí kanály je základním aspektem návrhu bezdrátových systémů, který zajišťuje integritu dat a efektivní využití spektra.

## Klíčové vlastnosti

- Kvantifikuje pravděpodobnost nesprávného dekódování TFCI během přenosu dat
- Používá se pro konformační testování přijímačů Node B a gNB
- Ovlivňuje návrh kanálového kódování TFCI a přidělení výkonu
- Vstupní parametr pro algoritmy řízení výkonu v uplinku
- Přímo ovlivňuje integritu uplinkových dat a efektivitu HARQ
- Definováno pro režimy FDD i TDD v příslušných specifikacích

## Související pojmy

- [DPCCH – Dedicated Physical Control Channel](/mobilnisite/slovnik/dpcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR

---

📖 **Anglický originál a plná specifikace:** [FDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/fdr/)
