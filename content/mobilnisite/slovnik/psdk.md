---
slug: "psdk"
url: "/mobilnisite/slovnik/psdk/"
type: "slovnik"
title: "PSDK – Public Safety Discovery Key"
date: 2025-01-01
abbr: "PSDK"
fullName: "Public Safety Discovery Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/psdk/"
summary: "Bezpečnostní klíč používaný ve službách komunikace na krátkou vzdálenost (3GPP ProSe) pro aplikace veřejné bezpečnosti. Zabezpečuje proces zjišťování mezi koncovými zařízeními, čímž zajišťuje, že se v"
---

PSDK je bezpečnostní klíč používaný ve službách komunikace na krátkou vzdálenost (Proximity Services) k zabezpečení procesu zjišťování (discovery), který zajišťuje, že se v situacích mimo síť mohou vzájemně zjišťovat pouze oprávněná koncová zařízení (UE) určená pro veřejnou bezpečnost.

## Popis

Public Safety Discovery Key (PSDK) je kryptografický klíč definovaný v rámci bezpečnostní architektury 3GPP pro služby komunikace na krátkou vzdálenost ([ProSe](/mobilnisite/slovnik/prose/)), speciálně přizpůsobený pro případy užití veřejné bezpečnosti. Je klíčovým prvkem bezpečnostního rámce ProSe Direct Discovery, který zajišťuje, že zprávy pro zjišťování jsou autentizované a chráněné z hlediska integrity, čímž brání neoprávněným zařízením v zjišťování nebo vydávání se za personál veřejné bezpečnosti. PSDK je odvozen a spravován v bezpečném prostředí univerzálního integrovaného obvodu (UICC) nebo vestavěné [SIM](/mobilnisite/slovnik/sim/) (eSIM).

Hlavní funkcí PSDK je zabezpečit kód ProSe Restricted Code používaný při omezeném zjišťování (restricted discovery) pro veřejnou bezpečnost. Při omezeném zjišťování musí zjišťující UE prokázat, že je oprávněno zjistit konkrétní cílové UE nebo skupinu. PSDK se používá k vytvoření a ověření kódu pro ověření zprávy ([MAC](/mobilnisite/slovnik/mac/)) pro zprávy zjišťování. Proces zahrnuje funkci ProSe v síti, která zajišťuje oprávněným UE veřejné bezpečnosti potřebný klíčový materiál a zásady. Samotný PSDK není přenášen vzduchem; místo toho se v signalizaci zjišťování používají odvozené klíče nebo tokeny vytvořené pomocí PSDK.

Z architektonického hlediska je PSDK součástí hierarchie klíčů. Může být odvozen z kořenového klíče sdíleného s funkcí ProSe. ProSe protokol v UE používá tento klíč, k němuž bezpečně přistupuje z UICC prostřednictvím aplikace [USIM](/mobilnisite/slovnik/usim/), k provádění kryptografických operací. Bezpečnostní postupy zajišťují, že i když jsou zprávy zjišťování vysílány otevřeně, pouze UE disponující odpovídajícím PSDK (nebo odvozeným klíčem) je mohou správně zpracovat a identifikovat oprávněného protějšek. Tento mechanismus je zásadní pro operace v prostředích bez infrastruktury, kde není dostupné tradiční síťové ověřování.

## K čemu slouží

PSDK byl zaveden, aby řešil kritické bezpečnostní požadavky pro služby [ProSe](/mobilnisite/slovnik/prose/) veřejné bezpečnosti, zejména pro přímé zjišťování a komunikaci, když není dostupná, je narušena nebo přetížena infrastruktura mobilní sítě. Předchozí bezpečnostní mechanismy byly zcela síťově orientované a spoléhaly na nepřetržitou interakci s entitami jádra sítě pro ověřování a dohodu klíčů. Tento přístup selhává právě ve scénářích, se kterými se operace veřejné bezpečnosti často setkávají: katastrofy, odlehlé oblasti nebo výpadky sítě.

Motivace vycházela z potřeby zabezpečeného přímého zjišťování mezi zařízeními (device-to-device) pro záchranáře. Bez PSDK by mohly být zprávy zjišťování zachyceny nebo falšovány, což by umožnilo škodlivým aktérům lokalizovat záchranný personál nebo se za něj vydávat, což by vedlo k selhání operace nebo nebezpečí. PSDK umožňuje bezpečnostní model, který funguje nezávisle na okamžité dostupnosti sítě. Umožňuje předem zřízené bezpečnostní vztahy a zásady, čímž zajišťuje, že zjišťování je omezeno pouze na oprávněné strany, zachovává důvěrnost přítomnosti týmu veřejné bezpečnosti a integritu procesu zjišťování, což je základ pro navázání následných zabezpečených komunikačních kanálů typu sidelink.

## Klíčové vlastnosti

- Ukládán a zpracováván v bezpečném prostředí UICC/eSIM
- Používán speciálně pro autentizaci a ochranu integrity zpráv pro omezené zjišťování (ProSe Restricted Discovery) veřejné bezpečnosti
- Umožňuje zabezpečení pro provozní scénáře jak v pokrytí sítí, tak mimo něj (plné)
- Součást hierarchie klíčů spravované síťovou funkcí ProSe Function
- Generuje nebo ověřuje kódy pro ověření zprávy (MAC) pro signalizaci zjišťování
- Zajišťuje, že zjišťování je omezeno pouze na oprávněná koncová zařízení (UE) veřejné bezpečnosti

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS

---

📖 **Anglický originál a plná specifikace:** [PSDK na 3GPP Explorer](https://3gpp-explorer.com/glossary/psdk/)
