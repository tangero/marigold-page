---
slug: "acelp"
url: "/mobilnisite/slovnik/acelp/"
type: "slovnik"
title: "ACELP – Algebraic Code-Excited Linear Prediction"
date: 2025-01-01
abbr: "ACELP"
fullName: "Algebraic Code-Excited Linear Prediction"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/acelp/"
infografika: "/assets/slovnik/acelp.jpg"
summary: "ACELP je řečový kódovací algoritmus používaný ve standardech 3GPP pro efektivní kompresi hlasu. Poskytuje vysoce kvalitní řeč při nízkých přenosových rychlostech modelováním hlasového traktu a použití"
---

ACELP je řečový kódovací algoritmus používaný ve standardech 3GPP, který poskytuje vysoce kvalitní kompresi hlasu při nízkých přenosových rychlostech modelováním hlasového traktu a použitím algebraických kodebooků pro excitační signály.

## Popis

Algebraic Code-Excited Linear Prediction (ACELP) je sofistikovaný řečový kódovací algoritmus, který kombinuje lineární predikci s excitací založenou na kodebooku. Algoritmus pracuje tak, že analyzuje řečové signály v rámcích, typicky 20–30 milisekund, a rozděluje je na dvě hlavní složky: spektrální obálku (reprezentující filtr hlasového traktu) a excitační signál (reprezentující glotální pulzy). Složka lineární predikce modeluje hlasový trakt pomocí sady koeficientů lineární predikce, které jsou transformovány na lineární spektrální páry ([LSP](/mobilnisite/slovnik/lsp/)) pro efektivnější kvantizaci a přenos.

Excitační signál v ACELP je generován pomocí algebraických kodebooků, které obsahují předdefinované pulzní sekvence, jež lze efektivně reprezentovat pomocí algebraických struktur. Tyto kodebooky používají řídké algebraické vektory s pouze několika nenulovými pulzy, což umožňuje rychlé vyhledávací algoritmy během kódování. Enkodér prohledává kodebook, aby našel excitační sekvenci, která minimalizuje percepční chybu mezi původní a syntetizovanou řečí, přičemž používá vážené chybové kritérium zohledňující lidské sluchové vnímání.

Klíčové komponenty algoritmu ACELP zahrnují filtr pro analýzu lineární predikce, adaptivní kodebook (pro periodicitu základního tónu), pevný algebraický kodebook (pro inovaci) a percepční váhovací filtr. Adaptivní kodebook zachycuje dlouhodobou periodicitu znělých řečových segmentů, zatímco algebraický kodebook reprezentuje zbývající stochastické složky. Tyto prvky spolupracují v uzavřené smyčce přístupu analýza-syntézou, kde enkodér simuluje činnost dekodéru za účelem optimalizace kódovacích parametrů.

V sítích 3GPP tvoří ACELP jádro několika řečových kodeků včetně [AMR](/mobilnisite/slovnik/amr/) (Adaptive Multi-Rate), [AMR-WB](/mobilnisite/slovnik/amr-wb/) (Wideband) a [EVS](/mobilnisite/slovnik/evs/) (Enhanced Voice Services). Algoritmus pracuje s různými přenosovými rychlostmi, které lze dynamicky přizpůsobovat na základě síťových podmínek, s typickými rychlostmi v rozsahu od 4,75 do 12,2 kbps pro úzkopásmové a od 6,6 do 23,85 kbps pro širokopásmové aplikace. Tato flexibilita umožňuje síťovým operátorům vyvažovat kvalitu řeči vůči požadavkům na šířku pásma při zachování robustního výkonu za různých kanálových podmínek.

## K čemu slouží

ACELP byl vyvinut, aby vyřešil základní výzvu přenosu vysoce kvalitní řeči přes mobilní sítě s omezenou šířkou pásma. Před kodeky založenými na ACELP nabízely starší techniky řečového kódování, jako je Regular Pulse Excitation (RPE) a Vector Sum Excited Linear Prediction (VSELP), omezenou kvalitu při nízkých přenosových rychlostech nebo vyžadovaly nadměrnou výpočetní složitost. Mobilní průmysl potřeboval řešení, které by dokázalo poskytovat kvalitu řeči na úrovni veřejné telefonní sítě a zároveň efektivně využívat omezené zdroje rádiového spektra.

Algebraická struktura kodebooků ACELP byla speciálně navržena tak, aby ve srovnání s tradičními stochastickými kodebooky snížila výpočetní složitost, což umožnilo realizaci v reálném čase na mobilních zařízeních s omezeným výpočetním výkonem. Tato inovace umožnila efektivnější prohledávání kodebooků bez snížení kvality řeči, což vedlo k rozšířenému přijetí vysoce kvalitních digitálních hlasových služeb ve 2G, 3G a následujících mobilních generacích. Flexibilita algoritmu pracovat s více přenosovými rychlostmi také podpořila mechanismy adaptivního řízení rychlosti, které mohly reagovat na měnící se síťové podmínky.

ACELP dále řešil potřebu zpětné kompatibility a interoperability napříč různými síťovými generacemi a regiony. Tím, že poskytl robustní základ pro řečové kódování, který mohl být vylepšen prostřednictvím širších šířek pásma a lepších zpracovatelských technik, umožnil ACELP vývoj od úzkopásmových k širokopásmovým a super-širokopásmovým hlasovým službám při zachování základních charakteristik, jako je nízké zpoždění a postupné snižování kvality při chybových podmínkách.

## Klíčové vlastnosti

- Algebraická struktura kodebooku s řídkými pulzními vektory pro efektivní reprezentaci
- Optimalizace v uzavřené smyčce metodou analýza-syntéza pro percepční kvalitu
- Adaptivní více-rychlostní provoz podporující přenosové rychlosti od 4,75 do 23,85 kbps
- Lineární predikce s kvantizací LSP pro kódování spektrální obálky
- Integrovaný adaptivní kodebook pro modelování periody základního tónu
- Percepční váhovací filtr založený na charakteristikách lidského sluchu

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TS 26.071** (Rel-19) — AMR Speech Codec Introduction
- **TS 26.090** (Rel-19) — AMR Speech Codec Detailed Mapping Specification
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TS 26.171** (Rel-19) — Introduction to AMR-WB Speech Processing
- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.274** (Rel-19) — AMR-WB+ Codec Conformance Testing Specification
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification
- **TS 26.441** (Rel-19) — EVS Audio Processing Introduction
- **TS 26.442** (Rel-19) — EVS Codec Fixed Point ANSI-C Code
- **TS 26.443** (Rel-19) — EVS Codec Floating-Point C Code
- **TS 26.444** (Rel-19) — EVS Codec Conformance Test Sequences
- **TS 26.450** (Rel-19) — EVS Codec DTX System Level Aspects
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [ACELP na 3GPP Explorer](https://3gpp-explorer.com/glossary/acelp/)
