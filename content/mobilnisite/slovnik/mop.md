---
slug: "mop"
url: "/mobilnisite/slovnik/mop/"
type: "slovnik"
title: "MOP – Maintenance Operations Protocol"
date: 2026-01-01
abbr: "MOP"
fullName: "Maintenance Operations Protocol"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mop/"
summary: "Protokol definovaný konsorciem 3GPP pro vzdálenou správu a údržbu síťových prvků. Umožňuje operátorům provádět správu poruch, monitorování výkonu a softwarové aktualizace, čímž zajišťuje spolehlivost"
---

MOP je protokol definovaný konsorciem 3GPP pro vzdálenou správu a údržbu síťových prvků, který umožňuje správu poruch, monitorování výkonu a softwarové aktualizace za účelem zajištění spolehlivosti sítě a provozní efektivity.

## Popis

Maintenance Operations Protocol (MOP) je standardizovaná sada protokolů v rámci specifikací 3GPP navržená pro provoz, správu a údržbu ([OAM](/mobilnisite/slovnik/oam/)) telekomunikačních síťových zařízení. Poskytuje rámec pro vzdálenou správu síťových prvků ([NE](/mobilnisite/slovnik/ne/)), jako jsou základnové stanice (eNodeB/gNB), uzly jádra sítě a další infrastrukturní komponenty. MOP definuje rozhraní, formáty zpráv a postupy nezbytné pro komunikaci systému pro podporu provozu ([OSS](/mobilnisite/slovnik/oss/)) nebo správce sítě ([NM](/mobilnisite/slovnik/nm/)) s řízenými síťovými prvky. Tato komunikace umožňuje klíčové funkce, jako je stažení a aktivace softwaru, správa konfigurace, dohled nad poruchami a sběr dat o výkonu.

Z architektonického hlediska MOP funguje v rámci řídicí roviny, odděleně od uživatelské a signalizační roviny. Typicky využívá model manažer-agent, kde OSS/NM vystupuje jako manažer iniciující operace a síťový prvek hostí agenta, který příkazy provádí a hlásí stav. Protokolový zásobník často spoléhá na podkladové transportní protokoly, jako je [TCP/IP](/mobilnisite/slovnik/tcp-ip/), pro spolehlivé doručování zpráv. Specifikace MOP podrobně popisují řadu spravovaných objektů ([MO](/mobilnisite/slovnik/mo/)), které reprezentují konfigurovatelné a monitorovatelné zdroje uvnitř síťového prvku, jako jsou hardwarové komponenty, softwarové moduly a logická rozhraní. Operace nad těmito objekty zahrnují vytvoření, čtení, aktualizaci, smazání ([CRUD](/mobilnisite/slovnik/crud/)), notifikace (pro alarmy a události) a přenos souborů pro softwarové balíčky.

Role MOP je zásadní pro dosažení automatizovaných, efektivních a standardizovaných síťových operací. Umožňuje centralizovanou správu sítí s více dodavateli tím, že poskytuje společný jazyk mezi systémy správy a zařízeními od různých výrobců. To snižuje provozní náklady, minimalizuje potřebu manuálních zásahů a urychluje nasazování nových služeb a funkcí. Díky umožnění vzdálené údržby je MOP nezbytný pro správu rozsáhlých, geograficky rozptýlených sítí, jako jsou sítě 5G, kde jsou návštěvy lokalit manuálně nepraktické. Jeho postupy zajišťují, že síťové prvky mohou být udržovány aktuální, monitorovány z hlediska stavu a opravovány nebo rekonfigurovány bez narušení uživatelských služeb.

## K čemu slouží

MOP byl vytvořen jako odpověď na rostoucí složitost a rozsah mobilních sítí, které činily manuální údržbu na místě stále nákladnější, pomalou a náchylnou k chybám. Před standardizací výrobci často používali proprietární protokoly pro správu prvků, což nutilo operátory používat více izolovaných systémů správy pro zařízení různých dodavatelů. To vedlo k vysokým provozním výdajům ([OPEX](/mobilnisite/slovnik/opex/)), problémům s integrací a bránilo automatizované, end-to-end poskytování služeb.

Hlavní motivací pro standardizaci MOP v rámci 3GPP bylo umožnit interoperabilitu více dodavatelů v řídicí rovině. Definováním společného protokolu mohli operátoři používat jediný OSS nebo správce sítě pro řízení a údržbu zařízení od různých dodavatelů. To podporuje konkurenci, snižuje závislost na jediném dodavateli a zjednodušuje síťové operace. Navíc, jak se sítě vyvíjely od 3G přes 4G k 5G a zahrnovaly koncepty jako virtualizace síťových funkcí (NFV) a síťové řezy, stala se potřeba agilního, softwarově řízeného a automatizovaného řízení životního cyklu prvořadá. MOP poskytuje základní mechanismy pro tyto pokročilé operace, jako je instanciace, škálování a samoléčení virtualizovaných síťových funkcí (VNF). Řeší problém udržování kontinuity služeb a spolehlivosti sítě ve stále více softwarově definovaných a hustých síťových prostředích.

## Klíčové vlastnosti

- Standardizované rozhraní pro správu síťových prvků od více dodavatelů
- Podpora správy softwaru včetně stažení, aktivace a vrácení zpět
- Správa konfigurace pro provisionování a aktualizaci spravovaných objektů
- Správa poruch prostřednictvím dohledu nad alarmy a notifikačních postupů
- Správa výkonu pro sběr a reportování dat o měřeních
- Schopnosti přenosu souborů pro logistiku, jako jsou softwarové balíčky a zálohy konfigurace

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TR 28.813** (Rel-17) — Study on New Energy Efficiency Aspects for 5G
- **TR 28.825** (Rel-17) — 5G Network Sharing Management Study
- **TS 32.130** (Rel-19) — Network Sharing OAM&P Requirements
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.755** (Rel-15) — US 600 MHz LTE Band 71 Technical Report
- **TS 36.858** (Rel-14) — LTE 2.6 GHz SDL Band Technical Report
- **TS 37.814** (Rel-12) — L-band Supplemental Downlink for UTRA/E-UTRA
- **TR 37.880** (Rel-17) — High-power UE for fixed-wireless/vehicle use
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.741** (Rel-19) — NTN L-/S-band for NR Technical Specification
- **TS 38.831** (Rel-16) — UE RF Requirements for FR2 Enhancements
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [MOP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mop/)
