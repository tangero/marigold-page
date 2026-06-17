---
slug: "irfft"
url: "/mobilnisite/slovnik/irfft/"
type: "slovnik"
title: "IRFFT – Inverse Radio Frequency Fast Fourier Transform"
date: 2025-01-01
abbr: "IRFFT"
fullName: "Inverse Radio Frequency Fast Fourier Transform"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/irfft/"
summary: "Operace inverzní rychlé Fourierovy transformace aplikovaná v kontextu generování rádiových signálů, konkrétně pro vytváření časových průběhů OFDM/OFDMA z frekvenčních symbolů. Je to klíčová matematick"
---

IRFFT je operace inverzní rychlé Fourierovy transformace používaná v LTE a 5G NR vysílačích k vytváření časových průběhů OFDM/OFDMA z frekvenčních symbolů.

## Popis

Inverzní rychlá Fourierova transformace pro rádiové kmitočty (IRFFT) je kritická operace digitálního zpracování signálu ([DSP](/mobilnisite/slovnik/dsp/)) ve fyzické vrstvě vysílače systémů založených na ortogonálním frekvenčním multiplexu ([OFDM](/mobilnisite/slovnik/ofdm/)) a ortogonálním frekvenčním multiplexu s vícenásobným přístupem ([OFDMA](/mobilnisite/slovnik/ofdma/)), jako jsou LTE a 5G New Radio (NR). Je to inverzní operace k RFFT (rychlá Fourierova transformace pro rádiové kmitočty) prováděné v přijímači. Funkcí IRFFT je transformovat blok komplexních modulačních symbolů, mapovaných na konkrétní subnosné ve frekvenční oblasti, na odpovídající časový průběh, který může být převeden na analogový signál a vysílán vzduchem.

Technicky proces začíná po fázích kanálového kódování, modulace (např. QPSK, [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/), 256QAM) a mapování na zdrojové prvky ve vysílacím řetězci. Výstupem mapování je vektor komplexních symbolů pro sadu aktivních subnosných v rámci periody OFDM symbolu, s nulovými hodnotami přiřazenými ochranným pásmům a stejnosměrné subnosné. Algoritmus IRFFT vypočítává inverzní diskrétní Fourierovu transformaci ([IDFT](/mobilnisite/slovnik/idft/)) tohoto frekvenčního vektoru. Kvůli výpočetní efektivitě je IDFT implementována pomocí algoritmu inverzní rychlé Fourierovy transformace ([IFFT](/mobilnisite/slovnik/ifft/)), přičemž velikost (N) IFFT určuje celkový počet subnosných (včetně nulových) v šířce pásma systému. Například LTE běžně používá 2048bodovou IFFT pro 20 MHz kanál.

Výstupem IRFFT je diskrétní časová posloupnost představující složený OFDM symbol v časové oblasti. Kritickým následujícím krokem je přidání cyklického prefixu ([CP](/mobilnisite/slovnik/cp/)). CP je vytvořen zkopírováním části z konce tohoto časového symbolu a připojením na jeho začátek. Tento CP zmírňuje intersymbolové rušení (ISI) způsobené vícecestným šířením. Konečný časový signál, skládající se z po sobě jdoucích CP-OFDM symbolů, je následně převeden na analogový, převeden na nosnou frekvenci, zesílen a vysílán. IRFFT je tedy matematickým motorem, který umožňuje paralelní přenos dat na více ortogonálních subnosných, poskytuje odolnost proti frekvenčně selektivnímu útlumu a tvoří základ moderných širokopásmových bezdrátových rozhraní.

## K čemu slouží

IRFFT existuje jako základní umožňující technologie pro OFDM, který byl vybrán jako hlavní modulační schéma pro 4G LTE a 5G NR díky své vynikající výkonnosti v prostředích s vícecestným šířením. Před rozšířeným přijetím OFDM používaly systémy jako 3G UMTS širokopásmový vícenásobný přístup s kódovým dělením (WCDMA), který měl problémy s intersymbolovým rušením v kanálech s velkým zpožděním, což vyžadovalo složité ekvalizéry v přijímači. Účelem IRFFT (a celého vysílacího řetězce OFDM) je transformovat obtížný širokopásmový kanál s frekvenčně selektivním útlumem na soubor mnoha paralelních úzkopásmových subkanálů s plochým útlumem.

To řeší několik klíčových problémů: Výrazně zjednodušuje ekvalizaci kanálu v přijímači (redukuje na jednoduchou korekci amplitudy/fáze na jednotlivých subnosných), poskytuje vnitřní odolnost vůči zpoždění vícecestného šíření díky použití cyklického prefixu a umožňuje flexibilní vícenásobný přístup uživatelů (OFDMA) prostřednictvím přidělování různých sad subnosných různým uživatelům. Motivací pro jeho specifickou definici ve specifikacích 3GPP (např. pro testování výkonu) je zajistit interoperabilitu a konzistentní RF charakteristiky. Standardizací očekávaného výstupu procesu IRFFT (včetně parametrů jako velikost IFFT, vzorkovací frekvence a dodržování spektrální masky) 3GPP zaručuje, že vysílače od různých výrobců produkují průběhy, které jsou správně dekódovány jakýmkoli přijímačem odpovídajícím standardu.

Historicky byla výpočetní složitost IFFT/FFT překážkou, ale pokrok v DSP a technologii integrovaných obvodů ji učinil proveditelnou pro spotřebitelská zařízení. Formalizace IRFFT v 3GPP Release 15 pro NR také zohlednila nové parametry signálu, jako je flexibilní numerologie (různé rozestupy subnosných) a podpora širších šířek pásma, což vyžadovalo přesnou definici velikostí transformací a okenovacích funkcí pro zachování ortogonality a kontrolu emisí mimo pásmo.

## Klíčové vlastnosti

- Transformuje modulační symboly z frekvenční oblasti na časový průběh OFDM
- Implementována pomocí výpočetně efektivních algoritmů inverzní rychlé Fourierovy transformace (IFFT)
- Velikost IFFT (N) určuje celkový počet subnosných systému
- Zpracovává vstupní vektory obsahující datové symboly, referenční signály a nulové subnosné
- Výstup je připraven pro vložení cyklického prefixu (CP)
- Klíčová, standardizovaná operace zajišťující shodu vysílaného průběhu

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [FFT – Fast Fourier Transformation](/mobilnisite/slovnik/fft/)

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats

---

📖 **Anglický originál a plná specifikace:** [IRFFT na 3GPP Explorer](https://3gpp-explorer.com/glossary/irfft/)
