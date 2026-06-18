---
slug: "tii"
url: "/mobilnisite/slovnik/tii/"
type: "slovnik"
title: "TII – Time-Independent Invocation"
date: 2025-01-01
abbr: "TII"
fullName: "Time-Independent Invocation"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/tii/"
summary: "Time-Independent Invocation (TII) je koncept v rámci správy sítí 3GPP (konkrétně v referenčním bodu integrace, IRP), kde mohou být řídicí operace naplánovány k provedení v konkrétní budoucí čas nebo z"
---

TII je koncept správy sítě, kde jsou operace naplánovány pro budoucí provedení nebo spuštěny při splnění specifických podmínek, což umožňuje automatizované úlohy konfigurace a správy poruch řízené časem nebo událostmi.

## Popis

Time-Independent Invocation (TII) je sofistikovaný mechanismus definovaný v rámci architektury správy sítí 3GPP, zejména pro referenční bod integrace ([IRP](/mobilnisite/slovnik/irp/)) mezi správcem sítě ([NM](/mobilnisite/slovnik/nm/)) a správcem prvku ([EM](/mobilnisite/slovnik/em/)) či síťovým prvkem ([NE](/mobilnisite/slovnik/ne/)). Umožňuje řídicímu systému vydat příkaz nebo požadavek na operaci, jehož provedení je odloženo na určený budoucí čas nebo je podmíněno výskytem definovaného stavu sítě. Tím odděluje vydání řídicí instrukce od jejího skutečného provedení, což umožňuje pokročilou automatizaci, plánování údržbových oken a koordinované změny v síti.

Architektonicky TII funguje v kontextu řešení IRP založených na architektuře 3GPP Common Object Request Broker Architecture ([CORBA](/mobilnisite/slovnik/corba/)) nebo později na webových službách. Řídicí systém (např. [OSS](/mobilnisite/slovnik/oss/)) odešle požadavek na vyvolání, který obsahuje parametry specifické pro TII, jako je naplánovaný čas zahájení, čas expirace nebo podmínka spouštěcí události. Tento požadavek přijme agent (např. na EM nebo NE), který jej potvrdí a uloží jako čekající operaci. Plánovač TII v agentovi pak monitoruje systémové hodiny nebo přihlášené proudy událostí. Když nastane zadaný čas nebo je splněna spouštěcí podmínka (např. se vyčistí určitý alarm nebo poklesne zatížení pod práh), agent automaticky provede původně požadovanou operaci, jako je softwarová aktualizace, změna konfigurace nebo diagnostický test.

Klíčové komponenty zahrnují IRP rozhraní s podporou TII, plánovač uvnitř agenta a informační modelové objekty reprezentující naplánovaná vyvolání (často spravované jako objekty "Schedule"). Provedení operace je transakční; pokud nejsou podmínky splněny před expirací, může být požadavek zahozen nebo může vyvolat oznámení o selhání. TII podporuje plánování podle absolutního času (např. "proveď ve 2:00") i relativního času (např. "proveď 30 minut po přijetí"). Jeho role je klíčová pro implementaci automatizace bez zásahu (zero-touch), což operátorům umožňuje předpřipravit rozsáhlé změny sítě (např. při nasazování síťového segmentování 5G), které proběhnou současně během údržbového okna bez manuálního zásahu, čímž se snižují provozní chyby a umožňuje se rozsáhlá, synchronizovaná správa sítě.

## K čemu slouží

TII byl vytvořen, aby řešil významná omezení tradičních modelů správy sítě s okamžitým vyvoláním, které vyžadovaly zásah člověka v reálném čase nebo složité externí skriptování pro provedení časově citlivých nebo podmíněných operací. Před zavedením TII vyžadovalo naplánování konfigurační aktualizace pro celou síť na období nízkého provozu, aby operátoři ručně spouštěli úlohy ve stanovenou hodinu, což bylo náchylné k chybám, neškálovatelné a nemožné pro skutečně synchronizované akce napříč tisíci prvky. TII to řeší vestavěním plánování a podmíněné logiky přímo do standardizovaného řídicího rozhraní, což síti umožňuje autonomně provádět řídicí akce v přesně stanovených časech nebo v reakci na specifické stavy sítě.

Historický kontext zahrnuje rostoucí složitost sítí 3GPP od Release 8 s příchodem LTE, samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)) a později 5G. Tyto sítě vyžadovaly vyšší úrovně automatizace pro efektivitu a spolehlivost. TII poskytuje základní schopnost pro pokročilé funkce SON, jako je plánovaná optimalizace, automatizované hojení a koordinovaná konfigurace. Například změna parametrů buňky určená k optimalizaci přenosu hovoru může být naplánována na noční hodiny nebo může být obnovovací skript spuštěn automaticky při detekci hardwarové závady.

Navíc TII podporuje regulatorní a obchodní požadavky na údržbová okna a procesy řízení změn. Umožňuje operátorům plánovat a schvalovat změny předem, přičemž systém je provede přesně podle plánu, což zlepšuje soulad s předpisy a trasu auditů. Přechodem od reaktivních, ručních operací k proaktivní, plánované automatizaci TII snižuje provozní výdaje ([OPEX](/mobilnisite/slovnik/opex/)), minimalizuje narušení služeb a umožňuje škálovatelnou správu vyžadovanou pro husté, heterogenní sítě 5G a IoT. Je klíčovým enablerem pro řízení založené na záměru (intent-based) a automatizaci s uzavřenou smyčkou v moderních telekomunikačních sítích.

## Klíčové vlastnosti

- Umožňuje odložené provedení řídicích operací v určeném absolutním nebo relativním čase
- Podporuje podmíněné provedení na základě spouštěcích událostí nebo změn stavu sítě
- Integrováno do frameworku 3GPP IRP (CORBA/Web Services) pro standardizovaná severní rozhraní
- Umožňuje plánování s časem zahájení, časem expirace a opakovacími vzory
- Usnadňuje rozsáhlé, synchronizované změny sítě (např. hromadné aktualizace konfigurace)
- Poskytuje transakční zpracování s oznámeními o úspěchu/selhání pro naplánované úlohy

## Související pojmy

- [IRP – Integration Reference Point](/mobilnisite/slovnik/irp/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TS 32.373** (Rel-9) — IRP Security Services CORBA Solution
- **TS 32.376** (Rel-19) — Security services for IRP Solution Set

---

📖 **Anglický originál a plná specifikace:** [TII na 3GPP Explorer](https://3gpp-explorer.com/glossary/tii/)
