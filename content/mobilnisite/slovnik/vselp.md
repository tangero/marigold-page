---
slug: "vselp"
url: "/mobilnisite/slovnik/vselp/"
type: "slovnik"
title: "VSELP – Vector-Sum Excited Linear Prediction"
date: 2025-01-01
abbr: "VSELP"
fullName: "Vector-Sum Excited Linear Prediction"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vselp/"
summary: "Vector-Sum Excited Linear Prediction (VSELP) je řečový kódovací algoritmus, konkrétně typ kodéru Code-Excited Linear Prediction (CELP). Byl standardizován pro použití v některých digitálních mobilních"
---

VSELP je řečový kódovací algoritmus a typ kodéru Code-Excited Linear Prediction (CELP), standardizovaný pro rané digitální mobilní systémy za účelem poskytnutí telefonní kvality řeči při středních přenosových rychlostech.

## Popis

Vector-Sum Excited Linear Prediction (VSELP) je řečový kódovací algoritmus patřící do rodiny vokodérů Code-Excited Linear Prediction ([CELP](/mobilnisite/slovnik/celp/)). Jako řečový kodek má za úkol digitálně komprimovat zvukový signál lidské řeči pro efektivní přenos přes digitální rádiové kanály. Algoritmus VSELP funguje tak, že modeluje lidský hlasový trakt pomocí filtru lineární prediktivní kódování ([LPC](/mobilnisite/slovnik/lpc/)). Budicí signál pro tento filtr – který představuje zbytkový zvuk po aplikaci LPC modelu – není generován jednoduchým pulzem nebo šumovým zdrojem, ale je vybírán z předdefinovaného kodebooku kandidátních budicích vektorů.

Klíčovou architektonickou inovací u VSELP je struktura jeho budicího kodebooku. Místo jediného velkého stochastického kodebooku VSELP typicky používá strukturovaný kodebook vytvořený z báze překrývajících se vektorů. Konečná budicí sekvence je tvořena součtem malého počtu těchto bázových vektorů, z nichž každý je škálován faktorem zesílení. Tato struktura umožňuje velmi efektivní vyhledávací proces. Enkódér analyzuje krátký rámec řeči (např. 20 ms), určí parametry pro LPC filtr (odrážející tvar hlasového traktu) a poté prohledá strukturovaný kodebook, aby našel budicí vektor, který při průchodu LPC filtrem vytvoří syntetizovanou řeč nejbližší originálu. Tyto parametry (LPC koeficienty, indexy kodebooku a zesílení) jsou poté přeneseny do dekodéru.

Dekodér rekonstruuje řeč tak, že pomocí přijatých indexů vyhledá budicí vektory ve svém identickém kodebooku, aplikuje zesílení a výsledný budicí signál nechá projít LPC syntetizačním filtrem. Klíčovými komponentami kodeku VSELP jsou LPC analýzní/syntetizační filtr, strukturovaný algebraický kodebook, adaptivní kodebook (pro modelování výšky tónu/pitch) a percepční váhový filtr používaný v procesu minimalizace chyby. Jeho role v síti, jak je uvedeno ve specifikacích 3GPP 46.002 a 46.020, spočívala v definované možnosti řečového kodeku, která zajišťovala interoperabilitu pro řečové služby v příslušných systémových implementacích.

## K čemu slouží

VSELP byl vytvořen za účelem poskytnutí vysoce kvalitní digitální komprese řeči vhodné pro omezenou šířku pásma raných digitálních mobilních rádiových systémů. Hlavní problém, který řešil, byla potřeba přenášet srozumitelnou řeč telefonní kvality v rámci omezené přenosové rychlosti kanálu (např. kolem 8 kbps nebo méně), a zároveň být realizovatelný s technologií digitálního zpracování signálu ([DSP](/mobilnisite/slovnik/dsp/)) konce 80. a počátku 90. let 20. století. Řešil tak omezení dřívějších řečových kodeků, jako bylo Regular Pulse Excitation (RPE) používané v plnorychlostním GSM, které měly nižší kvalitu, a složitějších variant [CELP](/mobilnisite/slovnik/celp/), které byly výpočetně neúnosné.

Motivace pro vývoj VSELP, zejména společností Motorola, která byla jeho průkopníkem, bylo dosažení příznivé rovnováhy mezi kvalitou řeči, přenosovou rychlostí, výpočetní náročností a odolností vůči chybám kanálu. Vyhledávání v jeho strukturovaném kodebooku bylo výrazně méně výpočetně náročné než úplné prohledávání nestrukturovaného stochastického kodebooku, což umožňovalo praktickou realizaci v reálném čase na dostupných DSP čipech. To bylo klíčovým předpokladem pro jeho přijetí v systémech, jako byl severoamerický standard digitálního mobilního systému [TIA](/mobilnisite/slovnik/tia/) IS-54 (D  AMPS).

V kontextu 3GPP jeho zařazení (odkazy v TS 46.002 pro slovník a TS 46.020 pro výkon) sloužilo k uchování záznamu o tomto historicky významném kodeku a k zajištění úplnosti specifikací pro systémy, které jej obsahovaly. Ačkoli byl VSELP v hlavních systémech 3GPP z velké části nahrazen pokročilejšími kodeky, jako jsou [AMR](/mobilnisite/slovnik/amr/) a [AMR-WB](/mobilnisite/slovnik/amr-wb/), které nabízejí lepší kvalitu a adaptabilitu, jeho vývoj byl důležitým krokem ve vývoji řečového kódování založeného na CELP, který demonstroval techniky pro snížení složitosti bez výrazného kompromisu v kvalitě.

## Klíčové vlastnosti

- Strukturovaný algebraický kodebook pro efektivní vyhledávání budicí sekvence
- Architektura Code-Excited Linear Prediction (CELP)
- Pracuje při středních přenosových rychlostech (např. 8 kbps)
- Přiměřená výpočetní náročnost vhodná pro DSP technologie 90. let
- Poskytuje srozumitelnost řeči na úrovni telefonní kvality
- Obsahuje adaptivní kodebook pro dlouhodobou (pitch) predikci

## Definující specifikace

- **TS 46.002** (Rel-19) — Introduction to GSM Half-Rate Speech Processing
- **TS 46.020** (Rel-19) — GSM Half Rate Speech Codec Specification

---

📖 **Anglický originál a plná specifikace:** [VSELP na 3GPP Explorer](https://3gpp-explorer.com/glossary/vselp/)
