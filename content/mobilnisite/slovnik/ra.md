---
slug: "ra"
url: "/mobilnisite/slovnik/ra/"
type: "slovnik"
title: "RA – Rate Adaptation Functions"
date: 2026-01-01
abbr: "RA"
fullName: "Rate Adaptation Functions"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ra/"
summary: "Funkce adaptace rychlosti (Rate Adaptation Functions) dynamicky upravují rychlost přenosu dat přes bezdrátový spoj na základě stavu přenosového kanálu. Tím je zajištěno efektivní využití spektra a udr"
---

RA je funkce, která dynamicky upravuje rychlost přenosu dat přes bezdrátový spoj na základě stavu přenosového kanálu, aby zajistila efektivní využití spektra a spolehlivost spojení.

## Popis

Funkce adaptace rychlosti (RA) jsou souborem algoritmů a protokolů v systémech 3GPP navržených k optimalizaci přenosu dat dynamickou úpravou datové rychlosti. Tato adaptace probíhá v reakci na měření stavu rádiového kanálu v reálném čase, jako je poměr signálu k šumu ([SNR](/mobilnisite/slovnik/snr/)), míra bitových chyb ([BER](/mobilnisite/slovnik/ber/)) a dostupná šířka pásma. Základním principem je výběr nejefektivnějšího modulačního a kódového schématu ([MCS](/mobilnisite/slovnik/mcs/)), které aktuální kanál spolehlivě podporuje, čímž se maximalizuje propustnost při minimalizaci ztráty paketů a retransmisí. Tyto funkce jsou implementovány napříč více vrstvami a síťovými elementy a zahrnují úzkou interakci mezi uživatelským zařízením (UE), rádiovou přístupovou sítí (RAN) a entitami core sítě pro rozhodování a konfiguraci parametrů.

Z architektonického hlediska jsou RA funkce distribuované. Ve UE a základnové stanici (např. NodeB, [eNB](/mobilnisite/slovnik/enb/), gNB) měření fyzické vrstvy průběžně vyhodnocují kvalitu kanálu. Tyto informace jsou hlášeny vyšším vrstvám a často i řídicí jednotce RAN. Na základě těchto hlášení a dalších faktorů, jako je zatížení sítě a požadavky QoS, RAN rozhodne o vhodné datové rychlosti. Adaptace může být rychlá, probíhající v rámci každého přenosového časového intervalu ([TTI](/mobilnisite/slovnik/tti/)) pro adaptaci spoje, nebo pomalejší, pro strategičtější alokaci zdrojů. Mezi klíčové zapojené komponenty patří mechanismus hlášení indikátoru kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), protokol hybridního automatického opakovaného dotazu ([HARQ](/mobilnisite/slovnik/harq/)) pro opravu chyb a plánovací algoritmy v základnové stanici.

Role RA je klíčová pro spektrální efektivitu a kontinuitu služeb. Umožňuje síti plynule snížit výkon při špatných podmínkách (např. na okraji buňky) namísto přerušení spojení a agresivně zvýšit rychlosti při výborných podmínkách. To je zásadní pro podporu různorodých služeb s odlišnými požadavky na QoS, od hlasových hovorů vyžadujících konzistentní nízké zpoždění až po přerušované datové relace s vysokou propustností. Funkce pokrývají jak okruhově, tak paketově komutovanou doménu, adaptují rychlosti pro vyhrazené kanály i sdílené kanály v technologiích [HSPA](/mobilnisite/slovnik/hspa/), LTE a NR.

## K čemu slouží

Funkce adaptace rychlosti (RA) byly vytvořeny, aby řešily základní výzvu časově proměnlivé a nepředvídatelné povahy bezdrátového rádiového kanálu. Rané digitální mobilní systémy používaly pevné datové rychlosti, které byly neefektivní – buď plýtvaly kapacitou za dobrých podmínek, nebo selhávaly za špatných podmínek. Primární problém, který RA řeší, je maximalizace spolehlivé datové propustnosti a síťové kapacity navzdory útlumu, interferencím a útlumu signálu souvisejícímu se vzdáleností.

Historicky zavedení RA v 3GPP Release 99 (a jeho základní práce v GSM EDGE) představovalo posun od okruhově komutovaných služeb s konstantní rychlostí k efektivním paketově komutovaným datům. Umožnilo technologie High-Speed Packet Access (HSPA), kde je dynamická adaptace rychlosti základním kamenem. Bez RA by sítě byly buď předimenzované pro nejhorší případ (plýtvání zdroji), nebo by poskytovaly špatný uživatelský komfort s častými přerušeními spojení. RA umožňuje síti 'surfovat na vlnách' kvality kanálu a extrahovat maximální možnou datovou rychlost v každém okamžiku.

RA je navíc klíčová pro podporu mixu služeb v moderních sítích. Poskytuje základní mechanismus pro diferenciaci QoS; vysokoprioritní video stream může být alokován s robustnějším (nižšího řádu) MCS, aby byla zajištěna kontinuita, zatímco stahování na pozadí může používat MCS vyššího řádu a méně robustní, když to podmínky dovolují. Tato flexibilita je klíčová pro efektivní správu rádiových zdrojů a naplnění různorodých uživatelských očekávání na sdíleném, omezeném spektru.

## Klíčové vlastnosti

- Dynamický výběr modulačního a kódového schématu (MCS) na základě indikátorů kvality kanálu (CQI) v reálném čase
- Integrace s hybridním ARQ (HARQ) pro rychlé zotavení po chybě a inkrementální redundanci
- Podpora adaptace rychlosti pro uplink i downlink napříč různými typy kanálů (vyhrazené, sdílené)
- Interakce s algoritmy pro plánování paketů v základnové stanici pro alokaci zdrojů
- Zohlednění identifikátorů třídy QoS (QCIs) a zatížení sítě při rozhodování o rychlosti
- Vývoj pro podporu scénářů agregace nosných a multi-konektivity pro kombinované řízení rychlosti

## Související pojmy

- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [MCS – Modulation and Coding Schemes](/mobilnisite/slovnik/mcs/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.202** (Rel-19) — CS Bearer Services Architecture in UMTS
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- … a dalších 21 specifikací

---

📖 **Anglický originál a plná specifikace:** [RA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ra/)
