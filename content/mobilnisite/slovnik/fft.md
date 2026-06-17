---
slug: "fft"
url: "/mobilnisite/slovnik/fft/"
type: "slovnik"
title: "FFT – Fast Fourier Transformation"
date: 2025-01-01
abbr: "FFT"
fullName: "Fast Fourier Transformation"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fft/"
summary: "Základní algoritmus digitálního zpracování signálu hojně využívaný v 3GPP rádiových technologiích, zejména v systémech založených na OFDM, jako jsou LTE a NR. Efektivně převádí signál mezi časovou a f"
---

FFT je základní algoritmus digitálního zpracování signálu, který efektivně převádí signál mezi časovou a frekvenční doménou a umožňuje klíčové operace, jako je generování ortogonálních podnosných v systémech založených na OFDM, například v LTE a NR.

## Popis

Rychlá Fourierova transformace (FFT) je výpočetně efektivní algoritmus pro výpočet diskrétní Fourierovy transformace ([DFT](/mobilnisite/slovnik/dft/)) a její inverze. V 3GPP rádiových přístupových sítích, konkrétně pro ortogonální multiplex s frekvenčním dělením ([OFDM](/mobilnisite/slovnik/ofdm/)) a ortogonální mnohonásobný přístup s frekvenčním dělením ([OFDMA](/mobilnisite/slovnik/ofdma/)) používané v LTE a NR, je FFT základní matematickou operací na fyzické vrstvě. Je implementována v digitálních signálových procesorech jak základnových stanic (gNB/[eNB](/mobilnisite/slovnik/enb/)), tak uživatelských zařízení (UE).

Pro vysílání se používá operace inverzní FFT ([IFFT](/mobilnisite/slovnik/ifft/)). Vysílač mapuje datové symboly (modulované bity z QPSK, [16QAM](/mobilnisite/slovnik/16qam/) atd.) na konkrétní podnosné ve frekvenční doméně. Na této sadě podnosných je pak provedena IFFT o velikosti N (kde N je velikost FFT, např. 2048 pro 20 MHz kanál LTE). Tím se frekvenční reprezentace převede na časový průběh – jeden OFDM symbol složený ze superpozice N ortogonálních sinusových podnosných. K tomuto časovému signálu je přidán cyklický prefix, aby se zmírnilo mezisymbolové rušení způsobené vícecestným šířením, než je signál odeslán do vysokofrekvenčního koncového stupně.

Pro příjem je proces obrácený. Přijímač vzorkuje příchozí časový průběh, odstraní cyklický prefix a na výsledné vzorky provede FFT. Tím se složený přijímaný signál převede zpět do frekvenční domény a oddělí se energie z každé ortogonální podnosné. Přijímač pak může extrahovat datové symboly z každé podnosné, vyrovnat vlivy kanálu na každé podnosné (což je díky struktuře OFDM jednodušší) a demodulovat je. Velikost FFT přímo souvisí s šířkou pásma systému: větší šířky pásma používají větší velikosti FFT pro zachování rozestupu podnosných (např. 15 kHz v LTE). Specifikace 3GPP (např. 36.104, 38.521) definují požadovaný výkon FFT jako součást charakteristik vysílače a přijímače v rádiovém spektru, což ovlivňuje metriky jako [EVM](/mobilnisite/slovnik/evm/) (velikost chybového vektoru) a únik do sousedního kanálu.

## K čemu slouží

Algoritmus FFT byl přijat ve standardech 3GPP, aby umožnil praktickou implementaci [OFDM](/mobilnisite/slovnik/ofdm/), přenosového schématu zvoleného pro LTE (Rel-8) a NR díky jeho vysoké spektrální účinnosti a odolnosti v prostředí s vícecestným šířením. Základním problémem, který OFDM řeší, je frekvenčně selektivní útlum ve širokopásmových kanálech, ale vyžaduje výpočetně proveditelnou metodu pro generování a dekódování velkého počtu těsně rozmístěných ortogonálních podnosných.

Přímé generování stovek podnosných pomocí jednotlivých oscilátorů bylo neproveditelné. Dvojice FFT/IFFT poskytuje elegantní řešení: umožňuje současné generování a dekódování všech podnosných prostřednictvím jediné blokové transformace. Aspekt „rychlosti“ je klíčový – snižuje složitost DFT z O(N²) na O(N log N), což umožňuje její realizaci v reálném čase pro velká N (např. 2048 nebo 4096) v rámci energetických a křemíkových omezení mobilních zařízení. Tato výpočetní efektivita byla klíčovým faktorem pro širokopásmové vícekanálové systémy, které definují 4G a 5G, a řešila omezení jedno-nosného přístupu CDMA používaného v 3G UMTS, který se při velmi vysokých přenosových rychlostech stával stále složitějším pro vyrovnávání.

## Klíčové vlastnosti

- Umožňuje efektivní převod z časové do frekvenční domény (FFT) a naopak (IFFT)
- Základní zpracovatelský blok pro modulaci a demodulaci OFDM/OFDMA v LTE a NR
- Velikost FFT se škáluje s šířkou pásma systému (např. 128, 256, 512, 1024, 2048, 4096)
- Implementována v digitálních základnopásmových procesorech síťových i uživatelských zařízení
- Umožňuje jednoduché vyrovnávání kanálu na každé podnosné ve frekvenční doméně
- Parametry výkonu (přesnost, šum) definovány v 3GPP specifikacích pro konformní testy RF

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)
- [DFT – Discrete Fourier Transform](/mobilnisite/slovnik/dft/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.747** (Rel-14) — Enhanced CRS and SU-MIMO IM Performance Requirements
- **TS 36.863** (Rel-12) — CRS Interference Mitigation for Homogeneous Networks
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.817** — 3GPP TR 38.817
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [FFT na 3GPP Explorer](https://3gpp-explorer.com/glossary/fft/)
