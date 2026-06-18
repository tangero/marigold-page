---
slug: "fps"
url: "/mobilnisite/slovnik/fps/"
type: "slovnik"
title: "FPS – Frame Pattern Substitution"
date: 2025-01-01
abbr: "FPS"
fullName: "Frame Pattern Substitution"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fps/"
summary: "Frame Pattern Substitution (FPS) je technika používaná v kodecích 3GPP, zejména pro Voice over LTE (VoLTE) a následné hlasové služby, pro zvládání ztracených nebo poškozených řečových rámců. Nahrazuje"
---

FPS je technika v kodecích 3GPP, která nahrazuje ztracené nebo poškozené řečové rámce syntetizovaným vzorkem, aby udržela kontinuitu a srozumitelnost zvuku a zlepšila kvalitu hlasu v nepříznivých rádiových podmínkách.

## Popis

Frame Pattern Substitution (FPS) je klíčovou součástí mechanismů pro skrytí chyb v řečových a audio kodecích 3GPP, jako jsou Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) kodeky. Funguje na straně dekodéru přijímače, když je řečový rámec během přenosu přes rozhraní RAN ztracen nebo přijat s neopravitelnými chybami. Primárním cílem je zmírnit slyšitelný dopad takových ztrát, které by se jinak projevily jako rušivé přestávky, klikání nebo zkreslení v dekódovaném řečovém signálu. FPS funguje tak, že na základě dříve přijatých, správně dekódovaných řečových rámců a inherentních vlastností řečového signálu vygeneruje náhradní rámec. Tento syntetizovaný rámec je navržen tak, aby plynule navázal na tvar řečové vlny, co nejlépe zachoval charakteristiky výšky tónu a spektra, a tím udržel přirozenost a srozumitelnost.

Technická implementace FPS je úzce integrována s konkrétním algoritmem kodeku. Například v kodeku AMR, když je rámec označen jako vadný (např. pomocí kontroly [CRC](/mobilnisite/slovnik/crc/)), dekodér vyvolá algoritmus FPS. Ten využívá parametry z posledního dobrého rámce, jako jsou lineární predikční koeficienty ([LPC](/mobilnisite/slovnik/lpc/)) reprezentující filtr hlasového traktu a perioda základního tónu (pro znělé zvuky), k extrapolaci a vygenerování nového excitačního signálu. Tento syntetizovaný excitační signál je následně filtrován přes LPC syntézní filtr, aby vytvořil řečový signál v časové oblasti pro chybějící rámec. Proces často zahrnuje postupnou atenuaci energie substituovaných rámců při výskytu po sobě jdoucích ztrát, aby se zabránilo generování umělého trvalého šumu, a poskytnutí plynulejšího přechodu zpět k normálnímu dekódování, jakmile se obnoví příjem dobrých rámců.

FPS je kritickou součástí Radio Access Bearer ([RAB](/mobilnisite/slovnik/rab/)) a pozdějšího QoS rámce pro konverzační hlas. Její účinnost je klíčovým faktorem pro dosažení vysokých hodnot Mean Opinion Score ([MOS](/mobilnisite/slovnik/mos/)) u hlasových služeb, zejména v náročných rádiových prostředích na okraji buňky nebo při přechodech mezi buňkami. Algoritmy jsou detailně specifikovány v 3GPP specifikacích řady TS 26 (např. 26.092 pro AMR), aby byla zajištěna interoperabilita. Zatímco FPS řeší ztráty na úrovni rámců, je součástí širší sady odolných funkcí zahrnujících redundanci (např. duplikaci rámců v RoHC), správu vyrovnávací paměti pro kolísání zpoždění a adaptaci režimu kodeku, které společně zajišťují robustní služby Voice over IP (VoIP) v mobilních sítích.

## K čemu slouží

FPS byla vytvořena, aby řešila základní výzvu doručování kvalitního placeného hlasu přes paketové sítě, které jsou na rozdíl od okruhově přepínaných sítí 2G/3G inherentně náchylné ke ztrátám paketů a kolísání zpoždění. V okruhově přepínaných spojeních vyhrazené kanály poskytovaly konzistentní bitový proud, zatímco paketové sítě (jako IP-bazované jádro LTE a 5G) zacházejí s hlasem jako s datovými pakety náchylnými ke ztrátě. Bez FPS by ztracené hlasové rámce způsobily slyšitelné a rušivé výpadky, které by vážně degradovaly uživatelský zážitek. Tato technologie tento problém řeší tím, že poskytuje softwarově bazovanou, inteligentní 'domněnku' o chybějícím obsahu, což umožňuje pokračovat konverzaci s minimálním vnímaným narušením.

Motivace vycházela z přechodu na plně IP sítě v 3GPP Release 8 (LTE), kde byl standardizován VoLTE. Aby bylo VoIP proveditelné přes bezdrátové spoje s kolísavou kvalitou, bylo robustní skrytí chyb nezbytností. Předchozí přístupy v okruhově přepínaných systémech měly jinou, často hardwarově bazovanou, opravu chyb. FPS představuje posun k sofistikovanému zpracování signálu uvnitř samotného kodeku, optimalizovanému pro statistickou povahu ztrát paketů. Řeší omezení jednoduchých metod skrytí ztrát paketů ([PLC](/mobilnisite/slovnik/plc/)), které by mohly vkládat ticho nebo jednoduchý šum, tím, že generuje signál, který je akusticky konzistentní s probíhající řečí, a tak tam, kde je to možné, zachovává přirozenost hovoru a identitu mluvčího.

## Klíčové vlastnosti

- Generuje náhradní řečové rámce na základě parametrů z předchozích dobrých rámců
- Pro syntézu signálu využívá extrapolaci lineární predikce (LP) a periody základního tónu
- Obsahuje atenuaci energie pro po sobě jdoucí ztracené rámce, aby se zabránilo umělému trvalému šumu
- Bezešvě se integruje s stavovými automaty kodeku (např. dekodér AMR, EVS)
- Algoritmicky specifikováno v řadě 3GPP TS 26 pro interoperabilitu
- Kritické pro udržení vysokého Mean Opinion Score (MOS) v nepříznivých rádiových podmínkách

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 22.864** (Rel-15) — 5G Network Operation Use Cases & Requirements
- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TR 38.835** (Rel-18) — Technical Report on XR Enhancements for NR
- **TS 48.020** (Rel-19) — PLMN Rate Adaptation Functions

---

📖 **Anglický originál a plná specifikace:** [FPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/fps/)
