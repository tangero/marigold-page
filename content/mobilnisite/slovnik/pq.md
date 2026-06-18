---
slug: "pq"
url: "/mobilnisite/slovnik/pq/"
type: "slovnik"
title: "PQ – Perceptual Quantization"
date: 2025-01-01
abbr: "PQ"
fullName: "Perceptual Quantization"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pq/"
summary: "PQ je přenosová funkce (EOTF), která převádí digitální video kódové hodnoty na světlo zobrazovače. Optimalizuje využití bitů na základě lidského vnímání, což umožňuje video s vysokým dynamickým rozsah"
---

PQ je přenosová funkce (transfer function), která převádí digitální video kódové hodnoty na světlo zobrazovače a optimalizuje využití bitů pro lidský zrak za účelem dosažení videa s vysokým dynamickým rozsahem (HDR).

## Popis

Perceptual Quantization (PQ), formálně standardizované jako SMPTE [ST](/mobilnisite/slovnik/st/) 2084 a přijaté konsorciem 3GPP pro doručování médií, je elektro-optická přenosová funkce ([EOTF](/mobilnisite/slovnik/eotf/)). EOTF definuje matematický vztah mezi digitálními kódovými hodnotami ve videosignálu a absolutními úrovněmi jasu (v nitech neboli kandelách na metr čtvereční) produkovanými zobrazovačem. Na rozdíl od tradičních gama křivek používaných pro standardní dynamický rozsah ([SDR](/mobilnisite/slovnik/sdr/)), které mají konstantní percepční odezvu, je PQ nelineární funkce pečlivě navržená tak, aby odpovídala kontrastní citlivosti lidského zrakového systému v extrémně širokém rozsahu jasu – od 0,0001 do 10 000 nitů.

Křivka PQ funguje tak, že přiděluje více digitálních kódových hodnot (bitů) úrovním jasu, kde lidské oko dokáže vnímat jemnější rozdíly v jasnosti, a méně bitů úrovním, kde jsou rozdíly méně patrné. To je založeno na Bartenově modelu zrakového vnímání, který zohledňuje faktory jako prostorová frekvence a okolní jas. Z technického hlediska je funkce definována tak, aby stejné kroky v kódové hodnotě odpovídaly stejným krokům ve vnímaném vizuálním kontrastu (právě postřehnutelným rozdílům neboli JND) v celém rozsahu jasu. Když video enkodér kvantuje lineární scénicky vztažená světelná data, použije inverzní PQ funkci (OETF) k vytvoření digitálního signálu. Zobrazovač pak na tento signál aplikuje PQ EOTF, aby rekonstruoval světlo, které je pro diváka vnímání jednotné.

V architektuře 3GPP pro mediální služby (např. Multimedia Broadcast Multicast Service - [MBMS](/mobilnisite/slovnik/mbms/) nebo Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) - [DASH](/mobilnisite/slovnik/dash/)) je PQ klíčovou součástí celého video řetězce. Je specifikována v rámci profilů a úrovní kodeků (např. pro [HEVC](/mobilnisite/slovnik/hevc/) a později [VVC](/mobilnisite/slovnik/vvc/)) a v popisech mediální prezentace. Mezi klíčové komponenty patří metadata popisující referenční zobrazovací zařízení (MaxCLL, MaxFALL), která definují možnosti původního HDR monitoru, a signalizace samotné přenosové funkce (např. 'pq' v Colour Description Box souborů ISOBMFF). Jejím úkolem je umožnit efektivní a kvalitní doručování HDR video obsahu přes mobilní sítě a zajistit, aby ohromující kontrast a barevný objem zamýšlený tvůrci obsahu byly zachovány od produkce přes přenos až po zobrazení na kompatibilních HDR displejích, jako jsou ty podporující HDR10.

## K čemu slouží

PQ bylo vytvořeno, aby překonalo vážná omezení gama křivky (BT.1886) používané pro SDR televizi a raná digitální videa. Gama křivka byla navržena pro fosfor CRT a omezený rozsah jasu (kolem 100 nitů). Pro HDR je nevhodná, protože plýtvá bity ve světlech a stínech, kde je percepční citlivost nízká, a neposkytuje dostatečné gradace ve středních tónech, kde je při sledování jasného obsahu oko nejcitlivější. Jak technologie zobrazování pokročila k podpoře tisíců nitů, byla potřebná nová přenosová funkce pro efektivní kódování tohoto rozšířeného rozsahu jasu v rámci omezení bitové hloubky video kodeků (typicky 10 nebo 12 bitů).

Problém, který PQ řeší, je bitově efektivní percepční kódování pro HDR. Bez PQ by reprezentace rozsahu 0–10 000 nitů lineárně vyžadovala neprakticky vysokou bitovou hloubku. PQ umožňuje mapovat tento široký rozsah do 10 nebo 12bitového signálu bez viditelného páskování nebo ztráty detailů v percepčně kritických oblastech. Motivací byl přesun průmyslu k HDR videu pro prémiový obsah (filmy, streamování) za účelem poskytnutí poutavějšího a realističtějšího zážitku se spekulárními odlesky, hlubokými černými a živými barvami. 3GPP přijalo PQ (a později Hybrid Log-Gamma - HLG) ke standardizaci doručování HDR videa přes mobilní sítě, což umožňuje služby jako 4K/HDR streamování a vysílání, které jsou klíčovými diferenciátory pro multimediální služby 5G.

## Klíčové vlastnosti

- Nelineární EOTF založená na kontrastní citlivosti lidského zraku (Bartenův model)
- Podporuje rozsah jasu od 0,0001 do 10 000 nitů
- Umožňuje efektivní 10bitové nebo 12bitové kódování HDR videa
- Standardizováno jako SMPTE ST 2084 a přijato v 3GPP TS 26.116
- Používáno v mediálních formátech HDR10 a Dolby Vision profil 5
- Vyžaduje přidružená statická metadata (Mastering Display Colour Volume)

## Související pojmy

- [EOTF – Electro-Optical Transfer Function](/mobilnisite/slovnik/eotf/)
- [HDR – High Dynamic Range](/mobilnisite/slovnik/hdr/)
- [HLG – Hybrid Log Gamma](/mobilnisite/slovnik/hlg/)

## Definující specifikace

- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services

---

📖 **Anglický originál a plná specifikace:** [PQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/pq/)
