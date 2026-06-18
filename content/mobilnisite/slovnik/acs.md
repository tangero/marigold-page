---
slug: "acs"
url: "/mobilnisite/slovnik/acs/"
type: "slovnik"
title: "ACS – Auto-Configuration Server"
date: 2025-01-01
abbr: "ACS"
fullName: "Auto-Configuration Server"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/acs/"
summary: "Auto-Configuration Server (ACS) je server pro správu sítě definovaný pro vzdálené řízení a konfiguraci zařízení na straně zákazníka (Customer Premises Equipment - CPE), jako jsou domácí routery a set-"
---

ACS je Auto-Configuration Server, server pro správu sítě, který vzdáleně spravuje a konfiguruje zařízení na straně zákazníka (Customer Premises Equipment) pomocí protokolu TR-069.

## Popis

Auto-Configuration Server (ACS) je klíčovou součástí architektury pro správu širokopásmových zařízení, standardizovanou Broadband Forgem v TR-069 ([CPE](/mobilnisite/slovnik/cpe/) [WAN](/mobilnisite/slovnik/wan/) Management Protocol) a široce přijatou a referencovanou v rámci specifikací 3GPP pro správu pevných a konvergentních síťových prvků. Funguje jako centrální server, který komunikuje s velkým počtem zařízení na straně zákazníka (Customer Premises Equipment - CPE) přes zabezpečené spojení, obvykle používající [SOAP](/mobilnisite/slovnik/soap/)/[HTTP](/mobilnisite/slovnik/http/)(S) přes IP síť. ACS iniciuje relace směrem k CPE, které funguje jako klient, za účelem provádění široké škály funkcí správy. Protokol definuje robustní mechanizmus [RPC](/mobilnisite/slovnik/rpc/) (Remote Procedure Call), pomocí kterého může ACS vyvolat metody na CPE pro získání nebo nastavení hodnot parametrů, nahrání/stáhnutí souborů a přijímání asynchronních oznámení o událostech ze zařízení.

Z architektonického hlediska ACS propojuje s dalšími backendovými systémy, jako jsou konfigurační systémy (provisioning systems), platformy pro správu poruch a systémy aktivace služeb. Používá datový model, často založený na modelu TR-181 (Device Data Model) od Broadband Forum, který poskytuje standardizovaný hierarchický strom parametrů reprezentujících konfiguraci, stav a schopnosti zařízení. Tento model umožňuje ACS interagovat s různými typy CPE od různých výrobců jednotným způsobem. Klíčovými komponentami ACS jsou rozhraní směrem k nadřazeným systémům (northbound interfaces - NBI) pro integraci s [OSS](/mobilnisite/slovnik/oss/)/[BSS](/mobilnisite/slovnik/bss/), jádro pro správu relací a protokolový engine pro zpracování komunikace TR-069 a databáze pro ukládání informací o zařízeních, historii relací a konfiguračních politik.

Během provozu ACS spravuje celý životní cyklus CPE. Při počátečním startu (fáze konfigurace - provisioning) CPE zjistí [URL](/mobilnisite/slovnik/url/) ACS, naváže zabezpečené spojení a informuje ACS o svých schopnostech. ACS následně zašle potřebnou konfiguraci (např. nastavení VLAN, SSID, parametry VoIP) pro zajištění služeb. Pro průběžnou správu může ACS provádět periodické diagnostiky, sledovat metriky výkonu a posílat aktualizace firmwaru. Také řeší správu poruch přijímáním a zpracováním oznámení o událostech (jako 'value change' nebo 'transfer complete') z CPE, což umožňuje proaktivní odstraňování problémů. Role ACS je klíčová pro umožnění konfigurace typu 'zero-touch', snížení počtu výjezdů techniků, zajištění konzistence služeb a udržování stavu nasazeného souboru zařízení.

## K čemu slouží

ACS byl vytvořen k řešení zásadních provozních výzev, kterým čelí poskytovatelé služeb při správě milionů vzdáleně nasazených zařízení CPE. Před TR-069 a ACS vyžadovalo konfigurování domácích bran a routerů buď manuální návštěvy techniků na místě, nebo spoléhání se na méně standardizované, výrobcem specifické nástroje správy. Tento přístup byl nákladný, pomalý, náchylný k chybám a neumožňoval škálování s rychlým růstem počtu širokopásmových předplatitelů. ACS poskytuje standardizovaný, automatizovaný a vzdálený rámec správy, který eliminuje potřebu fyzického přístupu k zákazníkovi pro většinu úloh konfigurace a aktualizací.

Historický kontext sahá do počátku 21. století s masovým nasazením DSL a rozšířením složitých domácích síťových zařízení nabízejících služby triple-play (data, hlas, video). Správa kvality služeb, nasazování nových funkcí a řešení problémů napříč heterogenním ekosystémem zařízení se staly hlavním úzkým místem. Protokol TR-069 a koncept serveru ACS byly vyvinuty, aby poskytly řešení nezávislé na výrobci a interoperabilní. Odstraňují omezení předchozích ad-hoc metod tím, že nabízejí zabezpečený, transakční a modelově řízený přístup ke správě zařízení, který je nezbytný pro rychlé zavádění služeb, konzistentní zákaznický zážitek a efektivní provoz sítě.

V rámci ekosystému 3GPP je ACS referencován v kontextech, jako je konvergence pevných a mobilních sítí (Fixed-Mobile Convergence - FMC), správa rezidenčních bran v sítích 5G a širší oblast správy sítě a automatizace. Řeší problémy spojené s onboardinkem zařízení, vynucováním politik a správou životního cyklu softwaru škálovatelným a automatizovaným způsobem, což je v souladu s cíli 3GPP v oblasti automatizace sítě a snížení provozních nákladů (OPEX).

## Klíčové vlastnosti

- Vzdálená konfigurace a nastavení parametrů CPE
- Správa a aktualizace zabezpečeného firmwaru a softwarových obrazů
- Sledování stavu v reálném čase a diagnostika výkonu
- Standardizovaný datový model (např. TR-181) pro interoperabilitu mezi výrobci
- Zpracování asynchronních oznámení o událostech ze spravovaných zařízení
- Integrační rozhraní pro systémy OSS/BSS a systémy aktivace služeb

## Související pojmy

- [CPE – Customer Premises Equipment](/mobilnisite/slovnik/cpe/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2
- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.111** (Rel-19) — LMU RF Characteristics for UTRA FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.703** (Rel-12) — HNB Emergency Warning Area Study for UTRA
- **TS 25.866** (Rel-9) — 1.28Mcps TDD Home NodeB Study Report
- **TR 25.942** (Rel-19) — UTRA RF System Scenarios Specification
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- … a dalších 71 specifikací

---

📖 **Anglický originál a plná specifikace:** [ACS na 3GPP Explorer](https://3gpp-explorer.com/glossary/acs/)
