---
slug: "bwm"
url: "/mobilnisite/slovnik/bwm/"
type: "slovnik"
title: "BWM – BandWidth Multiplier"
date: 2025-01-01
abbr: "BWM"
fullName: "BandWidth Multiplier"
category: "Physical Layer"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bwm/"
summary: "BWM je parametr ve specifikacích 3GPP, který definuje vztah mezi přenosovou šířkou pásma nosné a její kanálovou šířkou pásma. Je klíčový pro výpočet maximálního počtu bloků zdrojů a určení spektrální"
---

BWM je parametr 3GPP, který definuje vztah mezi přenosovou šířkou pásma nosné a její kanálovou šířkou pásma pro výpočet bloků zdrojů a spektrální účinnosti v LTE a NR.

## Popis

Multiplikátor šířky pásma (BWM) je základní parametr specifikovaný v 3GPP TS 26.103, který stanovuje matematický vztah mezi konfigurací přenosové šířky pásma nosné (N_RB) a její kanálovou šířkou pásma ([BW](/mobilnisite/slovnik/bw/)_Channel). Tento vztah je vyjádřen vzorcem N_RB = floor(BWM × BW_Channel / 0,18), kde N_RB představuje maximální počet bloků zdrojů, které lze přidělit v rámci dané kanálové šířky pásma. Hodnota BWM se liší v závislosti na konkrétním kmitočtovém pásmu a konfiguraci kanálové šířky pásma, přičemž typické hodnoty pro většinu nasazení LTE se pohybují od 0,8 do 0,9.

Z architektonického hlediska BWM funguje na rozhraní fyzické vrstvy mezi funkcemi správy rádiových zdrojů (RRM) a zpracováním fyzické vrstvy. Když operátor sítě nakonfiguruje nosnou s určitou kanálovou šířkou pásma, parametr BWM určuje, kolik bloků zdrojů lze v rámci tohoto přidělení šířky pásma prakticky využít. Tento výpočet zohledňuje ochranná pásma nezbytná pro zabránění interference se sousedními kanály a zajišťuje soulad s regulačními požadavky na spektrální masku. BWM efektivně představuje procento celkové kanálové šířky pásma, které lze použít pro skutečný přenos dat.

V praktické implementaci jsou hodnoty BWM standardizovány pro různé kombinace kmitočtových pásem a kanálových šířek pásma, aby byla zajištěna interoperabilita mezi síťovým zařízením od různých dodavatelů. Pro LTE jsou tyto hodnoty pečlivě vybírány tak, aby vyvážily spektrální účinnost vůči složitosti implementace a regulačním omezením. Parametr ovlivňuje klíčové metriky výkonu sítě včetně špičkových přenosových rychlostí, spektrální účinnosti a celkové kapacity systému. Nástroje pro plánování sítě používají výpočty BWM k určení optimálních konfigurací šířky pásma pro různé scénáře nasazení.

Koncept BWM přesahuje jednoduché výpočty šířky pásma a ovlivňuje protokoly vyšších vrstev a optimalizaci sítě. Protože počet dostupných bloků zdrojů přímo ovlivňuje algoritmy plánování, správu kvality služeb (QoS) a mechanismy koordinace interference, jsou přesné hodnoty BWM nezbytné pro správné dimenzování sítě. Ve scénářích agregace nosných se výpočty BWM stávají ještě kritičtějšími, protože určují kombinovanou dostupnost zdrojů napříč více komponentními nosnými. Parametr také hraje roli v optimalizaci energetické účinnosti sítě, protože pomáhá určit minimálně nutnou přenosovou šířku pásma pro daná zatížení provozem.

## K čemu slouží

Multiplikátor šířky pásma (BWM) byl zaveden ve verzi 3GPP Release 8, aby poskytl standardizovanou metodu pro výpočet použitelné přenosové šířky pásma v rámci přidělené kanálové šířky pásma. Před jeho standardizací používali různí dodavatelé zařízení proprietární výpočty pro určení přidělování bloků zdrojů, což vedlo k problémům s interoperabilitou a nekonzistentním predikcím výkonu sítě. Parametr BWM tento problém vyřešil stanovením jednotného matematického vztahu, který musí dodržovat všechny implementace LTE.

Tato standardizace byla obzvláště důležitá, protože LTE zavádělo flexibilní konfigurace šířky pásma v rozsahu od 1,4 MHz do 20 MHz. Bez konzistentní definice BWM by operátoři sítí čelili výzvám při přesném plánování kapacity sítě, predikci výkonu a zajišťování konzistentního uživatelského zážitku napříč nasazeními s více dodavateli. Parametr také řešil regulační požadavky tím, že zajistil, aby všechny implementace správně zohledňovaly nezbytná ochranná pásma a byly v souladu se spektrálními emisními maskami.

Dále BWM umožnil přesnější síťovou simulaci a modelování výkonu během procesu standardizace LTE. Tím, že poskytl jasný vztah mezi kanálovou šířkou pásma a dostupnými bloky zdrojů, umožnil konzistentní vyhodnocení různých konfigurací šířky pásma a jejich dopadu na kapacitu systému a spektrální účinnost. To bylo klíčové pro informovaná rozhodnutí o strategiích přidělování šířky pásma a pro vývoj efektivních algoritmů správy rádiových zdrojů, které se dokážou přizpůsobit různým scénářům šířky pásma.

## Klíčové vlastnosti

- Standardizovaný výpočet přenosové šířky pásma z kanálové šířky pásma
- Hodnoty parametrů závislé na kmitočtovém pásmu a šířce pásma
- Určuje maximální počet dostupných bloků zdrojů
- Zohledňuje nezbytná přidělení ochranných pásem
- Zajišťuje soulad s regulačními spektrálními maskami
- Umožňuje konzistentní interoperabilitu mezi více dodavateli

## Definující specifikace

- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO

---

📖 **Anglický originál a plná specifikace:** [BWM na 3GPP Explorer](https://3gpp-explorer.com/glossary/bwm/)
