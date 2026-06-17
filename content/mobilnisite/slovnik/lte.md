---
slug: "lte"
url: "/mobilnisite/slovnik/lte/"
type: "slovnik"
title: "LTE – Local Terminal Emulator"
date: 2025-01-01
abbr: "LTE"
fullName: "Local Terminal Emulator"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lte/"
summary: "Local Terminal Emulator (LTE) je funkce systému správy, která emuluje chování terminálu pro testování a diagnostiku v rámci sítě 3GPP. Umožňuje síťovým operátorům simulovat akce uživatelského zařízení"
---

LTE je funkce systému správy, která emuluje chování terminálu pro testování a diagnostiku v rámci sítě 3GPP, což operátorům umožňuje simulovat akce uživatelského zařízení za účelem ověření funkcí a řešení problémů.

## Popis

Local Terminal Emulator (LTE) je entita správy sítě definovaná v rámci architektury Operations, Administration, and Maintenance (OAM) dle 3GPP. Jedná se o softwarovou funkci, typicky součást systému správy sítě ([NMS](/mobilnisite/slovnik/nms/)) nebo systému správy prvků ([EMS](/mobilnisite/slovnik/ems/)), navrženou k emulaci chování uživatelského zařízení (UE) neboli terminálu. Jejím primárním operačním mechanismem je generování standardizovaných signalizačních zpráv 3GPP a simulace procedur UE – jako je připojení (attachment), servisní požadavky, mobilní události a datové relace – směrem k testovaným síťovým prvkům (např. eNodeB, [MME](/mobilnisite/slovnik/mme/), SGW/PGW v 4G, nebo gNB, [AMF](/mobilnisite/slovnik/amf/), [UPF](/mobilnisite/slovnik/upf/) v 5G). To umožňuje řízené a opakovatelné testování funkčnosti sítě v laboratorním, integračním nebo živém síťovém prostředí.

Z architektonického hlediska se LTE připojuje k síti prostřednictvím standardních rozhraní pro správu (např. Itf-N) a může využívat protokolové zásobníky pro přímou komunikaci s řídicí rovinou sítě. Mezi klíčové komponenty patří enginy pro skriptování testovacích scénářů, nástroje pro tvorbu/analýzu protokolových zpráv a analyzátory výsledků. LTE dokáže simulovat více virtuálních UE s různými profily, čímž generuje zátěž a různé vzorce chování. Hraje klíčovou roli v řízení životního cyklu sítě tím, že umožňuje testování shody (conformance), regresní testování po softwarových aktualizacích, izolaci chyb a měření výkonu. Emulací terminálů ověřuje, že síťové uzly správně zpracovávají signalizační sekvence a poskytují očekávané služby.

V praxi LTE funguje tak, že provádí předdefinované testovací případy napodobující reálné chování UE. Například může iniciovat proceduru připojení včetně autentizace a vytvoření relace a ověřit odezvy sítě vůči specifikacím 3GPP. Může také simulovat abnormální podmínky, jako jsou chybné zprávy nebo scénáře vysokého zatížení, pro testování odolnosti sítě. Rozsáhlý seznam specifikací (např. řada 32.xxx pro správu, 37.xxx pro testování shody) podrobně popisuje její požadavky a rozhraní. Její role je odlišná od rádiové technologie „LTE“ (Long Term Evolution); zde je LTE nástrojem pro síťové operátory a výrobce zařízení, který zajišťuje spolehlivost sítě, snižuje rizika nasazení a automatizuje provozní úkoly, čímž zlepšuje celkovou kvalitu služeb.

## K čemu slouží

Local Terminal Emulator existuje proto, aby řešil kritickou potřebu efektivního, škálovatelného a spolehlivého testování a diagnostiky ve složitých sítích 3GPP. Před existencí těchto emulačních nástrojů se operátoři při ověřování sítě výrazně spoléhali na fyzická testovací UE (dongly nebo telefony), což bylo časově náročné, nákladné a obtížně škálovatelné pro testování tisíců simultánních připojení nebo vzácných scénářů. Fyzická zařízení také přinášejí variabilitu a nelze je vždy přesně ovládat. LTE poskytuje softwarovou, automatizovanou alternativu, která dokáže simulovat velké množství terminálů s konzistentním a opakovatelným chováním, čímž řeší problémy v síťové integraci, přijímacím testování a správě poruch.

Historicky, jak se sítě vyvíjely z 2G/3G na 4G a 5G, signalizační složitost a počet síťových funkcí dramaticky vzrostly. Manuální testování se stalo nepraktickým. LTE vznikla z potřeby ověřit interoperabilitu v prostředí více dodavatelů, zajistit shodu se standardy 3GPP před nasazením a snížit provozní náklady ([OPEX](/mobilnisite/slovnik/opex/)) prostřednictvím automatizace. Umožňuje operátorům proaktivně testovat nové funkce, softwarové záplaty nebo konfigurace sítě v laboratorním prostředí před jejich zavedením do živé sítě, čímž minimalizuje rizika narušení služeb.

Dále LTE řeší omezení tradičního drive testování a fyzického sondování. Umožňuje nepřetržité („always-on“) testování z jádra sítě nebo z centra správy, bez geografických omezení. Pro síťové segmentování (network slicing) v 5G může LTE emulovat terminály patřící do různých řezů za účelem ověření jejich izolace a výkonu. Podporuje také bezpečnostní testování simulací útočných vzorců. LTE je tedy základním nástrojem OAM, který podporuje celý životní cyklus sítě – od počátečního vývoje a integrace přes nepřetržitý provoz až po optimalizaci – a zajišťuje tak robustnost sítě a kvalitu služeb.

## Klíčové vlastnosti

- Emuluje signalizační chování UE pro testování řídicí roviny (např. připojení, předávání spojení)
- Podporuje automatizaci testovacích scénářů a regresní testování
- Dokáže simulovat více virtuálních UE s konfigurovatelnými profily a podmínkami zatížení
- Spolupracuje se systémy správy sítě pro integrované pracovní postupy OAM
- Ověřuje shodu síťových funkcí se standardy 3GPP
- Umožňuje izolaci chyb a diagnostické testování bez fyzických zařízení

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.790** (Rel-15) — FRMCS Gap Analysis and Architecture Enhancements
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 24.171** (Rel-19) — NAS Protocol for LCS in E-UTRAN
- **TS 24.482** (Rel-19) — Mission Critical Services Identity Management
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.502** (Rel-19) — 5G Multicast-Broadcast User Services Architecture
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.862** (Rel-17) — Immersive Teleconferencing & Telepresence for Remote Terminals
- **TR 26.905** (Rel-19) — Study on Mobile 3D Video Services
- … a dalších 55 specifikací

---

📖 **Anglický originál a plná specifikace:** [LTE na 3GPP Explorer](https://3gpp-explorer.com/glossary/lte/)
