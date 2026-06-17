---
slug: "nc1"
url: "/mobilnisite/slovnik/nc1/"
type: "slovnik"
title: "NC1 – Network Control mode 1"
date: 2025-01-01
abbr: "NC1"
fullName: "Network Control mode 1"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nc1/"
summary: "NC1 je režim síťového řízení definovaný pro optimalizaci GSM/EDGE Radio Access Network (GERAN). Specifikuje režim, v němž síť poskytuje mobilní stanici řídicí parametry, které pak autonomně provádí mě"
---

NC1 je režim síťového řízení GERAN, v němž síť poskytuje řídicí parametry, což mobilní stanici umožňuje autonomně provádět a hlásit měření za účelem optimalizace správy rádiových zdrojů a snížení signalizační zátěže.

## Popis

Network Control mode 1 (NC1) je specifický operační režim definovaný ve specifikacích 3GPP [GERAN](/mobilnisite/slovnik/geran/) pro řízení procedur hlášení měření mobilní stanice ([MS](/mobilnisite/slovnik/ms/)). V tomto režimu síť (konkrétně Base Station Controller, [BSC](/mobilnisite/slovnik/bsc/)) poskytne MS sadu řídicích parametrů, jako jsou prahové hodnoty měření, kritéria pro hlášení a seznam sousedních buněk ke sledování. MS poté autonomně provádí požadovaná měření kvality a úrovně signálu jak u obsluhující, tak u sousedních buněk na základě těchto parametrů. Průběžně vyhodnocuje kritéria pro hlášení vůči výsledkům měření. MS odešle hlášení o měření síti pouze při splnění předdefinovaných podmínek (např. když signál sousední buňky překročí signál obsluhující buňky o určitý offset). Toto hlášení spouštěné událostí je klíčovou charakteristikou, navrženou ke snížení zbytečného signalizačního provozu v uplinku ve srovnání s periodickým hlášením.

Architektura zahrnuje BSC jako řídicí entitu, která konfiguruje parametry NC1 prostřednictvím signalizačních zpráv vrstvy 3, typicky v informačních prvcích kanálu SACCH (Slow Associated Control Channel). Fyzická vrstva MS provádí vlastní RF měření, zatímco její protokolový stack spravuje logiku vyhodnocení. Role NC1 je nedílnou součástí funkcí jako příprava handoveru a řízení výkonu. Díky přijímání cílených hlášení pouze při výskytu specifických rádiových podmínek může síť činit informovanější a včasnější rozhodnutí o tom, zda zahájit handover, aniž by byla zaplavována neustálými měřicími daty od všech připojených mobilních zařízení.

Klíčové komponenty procedury NC1 zahrnují řídicí zprávu měření ze sítě, interní měřicí a vyhodnocovací jednotku MS a následnou zprávu hlášení měření. Řídicí parametry definují 'popis sousední buňky' (číslo absolutního rádiového kmitočtového kanálu, [ARFCN](/mobilnisite/slovnik/arfcn/), které se má měřit), měřenou veličinu (např. Received Signal Strength Indication, RSSI) a pravidla pro hlášení. NC1 představuje vyvážený přístup k síťově řízené mobilitě, který poskytuje autonomii MS pro vyhodnocení podmínek za účelem optimalizace jak využití rádiových zdrojů, tak spotřeby baterie v zařízení, protože vysílač zařízení není pro hlášení aktivován, není-li to nutné.

## K čemu slouží

NC1 byl zaveden za účelem zvýšení efektivity hlášení měření v sítích GSM/[EDGE](/mobilnisite/slovnik/edge/). Před zavedením těchto síťově řízených režimů mohly jednodušší přístupy vést k nadměrné signalizaci nebo opožděným handoverům. Účelem NC1 je delegovat vyhodnocení podmínek na mobilní stanici, čímž se minimalizuje signalizační zátěž v uplinku na rádiovém rozhraní a sníží se latence detekce událostí vhodných pro handover. To je klíčové v celulárních sítích, kde jsou rádiové zdroje omezené a signalizační zátěž přímo ovlivňuje kapacitu a uživatelský zážitek.

Jeho vytvoření bylo motivováno potřebou inteligentnější správy rádiových zdrojů (RRM) s růstem hustoty sítě a počtu účastníků. Díky poskytnutí možnosti konfigurovat přesné spouštěče hlášení síti umožňuje NC1 proaktivní správu handoveru, což zlepšuje míru přerušení hovorů a celkovou kvalitu služeb. Řeší omezení jak síťově dotazovaných měření (která zavádějí zpoždění), tak nežádaných periodických hlášení od [MS](/mobilnisite/slovnik/ms/) (která plýtvají šířkou pásma). NC1 nachází rovnováhu a umožňuje síťově řízenou optimalizaci procedur mobility.

Historicky je NC1 součástí sady režimů síťového řízení definovaných pro [GERAN](/mobilnisite/slovnik/geran/), což odráží vývoj směrem k sofistikovanějším řídicím mechanismům. Poskytuje základní metodu pro hlášení řízené událostmi, která později ovlivnila principy konfigurace měření v systémech 3G UMTS a 4G LTE, ačkoli implementované s odlišnými protokoly a terminologií. Jeho specifikace v dokumentu 45.926 podtrhuje jeho roli v průběžné optimalizaci klasických sítí GSM.

## Klíčové vlastnosti

- Parametry měření a kritéria pro hlášení konfigurované sítí
- Autonomní vyhodnocování podmínek pro hlášení mobilní stanicí
- Hlášení měření spouštěné událostí pro minimalizaci signalizace
- Podpora měření síly/kvality signálu obsluhující a sousední buňky
- Konfigurace prostřednictvím řídicích zpráv rádiových zdrojů vrstvy 3
- Nedílná součást přípravy rozhodnutí o handoveru v GERAN

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [NC2 – Network Control mode 2](/mobilnisite/slovnik/nc2/)

## Definující specifikace

- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study

---

📖 **Anglický originál a plná specifikace:** [NC1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/nc1/)
