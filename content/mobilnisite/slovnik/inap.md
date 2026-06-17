---
slug: "inap"
url: "/mobilnisite/slovnik/inap/"
type: "slovnik"
title: "INAP – Intelligent Network Application Protocol"
date: 2025-01-01
abbr: "INAP"
fullName: "Intelligent Network Application Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/inap/"
summary: "Signalizační protokol používaný pro komunikaci mezi funkčními entitami Inteligentní sítě (IN), například mezi Service Switching Point (SSP) a Service Control Point (SCP). Přenáší dotazy a instrukce pr"
---

INAP je signalizační protokol používaný pro komunikaci mezi funkčními entitami Inteligentní sítě, například mezi Service Switching Point a Service Control Point, pro realizaci pokročilých telekomunikačních služeb.

## Popis

Intelligent Network Application Protocol (INAP) je transakčně orientovaný signalizační protokol aplikační vrstvy standardizovaný [ITU-T](/mobilnisite/slovnik/itu-t/) (řada Q.1218) a přijatý ve specifikacích 3GPP. Funguje nad zásobníkem signalizačního systému č. 7 (SS7), konkrétně využívá jako transport Transaction Capabilities Application Part (TCAP). INAP definuje zprávy a procedury, které umožňují distribuovaný interaktivní dialog mezi Service Switching Function (SSF) na Service Switching Point (SSP) a Service Control Function (SCF) na Service Control Point (SCP). Tento dialog je klíčovým mechanismem pro poskytování služeb založených na [IN](/mobilnisite/slovnik/in/).

INAP funguje prostřednictvím série operací a chybových stavů. Když událost hovoru na SSP odpovídá nakonfigurovanému Detection Point ([DP](/mobilnisite/slovnik/dp/)), SSF sestaví INAP zprávu Initial Detection Point ([IDP](/mobilnisite/slovnik/idp/)). Tato zpráva obsahuje podrobnosti o hovoru (volané/volající číslo, lokalitu atd.) a konkrétní spouštěč, který byl detekován. SSP odešle tuto IDP zprávu přes TCAP/SS7 na SCP. Servisní logika na SCP tyto informace zpracuje, případně se dotáže Service Data Point (SDP) na další data, a následně rozhodne, jak má být hovor zpracován. SCP odpoví jednou nebo více INAP operačními zprávami, aby SSP vydal instrukce. Mezi tyto operace mohou patřit "Connect" pro směrování hovoru na konkrétní číslo, "PlayAnnouncement" pro přehrání hlasové zprávy volajícímu, "RequestReportBCSMEvent" pro aktivaci budoucích spouštěčů nebo "ApplyCharging" pro řízení účtování u předplacených služeb.

Protokol je definován pomocí Abstract Syntax Notation One (ASN.1), což umožňuje přesnou, na platformě nezávislou specifikaci struktur zpráv. Byly standardizovány různé varianty neboli "capability sets" (CS-1, CS-2 atd.) INAP, z nichž každá přidává složitější operace a podporu širších servisních scénářů. V rámci 3GPP je INAP zvláště relevantní pro standard Customized Applications for Mobile network Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)), kde se používá jeho varianta specifická pro mobilní sítě nazvaná CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)). CAP je odvozen od INAP, ale obsahuje rozšíření přizpůsobená funkcím mobilních sítí, jako je správa mobility a interakce s GSM Service Control Function (gsmSCF). INAP/CAP tak tvoří klíčové signalizační pojivo, které umožňuje fungování distribuované architektury IN.

## K čemu slouží

INAP byl vytvořen, aby poskytl standardizovaný, na dodavateli nezávislý jazyk pro klíčový komunikační spoj v architektuře Inteligentní sítě: spoj mezi ústřednou (SSP) a servisním řadičem (SCP). Před INAP, pokud chtěl operátor zavést pokročilou službu, dodavatel ústředny poskytl proprietární rozhraní ke svému vlastnímu SCP, což vedlo k uzavřeným ekosystémům a závislosti na dodavateli. To znemožňovalo operátorovi kombinovat ústředny od jednoho dodavatele se servery servisní logiky od jiného, což výrazně omezovalo flexibilitu a zvyšovalo náklady.

Protokol tento problém řeší definicí kompletní sady abstraktních operací, které pokrývají všechny nezbytné interakce pro řízení služeb, nezávisle na implementaci podkladové hardwarové ústředny nebo softwarového SCP. To umožňuje interoperabilitu mezi více dodavateli. Vytvoření INAP bylo motivováno snahou telekomunikačního průmyslu o otevřené standardy v 80. a 90. letech 20. století, poháněnou deregulací a touhou po zvýšení konkurence a inovací. Umožnilo realizaci vize [IN](/mobilnisite/slovnik/in/), kde služby mohly být vytvořeny jednou a nasazeny v síti skládající se z zařízení od více dodavatelů.

V kontextu 3GPP bylo přijetí a odkaz na INAP (a jeho derivát [CAP](/mobilnisite/slovnik/cap/)) zásadní pro přenesení služeb IN do globálních mobilních sítí. Mobilní sítě přinesly složitosti, jako je roaming a mobilita účastníka, které pevné INAP původně neřešilo. 3GPP potřebovalo protokol, který by podporoval kontinuitu služeb, když se účastník přesouval mezi síťovými oblastmi nebo sítěmi různých operátorů. Zatímco se CAP stal primárním protokolem pro mobilní IN, základní principy a mnoho operací INAP zůstalo zachováno, což zajistilo, že se klíčový koncept standardizovaného signalizačního řízení služeb zachoval a rozšířil pro mobilní éru.

## Klíčové vlastnosti

- Standardizovaná sada operací (např. InitialDP, Connect, PlayAnnouncement, ApplyCharging) pro řízení služeb IN
- Jako spolehlivý transportní mechanismus využívá TCAP nad SS7
- Definován pomocí ASN.1 pro jednoznačné kódování a dekódování zpráv
- Podporuje více úrovní schopností (CS-1, CS-2) pro vyvíjející se složitost služeb
- Umožňuje dialog typu dotaz-odpověď mezi SSP (ústřednou) a SCP (serverem servisní logiky)
- Základ pro protokol CAMEL Application Part (CAP) používaný v mobilních sítích

## Související pojmy

- [IN – Intelligent Network](/mobilnisite/slovnik/in/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.198** (Rel-9) — OSA API Overview Specification
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [INAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/inap/)
