---
slug: "cazac"
url: "/mobilnisite/slovnik/cazac/"
type: "slovnik"
title: "CAZAC – Constant Amplitude Zero Auto-Correlation"
date: 2025-01-01
abbr: "CAZAC"
fullName: "Constant Amplitude Zero Auto-Correlation"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cazac/"
summary: "CAZAC posloupnosti jsou matematické posloupnosti s konstantní amplitudou v časové oblasti a nulovou autokorelací pro nenulové posuny. Jsou základním prvkem v technologiích 3GPP LTE a 5G NR pro generov"
---

CAZAC je matematická posloupnost s konstantní amplitudou a nulovou autokorelací, používaná v technologiích 3GPP LTE a 5G NR pro generování referenčních a synchronizačních signálů díky svým ideálním vlastnostem pro odhad kanálu a časování.

## Popis

CAZAC posloupnosti představují třídu komplexních posloupností charakterizovaných dvěma klíčovými matematickými vlastnostmi: konstantní obálkou (amplitudou) v časové oblasti a dokonalou periodickou autokorelací, což znamená, že korelace posloupnosti s časově posunutou verzí sebe sama je nulová pro všechny nenulové posuny. Nejvýznamnějšími CAZAC posloupnostmi používanými ve standardech 3GPP jsou Zadoff-Chu ([ZC](/mobilnisite/slovnik/zc/)) posloupnosti, pojmenované po svých tvůrcích. Zadoff-Chu posloupnost je definována kořenovým indexem 'u' a délkou 'N', kde N je prvočíslo. Posloupnost vykazuje konstantní amplitudu, což zajišťuje nízký poměr špičkového a průměrného výkonu ([PAPR](/mobilnisite/slovnik/papr/)), což je výhodné pro účinnost výkonového zesilovače. Její vlastnost nulové autokorelace znamená, že když je posloupnost zkorelována s cyklicky posunutou verzí sebe sama, výsledek je nulový, pokud není posun nulový, což poskytuje ideální ortogonalitu mezi různými cyklickými posuvy stejné kořenové posloupnosti.

Ve fyzické vrstvě architektury 3GPP LTE a 5G NR se CAZAC posloupnosti používají k vytvoření několika klíčových signálů. Primární synchronizační signály ([PSS](/mobilnisite/slovnik/pss/)) a sekundární synchronizační signály ([SSS](/mobilnisite/slovnik/sss/)) pro vyhledávání buněk a získání časování jsou odvozeny od Zadoff-Chu posloupností. Uplinkové demodulační referenční signály ([DM-RS](/mobilnisite/slovnik/dm-rs/)) a zkušební referenční signály ([SRS](/mobilnisite/slovnik/srs/)) jsou také konstruovány pomocí těchto posloupností, aby umožnily přesný odhad kanálu na základnové stanici. Dále je preambule kanálu fyzického náhodného přístupu ([PRACH](/mobilnisite/slovnik/prach/)) generována ze Zadoff-Chu posloupnosti, kde různé kořenové indexy a cyklické posuvy definují ortogonální preambule pro pokusy o náhodný přístup, což minimalizuje pravděpodobnost kolizí.

Generování a zpracování CAZAC posloupností zahrnuje specifické matematické operace definované ve specifikacích 3GPP. Základnová stanice a uživatelské zařízení (UE) generují tyto posloupnosti lokálně na základě známých vzorců a parametrů (kořenový index, délka posloupnosti, cyklický posuv). Pro odhad kanálu přijímač koreluje přijatý referenční signál (což je známá CAZAC posloupnost zkreslená kanálem) s lokálně vygenerovanou čistou posloupností. Díky vlastnosti nulové autokorelace tato korelace účinně izoluje impulsní odezvu kanálu, což umožňuje přesný odhad doby rozprostření kanálu a jeho frekvenční odezvy. To je zásadní pro koherentní demodulaci datových symbolů v systémech [OFDM](/mobilnisite/slovnik/ofdm/)/OFDMA.

Úloha CAZAC posloupností se rozšiřuje o poskytování ortogonality jak v časové, tak ve frekvenční oblasti. Různým uživatelským zařízením mohou být přiděleny různé cyklické posuvy stejné kořenové Zadoff-Chu posloupnosti pro jejich referenční signály, čímž vznikají ortogonální prostředky, které se navzájem neruší ani při současném vysílání. Tato ortogonalita je klíčová pro uplinkový víceuživatelský MIMO a pro přesný odhad kanálu ve scénářích s vysokou mobilitou. Vlastnost konstantní amplitudy také zjednodušuje konstrukci vysílače a zlepšuje účinnost výkonového zesilovače, protože snižuje zkreslení signálu a nežádoucí vyzařování mimo pásmo.

Shrnuto, CAZAC posloupnosti jsou základním matematickým nástrojem v moderních celulárních systémech. Jejich ideální korelační vlastnosti jsou základem kritických postupů fyzické vrstvy včetně synchronizace, odhadu kanálu a náhodného přístupu. Specifikace detailně popisující jejich aplikaci, jako je TS 36.211 pro LTE a TS 38.211 pro NR, definují přesné mapování těchto posloupností na časově-frekvenční prostředky, což zajišťuje interoperabilitu a robustní výkon napříč různými implementacemi sítí a výrobci zařízení.

## K čemu slouží

CAZAC posloupnosti byly zavedeny, aby řešily základní výzvy v bezdrátových systémech založených na ortogonálním frekvenčním multiplexu (OFDM), jako jsou LTE a NR. Předchozí přístupy pro referenční signály a synchronizaci používaly posloupnosti s méně ideálními korelačními vlastnostmi, což mohlo vést k vyšším chybám odhadu kanálu, zvýšenému rušení mezi uživateli a vyššímu poměru špičkového a průměrného výkonu (PAPR). Vysoký PAPR je pro OFDM zvláště problematický, protože snižuje účinnost výkonového zesilovače a zvyšuje náklady a spotřebu energie v uživatelských zařízeních. Potřeba posloupnosti s dokonalou periodickou autokorelací a konstantní amplitudou byla motivována požadavkem na vysoce přesné a nízko-složité zpracování signálu ve fyzické vrstvě.

Primární problém, který CAZAC posloupnosti řeší, je potřeba 'dokonalého' referenčního signálu pro odhad kanálu. Ve vícecestném (multipath) útlumovém kanálu musí přijímač odhadnout frekvenční odezvu kanálu, aby správně demoduloval data. Posloupnost s dokonalou autokorelací zajišťuje, že když je přijatý referenční signál zkorelován se známou vyslanou posloupností, výsledkem je impulsní odezva kanálu bez jakéhokoli rušení ze strany samotné posloupnosti. To vede k minimální chybě odhadu. Dále vlastnost konstantní amplitudy přímo bojuje proti vysokému PAPR vlastnímu vícekanálovým OFDM signálům, což umožňuje efektivnější a lineárnější zesílení výkonu.

Historicky, před přijetím CAZAC posloupností v 3GPP LTE (Rel-8), se v systémech jako WCDMA používaly jiné typy posloupností, například pseudo-náhodné šumové (PN) posloupnosti. Zatímco PN posloupnosti mají dobré vlastnosti vzájemné korelace, nemají dokonalou periodickou autokorelaci ani konstantní amplitudu CAZAC posloupností. Přechod na OFDMA pro uplink LTE (SC-FDMA) a downlink si vyžádal referenční signály, které byly ortogonální jak v časové, tak ve frekvenční oblasti a byly příznivé pro výkonové zesilovače. Matematické vlastnosti Zadoff-Chu posloupností z nich učinily ideální volbu, umožňující vysokou spektrální účinnost, robustní výkon při mobilitě a energetickou účinnost zařízení, které jsou charakteristické pro systémy 4G a 5G. Jejich přijetí bylo klíčovým faktorem pro výkonnostní skok od 3G k 4G.

## Klíčové vlastnosti

- Konstantní amplituda v časové oblasti, vedoucí k nízkému poměru špičkového a průměrného výkonu (PAPR)
- Dokonalá periodická autokorelace (nulová pro nenulové posuny) pro přesný odhad kanálu
- Generování ortogonálních signálů pomocí různých kořenových indexů a cyklických posuvů
- Základ pro kritické signály fyzické vrstvy (PSS, SSS, DM-RS, SRS, PRACH)
- Robustní výkon ve vysoce mobilních a vícecestných útlumových prostředích
- Umožňuje efektivní implementaci uplinkového víceuživatelského MIMO pomocí ortogonálních referenčních signálů

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services

---

📖 **Anglický originál a plná specifikace:** [CAZAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cazac/)
