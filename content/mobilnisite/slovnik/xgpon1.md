---
slug: "xgpon1"
url: "/mobilnisite/slovnik/xgpon1/"
type: "slovnik"
title: "XGPON1 – 10-Gigabit-capable Passive Optical Network (type 1)"
date: 2025-01-01
abbr: "XGPON1"
fullName: "10-Gigabit-capable Passive Optical Network (type 1)"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/xgpon1/"
summary: "XGPON1 je optická přístupová síťová technologie specifikovaná 3GPP pro drátovou část konvergence pevných a mobilních sítí. Poskytuje sdílenou infrastrukturu na bázi vlákna s rychlostmi směrem k uživat"
---

XGPON1 je optická přístupová technologie specifikovaná 3GPP pro konvergenci pevných a mobilních sítí (Fixed-Mobile Convergence). Poskytuje sdílenou infrastrukturu na bázi vlákna s rychlostmi směrem k uživateli (downstream) až 10 Gbps a směrem k síti (upstream) až 2,5 Gbps, a to jak pro mobilní přenosovou síť (backhaul), tak pro rezidenční širokopásmový přístup.

## Popis

XGPON1, standardizovaný [ITU-T](/mobilnisite/slovnik/itu-t/) jako řada G.987 a referencovaný v 3GPP, je technologie pasivní optické sítě s časovým multiplexem (TDM-PON). V kontextu 3GPP je specifikován jako důvěryhodný typ přístupové sítě mimo 3GPP (non-3GPP access), který se může propojit s jádrem 3GPP, zejména pro konvergenci pevných a mobilních sítí ([FMC](/mobilnisite/slovnik/fmc/)) a jako přenosová možnost pro síťové uzly. Systém se skládá z optické linkové terminace (OLT) v centrále poskytovatele služeb a z více optických síťových jednotek (ONU) nebo optických síťových terminálů (ONT) u zákazníka nebo na místě buňky. Ty jsou propojeny přes pasivní optický rozdělovač, který umožňuje, aby jediné vlákno z OLT obsloužilo více koncových bodů, což z něj činí nákladově efektivní sdílené médium.

Technologie pracuje s použitím různých vlnových délek pro provoz směrem k uživateli a směrem k síti, aby se zabránilo interferenci. Provoz směrem k uživateli (z OLT k ONU) je vysílán všesměrově na vlnové délce blízké 1577 nm, přičemž každá ONU selektivně čte data určená pro ni na základě šifrované adresace. Provoz směrem k síti (z ONU k OLT) využívá mnohonásobný přístup s časovým dělením ([TDMA](/mobilnisite/slovnik/tdma/)) na vlnové délce blízké 1270 nm, kde OLT přiděluje každé ONU specifické časové sloty pro vysílání jejích dat, čímž se předchází kolizím. Fyzická vrstva používá NRZ řádkové kódování. XGPON1 podporuje logický dosah až 60 km a dělicí poměr až 1:256, což umožňuje široké pokrytí z jediného portu OLT.

V rámci architektury 3GPP je XGPON1 integrován jako spolehlivý, vysokokapacitní drátový přístup. Pro konvergenci pevných a mobilních sítí může rezidenční brána ([RG](/mobilnisite/slovnik/rg/)) obsahující XGPON1 ONT připojit jak k 3GPP EPC/5GC pro mobilní služby, tak k IMS pro pevnou telefonii a [IPTV](/mobilnisite/slovnik/iptv/). Jako přenosová technologie může poskytovat přenosovou konektivitu (backhaul) pro 4G eNodeB a 5G gNB, spojuje je s jádrovou sítí s vysokou kapacitou a nízkou latencí a tvoří část transportní vrstvy mobilní sítě.

## K čemu slouží

XGPON1 byl vyvinut, aby uspokojil explozivní poptávku po vyšší přenosové kapacitě jak od rezidenčních širokopásmových uživatelů, tak od mobilních sítí. Jeho předchůdce, [GPON](/mobilnisite/slovnik/gpon/) (G.984), nabízel 2,5 Gbps směrem k uživateli a 1,25 Gbps směrem k síti, což se stávalo úzkým hrdlem pro vysoko-definiční video, cloudové služby a rostoucí kapacitní potřeby mobilní přenosové sítě (backhaul) s nasazováním sítí LTE. Primární motivací bylo zajistit budoucí připravenost vláknových přístupových sítí poskytnutím desetinásobného zvýšení kapacity směrem k uživateli.

Zařazení XGPON1 do specifikací 3GPP, počínaje Release 10, bylo motivováno strategickou iniciativou konvergence pevných a mobilních sítí ([FMC](/mobilnisite/slovnik/fmc/)). Cílem bylo standardizovat, jak mohou být vysoce výkonné drátové přístupové sítě, jako jsou [PON](/mobilnisite/slovnik/pon/), bezproblémově integrovány s 3GPP mobilním jádrem. To umožňuje operátorům s pevnými i mobilními aktivy nabízet jednotné služby, sdílet náklady na infrastrukturu a používat optickou síť jako kvalitní transportní vrstvu pro mobilní provoz. XGPON1 vyřešil problém poskytnutí standardizovaného, nákladově efektivního a vysokokapacitního řešení pro 'poslední míli' a 'přenosovou míli', které by mohlo podporovat náročné požadavky budoucích mobilních sítí, včetně nízké latence a vysoké dostupnosti pro funkce jako agregace nosných (carrier aggregation) a cloud RAN.

## Klíčové vlastnosti

- Asymetrická přenosová kapacita: přenosová rychlost 10 Gbps směrem k uživateli / 2,5 Gbps směrem k síti
- Provoz na oddělených vlnových délkách (1577 nm směrem k uživateli / 1270 nm směrem k síti) pro plně duplexní komunikaci
- Podporuje vysoké dělicí poměry (až 1:256) a dlouhý logický dosah (až 60 km)
- Využívá TDMA pro přenos směrem k síti ke správě přístupu ke sdílenému médiu
- Silné šifrování (AES-128) pro zabezpečení všesměrového vysílání směrem k uživateli
- Definován jako důvěryhodný typ přístupu mimo 3GPP (trusted non-3GPP access) pro integraci s 3GPP jádrovými sítěmi

## Související pojmy

- [GPON – Gigabit-capable Passive Optical Network](/mobilnisite/slovnik/gpon/)

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP

---

📖 **Anglický originál a plná specifikace:** [XGPON1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/xgpon1/)
