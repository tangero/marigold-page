---
slug: "vop"
url: "/mobilnisite/slovnik/vop/"
type: "slovnik"
title: "VOP – Video Object Plane"
date: 2025-01-01
abbr: "VOP"
fullName: "Video Object Plane"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vop/"
summary: "Video Object Plane (VOP) je základní typ snímku ve vizuálním kódování MPEG-4, který představuje snímek videoobjektu v daném čase. Je to základní jednotka pro kódování, dekódování a manipulaci jednotli"
---

VOP je základní typ snímku ve vizuálním kódování MPEG-4, který představuje snímek videoobjektu v daném čase pro účely kódování, dekódování a manipulace.

## Popis

V kontextu specifikací 3GPP (především TS 26.114 pro zpracování médií v IMS) je Video Object Plane (VOP) klíčový koncept převzatý z vizuálního standardu MPEG-4 Part 2. Představuje základní kódovací strukturu. Na rozdíl od tradičního videozáznamu založeného na snímcích (např. I/P/B snímky v [MPEG-2](/mobilnisite/slovnik/mpeg-2/), H.264/[AVC](/mobilnisite/slovnik/avc/)) zavedlo vizuální kódování MPEG-4 kódování založené na objektech, kde se scéna skládá z oddělených Video Objects (VO). VOP je časová instance – „snímek“ – jednoho takového videoobjektu. Obsahuje informace o tvaru, pohybu a textuře tohoto objektu v konkrétním časovém okamžiku.

Existuje několik typů VOP, analogických typům snímků v jiných kodecích. Intra-VOP (I-VOP) je kódován nezávisle pouze pomocí své vlastní prostorové informace a slouží jako vstupní bod. Predictive-VOP (P-VOP) je kódován pomocí pohybové kompenzace z předchozího I-VOP nebo P-VOP. Bidirectionally predictive-VOP (B-VOP) využívá predikci z minulých i budoucích referenčních VOP pro vyšší kompresi. Sprite-VOP je speciální typ používaný pro statické objekty pozadí. Posloupnost VOP pro jeden videoobjekt tvoří Video Object Layer (VOL).

Proces kódování VOP zahrnuje několik kroků. Nejprve kódování tvaru definuje hranici objektu libovolného tvaru (pomocí binární alfa roviny nebo stupňů šedi pro průhlednost). U pravoúhlých VOP se tento krok vynechává. Následuje odhad pohybu a pohybová kompenzace na bázi makrobloků uvnitř tvaru objektu, aby se využila časová redundance. Nakonec je na pohybově kompenzovaný reziduální rozdíl aplikováno kódování textury (založené na [DCT](/mobilnisite/slovnik/dct/), podobně jako u jiných kodeků). Syntaxe datového toku organizuje data VOP pomocí hlaviček udávajících jeho typ, časové razítko a kódovací parametry. Dekódování rekonstruuje VOP interpretací této syntaxe, provedením pohybové kompenzace a přidáním dekódovaného rezidua textury.

V rámci 3GPP jsou VOP relevantní, protože vizuální kodek MPEG-4 byl povinným videokodekem pro rané paketové streamování ([PSS](/mobilnisite/slovnik/pss/)) a služby zasílání zpráv ([MMS](/mobilnisite/slovnik/mms/)) v 3GPP. TS 26.114 specifikuje požadavky na mediální kodeky pro službu IMS Multimedia Telephony, a přestože pozdější vydání kladou důraz na H.264/AVC a [HEVC](/mobilnisite/slovnik/hevc/), pochopení VOP je součástí historických požadavků na interoperabilitu kodeků. Povaha VOP založená na objektech byla klíčovým diferenciátorem, který teoreticky umožňoval pokročilé funkce, jako je manipulace založená na obsahu, oddělené kódování popředí a pozadí a interaktivní kompozice scény, ačkoli tyto funkce zaznamenaly v mobilních sítích ve srovnání s jednoduššími kodeky založenými na snímcích omezené komerční nasazení.

## K čemu slouží

Koncept Video Object Plane byl vytvořen jako součást revolučního přístupu standardu MPEG-4 k multimediálnímu kódování. Předchozí standardy jako MPEG-1 a [MPEG-2](/mobilnisite/slovnik/mpeg-2/) byly založeny na snímcích a jako jednotku komprese používaly celý pravoúhlý videosnímek. To bylo efektivní pro ukládání a vysílání, ale nabízelo omezenou flexibilitu pro interakci a manipulaci s obsahem. Primárním účelem kódování založeného na objektech s VOP bylo posunout se k multimédiím zaměřeným na obsah, kde by jednotlivé audiovizuální objekty (jako osoba, auto, logo) mohly být kódovány, přenášeny a manipulovány nezávisle.

Tím se řešilo několik omezení. Umožnilo vysoce efektivní kódování pro specifické aplikace: například statické pozadí mohlo být odesláno jednou jako Sprite VOP, čímž se šetřila šířka pásma. Umožnilo škálovatelnost a opakované použití – objekty mohly být uloženy v knihovnách a skládány do různých scén. Nejvýznamnější bylo, že to otevřelo cestu interaktivním aplikacím, kde uživatelé mohli vybírat, přesouvat nebo jinak interagovat s jednotlivými objekty ve videoscéně, což je funkce relevantní pro rozšířenou realitu, interaktivní televizi a pokročilé hry.

V kontextu 3GPP byl MPEG-4 Visual (a tedy i VOP) standardizován, aby poskytoval bohatý a flexibilní videokodek pro rané multimediální služby přes sítě 2,5G a 3G ([GPRS](/mobilnisite/slovnik/gprs/), UMTS). Byl součástí souboru nástrojů pro umožnění atraktivních videoaplikací, jako je streamování, videotelefonie a multimediální zasílání zpráv. Výpočetní složitost DCT přizpůsobené tvaru a proces segmentace objektů spolu s rychlým vzestupem efektivnějších a jednodušších kodeků založených na snímcích, jako je H.264/AVC, však vedly k tomu, že pokročilé funkce VOP založené na objektech byly v praxi zřídka využívány. 3GPP nakonec přesunulo své hlavní povinné videokodeky na H.264 a později HEVC, ale podpora MPEG-4 Simple Profile (který používá pravoúhlé VOP) zůstala zachována kvůli zpětné kompatibilitě.

## Klíčové vlastnosti

- Základní kódovací jednotka pro Video Object ve vizuálním kódování MPEG-4
- Typy zahrnují I-VOP (intra), P-VOP (prediktivní), B-VOP (obousměrně prediktivní)
- Podporuje kódování libovolného tvaru pomocí alfa rovin, což umožňuje nepravoúhlé objekty
- Umožňuje časovou predikci založenou na objektech (pohybová kompenzace) a kódování textury
- Tvoří základ pro pokročilé funkce, jako je kódování sprite pro statická pozadí
- Definovaná syntaxe datového toku pro flexibilní kompozici a interakci videoobjektů

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling

---

📖 **Anglický originál a plná specifikace:** [VOP na 3GPP Explorer](https://3gpp-explorer.com/glossary/vop/)
