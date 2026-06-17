---
slug: "ep1"
url: "/mobilnisite/slovnik/ep1/"
type: "slovnik"
title: "EP1 – Elementary Procedure 1 (GSM Link Performance)"
date: 2025-01-01
abbr: "EP1"
fullName: "Elementary Procedure 1 (GSM Link Performance)"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ep1/"
summary: "Referenční bod pro měření výkonnosti GSM rádiového spoje, definovaný jako poměr nosná/rušení (C/I) 10 dB s hrubou chybovostí bitů (GBER) 5 %. Modeluje podmínky hluboko uvnitř buňky, daleko od rušením"
---

EP1 je referenční bod pro výkonnost GSM spojení definovaný jako poměr nosná/rušení (C/I) 10 dB vedoucí k hrubé chybovosti bitů (GBER) 5 %, modelující dobré podmínky hluboko uvnitř buňky.

## Popis

EP1 je specifická testovací podmínka definovaná ve specifikaci 3GPP TS 46.055 pro hodnocení výkonnosti GSM řečových kodeků a přidruženého kanálového kódování za řízeného rušení. Nejde o signalizační proceduru, ale o standardizovaný referenční bod pro charakterizaci výkonnosti. Podmínka je definována poměrem nosná/rušení ([C/I](/mobilnisite/slovnik/c-i/)) 10 decibelů (dB) a cílovou hrubou chybovostí bitů ([GBER](/mobilnisite/slovnik/gber/)) 5 %. Poměr C/I je klíčovou metrikou v celulárních sítích, která vyjadřuje sílu požadovaného signálu (nosná) vůči součtu rušivých signálů (rušení) z jiných buněk používajících stejnou frekvenci.

Prakticky řečeno, C/I 10 dB představuje relativně vysokou kvalitu rádiového spoje. Tento poměr značí, že výkon požadovaného signálu je desetkrát silnější než výkon rušení. Za těchto podmínek jsou schémata kanálového kódování a prokládání v GSM navržena tak, aby opravila většinu přenosových chyb, což vede k hrubé chybovosti bitů (GBER) 5 % před dekódováním kanálu. 'Hrubá' [BER](/mobilnisite/slovnik/ber/) se měří na zakódovaném bitovém toku po demodulaci, ale před aplikací korekce chyb ([FEC](/mobilnisite/slovnik/fec/)). GBER 5 % při této úrovni C/I je považována za přijatelnou, protože následný kanálový dekodér (např. pro plnorychlostnní nebo rozšířený plnorychlostní řečový kanál) dokáže úspěšně obnovit původní řečové rámce a poskytnout dobrou kvalitu hlasu.

Definice EP1 slouží jako srovnávací měřítko. Výrobci zařízení a projektanti sítí tuto podmínku používají k ověření, že mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) nebo subsystém základnové stanice ([BSS](/mobilnisite/slovnik/bss/)) splňuje minimální požadavky na výkonnost pro provoz v nekritických oblastech buňky. Když je zařízení testováno 'na EP1', znamená to, že výkonnost jeho přijímače je hodnocena pomocí testovacího signálu simulujícího toto specifické rušivé prostředí. Poté se měří výkonnostní metriky jako podíl zamítnutých rámců ([FER](/mobilnisite/slovnik/fer/)) nebo střední známka kvality řeči ([MOS](/mobilnisite/slovnik/mos/)), aby se zajistila shoda. To umožňuje konzistentní a srovnatelné testování výkonnosti napříč různými hardwarovými implementacemi.

## K čemu slouží

EP1 byl vytvořen, aby poskytl standardizovanou, opakovatelnou testovací podmínku pro kvantifikaci odolnosti GSM hlasových služeb vůči ko-kanálovému rušení. Před takovými standardizovanými referenčními body bylo obtížné objektivně porovnávat výkonnost různých mobilních přístrojů nebo síťových infrastrukturních zařízení. Definováním konkrétního C/I a očekávané GBER stanovil 3GPP společné měřítko, které musí všichni dodavatelé splňovat, čímž je zajištěna základní úroveň kvality hlasu pro účastníky nacházející se v oblastech s dobrými podmínkami signálu.

Řeší problém ověřování výkonnosti v řízeném, laboratorním prostředí, které koreluje se skutečnými síťovými podmínkami. 'Hluboko uvnitř buňky' je typický pracovní bod pro mnoho uživatelů. Definice této podmínky umožňuje inženýrům izolovat a testovat výkonnost řečového kodeku, kanálového kódování a demodulátoru bez extrémního zatížení podmínkami na okraji buňky. Zajišťuje, že základní výpočty úrovně signálu a citlivosti přijímače pro plánování sítě jsou založeny na všeobecně přijímaném kritériu výkonnosti.

Historicky se tyto typy výkonnostních bodů staly klíčovými s hustými vzory opakování frekvencí v GSM sítích, kde je rušení ze sousedních buněk používajících stejnou frekvenci (ko-kanálové rušení) hlavním limitujícím faktorem kapacity. EP1 spolu s EP2 poskytují dvoubodový model výkonnosti systému, pokrývající scénáře jak s dobrým, tak se špatným pokrytím. To bylo motivováno potřebou garantovat kvalitu služeb a podpořit zlepšování technologie přijímačů, což přímo ovlivňuje kapacitu sítě a uživatelský zážitek.

## Klíčové vlastnosti

- Definuje referenční poměr nosná/rušení (C/I) 10 dB
- Stanovuje cílovou hrubou chybovost bitů (GBER) 5 %
- Modeluje rádiové podmínky 'hluboko uvnitř buňky'
- Používá se pro testování shody výkonnosti GSM řečového kanálu
- Poskytuje měřítko pro citlivost přijímače za středního rušení
- Umožňuje srovnatelné hodnocení výkonnosti zařízení různých dodavatelů

## Související pojmy

- [EP2 – Elementary Procedure 2 (GSM Link Performance)](/mobilnisite/slovnik/ep2/)
- [GBER – Average Gross Bit Error Rate](/mobilnisite/slovnik/gber/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [EP1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/ep1/)
