---
slug: "ecu"
url: "/mobilnisite/slovnik/ecu/"
type: "slovnik"
title: "ECU – Error Concealment Unit"
date: 2025-01-01
abbr: "ECU"
fullName: "Error Concealment Unit"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ecu/"
summary: "Error Concealment Unit (ECU) je funkční komponenta v sítích 3GPP, která se zabývá zmírňováním chyb v přenášených médiích, jako je hlas nebo video. Je klíčová pro zachování vnímané kvality služby (QoS)"
---

ECU je funkční komponenta v sítích 3GPP, která zmírňuje přenosové chyby v médiích, jako je hlas nebo video, jejich maskováním nebo opravou za účelem zachování vnímané kvality služby.

## Popis

Error Concealment Unit (ECU) je sofistikovaná jednotka pro zpracování signálu definovaná v rámci servisního rámce 3GPP, konkrétně pro multimediální telefonii a streamovací služby. Jejím primárním úkolem je detekovat a maskovat chyby, které se vyskytují v kódovaných mediálních tocích v důsledku ztráty, poškození paketů nebo zpoždění (jitteru) během přenosu přes paketové sítě, jako jsou LTE a 5G. ECU funguje tak, že analyzuje přijaté mediální rámce, identifikuje chybějící nebo poškozené datové segmenty a aplikuje algoritmy pro jejich rekonstrukci nebo nahrazení způsobem, který minimalizuje slyšitelné nebo viditelné artefakty pro koncového uživatele.

Z architektonického hlediska může být ECU implementována v různých síťových uzlech, včetně uživatelského zařízení (UE), mediálních bran nebo vyhrazených serverů pro zpracování médií. Funguje ve spolupráci s kodeky (např. [AMR](/mobilnisite/slovnik/amr/), [EVS](/mobilnisite/slovnik/evs/) pro hlas; H.264, H.265 pro video) a dalšími mechanismy QoS, jako jsou vyrovnávací paměti pro zpoždění (jitter buffery) a techniky maskování ztráty paketů ([PLC](/mobilnisite/slovnik/plc/)). Při detekci chyby může ECU použít metody jako je substituce tvaru vlny, při které se opakuje nebo modifikuje předchozí správný rámec, nebo predikci na základě modelu, kde statistické modely mediálního signálu generují věrohodné náhrady. Ve složitějších scénářích může využívat informace napříč vrstvami od rádiové přístupové sítě (RAN) o stavu kanálu, aby dynamicky přizpůsobila svou strategii maskování.

Klíčovými součástmi funkčnosti ECU jsou moduly pro detekci chyb, knihovny algoritmů pro maskování a systémy vyrovnávací paměti. Její provoz je úzce integrován s protokolem Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) a protokolem RTP Control Protocol ([RTCP](/mobilnisite/slovnik/rtcp/)) pro přenos médií a zpětnou vazbu. Účinnost ECU se měří percepčními metrikami kvality, jako je Mean Opinion Score ([MOS](/mobilnisite/slovnik/mos/)), a její parametry jsou často konfigurovatelné na základě síťových politik a smluv o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)). V širším síťovém ekosystému hraje ECU zásadní roli při zajišťování konzistentní kvality médií, zejména v mobilních scénářích, kde se rádiové podmínky mění, čímž podporuje spolehlivé služby, jako je hlas přes LTE (VoLTE), videohovory a další služby komunikace v reálném čase.

## K čemu slouží

Error Concealment Unit byla zavedena, aby řešila inherentní výzvy spojené s poskytováním kvalitních služeb přenosu médií v reálném čase přes mobilní sítě založené na IP, které jsou náchylné ke ztrátě paketů a proměnlivé latenci. Před standardizací těchto mechanismů 3GPP bylo zpracování chyb v okruhově přepínaném hlasu jednodušší, ale méně efektivní, a rané implementace paketového přepínání často vedly k znatelnému zhoršení kvality při poruchách sítě. ECU poskytuje standardizovanou, robustní metodu pro maskování chyb, která zajišťuje, že dočasné síťové problémy neovlivní výrazně vnímání kvality hovoru nebo videa uživatelem.

Její vytvoření bylo motivováno přechodem na plně IP sítě ve 3GPP Release 8 a novějších, kde služby jako VoLTE vyžadovaly kvalitu hlasu na úrovni operátorů srovnatelnou s tradičními okruhově přepínanými sítěmi. Definováním schopností ECU ve specifikacích umožnila 3GPP interoperabilitu a konzistentní správu kvality napříč zařízeními různých dodavatelů a sítěmi operátorů. Řeší problém udržení přijatelnosti služeb v méně než ideálních rádiových podmínkách, což je klíčové pro udržení uživatelů a konkurenceschopnou nabídku služeb na telekomunikačním trhu.

## Klíčové vlastnosti

- Detekce ztráty paketů a bitových chyb v mediálních tocích
- Aplikace technik substituce tvaru vlny pro maskování chyb v audiu
- Využití prostorové a časové predikce pro maskování chyb ve videu
- Integrace s kodek-specifickými postprocesními algoritmy
- Adaptivní provoz na základě síťové zpětné vazby a podmínek kanálu
- Podpora konfigurovatelných politik maskování pro dosažení cílů QoS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TS 26.091** (Rel-19) — AMR Error Concealment Procedure
- **TS 26.191** (Rel-19) — AMR-WB Error Concealment Procedure
- **TS 26.255** (Rel-19) — IVAS Frame Loss Concealment Procedure

---

📖 **Anglický originál a plná specifikace:** [ECU na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecu/)
