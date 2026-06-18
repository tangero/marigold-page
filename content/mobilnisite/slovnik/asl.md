---
slug: "asl"
url: "/mobilnisite/slovnik/asl/"
type: "slovnik"
title: "ASL – Active Speech Level"
date: 2025-01-01
abbr: "ASL"
fullName: "Active Speech Level"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/asl/"
summary: "ASL je standardizovaná metrika pro měření průměrné úrovně výkonu aktivních řečových segmentů v audio signálech. Je klíčová pro zajištění konzistentní kvality řeči a hlasitosti v telekomunikacích, zejm"
---

ASL je standardizovaná metrika pro měření průměrné úrovně výkonu aktivních řečových segmentů v audio signálech za účelem zajištění konzistentní kvality řeči a hlasitosti v telekomunikacích, jako jsou VoNR a VoLTE.

## Popis

Úroveň aktivní řeči (Active Speech Level – ASL) je technický parametr definovaný 3GPP pro kvantifikaci průměrné úrovně výkonu řeči během aktivních mluvních úseků, s vyloučením období ticha a šumu na pozadí. Měří se v decibelech vzhledem k plnému rozsahu digitálního signálu (dBov) nebo vzhledem ke stanovenému referenčnímu bodu (dBm0). Výpočet zahrnuje segmentaci audio signálu, identifikaci intervalů aktivní řeči pomocí algoritmů detekce hlasové aktivity (Voice Activity Detection – [VAD](/mobilnisite/slovnik/vad/)) a výpočet střední kvadratické ([RMS](/mobilnisite/slovnik/rms/)) hodnoty výkonu v těchto intervalech. Tento proces zajišťuje, že k měření úrovně přispívají pouze složky řeči, čímž poskytuje spolehlivou metriku hlasitosti řeči nezávislou na tichu nebo šumu.

V architektuře 3GPP je ASL integrována do mediálních zpracovatelských funkcí IP Multimedia Subsystem (IMS) a jádra 5G sítě (5GC). Pro hlasové služby jako VoNR a VoLTE využívají měření ASL funkce Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) a Application Function ([AF](/mobilnisite/slovnik/af/)) ke sledování a řízení úrovní řeči. Metrika se uplatňuje v různých bodech přenosové cesty, včetně uživatelského zařízení (UE), rádiové přístupové sítě (RAN) a uzlů jádra sítě zapojených do zpracování médií. Toto end-to-end použití zajišťuje, že úrovně řeči zůstávají konzistentní napříč různými segmenty sítě a zařízeními.

Klíčové komponenty zapojené do implementace ASL zahrnují jednotky zpracování kodeků, které kódují a dekódují řečové signály, a moduly VAD, které rozlišují mezi řečovými a ner řečovými segmenty. Hodnota ASL se často používá ve spojení s dalšími parametry, jako je úroveň šumu (Noise Level – [NL](/mobilnisite/slovnik/nl/)) a variace úrovně řeči (Speech Level Variation – SLV), pro komplexní hodnocení kvality řeči. Ve specifikacích 3GPP, jako jsou TS 26.801 a TS 26.921, je ASL definována jako součást požadavků na výkonnost řečových kodeků a metrik kvality hlasových služeb. Hraje klíčovou roli při udržování interoperability mezi zařízeními různých výrobců a zajištění jednotného uživatelského zážitku.

Role ASL v síti sahá až k řízení kvality služeb (QoS) a optimalizaci sítě. Sledováním hodnot ASL mohou operátoři sítí detekovat problémy, jako je nadměrný útlum nebo zesílení v řečové cestě, které by mohly degradovat kvalitu hovoru. Data ASL mohou spouštět adaptivní mechanismy řízení úrovně, jako je automatické řízení zesílení (Automatic Gain Control – [AGC](/mobilnisite/slovnik/agc/)), pro dynamické úpravy úrovní řeči. To je obzvláště důležité v sítích 5G, kde musí hlasové služby splňovat přísné standardy kvality, aby konkurovaly aplikacím typu over-the-top ([OTT](/mobilnisite/slovnik/ott/)). ASL se dále používá v testovacích a certifikačních procesech k ověření, že zařízení a síťové prvky splňují specifikace 3GPP.

Celkově je ASL základní metrikou pro zpracování řeči v moderní telekomunikaci. Její standardizovaná definice umožňuje konzistentní měření a řízení hlasitosti řeči, což je nezbytné pro poskytování kvalitních hlasových služeb. Tím, že poskytuje jasný referenční bod pro výkon aktivní řeči, pomáhá ASL zmírňovat problémy spojené s nevyvážeností úrovní a zajišťuje, aby uživatelé zažívali jasnou a komfortní hlasovou komunikaci za různých síťových podmínek a na různých typech zařízení.

## K čemu slouží

Vytvoření metriky Úroveň aktivní řeči (ASL) bylo motivováno potřebou standardizované metody pro měření hlasitosti řeči v digitální hlasové komunikaci. Před její definicí vedly různé implementace měření úrovně řeči k nekonzistentnosti kvality hlasu napříč sítěmi a zařízeními. To mělo za následek uživatelský diskomfort, například příliš hlasité nebo tiché hovory, a komplikovalo interoperabilitu mezi zařízeními různých výrobců. ASL tyto problémy řeší tím, že poskytuje jednotnou metriku zaměřenou výhradně na aktivní řečové segmenty s vyloučením ticha a šumu, což umožňuje přesné a srovnatelné hodnocení úrovní řeči.

Historicky se analogové telefonní systémy spoléhaly na jednoduchá měření výkonu zahrnující všechny audio komponenty, která mohla být zavádějící kvůli šumu na pozadí. S přechodem na digitální a paketové sítě, jako jsou LTE a 5G, se přesná kontrola řečových parametrů stala klíčovou pro udržení kvality služeb voice over IP (VoIP). 3GPP zavedlo ASL ve verzi 16 jako součást vylepšených požadavků na hlasové služby pro 5G New Radio (NR), konkrétně pro VoNR. Tato standardizace zajišťuje, že úrovně řeči jsou konzistentně řízeny end-to-end, což podporuje plynulé předávání mezi různými rádiovými přístupovými technologiemi a jádry sítí.

ASL řeší omezení předchozích přístupů, kterým chybělo jasné rozlišení mezi řečovými a ner řečovými prvky, což mohlo zkreslovat měření úrovní a vést k nevhodným úpravám zesílení. Definováním ASL umožňuje 3GPP síťovým operátorům a výrobcům zařízení implementovat spolehlivé mechanismy řízení úrovně, jako je automatické řízení zesílení ([AGC](/mobilnisite/slovnik/agc/)) a normalizace hlasitosti. To je nezbytné pro splnění uživatelských očekávání v době, kdy se hlasové služby musí vyrovnávat s kvalitními aplikacemi typu OTT. ASL dále usnadňuje splnění regulatorních požadavků na standardy hlasitosti v telekomunikacích, což zajišťuje, že služby dodržují bezpečnostní a komfortní směrnice.

## Klíčové vlastnosti

- Standardizované měření výkonu aktivní řeči v dBov nebo dBm0
- Vyloučení období ticha a šumu na pozadí pomocí algoritmů VAD
- Integrace s IMS a 5GC pro end-to-end správu hlasových služeb
- Podpora sledování QoS a adaptivního řízení úrovní v sítích
- Využití při testování a certifikaci zařízení vyhovujících 3GPP
- Aplikace ve službách VoNR a VoLTE pro zajištění konzistentní hlasitosti řeči

## Definující specifikace

- **TS 26.801** (Rel-19) — Testing UEs with Non-Traditional Earpieces
- **TR 26.921** (Rel-19) — UE Performance in Ambient Noise

---

📖 **Anglický originál a plná specifikace:** [ASL na 3GPP Explorer](https://3gpp-explorer.com/glossary/asl/)
