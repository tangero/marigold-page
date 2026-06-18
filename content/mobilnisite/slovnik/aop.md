---
slug: "aop"
url: "/mobilnisite/slovnik/aop/"
type: "slovnik"
title: "AOP – Acoustic Overload Point"
date: 2025-01-01
abbr: "AOP"
fullName: "Acoustic Overload Point"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aop/"
summary: "AOP je klíčová metrika zvukového výkonu definovaná v 3GPP pro hlasové a zvukové služby. Určuje maximální hladinu akustického tlaku, kterou může mikrofon zařízení zpracovat, než dojde ke zkreslení, a z"
---

AOP je maximální hladina akustického tlaku, kterou může mikrofon zařízení zpracovat, než dojde ke zkreslení, jak je definováno 3GPP pro zajištění konzistentní kvality zvuku u hlasových služeb.

## Popis

Akustický bod přetížení (Acoustic Overload Point – AOP) je standardizovaný parametr zvukového výkonu definovaný ve specifikaci 3GPP TS 26.918, který charakterizuje maximální úroveň akustického vstupu, kterou může mikrofonní systém zařízení zpracovat, než dojde k významnému zkreslení. Technicky řečeno, AOP představuje hladinu akustického tlaku ([SPL](/mobilnisite/slovnik/spl/)), při které celkové harmonické zkreslení (THD) dosáhne stanoveného prahu, typicky 10 % nebo 3 %, v závislosti na použité metodice měření. Tento parametr je kritický, protože definuje horní limit dynamického rozsahu mikrofonu, za nímž se kvalita zvuku rychle zhoršuje v důsledku ořezání, saturace nebo nelineárního zkreslení ve zvukovém řetězci.

Z architektonického hlediska měření AOP zahrnuje celou zvukovou cestu záznamu včetně mikrofonního měniče, předzesilovače, analogově-digitálního převodníku ([ADC](/mobilnisite/slovnik/adc/)) a všech komponent digitálního zpracování signálu. Specifikace 3GPP definuje standardizované testovací postupy využívající kalibrovanou akustickou měřicí techniku v bezodrazových komorách nebo specializovaných akustických testovacích přípravcích. Během testu je aplikován čistý tón referenční frekvence (typicky 1 kHz) při rostoucích hladinách akustického tlaku, dokud není dosaženo stanoveného prahu zkreslení. Měření zohledňuje jak elektrické, tak akustické charakteristiky testovaného zařízení, což zajišťuje konzistentní výsledky napříč různými form-faktory a implementacemi mikrofonů.

V kontextu sítě jsou parametry AOP zohledňovány během certifikace zařízení a plánování sítě, aby byla zajištěna konzistentní uživatelská zkušenost. Operátoři využívají data AOP spolu s dalšími metrikami kvality zvuku, jako je Receive Loudness Rating ([RLR](/mobilnisite/slovnik/rlr/)) a Send Loudness Rating (SLR), k optimalizaci kvality hlasu ve svých sítích. Tento parametr je obzvláště důležitý pro služby Voice over LTE (VoLTE) a Voice over NR (VoNR), kde širokopásmové a super-širokopásmové kodeky jako [AMR-WB](/mobilnisite/slovnik/amr-wb/) a [EVS](/mobilnisite/slovnik/evs/) mohou poskytovat vynikající kvalitu zvuku, ale pouze pokud je mikrofonní systém schopen zachytit čistý zvuk v širokém dynamickém rozsahu.

Z implementační perspektivy AOP ovlivňuje více komponent ve zvukovém řetězci. Výrobci mikrofonů musí navrhovat měniče s dostatečnou rezervou (headroom), zatímco výrobci zařízení potřebují implementovat odpovídající nastavení zesílení a algoritmy pro prevenci ořezání. Digitální zpracování signálu ([DSP](/mobilnisite/slovnik/dsp/)) v moderních smartphonech často zahrnuje automatické řízení zesílení ([AGC](/mobilnisite/slovnik/agc/)) a omezovací obvody, které interagují s charakteristikami AOP. Porozumění AOP pomáhá inženýrům vyvážit citlivost (schopnost zachytit tiché zvuky) s ochranou proti přetížení (prevenci zkreslení od hlasitých zvuků), což je obzvlášť náročné u mobilních zařízení s malými rozměry a omezeným prostorem pro akustické komponenty.

Role AOP přesahuje rámec základních hlasových hovorů a zahrnuje všechny scénáře záznamu zvuku včetně nahrávání videa, hlasových asistentů a aplikací pro komunikaci v reálném čase. V sítích 5G, kde se objevují služby jako komunikace ve rozšířené realitě ([AR](/mobilnisite/slovnik/ar/)) a prostorový zvuk, se udržení vysoké kvality zvuku v různých akustických prostředích stává ještě kritičtějším. Standardizace AOP zajišťuje, že bez ohledu na výrobce zařízení nebo operátora sítě uživatelé zažívají konzistentní zvukový výkon, který splňuje minimální prahové hodnoty kvality definované 3GPP.

## K čemu slouží

Standardizace akustického bodu přetížení (AOP) byla zavedena, aby řešila významné rozdíly v kvalitě záznamu zvuku napříč různými mobilními zařízeními. Před formálním definováním AOP ve 3GPP Release 14 používali výrobci zařízení proprietární metody pro charakterizaci výkonu mikrofonů, což vedlo k nekonzistentní uživatelské zkušenosti. Některá zařízení by byla silně zkreslena v hlučném prostředí, jako jsou koncerty nebo rušné ulice, zatímco jiná mohla mít nedostatečnou citlivost pro tiché konverzace. Tato nekonzistence vytvářela výzvy pro operátory, kteří se snažili zajistit jednotnou kvalitu hlasových služeb napříč svou zákaznickou základnou.

Primární problém, který AOP řeší, je vytvoření společného rámce pro hodnocení a porovnávání výkonu mikrofonů v mobilních zařízeních. Definováním standardizovaných měřicích postupů a prahových hodnot výkonu umožnilo 3GPP objektivní srovnání schopností záznamu zvuku. To bylo obzvláště důležité, když se mobilní sítě vyvíjely z okruhově přepínaného hlasu na paketový Voice over LTE (VoLTE) a nakonec Voice over NR (VoNR). Tyto novější technologie slibovaly vyšší kvalitu zvuku prostřednictvím širokopásmových a super-širokopásmových kodeků, ale tento potenciál mohl být naplněn pouze tehdy, pokud mikrofonní hardware dokázal zachytit čistý zvuk v celém dynamickém rozsahu lidské řeči a okolních zvuků.

Historicky motivací pro standardizaci AOP byla rostoucí důležitost kvality zvuku jako konkurenčního diferenciátoru v mobilních službách. Jak se smartphony staly primárním komunikačním zařízením pro většinu uživatelů, očekávání ohledně kvality hovorů významně vzrostla. Operátoři investující do služeb HD Voice potřebovali jistotu, že zařízení v jejich sítích mohou poskytnout slibovaná zlepšení kvality. Parametr AOP spolu s dalšími metrikami zvukového výkonu standardizovanými v 3GPP poskytl technický základ pro certifikační programy zařízení a snahy o optimalizaci sítě zaměřené na poskytování konzistentně vysoké kvality hlasových služeb bez ohledu na model zařízení nebo prostředí použití.

## Klíčové vlastnosti

- Standardizované měření maximální úrovně akustického vstupu před zkreslením
- Definuje práh na základě metrik celkového harmonického zkreslení (THD)
- Aplikovatelné na všechny typy mikrofonů včetně MEMS a elektretových konstrukcí
- Integrováno s testováním celého zvukového řetězce včetně komponent DSP
- Podporuje metodologie bezodrazových komor i akustických testovacích přípravků
- Nezbytné pro certifikaci zařízení pro VoLTE a VoNR a zajištění kvality

## Definující specifikace

- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP

---

📖 **Anglický originál a plná specifikace:** [AOP na 3GPP Explorer](https://3gpp-explorer.com/glossary/aop/)
