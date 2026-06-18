---
slug: "mer"
url: "/mobilnisite/slovnik/mer/"
type: "slovnik"
title: "MER – Message Error Ratio"
date: 2025-01-01
abbr: "MER"
fullName: "Message Error Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mer/"
summary: "Message Error Ratio (MER) je klíčový výkonnostní ukazatel měřící podíl chybně přijatých transportních bloků nebo datových paketů přes rádiové rozhraní. Je zásadní pro hodnocení a optimalizaci kvality"
---

MER je podíl chybně přijatých transportních bloků nebo datových paketů přes rádiové rozhraní. Používá se k posouzení kvality a spolehlivosti přenosu dat na fyzické vrstvě.

## Popis

Message Error Ratio (MER) je základním výkonnostním měřením v digitálních komunikačních systémech, standardizovaným v rámci 3GPP pro UMTS, LTE a NR. Kvantifikuje spolehlivost přenosu datových paketů přes rozhraní vzduchu. Technicky je MER definován jako poměr počtu chybně přijatých transportních bloků (nebo v některých kontextech kódových bloků) k celkovému počtu vyslaných transportních bloků, měřený za určité pozorovací období. Transportní blok je základní jednotka dat předávaná z [MAC](/mobilnisite/slovnik/mac/) vrstvy na fyzickou vrstvu pro přenos. Chyba je zaznamenána, pokud kontrolní součet [CRC](/mobilnisite/slovnik/crc/) (Cyclic Redundancy Check) připojený k transportnímu bloku na fyzické vrstvě selže na přijímací straně po aplikaci veškeré opravy chyb (např. Turbo nebo [LDPC](/mobilnisite/slovnik/ldpc/) dekódování).

Fungování MER je vnitřně propojeno s řetězcem zpracování na fyzické vrstvě. Na vysílači je vygenerován transportní blok, pro detekci chyb je připojen CRC, a následně blok prochází kanálovým kódováním (přidání redundance), přizpůsobením rychlosti, modulací a mapováním na fyzické zdroje. Na přijímači je proces obrácený: demodulace, dekódování a nakonec kontrola CRC. Měření MER probíhá po fázi dekódování. Síťová infrastruktura, zejména základnová stanice (NodeB, [eNB](/mobilnisite/slovnik/enb/), gNB) a uživatelské zařízení (UE), neustále počítají MER pro aktivní spojení. To se děje počítáním selhání CRC na uplinku (na základnové stanici) a downlinku (na UE), často hlášených prostřednictvím měřicích reportů jako je Channel Quality Indicator ([CQI](/mobilnisite/slovnik/cqi/)) nebo přímějších měření na první vrstvě.

Jeho role v síti je klíčová pro adaptaci spojení a správu rádiových zdrojů. Vysoká hodnota MER indikuje špatné podmínky na kanále (např. nízký [SNR](/mobilnisite/slovnik/snr/), vysoké rušení). Vrstva Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a plánovač tuto informaci používají k dynamickému přizpůsobení přenosových parametrů. Například, pokud je downlink MER hlášený UE vysoký, gNB může přejít na robustnější modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)), zvýšit výkon vysílání nebo alokovat více zdrojů (např. využít frekvenční diverzitu). Naopak nízká hodnota MER umožňuje použití modulace vyššího řádu (jako 256QAM nebo 1024QAM) pro vyšší spektrální účinnost. MER je tedy přímým vstupem pro algoritmy, které vyvažují propustnost a spolehlivost, což z něj činí základní metriku pro udržení Quality of Service (QoS) a optimalizaci celkové kapacity sítě.

## K čemu slouží

MER existuje jako standardizovaná, jednoznačná metrika pro měření základního výkonu digitálního rádiového spoje. Než lze uvažovat o sofistikovanějších metrikách, jako je propustnost nebo latence, musí být zajištěna základní integrita přenášených dat. V raných digitálních celulárních systémech (jako GSM) byl běžnou metrikou Bit Error Rate (BER). Jak se však systémy vyvíjely směrem k paketovému přenosu s výkonným kanálovým kódováním (Turbo kódy v UMTS/LTE, LDPC v NR), účinnost spoje je lépe měřitelná na úrovni paketu/transportního bloku po dekódování. MER přímo odráží pravděpodobnost, že datový paket uživatele je přijat chybně, což je konečný zájem protokolů vyšších vrstev (které by následně spustily retransmise prostřednictvím HARQ).

Jeho vytvoření a standardizace napříč releasy zajišťují konzistentní hodnocení výkonu pro testování shody zařízení, optimalizaci nasazení sítě a odstraňování problémů. Inženýři používají MER jako referenční bod pro citlivost přijímače, hodnocení výkonu nových modulačních schémat a ověření účinnosti MIMO a dalších pokročilých anténních technik. Odstraňuje omezení jednodušších metrik, jako je Received Signal Strength Indicator (RSSI) nebo Signal-to-Noise Ratio (SNR), které sice indikují podmínky na kanále, ale přímo neodhalují výsledný výkon po komplexním zpracování moderní fyzické vrstvy. MER poskytuje toto přímé, na aplikaci relevantní měřítko úspěchu nebo neúspěchu pro každou jednotku dat.

## Klíčové vlastnosti

- Definován jako poměr chybných transportních bloků k celkovému počtu vyslaných bloků.
- Měřen po dekódování kanálu na fyzické vrstvě a kontrole CRC.
- Základní vstup pro adaptaci spojení a výběr MCS.
- Používán v testech shody pro přijímače UE a základnových stanic.
- Hlášen jak uživatelským zařízením (UE) pro downlink, tak sítí pro uplink.
- Aplikovatelný napříč více 3GPP technologiemi (UTRA, E-UTRA, NR).

## Související pojmy

- [BLER – Block Error Rate](/mobilnisite/slovnik/bler/)
- [CRC – Cyclic Redundancy Check](/mobilnisite/slovnik/crc/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [MER na 3GPP Explorer](https://3gpp-explorer.com/glossary/mer/)
