---
slug: "sync"
url: "/mobilnisite/slovnik/sync/"
type: "slovnik"
title: "SYNC – Synchronization User Plane Protocol"
date: 2025-01-01
abbr: "SYNC"
fullName: "Synchronization User Plane Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sync/"
summary: "Protokol uživatelské roviny používaný na rozhraních UTRAN Iur a Iub pro přenos synchronizačních informací, jako je časování a zarovnání rámců, mezi síťovými uzly. Zajišťuje koordinované vysílání a pří"
---

SYNC je protokol uživatelské roviny používaný na rozhraních UTRAN Iur a Iub pro přenos synchronizačních informací, jako je časování a zarovnání rámců, mezi síťovými uzly za účelem zajištění koordinovaného vysílání a příjmu.

## Popis

Synchronization User Plane Protocol (SYNC) je protokol vrstvy 2 definovaný v architektuře 3GPP [UTRAN](/mobilnisite/slovnik/utran/), konkrétně pro rozhraní Iur (mezi [RNC](/mobilnisite/slovnik/rnc/)) a rozhraní Iub (mezi RNC a Node B). Funguje jako součást zásobníku protokolů uživatelské roviny, nachází se nad transportní síťovou vrstvou (např. využívající [ATM](/mobilnisite/slovnik/atm/) nebo IP transport) a pod řídicími funkcemi vyšších vrstev rádiové sítě. Jeho primární rolí je přenášet řídicí synchronizační informace nezbytné pro koordinaci rádiového vysílání mezi různými síťovými prvky. To zahrnuje přenos časových informací, jako je Connection Frame Number ([CFN](/mobilnisite/slovnik/cfn/)) a Frame Sequence Number ([FSN](/mobilnisite/slovnik/fsn/)), které se používají k synchronizaci časování datových rámců mezi řídicím RNC ([CRNC](/mobilnisite/slovnik/crnc/)) a obsluhujícím Node B, nebo mezi RNC během scénářů měkkého předání hovoru.

Z architektonického hlediska je SYNC jedním z několika protokolů uživatelské roviny definovaných pro rozhraní UTRAN, spolu s dalšími, jako je Frame Protocol ([FP](/mobilnisite/slovnik/fp/)) pro přenos uživatelských dat. Typicky je implementován v rámci uživatelské roviny rádiové síťové vrstvy. Protokol definuje specifické SYNC protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)), které obsahují pole pro synchronizační parametry. Tyto PDU jsou vyměňovány mezi partnerskými entitami – například mezi CRNC a Node B přes rozhraní Iub – za účelem navázání a udržování časové synchronizace. Protokol zajišťuje inicializaci synchronizace, průběžné aktualizace časování a správu stavu synchronizace, čímž zaručuje, že všechny zúčastněné uzly mají společnou představu o časování rámců, což je zásadní pro procesy jako je makro-diverzitní kombinování při měkkém předání hovoru.

Během provozu SYNC spolupracuje se signalizačními protokoly Radio Resource Control (RRC) a Node B Application Part (NBAP). Například během nastavování rádiového spoje přes NBAP jsou nakonfigurovány synchronizační parametry a SYNC je následně využit k přenosu průběžných informací o časové synchronizaci na zřízeném přenosovém kanálu uživatelské roviny. Protokol podporuje jak synchronní, tak asynchronní režimy vzhledem k časovému referenčnímu zdroji sítě. Jeho správná funkce je zásadní pro udržení kvality služeb, zejména u služeb citlivých na zpoždění, a pro umožnění plynulého přechodu při předávání hovoru. Bez správné synchronizace by se rádiové přenosy mohly kolidovat nebo dostat z časové synchronizace, což by vedlo ke zvýšenému rušení, přerušeným hovorům a snížení kapacity systému.

## K čemu slouží

SYNC byl vytvořen, aby řešil kritickou potřebu přesné časové koordinace v UTRAN, což je synchronní síť založená na CDMA. V takových systémech je přesná časová synchronizace mezi Node B a RNC nezbytná pro několik klíčových funkcí: úspěšné měkké předání hovoru (kdy UE komunikuje s více buňkami současně), efektivní řízení výkonu a správný příjem a kombinování signálů. Před standardizací 3GPP mohla existovat proprietární řešení, ale standardizovaný protokol byl nezbytný pro zajištění interoperability mezi více dodavateli na otevřených rozhraních Iub a Iur.

Protokol řeší problém distribuce společné časové reference mezi geograficky rozptýlené síťové prvky, které mohou mít různé interní zdroje hodin. Poskytuje standardizovaný mechanismus pro přenos časových informací (jako je CFN) přes transportní síť, která sama může zavádět proměnlivá zpoždění (např. přes ATM nebo IP). To umožňuje RNC řídit a upravovat časování vysílání na Node B, a zajistit tak, že datové rámce z různých buněk dorazí k UE ve velmi těsném časovém okně pro efektivní kombinování. Vytvoření SYNC bylo motivováno architektonickou změnou ve 3G UMTS, která oddělila rádiové řízení (RNC) od rádiového vysílání (Node B), a vyžadovala proto spolehlivý a nízkolatenční protokol pro časovou koordinaci přes tato standardizovaná rozhraní, aby byly zachovány výkonnostní výhody technologie WCDMA.

## Klíčové vlastnosti

- Přenáší řídicí synchronizační informace (např. CFN, FSN) pro časovou synchronizaci
- Funguje na rozhraních Iur a Iub v zásobníku protokolů uživatelské roviny
- Podporuje inicializaci, udržování a hlášení stavu synchronizace
- Spolupracuje se signalizací NBAP a RRC pro správu rádiových spojů
- Umožňuje procedury makro-diverzity a měkkého předání hovoru v UTRAN
- Definuje specifické SYNC PDU pro spolehlivou výměnu časových parametrů

## Definující specifikace

- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.446** (Rel-19) — MBMS Synchronisation Protocol (SYNC)

---

📖 **Anglický originál a plná specifikace:** [SYNC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sync/)
