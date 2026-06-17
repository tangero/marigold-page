---
slug: "ltp"
url: "/mobilnisite/slovnik/ltp/"
type: "slovnik"
title: "LTP – Long Term Predictor"
date: 2025-01-01
abbr: "LTP"
fullName: "Long Term Predictor"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ltp/"
summary: "Long Term Predictor (LTP) je technika kódování řeči používaná v kodecích 3GPP, jako jsou AMR a AMR-WB. Modeluje dlouhodobou periodicitu (pitch) řečového signálu, aby efektivně odstranila redundanci, č"
---

LTP je technika kódování řeči používaná v kodecích 3GPP, která modeluje dlouhodobou periodicitu řeči za účelem odstranění redundance, čímž zlepšuje kompresi a kvalitu pro mobilní hlasové služby.

## Popis

Long Term Predictor (LTP) je klíčová komponenta algoritmu Algebraic Code-Excited Linear Prediction ([ACELP](/mobilnisite/slovnik/acelp/)) používaného v řečových kodecích 3GPP, jako je Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a Adaptive Multi-Rate Wideband ([AMR-WB](/mobilnisite/slovnik/amr-wb/)). Jejím hlavním úkolem je modelovat a využít dlouhodobou korelaci neboli pitch periodicitu vlastní znělým segmentům řeči. Znělé zvuky, jako jsou samohlásky, vykazují kvaziperiodickou strukturu, kde se tvar vlny přibližně opakuje v každém pitch periodě (typicky 2,5 ms až 20 ms). LTP tuto periodicitu identifikuje a používá ji k predikci aktuálního řečového rámce na základě zpožděné verze předchozího excitačního signálu.

Architektonicky LTP pracuje uvnitř smyčky syntézního filtru kodeku. Skládá se z dlouhodobého syntézního filtru, často reprezentovaného jako 1/(1 - gp*z^-T), kde 'T' je pitch lag (zpoždění) a 'gp' je pitch zesílení. Procedura analýzy syntézou kodeku určuje optimální celočíselný nebo zlomkový pitch lag (T) a odpovídající zesílení (gp), které minimalizují percepční chybu mezi originální a syntetizovanou řečí. Výstup LTP, nazývaný dlouhodobý predikční signál nebo excitační signál z adaptivního kodebooku, představuje periodickou složku excitace.

Tato predikovaná složka je následně kombinována se stochastickou složkou z pevného kodebooku (reprezentující inovaci nebo nepředvídatelné části signálu) za vzniku celkové excitace. Díky přesnému modelování pitch umožňuje LTP pevnému kodebooku soustředit se na reprezentaci zbývající inovace, což vede k efektivnější alokaci bitů. Parametry (lag a zesílení) jsou kvantovány a přenášeny do dekodéru, který rekonstruuje dlouhodobou predikci pomocí vlastního stavu filtru. Tento proces je zásadní pro dosažení vysoké kvality řeči při nízkých přenosových rychlostech, protože zachycuje významný zdroj redundance signálu.

Ve standardech jako TS 26.090 (AMR) a TS 26.190 (AMR-WB) jsou detaily implementace LTP, včetně rozsahu hledání, rozlišení (celočíselný nebo zlomkový lag) a kvantizace zesílení, pečlivě specifikovány pro zajištění interoperability. Jeho výkon je kritický napříč všemi vícebitovými režimy kodeku, přizpůsobujícími se různým podmínkám kanálu. Role LTP je tak zásadní, že vylepšení jeho přesnosti (např. rozlišení zlomkového lagu) přímo souvisí se zlepšenou kvalitou řeči, zejména pro hlasy s vysokým pitch (ženy, děti).

## K čemu slouží

Long Term Predictor byl vytvořen, aby řešil základní výzvu komprese řečových signálů pro digitální přenos přes kanály s omezenou přenosovou kapacitou, jako byly ty v raných mobilních sítích 2G a 3G. Předchozí řečové kodeky, ačkoli používaly lineární predikci pro modelování krátkodobé spektrální obálky, byly méně efektivní ve využívání dlouhodobých periodických korelací ve znělé řeči. To vedlo buď k vyšším požadovaným přenosovým rychlostem pro ekvivalentní kvalitu, nebo ke snížené kvalitě řeči při nižších přenosových rychlostech, což omezovalo kapacitu sítě a kvalitu služeb.

Motivace pro LTP vychází ze source-filter modelu produkce řeči, kde excitačním zdrojem pro znělé zvuky je kvaziperiodický glotální pulzní vlak. Explicitním modelováním této periocity LTP odstraňuje hlavní zdroj redundance, což umožňuje kodeku reprezentovat řečový signál s menším počtem bitů. To byla klíčová inovace, která umožnila vývoj velmi úspěšného kodeku [AMR](/mobilnisite/slovnik/amr/), který se stal povinným hlasovým kodekem pro sítě 3GPP GSM a UMTS. Vyřešil problém udržení robustní kvality hlasu za různých podmínek rádiového kanálu díky podpoře více přenosových rychlostí, přičemž efektivní modelování LTP bylo nezbytné při těch nižších rychlostech.

Historicky začlenění LTP do architektur code-excited linear prediction ([CELP](/mobilnisite/slovnik/celp/)) představovalo významný vývoj od jednodušších návrhů s multi-pulse nebo regular-pulse excitací. Vyřešilo to omezení těchto dřívějších přístupů, které neseparovaně modelovaly dlouhodobé a krátkodobé korelace, což vedlo k méně efektivnímu kódování excitace. Vytvoření LTP bylo hnací silou potřeby standardizovaného, vysoce výkonného algoritmu kódování řeči, který by maximalizoval počet hlasových kanálů na rádiový nosič při zachování kvality řeči na úrovni veřejné telefonní sítě, což byl klíčový ekonomický a technický faktor pro operátory mobilních sítí.

## Klíčové vlastnosti

- Modeluje dlouhodobou pitch periodicitu ve znělé řeči pomocí zpětnovazebního filtru
- Používá adaptivní kodebook ke generování periodické složky excitace
- Parametry zahrnují pitch lag (celočíselný nebo zlomkový) a pitch zesílení
- Integrální součást algoritmu ACELP v kodecích AMR a AMR-WB
- Snižuje přenosovou rychlost využitím redundance signálu
- Zlepšuje kvalitu řeči, zejména pro hlasy s vysokým pitch

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [ACELP – Algebraic Code-Excited Linear Prediction](/mobilnisite/slovnik/acelp/)

## Definující specifikace

- **TS 26.090** (Rel-19) — AMR Speech Codec Detailed Mapping Specification
- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification
- **TS 46.020** (Rel-19) — GSM Half Rate Speech Codec Specification
- **TS 46.042** (Rel-19) — GSM Half-Rate Voice Activity Detector Specification
- **TS 46.060** (Rel-19) — GSM Enhanced Full Rate Speech Codec
- **TS 46.082** (Rel-19) — GSM Enhanced Full Rate Voice Activity Detector

---

📖 **Anglický originál a plná specifikace:** [LTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ltp/)
