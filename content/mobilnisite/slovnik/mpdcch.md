---
slug: "mpdcch"
url: "/mobilnisite/slovnik/mpdcch/"
type: "slovnik"
title: "MPDCCH – MTC Physical Downlink Control Channel"
date: 2025-01-01
abbr: "MPDCCH"
fullName: "MTC Physical Downlink Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mpdcch/"
summary: "Fyzický downlinkový řídicí kanál v LTE navržený speciálně pro zařízení pro komunikaci mezi stroji (MTC), zejména pro ta pracující v režimech se zvýšeným pokrytím. Přenáší downlinkové řídicí informace"
---

MPDCCH je fyzický downlinkový řídicí kanál v LTE navržený pro zařízení pro komunikaci mezi stroji (MTC), optimalizovaný pro nízkou složitost a zvýšení pokrytí tím, že přenáší řídicí informace pro plánování přenosů dat.

## Popis

[MTC](/mobilnisite/slovnik/mtc/) Physical Downlink Control Channel (MPDCCH) je specializovaný fyzický kanál zavedený v LTE Release 13 jako součást vylepšení pro komunikaci mezi stroji (MTC), známou také jako LTE-M nebo eMTC. Je variantou původního Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) a Enhanced PDCCH ([EPDCCH](/mobilnisite/slovnik/epdcch/)), optimalizovanou pro požadavky MTC zařízení, které zahrnují nízkou cenu, nízkou spotřebu energie a zvýšené pokrytí. MPDCCH přenáší downlinkové řídicí informace ([DCI](/mobilnisite/slovnik/dci/)), které poskytují plánovací přiřazení a řídicí příkazy MTC uživatelským zařízením (UE). Konkrétně informuje UE o přidělení zdrojů pro Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)), kde jsou odesílána downlinková data, a pro Physical Uplink Shared Channel (PUSCH) pro uplinkové přenosy dat, stejně jako o příkazech pro řízení výkonu.

Z architektonického hlediska je MPDCCH vysílán v datové oblasti LTE podrámce, podobně jako EPDCCH, nikoli v řídicí oblasti jako původní PDCCH. To umožňuje flexibilnější přidělování zdrojů a plánování ve frekvenční oblasti. Skládá se z úrovní agregace ([AL](/mobilnisite/slovnik/al/)), kde jsou řídicí kanálové elementy ([CCE](/mobilnisite/slovnik/cce/)) agregovány, aby poskytly různé kódovací rychlosti a přizpůsobily se kanálovým podmínkám UE. Pro MTC UE v režimech se zvýšeným pokrytím (Coverage Enhancement, [CE](/mobilnisite/slovnik/ce/)) MPDCCH podporuje opakování napříč více podrámci, aby bylo dosaženo potřebného linkového rozpočtu pro zařízení v hlubokém vnitřním prostředí nebo venkovských oblastech. UE je konfigurováno pomocí signalizace vyšší vrstvy (RRC) s konkrétními parametry MPDCCH, včetně prohledávacího prostoru (sady kandidátních umístění řídicího kanálu) a počtu opakování.

Princip fungování spočívá v tom, že UE monitoruje svůj nakonfigurovaný prohledávací prostor MPDCCH pro formáty DCI relevantní pro MTC, jako jsou formáty DCI 6-0A/6-0B pro uplinková povolení a 6-1A/6-1B pro downlinková přiřazení. Tyto formáty DCI jsou kompaktní, navržené tak, aby snížily počet pokusů o slepé dekódování a šetřily energii UE. MPDCCH používá stejné zpracování na fyzické vrstvě jako EPDCCH, včetně scramblingu, modulace (QPSK), předkódování a mapování na zdrojové elementy. Pro zvýšení pokrytí může být stejný přenos MPDCCH opakován přes konfigurovatelný počet podrámců (např. od 1 do 256 opakování) a UE provádí měkké kombinování těchto opakování, aby úspěšně dekódovalo DCI. MPDCCH také podporuje jak společný, tak UE-specifický prohledávací prostor, což umožňuje broadcastové zprávy (jako paging nebo odpovědi na náhodný přístup) i dedikované plánování. Jeho role je klíčová pro efektivní plánování v masivních IoT nasazeních, zajišťující, že MTC zařízení s nízkou složitostí mohou spolehlivě přijímat řídicí informace i v podmínkách špatného pokrytí, což je zásadní pro aplikace jako chytré měřiče, sledovače aktiv a nositelná zařízení.

## K čemu slouží

MPDCCH byl vytvořen, aby řešil specifické požadavky řídicího kanálu pro zařízení pro komunikaci mezi stroji (MTC) v LTE sítích. Původní LTE řídicí kanály (PDCCH/EPDCCH) byly navrženy pro výkonné smartfony a nebyly optimální pro MTC zařízení, která se vyznačují omezenou výpočetní kapacitou, sníženou podporou šířky pásma (často 1,4 MHz) a potřebou extrémního zvýšení pokrytí. PDCCH, umístěný v prvních několika symbolech podrámce, postrádal flexibilitu a podporu opakování potřebnou pro hluboké pokrytí. EPDCCH, ačkoli flexibilnější, nezahrnoval optimalizace pro dekódování s nízkou složitostí a úsporu energie, které jsou zásadní pro IoT zařízení napájená bateriemi.

Hlavním problémem, který MPDCCH řeší, je poskytování spolehlivé řídicí signalizace MTC UE, zejména těm v náročných rádiových podmínkách, jako jsou sklepy nebo odlehlá zemědělská místa, bez nadměrné spotřeby energie. Podporou opakování a použitím kompaktních formátů DCI zajišťuje, že řídicí informace mohou dosáhnout těchto zařízení a umožnit plánovanou datovou komunikaci. To byl klíčový prvek pro LTE-M (eMTC), který umožnil LTE sítím efektivně podporovat masivní IoT nasazení vedle tradičních širokopásmových služeb.

Historicky byl zaveden v 3GPP Release 13 jako součást vylepšení LTE pro MTC, která zahrnovala také funkce jako snížená šířka pásma zařízení, nižší špičkové datové rychlosti a rozšířené nespojité příjímání (eDRX). MPDCCH přímo řešil omezení předchozích řídicích kanálů v podpoře režimů zvýšení pokrytí až o 15 dB nad typické LTE pokrytí. Mezi motivace jeho návrhu patřila minimalizace složitosti UE (snížení kandidátů pro slepé dekódování), umožnění efektivního využití systémových zdrojů pro velký počet zařízení a zajištění zpětné kompatibility, aby přenosy MPDCCH mohly koexistovat s původním LTE provozem ve stejném nosiči. To umožnilo operátorům nasazovat IoT služby s využitím jejich stávajícího LTE spektra a infrastruktury.

## Klíčové vlastnosti

- Optimalizován pro MTC UE s podporou provozu v šířce pásma 1,4 MHz
- Podporuje opakování pro zvýšení pokrytí (režimy CE A a B)
- Používá kompaktní formáty DCI (6-0A/0B, 6-1A/1B) ke snížení složitosti slepého dekódování
- Vysílán v datové oblasti podrámce, což umožňuje plánování ve frekvenční oblasti
- Konfigurovatelné prohledávací prostory a úrovně agregace pro adaptaci spojení
- Umožňuje úsporu energie díky sníženým příležitostem pro monitorování a efektivnímu plánování

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [EPDCCH – Enhanced Physical Downlink Control Channel](/mobilnisite/slovnik/epdcch/)

## Definující specifikace

- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [MPDCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpdcch/)
