---
slug: "bht"
url: "/mobilnisite/slovnik/bht/"
type: "slovnik"
title: "BHT – Busy Hour Traffic"
date: 2025-01-01
abbr: "BHT"
fullName: "Busy Hour Traffic"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bht/"
summary: "Busy Hour Traffic (BHT) je klíčový ukazatel výkonu (KPI) používaný v plánování a dimenzování sítě. Představuje maximální objem provozu přenesený síťovým prvkem nebo systémem během nejvytíženější 60min"
---

BHT je maximální objem provozu přenesený síťovým prvkem během nejvytíženější 60minutové periody typického dne, používaný jako klíčový ukazatel výkonu pro plánování a dimenzování sítě.

## Popis

Busy Hour Traffic (BHT) je základní metrika provozního inženýrství definovaná ve specifikacích 3GPP, konkrétně v TS 45.926, pro systémy GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Kvantifikuje špičkové zatížení, které síť zažívá, měřené v erlangech nebo jiných provozních jednotkách (jako je objem dat pro paketově přepínaný provoz), během souvislé jednohodinové periody. Toto měření není založeno na jedné anomální špičce, ale typicky je odvozeno ze statistické analýzy provozních dat za dny nebo týdny, aby byla identifikována konzistentně nejvytíženější hodina reprezentující typický vzorec špičkového využití sítě. BHT je klíčový pro převod využití účastníky a poptávky po službách na konkrétní technické požadavky na síťový hardware, software a přenosové zdroje.

Proces stanovení BHT zahrnuje kontinuální monitorování a sběr dat ze síťových prvků, jako jsou Base Station Controllers ([BSC](/mobilnisite/slovnik/bsc/)), Mobile Switching Centers ([MSC](/mobilnisite/slovnik/msc/)) a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Nodes ([SGSN](/mobilnisite/slovnik/sgsn/)). Systémy měření provozu agregují pokusy o spojení, časy úspěšného držení hovoru, paketová datová sezení a související objemy dat. Na tato historická data jsou pak aplikovány statistické metody pro vyhlazení odlehlých hodnot a identifikaci hodiny s nejvyšším konzistentním provozním zatížením. Pro přepojované hlasové služby okruhově je BHT vyjádřen v erlangech (kde 1 erlang představuje okruh obsazený po dobu jedné hodiny). Pro paketově přepínaná data může být vyjádřen v gigabytech za hodinu nebo podobných jednotkách objemu dat.

Z architektonického hlediska BHT ovlivňuje návrh a poskytování kapacity prakticky všech síťových domén. V Radio Access Network (RAN) BHT určuje požadovaný počet provozních kanálů ([TCH](/mobilnisite/slovnik/tch/)) v buňce, což ovlivňuje hardwarovou konfiguraci základnové stanice. V jádře sítě určuje potřebnou kapacitu přepínacích matic v MSC, kapacitu portů na Media Gateways ([MGW](/mobilnisite/slovnik/mgw/)) a výpočetní výkon řídicích uzlů. Přenosové síťové spoje musí být také dimenzovány na přenos špičkového zatížení BHT. Díky návrhu sítí tak, aby zvládly BHT s přijatelnou třídou služby (GoS) nebo kvalitou služby (QoS), operátoři zajišťují, že během špičkového využití jsou přetížení a blokování hovorů minimalizovány, což přímo ovlivňuje spokojenost zákazníků a spolehlivost sítě.

Jeho role přesahuje rámec počátečního nasazení a zasahuje do průběžného řízení a optimalizace sítě. Porovnání předpověděného BHT se skutečně naměřeným BHT umožňuje operátorům ověřit provozní modely a spustit projekty rozšíření kapacity ještě před vznikem přetížení. Je to primární vstup pro plánování rozšíření sítě, strategie migrace technologií (např. z 2G na 4G/5G) a ekonomické modelování. Analýza BHT navíc může odhalit vzorce využití spojené s konkrétními událostmi, lokalitami nebo službami, což umožňuje cílenou optimalizaci sítě a marketingové kampaně. V moderních sítích, ačkoliv koncept zůstává, může být měření segmentováno podle síťového řezu, typu služby nebo geografické oblasti, aby umožnilo podrobnější správu kapacity.

## K čemu slouží

Účelem definování a standardizace Busy Hour Traffic (BHT) v rámci 3GPP je poskytnout konzistentní, objektivní základ pro plánování kapacity sítě, dimenzování a srovnávání výkonnosti. Před standardizovanými metrikami, jako je BHT, bylo plánování sítě často založeno na nekonzistentních měřeních nebo pravidlech odhadu, což vedlo buď k nadměrnému poskytování kapacity (plýtvání kapitálovými výdaji), nebo k nedostatečnému poskytování (způsobující špatnou kvalitu služeb a ztrátu výnosů). BHT řeší základní problém sladění konečných síťových zdrojů s vysoce proměnlivou poptávkou uživatelů tím, že identifikuje předvídatelné špičkové zatížení, pro které musí být síť navržena.

Historicky, jak se telefonní sítě rozšiřovaly, potřebovali inženýři spolehlivý způsob dimenzování ústředen a spojovacích linek. Koncept 'vytížené hodiny' vzešel z teorie provozu (Erlangovy vzorce B a C) pro výpočet pravděpodobnosti blokování hovoru. Formální přijetí a specifikace BHT pro GSM a následné technologie ze strany 3GPP zajistila, že zařízení od různých dodavatelů může být dimenzováno za použití stejných provozních předpokladů, což podporuje interoperabilitu a spravedlivé srovnání výkonu. Řeší omezení používání průměrného provozu, které by vedlo k vážnému přetížení během špiček, a neproveditelnost návrhu pro absolutní maximální okamžitý provoz, který by byl ekonomicky neúnosný.

V kontextu GERAN a širších mobilních sítí je BHT nezbytný pro přechod od hlasově orientovaných sítí k víceúčelovým sítím (hlas, SMS, data). Umožňuje operátorům vhodně dimenzovat samostatné zdroje pro okruhově přepínanou a paketově přepínanou doménu. Motivací pro jeho pokračující relevanci až po Rel-12 a dále ve specifikacích jako 45.926 je jeho přizpůsobivost. I když se sítě vyvíjejí k LTE a 5G, základní princip plánování pro vytíženou hodinu zůstává, ačkoliv konkrétní měření (např. objem dat v TB/hod.) a aplikace (např. BHT specifický pro řez) se vyvíjejí. Zůstává základním kamenem pro zajištění nákladově efektivního nasazení sítě, které splňuje smluvní dohody o úrovni služeb (SLA) a očekávání uživatelů.

## Klíčové vlastnosti

- Standardizované měření špičkového provozu definované v 3GPP TS 45.926
- Základní vstup pro výpočty dimenzování sítě a plánování kapacity
- Umožňuje aplikaci Erlangových vzorců pro cíle třídy služby (GoS)
- Podporuje jak okruhově přepínaný (erlangy), tak paketově přepínaný (objem dat) typ provozu
- Klíčový pro optimalizaci OPEX/CAPEX prevencí nadměrného i nedostatečného poskytování kapacity
- Poskytuje konzistentní měřítko pro výkon sítě a spouštěče jejího rozšiřování

## Související pojmy

- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)

## Definující specifikace

- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study

---

📖 **Anglický originál a plná specifikace:** [BHT na 3GPP Explorer](https://3gpp-explorer.com/glossary/bht/)
