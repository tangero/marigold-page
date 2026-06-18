---
slug: "cc"
url: "/mobilnisite/slovnik/cc/"
type: "slovnik"
title: "CC – Component Carrier"
date: 2025-01-01
abbr: "CC"
fullName: "Component Carrier"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cc/"
summary: "Component Carrier (CC) je základní stavební prvek agregace nosných v 3GPP LTE a NR. Jedná se o samostatný souvislý blok spektra s vlastní konfigurací fyzické vrstvy. Více CC lze agregovat za vzniku ši"
---

CC (Component Carrier) je základní souvislý blok spektra v LTE a NR, který slouží jako samostatný stavební prvek pro agregaci nosných, což při kombinaci více takových bloků umožňuje širší přenosové pásmo a vyšší datové rychlosti.

## Popis

Component Carrier (CC) je definován jako jediný souvislý blok rádiového spektra s konkrétní nosnou frekvencí a šířkou pásma, fungující jako nezávislá entita fyzické vrstvy. V kontextu standardů 3GPP, zejména od LTE-Advanced (Rel-10) výše, jsou CC základní jednotky, které se agregují za účelem zvýšení celkového přenosového pásma dostupného uživatelskému zařízení (UE). Každý CC má svou vlastní kompletní sadu fyzických kanálů (např. [PDSCH](/mobilnisite/slovnik/pdsch/), [PUSCH](/mobilnisite/slovnik/pusch/), [PDCCH](/mobilnisite/slovnik/pdcch/)), synchronizačních signálů a buněčně specifických referenčních signálů. Lze jej nakonfigurovat se standardními šířkami pásma (např. 1,4, 3, 5, 10, 15, 20 MHz v LTE; až 100 MHz v NR) a pracuje s konkrétní numerologií (rozteč podnosných, cyklická předpona).

V konfiguraci agregace nosných ([CA](/mobilnisite/slovnik/ca/)) je UE připojeno k primární buňce (PCell) ukotvené na primárním komponentním nosném ([PCC](/mobilnisite/slovnik/pcc/)) a k jedné nebo více sekundárním buňkám (SCell) na sekundárních komponentních nosných ([SCC](/mobilnisite/slovnik/scc/)). PCC zajišťuje kritické řídicí funkce, jako je spojení řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)), informace o mobilitě neaccess stratum ([NAS](/mobilnisite/slovnik/nas/)) a aktivace zabezpečení. SCC se primárně používají k poskytnutí dodatečného pásma pro přenos dat uživatelské roviny a lze je dynamicky aktivovat nebo deaktivovat na základě poptávky po provozu. Agregace může být vnitropásmová (CC ve stejném kmitočtovém pásmu) nebo mezipásmová (CC napříč různými kmitočtovými pásmy), a to se souvislým nebo nesouvislým spektrem.

Síť CC spravuje pomocí signalizace RRC. eNB/gNB nakonfiguruje UE sadou obsluhujících buněk, z nichž každá odpovídá jednomu CC. Nařízení napříč nosnými umožňuje, aby řídicí informace pro přenos dat na jednom CC byly odesílány na PDCCH jiného CC, což poskytuje flexibilitu plánování a koordinaci rušení. Pro uplink může UE vysílat na více CC současně při dodržení omezení maximálního výkonu a spektrálních emisí. Zpracování fyzické vrstvy, včetně kódování, modulace a mapování prostředků, se provádí pro každý CC zvlášť, než jsou signály před vysíláním zkombinovány nebo po příjmu odděleny.

CC jsou klíčové pro využití fragmentovaných spektrálních aktiv. Operátoři mohou kombinovat licencované bloky spektra z různých pásem (např. nízkopásmové pro pokrytí a střední/vysokopásmové pro kapacitu) do jediného logického přenosového kanálu. Tato architektura je zpětně kompatibilní; UE Rel-10+ s podporou CA může agregovat CC, zatímco starší UE Rel-8 může obsadit a používat jediný CC jako samostatnou nosnou. V 5G NR se tento koncept rozšiřuje na širší pásma a flexibilnější numerologie a podporuje agregaci CC s různými roztečemi podnosných v rámci stejného nebo napříč různými kmitočtovými rozsahy (FR1 a FR2).

## K čemu slouží

Koncept Component Carrier byl zaveden primárně za účelem překonání omezení maximální šířky kanálu definované v jedné generaci rádiového přístupové technologie. V LTE Rel-8/9 byla maximální šířka kanálu omezena na 20 MHz, což limitovalo špičkové datové rychlosti dosažitelné jediným UE. S rostoucí poptávkou uživatelů po mobilním širokopásmovém připojení bylo zapotřebí metody, jak tento limit šířky pásma překonat, aniž by bylo nutné navrhnout zcela nové nekompatibilní rozhraní. Agregace nosných, postavená na CC, byla řešením standardizovaným v LTE-Advanced (Rel-10). Umožňuje systému splnit požadavky IMT-Advanced na špičkové datové rychlosti (např. 1 Gbps pro downlink) agregací více 20MHz nosných.

CC dále řeší praktický problém fragmentovaných spektrálních držav. Operátoři mobilních sítí jen zřídka disponují velkými souvislými bloky spektra. Místo toho vlastní několik menších bloků v různých kmitočtových pásmech získaných v aukcích nebo přebudováním. Model CC mění tuto fragmentaci ze slabiny v přednost. Umožňuje operátorům sdružovat tyto rozdílné spektrální zdroje a vytvářet tak virtuální širší kanál. To zlepšuje celkovou kapacitu sítě, spektrální účinnost a uživatelský zážitek. Poskytuje také pozvolnou migrační cestu, která umožňuje novým zařízením s podporou širšího pásma těžit z agregace, zatímco starší zařízení mohou nadále pracovat na jediném CC.

Evoluce do 5G NR dále využila koncept CC k podpoře neuvěřitelně rozmanité škály případů užití a typů spektra. NR definuje mnohem širší šířky pásma CC (až 100 MHz v pásmu pod 6 GHz a 400 MHz v mmWave) a umožňuje agregaci CC s různými numerologiemi (např. kombinace nosných s roztečí podnosných 15 kHz a 30 kHz). Tato flexibilita je zásadní pro efektivní podporu rozšířeného mobilního širokopásmového připojení (eMBB), ultra-spolehlivé nízkolatenční komunikace (URLLC) a komunikace s hromadnými strojovými zařízeními (mMTC) napříč nízkým, středním a vysokým pásmem spektra.

## Klíčové vlastnosti

- Základní jednotka šířky pásma pro agregaci nosných (CA)
- Lze konfigurovat se standardními šířkami pásma a nezávislými numerologiemi
- Podporuje vnitropásmovou i mezipásmovou agregaci, souvislou i nesouvislou
- Jeden primární CC (PCC) pro řízení a více sekundárních CC (SCC) pro data
- Umožňuje nařízení napříč nosnými pro flexibilní řízení prostředků
- Zpětně kompatibilní, umožňuje starším UE pracovat na jediném CC

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.796** (Rel-16) — FRMCS Architectural Analysis
- **TS 24.642** (Rel-19) — CCBS/CCNR/CCNL SIP Protocol Specification
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- … a dalších 86 specifikací

---

📖 **Anglický originál a plná specifikace:** [CC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cc/)
