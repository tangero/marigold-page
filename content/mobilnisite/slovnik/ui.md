---
slug: "ui"
url: "/mobilnisite/slovnik/ui/"
type: "slovnik"
title: "UI – Unnumbered Information frame"
date: 2025-01-01
abbr: "UI"
fullName: "Unnumbered Information frame"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ui/"
summary: "Rámec Unnumbered Information (UI) je typ rámce v protokolech vrstvy datového spoje, jako jsou ty používané v 3GPP pro přenos signalizace. Přenáší informace bez vyžadování čísel posloupnosti nebo potvr"
---

UI je typ rámce vrstvy datového spoje používaný v protokolech 3GPP pro přenos signalizace bez spojení, který přenáší informace bez použití čísel posloupnosti nebo potvrzení, což umožňuje přenos dat s nízkou režií.

## Popis

Rámec Unnumbered Information (UI) je specifický formát rámce definovaný v protokolech vrstvy datového spoje, zejména v protokolu Link Access Protocol for the D-channel ([LAPD](/mobilnisite/slovnik/lapd/)) a jeho derivátech používaných v systémech 3GPP. Jako 'nečíslovaný' rámec neobsahuje čísla posloupnosti (N(S) a N(R)) a není součástí číslované výměny pro potvrzovaný přenos dat se spojením. Místo toho jsou UI rámce navrženy pro přenos informací bez spojení. Struktura rámce zahrnuje hlavičku s adresním polem a řídicím polem, které jej identifikuje jako UI rámec, následovanou informačním polem obsahujícím datovou jednotku protokolu ([PDU](/mobilnisite/slovnik/pdu/)) vyšší vrstvy, a kontrolním součtem rámce ([FCS](/mobilnisite/slovnik/fcs/)) pro detekci chyb. V architekturách 3GPP se UI rámce používají u specifických rozhraní a protokolů. Klíčovým příkladem je jejich použití v protokolu vrstvy 2 pro přenos signalizačních zpráv přes rozhraní jako A-rozhraní (mezi [BSC](/mobilnisite/slovnik/bsc/) a [MSC](/mobilnisite/slovnik/msc/) v 2G/3G) nebo Iu rozhraní (mezi [RNC](/mobilnisite/slovnik/rnc/) a CN v 3G), kde jsou určité signalizační zprávy přenášeny jako UI rámce. Protokol funguje tak, že umožňuje odesílateli vyslat UI rámec bez předchozího navázání vyhrazeného logického spojení. Příjemce rámec zpracuje, ale neodesílá potvrzení na úrovni spojové vrstvy. Tento mechanismus je efektivní pro rozesílání broadcast informací, odesílání nekritických stavových aktualizací nebo přenos signalizace, kde spolehlivost zajišťují protokoly vyšších vrstev. Jeho úlohou je poskytnout odlehčený transportní mechanismus s nízkou latencí pro řídicí informace v transportní vrstvě sítě.

## K čemu slouží

Účelem UI rámce je poskytnout efektivní transportní mechanismus bez spojení pro informace, které nevyžadují garantované doručení ve správném pořadí nabízené potvrzovanými režimy (jako I-rámce). Řeší problém snížení režie pro určité typy síťového provozu. V historickém kontextu potřebovaly telekomunikační signalizační systémy jak spolehlivou signalizaci (pro sestavení hovoru), tak efektivní signalizaci s nízkou režií (pro broadcast informace, jako jsou systémové informace buňky nebo paging). Použití potvrzovaných režimů pro všechny zprávy by vytvořilo zbytečnou latenci a signalizační zátěž. UI rámec to řeší tím, že nabízí možnost 'odešli a zapomeň' na úrovni vrstvy datového spoje, přičemž spolehlivost případně přenechává vyšším vrstvám. Toto bylo motivováno zejména návrhem signalizace [ISDN](/mobilnisite/slovnik/isdn/) a [SS7](/mobilnisite/slovnik/ss7/), která ovlivnila protokoly 3GPP. Umožňuje síťovým prvkům rychle rozesílat informace bez potřeby handshaku a správy stavu vyžadovaných pro logické spojení, což zjednodušuje návrh pro specifické případy použití a šetří výpočetní prostředky síťových uzlů.

## Klíčové vlastnosti

- Formát rámce vrstvy datového spoje bez spojení
- Postrádá čísla posloupnosti (N(S), N(R)) pro řízení toku
- Nevyžaduje potvrzení na úrovni spojové vrstvy
- Obsahuje informační pole pro přenos PDU vyšší vrstvy
- Pro detekci chyb používá pouze kontrolní součet rámce (FCS)
- Využíván v specifických signalizačních transportních protokolech 3GPP (např. odvozených od LAPD)

## Související pojmy

- [LAPD – Link Access Procedure on the D-channel](/mobilnisite/slovnik/lapd/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TS 27.010** (Rel-19) — Multiplexing Protocol for UE-TE Interface
- **TS 31.114** (Rel-8) — USAT Interpreter Transmission Protocol
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [UI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ui/)
