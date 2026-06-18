---
slug: "sabp"
url: "/mobilnisite/slovnik/sabp/"
type: "slovnik"
title: "SABP – Service Area Broadcast Protocol"
date: 2025-01-01
abbr: "SABP"
fullName: "Service Area Broadcast Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sabp/"
summary: "SABP je protokol 3GPP používaný pro vysílání zpráv, jako je služba Cell Broadcast Service (CBS), v konkrétní servisní oblasti v sítích UMTS. Umožňuje efektivní doručování informací typu jeden-všem, na"
---

SABP je protokol 3GPP používaný pro vysílání zpráv, jako jsou například výstrahy pro případ nouze, v konkrétní servisní oblasti v sítích UMTS za účelem efektivního doručování informací více uživatelským zařízením současně.

## Popis

Service Area Broadcast Protocol (SABP) je klíčový protokol řídicí roviny definovaný v architektuře 3GPP UMTS, určený speciálně pro správu vysílacích služeb. Funguje mezi Cell Broadcast Centre ([CBC](/mobilnisite/slovnik/cbc/)) a UMTS Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), konkrétně Radio Network Controllerem ([RNC](/mobilnisite/slovnik/rnc/)). SABP je primární rozhraní (Iu-BC) pro doručování vysílacích služeb, které umožňuje CBC instruovat RNC k vysílání zpráv v definované geografické oblasti, známé jako Servisní oblast. Protokol zajišťuje navázání, změnu a ukončení vysílacích relací včetně přenosu vlastního obsahu vysílané zprávy a přidružených parametrů, jako jsou identifikátory zpráv, rychlost opakování a definice vysílací oblasti.

Architektonicky se SABP nachází v doméně Core Network pro řízení, ale přímo komunikuje s RAN pro provedení. CBC funguje jako zdroj a správce vysílacích zpráv a pomocí SABP komunikuje s jedním nebo více RNC. RNC je zodpovědný za mapování logické Servisní oblasti na fyzické buňky a za plánování vysílání na kanálu UMTS Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)) nebo Forward Access Channel ([FACH](/mobilnisite/slovnik/fach/)). Zprávy SABP jsou přenášeny přes spojení Signalling Connection Control Part ([SCCP](/mobilnisite/slovnik/sccp/)), což zajišťuje spolehlivé doručení řídicích příkazů. Protokol podporuje funkce jako Write-Replace, která umožňuje aktualizovat nebo zrušit probíhající vysílání, a Load Balancing pro správu provozu mezi různými RNC.

Provoz SABP je pro řízení spojově orientovaný, ale výsledné vysílání na uživatelské rovině je bez spojení. Typický tok zahrnuje odeslání WRITE-REPLACE požadavku z CBC do RNC, který obsahuje obsah zprávy, identifikátor zprávy, seznam cílových Servisních oblastí (definovaných sadou Location Areas nebo Routing Areas) a informace o plánování vysílání. RNC to potvrdí a začne vysílat zprávu v určených buňkách. SABP také zahrnuje mechanismy pro zpracování chyb a hlášení stavu, což CBC umožňuje sledovat úspěšnost nebo neúspěch pokusů o vysílání. Jeho návrh zajišťuje efektivní využití vysílacích zdrojů v RAN a to, že kritické informace, zejména pro systémy varování veřejnosti, mohou být v síti šířeny rychle a spolehlivě.

## K čemu slouží

SABP byl vytvořen za účelem standardizace a umožnění efektivních služeb vysílání do buněk v sítích 3G UMTS, což řeší potřebu spolehlivého mechanismu distribuce informací typu jeden-všem. Před 3G měl GSM službu Cell Broadcast Service, ale architektura UMTS vyžadovala nový, optimalizovaný protokol pro rozhraní mezi vyvinutým Core Network a [UTRAN](/mobilnisite/slovnik/utran/). Primární problém, který SABP řeší, je řízené doručování vysílacích zpráv (jako jsou výstrahy pro případ nouze, dopravní informace nebo reklama) všem uživatelským zařízením (UE) v konkrétní geografické oblasti bez nutnosti navazovat individuální spojení, čímž se šetří signalizační zdroje sítě a umožňuje okamžité, rozsáhlé oznámení.

Historicky vycházela motivace z regulatorních požadavků na systémy varování veřejnosti (např. EU-Alert, [CMAS](/mobilnisite/slovnik/cmas/)) a komerční poptávky po službách vysílání založených na poloze. SABP poskytl standardizovanou, síťově řízenou metodu pro CBC ke správě vysílání, což zajišťuje interoperabilitu mezi zařízeními od různých výrobců. Řešil omezení zpráv typu bod-bod pro hromadná oznámení, která by způsobila zahlcení signalizace. Definováním vyhrazeného protokolu pro správu vysílacích služeb zajistil 3GPP, že sítě UMTS mohou podporovat kritické bezpečnostní služby a inovativní vysílací aplikace se zaručeným výkonem a spolehlivostí.

## Klíčové vlastnosti

- Spravuje navázání, změnu a ukončení vysílacích relací mezi CBC a RNC
- Podporuje operace Write-Replace pro aktualizaci nebo zrušení probíhajících vysílacích zpráv
- Definuje Servisní oblasti pro geografické cílení pomocí seznamů Location Area nebo Routing Area
- Obsahuje mechanismy vyrovnávání zatížení pro distribuci vysílacího provozu mezi RNC
- Poskytuje indikaci chyb a hlášení selhání pro vysílací operace
- Umožňuje efektivní, bezspojové doručování vysílání přes rozhraní Iu-BC

## Související pojmy

- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.419** (Rel-19) — Service Area Broadcast Protocol (SABP)
- **TS 25.703** (Rel-12) — HNB Emergency Warning Area Study for UTRA

---

📖 **Anglický originál a plná specifikace:** [SABP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sabp/)
