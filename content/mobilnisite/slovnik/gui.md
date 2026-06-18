---
slug: "gui"
url: "/mobilnisite/slovnik/gui/"
type: "slovnik"
title: "GUI – Graphical User Interface"
date: 2026-01-01
abbr: "GUI"
fullName: "Graphical User Interface"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gui/"
summary: "Vizuální rozhraní pro operátory sítí, které slouží k monitorování, konfiguraci a správě síťových prvků a služeb. Nahrazuje příkazy v příkazovém řádku intuitivními nabídkami, ikonami a řídicími panely,"
---

GUI (grafické uživatelské rozhraní) je vizuální rozhraní pro operátory sítí, které slouží k monitorování, konfiguraci a správě síťových prvků a služeb; využívá intuitivní nabídky, ikony a řídicí panely ke zjednodušení složitých operací.

## Popis

Grafické uživatelské rozhraní (GUI) ve standardech 3GPP označuje vizuální systémy pro správu a provozní podporu používané správci a operátory sítí. Nejde o jedinou monolitickou aplikaci, ale o koncepční rámec implementovaný napříč různými nástroji pro provoz, správu a údržbu ([OAM](/mobilnisite/slovnik/oam/)) a systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)). Tato rozhraní poskytují člověku přizpůsobenou vrstvu nad podkladovými protokoly a datovými modely pro správu sítě definovanými v normách, jako jsou ty pro správu poruch, konfigurace, účtování, výkonu a zabezpečení (FCAPS). GUI překládá složité síťové parametry, alarmy, ukazatele výkonu a konfigurační úlohy do vizuálních prvků, jako jsou grafy, diagramy, topologické mapy, formulářové vstupy a klikací pracovní postupy. Tato abstrakce umožňuje personálu pracovat se sítí bez nutnosti hluboké znalosti konkrétních protokolů pro komunikaci mezi stroji, jako jsou [SNMP](/mobilnisite/slovnik/snmp/) nebo NETCONF, které ve skutečnosti příkazy provádějí a data načítají.

Z architektonického hlediska je GUI typicky klientská aplikace nebo webový portál, který komunikuje se správním serverem nebo přímo se síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)). Backend serveru komunikuje se spravovanými síťovými prvky prostřednictvím standardizovaných referenčních bodů a informačních modelů. Například normy jako TS 32.150 (Management and orchestration; Concept and requirements) a TS 32.827 (Telecommunication management; Integration Reference Point ([IRP](/mobilnisite/slovnik/irp/)) concepts and definitions) stanovují rámce, v jejichž rámci se GUI vyvíjejí, aby byla zajištěna konzistence a interoperabilita mezi systémy pro správu různých dodavatelů. GUI prezentuje informace uspořádané podle funkčních oblastí: správa poruch zobrazuje aktivní alarmy a jejich závažnost; správa konfigurace umožňuje ladění parametrů a aktualizace softwaru; správa výkonu zobrazuje klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)) v reálném čase a historické trendy; a správa zabezpečení poskytuje přehledy autentizačních záznamů a nastavení politik.

Její role v síti je klíčová pro provozní efektivitu a zajištění služeb. Poskytováním centralizovaného vizuálního kontrolního bodu umožňuje rychlou identifikaci a řešení poruch, zjednodušené zřizování nových služeb a efektivní plánování kapacity na základě vizualizovaných vzorců provozu. Pro sítě nové generace se GUI vyvíjejí tak, aby podporovaly správu založenou na záměru, kde jsou vysoké obchodní nebo servisní politiky („záměr“) zadávány prostřednictvím GUI a systém je automaticky převádí na nízkou úroveň síťových konfigurací. To zkracuje dobu uvedení nových služeb na trh a minimalizuje konfigurační chyby. Navíc ve virtualizovaných a cloud-nativních 5G sítích jsou GUI nezbytné pro správu životního cyklu virtualizovaných síťových funkcí ([VNF](/mobilnisite/slovnik/vnf/)) a cloud-nativních síťových funkcí ([CNF](/mobilnisite/slovnik/cnf/)), včetně vytváření instancí, škálování, obnovy a ukončování, a to vše prostřednictvím intuitivních řídicích panelů, které abstrahují složitost podkladové cloudové infrastruktury.

## K čemu slouží

Účelem standardizace aspektů grafického uživatelského rozhraní v rámci 3GPP je zlepšit použitelnost, efektivitu a konzistenci operací správy sítě v prostředích s více dodavateli. Před těmito úvahami se správa sítě prováděla převážně prostřednictvím rozhraní příkazového řádku (CLI) nebo proprietárních grafických nástrojů specifických pro dodavatele. CLI, ačkoli jsou výkonné pro odborníky, mají strmou křivku učení, jsou náchylné k syntaktickým chybám a neposkytují okamžitý přehled o stavu sítě. Proprietární GUI vytvářela závislost na dodavateli, zvyšovala náklady na školení pro operátory spravující heterogenní sítě a ztěžovala integrovanou, end-to-end správu služeb. Zařazení konceptů GUI do specifikací pro správu si klade za cíl definovat společné informační modely, reprezentace dat a funkční požadavky, které vedou dodavatele k vytváření správních rozhraní, jež jsou více interoperabilní a uživatelsky přívětivá.

Historicky, jak sítě rostly na složitosti od 2G přes 3G (R99) a dále, vzrostl objem spravovaných entit i kritičnost dostupnosti sítě. To vytvořilo naléhavou potřebu nástrojů, které by umožnily širšímu spektru provozního personálu, nejen hlubokým odborníkům na protokoly, efektivně provozovat síť. GUI tuto potřebu řeší vizualizací stavu sítě a převodem surových dat na praktické poznatky. Například namísto procházení řádků logu, aby našel vadnou kartu, může operátor vidět červenou ikonu na mapě sítě. Motivace je zásadně ekonomická a provozní: snížit střední dobu do opravy (MTTR), snížit provozní výdaje (OPEX) zjednodušením úloh a snížit riziko lidských chyb ovlivňujících služby během konfiguračních změn. V moderních 5G a budoucích sítích, s koncepty jako síťové segmenty a masivní IoT, je složitost správy o řády vyšší, což činí inteligentní, automatizovaná a vizuálně intuitivní GUI nejen pohodlím, ale nutností pro proveditelné provozování sítí.

## Klíčové vlastnosti

- Vizuální reprezentace topologie sítě a stavu prvků
- Řídicí panel pro monitorování klíčových ukazatelů výkonu (KPI) v reálném čase a historických trendů
- Konfigurační pracovní postupy založené na formulářích a průvodcích
- Správa alarmů s filtrováním, korelací a vizuálními indikátory závažnosti
- Řízení přístupu na základě rolí (RBAC) pro zabezpečené provozní přehledy
- Podpora správy založené na záměru a automatizace řízené politikami

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [IRP – Integration Reference Point](/mobilnisite/slovnik/irp/)

## Definující specifikace

- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework
- **TR 26.981** (Rel-19) — MBMS Provisioning & Content Ingestion Interface Study
- **TS 32.150** (Rel-19) — IRP Concept and Definitions
- **TS 32.827** (Rel-10) — UE Management over Itf-N for MDT/SON
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements

---

📖 **Anglický originál a plná specifikace:** [GUI na 3GPP Explorer](https://3gpp-explorer.com/glossary/gui/)
