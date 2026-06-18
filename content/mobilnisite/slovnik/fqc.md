---
slug: "fqc"
url: "/mobilnisite/slovnik/fqc/"
type: "slovnik"
title: "FQC – Frame Quality Classification"
date: 2025-01-01
abbr: "FQC"
fullName: "Frame Quality Classification"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fqc/"
summary: "Frame Quality Classification (FQC) je mechanismus používaný na rozhraních Iu (mezi RNC a Core Network) a Nb (mezi MSC Servers) v 3GPP UMTS sítích. Klasifikuje kvalitu přijatých hlasových rámců (např."
---

FQC je mechanismus na rozhraních Iu a Nb v sítích UMTS, který klasifikuje kvalitu přijatých hlasových rámců, aby umožnil selektivní zpracování a maskování chyb pro optimalizovanou hlasovou kvalitu.

## Popis

Frame Quality Classification (FQC) je funkční proces definovaný pro rozhraní Iu a Nb v architektuře 3GPP UMTS a pre-LTE core network. Jeho primární role je vyhodnotit a označit kvalitu jednotlivých hlasových rámců během jejich přenosu mezi síťovými elementy, konkrétně mezi Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) a Core Network (CN) přes rozhraní Iu a mezi uzly Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) nebo [MSC](/mobilnisite/slovnik/msc/) Servers přes rozhraní Nb. Tato klasifikace je klíčová, protože hlasové rámce mohou být poškozeny přes rozhraní Uu nebo během interního přenosu. FQC poskytuje standardizovaný 'ukazatel kvality', který cestuje spolu s datovým obsahem rámce (např. v Iu frame protocol nebo NbUP protokolu), a informuje tak následující uzly o integritě rámce, aby mohly uplatnit vhodné strategie zpracování.

Na rozhraní Iu provádí počáteční FQC RNC. Ten přijímá rámce od User Equipment (UE) přes rozhraní Uu a na základě kontrol fyzické vrstvy (jako jsou výsledky [CRC](/mobilnisite/slovnik/crc/)) každý rámec klasifikuje. Typická klasifikace je 'Good' (rámec je neporušený), 'Bad' (rámec je poškozený a nelze jej obnovit) nebo potenciálně 'Erased' (rámec byl očekáván, ale nebyl přijat). Tato klasifikace je pak vložena do Iu Data Frame odeslaného do Media Gateway (MGW) CN. MGW při přijetí těchto rámců může použít značku FQC k rozhodnutí o jejich zpracování. Například rámec 'Bad' může být úplně zahozen, nebo inteligentně předán dekodéru řečového kodeku, aby spustil jeho interní algoritmy Frame Erasure Concealment ([FEC](/mobilnisite/slovnik/fec/)) nebo Frame Pattern Substitution ([FPS](/mobilnisite/slovnik/fps/)), namísto pokusu o dekódování poškozených bitů, což by mohlo způsobit hlasité artefakty.

Na rozhraní Nb, které propojuje MGW v core network (např. ve scénáři transcodingu nebo tandem-free operation), jsou značky FQC zachovány a mohou být předávány dál. To umožňuje zpracování a směrování citlivé na kvalitu přes více síťových skoků. Mechanismus zabraňuje šíření poškozených rámců a umožňuje konzistentní aplikaci maskování chyb v konečném bodě dekódování, kterým je často terminující MGW nebo UE. FQC je specifikováno v protokolech jako Iu User Plane (IuUP) a Nb User Plane (NbUP), které detailně popisují strukturu rámce a kódování pole kvality. Je klíčovým prvkem pro udržení kvality hlasu od konce ke konci v UMTS tím, že ztrátu a poškození rámců činí explicitním a řízeným parametrem, nikoli skrytou vadou.

## K čemu slouží

FQC bylo vyvinuto pro řešení výzvy udržení hlasové kvality v segmentované síti, kde různé segmenty (rádiové, transportní, core) mají různé charakteristiky chyb. V raných digitálních systémech byly chyby často řešeny lokálně na každé hranici segmentu, což mohlo vést k suboptimální celkové kvalitě. Pro UMTS, s jeho oddělenými doménami RAN a CN, byla potřeba koordinované strategie řízení kvality. FQC to řeší tím, že poskytuje společný 'jazyk' kvality rámců, který cestuje s uživatelskými daty, což umožňuje každému síťovému uzlu činit informovaná rozhodnutí o tom, jak s každým rámcem nakládat.

Historický kontext je evoluce od kodeků GSM Full Rate/Enhanced Full Rate, kde bylo zpracování chyb těsněji vázáno na rádiový spoj, k éře UMTS s širší škálou kodeků (jako [AMR](/mobilnisite/slovnik/amr/)) a složitější síťovou architekturou zahrnující media gateway a potenciálně více transkódovacích bodů. Bez FQC by mohl poškozený rámec být slepě přeposlán [MGW](/mobilnisite/slovnik/mgw/), což by při jeho konečném dekódování způsobilo závažný audio artefakt. Alternativně by MGW mohlo zbytečně zahodit rámec, který by následující uzel mohl částečně obnovit. FQC umožňuje inteligentní zpracování citlivé na kvalitu od konce ke konci, což síti dovoluje minimalizovat vnímaný dopad chyb aplikací maskování v nejefektivnějším bodě, typicky co nejblíže posluchači.

## Klíčové vlastnosti

- Klasifikuje hlasové rámce do kategorií kvality (např. Good, Bad, Erased)
- Funguje na rozhraní Iu (RNC k CN) a Nb (mezi MGW)
- Vkládá značky kvality do rámců user plane protokolů (IuUP/NbUP)
- Umožňuje následujícím uzlům (MGW, UE) aplikovat vhodné maskování chyb
- Zabraňuje šíření a dekódování neobnovitelně poškozených rámců
- Umožňuje zpracování citlivé na kvalitu ve scénářích tandem-free operation

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)

## Definující specifikace

- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TS 26.453** (Rel-19) — EVS Codec Generic Frame Format for 3G CS Networks
- **TS 26.454** (Rel-19) — EVS Codec Mapping for 3G CS Networks
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [FQC na 3GPP Explorer](https://3gpp-explorer.com/glossary/fqc/)
