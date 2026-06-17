---
slug: "fid"
url: "/mobilnisite/slovnik/fid/"
type: "slovnik"
title: "FID – Flow Identifier"
date: 2025-01-01
abbr: "FID"
fullName: "Flow Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fid/"
summary: "Jedinečný identifikátor používaný k rozlišení jednotlivých IP toků nebo toků servisních dat v síti 3GPP. Je klíčový pro aplikaci specifických politik QoS, účtovacích pravidel a správy provozu na různé"
---

FID je jedinečný identifikátor, který rozlišuje jednotlivé IP toky nebo toky servisních dat v síti 3GPP a umožňuje aplikaci specifických politik QoS, účtovacích pravidel a správy provozu.

## Popis

Flow Identifier (FID) je základní parametr v architektuře Policy and Charging Control (PCC) dle 3GPP. Slouží jako jedinečná značka pro IP tok nebo tok servisních dat, což je sada toků IP paketů odpovídajících konkrétní šabloně toku servisních dat. FID používají síťové prvky jako Policy and Charging Rules Function (PCRF) a Policy and Charging Enforcement Function (PCEF) k identifikaci a aplikaci správných pravidel politiky a účtování na uživatelský provoz. PCRF tato pravidla definuje v PCC pravidlech, z nichž každé je asociováno s konkrétním FID a určuje parametry jako třídu QoS, datové toky a metody účtování.

Při provozu, když uživatel zahájí službu (např. video stream), PCRF autorizuje požadované zdroje a nainstaluje odpovídající PCC pravidla v PCEF (obvykle umístěném v PDN Gateway). Každé PCC pravidlo obsahuje FID, šablonu toku servisních dat (definující IP pakety pomocí 5-tice filtrů) a asociované instrukce pro řízení politiky (QoS) a řízení účtování. PCEF pak používá FID k mapování příchozích paketů uživatelské roviny na správnou sadu pravidel pro vynucení. To síti umožňuje rozlišovat např. mezi tokem VoIP s vysokou prioritou a best-effort tokem prohlížení webu pro stejného uživatele.

Role FID je klíčová pro pokročilé služebně-aware síťování. Poskytuje propojení mezi autorizací služeb na vysoké úrovni v řídicí rovině a detailním zpracováním na úrovni paketů v uživatelské rovině. Díky jedinečné identifikaci toků mohou operátoři implementovat sofistikovanou správu provozu, zajišťovat QoS pro služby v reálném čase a aplikovat přesné účtování na základě typu služby, obsahu nebo aplikace. FID je klíčovým enablerem pro scénáře síťového řezání (network slicing) a edge computingu, kde různé řezy nebo aplikace vyžadují odlišné politiky zpracování provozu.

## K čemu slouží

FID byl zaveden, aby řešil potřebu detailní, na toky založené kontroly politiky a účtování v IP mobilních sítích. Před jeho zavedením byla kontrola politiky často hrubozrnná, aplikovaná na uživatele nebo Access Point Name ([APN](/mobilnisite/slovnik/apn/)), což bylo nedostatečné pro širokou škálu služeb s různými požadavky na QoS a účtování, které se objevily s mobilním broadbandem. Rozšíření služeb v reálném čase, jako VoIP a video streamování, si vyžádalo mechanismus pro identifikaci a odlišné zacházení s jednotlivými aplikačními toky v rámci uživatelské relace.

Jeho vznik byl motivován evolucí směrem k all-IP sítím ve 3GPP Release 8 (EPS). Architektura PCC byla standardizována, aby poskytla jednotný rámec pro služebně-aware politiku a účtování. FID je jádrovou součástí tohoto rámce a řeší problém, jak jedinečně referencovat a spravovat množství souběžných datových toků, které může generovat jediný uživatel. Umožňuje operátorům překročit paušální účtování a best-effort doručování, a umožňuje tak diferenciaci služeb, optimalizované využití zdrojů a nové obchodní modely, jako je sponzorovaný přenos dat nebo kvalita na vyžádání.

Poskytnutím stabilního identifikátoru pro tok po celou dobu jeho životnosti FID zajišťuje konzistentní aplikaci politiky, i když se základní parametry paketových filtrů (jako zdrojová IP) změní v důsledku síťových událostí. Abstrahuje specifické charakteristiky paketů od pravidel politiky, čímž zjednodušuje správu a umožňuje dynamické aktualizace politik bez předefinování celé šablony toku.

## Klíčové vlastnosti

- Jednoznačně identifikuje tok servisních dat v rámci PDN připojení uživatele
- Klíčový parametr v PCC pravidlech pro svázání instrukcí politiky a účtování s konkrétním tokem
- Umožňuje detailní vynucení QoS (např. garantovaný datový tok, priorita) pro každý tok zvlášť
- Podporuje účtování založené na toku, včetně diferencovaného ratingu a reportingu
- Umožňuje dynamickou instalaci, modifikaci a odstranění politik specifických pro tok ze strany PCRF
- Usnadňuje detekci provozu a řízení přístupu (gating control) pro konkrétní aplikace nebo služby

## Definující specifikace

- **TS 23.261** (Rel-19) — IP Flow Mobility between 3GPP and WLAN
- **TS 24.303** (Rel-19) — Dual-Stack MIPv6 Mobility Management
- **TS 24.327** (Rel-12) — Mobility between I-WLAN and GPRS
- **TS 31.131** (Rel-19) — C Language Binding for (U)SIM API
- **TS 34.131** (Rel-19) — SIM API C Language Test Specification

---

📖 **Anglický originál a plná specifikace:** [FID na 3GPP Explorer](https://3gpp-explorer.com/glossary/fid/)
