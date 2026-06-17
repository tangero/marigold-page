---
slug: "rrc"
url: "/mobilnisite/slovnik/rrc/"
type: "slovnik"
title: "RRC – Radio Resource Control"
date: 2025-01-01
abbr: "RRC"
fullName: "Radio Resource Control"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rrc/"
summary: "Protokol Řízení rádiových zdrojů (RRC) je signalizační protokol vrstvy 3 na rádiovém rozhraní mezi UE a sítí (gNB/eNB/NodeB). Je zodpovědný za zřizování, konfiguraci, údržbu a uvolňování rádiových pře"
---

RRC je signalizační protokol vrstvy 3 mezi uživatelským zařízením a sítí, který zřizuje, konfiguruje, udržuje a uvolňuje rádiové přenosové kanály (radio bearers) a zároveň řídí funkce správy rádiových zdrojů a mobility na nižších vrstvách.

## Popis

Protokol Řízení rádiových zdrojů (RRC) je klíčovou součástí řídicí roviny v 3GPP rádiových přístupových sítích (UTRAN, E-UTRAN, NG-RAN). Funguje mezi uživatelským zařízením (UE) a uzlem rádiové přístupové sítě (Node B, eNodeB nebo gNodeB). Vrstva RRC je zodpovědná za zřizování, konfiguraci, údržbu a uvolňování signalizačních rádiových přenosových kanálů (SRBs) a datových rádiových přenosových kanálů (DRBs), které přenášejí řídicí a uživatelská data. Spravuje stavy připojení UE, především stavy IDLE a CONNECTED (s podstavy jako RRC_IDLE, RRC_INACTIVE a RRC_CONNECTED v 5G NR), které určují míru povědomí sítě o zařízení a přidělování zdrojů.

RRC funguje prostřednictvím řady procedur iniciovaných sítí nebo UE. Mezi klíčové procedury patří Zřízení RRC připojení, Aktivace zabezpečení, Nastavení/Reconfigurace rádiových přenosových kanálů, Předání spojení (Handover), Konfigurace měření a hlášení výsledků a Rozesílání systémových informací. Protokol přenáší klíčové konfigurační zprávy, které definují činnost nižších vrstev (PDCP, RLC, MAC a PHY). Například zpráva RRC Reconfiguration může přikázat UE použít nové šifrovací algoritmy, upravit priority logických kanálů, přidat nebo odebrat komponenty agregace nosných nebo se připravit na předání spojení do nové buňky.

Z architektonického hlediska jsou zprávy RRC přenášeny přes signalizační rádiové přenosové kanály (SRBs). V LTE a NR se SRB0 používá pro kontenční (contention-based) počáteční přístup (pomocí logického kanálu CCCH), SRB1 pro RRC zprávy (a volitelně i NAS zprávy) před zřízením SRB2 a SRB2 je vyhrazen pro NAS zprávy. Protokol je inherentně asymetrický, přičemž řídicí roli má síť. Zajišťuje, že UE pracuje v rámci parametrů nastavených sítí pro efektivitu využití rádiových zdrojů, správu rušení, robustnost mobility a plnění kvality služeb. Jeho návrh je vysoce parametrizovaný, aby podporoval širokou škálu služeb od hromadného IoT po ultra-spolehlivé komunikace s nízkou latencí.

## K čemu slouží

Protokol RRC byl vytvořen, aby poskytl centralizovaný, robustní a flexibilní mechanismus pro řízení všech funkcí specifických pro rádiové rozhraní spojení mobilního zařízení se sítí. Před jeho standardizací v 3GPP bylo řídicí signalizace méně strukturované. RRC poskytuje jednotný rámec pro správu připojení, mobility a řízení rádiových přenosových kanálů, který je zásadní pro efektivní využití spektra a poskytování služeb v celulárních sítích. Řeší problém, jak dynamicky spravovat sdílený rádiový zdroj náchylný k rušení mezi miliony zařízení s různými požadavky na služby.

K jeho vytvoření vedla potřeba sofistikované řídicí roviny pro podporu paketově orientovaných služeb a pokročilých funkcí zavedených v 3G UMTS a novějších systémech, jako jsou proměnné datové rychlosti, diferenciace kvality služeb a plynulá mobilita. RRC abstrahuje složitost fyzické a spojové vrstvy a poskytuje síti přímý prostředek k ovládání a konfiguraci rádiového chování UE. To umožňuje optimalizovaný výkon sítě, rychlou adaptaci na měnící se rádiové podmínky a zavádění nových funkcí prostřednictvím softwarových aktualizací specifikace protokolu RRC bez nutnosti přepracování celé architektury rádiového rozhraní.

## Klíčové vlastnosti

- Správa stavů připojení (IDLE, CONNECTED, INACTIVE)
- Rozesílání systémových informací (MIB, SIBs)
- Zřizování, modifikace a uvolňování rádiových přenosových kanálů
- Aktivace zabezpečení (šifrování a ochrana integrity)
- Řízení mobility (předání spojení, parametry převýběru buňky)
- Konfigurace měření a hlášení výsledků pro rádiové podmínky

## Definující specifikace

- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- … a dalších 98 specifikací

---

📖 **Anglický originál a plná specifikace:** [RRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rrc/)
