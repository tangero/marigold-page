---
slug: "nmc"
url: "/mobilnisite/slovnik/nmc/"
type: "slovnik"
title: "NMC – Network Management Centre"
date: 2025-01-01
abbr: "NMC"
fullName: "Network Management Centre"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nmc/"
summary: "Network Management Centre (NMC) je centralizované pracoviště nebo systém odpovědný za monitorování, řízení a správu telekomunikační sítě. Slouží jako operační centrum, kde se agregují informace o stav"
---

NMC je centralizované pracoviště nebo systém odpovědný za monitorování, řízení a správu telekomunikační sítě, které slouží jako operační centrum pro udržování kvality služeb a řešení problémů.

## Popis

Network Management Centre (NMC) představuje centrální operační a administrativní uzel pro správu telekomunikační sítě. Nejde o jediný protokol nebo rozhraní, ale o funkční koncept zahrnující fyzickou lokalitu, personál a integrovaný soubor Operations Support Systems ([OSS](/mobilnisite/slovnik/oss/)) používaných pro komplexní správu sítě. NMC poskytuje jednotný přehled o stavu, výkonu a konfiguraci sítě, agreguje data z různých podsítí, technologií (2G/3G/4G/5G, přenosová síť, core) a vendor-specific Element Management Systems ([EMS](/mobilnisite/slovnik/ems/)).

Z architektonického hlediska se NMC nachází na vrcholu hierarchie Telecommunications Management Network ([TMN](/mobilnisite/slovnik/tmn/)), nad Element Management Layer ([EML](/mobilnisite/slovnik/eml/)) a Network Element Layer (NEL). Rozhraní se systémy EMS a někdy přímo s Network Elements (NEs) pomocí standardizovaných (např. Itf-N) nebo proprietárních rozhraní. Mezi klíčové systémy v rámci NMC patří Fault Management ([FM](/mobilnisite/slovnik/fm/)) systémy pro dohled nad alarmy a správu tiketů, Performance Management ([PM](/mobilnisite/slovnik/pm/)) systémy pro sběr a analýzu [KPI](/mobilnisite/slovnik/kpi/), Configuration Management ([CM](/mobilnisite/slovnik/cm/)) systémy pro provisioning a správu softwaru a často také funkce Security Management (SM) a Accounting Management (AM). Tyto systémy jsou integrovány tak, aby poskytovaly korelované přehledy napříč doménami.

Jak funguje: NMC nepřetržitě přijímá proudy dat – alarmy, měření výkonu, aktualizace konfigurace a logy událostí – z celé sítě. Systémy Fault Management korelují alarmy za účelem identifikace hlavních příčin a prezentují operátorům filtrovaný přehled. Systémy Performance Management zpracovávají data KPI za účelem detekce degradací, generování reportů a spouštění thresholdů. Systémy Configuration Management umožňují operátorům zavádět nové síťové služby, aktualizovat software na síťových prvcích a měnit parametry. Úlohou NMC je převést toto obrovské množství dat na využitelné informace, což umožňuje centralizované řízení a kontrolu pro zajištění dostupnosti sítě, její efektivity a poskytování služeb.

## K čemu slouží

Koncept NMC vznikl ze základní potřeby spravovat stále větší, složitější a více-vendorové telekomunikační sítě z centralizovaného místa. Před vznikem sofistikovaných NMC byla správa sítě často decentralizovaná, manuální a reaktivní, přičemž technici spravovali jednotlivé síťové prvky nebo malé domény. Tento přístup se stal neudržitelným s růstem sítí, což vedlo k vysokým provozním nákladům, pomalým reakčním dobám a obtížím při diagnostice problémů napříč doménami.

NMC tyto problémy řeší tím, že poskytuje centralizovanou viditelnost, kontrolu a automatizaci. Umožňuje malému týmu expertů monitorovat celou síť, korelovat události napříč různými technologiemi (rádio, core, přenosová síť) a provádět koordinované změny. Je motivován snahou o provozní efektivitu, snížení OPEX, zlepšení kvality služeb a zkrácení doby uvedení nových služeb na trh. Vývoj NMC úzce souvisí s vývojem standardizovaných rámců pro správu, jako je TMN a specifikace Network Management (NM) od 3GPP, které umožňují integraci zařízení od více dodavatelů do jednotného přehledu správy.

## Klíčové vlastnosti

- Centralizované centrum pro komplexní monitorování a řízení sítě
- Integruje funkce správy poruch (Fault), výkonu (Performance), konfigurace (Configuration), zabezpečení (Security) a účtování (Accounting)
- Poskytuje jednotný, korelovaný přehled o více-technologických, více-vendorových sítích
- Umožňuje korelaci alarmů, analýzu hlavních příčin a automatizované generování tiketů
- Podporuje monitorování výkonu, reportování a plánování kapacity na základě analýzy KPI
- Umožňuje centralizovanou správu softwaru, provisioning a aktualizace síťové konfigurace

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)
- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [NMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/nmc/)
