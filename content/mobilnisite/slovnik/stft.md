---
slug: "stft"
url: "/mobilnisite/slovnik/stft/"
type: "slovnik"
title: "STFT – Short-Term Fourier Transform"
date: 2025-01-01
abbr: "STFT"
fullName: "Short-Term Fourier Transform"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/stft/"
summary: "Technika zpracování signálu používaná v 3GPP pro analýzu nestacionárních signálů, jako jsou audio nebo rádiové průběhy. Rozděluje signál na krátké, překrývající se časové segmenty a pro každý vypočítá"
---

STFT je technika zpracování signálu, která dělí nestacionární signál na krátké, překrývající se segmenty a pro každý z nich vypočítá Fourierovu transformaci, čímž vytvoří časově-frekvenční reprezentaci pro audiokodeky a rádiovou analýzu.

## Popis

Krátkodobá Fourierova transformace (Short-Term Fourier Transform, STFT) je základní technika digitálního zpracování signálu standardizovaná v rámci 3GPP pro analýzu časově proměnných signálů. Na rozdíl od standardní diskrétní Fourierovy transformace ([DFT](/mobilnisite/slovnik/dft/)), která předpokládá stacionaritu signálu, je STFT navržena pro nestacionární signály, jejichž frekvenční obsah se v čase mění, jako je řeč, audio nebo určité podmínky rádiového kanálu. Základní operace spočívá v segmentaci vstupního signálu na kratší, často se překrývající časová okna neboli rámce. Na každý segment je aplikována okénková funkce, například Hammingovo nebo Hannovo okno, pro snížení artefaktů spektrálního úniku. DFT je poté nezávisle vypočtena pro každý segment s okénkem. Výsledkem je dvourozměrná reprezentace: spektrogram, který ukazuje, jak se frekvenční spektrum vyvíjí v čase.

V architekturách 3GPP, zejména pro audio a řečové kodeky definované ve specifikacích jako TS 26.253, tvoří STFT analytickou páteř pro kódování v transformační doméně. Kodeky jako Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) nebo budoucí kodeky pro imerzivní audio používají STFT k převodu časových vzorků audia do časově-frekvenční domény. Zde lze aplikovat psychoakustické modely k identifikaci percepčně nevýznamných složek pro efektivní kvantizaci a kompresi. Parametry, jako je velikost okna, překrytí a délka transformace, jsou pečlivě voleny na základě charakteristik signálu a požadovaného kompromisu mezi časovým a frekvenčním rozlišením.

Pro aplikace v rádiové přístupové síti (RAN) lze STFT využít pro sondování kanálu, analýzu interference a snímání spektra. Aplikací STFT na přijaté základnové pásmové signály mohou inženýři pozorovat, jak se impulzní odezvy kanálu nebo vzorce interference mění v krátkých časových škálách, což je zásadní pro adaptivní modulaci a kódování, formování svazku a dynamické sdílení spektra. Implementace v síťových zařízeních zahrnuje optimalizované algoritmy, často využívající rychlou Fourierovu transformaci ([FFT](/mobilnisite/slovnik/fft/)), aby splnily požadavky na zpracování v reálném čase. Její role je zásadní pro umožnění kvalitních, efektivních multimediálních služeb a sofistikovaného řízení rádiových zdrojů v 5G-Advanced a dalších generacích.

## K čemu slouží

STFT byla zavedena do standardů 3GPP, aby vyřešila základní omezení tradiční Fourierovy analýzy při aplikaci na reálné komunikační signály. Signály jako lidská řeč, hudba a časově proměnné rádiové kanály jsou nestacionární; jejich statistické vlastnosti se v čase mění. [DFT](/mobilnisite/slovnik/dft/) celého signálu poskytuje pouze průměrné frekvenční vyjádření, čímž vymaže veškeré časové informace o tom, kdy se konkrétní frekvenční složky vyskytují. To je nedostatečné pro úlohy, jako je percepční audio kódování, kde je identifikace přechodových jevů (např. úder bubnu) versus trvalých tónů klíčová pro efektivitu komprese a kvalitu.

Před jejím formálním zahrnutím mohly návrhy kodeků používat proprietární nebo méně optimální časově-frekvenční transformace. Standardizace použití STFT, zejména od Release 18 a dále, poskytuje společný, efektivní matematický rámec pro kodeky příští generace pro audio a řeč. Umožňuje pokročilejší funkce, jako je rozšíření šířky pásma, potlačení šumu a kódování objektů pro imerzivní audio, tím, že nabízí přesnou, manipulovatelnou časově-frekvenční mřížku. Pro rádiové systémy poskytuje nástroj k překročení statických modelů kanálu, což umožňuje síti přizpůsobit se rychlému útlumu a změnám interference, což je nezbytné pro komunikaci s ultra-spolehlivým nízkým zpožděním ([URLLC](/mobilnisite/slovnik/urllc/)) a vysokofrekvenční pásma s výraznými Dopplerovými jevy.

## Klíčové vlastnosti

- Časově-frekvenční analýza nestacionárních signálů
- Segmentace signálu na překrývající se rámce s okénkem
- Vytvoření spektrogramu pro vizualizaci a zpracování
- Základ pro audiokodeky a řečové kodeky v transformační doméně
- Umožňuje aplikaci psychoakustických modelů pro percepční kódování
- Užitečné pro analýzu časově proměnných kanálů a interference v RAN

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [STFT na 3GPP Explorer](https://3gpp-explorer.com/glossary/stft/)
