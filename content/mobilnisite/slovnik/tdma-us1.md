---
slug: "tdma-us1"
url: "/mobilnisite/slovnik/tdma-us1/"
type: "slovnik"
title: "TDMA-US1 – TDMA United States 1 Speech Codec"
date: 2025-01-01
abbr: "TDMA-US1"
fullName: "TDMA United States 1 Speech Codec"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/tdma-us1/"
summary: "Hlasový kodek s přenosovou rychlostí 12,2 kbit/s definovaný pro systémy TDMA, technicky podobný kodeku GSM Enhanced Full Rate (GSM-EFR). Poskytuje vysokokvalitní hlasovou službu a představuje specific"
---

TDMA-US1 je hlasový kodek s přenosovou rychlostí 12,2 kbit/s pro severoamerický trh TDMA (IS-136), technicky podobný kodeku GSM-EFR, navržený k poskytování vysokokvalitní hlasové služby a zajištění parity se sítěmi GSM.

## Popis

TDMA-US1 je hlasový kodek specifikovaný pro buňkové systémy založené na [TDMA](/mobilnisite/slovnik/tdma/), pracující s přenosovou rychlostí 12,2 kbit/s. Je definován ve specifikacích 3GPP jako kodek s technickými charakteristikami podobnými kodeku GSM Enhanced Full Rate ([GSM-EFR](/mobilnisite/slovnik/gsm-efr/)). Označení 'US1' typicky odkazuje na jeho použití na trhu Spojených států pro systémy jako IS-136. Stejně jako [TDMA-EFR](/mobilnisite/slovnik/tdma-efr/) a GSM-EFR je založen na kódovací technice [ACELP](/mobilnisite/slovnik/acelp/) (Algebraic Code Excited Linear Prediction).

Provoz kodeku zahrnuje zpracování řeči v segmentech (rámcích). Analyzuje každý rámec za účelem stanovení parametrů pro lineárně prediktivní syntetický filtr a excitační signál. Excitace je konstruována ze záznamů v algebraickém kodebooku (reprezentující inovaci) a adaptivním kodebooku (reprezentující periodičnost základního tónu). Tyto parametry jsou kvantovány a zakódovány do 244bitového bloku pro každý 20ms rámec, což vede k přenosové rychlosti 12,2 kbit/s. Tato relativně vysoká přenosová rychlost ve srovnání s jinými buňkovými kodeky umožňuje méně agresivní kompresi, zachovává více charakteristik původního řečového signálu a poskytuje velmi vysokou subjektivní kvalitu.

V síťové architektuře funguje TDMA-US1 v rámci řetězce zpracování řeči. Je implementován v audiokodeku terminálu a v síťové jednotce Transcoder and Rate Adaptation Unit ([TRAU](/mobilnisite/slovnik/trau/)) nebo Media Gateway. Zakódovaný bitový proud je paketizován a přenášen přes přidělený provozní kanál na rozhraní TDMA. Specifikace 3GPP TS 26.093 poskytuje podrobný algoritmický popis a testovací sekvence pro tento kodek, čímž zajišťuje, že různé síťové prvky a mobilní telefony mohou vzájemně spolupracovat a poskytovat konzistentní, věrný hlasový službu koncovému uživateli.

## K čemu slouží

TDMA-US1 byl vyvinut, aby poskytl možnost vysokopřenosového, prémiového hlasového kodeku pro sítě [TDMA](/mobilnisite/slovnik/tdma/) (IS-136), zejména v Severní Americe. Kontextem byla konkurenční situace, kdy globální sítě GSM zaváděly vysokokvalitní kodek [GSM-EFR](/mobilnisite/slovnik/gsm-efr/). Operátoři TDMA potřebovali srovnatelnou nabídku, aby zajistili, že kvalita jejich hlasové služby nebude vnímána jako horší.

Řešený problém byl omezení dřívějších kodeků TDMA, které měly buď nižší kvalitu (full-rate), nebo vyžadovaly složitější provoz s proměnnou přenosovou rychlostí. TDMA-US1 nabídl přímočarou, vysokokvalitní alternativu s pevnou přenosovou rychlostí. Jeho vytvoření bylo motivováno snahou o standardizaci a harmonizaci kvality. Technickým sladěním s široce přijímaným GSM-EFR umožnil potenciální úspory z rozsahu ve vývoji a testování čipových sad a zajistil, že uživatelé TDMA mohli zažívat srovnatelnou srozumitelnost hovoru jako uživatelé jiných předních digitálních technologií. Sloužil jako kvalitativní benchmark pro hlasové služby TDMA před rozšířeným přijetím pokročilejších adaptivních vícerychlostních kodeků.

## Klíčové vlastnosti

- Hlasový kodek s pevnou přenosovou rychlostí 12,2 kbit/s
- Založen na kódovacím algoritmu ACELP, podobně jako GSM-EFR
- Zpracovává řeč ve 20ms rámcích, produkuje 244 bitů na rámec
- Navržen pro poskytování věrného, téměř telefonní kvality hlasu
- Standardizován pro interoperabilitu v systémech TDMA (IS-136)
- Obsahuje komplexní testovací sekvence pro validaci implementace

## Související pojmy

- [GSM-EFR – GSM Enhanced Full Rate Speech Codec](/mobilnisite/slovnik/gsm-efr/)
- [TDMA-EFR – TDMA Enhanced Full Rate Speech Codec](/mobilnisite/slovnik/tdma-efr/)
- [ACELP – Algebraic Code-Excited Linear Prediction](/mobilnisite/slovnik/acelp/)

## Definující specifikace

- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS

---

📖 **Anglický originál a plná specifikace:** [TDMA-US1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdma-us1/)
