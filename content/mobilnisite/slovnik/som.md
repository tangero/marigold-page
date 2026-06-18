---
slug: "som"
url: "/mobilnisite/slovnik/som/"
type: "slovnik"
title: "SOM – Service Operations Management"
date: 2025-01-01
abbr: "SOM"
fullName: "Service Operations Management"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/som/"
summary: "SOM je řídicí rámec a soubor standardů 3GPP pro správu operačního životního cyklu telekomunikačních služeb. Poskytuje principy, architekturu a požadavky pro poskytovatele služeb, aby mohli efektivně p"
---

SOM je řídicí rámec a soubor standardů 3GPP pro správu operačního životního cyklu telekomunikačních služeb, který poskytuje principy a architekturu pro poskytování, konfiguraci, zajištění kvality a účtování služeb.

## Popis

Service Operations Management (SOM) je komplexní řídicí rámec definovaný v technické specifikaci 3GPP 32.101. Zahrnuje procesy, funkce a informační modely potřebné pro správu operačního životního cyklu služeb v telekomunikačním prostředí. SOM není jediný nástroj, ale standardizovaná referenční architektura, která usměrňuje implementaci Operations Support Systems ([OSS](/mobilnisite/slovnik/oss/)) a Business Support Systems ([BSS](/mobilnisite/slovnik/bss/)). Pokrývá celé spektrum od koncepce a návrhu služby přes její poskytnutí, plnění, zajištění kvality, účtování až po případné vyřazení.

Architektura SOM je typicky popsána pomocí funkčních vrstev. Její jádro tvoří funkce správy služeb (Service Management Functions), které interagují s funkcemi správy zdrojů (Resource Management Functions – spravují podkladové síťové elementy) a funkcemi obchodní správy (Business Management Functions – řeší vztahy se zákazníky a účtování). Mezi klíčové procesy v SOM patří správa konfigurace služeb (nastavení parametrů služby), správa problémů služeb (řešení poruch a degradací ovlivňujících službu), správa kvality služeb (monitorování a reportování plnění smluv o úrovni služeb – [SLA](/mobilnisite/slovnik/sla/)) a správa účtování služeb (sledování využití služeb pro účely fakturace). Tyto procesy spoléhají na standardizované informační modely, například definované pomocí [UML](/mobilnisite/slovnik/uml/), aby zajistily konzistenci dat a interoperabilitu mezi různými řídicími systémy od různých dodavatelů.

SOM funguje na principu definování logického oddělení mezi vrstvou služeb a vrstvou síťových zdrojů. Tato abstrakce je klíčová. Zákaznická služba (např. '5G Enhanced Mobile Broadband s VoIP') je realizována orchestraci a konfigurací mnoha podkladových síťových zdrojů (např. síťových řezů, [PDU](/mobilnisite/slovnik/pdu/) session, QoS toků). SOM poskytuje řídicí schopnosti pro mapování požadavků služby na konfigurace zdrojů, monitorování celkového stavu a výkonu služby a provádění nápravných opatření v případě porušení SLA. Jeho úlohou je umožnit efektivní, automatizované a na zákazníka zaměřené operace, což je zásadní pro moderní komplexní služby, jako jsou síťové řezy, IoT a edge computing.

## K čemu slouží

SOM byl vytvořen, aby řešil rostoucí složitost a dynamickou povahu telekomunikačních služeb. V raných mobilních sítích byly služby relativně jednoduché (primárně hlas a [SMS](/mobilnisite/slovnik/sms/)) a jejich správa byla často manuální a izolovaná. Jak se sítě vyvíjely a začaly nabízet širokou škálu datových služeb, multimediálního obsahu a přizpůsobených podnikových řešení, stala se standardizovaná přístup ke správě služeb nezbytností. Nedostatek standardizace vedl k vysokým provozním nákladům, dlouhé době uvedení nových služeb na trh, obtížím se zajištěním kvality služeb od konce ke konci a výzvám při integraci více-dodavatelských prostředí [OSS](/mobilnisite/slovnik/oss/)/[BSS](/mobilnisite/slovnik/bss/).

Počáteční specifikace ve verzi (Release) 8 stanovila základní principy, podnícené potřebou společného rámce po přijetí IP Multimedia Subsystem (IMS) a rozšíření datových služeb. SOM poskytuje plán pro automatizaci operací životního cyklu služeb, což je klíčové pro škálování operací, snížení lidských chyb a zlepšení zákaznické zkušenosti. Řeší problém správy s ohledem na službu tím, že jako spravovanou entitu zaměřuje na zákaznickou službu, nikoli pouze na jednotlivé síťové elementy. To operátorům umožňuje efektivně spravovat balíčky služeb, garantovat SLA a rychle uvádět nové služby, což jsou klíčové konkurenční výhody na telekomunikačním trhu.

## Klíčové vlastnosti

- Standardizovaný rámec pro správu životního cyklu telekomunikačních služeb od konce ke konci
- Definuje klíčové procesy: Plnění (Fulfillment), Zajištění kvality (Assurance), Účtování (Billing) a Konfigurace
- Podporuje abstrakci mezi logikou služby a podkladovými síťovými zdroji
- Umožňuje automatizaci a orchestraci nasazení a provozu služeb
- Poskytuje základ pro správu a monitorování smluv o úrovni služeb (SLA)
- Usnadňuje integraci mezi systémy pro podporu provozu (OSS) a systémy pro podporu podnikání (BSS)

## Definující specifikace

- **TS 32.101** (Rel-19) — Management principles and high-level requirements

---

📖 **Anglický originál a plná specifikace:** [SOM na 3GPP Explorer](https://3gpp-explorer.com/glossary/som/)
