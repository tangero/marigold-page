---
slug: "pnfe"
url: "/mobilnisite/slovnik/pnfe/"
type: "slovnik"
title: "PNFE – Paging and Notification Control Functional Entity"
date: 2025-01-01
abbr: "PNFE"
fullName: "Paging and Notification Control Functional Entity"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pnfe/"
summary: "Funkční entita v jádrové síti UMTS odpovědná za zahajování a řízení procedur pagingu za účelem lokalizace uživatelského zařízení (UE) v režimu idle nebo connected. Spravuje distribuci pagingových poža"
---

PNFE je funkční entita v jádrové síti UMTS, která zahajuje a řídí procedury pagingu za účelem lokalizace uživatelského zařízení a spravuje distribuci pagingových požadavků ke správným radiovým síťovým řadičům.

## Popis

Paging and Notification Control Functional Entity (PNFE, funkční entita řídící paging a oznamování) je logická funkce uvnitř jádrové sítě UMTS (CN), konkrétně součást domény s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) a s přepojováním paketů ([PS](/mobilnisite/slovnik/ps/)). Nachází se v uzlu [SGSN](/mobilnisite/slovnik/sgsn/) pro PS doménu a v [MSC](/mobilnisite/slovnik/msc/)/[VLR](/mobilnisite/slovnik/vlr/) pro CS doménu. Hlavní operační role PNFE spočívá ve správě síťem iniciovaného úkolu lokalizace konkrétního uživatelského zařízení (UE), když přicházejí data nebo hovor a síť nezná přesnou buněčnou polohu UE. Slouží jako centrální rozhodovací bod pro zahájení a orchestraci procedury pagingu.

Fungování PNFE je nedílnou součástí mobility managementu. Když datový paket dorazí na SGSN pro UE v režimu idle nebo hovor dorazí na MSC/VLR, je aktivována PNFE příslušné domény. PNFE nejprve konzultuje mobilitní kontext UE, aby určila poslední známou směrovací oblast ([RA](/mobilnisite/slovnik/ra/)) pro PS nebo lokalizační oblast ([LA](/mobilnisite/slovnik/la/)) pro CS. Poté sestaví zprávu pagingového požadavku obsahující identitu UE (např. [IMSI](/mobilnisite/slovnik/imsi/), P-TMSI). Tento požadavek není odeslán přímo do rádiových buněk, ale je předán příslušnému radiovému síťovému řadiči (RNC) nebo skupině RNC, které řídí buňky v cílové RA nebo LA. PNFE odpovídá za logickou distribuci pagingové zátěže.

Architektura PNFE zahrnuje rozhraní s dalšími entitami jádrové sítě. Úzce spolupracuje s entitami mobility managementu (MM) a connection managementu (CM) uvnitř MSC/VLR nebo SGSN. Její funkce je klíčová pro efektivitu sítě a životnost baterie UE. Řízením kdy a kde provést paging zabraňuje zbytečným pagingovým vysíláním v celém systému. PNFE může také podporovat pokročilé funkce jako priorizaci pagingu a koordinaci mezi CS a PS doménami pro simultánní paging UE, což snižuje signalizační zátěž a zpoždění. Je to základní prvek procedur dosažitelnosti a navazování spojení v UMTS.

## K čemu slouží

PNFE byla vytvořena k řešení základní výzvy v mobilních sítích – efektivně lokalizovat mobilní zařízení, které není aktivně v komunikaci (režim idle) nebo je ve stavu, kdy jeho přesná poloha není sledována na úrovni buňky. Před existencí takové centralizované řídicí funkce mohla být pagingová logika rozptýlená a méně koordinovaná, což vedlo k neefektivnímu využití rádiových prostředků a zvýšené signalizační zátěži. PNFE poskytuje standardizovaný optimalizovaný mechanismus pro tento kritický síťem iniciovaný úkol.

Jejím účelem je minimalizovat dopad pagingu na síťové prostředky při maximalizaci pravděpodobnosti úspěšného dosažení UE. Řeší problém celoplošného pagingu napříč celou sítí tím, že inteligentně omezuje oblast pagingu na základě poslední známé registrační oblasti UE (směrovací oblast nebo lokalizační oblast). Tím šetří cennou rádiovou kapacitu a snižuje procesní zátěž všech RNC a Node B. Dále poskytuje jeden kontrolní bod pro politiky spojené s pagingem, jako jsou strategie opakování a priorizace nouzových nebo vysokoprioritních služeb.

Historicky, zavedena v 3G UMTS (Release 99), představovala PNFE evoluci a formalizaci řízení pagingu z 2G GSM/GPRS, kde podobné funkce existovaly, ale byly méně explicitně definovány jako samostatné funkční entity. Její vytvoření bylo motivováno zvýšenou složitostí 3G sítí, oddělením CS a PS domén a potřebou jasného architektonického modelu pro zajištění spolehlivého a škálovatelného mobility managementu s rostoucím počtem účastníků a datových služeb.

## Klíčové vlastnosti

- Centralizované řízení zahajování procedur pagingu v CS (MSC/VLR) i PS (SGSN) doménách jádrové sítě.
- Určuje oblast pagingu (lokalizační oblast nebo směrovací oblast) na základě poslední známé registrace UE.
- Sestavuje a předává pagingové požadavky příslušným radiovým síťovým řadičům (RNC).
- Spravuje strategie opakování pagingu a časovače pro neúspěšné pokusy.
- Podporuje koordinaci mezi CS a PS doménami pro kombinovaný paging za účelem snížení signalizace.
- Spolupracuje s entitami mobility managementu (MM) pro přístup ke kontextu a informacím o poloze UE.

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [PNFE na 3GPP Explorer](https://3gpp-explorer.com/glossary/pnfe/)
