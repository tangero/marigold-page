---
slug: "s-dpcch"
url: "/mobilnisite/slovnik/s-dpcch/"
type: "slovnik"
title: "S-DPCCH – Secondary Dedicated Physical Control Channel"
date: 2025-01-01
abbr: "S-DPCCH"
fullName: "Secondary Dedicated Physical Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/s-dpcch/"
summary: "S-DPCCH je řídicí kanál v uplinku v HSPA+, používaný spolu s primárním DPCCH, když je UE konfigurováno pro MIMO nebo vícekanálový provoz. Přenáší pilotní bity a indikátor kombinace transportního formá"
---

S-DPCCH je řídicí kanál v uplinku v HSPA+, který přenáší pilotní bity a TFCI pro sekundární datový proud, což umožňuje MIMO nebo vícekanálový provoz vedle primárního DPCCH.

## Popis

Sekundární dedikovaný fyzický řídicí kanál (S-DPCCH) je fyzický kanál v uplinku definovaný ve specifikacích 3GPP UMTS/[HSPA](/mobilnisite/slovnik/hspa/), konkrétně pro vylepšení jako [MIMO](/mobilnisite/slovnik/mimo/) (Multiple-Input Multiple-Output) a vícekanálové HSPA. Funguje ve spojení s primárním dedikovaným fyzickým řídicím kanálem ([DPCCH](/mobilnisite/slovnik/dpcch/)). Primární DPCCH je vždy přítomen a přenáší řídicí informace pro primární transportní kanál. S-DPCCH je aktivován, když je uživatelské zařízení (UE) konfigurováno v módech, které vyžadují signalizaci řídicích informací pro sekundární datový proud, jako je Dual-Cell HSPA (DC-HSPA) v uplinku nebo uplink MIMO.

Fyzicky je S-DPCCH kódově multiplexován s ostatními kanály v uplinku. Přenáší zásadní řídicí informace potřebné pro demodulaci a dekódování přidruženého sekundárního dedikovaného fyzického datového kanálu (S-DPDCH). Tyto informace typicky zahrnují pilotní bity pro odhad kanálu a indikátor kombinace transportního formátu ([TFCI](/mobilnisite/slovnik/tfci/)) pro sekundární proud. TFCI informuje Node B o transportním formátu (např. datový tok, velikost bloku) použitém na odpovídajícím S-DPDCH, což je klíčové pro úspěšné zpracování dat.

Jeho provoz je přísně řízen signalizací vyšší vrstvy Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Síť konfiguruje UE pro používání S-DPCCH prostřednictvím specifických parametrů v konfiguraci fyzického kanálu. Přítomnost S-DPCCH umožňuje síti podporovat vyšší datové toky v uplinku a lepší spektrální účinnost tím, že umožňuje simultánní přenos dvou datových proudů (u MIMO) nebo agregaci kapacity ze dvou nosných (u DC-HSPA). Výkon kanálu je řízen vzhledem k primárnímu DPCCH pro udržení kvality spoje.

## K čemu slouží

S-DPCCH byl zaveden pro podporu pokročilých funkcí uplinku v [HSPA](/mobilnisite/slovnik/hspa/) Evolution (HSPA+), konkrétně uplink [MIMO](/mobilnisite/slovnik/mimo/) a Dual-Cell HSPA. Samotný primární [DPCCH](/mobilnisite/slovnik/dpcch/) mohl přenášet řídicí informace pouze pro jediný datový proud nebo nosnou. Pro využití více antén nebo více frekvenčních pásem za účelem vyšší propustnosti v uplinku byl potřebný samostatný řídicí kanál pro sekundární proud/nosnou, který by přenášel jeho nezbytné pilotní a formátové informace.

Toto řešilo klíčové omezení starších releasů HSPA, které se primárně zaměřovaly na vylepšení downlinku. Zavedení S-DPCCH umožnilo symetrické vysokorychlostní datové služby zvýšením kapacity uplinku. Vyřešilo problém efektivní signalizace parametrů druhého, paralelního datového přenosu bez přetížení nebo nutnosti přepracování primárního řídicího kanálu, čímž byla zajištěna zpětná kompatibilita a efektivní správa rádiových prostředků.

## Klíčové vlastnosti

- Přenáší pilotní bity pro odhad kanálu sekundárního proudu
- Přenáší TFCI pro přidružený sekundární DPDCH (S-DPDCH)
- Je aktivován konfigurací vyšší vrstvy RRC pro MIMO nebo vícekanálový provoz
- Je kódově multiplexován ve struktuře fyzické vrstvy uplinku
- Podporuje funkce pro zvýšení datového toku v uplinku, jako je DC-HSPA a MIMO
- Má vlastní řízení výkonu vzhledem k primárnímu DPCCH

## Související pojmy

- [DPDCH – Dedicated Physical Data Channel](/mobilnisite/slovnik/dpdch/)
- [DPDCH – Dedicated Physical Data Channel](/mobilnisite/slovnik/dpdch/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol

---

📖 **Anglický originál a plná specifikace:** [S-DPCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-dpcch/)
