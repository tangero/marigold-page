---
slug: "sc-mcch"
url: "/mobilnisite/slovnik/sc-mcch/"
type: "slovnik"
title: "SC-MCCH – Single Cell Multicast Control Channel"
date: 2025-01-01
abbr: "SC-MCCH"
fullName: "Single Cell Multicast Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sc-mcch/"
summary: "SC-MCCH je logický kanál v LTE, který přenáší řídicí informace pro přenosy typu Single Cell Point-to-Multipoint (SC-PTM). Informuje uživatelská zařízení (UE) o konfiguraci a plánování multicastových k"
---

SC-MCCH je logický kanál v LTE, který přenáší řídicí informace pro přenos typu Single Cell Point-to-Multipoint (SC-PTM) a informuje uživatelská zařízení (UE) o konfiguraci a plánování přidružených multicastových kanálů pro přenos dat.

## Popis

Single Cell Multicast Control Channel (SC-MCCH) je downlinkový logický kanál definovaný v rámci LTE rádiové přístupové sítě pro funkci Single Cell Point-to-Multipoint ([SC-PTM](/mobilnisite/slovnik/sc-ptm/)). Funguje jako řídicí rovina pro SC-PTM, obdobně jako kanál [BCCH](/mobilnisite/slovnik/bcch/) (Broadcast Control Channel) funguje pro systémové informace v celé buňce. eNodeB používá SC-MCCH k vysílání základních konfiguračních a plánovacích informací všem uživatelským zařízením (UE) v buňce, která mají zájem přijímat služby SC-PTM. Tyto informace jsou klíčové pro to, aby UE mohla úspěšně lokalizovat, demodulovat a dekódovat skutečná multicastová data přenášená na přidružených kanálech Single Cell Multicast Traffic Channel ([SC-MTCH](/mobilnisite/slovnik/sc-mtch/)).

Z architektonického hlediska je SC-MCCH logický kanál mapovaný na transportní kanál Downlink Shared Channel ([DL-SCH](/mobilnisite/slovnik/dl-sch/)), který je následně přenášen na Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)). Je dynamicky plánován eNodeB, ale jeho plánování sleduje specifický opakovací vzor definovaný systémovými informacemi, aby bylo zajištěno, že jej UE mohou efektivně nalézt bez nutnosti nepřetržitého sledování. Obsah SC-MCCH je definován v [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control) zprávách, konkrétně ve zprávě SC-MCCH. Tato zpráva obsahuje seznam služeb SC-PTM (identifikovaných pomocí Group Radio Network Temporary Identifiers - G-RNTIs), které jsou v buňce aktuálně aktivní, spolu s podrobnou konfigurací pro každý odpovídající SC-MTCH, jako je modulační a kódovací schéma, periodicita a plánovací informace.

Funguje tak, že UE nejprve získá standardní systémové informace buňky ([SIB](/mobilnisite/slovnik/sib/)). Konkrétní System Information Block (SIB 20) poskytuje nezbytné parametry pro příjem SC-MCCH, včetně jeho plánovací periody, periody opakování a přidělení prostředků PDSCH. UE poté v indikovaných časech sleduje PDSCH, aby přijala zprávu SC-MCCH. Po jejím dekódování může UE identifikovat, zda je vysílána multicastová služba, o kterou má zájem (např. varování pro veřejnou bezpečnost, stream mobilní [TV](/mobilnisite/slovnik/tv/)). Pokud je služba přítomna, UE extrahuje konfiguraci SC-MTCH pro tuto službu a začne sledovat naplánované prostředky PDSCH, aby přijímala multicastová data. SC-MCCH může být aktualizován při spuštění nebo zastavení služeb a UE jej periodicky znovu získávají na základě modifikační periody, aby zůstala synchronizovaná.

## K čemu slouží

SC-MCCH byl vytvořen pro podporu efektivního doručování multicastových služeb v rámci jedné LTE buňky, což je funkce známá jako Single Cell Point-to-Multipoint (SC-PTM). Před SC-PTM nabízelo LTE vysílání/multicast primárně prostřednictvím eMBMS (evolved Multimedia Broadcast Multicast Service), což vyžadovalo synchronizovanou vícebuňkovou architekturu MBSFN (Multicast Broadcast Single Frequency Network). MBSFN je složitý na nasazení a správu, vhodný pro rozsáhlou distribuci obsahu, ale nepřiměřeně komplikovaný pro lokalizované nebo dynamické multicastové potřeby, jako je komunikace pro veřejnou bezpečnost v konkrétní oblasti nebo cílená reklama na stadionu.

Účelem SC-MCCH je poskytnout odlehčený, na buňku lokalizovaný řídicí mechanismus pro tyto jednodušší multicastové scénáře. Řeší problém, jak dynamicky informovat potenciálně velkou skupinu UE v rámci jedné buňky o dostupnosti a konfiguraci multicastových služeb bez nutnosti vytvářet individuální unicastová spojení pro signalizaci řízení. To je zásadní pro škálovatelnost a efektivitu sítě při obsluze mnoha uživatelů stejným obsahem.

Motivováno případy užití, jako je skupinová zpráva IoT, veřejná bezpečnost a lokalizovaná média, SC-PTM a jeho řídicí kanál SC-MCCH zaplňují mezeru mezi čistým unicastem (neefektivní pro skupinová data) a plnohodnotným eMBMS (komplexní pro nasazení v jedné buňce). Umožňuje operátorovi nebo poskytovateli služeb rychle nasadit multicastovou službu v konkrétní geografické oblasti (jedné buňce) s minimální konfigurací sítě, s využitím stávající infrastruktury sdíleného kanálu (PDSCH). SC-MCCH je klíčovým prvkem, který umožňuje toto dynamické, na buňku specifické zjišťování a konfiguraci multicastových služeb.

## Klíčové vlastnosti

- Přenáší RRC konfigurační zprávy pro služby SC-PTM
- Je dynamicky plánován na PDSCH, ale s definovanou periodicitou
- Poskytuje seznam aktivních služeb SC-PTM a jejich přidružených G-RNTI
- Obsahuje podrobnou konfiguraci fyzické vrstvy pro každý SC-MTCH
- Umožňuje efektivní zjišťování a získávání multicastových služeb UE v rámci buňky
- Funguje nezávisle na každé buňce, bez nutnosti synchronizace MBSFN

## Související pojmy

- [SC-PTM – Single-Cell Point-to-Multipoint](/mobilnisite/slovnik/sc-ptm/)
- [SC-MTCH – Single Cell Multicast Transport Channel](/mobilnisite/slovnik/sc-mtch/)
- [G-RNTI – GERAN Radio Network Temporary Identity](/mobilnisite/slovnik/g-rnti/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [SIB – System Information Block](/mobilnisite/slovnik/sib/)
- [DL-SCH – Downlink Shared Channel](/mobilnisite/slovnik/dl-sch/)

## Definující specifikace

- **TS 23.792** (Rel-16) — MBMS API for Mission Critical Services
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SC-MCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sc-mcch/)
