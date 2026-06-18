---
slug: "trs"
url: "/mobilnisite/slovnik/trs/"
type: "slovnik"
title: "TRS – Total Radiated Sensitivity"
date: 2026-01-01
abbr: "TRS"
fullName: "Total Radiated Sensitivity"
category: "Physical Layer"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/trs/"
summary: "Klíčový výkonnostní parametr pro bezdrátová zařízení, měřící celkovou citlivost přijímače s přihlédnutím ke kombinovanému účinku antény a přijímacího RF řetězce. Kvantifikuje nejslabší signál, který m"
---

TRS je klíčový výkonnostní parametr, který měří celkovou citlivost přijímače bezdrátového zařízení s přihlédnutím ke kombinovanému účinku jeho antény a přijímacího RF řetězce.

## Popis

Total Radiated Sensitivity (TRS), označovaná také jako Total Integrated Sensitivity, je komplexní metrika výkonu Over-The-Air ([OTA](/mobilnisite/slovnik/ota/)) definovaná ve specifikacích 3GPP pro hodnocení přijímacího výkonu uživatelského zařízení (UE) a v některých kontextech i základnových stanic. Na rozdíl od tradičních měření vedené citlivosti, která testují [RF](/mobilnisite/slovnik/rf/) přijímací port izolovaně, TRS měří citlivost celého zařízení jako systému včetně účinků antén, účinnosti antény, vyzařovacího diagramu a samotného přijímacího obvodu. Měření se provádí v bezodrazové komoře pomocí kalibrovaného testovacího systému, který osvětluje testované zařízení známým, řízeným RF signálem z různých úhlů příchodu.

Postup měření zahrnuje umístění UE na pozicionační systém, který jej otáčí ve sférických souřadnicích (azimut a elevace). V každé orientaci testovací systém vysílá referenční měřicí kanál (např. Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)) pro citlivost na downlink) na konkrétní úrovni výkonu. Přijímač UE se pokouší tento signál dekódovat a měří se Bit Error Rate ([BER](/mobilnisite/slovnik/ber/)) nebo Block Error Rate ([BLER](/mobilnisite/slovnik/bler/)). TRS je definována jako minimální úroveň výkonu dopadajícího signálu, integrovaná přes celou sféru, při které UE splňuje předdefinované výkonnostní kritérium (např. maximální povolenou BLER, typicky 1 % pro datové kanály). Obvykle se vyjadřuje v dBm. Výsledkem je jediná hodnota, která zachycuje schopnost zařízení přijímat slabé signály z libovolného směru, což odpovídá reálnému provozu zařízení v prostředí s vícecestným šířením a měnící se orientací.

Matematicky je TRS odvozena ze sférické integrace citlivosti změřené v každém bodě na vyzařovací sféře. Z podstaty zohledňuje nedokonalosti vyzařovacího diagramu a ztráty antény. Zařízení s vynikající vedenou citlivostí, ale s nevýkonnou, neefektivní anténou bude mít horší TRS. To činí z TRS mnohem realističtější ukazatel reálného výkonu, zejména u ručních zařízení, jejichž orientace vůči základnové stanici je nepředvídatelná. Specifikace 3GPP definují podrobné testovací sestavy, kalibrační metody a výkonnostní požadavky na TRS napříč různými kmitočtovými pásmy a technologiemi (LTE, NR). Jedná se o povinný konformační test pro certifikaci UE, který zajišťuje základní úroveň přijímacího výkonu pro všechna komerčně nasazovaná zařízení.

## K čemu slouží

TRS byla zavedena, aby odstranila významnou mezeru v hodnocení výkonu zařízení: nesoulad mezi ideálními laboratorními vedenými měřeními a reálnou uživatelskou zkušeností. Testy vedené citlivosti, které připojují kabel přímo k [RF](/mobilnisite/slovnik/rf/) portu zařízení, obcházejí anténu. Tato metoda nezohledňuje kompromisy v návrhu antény, integrační výzvy a vliv pouzdra zařízení a uživatelovy ruky (handgrip efekt) na příjem. Zařízení by mohlo projít vedenými testy, ale v reálném použití by mohlo mít špatný výkon kvůli suboptimální anténě.

Vytvoření TRS jako standardizované metriky [OTA](/mobilnisite/slovnik/ota/) bylo motivováno potřebou garantovat minimální reálný přijímací výkon pro koncové uživatele, což zajišťuje spolehlivé síťové připojení a konzistentní kvalitu služeb. Stala se stále kritičtější s rozšířením zařízení s kompaktním provedením (smartphony, IoT moduly, wearables), kde je návrh antény výrazně omezen velikostí, průmyslovým designem a přítomností více rádií (2G/3G/4G/5G, Wi-Fi, Bluetooth, [GNSS](/mobilnisite/slovnik/gnss/)). TRS zajišťuje, že výrobci optimalizují celý přijímací řetězec, nejen RF čipovou sadu.

Navíc, když sítě nasadily pokročilé techniky jako MIMO a agregace nosných, které spoléhají na více antén, stalo se zásadním zajistit výkon každé anténní cesty. Testování TRS, často prováděné na anténní port nebo v konfiguracích MIMO (např. Total Radiated Sensitivity for MIMO), pomáhá ověřit, že diverzitní a MIMO zisky jsou dosažitelné v praxi. Je to klíčový nástroj pro síťové operátory při akceptačním testování zařízení, aby se zabránilo nasazení zařízení, která by degradovala výkon sítě tím, že by vyžadovala vyšší vysílací výkon základnové stanice pro kompenzaci špatného příjmu UE, čímž by se snižovala celková kapacita a pokrytí sítě.

## Klíčové vlastnosti

- Měří celkovou citlivost přijímače včetně účinků antény prostřednictvím testování Over-The-Air
- Poskytuje jedinou hodnotu (dBm) představující sféricky integrovanou citlivost
- Zásadní pro validaci reálného výkonu, nad rámec ideálních vedených testů
- Povinný konformační test pro certifikaci UE dle 3GPP napříč více releasy
- Zohledňuje orientaci zařízení a nedokonalosti vyzařovacího diagramu antény
- Kritická pro hodnocení výkonu zařízení s více anténami a schopnostmi MIMO

## Definující specifikace

- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 22.989** (Rel-20) — FRMCS Analysis and Requirements
- **TS 25.144** (Rel-11) — UE OTA Antenna Performance Requirements
- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TS 37.144** (Rel-19) — UE OTA Antenna Performance Requirements
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TR 37.902** (Rel-19) — OTA TRP/TRS Measurement for LTE Terminals
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.561** (Rel-19) — UE Conformance for TRP/TRS FR1
- **TR 38.834** (Rel-17) — NR FR1 TRP/TRS Test Methodology
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [TRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/trs/)
