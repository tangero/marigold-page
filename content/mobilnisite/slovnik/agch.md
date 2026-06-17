---
slug: "agch"
url: "/mobilnisite/slovnik/agch/"
type: "slovnik"
title: "AGCH – Access Grant Channel"
date: 2025-01-01
abbr: "AGCH"
fullName: "Access Grant Channel"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/agch/"
summary: "Access Grant Channel (AGCH) je downlinkový logický kanál v GSM a UMTS, který přenáší zprávy okamžitého přiřazení ze sítě k mobilní stanici. Používá se k přidělení vyhrazeného kanálu (SDCCH) mobilní st"
---

AGCH je downlinkový logický kanál v GSM a UMTS, který přenáší zprávy okamžitého přiřazení (Immediate Assignment) ze sítě, aby mobilní stanici přidělil vyhrazený kanál pro sestavení hovoru nebo signalizaci.

## Popis

Access Grant Channel (AGCH) je základní logický řídicí kanál v rámci protokolové architektury rádiového rozhraní GSM a UMTS. Funguje na downlinku z základnové stanice ([BTS](/mobilnisite/slovnik/bts/)) nebo Node B k mobilní stanici ([MS](/mobilnisite/slovnik/ms/)). Jako vysílací (broadcast) kanál je mapován na nosnou Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)) fyzické vrstvy, konkrétně v rámci logické skupiny Common Control Channel ([CCCH](/mobilnisite/slovnik/ccch/)). Když mobilní stanice zahájí proceduru odesláním žádosti o kanál na Random Access Channel (RACH), Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) nebo Radio Network Controller (RNC) síťový prvek tuto žádost zpracuje a vyhodnotí dostupnost zdrojů. AGCH je médium použité k doručení odpovědi sítě, známé jako zpráva Immediate Assignment. Tato zpráva přikazuje mobilní stanici naladit se na konkrétní Stand-alone Dedicated Control Channel (SDCCH) nebo v některých případech přímo na Traffic Channel (TCH) pro následnou signalizační výměnu. Primární role AGCH spočívá v alokaci vyhrazeného, point-to-point signalizačního kanálu konkrétní mobilní stanici, čímž ji přesouvá z fáze konkurenčního náhodného přístupu do řízené fáze vyhrazené signalizace. Toto přidělení zahrnuje klíčové parametry, jako je přiřazená frekvence kanálu, časový slot, kód tréninkové sekvence a čas zahájení. Efektivní fungování AGCH je zásadní pro minimalizaci přístupového zpoždění, správu zahlcení společných zdrojů a zajištění spolehlivých procedur sestavení hovoru a správy mobility. Jeho návrh je základním kamenem přístupové vrstvy GSM/UMTS a umožňuje síti koordinovaně zvládat více současných pokusů o přístup.

## K čemu slouží

AGCH byl vytvořen k řešení základního problému uspořádaného a bezkolizního přístupu k mobilní síti pro signalizační účely. V raných mobilních systémech byl potřebný mechanismus pro přechod mobilní stanice z počátečního, nekoordinovaného pokusu o přístup na sdíleném uplinkovém kanálu (RACH) na vyhrazený, sítí řízený signalizační kanál. Bez AGCH by síť neměla efektivní způsob, jak přidělovat zdroje a dávat pokyny konkrétním mobilním stanicím, což by vedlo ke kolizím, neúspěšným pokusům o sestavení hovoru a nepředvídatelné kvalitě služeb. AGCH poskytuje toto řízené přidělení, které je nezbytné pro jakoukoli síťovou proceduru vyžadující rozsáhlejší signalizaci, jako je sestavení hovoru iniciované mobilní stanicí, odpověď na paging z terminované strany, aktualizace lokální oblasti a aktivace doplňkových služeb. Řeší omezení čistě náhodného přístupového systému zavedením řízené, naplánované odpovědi ze sítě, což výrazně zvyšuje pravděpodobnost úspěšného přístupu a celkovou kapacitu řídicí roviny. Historicky jeho specifikace v GSM Release 4 a jeho pokračování v UMTS stanovily robustní mechanismus přidělení přístupu, který zůstal konceptuálním základem pro pozdější generace, i když se konkrétní struktury kanálů vyvíjely.

## Klíčové vlastnosti

- Přenáší zprávy okamžitého přiřazení (Immediate Assignment) ze sítě k mobilní stanici
- Je mapován na downlinkový Common Control Channel (CCCH)
- Přiděluje vyhrazený SDCCH nebo TCH pro signalizaci
- Obsahuje parametry jako frekvence, časový slot a kód tréninkové sekvence
- Reaguje na žádosti o kanál přijaté na RACH
- Nezbytný pro sestavení hovoru, aktualizaci polohy a procedury SMS

## Související pojmy

- [CCCH – Common Control Channel](/mobilnisite/slovnik/ccch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [AGCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/agch/)
