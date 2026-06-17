---
slug: "mp-mlq"
url: "/mobilnisite/slovnik/mp-mlq/"
type: "slovnik"
title: "MP-MLQ – Multipulse Maximum Likelihood Quantization"
date: 2025-01-01
abbr: "MP-MLQ"
fullName: "Multipulse Maximum Likelihood Quantization"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mp-mlq/"
summary: "Pokročilý algoritmus řečového kodeku používaný v sítích 3GPP pro služby hlasové komunikace vysoké kvality. Jedná se o typ kodéru s lineární predikcí a kódovou excitací (CELP), který efektivně reprezen"
---

MP-MLQ je pokročilý algoritmus řečového kodeku používaný v sítích 3GPP pro služby hlasové komunikace vysoké kvality, založený na lineární predikci s kódovou excitací pro efektivní reprezentaci řečových signálů.

## Popis

Multipulse Maximum Likelihood Quantization (MP-MLQ) je algoritmus kódování řeči patřící do rodiny Code-Excited Linear Prediction ([CELP](/mobilnisite/slovnik/celp/)). Je standardizován v dokumentu 3GPP TS 26.110 pro řečový kodek Adaptive Multi-Rate Wideband ([AMR-WB](/mobilnisite/slovnik/amr-wb/)), kde funguje jako jeden z možných režimů pro vyšší přenosové rychlosti. Základním principem CELP je modelovat hlasový trakt pomocí lineárně prediktivního ([LP](/mobilnisite/slovnik/lp/)) filtru a reprezentovat zbytkový excitační signál pomocí kódové knihy. MP-MLQ konkrétně zdokonaluje modelování excitace. V tomto algoritmu je excitace reprezentována sekvencí pulsů (multipulse) s proměnnými pozicemi a amplitudami. Část 'Maximum Likelihood Quantization' odkazuje na sofistikovanou metodu používanou pro výběr optimální kombinace pozic pulsů a jejich zesílení, která při průchodu LP syntézním filtrem vytvoří syntetizovanou řeč nejbližší (v percepčním smyslu) původní vstupní řeči.

Proces kódování zahrnuje několik stupňů. Nejprve je na rámci řeči provedena lineárně prediktivní analýza pro získání koeficientů LP filtru, které jsou kvantovány a přenášeny. LP filtr je pak použit k vytvoření váženého kritéria chyby, které zvýrazňuje percepčně důležité frekvence. Kodér prohledává strukturovanou multipulsní kódovou knihu, aby našel excitační sekvenci minimalizující tuto percepčně váženou chybu mezi původní a syntetizovanou řečí. Toto prohledávání je výpočetně náročné, ale poskytuje syntézu vysoké kvality. Parametry popisující vybrané pozice pulsů a jejich amplitudy jsou kvantovány a spolu s LP parametry odeslány do dekodéru. Dekodér použije tyto přijaté parametry k rekonstrukci excitačního signálu a jeho průchodem LP syntézním filtrem reprodukuje řečový signál.

Uvnitř kodeku AMR-WB je MP-MLQ využíván pro režimy s vyšší přenosovou rychlostí (např. 23,85 kbit/s). Samotný AMR-WB poskytuje škálu přenosových rychlostí pro přizpůsobení se podmínkám kanálu a MP-MLQ v rámci této škály poskytuje nejvyšší věrnost. Kodek pracuje s 20ms rámci řeči. Použití MP-MLQ umožňuje velmi přirozenou a čistou kvalitu řeči, blížící se kvalitě pevné sítě, což je klíčové pro širokopásmový řečový prožitek (šířka pásma 50-7000 Hz). To jej činí vhodným pro Voice over LTE (VoLTE) a další služby hlasové komunikace vysoké kvality v sítích 4G a 5G. Složitost vyhledávacího algoritmu MP-MLQ znamená, že vyžaduje větší výpočetní výkon než jednodušší metody s algebraickou kódovou knihou (jako [ACELP](/mobilnisite/slovnik/acelp/) používaný v nižších režimech AMR-WB), ale tento kompromis je přijatelný pro pevné nebo mobilní scénáře s vysokou kapacitou, kde je kvalita prvořadá.

## K čemu slouží

MP-MLQ byl vyvinut za účelem posunutí hranic kvality řeči v rámci omezení digitálních mobilních komunikačních kanálů. Dřívější řečové kodeky, jako běžný [AMR](/mobilnisite/slovnik/amr/) (úzkopásmový), poskytovaly dobrou kvalitu, ale v omezeném pásmu (300-3400 Hz). Snaha o přirozenější, 'tváří v tvář' kvalitu hlasu vedla k širokopásmové řeči (50-7000 Hz). Kódování širšího pásma zvuku však vyžaduje více bitů nebo efektivnější algoritmy. MP-MLQ řeší tuto potřebu efektivity při vyšších přenosových rychlostech.

Řeší problém přesné reprezentace komplexního excitačního signálu v [CELP](/mobilnisite/slovnik/celp/) modelu. Jednodušší stochastické nebo algebraické kódové knihy ([ACELP](/mobilnisite/slovnik/acelp/)) jsou efektivní, ale mohou při nižších přenosových rychlostech zavádět artefakty. Pro vysoce kvalitní režimy [AMR-WB](/mobilnisite/slovnik/amr-wb/) poskytuje MP-MLQ flexibilnější a přesnější reprezentaci excitace, což vede k čistší syntetizované řeči s menším šumem a zkreslením. Jeho vytvoření bylo motivováno snahou nabídnout škálovatelný kodek (AMR-WB), který by mohl poskytnout jasnou kvalitativní výhodu pro VoLTE a další hlasové služby založené na IP, což by jim pomohlo konkurovat tradičním hlasovým službám v komutovaných okruzích a stát se preferovanou službou pro uživatele. MP-MLQ v kombinaci se širší šířkou pásma byl klíčovým faktorem umožňujícím zážitek HD Voice v mobilních sítích.

## Klíčové vlastnosti

- Multipulsní reprezentace excitačního signálu v CELP kodeku
- Používá kvantizaci s maximální věrohodností pro optimální výběr parametrů pulsů
- Poskytuje širokopásmovou řeč vysoké věrnosti (50-7000 Hz)
- Používá se v režimech s vysokou přenosovou rychlostí kodeku AMR-WB (např. 23,85 kbit/s)
- Minimalizace percepčně vážené chyby během kódování
- Vyšší výpočetní složitost ve srovnání s metodami používajícími algebraickou kódovou knihu

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [CELP – Code Excited Linear Prediction](/mobilnisite/slovnik/celp/)

## Definující specifikace

- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks

---

📖 **Anglický originál a plná specifikace:** [MP-MLQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/mp-mlq/)
