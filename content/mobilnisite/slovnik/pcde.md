---
slug: "pcde"
url: "/mobilnisite/slovnik/pcde/"
type: "slovnik"
title: "PCDE – Peak Code Domain Error"
date: 2025-01-01
abbr: "PCDE"
fullName: "Peak Code Domain Error"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pcde/"
summary: "Klíčový parametr RF měření pro systémy založené na CDMA, jako je UMTS, který kvantifikuje kvalitu vysílaného signálu měřením ortogonalitní chyby mezi rozprostíracími kódy. Je zásadní pro zajištění výk"
---

PCDE je klíčový parametr RF měření v systémech založených na CDMA, jako je UMTS, který kvantifikuje kvalitu signálu vysílače měřením ortogonalitní chyby mezi rozprostíracími kódy.

## Popis

Peak Code Domain Error (PCDE) je základní měření konformity rádiové frekvence ([RF](/mobilnisite/slovnik/rf/)) definované pro vysílač uživatelského zařízení (UE) v systému UMTS (Universal Mobile Telecommunications System) podle 3GPP. Kvantifikuje odchylku od dokonalé ortogonality mezi různými rozprostíracími kódy používanými v downlinku (z NodeB do UE) a uplinku (z UE do NodeB). V systémech založených na [CDMA](/mobilnisite/slovnik/cdma/) jsou vícekanálová uživatelská spojení oddělena pomocí ortogonálních rozprostíracích kódů (např. [OVSF](/mobilnisite/slovnik/ovsf/) kódů). V ideálním případě jsou tyto kódy dokonale ortogonální, což znamená, že jejich vzájemná korelace je nulová a umožňuje dokonalé oddělení na přijímači. Nicméně nedokonalosti v modulaci vysílače, jako je fázový šum, I/Q nerovnováha a nelinearita zesilovače, způsobují chyby, které tuto ortogonalitu degradují. PCDE měří špičkový výkon této chyby v kódové doméně vztažený k celkovému vysílanému výkonu a je vyjádřen v dB.

Měření provádí testovací zařízení přijímající vysílaný signál UE. Přijímač despreduje signál pomocí sady možných ortogonálních kódů. Pro každý kódový kanál porovnává přijatý výkon s ideálním očekávaným výkonem. Chyba je rozdílem a PCDE je maximální (špičkový) výkon chyby nalezený mezi všemi měřenými kódovými kanály vztažený k celkovému výkonu signálu. Vysoká hodnota PCDE značí významnou neortogonalitu, což se projevuje zvýšenou víceuživatelskou interferencí. Tato interference snižuje kapacitu systému a může degradovat kvalitu signálu pro ostatní uživatele, což vede k možným výpadkům hovorů nebo sníženým datovým rychlostem.

Testování PCDE je povinnou součástí schvalování typu UE a certifikace, aby bylo zajištěno, že zařízení negenerují nadměrnou interferenci poškozující výkon sítě. Testovací podmínky, včetně specifických testovacích modelů a úrovní výkonu, jsou přesně definovány ve specifikaci 3GPP 25.141 pro konformitu základnové stanice (NodeB) a jsou odkazovány ve specifikacích pro testování UE. Sledování a kontrola PCDE je pro síťové operátory zásadní pro udržení vysoké spektrální účinnosti a kvality služeb v jejich sítích UMTS.

## K čemu slouží

PCDE byl zaveden k řešení kritického omezení výkonu v systémech s vícečetným přístupem s kódovým dělením ([CDMA](/mobilnisite/slovnik/cdma/)): víceuživatelské interference. V ideálním CDMA systému jsou uživatelé dokonale odděleni ortogonálními kódy. Nicméně reálné nedokonalosti vysílače tuto ortogonalitu narušují, což způsobuje, že signál jednoho uživatele se jeví jako šum pro ostatní. Tento jev, známý jako intracelulární interference, přímo omezuje kapacitu buňky – čím více interference, tím méně současných uživatelů nebo nižších datových rychlostí buňka podporuje.

Před standardizovanými metrikami, jako je PCDE, bylo zajištění kvality vysílače méně přesné. Vytvoření PCDE poskytlo standardizovanou, kvantifikovatelnou a opakovatelnou metodu pro měření špičkové úrovně této ortogonalitní chyby. To umožňuje výrobcům zařízení navrhovat vysílače, které tuto chybu minimalizují, a regulátorům a operátorům stanovit jasný a vynutitelný limit. Vynucováním maximální hodnoty PCDE zajišťuje 3GPP, že všechna UE a NodeB uváděná na trh udržují základní úroveň čistoty vysílače, čímž chrání celkový výkon a kapacitu sítě před degradací způsobenou špatně fungujícími jednotlivými zařízeními.

Jeho význam je zakořeněn v základní fyzice CDMA. Na rozdíl od [TDMA](/mobilnisite/slovnik/tdma/)/[FDMA](/mobilnisite/slovnik/fdma/) v GSM, kde jsou uživatelé odděleni v čase a frekvenci, uživatelé CDMA sdílejí stejnou frekvenci a čas a pro oddělení se spoléhají výhradně na ortogonalitu kódů. Proto je jakákoli metrika chránící tuto ortogonalitu pro životaschopnost této technologie prvořadá. PCDE zůstává klíčovým měřením pro UMTS a je konceptuálním předchůdcem podobných měření chybového vektorového modulu ([EVM](/mobilnisite/slovnik/evm/)) a kvality konstelace používaných v systémech založených na [OFDMA](/mobilnisite/slovnik/ofdma/), jako jsou LTE a NR, které čelí odlišným, ale analogickým výzvám linearity a přesnosti modulace.

## Klíčové vlastnosti

- Kvantifikuje neortogonalitu způsobenou vysílačem v CDMA systémech
- Měří se jako špičkový výkon chyby napříč všemi kódovými kanály vztažený k celkovému výkonu (dB)
- Zásadní pro kontrolu intracelulární interference a zachování kapacity sítě
- Definováno jako test konformity pro rádiový výkon UE i NodeB
- Testovací postupy a limity specifikovány v 3GPP TS 25.141 a souvisejících specifikacích pro UE
- Přímo ovlivňuje kvalitu spoje a kapacitu systému v sítích UMTS

## Související pojmy

- [CDMA – Code Division Multiple Access](/mobilnisite/slovnik/cdma/)
- [EVM – Error Vector Magnitude](/mobilnisite/slovnik/evm/)
- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [PCDE na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcde/)
