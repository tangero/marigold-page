---
slug: "qpp"
url: "/mobilnisite/slovnik/qpp/"
type: "slovnik"
title: "QPP – Quadratic Permutation Polynomial"
date: 2025-01-01
abbr: "QPP"
fullName: "Quadratic Permutation Polynomial"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/qpp/"
summary: "Matematická funkce používaná v 3GPP LTE a NR pro generování pseudonáhodných prokládacích vzorů pro kanálové kódování. Promíchává bitové sekvence za účelem zlepšení výkonu opravy chyb rozprostřením shl"
---

QPP je matematická funkce používaná v 3GPP LTE a NR pro generování pseudonáhodných prokládacích vzorů pro kanálové kódování, která promíchává bitové sekvence za účelem rozprostření shlukových chyb a zlepšení opravy chyb.

## Popis

Kvadratický permutační polynom (Quadratic Permutation [Polynomial](/mobilnisite/slovnik/polynomial/), QPP) je klíčovou součástí návrhu prokladače pro turbokódy specifikovaného v normách 3GPP, především pro LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR. Je definován jednoduchou kvadratickou funkcí tvaru π(x) = (f1 * x + f2 * x²) mod K, kde x je vstupní index bitu (0 ≤ x < K), K je velikost bloku prokladače a f1 a f2 jsou celočíselné koeficienty standardizované pro různé hodnoty K. Tato funkce generuje deterministickou, vzájemně jednoznačnou permutaci, která mapuje každou vstupní pozici bitu na jedinečnou výstupní pozici. Činnost prokladače je nedílnou součástí procesu turbokódování, kde je aplikován pro oddělení dvou složkových kodérů, čímž zajišťuje, že generované paritní bity jsou založeny na různém uspořádání vstupních systematických bitů.

Z architektonického hlediska je QPP prokladač implementován v subsystému kanálového kódování fyzické vrstvy. Když je přepravní blok připraven k vysílání, je v případě potřeby nejprve segmentován na kódové bloky, z nichž každý má velikost odpovídající podporované hodnotě K. Pro každý kódový blok vypočítá QPP funkce sekvenci prokládaných adres. Tato sekvence se použije k přeuspořádání vstupních bitů předtím, než vstoupí do druhého složkového kodéru turbokodéru. Klíčovou vlastností QPP je, že generuje prokladač bez konfliktů (contention-free), což znamená, že více paralelních procesorů může přistupovat k paměti prokladače současně bez kolizí, což je zásadní pro hardwarové implementace s vysokou propustností a nízkou latencí.

Jeho úlohou v síti je zlepšit výkon schématu dopředné opravy chyb ([FEC](/mobilnisite/slovnik/fec/)). Tím, že rozptyluje shlukové chyby – běžné v útlumových bezdrátových kanálech – na chyby podobné náhodným, umožňuje QPP prokladač iteračnímu procesu turbodekodéru je efektivněji opravit. Algebraická struktura QPP umožňuje efektivní výpočet prokládacího vzoru bez nutnosti velkých vyhledávacích tabulek, což zjednodušuje návrh kodéru i dekodéru. Tato matematická elegance v kombinaci s prokázaným zlepšením výkonu z hlediska bitové chybovosti ([BER](/mobilnisite/slovnik/ber/)) a blokové chybovosti ([BLER](/mobilnisite/slovnik/bler/)) z ní učinila trvalou volbu od LTE Release 8 až po 5G NR.

## K čemu slouží

QPP byl zaveden, aby řešil konkrétní omezení prokladačů používaných v dřívějších normách 3GPP, jako je UMTS. Předchozí prokladače pro turbokódy, například ve [WCDMA](/mobilnisite/slovnik/wcdma/), byly založeny na algoritmických pravidlech nebo permutacích využívajících tabulky, které mohly být složité na implementaci a negarantovaly vlastnost bez konfliktů. S nárůstem požadavků na přenosové rychlosti a propustnost u LTE vznikla potřeba prokládacího schématu, které by podporovalo vysoce paralelní architektury dekodérů (s využitím více [MAP](/mobilnisite/slovnik/map/) dekodérů) pro dosažení cílů v latenci a propustnosti. Vlastnost bez konfliktů je pro paralelismus klíčová, protože zabraňuje konfliktům při přístupu do paměti, když více procesorů současně čte/zapisuje prokládaná data.

Historicky hledání vhodného prokladače zahrnovalo vyvážení výkonu (vlastností vzdálenostního spektra) s realizační proveditelností. Řešení QPP vzešlo z akademického výzkumu, který ukázal, že kvadratické polynomy mohou generovat permutace s vynikajícími rozptylovými vlastnostmi a inherentními charakteristikami bez konfliktů pro řadu faktorů paralelizace. 3GPP přijalo QPP prokladače v LTE Release 8, aby standardizovalo výkonný, přitom realizovatelný prokladač, který by standard připravil na budoucí vývoj hardwarových možností. Vyřešil problém umožnění efektivních, paralelních implementací turbodekodérů při zachování nadřazeného výkonu opravy chyb potřebného pro vysokorychlostní mobilní broadband, což je základ, který pokračuje i v 5G NR.

## Klíčové vlastnosti

- Prokládání bez konfliktů umožňující paralelní architektury dekodérů
- Definován jednoduchým kvadratickým polynomem π(x) = (f1*x + f2*x²) mod K
- Standardizované koeficienty (f1, f2) pro více velikostí bloků (K)
- Algebraická struktura umožňuje výpočet bez velkých vyhledávacích tabulek
- Poskytuje vynikající rozptyl chyb pro zlepšení výkonu turbokódu
- Podporuje implementace kanálového kódování s vysokou propustností a nízkou latencí

## Definující specifikace

- **TS 36.201** (Rel-19) — LTE Physical Layer General Description

---

📖 **Anglický originál a plná specifikace:** [QPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/qpp/)
