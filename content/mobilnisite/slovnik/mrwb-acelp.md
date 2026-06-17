---
slug: "mrwb-acelp"
url: "/mobilnisite/slovnik/mrwb-acelp/"
type: "slovnik"
title: "MRWB-ACELP – Wideband Multi-Rate Algebraic Code-Excited Linear Prediction"
date: 2025-01-01
abbr: "MRWB-ACELP"
fullName: "Wideband Multi-Rate Algebraic Code-Excited Linear Prediction"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mrwb-acelp/"
summary: "Širokopásmový řečový kodek používaný v sítích 3GPP, který rozšiřuje kodek AMR-WB o vícerychlostní strukturu založenou na ACELP. Poskytuje vysoce kvalitní hlasové služby díky podpoře více bitových rych"
---

MRWB-ACELP je širokopásmový řečový kodek používaný v sítích 3GPP, který rozšiřuje AMR-WB o vícerychlostní ACELP strukturu, aby poskytoval vysoce kvalitní adaptivní hlasové služby pro VoIP a VoLTE.

## Popis

MRWB-ACELP, neboli Wideband Multi-Rate [ACELP](/mobilnisite/slovnik/acelp/), je řečový kódovací algoritmus standardizovaný organizací 3GPP. Je v podstatě jádrem Algebraic Code-Excited Linear Prediction (ACELP) širokopásmového řečového kodeku Adaptive Multi-Rate Wideband ([AMR-WB](/mobilnisite/slovnik/amr-wb/)) a pracuje se širším zvukovým pásmem 50–7000 Hz ve srovnání s úzkopásmovým pásmem 300–3400 Hz. Kodek funguje tak, že analyzuje řečové signály, extrahuje parametry týkající se filtru hlasového traktu (pomocí lineární predikce) a excitačního signálu (pomocí algebraického kodebooku) a následně tyto parametry kvantuje pro přenos s proměnnou bitovou rychlostí.

Architektura kodeku je založena na vícerychlostní ACELP struktuře. Podporuje více zdrojových režimů kodeku, z nichž každý odpovídá konkrétní bitové rychlosti. Tyto režimy umožňují síti během aktivního hovoru nařídit změnu bitové rychlosti kodeku, což je proces známý jako adaptace režimu kodeku nebo adaptace spoje. Podporované bitové rychlosti pro MRWB-ACELP (AMR-WB) jsou 6,60, 8,85, 12,65, 14,25, 15,85, 18,25, 19,85, 23,05 a 23,85 kbit/s. Činnost kodeku zahrnuje rozdělení vstupní řeči na rámce (typicky 20ms rámce), provedení lineární prediktivní analýzy pro získání koeficientů filtru a následné prohledávání pevných a adaptivních kodebooků pro reprezentaci excitačního signálu, který při průchodu syntetickým filtrem nejlépe odpovídá původní řeči.

Jeho úlohou v síti je poskytovat vysoce kvalitní a odolnou hlasovou službu, zejména pro paketově přepínaný hlas přes IP (VoIP) v LTE (VoLTE) a 5G (VoNR). Širokopásmový zvuk poskytuje výrazně lepší přirozenost a srozumitelnost. Vícerychlostní schopnost je klíčová pro efektivitu a odolnost sítě; systém může snížit bitovou rychlost během období přetížení nebo špatných rádiových podmínek, aby udržel kontinuitu hovoru s vyšší ochranou proti chybám, nebo zvýšit bitovou rychlost za dobrých podmínek pro lepší kvalitu. Parametry kodeku jsou zabaleny do RTP paketů pro přenos přes IP jádrovou síť.

## K čemu slouží

MRWB-ACELP byl vyvinut, aby uspokojil rostoucí poptávku po vysoce kvalitních hlasových službách v mobilních sítích, které přesahují 'telefonní kvalitu' úzkopásmových kodeků. Primární motivací bylo poskytnout přirozenější a působivější hlasový zážitek zdvojnásobením zvukového pásma. To bylo hnací silou očekávání uživatelů nastavených pevnými širokopásmovými službami a možnostmi nových paketově přepínaných síťových architektur.

Řeší problém zajištění konzistentní kvality hlasu v proměnném bezdrátovém prostředí. Vícerychlostní povaha kodeku řeší omezení kodeků s pevnou rychlostí, které mohly buď plýtvat kapacitou, nebo přerušovat hovory za nepříznivých podmínek. Umožněním dynamické adaptace umožňuje MRWB-ACELP optimální kompromisy mezi kvalitou hlasu, kapacitou a pokrytím. Jeho vznik byl motivován evolucí směrem k All-IP sítím (IMS), kde byl efektivní adaptivní širokopásmový kodek nezbytný pro to, aby se VoIP přes mobilní síť stalo konkurenceschopným a lepším než tradiční hlas přes okruhově přepínanou síť. Stal se základním kamenem služeb [HD](/mobilnisite/slovnik/hd/) Voice v sítích 3GPP.

## Klíčové vlastnosti

- Širokopásmové zvukové pásmo (50-7000 Hz) pro vynikající přirozenost a srozumitelnost řeči.
- Vícerychlostní provoz s devíti zdrojovými bitovými rychlostmi kodeku od 6,6 do 23,85 kbit/s.
- Založeno na efektivním algoritmu ACELP (Algebraic Code-Excited Linear Prediction).
- Podporuje adaptaci režimu kodeku během hovoru na základě síťových podmínek a příkazů.
- Poskytuje odolný výkon proti přenosovým chybám prostřednictvím adaptace rychlosti a kanálového kódování.
- Standardizovaný formát přenosové jednotky (payload) pro přenos přes RTP/UDP/IP, což umožňuje VoIP/VoLTE/VoNR.

## Související pojmy

- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [ACELP – Algebraic Code-Excited Linear Prediction](/mobilnisite/slovnik/acelp/)

## Definující specifikace

- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification

---

📖 **Anglický originál a plná specifikace:** [MRWB-ACELP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mrwb-acelp/)
