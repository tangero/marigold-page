---
slug: "aac-ltp"
url: "/mobilnisite/slovnik/aac-ltp/"
type: "slovnik"
title: "AAC-LTP – Advanced Audio Coding Long Term Predictor Object Type"
date: 2025-01-01
abbr: "AAC-LTP"
fullName: "Advanced Audio Coding Long Term Predictor Object Type"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aac-ltp/"
summary: "AAC-LTP je specifický objektový typ (profil) v rámci rodiny Advanced Audio Coding (AAC) standardizovaný organizací 3GPP pro mobilní komunikaci. Zahrnuje nástroj dlouhodobého prediktoru (Long Term Pred"
---

AAC-LTP je specifický profil AAC standardizovaný organizací 3GPP, který využívá nástroj dlouhodobého prediktoru (Long Term Predictor) ke zlepšení komprese a kvality zvuku pro řeč a obecný audio signál v mobilních sítích.

## Popis

Advanced Audio Coding Long Term Predictor (AAC-LTP) je specifický audio objektový typ definovaný v rámci standardu MPEG-4 [AAC](/mobilnisite/slovnik/aac/) a přijatý organizací 3GPP pro použití v mobilní telekomunikaci. Jako objektový typ představuje konkrétní konfiguraci nebo profil kodeku AAC, který specifikuje použité kódovací nástroje. Jádrem AAC-LTP je integrace dlouhodobého prediktoru (Long Term Predictor) do standardního transformačního kódovacího rámce AAC. Samotný AAC je percepční audio kodek založený na modifikované diskrétní kosinové transformaci ([MDCT](/mobilnisite/slovnik/mdct/)), která převádí audio signály z časové domény do frekvenční reprezentace, což umožňuje efektivní kvantování na základě psychoakustických modelů pro odstranění neslyšitelných informací.

Dlouhodobý prediktor ([LTP](/mobilnisite/slovnik/ltp/)) je klíčovou odlišující vlastností tohoto objektového typu. Na rozdíl od standardního AAC, který může používat jiné predikční nástroje jako Temporal Noise Shaping (TNS) nebo se spoléhat pouze na vnitrorámcové kódování, LTP zavádí formu dlouhodobé predikce napříč více audio rámci. Funguje tak, že analyzuje periodické nebo kvaziperiodické složky v audio signálu, které jsou běžné ve zvuku znělé řeči a u některých hudebních tónů. Prediktor identifikuje redundanci mezi vzdálenými vzorky (v delším časovém rozpětí než krátkodobé prediktory) a tuto redundanci kóduje efektivněji, čímž snižuje datový tok potřebný pro danou úroveň vnímané kvality zvuku nebo zlepšuje kvalitu při pevném datovém toku.

Z architektonického hlediska je v rámci systému 3GPP AAC-LTP implementován jako součást vrstvy mediálních kodeků v uživatelském zařízení (UE) a síťových prvcích, jako je Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) nebo Multimedia Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)). Pracuje s audio rámci, typicky o délce 20 ms. Proces kódování zahrnuje: 1) Časově-frekvenční transformaci pomocí MDCT, 2) Psychoakustické modelování pro určení prahů maskování, 3) Aplikaci dlouhodobého prediktoru (LTP) pro využití mezirámcové redundancy, 4) Kvantování a entropické kódování spektrálních dat a parametrů prediktoru. Dekodér tento proces obrací a pomocí přijatých parametrů LTP přesně rekonstruuje predikované složky signálu, čímž syntetizuje výstupní audio.

Jeho role v síti 3GPP je primárně v rámci přenosové a služební vrstvy pro doručování audia. Je podporovaným kodekem pro okruhově spínané i paketově spínané hlasové služby (např. v časných nasazeních EPS pro scénáře přechodu na VoLTE), multimediální zprávy ([MMS](/mobilnisite/slovnik/mms/)) a streamovací služby. Začlenění LTP jej činí zejména robustním a efektivním pro obsah dominovaný řečí ve srovnání s objektovými typy AAC Main nebo AAC Low Complexity ([LC](/mobilnisite/slovnik/lc/)), neboť nabízí dobrou rovnováhu mezi výpočetní složitostí a kompresním výkonem. Je definován v dokumentu 3GPP TS 26.401, který specifikuje obecné funkce zpracování audia pro audio kodeky.

## K čemu slouží

AAC-LTP byl vytvořen pro uspokojení potřeby vysoce kvalitního, efektivního a robustního standardu pro kódování zvuku vhodného pro omezení mobilních sítí. Před jeho standardizací ve vydání 3GPP Release 8 se mobilní audio služby spoléhaly na kodeky jako [AMR-NB](/mobilnisite/slovnik/amr-nb/)/WB pro řeč a jednodušší AAC profily pro obecný audio obsah. Tyto kodeky byly často optimalizovány pro konkrétní typ obsahu (řeč vs. hudba) a mohly být pro smíšený obsah neefektivní nebo poskytovat nižší kvalitu. Motivací bylo využít pokročilou kompresi MPEG-4 AAC a zároveň zlepšit jeho výkon pro periodické signály charakteristické pro řeč, aniž by byla vyžadována velmi vysoká složitost zpětně adaptivního prediktoru profilu AAC Main.

Dlouhodobý prediktor (LTP) konkrétně řeší problém efektivního kódování periodicty základního tónu (pitch) ve zvucích znělé řeči. Standardní AAC, ačkoli je výborný pro hudbu, tuto dlouhodobou korelaci explicitně nemodeluje, což může vést k vyšším datovým tokům pro řeč nebo k artefaktům. Integrací LTP dosahuje AAC-LTP lepší kvality řeči při nižších datových tocích ve srovnání s AAC-LC, což jej činí vhodnějším pro hlasově orientované aplikace a služby, kde je přenosová kapacita omezená. Jeho návrh navíc zohledňuje požadavky na odolnost vůči chybám v bezdrátových kanálech; struktura prediktoru může do určité míry pomoci zmírnit dopad ztráty rámců, protože dekodér může pro predikci využívat dříve správně přijaté rámce.

Historicky jeho zavedení ve vydání Release 8 časově souviselo s rozšířením služeb 3GPP mimo základní hlasové služby směrem k bohatším multimédiím. Poskytl síťovým operátorům a výrobcům zařízení standardizovanou, licenčně podmíněnou, ale technicky pokročilou možnost audio kodeku, který dokáže zpracovat jak řeč, tak audio s dobrou účinností, čímž podpořil vývoj směrem ke konvergentním IP multimediálním službám (IMS). Odstranil omezení předchozích kodeků tím, že nabídl širší audio šířku pásma a lepší kvalitu pro hudbu než čistě řečové kodeky a lepší účinnost pro řeč než základní AAC profily, a sloužil tak jako univerzální nástroj v sadě audio kodeků 3GPP.

## Klíčové vlastnosti

- Integruje nástroj dlouhodobého prediktoru (Long Term Predictor, LTP) do rámce AAC pro vylepšenou kompresi periodických signálů
- Definován jako specifický MPEG-4 Audio Object Type (profil) v rámci standardů 3GPP
- Poskytuje zvýšenou účinnost kódování řeči a lepší kvalitu ve srovnání se standardním profilem AAC Low Complexity
- Podporuje široké rozpětí datových toků a audio šířek pásma vhodných pro mobilní aplikace
- Navržen s ohledem na robustnost v prostředích náchylných k chybám při bezdrátovém přenosu
- Umožňuje vysokou kvalitu zvuku pro služby jako hlasové hovory, zasílání zpráv a streamování v sítích 3GPP

## Související pojmy

- [AAC – Advanced Audio Coding](/mobilnisite/slovnik/aac/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TS 26.401** (Rel-19) — Enhanced aacPlus Audio Codec Mapping

---

📖 **Anglický originál a plná specifikace:** [AAC-LTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/aac-ltp/)
