---
slug: "its-aid"
url: "/mobilnisite/slovnik/its-aid/"
type: "slovnik"
title: "ITS-AID – ITS Application Identifier"
date: 2025-01-01
abbr: "ITS-AID"
fullName: "ITS Application Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/its-aid/"
summary: "Jedinečný identifikátor pro aplikace inteligentních dopravních systémů (ITS), standardizovaný organizací 3GPP. Umožňuje síti a zařízením rozpoznávat a spravovat konkrétní služby V2X, čímž zajišťuje sp"
---

ITS-AID je jedinečný identifikátor standardizovaný organizací 3GPP pro aplikace inteligentních dopravních systémů (ITS), který umožňuje sítím a zařízením rozpoznávat a spravovat konkrétní služby V2X za účelem správného směrování, zabezpečení a kvality služeb (QoS).

## Popis

Identifikátor aplikace [ITS](/mobilnisite/slovnik/its/) (ITS-AID) je standardizovaný číselný identifikátor definovaný ve specifikacích 3GPP, který jednoznačně reprezentuje konkrétní aplikaci nebo službu inteligentních dopravních systémů (ITS). Funguje jako klíčová značka v rámci protokolového zásobníku pro komunikaci Vozidlo-se-vším (V2X), která umožňuje síťovým entitám a uživatelskému zařízení (UE) identifikovat typ přenášené nebo vyžadované služby. Tato identifikace je zásadní pro diferenciaci služeb, protože umožňuje uplatňovat odpovídající bezpečnostní politiky, řízení kvality služeb (QoS) a směrování zpráv na základě požadavků dané aplikace. Například bezpečnostně kritická aplikace, jako jsou zprávy decentralizovaného environmentálního oznamování ([DENM](/mobilnisite/slovnik/denm/)), bude mít odlišný ITS-AID než služba pro zvýšení dopravní efektivity, jako jsou kooperativní zprávy o povědomí ([CAM](/mobilnisite/slovnik/cam/)), což síti umožní upřednostnit první jmenovanou.

Z architektonického hlediska je ITS-AID vložen do jednotek protokolových dat V2X zpráv, typicky ve vrstvách nad přístupovou vrstvou, jako je vrstva služeb (facilities layer) nebo aplikační vrstva dle definice zásobníku [ETSI](/mobilnisite/slovnik/etsi/) ITS. Když UE generuje V2X zprávu, zahrne do ní ITS-AID odpovídající zdrojové aplikaci. Tento identifikátor je následně použit přijímajícím UE nebo síťovými funkcemi, jako je V2X řídicí funkce, ke správnému zpracování zprávy. Jádrová síť 3GPP, konkrétně funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) a jednotná správa dat ([UDM](/mobilnisite/slovnik/udm/)), může využívat politiky klíčované na ITS-AID k autorizaci používání V2X služeb UE a k vynucování specifických parametrů QoS pro přidružené datové toky přes referenční bod PC5 (sidelink) nebo Uu (buněčná síť).

Mezi klíčové komponenty, které s ITS-AID interagují, patří V2X aplikační vrstva v UE, V2X řídicí funkce v síti a entity pro správu politik. Samotný identifikátor je přidělován ze spravovaného číselného prostoru, který je často koordinován s dalšími standardizačními orgány, jako je ETSI, aby byla zajištěna globální jedinečnost a interoperabilita. Jeho role přesahuje pouhou identifikaci; je nedílnou součástí bezpečnostního rámce pro V2X. Specifikace jako TS 33.836 podrobně popisují, jak je ITS-AID použit při generování a ověřování bezpečnostních přihlašovacích údajů, propojují autorizaci aplikace s konkrétními identifikátory, aby se zabránilo podvržení a zajistilo, že pouze legitimní UE mohou vysílat zprávy pro bezpečnostně kritické aplikace. Tím vzniká důvěryhodný ekosystém, kde lze zprávy ověřovat z hlediska autenticity a integrity na základě jejich deklarovaného aplikačního účelu.

## K čemu slouží

ITS-AID byl vytvořen, aby řešil zásadní výzvu diferenciace a správy služeb v rozvíjející se oblasti buněčných komunikací V2X (C-V2X). Před jeho standardizací systémy V2X, často založené na [IEEE](/mobilnisite/slovnik/ieee/) 802.11p (DSRC), postrádaly jednotnou, síťově uvědomělou metodu pro identifikaci různých typů aplikací v rámci protokolového zásobníku. To ztěžovalo sítím 3GPP, které jsou ze své podstaty služebně a politicky uvědomělé, uplatňovat podrobnou kontrolu, zabezpečení a mechanismy QoS na datové toky V2X. Rozmach různorodých V2X aplikací – od varování před nouzovým brzděním a upozornění na kolize na křižovatkách po optimalizaci dopravního proudu a infotainment – vyžadoval standardizovaný identifikátor, který by mohl spouštět chování sítě specifické pro danou aplikaci.

Historicky IP služby používají pro klasifikaci čísla portů nebo hloubkovou kontrolu paketů (DPI), tyto metody jsou však pro citlivé na zpoždění a někdy ne-IP V2X zprávy neefektivní nebo nespolehlivé. ITS-AID poskytuje lehkou, explicitní značku, která je nezávislá na transportním protokolu. Jeho vytvoření bylo motivováno integrací V2X do architektury 3GPP počínaje Release 14, což vyžadovalo most mezi světem automobilových aplikací a správou buněčných sítí. Řeší problém, jak může síť rozpoznat, že konkrétní datový paket je vysoce prioritní bezpečnostní zpráva oproti méně prioritní informační značce, bez nutnosti složité a intruzivní kontroly, což umožňuje efektivní alokaci zdrojů a splnění přísných požadavků na spolehlivost a latenci v kooperativní jízdě.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro aplikace ITS
- Umožňuje síťové řízení politik a diferenciaci QoS pro V2X toky
- Nedílná součást bezpečnostního rámce V2X pro autorizaci aplikací
- Používá se pro směrování a zpracování zpráv v UE a síťových funkcích
- Nezávislý na protokolu, lze jej použít s IP i ne-IP V2X zprávami
- Standardizovaný číselný prostor koordinovaný mezi 3GPP a ETSI

## Definující specifikace

- **TS 22.186** (Rel-19) — Service requirements for enhanced V2X support
- **TS 23.285** (Rel-19) — V2X Architecture Enhancements for LTE
- **TS 23.287** (Rel-19) — 5G V2X Architecture Enhancements
- **TS 33.836** (Rel-16) — Security Study for Advanced V2X Services

---

📖 **Anglický originál a plná specifikace:** [ITS-AID na 3GPP Explorer](https://3gpp-explorer.com/glossary/its-aid/)
