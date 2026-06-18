---
slug: "sapi"
url: "/mobilnisite/slovnik/sapi/"
type: "slovnik"
title: "SAPI – Service Access Point Identifier"
date: 2025-01-01
abbr: "SAPI"
fullName: "Service Access Point Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sapi/"
summary: "Číselný identifikátor používaný ve vrstvách datového spoje (jako LAPDm v GSM) k rozlišení různých logických kanálů nebo služeb multiplexovaných přes jediné fyzické spojení. Identifikuje konkrétní enti"
---

SAPI je číselný identifikátor používaný na vrstvě datového spoje k rozlišení různých logických kanálů nebo služeb, který identifikuje konkrétní entitu protokolu vyšší vrstvy, pro kterou je rámec určen.

## Popis

Service Access Point Identifier (SAPI) je klíčové pole v hlavičce rámců vrstvy datového spoje, nejvýznamněji definované pro protokol LAPDm (Link Access Protocol on the Dm channel) používaný v GSM. Funguje na vrstvě 2 (Layer 2) protokolového zásobníku. Hodnota SAPI jednoznačně identifikuje logický přístupový bod služby (service access point) v rámci entity vrstvy datového spoje, čímž efektivně určuje, která entita nebo služba vyšší vrstvy je zdrojem nebo cílem přenášeného rámce. To umožňuje multiplexovat více logických komunikačních kanálů přes jeden fyzický rádiový prostředek (jako [SDCCH](/mobilnisite/slovnik/sdcch/) nebo [SACCH](/mobilnisite/slovnik/sacch/)).

Fungování SAPI je nedílnou součástí adresování a demultiplexování rámců. Když protokol vyšší vrstvy (např. řízení hovoru ([CC](/mobilnisite/slovnik/cc/)), správa mobility ([MM](/mobilnisite/slovnik/mm/)) nebo služba krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/))) potřebuje odeslat zprávu, předá svá datové vrstvě datového spoje prostřednictvím specifického [SAP](/mobilnisite/slovnik/sap/) spojeného s předdefinovanou hodnotou SAPI. Entita LAPDm poté sestaví rámec a umístí tuto hodnotu SAPI do adresního pole hlavičky rámce společně s identifikátorem koncového bodu terminálu ([TEI](/mobilnisite/slovnik/tei/)). Tento rámec je odeslán přes rozhraní vzduchu. Přijímající entita vrstvy datového spoje prozkoumá SAPI v hlavičce příchozího rámce. Na základě této hodnoty směruje extrahovaný užitečný obsah (zprávu vrstvy 3) k odpovídající entitě protokolu vyšší vrstvy. Například rámec s SAPI=0 je doručen protokolu řízení hovoru, zatímco rámec s SAPI=3 je doručen entitě zpracovávající SMS.

Klíčové komponenty zahrnují samotné pole SAPI (obvykle široké 3 nebo 6 bitů), přidružené spojení vrstvy datového spoje a mapovací tabulku v protokolovém zásobníku, která spojuje každou hodnotu SAPI s její odpovídající službou vyšší vrstvy. Jeho úlohou je poskytovat efektivní souběžnou podporu pro více toků řídicí signalizace a služeb uživatelských dat (jako alternativní řeč/data) bez nutnosti samostatných fyzických kanálů pro každý z nich. Tento multiplex je klíčový pro optimalizaci využití vzácných rádiových prostředků a správu složitosti signalizace mobilní stanice.

## K čemu slouží

SAPI byl vytvořen k řešení potřeby efektivního multiplexování více logických signalizačních a datových kanálů přes omezené fyzické kanály dostupné v systému GSM (a později [GPRS](/mobilnisite/slovnik/gprs/)). V raných mobilních systémech by vyčlenění fyzického kanálu pro každý typ řídicího signálu (zřizování hovoru, aktualizace mobility, SMS) bylo extrémně nehospodárné z hlediska spektra. Mechanismus SAPI umožňuje těmto různým tokům sdílet společné spojení vrstvy datového spoje.

Řeší problém demultiplexování na přijímací straně. Bez jasného identifikátoru v každém rámci by přijímací zásobník nevěděl, zda daná zpráva obsahuje příkaz k předání hovoru, odeslání SMS nebo uživatelská data. SAPI poskytuje tuto cílovou adresu na úrovni logického spoje. To umožňuje telefonu a síti současně spravovat hlasový hovor (SAPI=0), odesílat SMS (SAPI=3) a potenciálně zpracovávat paketová data (hodnoty SAPI pro GPRS) vše na stejném přiděleném časovém slotu.

Historicky bylo jeho zavedení v GSM (a formalizace v 3GPP Rel-4) motivováno požadavkem na podporu rostoucího souboru služeb nad rámec základní hlasové telefonie na jediné, jednotné signalizační infrastruktuře. Řešilo omezení jednodušších spojových protokolů tím, že poskytlo standardizované, flexibilní adresovací schéma schopné pojmout nové služby (jako GPRS) přiřazením nových hodnot SAPI, čímž budoucím způsobem zajistilo architekturu vrstvy datového spoje.

## Klíčové vlastnosti

- Jednoznačně identifikuje logickou službu nebo entitu protokolu vyšší vrstvy v rámci spojení vrstvy datového spoje.
- Používá se k multiplexování více logických kanálů (např. signalizace, SMS) přes jeden fyzický kanál.
- Jádrová součást adresního pole rámce v protokolu LAPDm (GSM) a příbuzných protokolech vrstvy datového spoje.
- Umožňuje vrstvě datového spoje správně směrovat příchozí rámce k příslušné službě vyšší vrstvy.
- Předdefinované hodnoty pro specifické služby (např. SAPI=0 pro řízení hovoru, SAPI=3 pro SMS).
- Nezbytný pro efektivní využití rádiových prostředků díky podpoře souběžných služeb.

## Související pojmy

- [Multiplexing](/mobilnisite/slovnik/multiplexing/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 24.065** (Rel-4) — GPRS Subnetwork Dependent Convergence Protocol
- **TS 34.109** (Rel-19) — UE Conformance Test Functions for UMTS
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.065** (Rel-19) — GPRS SNDCP Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TS 49.008** (Rel-19) — BSSAP on E-interface for inter-MSC handover
- **TS 52.021** (Rel-19) — GSM A-bis Interface Network Management

---

📖 **Anglický originál a plná specifikace:** [SAPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sapi/)
