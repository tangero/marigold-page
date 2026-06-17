---
slug: "dbss"
url: "/mobilnisite/slovnik/dbss/"
type: "slovnik"
title: "DBSS – Drift Base Station Subsystem"
date: 2025-01-01
abbr: "DBSS"
fullName: "Drift Base Station Subsystem"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dbss/"
summary: "DBSS označuje driftovou podsystém základnové stanice v sítích 3GPP UMTS, konkrétně v rámci architektury UTRAN. Jedná se o BSS (podsystém základnové stanice), který není přímo připojen k ústředně MSC j"
---

DBSS je driftová podsystém základnové stanice v sítích UMTS, která se k ústředně MSC jádra sítě připojuje přes jiný BSS namísto přímého spojení pro směrování a správu předávání hovoru.

## Popis

Driftová podsystém základnové stanice (DBSS) je základní architektonický koncept v rámci rádiové přístupové sítě 3GPP UMTS (UTRAN), definovaný v technické specifikaci 25.423. Funguje v kontextu rozhraní Iur, které propojuje dva řadiče rádiové sítě (RNC). V této architektuře, když je uživatelské zařízení (UE) zapojeno do předávání hovoru mezi RNC nebo využívá prostředky od RNC odlišného od svého řídicího RNC, zaujímají zúčastněné RNC specifické role: obsluhující RNC (SRNC) a driftový RNC ([DRNC](/mobilnisite/slovnik/drnc/)). DBSS je souhrnný termín pro síťové prvky (především DRNC a jím řízené Node B), které poskytují uživatelskému zařízení rádiové prostředky, ale nejsou primárním bodem kontroly pro připojení tohoto UE k jádru sítě.

DBSS funguje tak, že mezi SRNC a DRNC vytváří přes rozhraní Iur logické spojení. SRNC udržuje připojení k jádru sítě (CN) přes rozhraní Iu a zpracovává protokoly vyšších vrstev, jako je řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)). DRNC jako součást DBSS poskytuje UE dodatečné rádiové prostředky (např. buňky). Uživatelská a řídicí data jsou tunelována mezi SRNC a DRNC. DRNC je zodpovědný za přidělování a správu rádiových prostředků (jako jsou kanalizační kódy) ve svých buňkách a provádí plánování nižších vrstev a kombinaci/dekombinaci pro makrodiverzitu, pokud se UE nachází v měkkém předávání hovoru mezi Node B patřícími k různým RNC.

Klíčové součásti DBSS zahrnují samotný driftový RNC (DRNC) a skupinu základnových stanic Node B pod jeho kontrolou, které UE využívá. DRNC obsahuje nezbytnou funkcionalitu pro správu rozhraní Iur, přidělování prostředků pro "driftyjící" UE a rozdělování/kombinování datových proudů pro rádiové rozhraní. Úlohou DBSS je rozšířit služební oblast a kapacitu dostupnou pro UE bez nutnosti předání bodu připojení k jádru sítě (SRNC). To umožňuje flexibilnější využití prostředků a efektivní podporu mobility, zejména v hustých nebo překrývajících se nasazeních sítě.

Z pohledu protokolů se DBSS účastní specifických signalizačních procedur na Iur. SRNC řídí spojení pomocí signalizace RNSAP (Radio Network Subsystem Application Part) směrem k DRNC. DRNC převážně jedná na základě příkazů od SRNC týkajících se nastavení, přidání a zrušení rádiového spoje pro UE. Uživatelská data jsou přenášena mezi RNC pomocí přenosových kanálů Iur, které jsou typicky založeny na [ATM](/mobilnisite/slovnik/atm/) nebo IP v závislosti na implementaci sítě. Koncept DBSS je nedílnou součástí distribuované architektury UTRAN a umožňuje funkce jako měkké předávání hovoru mezi RNC a tvrdé předávání hovoru mezi RNC, které jsou nezbytné pro plynulou mobilitu a kontinuitu služeb.

## K čemu slouží

Koncept DBSS byl vytvořen, aby řešil omezení rigidní architektury řízené jediným RNC v sítích UMTS. V raných návrzích celulárních sítí byl mobilní terminál typicky obsluhován jediným řadičem základnových stanic. Jak však sítě houstly a vzorce mobility uživatelů se stávaly složitějšími, byl potřebný mechanismus, který by umožnil uživateli využívat rádiové prostředky z více geograficky oddělených domén řadičů, aniž by docházelo k signalizační zátěži a potenciálnímu přerušení služby v důsledku neustálého přesunu kotvícího bodu v jádře sítě (připojení k [MSC](/mobilnisite/slovnik/msc/) nebo SGSN). Architektura DBSS to řeší zavedením hierarchického modelu řízení.

Konkrétně řeší problém efektivního využití prostředků a plynulé mobility přes administrativní hranice uvnitř RAN. Bez konceptu DBSS/driftového RNC by pokaždé, když by UE přešlo do buňky řízené jiným RNC, byla vyžadována úplná procedura přesunu SRNC s účastí jádra sítě. Jedná se o složitý postup, který může ovlivnit kvalitu hovoru. Model DBSS umožňuje UE "driftyovat" do pokrytí jiného RNC, využívat jeho prostředky, a zároveň si zachovat původní signalizační spojení ([RRC](/mobilnisite/slovnik/rrc/) spojení) a cestu k jádru sítě přes původní obsluhující RNC (SRNC). Tím se minimalizuje signalizace v jádře sítě, snižuje se zpoždění při předávání hovoru a umožňují se pokročilé funkce, jako je kombinování makrodiverzity mezi RNC.

Historicky šlo o významný vývoj oproti architektuře [BSS](/mobilnisite/slovnik/bss/) v GSM, kde měl řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) přímější a výlučnější vztah k obsluhované [MS](/mobilnisite/slovnik/ms/). Návrh UTRAN od 3GPP, s oddělením rolí SRNC a DRNC, poskytl flexibilnější a škálovatelnější rámec pro správu rádiových prostředků v síti orientované na pakety podporující vysokorychlostní data a sofistikované typy předávání hovoru. DBSS je tedy základním kamenem schopnosti UTRAN podporovat měkké předávání hovoru mezi Node B připojenými k různým RNC, což je klíčová vlastnost pro zlepšení pokrytí a kvality na hranicích buněk.

## Klíčové vlastnosti

- Umožňuje mobilitu mezi RNC bez přesunu SRNC
- Podporuje procedury měkkého a tvrdého předávání hovoru mezi RNC
- Umožňuje sdílení prostředků přes administrativní hranice RNC
- Minimalizuje signalizaci jádra sítě pro mobilitu uživatele
- Umožňuje kombinování makrodiverzity z Node B pod různými RNC
- Pro řízení (RNSAP) a tunelování uživatelských dat mezi RNC využívá rozhraní Iur

## Související pojmy

- [DRNC – Drift Radio Network Controller](/mobilnisite/slovnik/drnc/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification

---

📖 **Anglický originál a plná specifikace:** [DBSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dbss/)
