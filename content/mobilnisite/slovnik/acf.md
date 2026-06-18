---
slug: "acf"
url: "/mobilnisite/slovnik/acf/"
type: "slovnik"
title: "ACF – Autocorrelation Function"
date: 2025-01-01
abbr: "ACF"
fullName: "Autocorrelation Function"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/acf/"
summary: "Autokorelační funkce (ACF) je základním nástrojem zpracování signálu používaným k měření podobnosti signálu s jeho časově posunutou verzí. V systémech 3GPP je klíčová pro synchronizaci, odhad kanálu a"
---

ACF je funkce zpracování signálu, která měří podobnost mezi signálem a jeho časově zpožděnou kopií. Používá se v systémech 3GPP pro synchronizaci, odhad kanálu a detekci signálu.

## Popis

Autokorelační funkce (ACF) je matematická operace, která kvantifikuje míru podobnosti mezi daným signálem a jeho zpožděnou (posunutou) kopií v závislosti na časovém zpoždění (posunu). V kontextu bezdrátových komunikačních systémů 3GPP se jedná o základní statistický nástroj aplikovaný na fyzickou vrstvu při zpracování signálů. Formálně, pro diskrétní signál x[n] je autokorelace R_xx[τ] při posunu τ často odhadována jako R_xx[τ] = Σ (x[n] * x*[n+τ]), kde součet probíhá přes dostupné vzorky a x* označuje komplexně sdruženou hodnotu pro komplexní signály, jako jsou ty v [OFDM](/mobilnisite/slovnik/ofdm/). Tato funkce odhaluje vnitřní strukturu signálu, jeho periodicitu a přítomnost opakujících se vzorů.

V praktické implementaci je ACF klíčová pro několik základních funkcí přijímače. Během počátečního hledání buňky a synchronizace mobilní zařízení (UE) koreluje přijaté sekvence, jako je Primární synchronizační signál ([PSS](/mobilnisite/slovnik/pss/)) a Sekundární synchronizační signál ([SSS](/mobilnisite/slovnik/sss/)), s lokálními známými replikami. Pík ve výstupu vypočtené autokorelace indikuje úspěšné časové zarovnání. Pro odhad kanálu jsou využívány vlastnosti ACF vysílaných referenčních signálů (jako [DM-RS](/mobilnisite/slovnik/dm-rs/) nebo [SRS](/mobilnisite/slovnik/srs/)) k odhadu impulsní odezvy kanálu nebo jeho frekvenční selektivity. Šířka hlavního laloku ACF souvisí s šířkou pásma signálu, zatímco pokles jeho postranních laloků poskytuje informace o rozprostření zpoždění kanálu a přítomnosti vícecestných složek.

Výpočetní realizace ACF může být provedena přímo v časové oblasti nebo, efektivněji pro dlouhé sekvence, pomocí technik rychlé Fourierovy transformace ([FFT](/mobilnisite/slovnik/fft/)) prostřednictvím Wienerova–Khinchinova teorému, který říká, že ACF je inverzní Fourierova transformace výkonové spektrální hustoty signálu. V základnových stanicích 3GPP (gNB/[eNB](/mobilnisite/slovnik/enb/)) a v UE tyto korelace v reálném čase provádějí specializované hardwarové jednotky v digitálních signálových procesorech ([DSP](/mobilnisite/slovnik/dsp/)) nebo optimalizované softwarové knihovny. Výkonnost algoritmů spoléhajících na ACF, jako je filtrace přizpůsobená vzorku pro detekci preambule při náhodném přístupu (PRACH) nebo časové sledovací smyčky, přímo ovlivňuje citlivost systému, dobu akvizice a celkovou robustnost vůči rušení a šumu.

Dále je ACF hluboce spojena s návrhem rozprostíracích kódů a referenčních signálů. Kódy s ideálními autokorelačními vlastnostmi (ostrý pík při nulovém posunu a téměř nulové hodnoty jinde, jako jsou Zadoff-Chuovy sekvence) jsou ve specifikacích 3GPP vysoce ceněny pro synchronizační kanály a řídicí informace v uplinku. Tyto vlastnosti minimalizují falešné detekce a intersymbolové interference. Analýza ACF přijatého signálu také napomáhá pokročilým technikám přijímače, jako je potlačení interference a adaptivní ekvalizace, protože pomáhá charakterizovat statistické vlastnosti kanálu a šumu.

## K čemu slouží

Autokorelační funkce existuje jako základní matematický a signálový koncept nezbytný pro extrakci informace ze signálů zkreslených šumem a distorzí v komunikačních kanálech. Jejím hlavním účelem v systémech 3GPP je řešit základní problémy detekce, synchronizace a odhadu parametrů. Bez robustních korelačních technik by přijímač nemohl spolehlivě určit přesné načasování příchozí dávky signálu, odlišit ji od šumu na pozadí nebo přesně odhadnout zkreslující účinky rádiového kanálu, což by znemožnilo digitální komunikaci.

Historicky byly korelační techniky ústřední pro radar, sonar a rané systémy digitální komunikace. V kontextu celulárních sítí od GSM po 5G NR se výzvy zvětšily s rostoucími šířkami pásma, vyššími kmitočty nosné a složitějšími schématy mnohonásobného přístupu (jako OFDMA a SC-FDMA). Předchozí jednodušší metody detekce byly nedostatečné pro podmínky provozu s nízkým poměrem signál-šum (SNR) a silné vícecestné útlumy mobilního prostředí. ACF poskytuje statisticky optimální metodu (za předpokladu bílého Gaussovského šumu) pro detekci známých vzorů a tvoří páteř přizpůsobeného filtru, který maximalizuje SNR v rozhodovacím bodě.

Motivace pro její explicitní i implicitní použití v celých specifikacích 3GPP je hnána potřebou efektivity a spolehlivosti. Efektivní synchronizace snižuje spotřebu energie zařízení a přístupovou latenci. Přesný odhad kanálu, umožněný analýzou referenčních signálů s dobrými autokorelačními vlastnostmi, je zásadní pro dosažení vysoké spektrální účinnosti slibované MIMO a pokročilými modulačními schématy. ACF tedy není pouze teoretickým nástrojem, ale praktickým inženýrským pilířem, který řeší omezení nekoherentní detekce a umožňuje sofistikované postupy fyzické vrstvy definující moderní celulární technologii.

## Klíčové vlastnosti

- Umožňuje optimální detekci známých signálových vzorů v aditivním bílém Gaussovském šumu (AWGN) prostřednictvím přizpůsobené filtrace
- Základní pro postupy časové a frekvenční synchronizace, jako je detekce PSS/SSS a výpočet časového předstihu
- Používá se k odhadu impulsní odezvy kanálu a rozprostření zpoždění analýzou korelace přijatých referenčních signálů
- Podkládá návrh a vyhodnocování sekvencí (např. Zadoff-Chuovy, Goldovy kódy) pro synchronizační a referenční signály
- Umožňuje měření vlastností signálu, jako je periodicita, výkon šumu a přítomnost vícecestných složek
- Implementována efektivně v hardwaru/softwaru pomocí metod kruhové konvoluce založených na FFT pro dlouhé sekvence

## Definující specifikace

- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework
- **TS 46.042** (Rel-19) — GSM Half-Rate Voice Activity Detector Specification
- **TS 46.082** (Rel-19) — GSM Enhanced Full Rate Voice Activity Detector

---

📖 **Anglický originál a plná specifikace:** [ACF na 3GPP Explorer](https://3gpp-explorer.com/glossary/acf/)
