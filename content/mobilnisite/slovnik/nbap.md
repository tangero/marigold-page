---
slug: "nbap"
url: "/mobilnisite/slovnik/nbap/"
type: "slovnik"
title: "NBAP – Node B Application Protocol"
date: 2025-01-01
abbr: "NBAP"
fullName: "Node B Application Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nbap/"
summary: "Signalizační protokol používaný v rádiové přístupové síti UMTS (UTRAN) pro komunikaci mezi řadičem rádiové sítě (RNC) a Node B. Spravuje řízení rádiových zdrojů, konfiguraci buněk a hlášení měření, co"
---

NBAP je signalizační protokol používaný v rádiové přístupové síti UMTS pro komunikaci mezi řadičem rádiové sítě (RNC) a Node B za účelem správy rádiových zdrojů, konfigurace buněk a měření.

## Popis

Node B Application Protocol (NBAP) je klíčový signalizační protokol v pozemní rádiové přístupové síti UMTS (UTRAN), který funguje přes rozhraní Iub mezi řadičem rádiové sítě (RNC) a Node B (základnová stanice). Dělí se na dvě logické části: Common NBAP (C-NBAP) a Dedicated NBAP (D-NBAP). C-NBAP zpracovává společné procedury týkající se celého Node B nebo buňky, jako je nastavení buňky, její zrušení a správa vysílaných informací. D-NBAP se zabývá vyhrazenými procedurami pro jednotlivá uživatelská zařízení (UE), včetně zřizování, rekonfigurace a rušení rádiových spojů. Zprávy NBAP jsou přenášeny přes [ATM](/mobilnisite/slovnik/atm/) nebo IP v závislosti na implementaci sítě, s využitím signalizačních přenašečů pro spolehlivé doručení.

NBAP funguje tak, že umožňuje RNC dynamicky řídit operace Node B. Například při sestavování hovoru RNC použije D-NBAP k vyžádání rádiového spoje s konkrétními parametry, jako je rozprostírací faktor a nastavení řízení výkonu. Node B odpoví potvrzením a poskytne hlášení měření o kvalitě uplinku, interferenci a poloze UE. Tato hlášení umožňují RNC rozhodovat o předávání spojení a optimalizovat přidělování zdrojů. Mezi klíčové komponenty patří typy zpráv pro správu rádiových spojů, rekonfiguraci fyzických kanálů a správu poruch, což zajišťuje přizpůsobení rozhraní vzduch provozním podmínkám a událostem mobility.

V síťové architektuře hraje NBAP ústřední roli v řízení rádiových zdrojů (RRM), podporuje funkce jako řízení přístupu, vyvažování zátěže a řízení zahlcení. Usnadňuje měkká předávání spojení koordinací více Node B pro jedno UE, čímž zlepšuje pokrytí a spolehlivost. Protokol také zajišťuje synchronizaci a časové sladění mezi Node B a RNC, což je klíčové pro systémy WCDMA založené na [CDMA](/mobilnisite/slovnik/cdma/). Napříč releasy byl NBAP rozšířen o podporu funkcí jako [HSDPA](/mobilnisite/slovnik/hsdpa/) a [HSUPA](/mobilnisite/slovnik/hsupa/), integruje nové procedury pro vysokorychlostní datové kanály při zachování zpětné kompatibility s dřívějšími nasazeními UMTS.

## K čemu slouží

NBAP byl vytvořen, aby poskytl standardizovaný signalizační mechanismus pro UTRAN, který řeší potřebu efektivního řízení a koordinace mezi RNC a Node B v sítích UMTS. Před UMTS používal GSM Base Station System Application Part ([BSSAP](/mobilnisite/slovnik/bssap/)) pro podobné funkce, ale zavedení technologie WCDMA vyžadovalo nový protokol pro zvládnutí operací specifických pro [CDMA](/mobilnisite/slovnik/cdma/), jako je měkké předávání spojení a dynamické přidělování zdrojů. NBAP řeší problém správy složitých rádiových zdrojů v prostředí s rozprostřeným spektrem, umožňuje provádět úpravy rádiových spojů v reálném čase na základě síťových podmínek.

Vývoj protokolu byl motivován přechodem z TDMA na CDMA ve 3G, který přinesl výzvy v řízení interference a koordinaci více buněk. NBAP umožňuje RNC centralizovat rozhodovací kontrolu a zároveň využívat Node B pro lokální měření, čímž distribuuje inteligenci napříč RAN. Toto oddělení zájmů zlepšuje škálovatelnost a výkon, protože RNC může efektivně spravovat více Node B. Také podporuje zavedení paketově orientovaných služeb usnadněním nastavení datových kanálů a vynucování QoS.

Historicky NBAP zaplnil mezeru ve 3GPP Release 99 a poskytl základ pro provoz UTRAN. Odstranil omezení dřívějších protokolů tím, že nabídl flexibilitu pro budoucí vylepšení, jako je podpora pokročilých anténních systémů a vyšších datových rychlostí. Jeho kontinuální vývoj napříč releasy zajišťuje, že sítě UMTS mohou integrovat nové technologie při zachování spolehlivých hlasových a datových služeb.

## Klíčové vlastnosti

- Spravuje zřizování, rekonfiguraci a rušení rádiových spojů prostřednictvím D-NBAP
- Zpracovává nastavení buňky, vysílané informace a společné zdroje prostřednictvím C-NBAP
- Podporuje hlášení měření pro interferenci, výkon a určování polohy UE
- Umožňuje koordinaci měkkého předávání spojení mezi více Node B
- Usnadňuje řízení rádiových zdrojů včetně řízení přístupu a zátěže
- Přenos přes ATM nebo IP se spolehlivými signalizačními přenašeči

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.432** (Rel-19) — Iub NBAP Signalling Transport Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [NBAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nbap/)
