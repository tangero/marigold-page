---
slug: "pdcch"
url: "/mobilnisite/slovnik/pdcch/"
type: "slovnik"
title: "PDCCH – Physical Downlink Control Channel"
date: 2025-01-01
abbr: "PDCCH"
fullName: "Physical Downlink Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pdcch/"
summary: "Základní fyzický kanál pro přenos směrem dolů v LTE a NR, který přenáší řídicí informace pro přenos směrem dolů (DCI). Je klíčový pro přidělování zdrojů, udělení plánovacích oprávnění, příkazy pro říz"
---

PDCCH je základní fyzický kanál pro přenos směrem dolů v LTE a NR, který přenáší řídicí informace pro přenos směrem dolů (DCI) pro přidělování zdrojů, plánování a další kritické řídicí signalizaci k uživatelskému zařízení.

## Popis

Fyzický řídicí kanál pro přenos směrem dolů (PDCCH) je klíčový fyzický kanál v LTE (E-UTRA) i NR (New Radio), který přenáší řídicí informace pro přenos směrem dolů (DCI) ze sítě (gNB v NR, eNB v LTE) k uživatelským zařízením (UE). Funguje v řídicí oblasti podrámce (LTE) nebo slotu (NR). PDCCH nepřenáší data vyšších vrstev; místo toho přenáší zásadní plánovací přiřazení a řídicí příkazy. Uživatelské zařízení musí nepřetržitě monitorovat sadu kandidátních PDCCH pro potenciální DCI adresované jemu, přičemž používá jedinečný identifikátor (C-RNTI, SI-RNTI atd.) zakódovaný do cyklického redundantního součtu (CRC) DCI.

Z architektonického hlediska zahrnuje přenos PDCCH několik klíčových kroků. Nejprve je vygenerováno datové pole DCI, které obsahuje informace jako přiřazení zdrojových bloků, schéma modulace a kódování (MCS), číslo HARQ procesu a příkazy pro řízení výkonu. K tomuto datovému poli je připojen CRC, který je následně zakódován pomocí RNTI cílového uživatelského zařízení. Bitová sekvence je pak kanálově zakódována (v LTE pomocí konvolučního kódování s uzavřenou smyčkou, v NR ve většině případů pomocí polárního kódování), přizpůsobena přenosové rychlosti a namapována na prvky řídicího kanálu (CCE). V LTE jsou CCE seskupeny (úrovně agregace 1, 2, 4, 8), aby poskytly různé kódovací rychlosti pro adaptaci spojení. Tyto CCE jsou pak namapovány na specifické skupiny zdrojových prvků (REG) v řídicí oblasti mřížky OFDMA, která je definována prvním několika OFDM symboly podrámce, jak je indikováno PCFICH.

V NR se tento koncept vyvinul do pružnější struktury. NR-PDCCH je organizován v sadách řídicích zdrojů (CORESET) a prohledávacích prostorech. CORESET definuje časově-frekvenční oblast (až 3 OFDM symboly a konfigurovatelnou šířku pásma), kde může být PDCCH vysílán. Uvnitř CORESET uživatelské zařízení monitoruje předdefinované kandidáty PDCCH v jednom nebo více prohledávacích prostorech (společných nebo specifických pro UE). NR používá pro DCI polární kódování a podporuje úrovně agregace od 1 do 16. Role PDCCH je pro provoz sítě naprosto klíčová: doručuje oprávnění pro přenos směrem nahoru (sděluje uživatelskému zařízení, kdy a kde vysílat), přiřazení pro přenos směrem dolů (sděluje uživatelskému zařízení, kde přijímat PDSCH), indikátory formátu slotu, indikace předběžného obsazení a příkazy pro řízení výkonu. Jeho spolehlivý příjem je předpokladem pro jakýkoli datový přenos, což činí jeho návrh kritickým pro kapacitu systému, latenci a výdrž baterie uživatelského zařízení.

## K čemu slouží

PDCCH byl vytvořen, aby vyřešil základní problém dynamického a efektivního přidělování zdrojů v paketových buňkových systémech s OFDMA, jako jsou LTE a NR. Předchozí systémy, jako UMTS, používaly vyhrazené kanály nebo méně dynamické sdílené kanály, které byly pro přerušovaný datový provoz neefektivní. PDCCH umožňuje rychlé plánování na úrovni podrámce (nebo slotu), což síti dovoluje přiřazovat rádiové zdroje optimálně na základě okamžitých podmínek kanálu, požadavků provozu a požadavků QoS pro více uživatelských zařízení.

Historicky si přechod na plně IP, paketově orientované architektury vyžádal řídicí kanál, který by zvládl rychlá plánovací rozhodnutí. PDCCH to poskytuje tím, že přenáší kompaktní zprávy DCI, které uživatelským zařízením přesně instruují, které časově-frekvenční zdroje jsou jim přiděleny pro jejich datové přenosy směrem nahoru nebo dolů (na PUSCH nebo PDSCH). Tím se řeší omezení statického nebo semistatického přidělování, což dramaticky zlepšuje spektrální účinnost a podporuje pokročilé funkce jako frekvenčně selektivní plánování, víceuživatelské MIMO a komunikaci s nízkou latencí.

Dále, návrh PDCCH řeší výzvu kapacity a spolehlivosti řídicího kanálu. Použitím agregace CCE a adaptace spojení zajišťuje, že se řídicí informace mohou dostat k uživatelským zařízením i na okraji buňky. Zavedení vylepšeného PDCCH (EPDCCH) v LTE Rel-11 a kompletně přepracovaného NR-PDCCH v Rel-15 bylo motivováno potřebou zvýšené kapacity řídicího kanálu, lepší koordinace interference, podpory formování svazku a pružnosti pro různé případy užití, jako je masivní IoT a komunikace s ultra-spolehlivou nízkou latencí (URLLC). PDCCH je tedy primárním nástrojem vrstvy řízení přístupu k médiu (MAC) pro výkon její plánovací funkce, což jej činí nepostradatelným pro výkon moderních buňkových sítí.

## Klíčové vlastnosti

- Přenáší řídicí informace pro přenos směrem dolů (DCI) pro plánování
- Podporuje více formátů DCI pro oprávnění přenosu směrem nahoru, přiřazení přenosu směrem dolů a další příkazy
- Využívá agregaci prvků řídicího kanálu (CCE) pro adaptaci spojení (LTE)
- Funguje v rámci definované řídicí oblasti (LTE) nebo pružných sad řídicích zdrojů CORESET (NR)
- Vyžaduje, aby uživatelské zařízení monitorovalo sadu kandidátních PDCCH v prohledávacích prostorech
- Používá adresování specifických uživatelských zařízení nebo skupin pomocí zakódování CRC na základě RNTI

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.216** (Rel-19) — LTE Relay Node Physical Layer
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- … a dalších 33 specifikací

---

📖 **Anglický originál a plná specifikace:** [PDCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdcch/)
