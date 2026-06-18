---
slug: "bs"
url: "/mobilnisite/slovnik/bs/"
type: "slovnik"
title: "BS – Base Station"
date: 2026-01-01
abbr: "BS"
fullName: "Base Station"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bs/"
summary: "Základnová stanice (BS) je síťový prvek, který v buňkové síti poskytuje rádiové pokrytí a konektivitu uživatelskému zařízení (UE). Spravuje alokaci rádiových zdrojů, přenos/příjem signálu a protokoly"
---

BS (základnová stanice) je síťový prvek, který v buňkové síti poskytuje rádiové pokrytí a konektivitu mobilním zařízením, spravuje rádiové zdroje a slouží jako kritický spojovací článek k páteřní síti.

## Popis

Základnová stanice (BS) je základní součástí rádiové přístupové sítě (RAN) v systémech 3GPP, odpovědná za navázání a udržování bezdrátových komunikačních spojení s uživatelským zařízením (UE) ve své pokryté oblasti, známé jako buňka. Provádí kritické funkce, jako je modulace/demodulace rádiového signálu, kanálové kódování/dekódování, řízení výkonu, správa předávání hovoru a plánování rádiových zdrojů. BS rozhraní s páteřní sítí přes backhaulové spoje (např. k ústředně mobilního přepojování ve 2G/3G nebo k Next Generation NodeB/gNB v architekturách 4G/5G) a se sousedními BS pro koordinaci a podporu mobility.

Architektonicky se BS skládá z několika klíčových podsystémů: Rádiová jednotka ([RU](/mobilnisite/slovnik/ru/)) zajišťuje analogový vysokofrekvenční ([RF](/mobilnisite/slovnik/rf/)) přenos a příjem, včetně zesílení výkonu a filtrace; Základnová pásmová jednotka ([BBU](/mobilnisite/slovnik/bbu/)) zpracovává digitální základnově pásmové signály, implementuje fyzické vrstvy protokolů, opravu chyb a plánování zdrojů; a řídicí a správní jednotka dohlíží na funkce provozu, správy a údržby ([OAM](/mobilnisite/slovnik/oam/)). V moderních nasazeních, jako je 5G, mohou být tyto komponenty rozděleny na centralizované ([CU](/mobilnisite/slovnik/cu/)), distribuované ([DU](/mobilnisite/slovnik/du/)) a rádiové (RU) jednotky v rámci architektury Open RAN (O-RAN) pro zvýšení flexibility a škálovatelnosti.

BS pracuje v definovaných RF šířkách pásma s konkrétními kmitočtovými hranami (dolní a horní), které určují jeho provozní spektrum. Spravuje více přístupových technologií (např. [FDMA](/mobilnisite/slovnik/fdma/), [TDMA](/mobilnisite/slovnik/tdma/), CDMA, OFDMA v závislosti na generaci) pro současné obsluhování více UE. Mezi klíčové implementované protokoly patří Řízení rádiových zdrojů (RRC) pro správu spojení, Protokol konvergence paketových dat (PDCP) pro kompresi hlaviček a šifrování, Řízení rádiového spoje (RLC) pro segmentaci a ARQ a Řízení přístupu k médiu (MAC) pro plánování a multiplexování. BS také provádí měření pro kvalitu spojení, správu rušení a podporuje procedury mobility, jako je předávání hovoru, což zajišťuje plynulou kontinuitu služeb při pohybu UE mezi buňkami.

V širším síťovém ekosystému funguje BS jako primární bod rádiového přístupu, převádějící příkazy páteřní sítě na přenosy přes rozhraní vzduch a naopak. Vynucuje zásady kvality služeb (QoS), spravuje efektivitu využití spektra a podporuje pokročilé funkce, jako je agregace nosných, massive MIMO a formování svazku v pozdějších vydáních. Jeho výkon přímo ovlivňuje kapacitu sítě, pokrytí a uživatelský zážitek, což z něj činí středobod optimalizace a inovací v buňkových standardech.

## K čemu slouží

Základnová stanice existuje za účelem umožnění bezdrátové mobilní komunikace tím, že poskytuje potřebnou infrastrukturu pro připojení uživatelského zařízení k telekomunikační síti. Řeší základní problém rozšíření síťových služeb po geografické oblasti bez kabelového připojení každého zařízení, usnadňuje mobilitu a všudypřítomný přístup. Historicky používaly rané buňkové systémy (jako 1G) základnové stanice s omezenými schopnostmi, ale s rostoucí poptávkou po vyšších přenosových rychlostech, lepší spektrální efektivitě a pokročilejších službách se BS vyvinula, aby těmto potřebám vyhověla prostřednictvím digitálního zpracování signálu, chytřejší správy zdrojů a podpory paketově přepínaných dat.

Motivována omezeními předchozích přístupů – jako je náchylnost analogových systémů k rušení a neefektivita nebo neschopnost raných digitálních systémů zpracovat vysokorychlostní data – byla BS ve standardech 3GPP navržena jako škálovatelná, programovatelná platforma. Umožňuje více přístupová schémata, adaptivní modulaci a kódování a sofistikované anténní technologie pro maximalizaci propustnosti a spolehlivosti. BS také řeší provozní výzvy, jako je plánování sítě, koordinace rušení a energetická účinnost, a stává se klíčovým prvkem pro generace od GSM (2G) po 5G a dále.

## Klíčové vlastnosti

- Vysokofrekvenční přenos a příjem v rámci stanovených kmitočtových hran pásma
- Správa protokolů rozhraní vzduch (např. RRC, PDCP, RLC, MAC)
- Dynamická alokace rádiových zdrojů a plánování pro více UE
- Podpora procedur mobility včetně předávání hovoru a převýběru buňky
- Implementace pokročilých anténních technik, jako je MIMO a formování svazku
- Schopnosti provozu, správy a údržby (OAM) pro správu sítě

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.085** (Rel-19) — Closed User Group (CUG) Supplementary Service Stage 2
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.815** (Rel-5) — IMS Charging Implications
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.103** (R99) — RF Requirements for RRM
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- … a dalších 157 specifikací

---

📖 **Anglický originál a plná specifikace:** [BS na 3GPP Explorer](https://3gpp-explorer.com/glossary/bs/)
