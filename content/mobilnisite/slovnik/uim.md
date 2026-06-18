---
slug: "uim"
url: "/mobilnisite/slovnik/uim/"
type: "slovnik"
title: "UIM – Umbrella Information Model"
date: 2025-01-01
abbr: "UIM"
fullName: "Umbrella Information Model"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/uim/"
summary: "Standardizovaný informační model pro řízení telekomunikačních sítí, který poskytuje obecný rámec pro reprezentaci dat. Umožňuje konzistentní konfiguraci, řízení poruch, výkonu a zabezpečení v prostřed"
---

UIM je standardizovaný informační model, který poskytuje obecný rámec pro reprezentaci dat, aby umožnil konzistentní konfiguraci, řízení poruch, výkonu a zabezpečení v telekomunikačních síťích s více dodavateli a více technologiemi.

## Popis

Umbrella Information Model (UIM) je komplexní, technologicky neutrální informační model definovaný 3GPP pro řízení síťových procesů. Funguje jako základní schéma, které popisuje řízené objekty, jejich atributy, operace a vztahy v telekomunikační síti. Model je strukturován pomocí objektově orientovaných principů a je typicky vyjádřen v modelovacím jazyce, jako je [UML](/mobilnisite/slovnik/uml/) (Unified Modeling Language). Poskytuje standardizovaný způsob reprezentace síťových prostředků, služeb a souvisejících řídicích dat, které jsou pak mapovány na specifické protokolové datové modely, například ty používané [SNMP](/mobilnisite/slovnik/snmp/) nebo NETCONF/YANG.

Architektonicky je UIM jádrem Systému řízení 3GPP a komunikuje s Model síťových prostředků ([NRM](/mobilnisite/slovnik/nrm/)) a dalšími doménově specifickými modely. Definuje sadu základních tříd a balíků, které zachycují obecné řídicí koncepty použitelné v různých síťových doménách, včetně základní síťové části (Core Network) a rádiové přístupové síťové části (Radio Access Network). Klíčové komponenty obsahují třídy pro reprezentaci řízených elementů, zařízení, software, poruch, měření výkonu a konfiguračních dat. Tyto třídy jsou odvozeny z obecného kořene a vytvářejí vztahy, jako je obsahování a závislost, což vytváří jednotný pohled na síť.

Operačně UIM umožňuje řídicím aplikacím komunikovat s síťovými elementy konzistentním způsobem. Když je zaváděna nová síťová funkce nebo technologie, její řídicí interface může být definován jako rozšíření UIM, což zajišťuje zpětnou kompatibilitu a snižuje komplexnost integrace. Role modelu je oddělit řídicí sémantiku od podkladových komunikačních protokolů a datového kódování, což umožňuje flexibilnější a odolnější řídicí řešení. Je integrální částí vize 3GPP pro automatizované, samoorganizující se síťové části tím, že poskytuje strukturovaný datový základ nutný pro analytické procesy a orchestraci.

## K čemu slouží

UIM byl vytvořen k řešení kritického problému řízení rostoucí heterogenity a komplexnosti telekomunikačních sítí. Před jeho standardizací systémy řízení síťových procesů často závisely na proprietárních, dodavatelsky specifických informačních modelech, což vedlo k vážným problémům interoperabilnosti. To značně ztěžovalo a zvyšovalo náklady na integraci zařízení od více dodavatelů, automatizaci operačních úloh a implementaci řízení služeb end-to-end. Rozšíření nových technologií a síťových funkcí v ekosystému 3GPP tento problém ještě prohloubilo.

Primární motivací pro vývoj UIM bylo vytvoření jediného, autoritativního zdroje pravdivých informací pro řízení všech síťových entit definovaných 3GPP. Poskytnutím obecného jazyka a datového schématu řeší problém sémantické nekonzistence mezi různými řídicími interfaces. Tato standardizace snižuje operační náklady ([OPEX](/mobilnisite/slovnik/opex/)) tím, že umožňuje vývoj obecných řídicích aplikací a nástrojů, které mohou pracovat s jakýmkoli kompatibilním síťovým elementem, bez ohledu na podkladový hardware nebo dodavatele software.

Historicky jeho zavádění ve Release 11 bylo částí širšího úsilí v 3GPP formalizovat a sjednotit řídicí rámce, v souladu s průmyslovými trendy směřujícími k řízení řízenému modely a software-defined networking. Řeší omezení předchozích fragmentovaných přístupů tím, že zajišťuje konzistentní reprezentaci řídicích dat pro poruchy, konfiguraci, výkon, účtování a zabezpečení (FCAPS), a tím umožňuje automatizované provisioning, assurance a řízení životního cyklu v moderních síťových částích 5G a dalších.

## Klíčové vlastnosti

- Technologicky neutrální základní model pro řízené objekty
- Objektově orientovaný design využívající UML pro jasnou sémantiku a vztahy
- Poskytuje základ pro odvození protokolově specifických datových modelů (např. pro SNMP, NETCONF/YANG)
- Podporuje interoperabilitu řízení síťových procesů s více dodavateli a více technologiemi
- Umožňuje konzistentní reprezentaci FCAPS (Fault, Configuration, Accounting, Performance, Security) dat
- Usnadňuje automatizaci síťových procesů a orchestraci prostřednictvím standardizované výměny informací

## Související pojmy

- [NRM – Network Resource Model](/mobilnisite/slovnik/nrm/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)

## Definující specifikace

- **TS 28.620** (Rel-19) — FMC Federated Network Information Model (FNIM) UIM
- **TS 28.821** (Rel-13) — UML Model Repertoire for FMC Management
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.103** (Rel-19) — 3GPP Management IRP Overview
- **TS 32.107** (Rel-19) — Federated Network Information Model (FNIM)

---

📖 **Anglický originál a plná specifikace:** [UIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/uim/)
