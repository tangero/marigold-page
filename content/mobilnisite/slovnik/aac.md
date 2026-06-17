---
slug: "aac"
url: "/mobilnisite/slovnik/aac/"
type: "slovnik"
title: "AAC – Advanced Audio Coding"
date: 2025-01-01
abbr: "AAC"
fullName: "Advanced Audio Coding"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aac/"
summary: "Advanced Audio Coding (AAC) je standardizovaný ztrátový audio kompresní kodek definovaný organizací 3GPP pro služby digitálního audia vysoké kvality. Poskytuje lepší zvukovou kvalitu při nižších přeno"
---

AAC je standardizovaný ztrátový audio kompresní kodek definovaný organizací 3GPP pro služby digitálního audia vysoké kvality, který poskytuje vynikající zvukovou kvalitu při nižších přenosových rychlostech pro efektivní doručování přes mobilní sítě.

## Popis

Advanced Audio Coding (AAC) je algoritmus percepčního kódování audia standardizovaný skupinou Moving Picture Experts Group ([MPEG](/mobilnisite/slovnik/mpeg/)) jako součást standardů [MPEG-2](/mobilnisite/slovnik/mpeg-2/) a MPEG-4 a přijatý organizací 3GPP pro použití v mobilních multimediálních službách. Funguje na principu využití psychoakustických vlastností lidského sluchu, jako je frekvenční maskování a časové maskování, k odstranění zvukových dat, která jsou pro posluchače nepostřehnutelná. Proces kódování zahrnuje transformaci časových zvukových signálů do frekvenční oblasti pomocí modifikované diskrétní kosinové transformace ([MDCT](/mobilnisite/slovnik/mdct/)), která umožňuje efektivní reprezentaci spektrálních složek. Na spektrální data jsou následně aplikovány kvantizace a entropické kódování, přičemž přidělení bitů je optimalizováno na základě percepčního modelu, aby byla maximalizována zvuková kvalita při dané přenosové rychlosti. Dekodér rekonstruuje zvukový signál inverzní transformací kvantovaných spektrálních koeficientů, což vede k výstupu vysoké věrnosti, který se blíží původnímu zdroji.

AAC podporuje široký rozsah vzorkovacích frekvencí (od 8 kHz do 96 kHz) a přenosových rychlostí (typicky od 8 kbps do přes 320 kbps), což jej činí univerzálním pro různé aplikace od řeči s nízkou přenosovou rychlostí až po hudbu vysoké kvality. Klíčové profily zahrnují [AAC-LC](/mobilnisite/slovnik/aac-lc/) (Low Complexity) pro všeobecné použití, HE-AAC (High Efficiency AAC, též známý jako AAC+), který kombinuje AAC s technikou Spectral Band Replication (SBR) pro vyšší účinnost při nízkých přenosových rychlostech, a HE-AAC v2, který přidává Parametric Stereo (PS) pro další snížení přenosové rychlosti u stereofonního obsahu. Tyto profily umožňují poskytovatelům služeb vybrat optimální kompromis mezi zvukovou kvalitou, přenosovou rychlostí a výpočetní složitostí pro různé případy použití.

V rámci architektury 3GPP je AAC specifikován jako povinný nebo doporučený kodek pro více služeb napříč různými technickými specifikacemi (TS). Je nedílnou součástí služby paketového streamování (PSS), služby multimediálního vysílání/multicastu ([MBMS](/mobilnisite/slovnik/mbms/)) a multimediální telefonní služby pro IMS ([MTSI](/mobilnisite/slovnik/mtsi/)). Kodek je zapouzdřen v transportních formátech, jako jsou [3GP](/mobilnisite/slovnik/3gp/) a [MP4](/mobilnisite/slovnik/mp4/) pro doručování založené na souborech, nebo protokolu Real-time Transport Protocol (RTP) pro streamování. Specifikace 3GPP definují přesné konformační body pro implementace kodérů a dekodérů, včetně testovacích sekvencí a požadavků na výkon, aby byla zajištěna interoperabilita mezi zařízeními a sítěmi. Účinnost AAC přímo ovlivňuje kapacitu sítě a uživatelský zážitek snížením šířky pásma potřebné pro audio služby při zachování vysoké percepční kvality.

Konstrukce AAC zahrnuje několik pokročilých technik pro dosažení svého výkonu. Používá banku filtrů s vyšším frekvenčním rozlišením než MP3, což umožňuje přesnější kontrolu tvarování kvantizačního šumu. Nástroj Temporal Noise Shaping (TNS) zmírňuje artefakty předozvuku v přechodových signálech aplikací predikce ve frekvenční oblasti. Perceptual Noise Substitution (PNS) nahrazuje šumově podobné složky signálu parametrickými popisy, čímž šetří bity. Tyto nástroje, kombinované se sofistikovaným multiplexováním bitového toku a mechanismy odolnosti proti chybám, činí AAC robustním pro náchylné mobilní kanály. Modulární struktura kodeku také usnadňuje škálovatelnost a rozšiřitelnost, podporuje vícekanálové audio konfigurace až do 48 kanálů a objektově orientované audio v pozdějších vývojových stupních.

## K čemu slouží

AAC byl vyvinut, aby uspokojil rostoucí poptávku po službách digitálního audia vysoké kvality přes sítě s omezenou šířkou pásma, zejména v mobilním prostředí. Předchozí audio kodeky, jako MP3 (MPEG-1 Audio Layer III), byly přelomové, ale měly omezení v účinnosti komprese a zvukové kvalitě při nižších přenosových rychlostech. Jak se mobilní sítě vyvíjely od 2G přes 3G a dále a umožňovaly multimediální aplikace, vznikla potřeba kodeku, který by mohl poskytovat kvalitu audia na úrovni CD při výrazně snížených přenosových rychlostech, aby se šetřily omezené rádiové zdroje a snížily datové náklady pro uživatele. AAC byl navržen jako nástupce MP3, nabízející lepší zvukovou kvalitu při podobných přenosových rychlostech nebo ekvivalentní kvalitu při přibližně o 30 % nižších přenosových rychlostech, což jej činí ideálním pro streamování hudby, zvukové stopy videí a služby s vylepšeným hlasem.

Přijetí AAC v rámci standardů 3GPP, počínaje Release 8, bylo hnací silou potřeby jednotného, vysoce výkonného audio kodeku pro paketové služby. Starší verze 3GPP se spoléhaly na řečově orientované kodeky, jako AMR-NB/WB pro hlas, a MP3 nebo AAC pro hudbu, ale postrádaly komplexní, optimalizované řešení pro širokou škálu audio obsahu. AAC tuto mezeru zaplnil tím, že poskytl jedinou rodinu kodeků schopnou efektivně zpracovávat hudbu, řeč a smíšený obsah. Jeho standardizace zajistila interoperabilitu napříč zařízeními a sítěmi, což podpořilo růst mobilních multimediálních ekosystémů. Snížením potřebné šířky pásma pro audio AAC také zmírnilo zahlcení sítě a umožnilo poskytovatelům služeb nabízet kvalitnější zážitky bez úměrného zvýšení nákladů na infrastrukturu.

Navíc škálovatelnost a systém profilů AAC mu umožnily přizpůsobit se různým síťovým podmínkám a možnostem zařízení. Například HE-AAC umožnil přijatelnou zvukovou kvalitu při velmi nízkých přenosových rychlostech (např. 24 kbps pro stereo), což bylo klíčové pro rané streamování přes 3G a vysílací služby jako MBMS. Tato účinnost byla zásadní pro uskutečnění streamování hudby a mobilní TV přes celulární sítě. Jak mobilní spotřeba dat rostla, role AAC se rozšířila o služby audia vysokého rozlišení a imerzivní formáty, čímž podpořila vývoj směrem k obohaceným mediálním zážitkům. Jeho kontinuální vylepšování prostřednictvím vydání 3GPP odráží neustálou snahu o optimální doručování audia v éře stále rostoucích kvalitativních očekávání a síťových požadavků.

## Klíčové vlastnosti

- Percepční kódování audia využívající MDCT pro vysoké frekvenční rozlišení
- Podpora více profilů: AAC-LC, HE-AAC (se SBR), HE-AAC v2 (se SBR a PS)
- Široký rozsah přenosových rychlostí (8 kbps až přes 320 kbps) a vzorkovacích frekvencí až do 96 kHz
- Pokročilé nástroje jako Temporal Noise Shaping (TNS) a Perceptual Noise Substitution (PNS)
- Škálovatelnost na vícekanálové audio konfigurace (např. surround 5.1)
- Odolnost proti chybám a robustní syntaxe bitového toku pro mobilní přenos

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.117** (Rel-19) — 5G Media Streaming Speech/Audio Capabilities
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.143** (Rel-19) — 5G Messaging Media Types and Codecs
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 26.401** (Rel-19) — Enhanced aacPlus Audio Codec Mapping
- **TS 26.402** (Rel-19) — Enhanced aacPlus Error Concealment & Processing
- **TS 26.403** (Rel-19) — Enhanced aacPlus AAC Encoder Specification
- **TS 26.405** (Rel-19) — Parametric Stereo Encoder for Enhanced aacPlus
- **TS 26.410** (Rel-19) — Enhanced aacPlus Floating-Point ANSI-C Code
- **TS 26.411** (Rel-19) — Enhanced aacPlus Fixed-Point ANSI-C Code
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [AAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/aac/)
