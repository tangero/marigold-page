---
slug: "iov"
url: "/mobilnisite/slovnik/iov/"
type: "slovnik"
title: "IOV – Input Offset Value"
date: 2025-01-01
abbr: "IOV"
fullName: "Input Offset Value"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iov/"
summary: "Parametr používaný v algoritmech řízení výkonu GSM/EDGE Radio Access Network (GERAN). Představuje síťově konfigurovanou hodnotu posunutí aplikovanou na měření úrovně přijímaného signálu v uplinku, kte"
---

IOV je síťově konfigurovaná hodnota posunutí aplikovaná na měření signálu v uplinku při řízení výkonu v GERAN, která ovlivňuje vysílací výkon mobilní stanice a optimalizuje výkon.

## Popis

Input Offset Value (IOV) je klíčový síťově řízený parametr v mechanismu řízení výkonu GSM a [EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), specifikovaný v 3GPP TS 44.064. Funguje v rámci smyčky řízení výkonu v uplinku, což je dynamický proces, při kterém síť instruuje mobilní stanici ([MS](/mobilnisite/slovnik/ms/)), aby upravila svůj vysílací výkon na základě naměřených rádiových podmínek. Primárním měřením pohánějícím tuto smyčku je úroveň přijímaného signálu v uplinku na základnové stanici ([BTS](/mobilnisite/slovnik/bts/)), často označovaná jako [RXLEV](/mobilnisite/slovnik/rxlev/). Surové měření RXLEV se však nepoužívá přímo; místo toho je kombinováno s IOV za účelem vytvoření upraveného vstupu pro algoritmus řízení výkonu.

Z architektonického hlediska je IOV konfigurovatelné posunutí (vyjádřené v dB) uložené v řadiči základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)). Během aktivní komunikace BTS kontinuálně měří RXLEV od MS. BSC následně vypočítá příkaz pro řízení výkonu aplikací algoritmu (definovaného ve specifikacích) na upravené měření: Upravený_RXLEV = Naměřený_RXLEV + IOV. Tato upravená hodnota je porovnána s cílovým rozsahem úrovně signálu. Pokud je upravená hodnota příliš nízká, BSC nařídí MS zvýšit výkon; pokud je příliš vysoká, nařídí jeho snížení. IOV tedy funguje jako 'zauzlení' nebo 'ladicí prvek', který může operátor sítě použít k posunutí efektivního pracovního bodu smyčky řízení výkonu.

Jak to funguje v praxi, zahrnuje pečlivé plánování a optimalizaci sítě. Nastavením kladného IOV síť způsobí, že naměřený signál se algoritmu jeví silnější, což ho vede k příkazu snížit vysílací výkon MS. To může snížit celkovou interferenci v uplinku a šetřit životnost baterie MS, ale pokud je nastaveno příliš vysoko, může vést k nedostatečné kvalitě signálu. Záporné IOV způsobí, že signál se jeví slabší, což vede MS ke zvýšení výkonu, což může zlepšit odolnost spoje na okraji buňky, ale zvyšuje interferenci a spotřebu energie. IOV spolu s dalšími parametry, jako jsou prahové hodnoty a kroky řízení výkonu, umožňuje operátorům jemně vyvažovat kompromisy mezi pokrytím, kapacitou, interferencí a životností baterie v různých síťových prostředích (např. hustě zastavěné městské vs. venkovské). Jeho role je nezbytná pro udržování stabilních a efektivních spojení v uplinku v ekosystému GSM/EDGE.

## K čemu slouží

IOV bylo zavedeno, aby poskytlo síťovým operátorům flexibilní a účinný nástroj pro optimalizaci výkonu v uplinku v sítích GSM, což byla schopnost, která se stávala stále důležitější s rostoucí hustotou sítí a zvyšující se zátěží. Rané mechanismy řízení výkonu byly relativně jednoduché a reagovaly přímo na surová měření signálu. Tento přístup postrádal jemnost potřebnou k zohlednění specifických konfigurací buněk, požadovaných cílů kvality služeb nebo profilů interference jedinečných pro určité oblasti.

IOV to řeší oddělením surového rádiového měření od rozhodovací logiky řízení výkonu. Umožňuje operátorům aplikovat systematické zauzlení, čímž efektivně 'učí' algoritmus řízení výkonu pracovat v požadované oblasti křivky úrovně signálu versus kvalita. To bylo motivováno potřebou řešit konkrétní problémy, jako je přetrvávající interference v uplinku v určitých sektorech, zajištění spolehlivé služby pro uživatele na okraji buňky bez nadměrného zvyšování výkonu a řízení celkového nárůstu šumu v síti za účelem maximalizace kapacity.

Poskytnutím tohoto konfigurovatelného posunutí řeší IOV omezení univerzální strategie řízení výkonu. Umožňuje cílenou optimalizaci, což operátorovi umožňuje například aplikovat vyšší IOV v interferenčně omezené mikrobunce pro agresivní snížení výkonu [MS](/mobilnisite/slovnik/ms/), nebo nižší (či záporné) IOV v pokrytím omezené venkovské buňce pro zajištění dostatečné síly signálu. Tento parametr je klíčovým prvkem v sadě nástrojů pro inženýry optimalizace rádiové frekvence ([RF](/mobilnisite/slovnik/rf/)) a přímo přispívá ke zlepšení kvality sítě, zvýšení kapacity a lepší uživatelské zkušenosti.

## Klíčové vlastnosti

- Síťově konfigurovatelná hodnota posunutí (v dB) aplikovaná na měření RXLEV v uplinku
- Klíčový vstup do algoritmu řízení výkonu v uplinku GERAN definovaného v TS 44.064
- Umožňuje operátorům zauzlovat pracovní bod smyčky řízení výkonu
- Používá se k optimalizaci kompromisů mezi silou signálu, interferencí a životností baterie MS
- Ukládáno a aplikováno řadičem základnových stanic (BSC)
- Umožňuje strategie optimalizace řízení výkonu specifické pro buňku nebo oblast

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [RXLEV – Received Signal Level](/mobilnisite/slovnik/rxlev/)

## Definující specifikace

- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [IOV na 3GPP Explorer](https://3gpp-explorer.com/glossary/iov/)
