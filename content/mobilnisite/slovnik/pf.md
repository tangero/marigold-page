---
slug: "pf"
url: "/mobilnisite/slovnik/pf/"
type: "slovnik"
title: "PF – Probability Factor"
date: 2025-01-01
abbr: "PF"
fullName: "Probability Factor"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pf/"
summary: "Klíčový parametr v algoritmu plánování Proportional Fair (PF) používaném základnovými stanicemi (eNodeB/gNB) v LTE a 5G NR. Dynamicky počítá metriku priority pro každého uživatele, čímž vyvažuje cíl m"
---

PF je parametr v algoritmu plánování Proportional Fair, který počítá metriku priority pro každého uživatele, aby vyvážil celkovou propustnost buňky se spravedlností.

## Popis

Probability Factor (PF) je klíčový výpočetní prvek v široce nasazovaném algoritmu plánování Proportional Fair (PF) používaném v downlinku a uplinku mobilních sítí, jako jsou LTE a 5G New Radio (NR). Plánovač, umístěný ve vrstvě Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) základnové stanice, se musí v každém Transmission Time Intervalu ([TTI](/mobilnisite/slovnik/tti/)) a na každém Physical Resource Block ([PRB](/mobilnisite/slovnik/prb/)) rozhodnout, kterému uživatelskému zařízení (UE) bude přidělen zdroj. Algoritmus PF usiluje o dosažení vícekriteriální optimalizace: maximalizaci celkové spektrální účinnosti buňky (propustnosti) při zachování určité míry spravedlnosti, aby uživatelé se špatnými podmínkami na rádiovém kanále (např. na okraji buňky) stále dostávali službu. Metrika PF pro daného uživatele 'i' v čase plánování 't' se vypočítá jako: PF_i(t) = DRCi(t) / T_i(t), kde DRCi(t) je okamžitá datová rychlost, kterou může uživatel podporovat (na základě nahlášeného Channel Quality Indicator - [CQI](/mobilnisite/slovnik/cqi/)), a T_i(t) je exponenciálně vážený průměrný výkon uživatele za uplynulé časové okno.

Algoritmus funguje tak, že pro každého aktivního uživatele průběžně aktualizuje dvě klíčové hodnoty. Za prvé, okamžitě dosažitelná rychlost ([DRC](/mobilnisite/slovnik/drc/)) je odvozena z informace o stavu kanálu, kterou UE často hlásí. Tato rychlost je vysoká, když má uživatel dobré rádiové podmínky (např. vysoký Signal-to-Interference-plus-Noise Ratio - [SINR](/mobilnisite/slovnik/sinr/)), a nízká, když jsou podmínky špatné. Za druhé, průměrný výkon (T_i) se aktualizuje pomocí filtru klouzavého průměru: T_i(t+1) = (1 - 1/t_c) * T_i(t) + (1/t_c) * R_i(t), kde t_c je časová konstanta filtru a R_i(t) je skutečná datová rychlost přidělená uživateli v aktuálním TTI (která je nulová, pokud uživatel nebyl naplánován). Časová konstanta t_c řídí okno spravedlnosti; větší t_c klade důraz na dlouhodobou spravedlnost, zatímco menší t_c činí plánovač více oportunistickým.

Při každém rozhodnutí o plánování základnová stanice vypočítá metriku PF (DRC/T) pro všechny kandidátní uživatele. Uživatel s nejvyšší metrikou PF získá zdroj. Tím se elegantně vyvažují oba cíle: uživatel s momentálně vysokou DRC (díky dobrému kanálu) získá vysokou prioritu, což podporuje propustnost. Pokud však uživatel nebyl dlouho naplánován, jeho průměrný výkon T_i klesá, což zvyšuje jeho metriku PF, a tedy i šanci na naplánování příště, což vynucuje spravedlnost. Plánovač PF je adaptivní a bere v úvahu stav kanálu, což jej činí vysoce účinným pro paketové datové služby s přerušovaným provozem. Jeho výkon a parametry (jako časová konstanta filtru) jsou podrobně popsány ve specifikacích 3GPP pro studii výkonnosti (např. TR 37.470, TR 38.470) a tvoří základ pro pokročilejší plánovače s ohledem na QoS, které zahrnují více tříd QoS a požadavky na latenci.

## K čemu slouží

Plánovač Proportional Fair a jeho Probability Factor (faktor pravděpodobnosti) byly vyvinuty k řešení základních výzev v plánování paketů na sdíleném kanálu pro mobilní datové sítě, což představuje posun oproti omezením jednodušších algoritmů. Rané přístupy k plánování, jako je Maximum [CQI](/mobilnisite/slovnik/cqi/) (Max-C/I), které vždy obslouží uživatele s nejlepší okamžitou kvalitou kanálu, maximalizují celkovou propustnost buňky, ale jsou krajně nespravedlivé – uživatelé na okraji buňky nebo v hlubokém útlumu mohou být na neurčito ochuzeni o zdroje. Naopak, čistě round-robin plánovač je dokonale spravedlivý v čase, ale ignoruje podmínky na kanálu, což vede k velmi nízké spektrální účinnosti, protože zdroje jsou plýtvány na uživatele se špatnými kanály, kteří mohou podporovat pouze nízké datové rychlosti.

Algoritmus PF byl koncipován tak, aby našel optimální kompromis mezi těmito dvěma extrémy propustnosti a spravedlnosti, což je zásadní pro komerční sítě obsluhující mix uživatelů s různými podmínkami na kanálu a očekáváními služeb. Umožňuje zisk z "multi-user diversity" (různorodosti více uživatelů) tím, že využívá skutečnost, že různí uživatelé v čase zažívají nezávislé fluktuace kanálu; plánovač může vybrat uživatele, který je právě na vrcholu kanálu. Probability Factor poskytuje matematický mechanismus pro kvantifikaci této příležitosti vzhledem k historické službě uživatele, což zajišťuje, že uživatel čekající na vrchol kanálu bude nakonec obsloužen.

Jeho zavedení a standardizace v 3GPP (od verze LTE Release 6 dále) byla hnána potřebou efektivní podpory datových služeb typu best-effor pro přístup k internetu (jako je prohlížení webu a stahování souborů) přes sdílené rádiové zdroje. Plánovač PF se stal výchozím nebo vysoce doporučovaným algoritmem pro non-GBR (Guaranteed Bit Rate) přenosy. Poskytl robustní, předvídatelnou a implementovatelnou strategii plánování, kterou mohli dodavatelé sítí optimalizovat a operátoři ladit (pomocí parametru průměrovacího okna), aby odpovídala jejich specifickým cílům politiky spravedlnost-propustnost, čímž položil základ pro pozdější, složitější plánovače podporující služby kritické na latenci a rozlišené podle QoS v 4G a 5G.

## Klíčové vlastnosti

- Dynamická metrika priority vyvažující okamžitou kvalitu kanálu a historický výkon
- Umožňuje zisk z různorodosti více uživatelů plánováním uživatelů na vrcholu jejich kanálu
- Konfigurovatelné okno spravedlnosti pomocí časové konstanty exponenciálního průměrování
- Použitelné pro plánování downlinku i uplinku v LTE a NR
- Tvoří základ pro rozšíření s ohledem na QoS a plánování více služeb
- Standardizovaná metodika hodnocení výkonnosti v technických zprávách 3GPP

## Související pojmy

- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 25.346** (Rel-19) — MBMS in UTRA Technical Specification
- **TS 28.311** (Rel-19) — Policy Management for 4G Networks
- **TS 37.470** (Rel-19) — W1 Interface Introduction for ng-eNB
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.470** (Rel-19) — F1 Interface Introduction
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TR 38.864** (Rel-18) — Technical Report on Network Energy Savings for NR

---

📖 **Anglický originál a plná specifikace:** [PF na 3GPP Explorer](https://3gpp-explorer.com/glossary/pf/)
