---
author: Patrick Zandl
categories:
- AI
- IDE
- Windsurf
- Codeium
- vývoj software
layout: post
post_excerpt: Windsurf představil Wave 12 s funkcemi DeepWiki, Vibe and Replace a podporou vývojových kontejnerů pro pokročilé úpravy kódu.
summary_points:
- DeepWiki umožňuje získat vysvětlení kódových symbolů přímo v editoru pomocí umělé inteligence
- Funkce Vibe and Replace nabízí hromadné úpravy kódu s použitím AI promptů
- Přidána podpora vývojových kontejnerů a vylepšený agent Cascade s automatickým plánováním
- Redesign uživatelského rozhraní pro lepší přehlednost v panelech Chat a Cascade
- Rychlejší funkce Tab s lepšími návrhy a méně rušivým rozhraním
- Windsurf je AI-nativní IDE od společnosti Codeium s více než milionem vývojářů
title: Windsurf představil Wave 12 s funkcemi DeepWiki a Vibe and Replace
---

Společnost Codeium vydala novou verzi své vývojové platformy [Windsurf](https://windsurf.com/) s označením Wave 12, která přináší významné rozšíření možností editoru kódu s využitím umělé inteligence. Hlavními novinkami jsou funkce DeepWiki pro vysvětlování kódu, Vibe and Replace pro pokročilé úpravy a podpora vývojových kontejnerů.

## DeepWiki - inteligentní dokumentace kódu

Klíčovou novinkou je funkce DeepWiki, která poskytuje vysvětlení kódových symbolů přímo v editoru. Při najetí myší nad symbol v kódu získá vývojář vysvětlení generované umělou inteligencí, které překračuje běžné typové informace dostupné v tradičních editorech. Kombinací kláves Cmd/Ctrl+Shift+Click lze otevřít podrobné vysvětlení v postranním panelu a přidat je jako kontext pro agenta Cascade.

Tato funkce využívá znalosti z celého projektu pro vytvoření kontextového vysvětlení, které pomáhá vývojářům pochopit složitější části kódu bez nutnosti ručního prohledávání dokumentace. DeepWiki tak efektivně nahrazuje časově náročné hledání informací o funkcích a metodách.

## Vibe and Replace - hromadné úpravy s AI

Druhá zásadní novinka je funkce Vibe and Replace, která umožňuje provádět inteligentní hromadné úpravy napříč celým projektem. Vývojář může najít přesné textové shody v kódu a následně aplikovat AI prompty pro kontextově vědomé transformace. Systém dokáže provést změny na více místech současně s respektováním kontextu každého výskytu.

Funkce je užitečná především při refaktoringu kódu, kdy je třeba upravit podobné konstrukce na různých místech projektu. Místo manuálního hledání a nahrazování může vývojář popsat požadovanou změnu v přirozeném jazyce a nechat AI provést odpovídající transformace.

## Vylepšení agenta Cascade

Agent Cascade získal automatický režim plánování, který eliminuje nutnost manuálního přepínání mezi módy. Systém nyní vytváří autonomní seznamy úkolů a využívá přepracované nástroje pro přesnější úpravy kódu. Cascade také lépe využívá dlouhokontextové modely pro prozkoumávání kódu.

Cascade je základní funkcí Windsurf, která umožňuje vývojářům spolupracovat s AI na úlohách přesahujících jednoduchá doplnění kódu. Agent může provádět změny v mnoha souborech současně a udržuje přehled o postupu práce.

## Podpora vývojových kontejnerů

Wave 12 přidává podporu pro vývojové kontejnery přes vzdálený SSH přístup. Vývojáři tak mohou pracovat s kontejnerizovanými prostředími přímo z Windsurf IDE bez nutnosti lokální instalace závislostí. Tato funkce je zvlášť užitečná při práci s projekty vyžadujícími specifické nastavení prostředí.

## Redesign uživatelského rozhraní

Nová verze obsahuje kompletní redesign panelů Chat a Cascade pro lepší přehlednost při sledování akcí agenta a porozumění volání nástrojů. Vylepšení se týkají především vizualizace postupu práce a snadnějšího pochopení kroků, které AI provádí.

Funkce Tab autocomplete byla zrychlena s novým modelem poskytujícím častější a přesnější návrhy. Uživatelské rozhraní je méně rušivé a používá lepší algoritmus pro zobrazení rozdílů v kódu.

## O společnosti Windsurf

Windsurf je AI-nativní vývojové prostředí od společnosti Codeium, které používá více než milion vývojářů. Platforma se zaměřuje na udržení vývojářů v produktivním stavu pomocí pokročilých AI funkcí. Codeium původně začínala jako infrastrukturní společnost pro virtualizaci GPU, později se však přesunula k vývoji nástrojů pro programátory.

Společnost dosáhla valuace jedné miliardy dolarů a nabízí jak bezplatnou verzi pro individuální vývojáře, tak podnikové řešení. Windsurf konkuruje dalším AI editorům jako je Cursor, přičemž se odlišuje podporou více vývojových prostředí a zaměřením na podnikové zákazníky.

Wave 12 je dostupná ke stažení na [oficiálních stránkách Windsurf](https://windsurf.com/) pro operační systémy Mac, Windows a Linux.