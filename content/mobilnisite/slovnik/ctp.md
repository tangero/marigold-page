---
slug: "ctp"
url: "/mobilnisite/slovnik/ctp/"
type: "slovnik"
title: "CTP – Connection Termination Point"
date: 2025-01-01
abbr: "CTP"
fullName: "Connection Termination Point"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ctp/"
summary: "Connection Termination Point (CTP) je logický koncový bod v jádrové síti UMTS, který představuje ukončení transportního spojení používaného pro provozní a údržbový provoz (O&M). Je to základní koncept"
---

CTP je logický koncový bod v jádrové síti UMTS, který ukončuje transportní spojení používané pro provozní a údržbový provoz.

## Popis

Connection Termination Point (CTP) je logická entita definovaná ve specifikacích 3GPP pro transportní síťovou vrstvu (TNL) jádrové sítě UMTS. Slouží jako abstraktní reprezentace koncového bodu pro transportní spojení, konkrétně pro ta, která přenášejí provozní a údržbový provoz (O&M). Tento O&M provoz zahrnuje kritické správní informace, alarmy, měření výkonu a konfigurační data vyměňovaná mezi síťovými prvky ([NE](/mobilnisite/slovnik/ne/)) a provozním systémem (OS) nebo mezi samotnými síťovými prvky. CTP není fyzický port, ale logický koncept používaný v architektuře správy sítě pro modelování a řízení těchto komunikačních cest.

Architektonicky existuje CTP ve vrstvené struktuře modelu Telecommunications Management Network (TMN) aplikovaného organizací 3GPP. Je asociován se síťovým prvkem (NE) a tvoří část hierarchie Logical Termination Point ([LTP](/mobilnisite/slovnik/ltp/)). LTP představuje obecnější koncový bod a CTP je specifický typ LTP používaný pro transport s navázáním spojení. CTP je definován ve vztahu k podkladové transportní technologii, která v kontextu jeho primárních specifikací (řada 25 pro UTRAN) může být založena na [ATM](/mobilnisite/slovnik/atm/) nebo IP. Poskytuje správnímu systému prostředek pro monitorování stavu, konfiguraci parametrů a sběr dat o výkonu (jako je variace zpoždění buňky, ztráta paketů) pro konkrétní O&M transportní spojení.

Z funkční perspektivy CTP charakterizuje vlastnosti transportního spojení, které ukončuje. To zahrnuje atributy jako asociovaná transportní adresa, typ služby (např. pro signalizaci O&M), jeho administrativní a provozní stav (povoleno, zakázáno, testování) a všechny parametry kvality služby relevantní pro správní provoz. Správní aplikace používají tyto objekty CTP k navázání, udržování a uvolnění O&M spojení. CTP slouží jako kotvící bod pro správu poruch (např. generování alarmů ztráty spojení) a správu výkonu (např. měření dostupnosti a propustnosti spojení).

Jeho role v síti je klíčová pro automatizovanou a spolehlivou správu sítě. Abstrakcí koncového bodu transportního spojení do spravovaného objektu (CTP) umožňují standardy 3GPP interoperabilitu správních funkcí mezi více dodavateli. Systémy správy sítě mohou jednotně detekovat CTP, monitorovat jejich stav a provádět diagnostiku bez ohledu na podkladový transportní hardware. Tato abstrakce je klíčová pro přístup 'spravovaného objektu' modelu TMN, který umožňuje, aby byla řídicí rovina do určité míry nezávislá na technologii, a soustředila se na logickou konektivitu vyžadovanou pro O&M spíše než na specifika fyzické vrstvy.

## K čemu slouží

Connection Termination Point (CTP) byl zaveden, aby řešil potřebu standardizované, abstraktní správy transportních spojení vyhrazených pro provoz a údržbu v sítích 3GPP, konkrétně UMTS. Před takovými standardizovanými abstrakcemi byla správa transportních spojení často specifická pro dodavatele a těsně svázaná s fyzickými rozhraními, což činilo správu sítí s více dodavateli složitou a neefektivní. CTP poskytuje jednotný model pro reprezentaci těchto logických koncových bodů, který je nezbytný pro automatizaci úloh správy poruch, konfigurace a výkonu (FCAPS).

Primární problém, který řeší, je oddělení zájmů mezi řídicí rovinou a transportní technologií. Jak se sítě vyvíjely k využívání různých transportních protokolů (jako [ATM](/mobilnisite/slovnik/atm/) a později IP), bylo vyžadováno společné správní rozhraní. Koncept CTP, definovaný v rámci modelu TMN přijatého organizací 3GPP, umožňuje správním systémům komunikovat s konzistentním objektovým modelem reprezentujícím O&M spojení, bez ohledu na to, zda je podkladovou vrstvou ATM VCC nebo IP sokety. To umožňuje škálovatelnou a interoperabilní správu rostoucích a složitých transportních sítí, které podporují infrastrukturu mobilních sítí.

Historicky bylo jeho vytvoření motivováno přijetím principů TMN pro správu sítí organizací 3GPP. Specifikace jako 32.854 (Management of CTP and VCC Trail Termination Point) formalizují, jak jsou tyto objekty spravovány. CTP je základním prvkem pro implementaci správy '[GTP](/mobilnisite/slovnik/gtp/)' (Generic Transport Protocol) v UTRAN podle 25.412 a 25.420. Řeší omezení spočívající v uzamčení správní inteligence do proprietárních systémů správy prvků a napomáhá tak vizi jednotného, standardy založeného Operations Support System ([OSS](/mobilnisite/slovnik/oss/)), který může spravovat sítě skládající se ze zařízení od více dodavatelů.

## Klíčové vlastnosti

- Logická reprezentace koncového bodu transportního spojení pro O&M provoz
- Definován jako spravovaný objekt v architektuře správy TMN/3GPP
- Asociován s nadřazeným síťovým prvkem (NE) a Logical Termination Point (LTP)
- Nese atributy pro administrativní stav, provozní stav a metriky výkonu
- Umožňuje technologicky nezávislou správu transportu (např. ATM, IP)
- Slouží jako kotvící bod pro správu poruch (alarmy) a správu výkonu (měření) na O&M spojích

## Definující specifikace

- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 32.854** (Rel-11) — FMC Federated Network Information Model

---

📖 **Anglický originál a plná specifikace:** [CTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctp/)
