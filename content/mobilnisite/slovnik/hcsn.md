---
slug: "hcsn"
url: "/mobilnisite/slovnik/hcsn/"
type: "slovnik"
title: "HCSN – HS-SCCH Cyclic Sequence Number"
date: 2025-01-01
abbr: "HCSN"
fullName: "HS-SCCH Cyclic Sequence Number"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hcsn/"
summary: "Pořadové číslo používané na vysokorychlostním sdíleném řídicím kanálu (HS-SCCH) pro HSDPA v UMTS. Zajišťuje správné řazení a identifikaci řídicích informací odesílaných k uživatelskému zařízení (UE),"
---

HCSN (HS-SCCH Cyclic Sequence Number) je cyklické pořadové číslo používané na řídicím kanálu HS-SCCH pro HSDPA v UMTS, které zajišťuje správné řazení a identifikaci řídicích informací odesílaných k uživatelskému zařízení (UE).

## Popis

[HS-SCCH](/mobilnisite/slovnik/hs-scch/) Cyclic Sequence Number (HCSN) je klíčovou součástí funkce High-Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)) v UMTS, specifikovanou v 3GPP TS 25.321. Funguje v rámci vrstvy Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)), konkrétně entity MAC-hs v Node B. HS-SCCH je downlinkový fyzický řídicí kanál, který přenáší základní signalizační informace k uživatelskému zařízení (UE) předtím, než dojde k samotnému přenosu vysokorychlostních dat na [HS-PDSCH](/mobilnisite/slovnik/hs-pdsch/). Tyto informace zahrnují sadu kanalizačních kódů, modulační schéma a velikost transportního bloku. HCSN je 3bitové pole v rámci informací typu 1 na HS-SCCH, které poskytuje cyklické pořadové číslo pro řídicí zprávy.

Jeho hlavní funkcí je poskytnout mechanismus, pomocí kterého může uživatelské zařízení (UE) detekovat, zda mu unikl přenos na HS-SCCH. Node B zvyšuje hodnotu HCSN pro každý nový přenos na HS-SCCH určený pro konkrétní uživatelské zařízení (UE). Uživatelské zařízení (UE) sleduje kanál HS-SCCH a monitoruje přijaté hodnoty HCSN. Kontrolou této sekvence může uživatelské zařízení (UE) identifikovat mezery, které indikují ztracené řídicí informace. Tato detekce je klíčová, protože ztráta řídicích informací by vedla k neschopnosti uživatelského zařízení (UE) správně dekódovat následný přenos dat na HS-PDSCH, což by způsobilo ztrátu paketů a vyžadovalo by opakované přenosy na vyšších vrstvách.

HCSN funguje ve spojení s dalšími parametry HS-SCCH a [HARQ](/mobilnisite/slovnik/harq/) procesy uživatelského zařízení (UE). Když uživatelské zařízení (UE) detekuje novou hodnotu HCSN, ví, že přidružený přenos na HS-PDSCH obsahuje nová data. Pokud hodnota HCSN indikuje opakovaný přenos (shoduje se s předchozím pořadovým číslem pro stejný HARQ proces), uživatelské zařízení (UE) zkombinuje nová data s dříve uloženými měkkými bity pro HARQ kombinování s inkrementální redundancí. Toto těsné propojení signalizace řídicího kanálu (prostřednictvím HCSN) a datového kanálu je zásadní pro rychlou, na spojení adaptivní povahu HSDPA, což umožňuje efektivní využití rádiových zdrojů a vysoké uživatelské datové rychlosti.

## K čemu slouží

HCSN bylo zavedeno, aby vyřešilo problém spolehlivé řídicí signalizace pro nový, rychle plánovaný kanál [HSDPA](/mobilnisite/slovnik/hsdpa/) v UMTS Release 5. Před zavedením HSDPA používala downlinková paketová data vyhrazené kanály s pomalejším plánováním řízeným RNC. HSDPA přesunulo plánování do Node B (základnové stanice), aby mohlo rychle reagovat na podmínky rádiového kanálu, což vyžadovalo robustní řídicí kanál s nízkou latencí ([HS-SCCH](/mobilnisite/slovnik/hs-scch/)) pro informování uživatelského zařízení (UE) o blížících se datových dávkách.

Problém spočíval v tom, že uživatelské zařízení (UE) mohlo zmeškat přenos na HS-SCCH kvůli špatným rádiovým podmínkám. Bez pořadového čísla by si uživatelské zařízení (UE) nemuselo uvědomit, že zmeškalo řídicí signál, a pak by neposlouchalo odpovídající data na [HS-PDSCH](/mobilnisite/slovnik/hs-pdsch/), nebo by mohlo chybně interpretovat opakovaný přenos jako nová data. HCSN poskytuje jednoduchý, nenáročný sekvenční mechanismus, který umožňuje uživatelskému zařízení (UE) udržovat synchronizaci s přenosovým plánem Node B, a zajišťuje tak správný příjem dat a správnou správu HARQ procesů. Řeší konkrétní problém spolehlivosti řídicího kanálu bez přidání nadměrné režie, což bylo klíčové pro zachování cílů nízké latence a vysoké efektivity HSDPA.

## Klíčové vlastnosti

- 3bitové pole cyklického pořadového čísla v rámci informací typu 1 na HS-SCCH
- Umožňuje uživatelskému zařízení (UE) detekovat zmeškané přenosy řídicích informací na HS-SCCH
- Indikuje, zda přidružený přenos na HS-PDSCH obsahuje nová data nebo opakovaný přenos
- Základní pro správnou funkci HARQ procesů v HSDPA
- Poskytuje synchronizaci mezi plánováním v Node B a příjmem v uživatelském zařízení (UE)
- Nízko-režiový mechanismus klíčový pro rychlé plánování v Node B

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [HS-SCCH – High Speed Physical Downlink Shared Control Channel](/mobilnisite/slovnik/hs-scch/)
- [HS-PDSCH – High Speed Physical Downlink Shared Channel](/mobilnisite/slovnik/hs-pdsch/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN

---

📖 **Anglický originál a plná specifikace:** [HCSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/hcsn/)
