---
slug: "ifft"
url: "/mobilnisite/slovnik/ifft/"
type: "slovnik"
title: "IFFT – Inverse Fast Fourier Transform"
date: 2025-01-01
abbr: "IFFT"
fullName: "Inverse Fast Fourier Transform"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ifft/"
summary: "Základní algoritmus digitálního zpracování signálu používaný ve vysílacím řetězci systémů založených na OFDM, jako jsou 4G LTE a 5G NR. Převádí reprezentaci signálu ve frekvenční oblasti (subnosné) zp"
---

IFFT je základní algoritmus digitálního zpracování signálu, který převádí signál ve frekvenční oblasti zpět na časovou průběhovou funkci pro přenos v systémech založených na OFDM, jako jsou 4G LTE a 5G NR.

## Popis

Inverzní rychlá Fourierova transformace (IFFT) je výpočetně efektivní algoritmus pro provedení inverzní diskrétní Fourierovy transformace ([IDFT](/mobilnisite/slovnik/idft/)). V mobilních komunikačních systémech 3GPP, zejména těch využívajících ortogonální multiplex s frekvenčním dělením ([OFDM](/mobilnisite/slovnik/ofdm/)), jako jsou LTE a NR, je IFFT klíčovým blokem zpracování fyzické vrstvy ve vysílacím řetězci. Její primární funkcí je transformovat sadu komplexních modulačních symbolů, z nichž každý je přiřazen konkrétní ortogonální subnosné ve frekvenční oblasti, na složenou sekvenci vzorků časového signálu připravenou k přenosu vzduchem.

Z architektonického hlediska IFFT pracuje uvnitř jednotky základního pásma vysílače. Proces začíná daty z vyšších vrstev, která jsou zakódována, modulována (např. pomocí QPSK, [16QAM](/mobilnisite/slovnik/16qam/)) a namapována na zdrojové prvky v rámci OFDM symbolu. Tyto zdrojové prvky odpovídají konkrétním aktivním subnosným. IFFT vezme tento blok N komplexních symbolů ve frekvenční oblasti (kde N je velikost [FFT](/mobilnisite/slovnik/fft/)/IFFT, např. 2048 pro 20 MHz kanál LTE) jako svůj vstup. Nepoužité subnosné nebo subnosné ochranného pásma jsou považovány za nulové vstupy. Algoritmus následně vypočítá reprezentaci v časové oblasti sečtením N komplexních sinusovek, z nichž každá kmitá na jiné frekvenci subnosné, vynásobených příslušnými modulačními symboly. Výstupem je blok N časových vzorků, které tvoří jeden OFDM symbol v časové oblasti, k němuž je následně připojena cyklická předpona.

Její princip fungování je založen na matematické zásadě, že jakákoli diskrétní časová sekvence může být reprezentována jako součet ortogonálních komplexních exponenciálních funkcí (sinusovek). IFFT tento součet efektivně vypočítává pomocí algoritmu s motýlkovou strukturou (jako je Cooley-Tukeyův algoritmus), který snižuje výpočetní složitost z O(N²) pro přímý výpočet IDFT na O(N log N). Tento masivní pokles počtu operací je tím, co umožňuje praktický vysokorychlostní OFDM přenos. Klíčovými součástmi její implementace jsou digitální signálové procesory ([DSP](/mobilnisite/slovnik/dsp/)) nebo specializované hardwarové bloky (jádra FFT/IFFT) v ASIC nebo FPGA, paměť pro uložení vstupních/výstupních dat a rotačních faktorů a řídicí logika pro tok dat. Její role je nepostradatelná: je mechanismem, který vytváří skutečný průběh signálu. Ortogonalita subnosných, zajištěná IFFT, umožňuje jejich těsné rozmístění ve frekvenci bez vzájemného rušení, což vede k vysoké spektrální účinnosti. Navíc převodem do časové oblasti může systém snadno přidat cyklickou předponu, která transformuje lineární konvoluci kanálu na kruhovou, což zjednodušuje ekvalizaci kanálu v přijímači na prosté dělení pro každou subnosnou ve frekvenční oblasti.

## K čemu slouží

IFFT existuje jako umožňující motor pro praktickou [OFDM](/mobilnisite/slovnik/ofdm/) modulaci, kterou 3GPP přijalo k řešení kritických problémů v širokopásmovém bezdrátovém spojení. Před OFDM se modulační schémata s jedním nosným potýkala s vysokorychlostním přenosem dat přes kanály s frekvenčně selektivním útlumem, běžnými v mobilním prostředí. V takových kanálech různé frekvenční složky širokopásmového signálu podléhají různým útlumům, což způsobuje mezisymbolové rušení ([ISI](/mobilnisite/slovnik/isi/)), které je složité ekvalizovat. OFDM, implementovaný pomocí IFFT/[FFT](/mobilnisite/slovnik/fft/), rozděluje širokopásmový kanál na mnoho úzkopásmových subnosných s plochým útlumem, což ekvalizaci značně zjednodušuje (pouze skalární násobení na subnosnou).

Historická motivace pro její zařazení sahá k výběru OFDMA pro downlink LTE v Rel-8, což znamenalo odklon od WCDMA používaného v 3G UMTS. Výpočetní náročnost provedení velké IDFT v reálném čase pro každý OFDM symbol byla hlavní překážkou. Vývoj rodiny algoritmů rychlé Fourierovy transformace poskytl potřebný průlom v efektivitě. Účelem IFFT je provést tuto kritickou transformaci z snadno manipulovatelné frekvenční mřížky zdrojů na přenositelný časový signál s přijatelnými výpočetními náklady.

Řeší omezení dřívějších vícekanálových konceptů tím, že poskytuje rychlou, stabilní a hardwarově implementovatelnou metodu. Bez IFFT by nebylo možné dosáhnout spektrální účinnosti, odolnosti vůči vícecestnému šíření a škálovatelné podpory šířky pásma, které definují 4G a 5G. Její vznik v oblasti zpracování signálu předchází 3GPP, ale její standardizace jako nedílné součásti OFDM průběhu zajišťuje, že všechny vysílače generují spektrálně kompatibilní signály, což garantuje, že přijímače používající doplňkovou FFT mohou data správně dekódovat, a tím zajišťuje globální interoperabilitu pro vysokorychlostní mobilní širokopásmový přenos.

## Klíčové vlastnosti

- Klíčový algoritmus pro generování OFDM a OFDMA průběhů v LTE a NR
- Efektivně převádí symboly z frekvenční oblasti na časové vzorky
- Umožňuje ortogonální multiplexování subnosných pro vysokou spektrální účinnost
- Snižuje výpočetní složitost na O(N log N) pomocí motýlkových operací
- Umožňuje jednoduchou ekvalizaci jedním koeficientem ve frekvenční oblasti na straně přijímače
- Implementována v hardwaru pro zpracování v reálném čase v čipech základního pásma

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [FFT – Fast Fourier Transformation](/mobilnisite/slovnik/fft/)

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats

---

📖 **Anglický originál a plná specifikace:** [IFFT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ifft/)
