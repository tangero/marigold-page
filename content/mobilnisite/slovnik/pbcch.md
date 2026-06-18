---
slug: "pbcch"
url: "/mobilnisite/slovnik/pbcch/"
type: "slovnik"
title: "PBCCH – Packet Broadcast Control Channel"
date: 2025-01-01
abbr: "PBCCH"
fullName: "Packet Broadcast Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pbcch/"
summary: "Logický vysílací kanál v sítích GPRS a EDGE sloužící k přenosu systémových informací a řídicích parametrů specifických pro služby s přepojováním paketů všem mobilním stanicím v buňce. Umožňuje efektiv"
---

PBCCH je logický vysílací kanál v sítích GPRS a EDGE, který přenáší systémové informace a řídicí parametry pro přepojování paketů všem mobilním stanicím v buňce za účelem efektivního výběru buňky a přístupu k paketovým datům.

## Popis

Packet Broadcast Control Channel (PBCCH) je logický kanál v systémech GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), zavedený pro podporu služeb s přepojováním paketů prostřednictvím [GPRS](/mobilnisite/slovnik/gprs/). Funguje jako jednosměrný vysílací kanál (downlink), obdobně jako Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)) používaný pro služby s přepojováním okruhů, ale je specificky přizpůsoben pro paketová data. PBCCH vysílá základní systémové informace, které mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) potřebují pro přístup a využití sítě GPRS v rámci buňky. Tyto informace zahrnují parametry pro výběr a převýběr buňky, podrobnosti o dostupných Packet Data Channels ([PDCH](/mobilnisite/slovnik/pdch/)), řídicí parametry přístupu pro Packet Random Access Channel ([PRACH](/mobilnisite/slovnik/prach/)) a režimy provozu sítě.

PBCCH je mapován na fyzické prostředky, konkrétně na jeden nebo více Packet Data Traffic Channels ([PDTCH](/mobilnisite/slovnik/pdtch/)) nakonfigurovaných pro vysílací účely. Buňka může mít PBCCH, nebo ne; pokud jej nemá, jsou související systémové informace GPRS vysílány na klasickém BCCH. Pokud je PBCCH přítomen, přenáší sadu zpráv Packet System Information (PSI). Tyto zprávy, jako PSI1, PSI2 atd., jsou organizovány v rozvrhu a opakovány cyklicky. MS monitoruje PBCCH, aby získala parametry jako parametry výběru buňky GPRS (C31, C32), seznam dostupných PDCH, řídicí parametry PRACH (např. maximální počet opakování, Tx-integer) a kóty směrovací oblasti. Tyto informace jsou klíčové pro MS k provádění procedur, jako je připojení k GPRS (GPRS attach), aktualizace směrovací oblasti a převýběr buňky pro paketové služby.

Z pohledu sítě umožňuje implementace PBCCH efektivnější a vyhrazené vysílání parametrů specifických pro pakety bez přetížení BCCH. Poskytuje síti větší flexibilitu pro nezávislé řízení paketových prostředků bez ohledu na provoz s přepojováním okruhů. Přítomnost PBCCH je signalizována na BCCH. MS používá informace přijaté na PBCCH k synchronizaci s časovou strukturou paketů, identifikaci uplink PDCH pro odesílání přístupových požadavků na PRACH a určení vhodnosti buňky pro služby GPRS. PBCCH spolu s Packet Common Control Channel (PCCCH) tvoří vysílací a společný řídicí rámec, který umožňuje efektivní a škálovatelnou podporu mobilních paketových dat na vývojové cestě GSM.

## K čemu slouží

PBCCH byl zaveden, aby řešil omezení používání stávajícího BCCH pro přepojování okruhů k vysílání systémových informací specifických pro GPRS. Před GPRS přenášel BCCH veškeré potřebné informace o buňce, ale přidání služeb s přepojováním paketů přineslo novou sadu složitých parametrů souvisejících s přidělováním paketových prostředků, přístupovými schématy a správou mobility pro data. Vysílání těchto informací na BCCH by zvýšilo jeho zatížení a složitost, což by mohlo ovlivnit služby s přepojováním okruhů. Navíc mají paketové služby odlišné požadavky na optimalizaci, jako je rychlejší převýběr buňky pro data.

Vytvoření vyhrazeného PBCCH umožnilo samostatný a optimalizovaný informační tok pro uživatele GPRS/EDGE. Vyřešil problém efektivního informování mobilních stanic o dynamicky přidělovaných paketových prostředcích (PDCH) a přístupových parametrech bez ovlivnění signalizace zaměřené na hlas. Toto oddělení umožnilo sítím nezávisle rozvíjet jejich schopnosti v oblasti paketových dat. PBCCH byl klíčovým prvkem pro efektivní algoritmy výběru a převýběru buňky GPRS, což zlepšilo uživatelský zážitek u raných mobilních datových služeb tím, že zajistilo, aby se mobilní zařízení mohla rychle najít a připojit k buňkám s dostupnými paketovými prostředky, a podpořilo tak zavedení trvalého datového připojení v sítích 2G.

## Klíčové vlastnosti

- Vysílá zprávy Packet System Information (PSI) potřebné pro provoz GPRS/EDGE.
- Přenáší parametry pro výběr a převýběr buňky GPRS (např. C31, C32).
- Poskytuje informace o dostupných Packet Data Channels (PDCH) a jejich konfiguraci.
- Vysílá řídicí parametry přístupu pro Packet Random Access Channel (PRACH).
- Signalizuje režimy provozu sítě (NMO I, II, III) a informace o směrovací oblasti.
- Může existovat samostatně; pokud chybí, jsou jeho informace vysílány na standardním BCCH.

## Související pojmy

- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)
- [PCCCH – Packet Common Control Channel](/mobilnisite/slovnik/pccch/)
- [PDCH – Packet Data Channel](/mobilnisite/slovnik/pdch/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [PSI – Provide Subscriber Information](/mobilnisite/slovnik/psi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PBCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pbcch/)
