---
slug: "pruk"
url: "/mobilnisite/slovnik/pruk/"
type: "slovnik"
title: "PRUK – ProSe Relay User Key Identity"
date: 2025-01-01
abbr: "PRUK"
fullName: "ProSe Relay User Key Identity"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/pruk/"
summary: "Identifikátor bezpečnostního klíče používaný ve službách komunikace na krátkou vzdálenost (ProSe) pro reléovou komunikaci. Jednoznačně identifikuje bezpečnostní klíč používaný k ochraně komunikace mez"
---

PRUK je identifikátor bezpečnostního klíče používaný v ProSe reléové komunikaci k jednoznačné identifikaci klíče chránícího komunikaci mezi vzdáleným UE a ProSe UE-to-Network Reléem.

## Popis

[ProSe](/mobilnisite/slovnik/prose/) Relay User Key Identity (PRUK) je klíčový bezpečnostní identifikátor v architektuře služeb komunikace na krátkou vzdálenost (ProSe) podle 3GPP, konkrétně pro funkci UE-to-Network Relay. UE-to-Network Relay je UE, které zajišťuje připojení k síti pro jiná 'vzdálená' UE, jež jsou mimo dosah buněčného pokrytí, a to využitím komunikace zařízení-zařízení ([D2D](/mobilnisite/slovnik/d2d/)) přes sidelink (rozhraní PC5). PRUK je asociován s dlouhodobým bezpečnostním klíčem, ProSe Relay User Key (PRUK key), který je odvozen a bezpečně poskytnut autorizovaným UE.

PRUK slouží jako reference k tomuto klíči během bezpečnostních procedur. Když vzdálené UE objeví a vybere reléové UE, navážou spolu zabezpečené spojení přes rozhraní PC5. Tento bezpečnostní kontext je založen na klíčích odvozených z PRUK klíče. Identita PRUK samotná je používána v signalizačních zprávách k označení, který klíčový materiál má být použit pro autentizaci a šifrování. Jádro sítě, konkrétně ProSe Function, spravuje životní cyklus PRUK a PRUK klíčů, včetně jejich generování, distribuce autorizovaným UE (jak vzdáleným UE, tak potenciálním reléovým UE) a zrušení.

Architektonicky je PRUK součástí širší hierarchie klíčů definované pro ProSe. PRUK klíč může být odvozen z kořenového klíče sdíleného mezi UE a sítí. Použití PRUK umožňuje vzájemnou autentizaci mezi vzdáleným UE a sítí prostřednictvím relé. Zajišťuje, že pouze autorizovaná UE mohou fungovat jako relé nebo využívat reléové služby, čímž chrání proti neoprávněnému přístupu k síti a odposlechu na sidelinku. Bezpečnostní procedury zahrnující PRUK jsou detailně popsány v bezpečnostních specifikacích 3GPP, které definují jeho použití v protokolech autentizace a dohody klíčů pro spojení PC5.

## K čemu slouží

PRUK byl vytvořen k řešení bezpečnostních výzev vlastních reléové komunikaci UE-to-Network Relay pro [ProSe](/mobilnisite/slovnik/prose/), funkci zavedené pro rozšíření síťového pokrytí a podporu skupinové komunikace pro veřejnou bezpečnost a komerční účely. Bez relé je UE mimo síťové pokrytí izolováno. Reléové UE může rozšířit pokrytí, což však vytváří bezpečnostní zranitelnost: jak síť autentizuje vzdálené UE připojující se přes nedůvěryhodné, uživatelem ovládané relé? Jak je chráněna komunikace přes sidelink (PC5) mezi vzdáleným UE a reléem?

Předchozí modely [D2D](/mobilnisite/slovnik/d2d/) komunikace postrádaly tento specifický bezpečnostní kontext pro relé připojené k síti. Mechanismus PRUK poskytuje škálovatelný způsob poskytnutí přihlašovacích údajů specifických pro relé UE autorizovaným pro služby ProSe. Umožňuje síti zachovat kontrolu a vynucování pravidel i v případě, že komunikační cesta UE zahrnuje přeskok přes sidelink. Identita PRUK umožňuje zúčastněným stranám (vzdálenému UE, reléovému UE a síťovým funkcím) efektivně odkazovat na správný bezpečnostní klíčový materiál bez nutnosti přenášet samotný klíč v signalizaci. Tato architektura řeší omezení jednoduché peer-to-peer bezpečnosti integrací scénáře s relé do síťového rámce pro autentizaci a správu klíčů, což je nezbytné pro služby řízené operátorem, zejména pro komunikace v rámci veřejné bezpečnosti s požadavkem na mimořádnou důvěryhodnost, kde je zabezpečené a spolehlivé připojení prvořadé.

## Klíčové vlastnosti

- Jednoznačně identifikuje ProSe Relay User Key (PRUK key) pro dané UE
- Umožňuje zabezpečenou autentizaci mezi vzdáleným UE a sítí prostřednictvím relé
- Používá se v bezpečnostní signalizaci přes sidelinkové rozhraní PC5 pro scénáře s relé
- Spravován a poskytován síťovou funkcí ProSe Function
- Podporuje řízení autorizace pro funkci UE-to-Network Relay
- Integruje zabezpečení relé do celkové hierarchie klíčů ProSe

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TR 33.740** (Rel-18) — Security and Privacy Aspects of Proximity Based Services in 5G System Phase 2
- **TS 33.843** (Rel-15) — Security Study for ProSe UE-to-Network Relay

---

📖 **Anglický originál a plná specifikace:** [PRUK na 3GPP Explorer](https://3gpp-explorer.com/glossary/pruk/)
