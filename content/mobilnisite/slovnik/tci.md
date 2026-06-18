---
slug: "tci"
url: "/mobilnisite/slovnik/tci/"
type: "slovnik"
title: "TCI – Transmission Configuration Indicator"
date: 2025-01-01
abbr: "TCI"
fullName: "Transmission Configuration Indicator"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tci/"
summary: "Indikátor používaný v 5G NR k signalizaci konkrétní sady parametrů pro přenos v downlinku směrem k UE. Odkazuje na předem nakonfigurovaný stav přenosové konfigurace (TCS) obsahující předpoklady QCL pr"
---

TCI je indikátor používaný v 5G NR k signalizaci konkrétní sady parametrů pro přenos v downlinku směrem k UE odkazem na předem nakonfigurovaný stav obsahující předpoklady QCL pro demodulaci.

## Popis

Transmission Configuration Indicator (TCI) je základní koncept ve fyzické vrstvě 5G New Radio (NR), konkrétně v rámci správy paprsků a kvazi-kolokace ([QCL](/mobilnisite/slovnik/qcl/)). Jedná se o index nebo identifikátor signalizovaný gNodeB (gNB) směrem k uživatelskému zařízení (UE) prostřednictvím downlink control information ([DCI](/mobilnisite/slovnik/dci/)) nebo signalizace vyšší vrstvy Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Tento indikátor odkazuje UE na konkrétní stav přenosové konfigurace (TCS), který byl předtím nakonfigurován pomocí RRC. Každý TCS obsahuje klíčové informace, především předpoklady kvazi-kolokace (QCL) mezi anténními porty různých referenčních signálů. V podstatě TCI říká UE, který referenční signál (např. konkrétní [CSI-RS](/mobilnisite/slovnik/csi-rs/) nebo [SS](/mobilnisite/slovnik/ss/)/[PBCH](/mobilnisite/slovnik/pbch/) blok) lze použít k odvození parametrů odhadu kanálu (jako je rozptyl zpoždění, rozptyl Dopplera, Dopplerův posuv, průměrné zpoždění a prostorové Rx parametry) pro demodulaci následného přenosu na physical downlink shared channel ([PDSCH](/mobilnisite/slovnik/pdsch/)) nebo physical downlink control channel ([PDCCH](/mobilnisite/slovnik/pdcch/)).

Z architektonického hlediska jsou stavy TCI konfigurovány na část šířky pásma (BWP) a jsou spravovány vrstvami Medium Access Control (MAC) a RRC v gNB. Proces zahrnuje několik kroků. Nejprve síť nakonfiguruje seznam stavů TCI pro UE pomocí RRC signalizace (dle 38.331). Každý stav TCI zahrnuje parametry spojující cílový referenční signál (jako DM-RS pro PDSCH) se zdrojovým referenčním signálem (jako CSI-RS) a specifikuje typ QCL vztahu (Typ A, B, C nebo D). Typ D je zvláště důležitý pro správu paprsků, protože indikuje podobnost prostorových Rx parametrů, což znamená, že UE může předpokládat, že stejný přijímací paprsek lze použít pro zdrojové i cílové signály. Když gNB naplánuje přenos PDSCH, zahrne pole TCI v DCI (formát 1_1 nebo 1_2), aby dynamicky indikoval, který z předkonfigurovaných stavů TCI se vztahuje na tento konkrétní přenos PDSCH. Pro PDCCH může být stav TCI indikován prostřednictvím MAC Control Element (MAC CE) pro indikaci paprsku řídicího kanálu.

Jak to funguje operativně: UE po přijetí DCI s indikátorem TCI vyhledá odpovídající stav TCI ze svého nakonfigurovaného seznamu. Poté aplikuje předpoklady QCL z tohoto stavu. Například, pokud stav TCI #3 indikuje, že porty DM-RS pro PDSCH jsou QCL Typ D s CSI-RS zdrojem #5, UE ví, že může použít stejná nastavení příjemového formování paprsku (prostorový filtr), která úspěšně použila pro příjem CSI-RS #5, když se pokusí demodulovat nadcházející PDSCH. To je zásadní v systému s formováním paprsků na mmWave nebo massive MIMO, kde je optimální směr paprsku úzký a musí být přesně zarovnán. Rámec TCI tedy odděluje podrobné postupy měření a reportování paprsků (zahrnující CSI-RS/SSB) od dynamického plánování dat, což umožňuje rychlé a efektivní přepínání paprsků bez nadměrné signalizační režie. Je to základní kámen pro spolehlivou vysokofrekvenční komunikaci a pokročilou vícepaprskovou operaci v 5G NR.

## K čemu slouží

TCI bylo vytvořeno k řešení kritické výzvy správy korespondence paprsků a informací o stavu kanálu v pokročilých anténních systémech, zejména pro 5G NR, které pracuje ve vysokofrekvenčních pásmech (včetně mmWave) a využívá massive MIMO. V těchto prostředích komunikace závisí na úzkých, směrových paprscích k překonání vysoké útlumové ztráty. Jádrem problému bylo, jak efektivně informovat UE, který paprsek (nebo přesněji, který prostorový přijímací filtr) má použít pro příjem naplánovaného downlink přenosu, zvláště když se paprsky mohou rychle měnit kvůli mobilitě nebo potřebám plánování. Předchozí systémy LTE měly jednodušší, méně dynamickou správu paprsků a postrádaly jednotný rámec pro indikaci prostorových vztahů napříč různými typy kanálů.

Omezení předchozích přístupů zahrnovala vysokou signalizační režii, pokud musely být informace o paprsku explicitně signalizovány pro každý přenos, a nedostatek flexibility ve spojování různých referenčních signálů. Koncept TCI to řeší zavedením vrstvy nepřímosti a předkonfigurace. Umožňuje síti předem nakonfigurovat sadu možných přenosových konfigurací (stavů TCI) pomocí polo-statické RRC signalizace. Poté během dynamického plánování potřebuje odeslat pouze krátký indikátor (několik bitů v DCI) k aktivaci jednoho z těchto stavů. To dramaticky snižuje režii a latenci řídicího kanálu, což je zásadní pro nízkolatencní use case 5G. Řeší problém efektivní správy prostorových QCL vztahů v dynamickém prostředí s formováním paprsků.

Dále TCI umožňuje pokročilé funkce jako operace s více TRP (Transmission Reception Point) a plánování s více paprsky. Konfigurací stavů TCI asociovaných s různými TRP nebo různými paprsky může síť rychle přepínat přijímací bod nebo paprsek UE pro zisk diverzity nebo kapacity. Vytvoření TCI bylo motivováno potřebou škálovatelného, flexibilního a efektivního rámce pro správu paprsků, který by mohl podporovat široké spektrum scénářů nasazení 5G, od sub-6 GHz po mmWave a od jednoho paprsku po komplexní vícepaprskové operace. Je to klíčový enabler pro výkonnostní a spolehlivostní sliby 5G NR.

## Klíčové vlastnosti

- Signalizuje předem nakonfigurovaný stav přenosové konfigurace (TCS) směrem k UE pro downlink přenos.
- Přenáší předpoklady kvazi-kolokace (QCL), klíčové pro odhad kanálu a zarovnání formování paprsků.
- Může být indikováno dynamicky prostřednictvím DCI pro PDSCH nebo prostřednictvím MAC CE pro PDCCH, což umožňuje rychlé přepínání paprsků.
- Podporuje více typů QCL (A, B, C, D), přičemž Typ D je klíčový pro indikaci prostorových Rx parametrů (paprsku).
- Konfigurováno na část šířky pásma (BWP) prostřednictvím RRC signalizace, což poskytuje flexibilitu a snižuje režii dynamické signalizace.
- Základní pro správu paprsků, operaci s více TRP a spolehlivý příjem v 5G NR MIMO/systémech s formováním paprsků.

## Související pojmy

- [QCL – Quasi Co-Location](/mobilnisite/slovnik/qcl/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.771** (Rel-19) — FR2-1 OTA Testing for STxMP UEs
- **TR 38.833** (Rel-17) — NR Demodulation Performance Enhancement
- **TR 38.878** (Rel-18) — Technical Report on Advanced Receiver for MU-MIMO

---

📖 **Anglický originál a plná specifikace:** [TCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tci/)
