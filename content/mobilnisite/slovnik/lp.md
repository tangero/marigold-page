---
slug: "lp"
url: "/mobilnisite/slovnik/lp/"
type: "slovnik"
title: "LP – Linear Prediction"
date: 2025-01-01
abbr: "LP"
fullName: "Linear Prediction"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lp/"
summary: "Základní technika digitálního zpracování signálu hojně využívaná v řečových a audio kodecích k modelování spektrální obálky signálu. Předpovídá hodnotu vzorku jako lineární kombinaci jeho předchozích"
---

LP je základní technika digitálního zpracování signálu používaná v řečových kodecích k modelování spektrální obálky signálu předpovědí hodnoty vzorku jako lineární kombinace předchozích vzorků za účelem efektivní komprese.

## Popis

Lineární predikce (LP) je matematická operace, při které je budoucí hodnota diskrétního časového signálu odhadnuta jako vážený součet (lineární kombinace) jeho předchozích hodnot. V kontextu kódování řeči je řečový signál s(n) modelován jako výstup celopólového filtru (syntézního filtru) buzeného vstupním signálem e(n), což je buď periodický pulzní vlak (pro znělé zvuky), nebo bílý šum (pro neznělé zvuky). Vztah je vyjádřen jako s(n) = Σ (a_k * s(n-k)) + G * e(n), pro k=1 až p, kde 'a_k' jsou koeficienty lineární predikce (LPCs), 'p' je řád predikce a G je činitel zesílení. Koeficienty 'a_k' definují spektrální obálku neboli formanty řeči.

Proces kódování zahrnuje analýzu krátkého rámce řeči (např. 20 ms) za účelem výpočtu sady LPCs, které nejlépe předpovídají signál v tomto rámci. To se obvykle provádí řešením Yule-Walkerových rovnic pomocí metod jako je Levinson-Durbinova rekurze. Rozdíl mezi původním řečovým signálem a předpověděným signálem je LP reziduum, které reprezentuje buzení. Vysoce kvalitní kodeky toto reziduum dále kódují. Pro velmi nízké přenosové rychlosti může být reziduum modelováno parametrickým způsobem (jako v Algebraic Code-Excited Linear Prediction, [ACELP](/mobilnisite/slovnik/acelp/)), kdy se přenáší pouze typ buzení (znělé/neznělé), perioda základního tónu a index pevného kodebooku.

V dekodéru jsou přijaté LPCs použity k sestavení syntézního filtru. Přijaté parametry buzení se použijí k vygenerování buzení e(n), které je následně přivedeno přes tento syntézní filtr k rekonstrukci řečového průběhu. Stabilita syntézního filtru je zajištěna převodem LPCs na robustnější reprezentaci, jako jsou Line Spectral Pairs (LSPs) nebo Immittance Spectral Fairs (ISFs), pro kvantování a přenos. LP je výpočetně náročné, ale poskytuje extrémně vysokou účinnost komprese, což z něj činí základ všech moderních úzkopásmových a širokopásmových řečových kodeků standardizovaných 3GPP, jako jsou Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) kodeky.

## K čemu slouží

Lineární predikce existuje k řešení problému efektivní digitalizace a komprese řečových signálů pro přenos přes rádiové kanály s omezenou šířkou pásma. Jejím primárním účelem je využít silnou krátkodobou korelaci (redundanci) přítomnou v řečových signálech, kde je každý vzorek vysoce předvídatelný z předchozích vzorků díky fyzikálním vlastnostem lidského hlasového traktu. Modelováním této korelace umožňuje LP kodeku přenášet pouze parametry modelu (LPCs) a zjednodušenou reprezentaci buzení, čímž dosahuje vysokých kompresních poměrů (např. z 64 kbps [PCM](/mobilnisite/slovnik/pcm/) na 5,9 kbps [AMR](/mobilnisite/slovnik/amr/)) při zachování srozumitelné kvality řeči.

Historicky LP kódování nahradilo jednodušší vlnové kodeky (jako PCM a [ADPCM](/mobilnisite/slovnik/adpcm/)) pro mobilní hlas, protože nabízelo mnohem lepší kompresi, což bylo klíčové pro rané digitální buněčné systémy (2G GSM) s omezenou spektrální účinností. Zavedení řečového kodeku Full-Rate v GSM, založeného na Regular Pulse Excitation-Long Term Prediction ([RPE-LTP](/mobilnisite/slovnik/rpe-ltp/)), znamenalo přijetí principů LP. Následný vývoj prostřednictvím kodeku AMR v 3G UMTS a kodeku [EVS](/mobilnisite/slovnik/evs/) v 4G/5G průběžně zdokonaloval LP techniky, zvyšoval řád predikce, zlepšoval kvantování LPCs (pomocí LSPs) a vylepšoval modelování buzení (např. pomocí ACELP a TCX). Tento vývoj řešil omezení, jako je špatné zpracování hudby a robotické hlasové artefakty, a rozšířil využitelnost LP z úzkopásmové telefonie na vysoce kvalitní fullband audio a služby voice-over-LTE (VoLTE).

## Klíčové vlastnosti

- Modeluje řečový signál jako celopólový filtr buzený periodickým nebo šumově podobným zdrojem
- Extrahuje koeficienty lineární predikce (LPCs) reprezentující spektrální obálku (formanty) řeči
- Dosahuje vysoké komprese přenosem pouze LPCs a kompaktní reprezentace buzení
- Používá robustní parametrizace, jako jsou Line Spectral Pairs (LSPs), pro stabilní kvantování a přenos
- Tvoří základní analýzně-syntetickou strukturu kodeků jako AMR, AMR-WB a EVS
- Umožňuje víceúrovňový provoz změnou přidělení bitů pro kvantování LPC a buzení

## Definující specifikace

- **TS 26.090** (Rel-19) — AMR Speech Codec Detailed Mapping Specification
- **TS 26.092** (Rel-19) — AMR Comfort Noise for SCR Operation
- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.192** (Rel-19) — AMR-WB Comfort Noise Requirements
- **TS 26.226** (Rel-19) — Cellular Text Telephone Modem (CTM)
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.267** (Rel-19) — eCall In-band Modem Specification
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TS 46.060** (Rel-19) — GSM Enhanced Full Rate Speech Codec
- **TS 46.062** (Rel-19) — GSM EFR DTX Comfort Noise Specification

---

📖 **Anglický originál a plná specifikace:** [LP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lp/)
