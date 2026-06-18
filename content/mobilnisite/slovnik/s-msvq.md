---
slug: "s-msvq"
url: "/mobilnisite/slovnik/s-msvq/"
type: "slovnik"
title: "S-MSVQ – Split-MultiStage Vector Quantization"
date: 2025-01-01
abbr: "S-MSVQ"
fullName: "Split-MultiStage Vector Quantization"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/s-msvq/"
summary: "Split-MultiStage Vector Quantization (S-MSVQ) je technika kvantizace v řečových a audio kodecích standardizovaná v 3GPP. Účinně komprimuje parametry lineární prediktivní kodéry (LPC), jako jsou lineár"
---

S-MSVQ je technika kvantizace řečových kodeků standardizovaná v 3GPP, která komprimuje LPC parametry rozdělením vektoru na podvektory a aplikací vícefázové kvantizace pro účinné kódování.

## Popis

Split-MultiStage Vector Quantization (S-MSVQ) je pokročilý kvantizační algoritmus používaný primárně pro účinnou digitální reprezentaci parametrů lineární prediktivní kodéry ([LPC](/mobilnisite/slovnik/lpc/)) v řečových a audio kodecích, jako jsou rodiny Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a [AMR-WB](/mobilnisite/slovnik/amr-wb/). Typicky kvantizuje parametry Line Spectral Frequencies ([LSF](/mobilnisite/slovnik/lsf/)) nebo Immittance Spectral Frequencies ([ISF](/mobilnisite/slovnik/isf/)), které reprezentují spektrální obálku řečového signálu. Klíčovou výzvou je kvantizovat vysokodimenzionální vektor (např. LPC 10. řádu dává 10-dimenzionální LSF vektor) s vysokou přesností při použití omezeného počtu bitů. S-MSVQ tuto výzvu řeší kombinací dvou technik: dělení a vícefázové kvantizace. Nejprve je vysokodimenzionální LSF vektor rozdělen na několik nízkodimenzionálních podvektorů (např. rozdělení 10-D vektoru na dva 5-D podvektory). Tento krok 'split' redukuje složitost prohledávání kodebooku z exponenciální na lineárnější škálu. Každý z těchto podvektorů je následně kvantizován pomocí vícefázového vektorového kvantizéru (MSVQ). V MSVQ se kvantizace provádí v několika sekvenčních fázích. První fáze použije kodebook k vytvoření hrubé aproximace vstupního podvektoru. Kvantizační chyba (reziduum) z první fáze je následně vypočtena a použita jako vstup pro druhou fázi, která ji kvantizuje pomocí dalšího kodebooku a poskytne tak zpřesnění. Tento proces může pokračovat pro další fáze. Konečný kvantovaný výstup je součtem kódových vektorů vybraných z kodebooku každé fáze. Indexy těchto vybraných kódových vektorů jsou vysílány do dekodéru. Dekodér, který má identické kodebooky, jednoduše sečte odpovídající kódové vektory, aby rekonstruoval kvantovaný LSF podvektor. Struktura S-MSVQ umožňuje velmi účinné přidělení bitů, kdy lze více bitů přidělit perceptuálně důležitějším podvektorům nebo fázím, čímž se optimalizuje celková percepční kvalita pro daný datový tok.

## K čemu slouží

S-MSVQ byl vyvinut k řešení kritického problému účinné a přesné kvantizace parametrů spektrální obálky v řečových kodecích s nízkým až středním datovým tokem. Jednoduchá skalární kvantizace [LPC](/mobilnisite/slovnik/lpc/) parametrů je neúčinná a vyžaduje příliš mnoho bitů. Plně prohledávaná vektorová kvantizace ([VQ](/mobilnisite/slovnik/vq/)) celého vysokodimenzionálního vektoru, ačkoli teoreticky optimální, je výpočetně neproveditelná kvůli exponenciálně rostoucí velikosti kodebooku a složitosti prohledávání. Motivací pro S-MSVQ bylo dosáhnout téměř optimální rovnováhy mezi kódovou účinností (minimalizace zkreslení pro daný bitový rozpočet) a výpočetní složitostí (umožnění realizace v reálném čase na zařízeních s omezeným výpočetním výkonem). Přístup 'split' přímo řeší problém složitosti prací na menších vektorech. Přístup 'multi-stage' poskytuje způsob postupného zpřesňování kvantizační přesnosti, což umožňuje flexibilní a účinnou strukturu přidělování bitů. Tato technika byla zásadní pro úspěch 3GPP kodeků jako [AMR](/mobilnisite/slovnik/amr/) a AMR-WB, které potřebovaly poskytovat vysokou kvalitu řeči v rozsahu datových toků pro okruhově spínané hlasové služby v sítích 2G, 3G a 4G. Umožnila těmto kodekům věnovat významnou část svého datového toku přesné reprezentaci perceptuálně klíčové spektrální obálky, což vedlo k čistému a přirozeně znějícímu hlasu i při tocích nízkých jako 4,75 kbps.

## Klíčové vlastnosti

- Kombinuje dělení vektorů a vícefázovou kvantizaci pro zvládnutí složitosti
- Účinně kvantizuje vysokodimenzionální spektrální parametry jako LSF/ISF
- Umožňuje flexibilní a percepčně motivované přidělování bitů napříč podvektory a fázemi
- Poskytuje dobrou rovnováhu mezi přesností kvantizace a výpočetní náročností
- Umožňuje vysoce kvalitní kódování řeči při nízkých až středních datových tocích
- Základní kvantizační metoda ve standardech jako AMR, AMR-WB a jejich vývojových verzích

## Definující specifikace

- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification

---

📖 **Anglický originál a plná specifikace:** [S-MSVQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-msvq/)
