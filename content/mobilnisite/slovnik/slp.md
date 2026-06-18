---
slug: "slp"
url: "/mobilnisite/slovnik/slp/"
type: "slovnik"
title: "SLP – Service Location Protocol"
date: 2026-01-01
abbr: "SLP"
fullName: "Service Location Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/slp/"
summary: "Protokol definovaný 3GPP pro vyhledávání a výběr lokalizačních služeb a serverů v rámci sítě. Umožňuje uživatelskému zařízení (UE) lokalizovat služby, jako jsou pozicovací servery (např. SLP), a je kl"
---

SLP je protokol 3GPP pro vyhledávání a výběr lokalizačních služeb a serverů, jako jsou např. pozicovací servery, v rámci sítě za účelem umožnění lokalizačních aplikací a efektivního vyhledávání služeb.

## Popis

Service Location Protocol (SLP) je protokol definovaný [IETF](/mobilnisite/slovnik/ietf/) ([RFC](/mobilnisite/slovnik/rfc/) 2608), který 3GPP přijalo a profilovalo pro použití ve své architektuře, primárně za účelem usnadnění vyhledávání služeb. V kontextu 3GPP je SLP klíčovým prvkem pro lokalizační služby ([LCS](/mobilnisite/slovnik/lcs/)), který umožňuje klientovi, jako je uživatelské zařízení (UE) nebo síťová entita, objevit adresu lokalizačního serveru, především Secure User Plane Location ([SUPL](/mobilnisite/slovnik/supl/)) Location Platform (SLP). Protokol funguje v modelu klient-server, kde User Agents ([UA](/mobilnisite/slovnik/ua/)) vydávají požadavky na služby a Service Agents ([SA](/mobilnisite/slovnik/sa/)) služby inzerují. Directory Agents ([DA](/mobilnisite/slovnik/da/)) mohou být volitelně použity jako centralizované úložiště pro inzerci služeb, což zlepšuje škálovatelnost ve velkých sítích. Protokol používá služební [URL](/mobilnisite/slovnik/url/) a atributy k popisu služeb a vyhledávání lze provádět pomocí multicastu nebo unicastu. V rámci 3GPP se SLP často používá v architektuře SUPL, kde SUPL Enabled Terminal (SET) využívá SLP k objevení adresy svého Home SLP (H-SLP) nebo Discovered SLP (D-SLP) pro zahájení pozicovací relace. Toto vyhledávání je klíčové pro navázání zabezpečeného spojení na uživatelské rovině pro doručení lokalizační informace. Protokol podporuje autentizaci a poskytuje flexibilní rámec pro vyhledávání různých typů služeb nad rámec pouhé lokalizace, ačkoli jeho primární aplikace v rámci 3GPP je v ekosystému SUPL. Jeho integrace umožňuje decentralizované vyhledávání služeb bez nutnosti předkonfigurace serverových adres v každém zařízení, což zvyšuje flexibilitu a spravovatelnost pro síťové operátory.

## K čemu slouží

SLP byl zaveden, aby řešil problém dynamického vyhledávání služeb v IP sítích, což se stalo stále důležitějším s nástupem mobilních datových služeb a lokalizačních aplikací. Před standardizovaným vyhledáváním služeb často zařízení vyžadovala manuální konfiguraci adres serverů (jako je domovský lokalizační server), což bylo nepružné, obtížně spravovatelné ve velkém měřítku a bránilo přenositelnosti služeb a roamingu. Protokol poskytuje standardizovanou, automatizovanou metodu pro klienty k nalezení potřebných síťových služeb. V rámci 3GPP bylo jeho přijetí, zejména počínaje Release 7 s SUPL 1.0, motivováno potřebou efektivního řešení lokalizace na uživatelské rovině. SLP umožňuje SUPL Enabled Terminal dynamicky objevit jeho příslušný SLP, ať už se jedná o SLP domovské sítě nebo SLP navštívené sítě během roamingu. Tato schopnost je zásadní pro tísňové služby (např. E911), komerční lokalizační služby a regulatorní soulad, protože zajišťuje, že zařízení může vždy najít pozicovací server bez zásahu uživatele. Odděluje klienta od statické síťové konfigurace, což operátorům umožňuje volněji nasazovat a přesouvat servery a podporovat rostoucí ekosystém lokalizačních služeb.

## Klíčové vlastnosti

- Standardizovaný mechanismus vyhledávání služeb využívající služební URL a atributy
- Podpora tří typů agentů: User Agent (UA), Service Agent (SA) a Directory Agent (DA)
- Umožňuje jak multicastový, tak unicastový režim vyhledávání pro flexibilitu v návrhu sítě
- Poskytuje rámec pro autentizaci a zabezpečení služeb
- Ústřední prvek architektury SUPL pro vyhledání Home SLP (H-SLP) a Discovered SLP (D-SLP)
- Nezávislý na jazyku a rozšiřitelný pro různé typy služeb nad rámec lokalizace

## Související pojmy

- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.303** (Rel-19) — Proximity Services (ProSe) Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 23.868** (Rel-9) — Study on IMS Emergency Calls
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.171** (Rel-19) — LCS Application Protocol (LCS-AP) Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 29.819** (Rel-13) — Diameter Base Protocol Update Analysis
- **TS 33.533** (Rel-19) — Security for 5G Ranging & Sidelink Positioning
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 36.809** (Rel-12) — Study on RF Pattern Matching for LTE Positioning
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [SLP na 3GPP Explorer](https://3gpp-explorer.com/glossary/slp/)
