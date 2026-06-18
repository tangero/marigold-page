---
slug: "srb"
url: "/mobilnisite/slovnik/srb/"
type: "slovnik"
title: "SRB – Signalling Radio Bearer"
date: 2025-01-01
abbr: "SRB"
fullName: "Signalling Radio Bearer"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/srb/"
summary: "Logický kanál v mobilních sítích vyhrazený pro přenos signalizačních zpráv řídicí roviny mezi UE a sítí. Zajišťuje spolehlivé doručení kritické signalizace pro navázání spojení, mobilitu a konfiguraci"
---

SRB je vyhrazený logický kanál, který přenáší signalizační zprávy řídicí roviny mezi UE a sítí, aby zajistil spolehlivé doručení pro navázání spojení, mobilitu a konfiguraci.

## Popis

Signalling Radio Bearer (SRB) je základní koncept v mobilních sítích 3GPP, který označuje logický kanál speciálně přidělený pro přenos signalizačních zpráv řídicí roviny mezi uživatelským zařízením (UE) a rádiovou přístupovou sítí (RAN). Na rozdíl od datových rádiových přenašečů ([DRB](/mobilnisite/slovnik/drb/)), které přenášejí data uživatelské roviny, jsou SRB výhradně používány pro signalizaci, která zahrnuje zprávy pro řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)), ne-přístupovou vrstvu ([NAS](/mobilnisite/slovnik/nas/)) a další řídicí protokoly. SRB jsou zřizovány a spravovány protokolem RRC, aby zajistily spolehlivé a prioritní doručení kritických signalizačních informací. Pracují přes rozhraní vzduchem (např. Uu v LTE/5G) a jsou mapovány na specifické transportní kanály a fyzické zdroje nižšími vrstvami ([MAC](/mobilnisite/slovnik/mac/) a [PHY](/mobilnisite/slovnik/phy/)).

Z architektonického hlediska jsou SRB definovány jako součást protokolového zásobníku rádiového rozhraní, přičemž různé typy SRB slouží odlišným účelům. Například SRB0 se používá pro počáteční navázání RRC spojení přes společné řídicí kanály, zatímco SRB1 je vyhrazen pro RRC zprávy a může také přenášet NAS zprávy před zřízením dalších SRB. SRB jsou charakterizovány svými konfiguračními parametry, jako je režim [RLC](/mobilnisite/slovnik/rlc/) (typicky potvrzovaný režim pro spolehlivost), identita logického kanálu a nastavení prioritizace. Síť konfiguruje SRB během stavů jako RRC_IDLE, RRC_INACTIVE a RRC_CONNECTED, aby usnadnila signalizační výměnu pro funkce jako předávání spojení, zřizování přenašečů a aktivace zabezpečení.

Princip fungování SRB zahrnuje vrstvu RRC v UE a gNB (nebo [eNB](/mobilnisite/slovnik/enb/)), které tyto přenašeče zřizují podle potřeby. Signalizační zprávy jsou zapouzdřeny do RRC protokolových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)) a přenášeny přes přidělený SRB. Vrstva RLC zajišťuje spolehlivé doručení prostřednictvím retransmisí, pokud je v potvrzovaném režimu, zatímco MAC se stará o plánování a multiplexování s dalšími logickými kanály. SRB jsou klíčové pro provoz sítě, protože přenášejí nezbytné informace pro správu mobility (např. příkazy k předání spojení), správu relací (např. požadavky na připojení PDN) a bezpečnostní procedury (např. autentizaci a odvození klíčů). Jejich spolehlivý provoz je zásadní pro udržení síťové konektivity a kontinuity služeb.

## K čemu slouží

SRB existují, aby poskytly vyhrazený a spolehlivý kanál pro signalizaci řídicí roviny, oddělující kritické síťové řídicí zprávy od datového provozu uživatele. V raných mobilních systémech signalizace a data často sdílely zdroje, což vedlo k potenciálnímu zahlcení a zpožděním v nezbytných řídicích funkcích. Standardizace SRB v 3GPP, počínaje UMTS a pokračující přes LTE a 5G, to řeší zajištěním, že signalizace má garantované zdroje a prioritu. Tím se řeší problémy jako pomalé navazování spojení, nespolehlivá předání spojení a neefektivní správa zdrojů, které jsou kritické pro stabilitu sítě a uživatelský zážitek.

Historicky byly SRB zavedeny, aby podpořily rostoucí složitost mobilních sítí, které vyžadují rozsáhlou signalizaci pro funkce jako paketové služby, správa kvality služeb (QoS) a pokročilá mobilita. Ve verzi 5 s HSDPA se SRB staly ještě důležitějšími pro zvládání řízení relací vysokorychlostních dat. V průběhu verzí se SRB vyvinuly, aby podporovaly nové funkčnosti, jako je agregace nosných, duální konektivita a síťové segmentování, přenášením odpovídajících RRC konfigurací. Jejich účelem je umožnit robustní a efektivní komunikaci řídicí roviny, která tvoří páteř provozu mobilní sítě, a zajistit, aby se UE mohla spolehlivě připojit, pohybovat a komunikovat v rámci sítě.

## Klíčové vlastnosti

- Vyhrazený logický kanál pro signalizaci řídicí roviny
- Přenáší RRC a NAS zprávy mezi UE a sítí
- Konfigurován se spolehlivým potvrzovaným režimem RLC
- Prioritizován oproti datovým přenašečům pro kritickou signalizaci
- Podporuje více typů (např. SRB0, SRB1, SRB2) pro různé funkce
- Nezbytný pro navázání spojení, mobilitu a bezpečnostní procedury

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [DRB – Data Radio Bearer](/mobilnisite/slovnik/drb/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TR 25.993** (Rel-19) — UTRA RAB Examples and Radio Interface Mapping
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.314** (Rel-19) — E-UTRA Radio Measurements Specification
- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview
- **TS 37.470** (Rel-19) — W1 Interface Introduction for ng-eNB
- **TS 38.323** (Rel-19) — Packet Data Convergence Protocol (PDCP)
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.470** (Rel-19) — F1 Interface Introduction
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SRB na 3GPP Explorer](https://3gpp-explorer.com/glossary/srb/)
