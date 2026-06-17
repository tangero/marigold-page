---
slug: "dcch"
url: "/mobilnisite/slovnik/dcch/"
type: "slovnik"
title: "DCCH – Dedicated Control Channel"
date: 2025-01-01
abbr: "DCCH"
fullName: "Dedicated Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dcch/"
summary: "Point-to-point obousměrný logický kanál používaný pro přenos vyhrazených řídicích informací mezi sítí a konkrétním uživatelským zařízením (UE). Je nezbytný pro správu spojení řízení rádiových zdrojů ("
---

DCCH je vyhrazený, point-to-point obousměrný logický kanál používaný pro přenos řídicích informací mezi sítí a konkrétním UE, který je nezbytný pro RRC spojení, mobilitu a signalizaci vyšších vrstev.

## Popis

Dedicated Control Channel (DCCH) je základní logický kanál v architektuře protokolů rádiového rozhraní 3GPP, který funguje v řídicí rovině. Je zřízen pro konkrétní uživatelské zařízení (UE) při navázání spojení řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) a poskytuje vyhrazenou, spolehlivou signalizační cestu. DCCH je obousměrný kanál, což znamená, že se používá pro přenos řídicích informací jak v uplinku (UE k síti), tak v downlinku (síť k UE). Existuje pouze ve stavu RRC_CONNECTED, protože je neodmyslitelně spojen se správou aktivního spojení. Jako logický kanál je DCCH mapován na transportní kanály (jako je Dedicated Transport Channel, [DTCH](/mobilnisite/slovnik/dtch/), nebo společné transportní kanály během navazování spojení) a následně na fyzické kanály pro přenos vzduchem, přičemž konkrétní mapování definuje technologie rádiového přístupu (RAT), jako je UMTS, LTE nebo NR.

Z hlediska fungování přenáší DCCH veškerou vyhrazenou řídicí signalizaci pro připojené UE. To zahrnuje zprávy protokolu RRC, které spravují samotné spojení, jako je RRC Connection Reconfiguration, RRC Connection Release a příkazy pro hlášení měření. Klíčové je, že DCCH také slouží jako přenosová cesta pro zprávy signalizace vyšších vrstev, Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)), mezi UE a jádrem sítě (např. [MME](/mobilnisite/slovnik/mme/) v LTE, [AMF](/mobilnisite/slovnik/amf/) v 5G). Tyto zprávy NAS, které jsou pro RAN transparentní, jsou zapouzdřeny v rámci RRC zpráv pro přenos přes DCCH. Kanál využívá potvrzovaný režim ([AM](/mobilnisite/slovnik/am/)) vrstvy RLC (Radio Link Control) k zajištění spolehlivého doručování signalizačních zpráv ve správném pořadí, což je zásadní pro udržení konzistence stavu spojení a provedení složitých procedur, jako je předání spojení.

Klíčovými komponentami spojenými s DCCH jsou entity protokolu RRC v UE a v gNB/[eNB](/mobilnisite/slovnik/enb/)/NodeB a vrstva RLC nakonfigurovaná v potvrzovaném režimu. Jeho role je ústřední pro prakticky všechny procedury v připojeném režimu: správu mobility (příprava a provedení předání spojení), správu rádiových přenosových kanálů (zřízení, změna, uvolnění), aktivaci zabezpečení (šifrování a ochrana integrity signalizace) a přenos informací o schopnostech UE. Zřízení, údržba a uvolnění DCCH jsou synonymem životního cyklu RRC spojení. V 5G NR, zatímco základní koncept zůstává, je protokolový zásobník a některé struktury zpráv vyvinuté, ale role DCCH jako vyhrazeného signalizačního přenašeče pro připojené UE je zachována a je nezbytná pro mobilitu řízenou sítí a správu služeb.

## K čemu slouží

DCCH byl vytvořen, aby poskytoval spolehlivou, vyhrazenou a bezpečnou signalizační cestu pro jednotlivá UE poté, co přejdou z režimu idle do připojeného režimu. Před navázáním spojení používají UE pro počáteční přístup společné řídicí kanály (jako je [CCCH](/mobilnisite/slovnik/ccch/)), ty jsou však sdílené, založené na soutěžení a nevhodné pro průběžnou, obousměrnou výměnu citlivých řídicích informací potřebných k udržení aktivní relace. DCCH řeší problém správy složitých interakcí se stavem – jako jsou předání spojení, správa přenosových kanálů a zabezpečená signalizace NAS – tím, že poskytuje point-to-point logické spojení se zárukami doručení.

Historicky, zavedený v 3G UMTS (Release 99), byl DCCH klíčovou inovací, která umožnila efektivní, sítí řízenou mobilitu a správu kvality služeb pro paketově přepínané služby. Odstranil omezení používání pouze společných nebo vysílacích kanálů pro veškerou řídicí signalizaci, což by bylo neefektivní, nezabezpečené a neschopné podporovat sofistikované stavy spojení. DCCH umožňuje síti udržovat přesný kontext pro každé připojené UE, což umožňuje rychlou adaptaci rádiových zdrojů, plynulou mobilitu mezi buňkami a zabezpečený přenos signalizace správy předplatného a relace mezi UE a jádrem sítě.

Jeho pokračující existence přes LTE až do 5G NR podtrhuje jeho základní účel: oddělit spolehlivý přenos vyhrazené řídicí signalizace od uživatelských datových toků a od počáteční přístupové signalizace, čímž se vytvoří robustní architektura řídicí roviny. Toto oddělení je klíčové pro škálovatelnost sítě, zabezpečení (umožnění ochrany integrity a šifrování signalizace) a efektivní provádění řídicích procedur v reálném čase, které jsou základem mobility uživatele a kontinuity služeb.

## Klíčové vlastnosti

- Point-to-point obousměrný logický kanál pro vyhrazenou signalizaci UE
- Je zřízen a existuje pouze během stavu RRC_CONNECTED
- Přenáší jak zprávy protokolu RRC, tak zapouzdřenou signalizaci NAS
- Využívá potvrzovaný režim (AM) RLC pro spolehlivé doručování ve správném pořadí
- Nezbytný pro procedury mobility, jako je předání spojení a hlášení měření
- Podporuje bezpečnostní funkce včetně ochrany integrity a šifrování řídicích zpráv

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [CCCH – Common Control Channel](/mobilnisite/slovnik/ccch/)
- [DTCH – Dedicated Traffic Channel](/mobilnisite/slovnik/dtch/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TR 26.902** (Rel-19) — Video Codec Performance for 3GPP Packet Services
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.314** (Rel-19) — E-UTRA Radio Measurements Specification
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [DCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/dcch/)
