---
slug: "cuc"
url: "/mobilnisite/slovnik/cuc/"
type: "slovnik"
title: "CUC – Centralized User Configuration"
date: 2025-01-01
abbr: "CUC"
fullName: "Centralized User Configuration"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cuc/"
summary: "Centralized User Configuration (CUC) je funkce správy sítě 5G, která umožňuje centralizované ukládání, správu a distribuci uživatelsky specifických konfiguračních dat napříč síťovými funkcemi. Poskytu"
---

CUC je funkce správy sítě 5G, která poskytuje centralizované ukládání a distribuci konfiguračních dat uživatelů jako jediný zdroj pravdy pro síťové funkce.

## Popis

Centralized User Configuration (CUC) je síťová funkce zavedená ve specifikaci 3GPP Release 17, která slouží jako centralizované úložiště a správní bod pro uživatelsky specifická konfigurační data v rámci jádra sítě 5G. Funguje jako logická funkce, která může být implementována jako součást Unified Data Repository ([UDR](/mobilnisite/slovnik/udr/)) nebo jako samostatná entita, a komunikuje s ostatními síťovými funkcemi prostřednictvím standardizovaných rozhraní založených na službách (service-based interfaces). CUC ukládá konfigurační parametry specifické pro jednotlivé účastníky nebo uživatelská zařízení (UE), jako jsou politiky specifické pro služby, preference výběru síťových řezů (network slices), profily kvality služeb (QoS) a nastavení správy mobility. Tento centralizovaný přístup odstraňuje potřebu, aby si každá síťová funkce udržovala vlastní oddělené úložiště konfigurací pro uživatele, což snižuje redundanci dat a složitost synchronizace.

Z architektonického hlediska se CUC integruje do architektury 5G založené na službách (Service-Based Architecture, [SBA](/mobilnisite/slovnik/sba/)) prostřednictvím rozhraní služeb Nucf, což umožňuje ostatním síťovým funkcím dotazovat se na a aktualizovat uživatelská konfigurační data. Typicky komunikuje s funkcí Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) pro konfigurace související s politikami, s funkcí Network Slice Selection Function ([NSSF](/mobilnisite/slovnik/nssf/)) pro preference řezů, s funkcí Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) pro nastavení mobility a s funkcí Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) pro parametry související se sezeními. CUC udržuje konfigurační data ve strukturovaném formátu, často uspořádaná podle identifikátoru účastníka ([SUPI](/mobilnisite/slovnik/supi/)) nebo jiných uživatelských identifikátorů, s podporou verzování a záznamů pro auditování změn konfigurace v čase.

Z provozní perspektivy CUC funguje tak, že přijímá konfigurační požadavky od konzumních síťových funkcí, zpracovává je na základě uložených politik a datových modelů a vrací příslušné konfigurační parametry. Podporuje jak dotazy založené na principu pull (kdy síťové funkce vyžádají specifické konfigurační prvky), tak notifikace založené na principu push (kdy CUC proaktivně informuje síťové funkce o změnách konfigurace). Funkce zahrnuje schopnosti pro řešení konfliktů, když existuje více zdrojů konfigurace, validaci konfiguračních parametrů vůči definovaným schématům a autorizační kontroly, které zajišťují, že pouze oprávněné síťové funkce mohou měnit specifické konfigurační prvky. Tento centralizovaný přístup ke správě umožňuje efektivnější síťové operace, zejména v prostředích s více dodavateli, kde je obtížné udržovat konzistenci napříč různými síťovými funkcemi.

CUC hraje klíčovou roli při umožňování pokročilých funkcí 5G, jako je síťové řezání (network slicing), tím, že poskytuje centralizovaný mechanismus pro ukládání a distribuci uživatelských konfigurací specifických pro řez. Když uživatel požaduje konkrétní síťový řez, různé síťové funkce se mohou dotázat CUC a získat uživatelovu specifickou konfiguraci pro tento řez, čímž je zajištěno konzistentní chování v celé síti. To je obzvláště důležité pro podnikové uživatele a specializované služby, které vyžadují specifické konfigurace odlišné od výchozího síťového chování. CUC také podporuje dynamické aktualizace konfigurace, což operátorům umožňuje měnit uživatelské konfigurace v reálném čase bez nutnosti ručních aktualizací více distribuovaných systémů.

## K čemu slouží

CUC bylo vytvořeno, aby řešilo rostoucí složitost správy uživatelských konfigurací v sítích 5G, zejména se zavedením síťového řezání (network slicing) a různorodých požadavků služeb. V předchozích nasazeních 4G a raných 5G byla uživatelská konfigurační data často rozptýlena napříč více síťovými funkcemi, což vedlo k nekonzistencím, problémům se synchronizací a provozní režii. Každá síťová funkce udržovala vlastní konfigurační úložiště, což ztěžovalo zajištění, aby všechny funkce měly stejný pohled na parametry uživatelské konfigurace. Tento distribuovaný přístup také komplikoval implementaci pokročilých funkcí, jako je síťové řezání, kde bylo třeba uživatelsky specifické konfigurace řezů konzistentně aplikovat napříč více síťovými elementy.

Omezení předchozích přístupů se stala zvláště zjevná s uvedením samostatných sítí 5G Standalone a rostoucím přijetím síťového řezání pro podnikové a vertikální aplikace. Bez centralizovaného systému správy konfigurace čelili operátoři významným výzvám při udržování konzistence konfigurace napříč různými síťovými funkcemi, zejména v prostředích s více dodavateli. Změny konfigurace vyžadovaly aktualizace více systémů, což zvyšovalo riziko chyb a výpadků služeb. Navíc absence jediného zdroje pravdy pro uživatelské konfigurace ztěžovala implementaci sofistikované servisní logiky, která závisela na koordinované konfiguraci napříč více síťovými doménami.

CUC tyto problémy řeší tím, že poskytuje centralizované úložiště pro všechna uživatelsky specifická konfigurační data a slouží jako jediný zdroj pravdy, na který se mohou všechny síťové funkce odkazovat. Tím odstraňuje nekonzistence v konfiguraci, snižuje provozní složitost a umožňuje efektivnější implementaci pokročilých funkcí 5G. Standardizací ukládání a distribuce uživatelských konfigurací CUC také usnadňuje interoperabilitu mezi implementacemi různých dodavatelů a podporuje agilnější nasazování služeb. Vytvoření CUC odráží širší trend v 5G směrem k centralizovaným funkcím správy a řízení, které jsou schopné škálovat pro podporu různorodých požadavků sítí nové generace.

## Klíčové vlastnosti

- Centralizované ukládání uživatelsky specifických konfiguračních parametrů
- Standardizované rozhraní založené na službách (Nucf) pro přístup síťových funkcí
- Podpora uživatelských konfigurací specifických pro síťový řez (network slice)
- Mechanismy pro řešení konfliktů při správě konfigurace
- Záznamy pro audit a verzování změn konfigurace
- Integrace s architekturou 5G založenou na službách (Service-Based Architecture)

## Související pojmy

- [UDR – Unified Data Repository](/mobilnisite/slovnik/udr/)
- [NSSF – Network Slice Selection Function](/mobilnisite/slovnik/nssf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.585** (Rel-19) — TSN Interworking Protocol for 5G System
- **TR 33.851** (Rel-17) — Security for Industrial IoT in 5G

---

📖 **Anglický originál a plná specifikace:** [CUC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cuc/)
