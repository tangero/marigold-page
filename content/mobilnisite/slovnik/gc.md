---
slug: "gc"
url: "/mobilnisite/slovnik/gc/"
type: "slovnik"
title: "GC – General Control (SAP)"
date: 2025-01-01
abbr: "GC"
fullName: "General Control (SAP)"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gc/"
summary: "Service Access Point (SAP, přístupový bod služby) používaný v protokolové architektuře rádiových přístupových vrstev UMTS a LTE. Označuje logické rozhraní a servisní primitiva pro obecnou řídicí signa"
---

GC je General Control Service Access Point (přístupový bod služby obecného řízení), který poskytuje logické rozhraní pro signalizaci řízení mezi vrstvou Radio Resource Control a nižšími vrstvami v rádiových přístupových sítích UMTS a LTE.

## Popis

General Control Service Access Point ([GC-SAP](/mobilnisite/slovnik/gc-sap/)) je konceptuální bod ve vrstvené protokolové architektuře uživatelského zařízení (UE) a sítě [UTRAN](/mobilnisite/slovnik/utran/)/[E-UTRAN](/mobilnisite/slovnik/e-utran/). [SAP](/mobilnisite/slovnik/sap/) definuje, jak spolu komunikují sousední protokolové vrstvy; specifikuje služby poskytované nižší vrstvou vrstvě nad ní. GC-SAP je konkrétně bod, přes který vrstva Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) vydává obecné řídicí příkazy a přijímá indikace od nižších vrstev, které zahrnují Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)), Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)), Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) a Physical (PHY) vrstvu. Na rozdíl od vyhrazených řídicích SAP pro specifické funkce, GC-SAP zpracovává široké, nevyhrazené řídicí operace.

Architektonicky je vrstva RRC správcem řídicí roviny v protokolové zásobníku rádiového rozhraní. Pro správu rádiových zdrojů potřebuje konfigurovat a řídit nižší vrstvy. To se děje právě prostřednictvím SAP. GC-SAP je jedním z několika SAP (další zahrnují např. DCCH pro vyhrazený řídicí provoz a DTCH pro vyhrazený uživatelský provoz). Prostřednictvím GC-SAP používá vrstva RRC servisní primitiva – standardizované zprávy jako 'RLC-CONFIG', 'MAC-CONFIG' nebo 'PHY-CONFIG' – k vytváření, modifikaci nebo uvolňování protokolových entit a jejich parametrů v nižších vrstvách. Například, když se RRC rozhodne zřídit nový rádiový nosič, odešle konfigurační zprávy přes GC-SAP, aby instruovala vrstvu RLC, jaký režim použít (Transparentní, Nepotvrzovaný, Potvrzovaný), vrstvu MAC o prioritě a mapování logických kanálů a vrstvu PHY o konfiguraci transportních kanálů.

Funguje na základě modelu požadavek-potvrzení/indikace-odpověď. RRC (uživatel služby) vydá požadavek (request primitive) směrem dolů přes GC-SAP. Příjemce v nižší vrstvě (poskytovatel služby) požadavek zpracuje a může vrátit potvrzení (confirm primitive) zpět nahoru přes SAP. Naopak, nižší vrstvy mohou použít GC-SAP k odeslání indikačních primitiv (indication primitive) směrem nahoru k RRC, aby nahlásily události (např. dokončení náhodného přístupu, selhání rádiového spoje) nebo změny stavu. Toto abstrahované rozhraní umožňuje, aby logika RRC byla z velké části nezávislá na konkrétní implementaci nižších vrstev, což podporuje modularitu v návrhu protokolu. Jeho role je klíčová pro správu všech rádiových nosičů, provádění předávání hovoru (handover) a procedur mobility spojení, protože všechny tyto procesy vyžadují koordinovanou rekonfiguraci napříč více protokolovými vrstvami.

## K čemu slouží

GC-SAP byl vytvořen, aby poskytoval čisté, standardizované a abstrahované řídicí rozhraní uvnitř složitého protokolového zásobníku rádiového rozhraní systémů 3GPP. V raných bezdrátových systémech bylo řízení často těsně provázáno, což činilo protokoly nepružnými a obtížně vyvíjitelnými. Vrstvená architektura s dobře definovanými SAP, včetně GC, byla zavedena pro oddělení funkcí: vrstva RRC činí strategická rozhodnutí o rádiových zdrojích, zatímco nižší vrstvy zajišťují taktické provádění přenosu dat. GC-SAP řeší problém, jak může strategická vrstva (RRC) spolehlivě a jednoznačně řídit taktické vrstvy, aniž by se zabývala jejich vnitřními detaily.

Historická motivace vychází z potřeby robustní řídicí roviny v UMTS pro podporu sofistikovaných služeb s různými požadavky na QoS. Vrstva RRC potřebovala dynamicky spravovat více paralelních rádiových nosičů, každý s různým nastavením RLC/MAC/PHY. Vyhrazený řídicí kanál pro signalizaci (DCCH) přenáší RRC zprávy mezi UE a sítí, ale GC-SAP je vnitřní mechanismus pro lokální RRC entitu, aby řídila svůj vlastní protokolový zásobník. Tento návrh řeší omezení monolitických řídicích struktur a umožňuje funkce jako bezproblémová rekonfigurace nosiče během předávání hovoru nebo změny služby. Formalizuje interní 'příkazový a řídicí' jazyk softwaru UE a NodeB/eNodeB, což je nezbytné pro testování interoperability a konzistentní chování napříč různými výrobci čipových sad a infrastruktury.

## Klíčové vlastnosti

- Definuje servisní rozhraní pro řízení nižších vrstev (RLC, MAC, PHY) ze strany RRC.
- Používá standardizovaná servisní primitiva pro konfiguraci a hlášení stavu.
- Zpracovává nevyhrazené, obecné řídicí příkazy (např. zřizování/uvolňování entit).
- Umožňuje abstrahovaný a modulární návrh protokolového zásobníku.
- Podporuje komunikační model požadavek/potvrzení a indikace/odpověď.
- Nezbytný pro dynamickou správu rádiových nosičů a transportních kanálů.

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.768** (Rel-12) — Group Communication System Enablers for LTE
- **TS 24.481** (Rel-19) — Mission Critical Services (MCS) group management
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 33.888** (Rel-12) — Security Study for Group Communication in LTE
- **TS 38.744** (Rel-19) — AI/ML for NR Mobility Study
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [GC na 3GPP Explorer](https://3gpp-explorer.com/glossary/gc/)
