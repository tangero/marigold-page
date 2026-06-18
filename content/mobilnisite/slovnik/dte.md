---
slug: "dte"
url: "/mobilnisite/slovnik/dte/"
type: "slovnik"
title: "DTE – Data Terminal Equipment"
date: 2025-01-01
abbr: "DTE"
fullName: "Data Terminal Equipment"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dte/"
summary: "Data Terminal Equipment (DTE) je obecný termín pro koncové uživatelské zařízení, které iniciuje nebo ukončuje datovou komunikaci, například počítač nebo router. V kontextech 3GPP často odkazuje na uži"
---

DTE je obecný termín 3GPP pro uživatelské zařízení nebo terminál, který iniciuje nebo ukončuje datovou komunikaci, čímž se odlišuje od síťového zařízení pro ukončení datového okruhu (Data Circuit-terminating Equipment, DCE).

## Popis

Data Terminal Equipment (DTE) je základní koncept v telekomunikacích a datových sítích, který byl převzat do specifikací 3GPP pro definici koncového bodu datového komunikačního okruhu. V kontextu systémů 3GPP, zejména ve specifikacích jako TS 21.905 (Slovníček) a TS 48.014 (rozhraní BSS-MSC), DTE typicky odkazuje na mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) nebo uživatelské zařízení (UE), když je modelováno v určitých zastaralých architekturách okruhově přepínaných datových služeb. Představuje zdroj nebo cíl digitálního datového toku. DTE neprovádí převod signálu ani taktování linky; to jsou funkce zařízení pro ukončení datového okruhu ([DCE](/mobilnisite/slovnik/dce/)), jako je modem nebo, v mobilní síti, funkce síťového adaptéru v rámci síťové infrastruktury.

Architektonicky, v raných datových službách GSM (jako jsou ty odkazované ve verzi Rel-4), by se DTE (mobilní telefon nebo datová karta) připojovalo přes funkci terminálového adaptéru k mobilní síti, která poskytovala funkci DCE pro rozhraní s veřejnou telefonní sítí ([PSTN](/mobilnisite/slovnik/pstn/)) nebo jinými sítěmi. Interakce mezi DTE a DCE se řídí standardizovanými rozhraními, nejznáměji doporučeními řady V a řady X od [ITU-T](/mobilnisite/slovnik/itu-t/), která definují fyzikální, elektrické a procedurální charakteristiky. V 3GPP se tyto koncepty používají k zajištění interoperability mezi uživatelským zařízením a síťovým zařízením pro ne-IP datové služby.

Jeho role v síti je primárně klasifikační a referenční. Pomáhá jednoznačně definovat odpovědnosti v protokolových zásobnících a popisech služeb. Například v kontextu specifikace rozhraní BSS-MSC (TS 48.014) je objasnění, která entita vystupuje jako DTE nebo DCE, klíčové pro správné zpracování datových hovorů a procedur přizpůsobení rychlosti. Ačkoli je tento termín méně výrazný v čistě IP architekturách pozdějších vydání, zůstává klíčovou součástí základního slovníku pro pochopení modelů datové komunikace v rámci i mimo systémy 3GPP.

## K čemu slouží

Účelem definice DTE v rámci standardů 3GPP je poskytnout jasný, standardizovaný referenční model pro koncové body datové komunikace, převzatý z širšího telekomunikačního průmyslu. To bylo zásadní v raných fázích mobilních dat (před 3G), kdy služby často zahrnovaly okruhově přepínaná spojení napodobující tradiční modemové linky přes rádiové rozhraní. Přijetím dobře zavedeného modelu DTE/[DCE](/mobilnisite/slovnik/dce/) mohlo 3GPP využít stávajících mezinárodních standardů ([ITU-T](/mobilnisite/slovnik/itu-t/)) pro interoperabilitu, což zajišťovalo, že mobilní stanice mohou být jednoznačně popsány jako koncová zařízení v koncových datových hovorech.

Historicky, před všudypřítomným IP, potřebovaly mobilní datové služby jako GSM Data a Fax komunikovat s [PSTN](/mobilnisite/slovnik/pstn/) a dalšími pevnými datovými sítěmi. Tyto sítě fungovaly na principu připojení DTE (jako je počítač) přes DCE (jako je modem) k síti. Mobilní síť sama musela převzít roli DCE nebo poskytnout funkci pro vzájemné propojení. Definice [MS](/mobilnisite/slovnik/ms/) jako DTE vytvořila konzistentní rámec pro specifikaci protokolů, přizpůsobení rychlosti a zpracování chyb napříč rozhraními Um (rádiové) a A. Tento model řešil omezení spočívající v absenci standardizovaného způsobu popisu role terminálu v datovém toku, což bylo kritické pro spolehlivou implementaci a testování služeb.

## Klíčové vlastnosti

- Definuje koncový bod, který iniciuje nebo ukončuje relaci datové komunikace.
- Používá se ve spojení se zařízením pro ukončení datového okruhu (DCE) k modelování kompletních datových cest.
- Odkazuje se na něj v 3GPP pro zastaralé architektury okruhově přepínaných datových služeb.
- Aplikuje standardizované procedury rozhraní (např. V.24, X.21) v rámci popisů systému.
- Poskytuje jasné funkční oddělení rolí mezi uživatelským zařízením a síťovým zařízením.
- Základní koncept pro interoperabilitu v raných datových a faxových službách GSM.

## Související pojmy

- [DCE – Data Circuit-terminating Equipment](/mobilnisite/slovnik/dce/)
- [MS – Mobile Station](/mobilnisite/slovnik/ms/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 48.014** (Rel-19) — Gb Interface Physical Layer Specification

---

📖 **Anglický originál a plná specifikace:** [DTE na 3GPP Explorer](https://3gpp-explorer.com/glossary/dte/)
