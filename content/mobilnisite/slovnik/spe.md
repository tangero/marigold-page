---
slug: "spe"
url: "/mobilnisite/slovnik/spe/"
type: "slovnik"
title: "SPE – SPeech Encoder"
date: 2025-01-01
abbr: "SPE"
fullName: "SPeech Encoder"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/spe/"
summary: "Řečový kodekový komponent definovaný konsorciem 3GPP pro převod analogových hlasových signálů na komprimovaný digitální bitový tok pro přenos. Je základním prvkem pro hlasové služby v mobilních sítích"
---

SPE je řečový kodér definovaný konsorciem 3GPP, který převádí analogový hlasový signál na komprimovaný digitální bitový tok pro přenos v mobilní síti, čímž zajišťuje efektivní využití přenosového pásma a kvalitu hlasu.

## Popis

Řečový kodér (SPE) je základní funkční blok v architektuře řečového kodeku dle 3GPP, odpovědný za zdrojové kódování hlasových signálů. Jeho hlavní činnost zahrnuje vzorkování analogového hlasového vstupu, aplikaci sofistikovaných algoritmů digitálního zpracování signálu pro analýzu a modelování řečového signálu a následný výstup komprimované digitální reprezentace. Tento proces typně využívá techniky jako lineární prediktivní kódování ([LPC](/mobilnisite/slovnik/lpc/)), které modeluje hlasový trakt, a metody analýzy syntézou pro minimalizaci chyby mezi původní a syntetizovanou řečí. Kodér pracuje v tandemu s odpovídajícím řečovým dekodérem ([SPD](/mobilnisite/slovnik/spd/)) na přijímací straně pro rekonstrukci zvukového signálu.

Architektura SPE je definována v rámci konkrétních standardů kodeků, jako jsou například kodeky Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) nebo [AMR-WB](/mobilnisite/slovnik/amr-wb/). Mezi klíčové vnitřní komponenty patří předzpracovací filtr, modul pro LPC analýzu, percepční váhovací filtr a modul pro hledání buzení (u kodeků založených na kódových knihách). Kodér pracuje na rámcích řečových dat, typicky o délce 20 ms, a vytváří odpovídající rámec zakódovaných parametrů (jako jsou LPC koeficienty, indexy adaptivní a fixní kódové knihy a zesílení). Tyto parametry jsou následně zabaleny do paketů pro přenos přes rozhraní rádiového přístupu.

Jeho role v síti je klíčová pro služby Voice over LTE (VoLTE) a okruhově spínané hlasové služby. Efektivita SPE přímo ovlivňuje kapacitu systému a uživatelský zážitek. Efektivnější kodér umožňuje větší počet současných hovorů ve stejném rádiovém pásmu. Specifikace (např. 3GPP TS 26.071, 26.102) definují přesné algoritmické kroky, bitově přesné výstupy a rozhraní, což zajišťuje, že jakýkoli kompatibilní kodér vyprodukuje bitový tok, který jakýkoli kompatibilní dekodér dokáže správně interpretovat, a garantuje tak interoperabilitu koncové hlasové služby napříč infrastrukturou a koncovými zařízeními různých výrobců.

## K čemu slouží

Řečový kodér existuje proto, aby umožnil digitální hlasovou komunikaci přes rádiové kanály s omezenou šířkou pásma. Základním problémem je přenos lidského hlasu s přijatelnou věrností při současné minimalizaci požadované datové rychlosti, což je ve wireless systémech vzácný zdroj. Rané mobilní systémy používaly jednoduché kódování, ale s vývojem sítí rostla potřeba vyšší spektrální efektivity a odolnosti vůči chybám na kanálu.

Historicky bylo motivací pro standardizaci řečových kodérů, jako jsou ty definované pod hlavičkou SPE, překročit proprietární kodeky a zajistit globální interoperabilitu pro roaming. Před takovou standardizací mohly různé regiony nebo výrobci používat nekompatibilní kodeky, což bránilo plynulým mezinárodním hovorům. Vytvoření rodiny kodeků [AMR](/mobilnisite/slovnik/amr/), která zahrnuje funkci SPE, bylo hnací silou potřeby jediného adaptivního kodeku, který by poskytoval vysokou kvalitu v dobrých rádiových podmínkách a v podmínkách špatných přecházel na robustnější režim s nižší bitovou rychlostí, čímž řešil problém udržení kontinuity hovoru na okraji buňky nebo při interferenci.

Specifikace SPE řeší omezení předchozích neadaptivních nebo fixních kodeků tím, že poskytují rámec pro víceúrovňový provoz. To umožňuje síti dynamicky vybírat optimální rovnováhu mezi kvalitou hlasu a kapacitou kanálu na bázi jednotlivých rámců, což byla schopnost klíčová pro efektivní nasazení hlasových služeb 3G (UMTS) a později 4G/5G.

## Klíčové vlastnosti

- Zdrojové kódování analogových hlasových signálů do komprimovaných digitálních parametrů
- Zpracování po rámcích, typicky na 20ms segmentech řeči
- Využívá lineární prediktivní kódování (LPC) pro modelování hlasového traktu
- Používá techniky analýzy syntézou pro hledání buzení
- Definuje bitově přesný algoritmický chování pro interoperabilitu
- Může pracovat s více bitovými rychlostmi (např. v kodeku AMR)

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TS 26.071** (Rel-19) — AMR Speech Codec Introduction
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.171** (Rel-19) — Introduction to AMR-WB Speech Processing
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification

---

📖 **Anglický originál a plná specifikace:** [SPE na 3GPP Explorer](https://3gpp-explorer.com/glossary/spe/)
