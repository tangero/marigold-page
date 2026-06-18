---
slug: "seg"
url: "/mobilnisite/slovnik/seg/"
type: "slovnik"
title: "SEG – Speech Expert Group"
date: 2026-01-01
abbr: "SEG"
fullName: "Speech Expert Group"
category: "Other"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/seg/"
summary: "Pracovní skupina 3GPP odpovědná za standardizaci řečových a audio kodeků, metod hodnocení kvality a souvisejících aspektů komplexního výkonu pro systémy mobilní komunikace. Zajišťuje vysoce kvalitní h"
---

SEG je pracovní skupina 3GPP odpovědná za standardizaci řečových a audio kodeků a hodnocení jejich kvality, aby zajistila vysoce kvalitní hlasové služby napříč mobilními systémy.

## Popis

Skupina expertů pro řeč (Speech Expert Group, SEG) je specializovaná technická pracovní skupina v rámci organizační struktury 3GPP, která působí pod Technickou specifikační skupinou pro služby a aspekty systémů ([TSG](/mobilnisite/slovnik/tsg/) [SA](/mobilnisite/slovnik/sa/)). Jejím hlavním úkolem je standardizace řečových a audio kodeků a také metodik pro testování a hodnocení jejich kvality a výkonu v mobilních sítích. Práce skupiny je klíčová pro zajištění interoperabilních, vysoce kvalitních hlasových a audio služeb ve všech systémech definovaných 3GPP, od GSM a UMTS přes LTE až po 5G. SEG sama nevyvíjí základní algoritmy kodeků, ale vybírá, profiluje a standardizuje kodeky vyvinuté externími orgány (jako [ITU-T](/mobilnisite/slovnik/itu-t/), [ETSI](/mobilnisite/slovnik/etsi/) nebo členskými společnostmi 3GPP) pro použití v ekosystému 3GPP.

Činnost SEG zahrnuje několik klíčových oblastí. Za prvé specifikuje datové toky, rámcové struktury a provozní režimy, které musí podporovat koncová zařízení a síťové prvky pro povinné kodeky, jako je adaptivní vícebitový kodek ([AMR](/mobilnisite/slovnik/amr/)) pro úzkopásmovou řeč a širokopásmový adaptivní vícebitový kodek ([AMR-WB](/mobilnisite/slovnik/amr-wb/)) pro [HD](/mobilnisite/slovnik/hd/) Voice. Za druhé definuje podrobný protokol pro vyjednávání kodeku a adaptaci režimu během sestavování hovoru a v jeho průběhu (pásmový signalizace), což je nezbytné pro robustní provoz v proměnných rádiových podmínkách. Za třetí skupina vyvíjí a udržuje testovací specifikace pro výkon kodeků, včetně metodik objektivního a subjektivního měření kvality (např. pomocí algoritmů [PESQ](/mobilnisite/slovnik/pesq/) nebo POLQA) a postupů testování shody, aby zajistila interoperabilitu mezi implementacemi různých dodavatelů.

Jak SEG pracuje, zahrnuje standardizační proces založený na konsenzu. Skupina posuzuje příspěvky členských společností, vyhodnocuje kandidátní kodeky prostřednictvím důkladných testovacích kampaní (často za účasti více nezávislých laboratoří) a vytváří technické specifikace, které definují profil kodeku pro 3GPP. Tyto specifikace pokrývají rozhraní kodeku k protokolům rádiového přístupu a jádra sítě, jeho adaptaci pro okruhově a paketově spínané domény (např. ve VoLTE a VoNR) a jeho integraci se službami jako je hlas přes IP a nouzové hovory. SEG se také zabývá novými požadavky na audio, jako je doručování hudby, vícekanálový zvuk a imerzivní audio zážitky, čímž rozšiřuje svůj rozsah mimo tradiční telefonní řeč. Její výstupy jsou integrální specifikace, které zajišťují, že uživatel v síti GSM může mít vysoce kvalitní hlasový hovor s uživatelem na 5G VoNR spojení s využitím nejvhodnějšího kodeku, který je mezi zařízeními a sítěmi bezproblémově vyjednán.

## K čemu slouží

SEG byla zformována, aby řešila základní požadavek na standardizovaný, vysoce kvalitní digitální hlas v mobilních sítích. V počátcích digitální celulární komunikace (GSM) by proprietární kodeky vedly k problémům s interoperabilitou a špatným uživatelským zážitkem. Účelem skupiny je poskytnout jedinou, dohodnutou sadu standardů řečových kodeků, které implementují všichni operátoři sítí a výrobci zařízení, čímž se zaručí, že hlasové hovory fungují spolehlivě a znějí dobře napříč různými sítěmi, zeměmi a typy zařízení. Řeší problém fragmentace a zajišťuje konzistentní základní úroveň kvality hlasu.

Historicky, jak se sítě vyvíjely od okruhově spínaného hlasu k hlasu přes paketovou síť (VoIP), role SEG se rozšířila o adaptaci řečových kodeků pro IP přenos, správu maskování ztrát paketů a definici požadavků na kvalitu služeb pro hlasové pakety. Motivací pro vytvoření a udržování SEG je neustálá snaha o zlepšení kvality hlasu (např. přechod od úzkopásmového k širokopásmovému a plnopásmovému audiu), zvýšení efektivity šířky pásma (lepší kvalita při nižších datových tocích) a podpora nových služeb jako hlas přes LTE (VoLTE) a hlas přes NR (VoNR). Skupina zajišťuje zpětnou kompatibilitu a zároveň umožňuje pokročilá vylepšení, vyvažuje kvalitu, složitost a interoperabilitu v každé nové verzi standardů 3GPP.

## Klíčové vlastnosti

- Standardizace a výběr povinných a volitelných řečových/audio kodeků pro systémy 3GPP
- Definice postupů pro vyjednávání kodeku a adaptaci režimu pro okruhově a paketově spínané domény
- Vývoj testovacích specifikací pro výkon kodeků a shodu
- Specifikace metodik objektivního a subjektivního hodnocení kvality řeči
- Profilace externích kodeků (např. od ITU-T) pro implementaci v sítích a zařízeních 3GPP
- Vývoj standardů kodeků pro podporu HD Voice, super-širokopásmového a plnopásmového audia

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [SA4 – Service and System Aspects Working Group 4](/mobilnisite/slovnik/sa4/)

## Definující specifikace

- **TS 29.204** (Rel-19) — SS7 Security Gateway Functional Description
- **TS 32.843** (Rel-13) — PS Domain Online Charging in Roaming
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.141** (Rel-19) — Security for Presence Service (Ut reference point)
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.203** (Rel-19) — IMS Security Specification
- **TS 33.210** (Rel-19) — UMTS Security for IP Networks
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 33.310** (Rel-19) — 3GPP Authentication Framework for Network Nodes
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.838** (Rel-11) — Study on Protection against Unsolicited Communication for IMS
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance
- **TS 46.085** (Rel-19) — GSM Speech Codec Interoperability Test Report

---

📖 **Anglický originál a plná specifikace:** [SEG na 3GPP Explorer](https://3gpp-explorer.com/glossary/seg/)
