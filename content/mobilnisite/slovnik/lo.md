---
slug: "lo"
url: "/mobilnisite/slovnik/lo/"
type: "slovnik"
title: "LO – Local Oscillator"
date: 2025-01-01
abbr: "LO"
fullName: "Local Oscillator"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lo/"
summary: "Kritický elektronický obvod, který generuje stabilní referenční frekvenci používanou pro frekvenční transpozici v rádiových vysílačích-přijímačích. Umožňuje převod základního pásma na rádiové kmitočty"
---

LO (místní oscilátor) je elektronický obvod, který generuje stabilní referenční frekvenci pro převod signálů na vyšší a nižší kmitočet v rádiovém vysílači-přijímači.

## Popis

Místní oscilátor (LO) je klíčová součást vysokofrekvenční (RF) předkoncové části jak uživatelského zařízení (UE), tak základnových stanic (gNB/[eNB](/mobilnisite/slovnik/enb/)). Generuje signál spojité vlny na přesné frekvenci, který se míchá s informačním signálem za účelem převodu kmitočtu. Pro vysílání je signál základního pásma obsahující modulovaná data smíchán se signálem LO, čímž je převeden na určenou kmitočtovou nosnou pro vyzáření anténou. Naopak pro příjem je vysokofrekvenční signál zachycený anténou smíchán se signálem LO, aby byl převeden na nižší mezifrekvenci ([IF](/mobilnisite/slovnik/if/)) nebo přímo na základní pásmo, kde může být digitalizován a zpracován modemem.

Výkon LO je prvořadý a je charakterizován parametry jako přesnost frekvence, fázový šum, parazitní emise a ladicí rozsah. Přesnost frekvence zajišťuje, že vysílaný signál zůstává v rámci přiděleného kanálového pásma a že přijímač je správně naladěn. Fázový šum, představující krátkodobé náhodné fluktuace fáze oscilátorového signálu, přímo ovlivňuje poměr signál-šum (SNR) a může způsobit interferenci mezi nosnými v systémech s ortogonálním frekvenčním multiplexem ([OFDM](/mobilnisite/slovnik/ofdm/)), jako jsou LTE a NR. Nízký fázový šum je proto nezbytný pro udržení modulačních schémat vysokého řádu (např. 256QAM, 1024QAM) a dosažení vysokých přenosových rychlostí.

Z architektonického hlediska lze LO realizovat různými technologiemi, včetně krystalových oscilátorů, oscilátorů řízených napětím (VCO) a smyček fázového závěsu (PLL), které jsou často integrovány do vysokofrekvenčních integrovaných obvodů (RFIC). V moderních mobilních systémech je frekvence LO dynamicky řízena základnovým procesorem na základě přiděleného kanálu. Jeho návrh musí také zohledňovat agregaci nosných, kde může být vyžadováno více LO nebo LO s širokým laděním pro současné zpracování více komponentních nosných napříč potenciálně odlišnými kmitočtovými pásmy. Integrita LO je tak kritická, že jeho charakteristiky jsou podrobně specifikovány v 3GPP specifikacích pro testy shody (např. TS 38.171, TS 36.171), aby byla zajištěna interoperabilita a výkon sítě.

## K čemu slouží

Místní oscilátor existuje k řešení základního problému frekvenční transpozice, která je nezbytná, protože zpracování signálů základního pásma funguje na nízkých kmitočtech zvládnutelných digitálními obvody, zatímco bezdrátový přenos vyžaduje převod těchto signálů na mnohem vyšší rádiové kmitočty přidělené pro mobilní komunikaci. Bez LO by byl přímý přenos signálů základního pásma nemožný kvůli omezením velikosti antény a regulačnímu přidělování spektra. LO poskytuje stabilní vysokofrekvenční referenci, která propojuje digitální a RF doménu.

Historicky, jak se mobilní systémy vyvíjely od analogových (1G) k digitálním (2G a dále) a migrovaly na vyšší kmitočty nosných (např. milimetrové vlny v 5G NR), požadavky na výkon LO zesílily. Starší systémy s užšími šířkami pásma a modulacemi nižšího řádu mohly tolerovat vyšší fázový šum. Moderní systémy vyžadují extrémně nízký fázový šum pro podporu širokých pásem a složitých modulací, což pohání pokrok v návrhu LO, včetně použití teplotně kompenzovaných a termostatovaných krystalových oscilátorů (TCXO, OCXO) a sofistikovaných syntezátorů s frakčním-N PLL. Účel LO přesahuje rámec základního převodu; je klíčovým prvkem umožňujícím spektrální účinnost, datovou propustnost a spolehlivé připojení.

## Klíčové vlastnosti

- Generuje stabilní, přesnou referenční frekvenci spojité vlny pro převod kmitočtu
- Umožňuje převod signálů základního pásma na RF pro vysílání a převod RF signálů na základní pásmo pro příjem
- Kritické výkonnostní parametry zahrnují nízký fázový šum, vysokou přesnost frekvence a nízké parazitní emise
- Podporuje široké ladicí rozsahy pro pokrytí více kmitočtových pásem a scénářů agregace nosných
- Často realizován pomocí syntezátorů se smyčkou fázového závěsu (PLL) integrovaných do čipů RF vysílače-přijímače
- Jeho výkon přímo omezuje dosažitelný řád modulace (např. 1024QAM) a poměr signál-šum systému

## Definující specifikace

- **TS 28.538** (Rel-19) — Edge Computing Management (ECM)
- **TS 36.755** (Rel-15) — US 600 MHz LTE Band 71 Technical Report
- **TS 36.790** (Rel-15) — LAA/eLAA for CBRS 3.5GHz Band in US
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.774** (Rel-19) — Rel-19 LP-WUS/WUR RF Requirements TR
- **TS 38.831** (Rel-16) — UE RF Requirements for FR2 Enhancements
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR
- **TR 38.892** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [LO na 3GPP Explorer](https://3gpp-explorer.com/glossary/lo/)
