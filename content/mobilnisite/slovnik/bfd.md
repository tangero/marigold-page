---
slug: "bfd"
url: "/mobilnisite/slovnik/bfd/"
type: "slovnik"
title: "BFD – Beam Failure Detection"
date: 2025-01-01
abbr: "BFD"
fullName: "Beam Failure Detection"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bfd/"
summary: "Beam Failure Detection (BFD) je mechanismus v NR, který sleduje kvalitu beamformovaných spojení mezi gNB a UE. Detekuje, kdy se servírující beam stane nespolehlivým, a spustí procedury obnovy pro zach"
---

BFD je mechanismus v 5G NR, který sleduje kvalitu beamu, aby detekoval, kdy se servírující beam stane nespolehlivým, a spustí procedury obnovy pro zachování konektivity.

## Popis

Beam Failure Detection (BFD) je základní procedura fyzické vrstvy v 5G New Radio (NR), která umožňuje uživatelskému zařízení (UE) sledovat kvalitu svého servírujícího beamu a detekovat, kdy se tento beam stane nespolehlivým nebo selže. Mechanismus funguje kontinuálním vyhodnocováním hypotetické blokové chybovosti ([BLER](/mobilnisite/slovnik/bler/)) přenosů na fyzickém downlinkovém řídicím kanálu ([PDCCH](/mobilnisite/slovnik/pdcch/)) přijímaných na specifických referenčních signálech. UE konfiguruje sadu zdrojů referenčního signálu pro detekci selhání beamu ([BFD-RS](/mobilnisite/slovnik/bfd-rs/)), která typicky sestává z bloků synchronizačního signálu (SSB) nebo referenčních signálů pro informace o stavu kanálu ([CSI-RS](/mobilnisite/slovnik/csi-rs/)), jež reprezentují kvalitu servírujícího beamu. UE měří kvalitu přijímaného signálu (např. pomocí [L1-RSRP](/mobilnisite/slovnik/l1-rsrp/)) na těchto zdrojích BFD-RS a porovnává ji s nastaveným prahem (Q_out). Instance selhání beamu je deklarována, když naměřená kvalita klesne pod tento práh. UE udržuje čítač detekce selhání beamu, který se zvyšuje s každou takovou instancí a resetuje se při úspěšném měření nad prahem. Když tento čítač dosáhne nastavené maximální hodnoty (beamFailureDetectionTimer), je deklarováno selhání beamu, což spustí proceduru obnovy po selhání beamu ([BFR](/mobilnisite/slovnik/bfr/)).

Architektura BFD zahrnuje koordinaci mezi fyzickou vrstvou (Layer 1) UE a vyššími vrstvami ([MAC](/mobilnisite/slovnik/mac/) a [RRC](/mobilnisite/slovnik/rrc/)). gNB konfiguruje parametry BFD prostřednictvím signalizace RRC, včetně sady zdrojů BFD-RS, prahu Q_out, časovače beamFailureDetectionTimer a parametru beamFailureInstanceMaxCount. Fyzická vrstva provádí kontinuální měření a hlásí instance selhání beamu vrstvě MAC, která spravuje čítač a časovač. Když je deklarováno selhání beamu, MAC iniciuje proceduru BFR spuštěním přenosu na náhodném přístupovém kanálu (RACH) na kandidátním beamu identifikovaném během fáze detekce. UE během BFD monitoruje referenční signály pro identifikaci kandidátního beamu (CBI-RS), aby identifikovalo alternativní beamy s dostatečnou kvalitou a připravilo se na rychlou obnovu.

BFD funguje ve spojení s dalšími procedurami správy beamů, jako je měření beamů, reportování beamů a přepínání beamů. Je obzvláště kritická pro provoz ve frekvenčním rozsahu 2 (FR2) nad 24 GHz, kde je úzké beamforming nutné pro překonání výrazných výzev v šíření. Detekční mechanismus musí vyvážit citlivost (pro rychlou detekci skutečných selhání) se stabilitou (aby se zabránilo falešným spuštěním od dočasného útlumu). Parametry BFD jsou typicky konfigurovány na základě scénářů nasazení, vzorců mobility a požadavků služby. Procedura podporuje provoz jak v připojeném režimu (RRC_CONNECTED), tak v neaktivním režimu (RRC_INACTIVE), s možností různých sad parametrů pro různé části přenosového pásma (BWP) a komponentové nosné.

Technická implementace zahrnuje specifické zpracování na fyzické vrstvě, kde UE vyhodnocuje hypotetickou BLER PDCCH na základě měření BFD-RS. To se počítá pomocí ustálených vztahů mezi kvalitou referenčního signálu a výkonem řídicího kanálu. Specifikace 3GPP definují podrobné požadavky na přesnost a včasnost BFD, včetně maximálních dob detekce a pravděpodobnosti falešného poplachu. BFD funguje spolu s monitorováním rádiového spoje (RLM), ale slouží jinému účelu: zatímco RLM sleduje celkové selhání rádiového spoje na úrovni buňky, BFD se konkrétně zabývá selháními na úrovni beamu uvnitř buňky. Toto rozlišení je zásadní v nasazeních s více beamy, kde jednotlivé beamy mohou selhat, zatímco jiné zůstávají použitelné, což umožňuje obnovu bez deklarace úplného selhání rádiového spoje.

## K čemu slouží

BFD bylo vytvořeno, aby řešilo základní výzvy komunikace na milimetrových vlnách (mmWave) v 5G NR, kde je směrový beamforming nezbytný kvůli vysokému útlumu na dráze a atmosférické absorpci. V tradičních systémech pod 6 GHz mohly všesměrové nebo širokopásmové přenosy udržet konektivitu i při degradaci signálu, ale mmWave systémy spoléhají na úzké beamy s vysokým ziskem, které mohou být snadno blokovány překážkami, lidskými těly nebo změnami prostředí. Bez rychlé detekce selhání beamu by mmWave spojení zažívala časté výpadky, což by je činilo nespolehlivými pro aplikace s kritickými požadavky. BFD umožňuje systému rychle identifikovat, kdy se servírující beam stane nepoužitelným, a spustit procedury obnovy dříve, než je spojení zcela ztraceno.

Technologie řeší omezení předchozích buněčných systémů, kterým chyběla sofistikovaná správa beamů. V LTE a starších technologiích se beamforming primárně používal pro zvýšení kapacity, nikoliv pro základní udržování konektivity. Tyto systémy používaly procedury selhání rádiového spoje (RLF), které fungovaly na úrovni buňky s relativně pomalými dobami detekce (stovky milisekund až sekundy). Pro mmWave s jeho rychlými změnami kanálu by takto pomalá detekce vedla k nepřijatelným přerušením služby. BFD poskytuje granularitu na úrovni beamu s dobami detekce v řádu desítek milisekund, což umožňuje rychlé přepínání beamů a zachování plynulé konektivity.

Historický kontext ukazuje, že koncepty správy beamů se vyvíjely napříč releasy 3GPP, přičemž Rel-15 zavedlo základní BFD pro počáteční nasazení 5G a následující releasy jej vylepšily pro složitější scénáře. Vytvoření BFD bylo motivováno potřebou učinit mmWave praktickými pro mobilní komunikaci, kde mobilita uživatelů a dynamika prostředí způsobují časté nezarovnání beamů. Detekcí selhání beamů včas a spuštěním odpovídajících akcí pro obnovu umožňuje BFD spolehlivost nezbytnou pro slibované use case 5G, jako je rozšířené mobilní širokopásmové připojení, ultra-spolehlivá komunikace s nízkou latencí a průmyslové IoT aplikace v náročných rádiových prostředích.

## Klíčové vlastnosti

- Kontinuální monitorování kvality servírujícího beamu pomocí konfigurovaných referenčních signálů
- Deklarace instance selhání beamu, když naměřená kvalita klesne pod práh Q_out
- Konfigurovatelný čítač a časovač detekce selhání beamu pro řízení stability
- Integrace s procedurou obnovy po selhání beamu (BFR) pro rychlou obnovu
- Podpora jak SSB, tak CSI-RS jako referenčních signálů pro detekci selhání beamu
- Provoz jak ve stavech RRC_CONNECTED, tak RRC_INACTIVE s odpovídající parametrizací

## Definující specifikace

- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 37.816** (Rel-16) — RAN-centric Data Collection & Utilization Study
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement

---

📖 **Anglický originál a plná specifikace:** [BFD na 3GPP Explorer](https://3gpp-explorer.com/glossary/bfd/)
