---
slug: "rua"
url: "/mobilnisite/slovnik/rua/"
type: "slovnik"
title: "RUA – RANAP User Adaptation"
date: 2025-01-01
abbr: "RUA"
fullName: "RANAP User Adaptation"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rua/"
summary: "RUA je protokolová vrstva, která přenáší zprávy RANAP přes IP signalizační transportní sítě, jako je Iu-flex. Umožňuje oddělení řídicí a uživatelské roviny a podporuje efektivní signalizaci mezi RNC a"
---

RUA je protokol, který přenáší signalizační zprávy RANAP přes sítě založené na IP a umožňuje efektivní řídicí signalizaci mezi RNC a jádrovou sítí v systémech 3G UMTS.

## Popis

[RANAP](/mobilnisite/slovnik/ranap/) User Adaptation (RUA) je klíčový adaptační vrstvový protokol definovaný ve standardech 3GPP, který je speciálně navržen pro usnadnění přenosu signalizačních zpráv RANAP (Radio Access Network Application Part) přes IP transportní sítě. Funguje jako součást architektury rozhraní Iu, které spojuje Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)) s jádrovou sítí (CN). RUA funguje tak, že zapouzdřuje zprávy RANAP, které jsou inherentně navrženy pro přepojování okruhů (např. přes [SS7](/mobilnisite/slovnik/ss7/)), do formátu vhodného pro přenos přes paketové IP sítě. Tato adaptace je dosažena definovanou strukturou zpráv, která zahrnuje hlavičky pro správu relací, řízení toku a zpracování chyb, čímž zajišťuje spolehlivé a uspořádané doručování signalizačních informací mezi RNC a uzly jádrové sítě, jako je [MSC](/mobilnisite/slovnik/msc/) nebo [SGSN](/mobilnisite/slovnik/sgsn/).

Architektonicky se RUA nachází nad spolehlivou transportní vrstvou, typicky Stream Control Transmission Protocol ([SCTP](/mobilnisite/slovnik/sctp/)), která poskytuje spojově orientovaný přenos dat bez chyb. Protokol navazuje asociace (logická spojení) mezi koncovými body RNC a CN a spravuje více proudů v rámci jedné asociace, aby nezávisle zpracovával různé signalizační dialogy, čímž předchází blokování hlavy fronty. Mezi klíčové komponenty RUA patří entita RUA vrstvy, která zpracovává adaptaci, a nad ní umístěná RANAP vrstva, která generuje vlastní signalizaci rádiové sítě. RUA také podporuje funkce jako mechanismus heartbeat pro monitorování asociací a postupy řádného uvolnění pro udržení stability sítě.

V širším síťovém kontextu hraje RUA klíčovou roli při umožnění pokročilých architektur, jako je Iu-flex, kde více uzlů jádrové sítě může obsluhovat jediné RNC, což zvyšuje vyrovnávání zátěže a redundanci. Díky abstrakci podkladového transportu umožňuje RUA, aby RANAP zůstal nezměněn, čímž zachovává interoperabilitu při modernizaci transportní infrastruktury. Jeho provoz zahrnuje přenos zpráv, navázání a ukončení asociace a hlášení chyb, čímž zajišťuje, že kritické funkce, jako je nastavení rádiového přenosového kanálu, řízení předávání hovoru a paging, jsou efektivně podporovány přes IP, což přispívá k vývoji směrem k plně IP sítím ve 3G a dalších generacích.

## K čemu slouží

RUA byl vytvořen, aby řešil omezení tradiční signalizace s přepojováním okruhů v sítích UMTS, která spoléhala na [SS7](/mobilnisite/slovnik/ss7/) a byla neefektivní pro vznikající infrastruktury založené na IP. Jak se sítě 3GPP vyvíjely směrem k plně IP architekturám, vznikla potřeba oddělit řídicí a uživatelskou rovinu a využít nákladově efektivní a škálovatelný IP transport pro signalizaci. RUA to umožňuje tím, že adaptuje RANAP, klíčový signalizační protokol pro komunikaci UTRAN-CN, pro běh přes IP sítě, čímž usnadňuje funkce jako Iu-flex a podporuje konsolidaci sítě.

Historicky dřívější verze UMTS používaly přímý RANAP přes ATM nebo SS7, což postrádalo flexibilitu a škálovatelnost pro distribuované jádrové sítě. RUA tyto problémy řeší tím, že poskytuje standardizovanou metodu pro přenos RANAP přes SCTP/IP, což umožňuje lepší distribuci zátěže, redundanci a zjednodušenou správu sítě. Jeho zavedení ve verzi 8 bylo motivováno snahou o provozní efektivitu a přechod k plošším a přizpůsobivějším síťovým architekturám, což je v souladu s širším odvětvovým posunem směrem k telekomunikacím založeným na IP.

## Klíčové vlastnosti

- Zapouzdřuje zprávy RANAP pro IP transport
- Funguje nad SCTP pro spolehlivý přenos
- Podporuje více proudů v rámci jedné asociace
- Umožňuje architekturu Iu-flex pro sdružování jádrové sítě
- Poskytuje mechanismy heartbeat a hlášení chyb
- Usnadňuje oddělení řídicí a uživatelské roviny

## Související pojmy

- [RANAP – Radio Access Network Application Protocol](/mobilnisite/slovnik/ranap/)
- [SCTP – Stream Control Transmission Protocol](/mobilnisite/slovnik/sctp/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TS 23.826** (Rel-9) — Voice Call Continuity for Emergency Calls
- **TS 23.892** (Rel-8) — IMS Centralized Services Control
- **TS 25.468** (Rel-19) — RANAP User Adaption (RUA) protocol specification
- **TS 25.820** (Rel-8) — 3G Home NodeB Study Report

---

📖 **Anglický originál a plná specifikace:** [RUA na 3GPP Explorer](https://3gpp-explorer.com/glossary/rua/)
