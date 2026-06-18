---
slug: "sealdd"
url: "/mobilnisite/slovnik/sealdd/"
type: "slovnik"
title: "SEALDD – Service Enabler Architecture Layer – Data Delivery"
date: 2026-01-01
abbr: "SEALDD"
fullName: "Service Enabler Architecture Layer – Data Delivery"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sealdd/"
summary: "SEALDD je funkční komponenta v rámci architektury SEAL, která poskytuje optimalizované, aplikací řízené služby doručování dat pro vertikály. Zajišťuje směrování dat, ukládání do mezipaměti, překódován"
---

SEALDD je funkční komponenta v rámci architektury SEAL (Service Enabler Architecture Layer), která poskytuje optimalizované, aplikací řízené služby doručování dat, zajišťující směrování, ukládání do mezipaměti, překódování a distribuci pro vertikály jako V2X a IoT.

## Popis

Service Enabler Architecture Layer – Data Delivery (SEALDD) je specializovaná funkce zavedená jako součást širší architektury [SEAL](/mobilnisite/slovnik/seal/) ve specifikaci 3GPP Release 18. Jejím hlavním úkolem je řídit a optimalizovat doručování dat mezi vertikálními aplikacemi a skupinami uživatelských zařízení (UE) nebo mezi samotnými UE. SEALDD funguje jako inteligentní agent datové roviny, který rozumí kontextu aplikace a stavu sítě. Mezi klíčové architektonické komponenty patří logika směrování dat, možnosti ukládání do mezipaměti, funkce pro překódování/adaptaci a rozhraní pro správu skupin. Funguje tak, že přijímá požadavky na doručení dat od vertikální aplikace prostřednictvím severozápadního [API](/mobilnisite/slovnik/api/) SEAL. Tyto požadavky specifikují parametry, jako je cílová skupina (definovaná pomocí služby SEAL Group Management), priorita dat, požadovaná latence a geografická oblast. SEALDD poté určí nejefektivnější strategii doručení, která může zahrnovat mechanismy unicast, multicast nebo broadcast, případně s využitím služeb 5G Multicast-Broadcast Services ([MBS](/mobilnisite/slovnik/mbs/)). Může ukládat oblíbený obsah na okraji sítě, aby snížila latenci a zatížení páteřní sítě. Například ve scénáři [V2X](/mobilnisite/slovnik/v2x/) může SEALDD efektivně distribuovat aktualizace map ve vysokém rozlišení všem vozidlům v konkrétní městské čtvrti. Spolupracuje s dalšími službami SEAL (pro informace o skupině a poloze) a s funkcemi jádra sítě, jako je Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), aby provedla doručení. Její provoz zahrnuje uplatňování příslušných politik pro kvalitu služeb (QoS), zabezpečení a účtování. Tím, že abstrahuje tyto složité mechanismy doručování dat, umožňuje SEALDD vertikálním aplikacím požadovat sofistikovanou distribuci dat bez nutnosti spravovat podrobnosti podkladového síťového přenosu.

## K čemu slouží

SEALDD byla vytvořena, aby řešila konkrétní výzvy spojené s doručováním dat, kterým čelí vertikální aplikace v 5G a dalších sítích. Před jejím zavedením, zatímco [SEAL](/mobilnisite/slovnik/seal/) poskytovala služby pro správu, efektivní, škálovatelná a kontextově řízená distribuce dat nebyla plně standardizována. Vertikály, jako jsou propojená vozidla ([V2X](/mobilnisite/slovnik/v2x/)), roje dronů a rozsáhlá nasazení IoT, vyžadují efektivní skupinovou komunikaci, nízkolatenční doručování dat a adaptivní doručování obsahu na základě polohy nebo stavu sítě. Implementace těchto funkcí ad-hoc byla složitá a neefektivní. Účelem SEALDD je tuto mezeru zaplnit poskytnutím standardizované, síťově integrované služby doručování dat v rámci ekosystému SEAL. Řeší problémy, jako je zahlcení sítě redundantními unicastovými toky, vysoká latence pro okrajové služby a složitost přímého používání služeb multicast/broadcast. Tím, že nabízí aplikací řízené doručování dat jako službu, umožňuje SEALDD vertikálám vytvářet škálovatelné datově náročné aplikace, optimalizuje využití síťových zdrojů a je klíčovým prvkem pro pokročilé případy použití 5G Advanced, jako je rozšířená realita (XR) a kolaborativní roboti, kde je efektivní šíření dat zásadní.

## Klíčové vlastnosti

- Poskytuje optimalizované mechanismy doručování dat včetně unicastu, multicastu a broadcastu
- Podporuje aplikací řízené ukládání dat do mezipaměti a replikaci na okraji sítě
- Umožňuje efektivní skupinovou distribuci dat s využitím služby SEAL Group Management
- Provádí adaptaci dat (např. překódování, rozdělení) na základě možností UE a stavu sítě
- Spolupracuje se službami 5G Multicast-Broadcast Services (MBS) pro efektivní hromadné doručování obsahu
- Aplikuje řízení založené na politikách pro QoS, zabezpečení a účtování během doručování dat

## Související pojmy

- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)

## Definující specifikace

- **TS 23.433** (Rel-20) — SEAL Data Delivery (SEALDD) for Verticals
- **TS 23.482** (Rel-20) — AIML Enablement Service Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 24.486** (Rel-19) — V2X Application Enabler (VAE) Protocol Spec
- **TS 24.538** (Rel-19) — MSGin5G Service Protocol Specification
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TS 29.548** (Rel-19) — SEAL Data Delivery Server Services Stage 3
- **TS 29.549** (Rel-19) — SEAL API Specification for Vertical Applications
- **TS 29.558** (Rel-19) — Enabling Edge Applications

---

📖 **Anglický originál a plná specifikace:** [SEALDD na 3GPP Explorer](https://3gpp-explorer.com/glossary/sealdd/)
