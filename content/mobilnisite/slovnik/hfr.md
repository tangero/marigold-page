---
slug: "hfr"
url: "/mobilnisite/slovnik/hfr/"
type: "slovnik"
title: "HFR – Higher Frame Rates"
date: 2025-01-01
abbr: "HFR"
fullName: "Higher Frame Rates"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hfr/"
summary: "Vyšší snímkové frekvence (HFR) označují videoobsah s frekvencemi výrazně převyšujícími konvenčních 24-30 fps, například 60, 100 nebo 120 snímků za sekundu, standardizované organizací 3GPP pro vylepšen"
---

HFR je použití vyšších snímkových frekvencí videa, jako je 60 nebo 120 fps, standardizované organizací 3GPP, které umožňuje plynulejší pohyb a lepší vizuální kvalitu pro služby jako sportovní přenosy a hraní her přes mobilní sítě.

## Popis

Vyšší snímkové frekvence (HFR) ve standardech 3GPP definují schopnost kódovat, přenášet a zobrazovat videoobsah na zvýšených snímkových frekvencích, typicky 60 snímků za sekundu (fps) a více, ve srovnání s tradičními frekvencemi 24-30 fps. Technicky HFR zahrnuje úpravy napříč řetězcem doručování médií: vytváření obsahu vysokorychlostními kamerami, efektivní videokódování, robustní síťový přenos a schopné zobrazovací zařízení. Specifikace 3GPP, zejména v kontextu vylepšeného mobilního širokopásmového přístupu (eMBB) a streamování médií, řeší podporu kodeků (např. v [HEVC](/mobilnisite/slovnik/hevc/)/H.265 a později [VVC](/mobilnisite/slovnik/vvc/)/H.266), kontejnerové formáty a streamovací protokoly pro akomodaci HFR. Zvýšená snímková frekvence snižuje rozmazání pohybu a trhání obrazu, což vede k realističtějšímu a působivějšímu zážitku ze sledování, zejména u obsahu s rychlým pohybem.

Z architektonického pohledu HFR ovlivňuje několik síťových a zařízeníových komponent. Na straně kódování musí kodeky efektivně komprimovat dodatečné časové informace bez nadměrného zvýšení datového toku, často s využitím pokročilých nástrojů pro predikci pohybu a kompresi. 3GPP definuje profily a úrovně v rámci specifikací kodeků, které podporují HFR. Pro přenos jsou streamovací protokoly jako Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)) nebo HTTP Live Streaming ([HLS](/mobilnisite/slovnik/hls/)) rozšířeny o signalizaci možností HFR a umožňují adaptivní přepínání mezi reprezentacemi s různými snímkovými frekvencemi na základě síťových podmínek a možností zařízení. Mediální engine uživatelského zařízení (UE) musí dekódovat a vykreslovat video s vysokou snímkovou frekvencí, což vyžaduje dostatečný výpočetní výkon a kompatibilitu s obnovovací frekvencí displeje.

Úloha HFR v mobilních sítích spočívá v umožnění prémiových mediálních služeb, které využívají vysokou šířku pásma a nízkou latenci sítí 4G LTE a 5G NR. Je klíčovým prvkem pro aplikace jako živé vysílání sportovních událostí v ultra vysokém rozlišení, cloudové hraní her a rozšířená/virtuální realita, kde je plynulý pohyb klíčový pro realističnost a uživatelský komfort. Práce 3GPP zajišťuje interoperabilitu mezi poskytovateli obsahu, síťovými operátory a výrobci zařízení, což usnadňuje široké přijetí. Specifikace také zvažují kompromisy, jako jsou zvýšené nároky HFR na datový tok, a poskytují mechanismy pro efektivní doručování, včetně adaptace kvality a síťově citlivého streamování.

## K čemu slouží

Vyšší snímkové frekvence byly standardizovány, aby vyhověly rostoucí poptávce spotřebitelů po vyšší kvalitě videa a působivějších mediálních zážitcích na mobilních zařízeních. Tradiční snímkové frekvence, ačkoli dostačující pro mnoho typů obsahu, vykazují při rychlých scénách znatelné rozmazání pohybu a trhání, což zhoršuje zážitek ze sledování sportu, akčních filmů a interaktivních aplikací. HFR tyto nedostatky řeší zachycením a zobrazením většího počtu snímků za sekundu, což vede k plynulejšímu pohybu a vyšší časové rozlišovací schopnosti.

Tlak na HFR v rámci 3GPP byl hnán vývojem zobrazovacích technologií (např. 120Hz displeje chytrých telefonů) a rostoucími možnostmi mobilních sítí, zejména s vylepšeným mobilním širokopásmovým přístupem 5G. Před standardizací bránily konzistentnímu doručování napříč různými sítěmi a zařízeními proprietární řešení a fragmentace. Zapojení 3GPP, počínaje vydáním 14, poskytlo jednotný rámec pro HFR v ekosystémech mobilního streamování, což zajišťuje, že obsah s vysokou snímkovou frekvencí může být efektivně zakódován, dynamicky přizpůsoben a spolehlivě doručován za různých síťových podmínek. Tím se řeší problém doručování kinematografické plynulosti pohybu na přenosná zařízení, což otevírá nové zdroje příjmů pro operátory a poskytovatele obsahu prostřednictvím prémiových úrovní služeb.

## Klíčové vlastnosti

- Podpora snímkových frekvencí videa 60 fps, 100 fps, 120 fps a vyšších
- Integrace s pokročilými videokodeky jako HEVC a VVC pro efektivní kompresi
- Signalizace v adaptivních streamovacích protokolech (např. DASH, HLS) pro reprezentace HFR
- Vylepšené zobrazení pohybu se sníženým rozmazáním a trháním pro obsah s rychlou akcí
- Kompatibilita s displeji s vysokou obnovovací frekvencí na mobilních zařízeních
- Síťově citlivá adaptace pro vyvážení datového toku, latence a kvality u HFR streamů

## Definující specifikace

- **TR 22.826** (Rel-17) — Study on 5G for Critical Medical Applications
- **TR 26.805** (Rel-17) — Study on Media Production over 5G NPN Systems
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [HFR na 3GPP Explorer](https://3gpp-explorer.com/glossary/hfr/)
