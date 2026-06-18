---
slug: "s-e-dpcch"
url: "/mobilnisite/slovnik/s-e-dpcch/"
type: "slovnik"
title: "S-E-DPCCH – Secondary Enhanced Dedicated Physical Control Channel"
date: 2025-01-01
abbr: "S-E-DPCCH"
fullName: "Secondary Enhanced Dedicated Physical Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/s-e-dpcch/"
summary: "S-E-DPCCH je řídicí kanál pro uplink v HSUPA, používaný, když je UE nakonfigurováno s více E-DCH transportními kanály (víceproudový přenos). Nese Happy Bit a číslo sekvence retransmisí (RSN) pro sekun"
---

S-E-DPCCH je řídicí kanál HSUPA pro uplink, který nese Happy Bit a číslo sekvence retransmisí (Retransmission Sequence Number) pro sekundární datový proud, když UE používá více E-DCH transportních kanálů.

## Popis

Sekundární rozšířený vyhrazený fyzický řídicí kanál (Secondary Enhanced Dedicated Physical Control Channel, S-E-DPCCH) je fyzický kanál pro uplink v rádiovém rozhraní UMTS/[HSPA](/mobilnisite/slovnik/hspa/), konkrétně pro rozšířený uplink ([E-DCH](/mobilnisite/slovnik/e-dch/) neboli [HSUPA](/mobilnisite/slovnik/hsupa/)). Používá se, když je uživatelské zařízení (UE) nakonfigurováno k vysílání na dvou nebo čtyřech rozšířených vyhrazených kanálech (E-DCH) současně, což je funkce známá jako víceproudový přenos zavedený v pozdějších vydáních HSPA+. Primární rozšířený vyhrazený fyzický řídicí kanál ([E-DPCCH](/mobilnisite/slovnik/e-dpcch/)) přenáší řídicí informace pro primární E-DCH transportní kanál, zatímco S-E-DPCCH přenáší řídicí informace pro sekundární E-DCH transportní kanál(y).

S-E-DPCCH vysílá klíčové informace pro plánovač Node B a procesy hybridního automatického opakování ([HARQ](/mobilnisite/slovnik/harq/)) související se sekundárním proudem. To zahrnuje číslo sekvence retransmisí ([RSN](/mobilnisite/slovnik/rsn/)), které udává, zda je aktuální přenos nový paket nebo retransmise, a Happy Bit. Happy Bit je jednobitový indikátor, který informuje síť, zda je UE 'spokojeno' s aktuálně přidělenými uplinkovými prostředky, nebo si přeje vyšší přenosovou rychlost. Tato zpětná vazba je zásadní pro Node B, aby mohl provádět efektivní plánování paketů a adaptaci spoje.

Z pohledu fyzické vrstvy je S-E-DPCCH vysílán pomocí specifického kanalizačního kódu a je časově synchronizován s přidruženým sekundárním rozšířeným vyhrazeným fyzickým datovým kanálem ([S-E-DPDCH](/mobilnisite/slovnik/s-e-dpdch/)). Jeho přítomnost je podmíněna konfigurací E-DCH v UE. Kanál umožňuje detailnější řízení a zpětnou vazbu pro více paralelních uplinkových přenosů, čímž zvyšuje efektivitu systému HSUPA díky lepšímu využití výkonu UE a uplinkové kapacity buňky, když má UE k odeslání více paketů.

## K čemu slouží

S-E-DPCCH byl vytvořen pro podporu víceproudového přenosu v [HSUPA](/mobilnisite/slovnik/hsupa/) (rozšířený uplink). Původní HSUPA (Rel-6) podporovala jediný E-DCH transportní kanál. Pro zvýšení špičkových uplinkových přenosových rychlostí a zlepšení propustnosti, zejména u trhavého provozu, pozdější vydání zavedla schopnost používat více E-DCH transportních kanálů paralelně. Každý nezávislý transportní kanál však vyžaduje vlastní řídicí signalizaci pro HARQ a plánovací zpětnou vazbu.

Primární E-DPCCH tuto víceproudovou operaci nemohl podporovat. S-E-DPCCH byl zaveden, aby tento problém vyřešil poskytnutím vyhrazeného řídicího kanálu pro sekundární proud(y). To umožnilo funkce jako 2ms TTI s více HARQ procesy na proud, což vedlo k vyšším uplinkovým přenosovým rychlostem, snížení latence a efektivnějšímu využití vysílacího výkonu UE díky paralelním přenosům paketů. Šlo o klíčové vylepšení pro udržení konkurenceschopnosti HSUPA a zvýšení spektrální účinnosti uplinku.

## Klíčové vlastnosti

- Nese zpětnou vazbu Happy Bit pro sekundární E-DCH proud
- Přenáší číslo sekvence retransmisí (RSN) pro HARQ proces sekundárního proudu
- Používá se, když je UE nakonfigurováno s více E-DCH transportními kanály
- Umožňuje víceproudový provoz HSUPA pro vyšší uplinkovou propustnost
- Fyzicky asociován s kanálem S-E-DPDCH
- Konfigurován prostřednictvím signalizace RRC na základě schopností UE a nastavení sítě

## Související pojmy

- [E-DPCH – EDCH – Dedicated Physical Channel](/mobilnisite/slovnik/e-dpch/)
- [E-DPCH – EDCH – Dedicated Physical Channel](/mobilnisite/slovnik/e-dpch/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [S-E-DPCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-e-dpcch/)
