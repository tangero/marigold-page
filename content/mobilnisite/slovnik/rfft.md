---
slug: "rfft"
url: "/mobilnisite/slovnik/rfft/"
type: "slovnik"
title: "RFFT – Real Fast Fourier Transform"
date: 2025-01-01
abbr: "RFFT"
fullName: "Real Fast Fourier Transform"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rfft/"
summary: "Výpočetně efektivní algoritmus pro provedení rychlé Fourierovy transformace na signálech s reálnými vstupními hodnotami. Je klíčový v 5G NR pro zpracování OFDM signálu, umožňuje úlohy jako odhad kanál"
---

RFFT je výpočetně efektivní algoritmus pro provedení rychlé Fourierovy transformace na signálech s reálnými vstupními hodnotami, klíčový v 5G NR pro úlohy zpracování OFDM signálu, jako je odhad kanálu.

## Popis

Real Fast Fourier Transform (RFFT) je specializovaná implementace algoritmu rychlé Fourierovy transformace optimalizovaná pro zpracování sekvencí vstupních dat s reálnými hodnotami. V kontextu 3GPP 5G New Radio (NR) se jedná o základní blok pro zpracování signálu hojně využívaný ve fyzické vrstvě, zejména pro vlnové formy Orthogonal Frequency Division [Multiplexing](/mobilnisite/slovnik/multiplexing/) ([OFDM](/mobilnisite/slovnik/ofdm/)). Systém OFDM je závislý na transformaci časově doménových signálů do frekvenční domény pro modulaci a demodulaci subnosných. Jelikož mnoho základních pásmových signálů, jako jsou fázové (I) a kvadraturní (Q) složky z analogově-digitálního převodníku, má reálné hodnoty, použití standardní komplexní [FFT](/mobilnisite/slovnik/fft/) by bylo výpočetně plýtvavé, protože by zpracovávala redundantní imaginární části nastavené na nulu.

Algoritmus RFFT využívá vlastnosti Hermitovské symetrie, která je vlastní Fourierově transformaci dat s reálnými hodnotami. Tato vlastnost říká, že pro reálnou vstupní sekvenci délky N vykazuje výsledný komplexní výstup ve frekvenční doméně symetrii: hodnota ve frekvenčním binu k je komplexně sdružená k hodnotě v binu N-k. V důsledku toho algoritmus RFFT potřebuje vypočítat a uložit pouze přibližně polovinu výstupních bodů (N/2 + 1 pro sudé N), což významně snižuje nároky na paměť a výpočetní operace. Typická implementace zahrnuje předzpracování reálného vstupu, provedení komplexní FFT o poloviční délce a následné zpracování výsledků pro rekonstrukci úplné sady unikátních frekvenčních binů.

V rámci architektury 5G NR je RFFT klíčovou součástí procesu odhadu kanálu a ekvalizace v přijímacím řetězci. Poté, co je z OFDM symbolu odstraněn cyklický prefix, jsou časově doménové vzorky přivedeny do bloku RFFT, který je převede na hodnoty subnosných ve frekvenční doméně. Tyto hodnoty jsou následně použity pro úlohy jako demodulace symbolů kvadraturní amplitudové modulace ([QAM](/mobilnisite/slovnik/qam/)), odhad frekvenční odezvy kanálu pomocí referenčních signálů (např. [DM-RS](/mobilnisite/slovnik/dm-rs/), [CSI-RS](/mobilnisite/slovnik/csi-rs/)) a provádění potlačení interference. Jeho efektivita přímo ovlivňuje spotřebu energie a zpracovatelskou latenci uživatelských zařízení (UE) a základnových stanic gNodeB, což jej činí nezbytným pro splnění požadavků 5G na vysokou propustnost a nízkou latenci.

Specifikace charakteristik RFFT, včetně podporovaných velikostí transformace a numerické přesnosti, je podrobně popsána v dokumentu 3GPP TS 26.118, který se zaměřuje na požadavky na výkon pro rádiový přenos a příjem UE. Velikosti transformace jsou sladěny s podporovanou OFDM numerologií (rozteč subnosných) a konfiguracemi šířky pásma v NR. Standardizací těchto požadavků na zpracování zajišťuje 3GPP interoperabilitu a konzistentní výkonnostní referenční hodnoty napříč různými výrobci čipových sad a síťových zařízení, což umožňuje robustní a efektivní globální ekosystém 5G.

## K čemu slouží

RFFT byl zaveden, aby řešil specifické výpočetní nároky fyzické vrstvy 5G New Radio, která využívá široká pásma a vysokou [OFDM](/mobilnisite/slovnik/ofdm/) numerologii. Zpracování těchto širokopásmových signálů pomocí standardních komplexních [FFT](/mobilnisite/slovnik/fft/) by na zařízeních představovalo zbytečnou výpočetní zátěž, vedoucí k vyšší spotřebě energie, větší ploše křemíku a potenciálním tepelným problémům, zejména v uživatelských zařízeních napájených baterií. Primární motivací bylo definovat standardizovanou, efektivní metodu zpracování signálu, která využívá inherentní vlastnosti základních pásmových signálů s reálnými hodnotami ke snížení složitosti bez obětování výkonu.

Historicky, jak se bezdrátové standardy vyvíjely od 3G přes 4G LTE až k 5G, se šířka kanálu a datové rychlosti exponenciálně zvyšovaly. LTE primárně používalo maximální šířku pásma 20 MHz, zatímco 5G NR podporuje šířky pásma až 400 MHz v pásmu FR2 (mmWave) a 100 MHz v pásmu FR1 (sub-6 GHz). Tento masivní nárůst vzorkovacích frekvencí a velikostí FFT učinil výpočetní efektivitu kritickým konstrukčním omezením. RFFT poskytuje matematicky optimální řešení, které snižuje potřebný počet násobení a sčítání téměř na polovinu ve srovnání s plnou komplexní FFT stejné délky.

Specifikací RFFT v Release 15 poskytlo 3GPP jasný výkonnostní cíl pro návrháře procesorů základního pásma. Vyřešilo problém definice, jak má UE efektivně provádět nezbytnou Fourierovu transformační operaci, a zajistilo, že všechna kompatibilní zařízení dosáhnou základní úrovně efektivity. Tato standardizace zabraňuje fragmentaci, kde by různí výrobci mohli implementovat proprietární optimalizace, což by potenciálně vedlo k problémům s interoperabilitou nebo nekonzistentními výkonnostními metrikami při testování a certifikaci sítě.

## Klíčové vlastnosti

- Optimalizováno pro sekvence vstupních dat s reálnými hodnotami
- Využívá Hermitovskou symetrii ke snížení počtu výstupních datových bodů
- Významně nižší výpočetní složitost než standardní komplexní FFT
- Definované velikosti transformace sladěné s 5G NR OFDM numerologií
- Klíčové pro OFDM demodulaci a odhad kanálu
- Standardizované požadavky na výkon v TS 26.118 pro kompatibilitu UE

## Související pojmy

- [FFT – Fast Fourier Transformation](/mobilnisite/slovnik/fft/)
- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats

---

📖 **Anglický originál a plná specifikace:** [RFFT na 3GPP Explorer](https://3gpp-explorer.com/glossary/rfft/)
