---
slug: "rsvp"
url: "/mobilnisite/slovnik/rsvp/"
type: "slovnik"
title: "RSVP – Resource ReserVation Protocol"
date: 2025-01-01
abbr: "RSVP"
fullName: "Resource ReserVation Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rsvp/"
summary: "RSVP je signalizační protokol používaný k rezervaci síťových prostředků podél datové cesty, který zajišťuje kvalitu služeb (QoS) pro konkrétní datové toky. Umožňuje aplikacím žádat od sítě záruky na š"
---

RSVP je signalizační protokol používaný k rezervaci síťových prostředků podél datové cesty za účelem zajištění kvality služeb pro konkrétní datové toky, například pro aplikace v reálném čase.

## Popis

Protokol pro rezervaci prostředků (Resource ReserVation Protocol, RSVP) je transportní protokol definovaný [IETF](/mobilnisite/slovnik/ietf/) ([RFC](/mobilnisite/slovnik/rfc/) 2205) a přijatý ve specifikacích 3GPP pro správu QoS. Funguje jako signalizační mechanismus pro nastavení a udržování rezervací prostředků pro unicastové nebo multicastové datové toky v IP sítích. RSVP nepřenáší aplikační data, ale komunikuje žádosti o rezervaci mezi síťovými uzly (směrovači a hostiteli), aby zajistil alokaci prostředků, jako je šířka pásma, prostor v bufferu a kapacita zpracování, podél cesty.

Architektura: RSVP používá přístup soft-state, kdy musí být rezervace periodicky obnovovány, aby zůstaly aktivní, což umožňuje dynamickou adaptaci na měnící se síťové podmínky. Klíčové zprávy zahrnují PATH zprávy, odesílané ze zdroje dat k příjemci k vytvoření trasy a specifikaci charakteristik provozu (TSpec), a RESV zprávy, vracející se od příjemce ke zdroji k rezervaci prostředků na každém mezilehlém uzlu. Každý uzel před potvrzením rezervace provádí přijímací řízení na základě dostupných prostředků a kontrol politik.

Jak funguje: Když aplikace vyžaduje QoS, odesílatel vyšle PATH zprávu, která prochází směrovači a ukládá si informace o cestě. Příjemce odpoví RESV zprávou, která sleduje zpětnou cestu a žádá o prostředky, jako je garantovaná služba nebo služba s řízeným zatížením. Směrovače podél cesty rezervují prostředky pomocí klasifikátorů (k identifikaci paketů patřících do toku) a plánovačů (pro prioritní předávání paketů). RSVP podporuje různé styly rezervace (např. fixed-filter, shared-explicit) pro přizpůsobení různým multicastovým scénářům.

V sítích 3GPP je RSVP uváděn v kontextu IP Multimedia Subsystem (IMS) a poskytování QoS end-to-end. Integruje se s funkcemi řízení politik ([PCRF](/mobilnisite/slovnik/pcrf/)) pro vynucení síťových politik. Přestože novější mechanismy, jako je DiffServ a [MPLS](/mobilnisite/slovnik/mpls/), RSVP v některých oblastech nahradily, zůstává relevantní pro explicitní rezervace na úrovni toku ve scénářích vyžadujících přesnou kontrolu QoS, jako je vytváření vyhrazených nosičů v mobilních jádrech nebo mezidoménové řízení prostředků.

## K čemu slouží

RSVP byl vytvořen pro řešení best-effort povahy raných IP sítí, kterým chyběly mechanismy pro zaručení QoS pro aplikace v reálném čase. S příchodem multimediálních služeb, jako je videokonference a VoIP, byla potřeba předvídatelná latence, kolísání a šířka pásma, což tradiční IP směrování nemohlo zajistit. RSVP poskytuje standardizovaný způsob, jak mohou aplikace signalizovat své požadavky na QoS síti, což umožňuje rezervaci prostředků end-to-end.

Zařazení RSVP do norem 3GPP, počínaje [R99](/mobilnisite/slovnik/r99/), bylo motivováno potřebou QoS v mobilních sítích podporujících pokročilé multimediální služby. Řešilo omezení statických konfigurací QoS tím, že umožnilo dynamické rezervace na úrovni toku přizpůsobené uživatelským relacím. RSVP usnadňuje spolupráci mezi buněčnými a pevnými IP sítěmi a zajišťuje konzistentní kvalitu služeb napříč heterogenními doménami.

Historicky předchozí přístupy, jako IntServ (Integrated Services), vyžadovaly stav na úrovni toku ve směrovačích, což vyvolávalo obavy z škálovatelnosti. Návrh RSVP jako soft-state tento problém zmírňuje tím, že umožňuje vypršení stavu bez explicitního ukončení, i když škálovatelnost zůstává výzvou ve velkých sítích. Jeho vytvoření bylo motivováno růstem multicastových aplikací (např. živé vysílání), kde jsou rezervace prostředků složité. V 3GPP RSVP podporuje kritické funkce, jako je priorita nouzových služeb a správa IMS relací, v souladu s regulatorními a služebními požadavky.

## Klíčové vlastnosti

- Signalizuje rezervace prostředků pro unicastové a multicastové toky
- Používá zprávy PATH a RESV pro obousměrné nastavení
- Podporuje rezervace typu soft-state vyžadující periodické obnovení
- Provádí na uzlech přijímací řízení a vynucování politik
- Integruje se s modelem IntServ pro garantovanou QoS
- Umožňuje styly rezervace pro flexibilní sdílení prostředků v multicastu

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.960** (Rel-4) — UMTS Mobile Multimedia Technical Challenges
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 29.421** (Rel-8) — IMS Interworking with External IP Networks
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework

---

📖 **Anglický originál a plná specifikace:** [RSVP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rsvp/)
