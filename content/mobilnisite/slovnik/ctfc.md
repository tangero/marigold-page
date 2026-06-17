---
slug: "ctfc"
url: "/mobilnisite/slovnik/ctfc/"
type: "slovnik"
title: "CTFC – Calculated Transport Format Combinations"
date: 2025-01-01
abbr: "CTFC"
fullName: "Calculated Transport Format Combinations"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ctfc/"
summary: "CTFC je parametr používaný v UMTS k jednoznačné identifikaci konkrétní kombinace Transportních formátů (TF) napříč více transportními kanály multiplexovanými na jeden kódovaný složený transportní kaná"
---

CTFC je parametr v UMTS, který jednoznačně identifikuje konkrétní kombinaci transportních formátů napříč více kanály. Používá ho vrstva RRC k signalizaci povolených konfigurací přenosu nižším vrstvám.

## Popis

Vypočtené kombinace transportních formátů (CTFC) je základní koncept v rádiové přístupové síti UMTS (UTRAN), konkrétně definovaný v protokolu řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) (specifikace 25.331). Slouží jako kompaktní, vypočtený index, který reprezentuje konkrétní kombinaci transportních formátů (TFC). TFC definuje sadu transportních formátů (TF) současně aktivních na různých transportních kanálech (TrCH), které jsou spolu multiplexovány na jeden kódovaný složený transportní kanál (CCTrCH) pro přenos přes fyzickou vrstvu.

Z architektonického hlediska CTFC funguje na rozhraní mezi vrstvou RRC (vrstva 3) a nižšími vrstvami, především řízením přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)). Vrstva RRC je zodpovědná za konfiguraci rádiového beareru a definici sady povolených TFC, které může UE nebo NodeB používat na základě přidělených rádiových prostředků a požadavků QoS. Namísto signalizace úplného, podrobného popisu každého povoleného TFC obsahují konfigurační zprávy RRC seznam hodnot CTFC. Každá hodnota CTFC je vypočtené celé číslo, které jednoznačně odpovídá jedné konkrétní kombinaci transportních formátů napříč multiplexovanými transportními kanály.

Výpočet hodnoty CTFC je deterministický algoritmus definovaný ve specifikacích 3GPP. V podstatě zakóduje vybraný transportní formát (určený svým indikátorem transportního formátu, TFI) pro každý transportní kanál v rámci kombinace do jedné číselné hodnoty. Tento výpočet zohledňuje pořadí a konfiguraci transportních kanálů. Vrstva MAC po přijetí seznamu povolených CTFC od RRC může tyto hodnoty dekódovat, aby porozuměla kompletní sadě povolených přenosových rychlostí a velikostí bloků pro přenos. Během provozu MAC vybírá TFC z povolené sady na základě dostupnosti dat a priority a používá odpovídající identifikátor CTFC interně a pro reportování.

Role CTFC je klíčová pro efektivní signalizaci a dynamické řízení přenosové rychlosti. Minimalizuje signalizační režii v rekonfiguračních zprávách RRC, což je zásadní pro efektivitu sítě a životnost baterie UE. Dále poskytuje jasný, jednoznačný odkaz na povolené přenosové formáty, což umožňuje plánovači MAC rychle vybrat vhodnou kombinaci pro aktuální rádiové podmínky a stav datové fronty, což přímo ovlivňuje uživateli vnímanou propustnost dat a latenci.

## K čemu slouží

CTFC bylo zavedeno, aby vyřešilo problém efektivní signalizace a správy množství možných přenosových formátů v UMTS. V UMTS založeném na WCDMA jsou vícečetné transportní kanály (např. pro různé služby nebo logické kanály) multiplexovány na jeden fyzický kanál. Každý transportní kanál může pracovat s různými transportními formáty (definujícími velikost bloku, kódování atd.), což vede ke kombinatorické explozi možných kombinací transportních formátů (TFC). Explicitní signalizace každého možného TFC se všemi jeho parametry by byla z hlediska velikosti signalizačních zpráv a zpracovatelské režie nepřijatelně neefektivní.

Vytvoření CTFC bylo motivováno potřebou kompaktní, jednoznačné reprezentace. Před takovým mechanismem by správa přizpůsobení rychlosti a plánování vyžadovala složitou a objemnou signalizaci, která by zpomalovala rekonfiguraci a adaptaci na měnící se rádiové podmínky. CTFC poskytuje standardizovaný algoritmus pro výpočet jediného celočíselného indexu pro jakoukoli danou TFC. To umožňuje vrstvě [RRC](/mobilnisite/slovnik/rrc/) jednoduše odeslat seznam těchto indexů (CTFC), aby definovala povolenou sadu, což drasticky snižuje signalizační zátěž. Nižší vrstvy ([MAC](/mobilnisite/slovnik/mac/)) pak používají stejný standardizovaný algoritmus k interpretaci těchto indexů, čímž je zajištěna konzistence.

Tento přístup řeší omezení podrobnějších signalizačních metod, umožňuje rychlejší nastavení a rekonfiguraci rádiového beareru, dynamičtější řízení přenosové rychlosti a efektivní podporu smíšených služeb s různými požadavky QoS na stejném spojení. Je to klíčový prvek sofistikovaného paketového plánování a správy QoS, které odlišuje UMTS od dřívějších systémů 2G.

## Klíčové vlastnosti

- Poskytuje kompaktní celočíselný index reprezentující úplnou kombinaci transportních formátů
- Umožňuje efektivní signalizaci RRC snížením velikosti konfiguračních zpráv pro TFC
- Standardizovaný výpočetní algoritmus zajišťuje konzistentní interpretaci mezi vrstvami RRC a MAC
- Jednoznačně mapuje na konkrétní sadu transportních formátů (TF) pro všechny multiplexované transportní kanály
- Nezbytný pro dynamický výběr TFC plánovačem MAC na základě dostupnosti dat
- Základní pro přizpůsobení přenosové rychlosti a zpracování transportního kanálu v UMTS

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 45.902** (Rel-19) — Flexible Layer One (FLO) for GERAN

---

📖 **Anglický originál a plná specifikace:** [CTFC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctfc/)
