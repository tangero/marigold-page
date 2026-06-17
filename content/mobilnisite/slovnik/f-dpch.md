---
slug: "f-dpch"
url: "/mobilnisite/slovnik/f-dpch/"
type: "slovnik"
title: "F-DPCH – Fractional Dedicated Physical Channel"
date: 2025-01-01
abbr: "F-DPCH"
fullName: "Fractional Dedicated Physical Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/f-dpch/"
summary: "Downlinkový fyzický kanál v UMTS (UTRAN) používaný výhradně v režimu duplexu s frekvenčním dělením (FDD). Efektivně přenáší příkazy pro řízení výkonu (TPC) k více uživatelským zařízením (UE) tím, že č"
---

F-DPCH je downlinkový fyzický kanál UMTS v režimu FDD, který efektivně přenáší TPC příkazy k více uživatelským zařízením (UE) tím, že časově multiplexuje jejich signály na jeden kódový kanál, čímž šetří kódové zdroje Node B.

## Popis

Fractional Dedicated Physical Channel (F-DPCH) je downlinkový fyzický kanál definovaný v rádiovém rozhraní UMTS WCDMA. Jeho primární funkcí je přenášet příkazy pro řízení výkonu (TPC) a volitelně bity indikátoru kombinace transportního formátu (TFCI) k uživatelskému zařízení (UE) pro řízení výkonu v uplinku. Klíčovou inovací F-DPCH je jeho 'frakční' povaha: namísto přidělení plného kanalizačního kódu (vzácného zdroje v downlinku) pro vyhrazený fyzický řídicí kanál každému UE umožňuje časové multiplexování TPC příkazů pro více UE na jediný kanalizační kód. Každý rámec F-DPCH je rozdělen na časové sloty. V rámci slotu je část bitů přidělena konkrétnímu UE. Pozice TPC bitů pro dané UE ve slotu je konfigurována vyššími vrstvami prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/). To je v protikladu k plnému [DPCH](/mobilnisite/slovnik/dpch/), který používá vyhrazený kód na každé UE. F-DPCH je vždy asociován s uplinkovým vyhrazeným fyzickým řídicím kanálem ([DPCCH](/mobilnisite/slovnik/dpcch/)) od UE. Node B využívá kvalitu přijímaného uplinkového DPCCH ke generování TPC příkazu, který je následně odeslán na UE na jeho přidělené části F-DPCH. Tento mechanismus vyžaduje přesné časové sladění. F-DPCH je definován v několika specifikacích fyzické vrstvy UMTS (25.211, 25.212, 25.213) a přímo ovlivňuje procedury řízení rádiových zdrojů detailně popsané v specifikacích jako 25.133 (požadavky) a 25.331 (RRC).

## K čemu slouží

F-DPCH byl zaveden k řešení kritického omezení kapacity v sítích UMTS: vyčerpání downlinkových kanalizačních kódů, zejména ve scénářích s mnoha simultánními uživateli hlasu nebo nízkorychlostních dat (např. VoIP). V původním návrhu WCDMA vyžadovalo každé připojené UE alespoň jeden vyhrazený downlinkový kanalizační kód pro signalizaci řízení výkonu (na [DPCH](/mobilnisite/slovnik/dpch/)), i když uživatel neměl žádná skutečná downlinková data k odeslání. To omezovalo počet uživatelů, které buňka mohla podporovat, protože strom kódů je konečný zdroj (512 kódů na scrambling kód). F-DPCH to řeší tím, že umožňuje jednomu kódu obsluhovat příkazy řízení výkonu pro až 10 UE (v závislosti na konfiguraci), což dramaticky zlepšuje efektivitu využití downlinkových kódových zdrojů. To bylo obzvláště důležité pro podporu vysokého objemu VoIP hovorů od Release 6 a dále. Umožnilo operátorům podporovat více simultánních připojení na buňku, čímž zvýšilo kapacitu sítě a spektrální účinnost bez potřeby dodatečného spektra. Návrh byl specificky zaměřen na režim [FDD](/mobilnisite/slovnik/fdd/), kde je toto omezení kódů nejakutnější, a stal se klíčovou vlastností pro efektivní podporu služeb citlivých na zpoždění s nízkou přenosovou rychlostí v sítích UMTS/[HSPA](/mobilnisite/slovnik/hspa/).

## Klíčové vlastnosti

- Časově multiplexuje TPC příkazy pro více UE na jediný downlinkový kanalizační kód
- Funguje pouze v režimu UMTS FDD
- Přenáší TPC bity a volitelně TFCI bity pro asociované UE
- Formát slotu specifický pro UE je konfigurován prostřednictvím signalizace RRC
- Vyžaduje těsné časové synchronizace s uplinkovým DPCCH od UE
- Významně zvyšuje kapacitu downlinkových kódů pro řídicí signalizaci

## Související pojmy

- [DPCH – Dedicated Physical Channel](/mobilnisite/slovnik/dpch/)

## Definující specifikace

- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.215** (Rel-19) — UTRA FDD Measurement Definitions
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.706** (Rel-13) — Downlink Enhancements for UMTS Study
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [F-DPCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/f-dpch/)
