---
author: Patrick Zandl
categories:
- AI
- Anthropic
- Claude
- Claude Code
- programování
- vývojářské nástroje
layout: post
post_excerpt: Anthropic vydal Claude Code 2.0 s funkcí /rewind pro rychlé vrácení změn, rozšířením pro VS Code a novým SDK pro vývojáře agentů
summary_points:
- Claude Code 2.0 přináší funkci /rewind pro okamžité vrácení posledních změn pomocí Esc+Esc
- Nové rozšíření pro VS Code umožňuje práci přímo v integrovaném vývojovém prostředí
- Claude Agent SDK poskytuje vývojářům stejné nástroje, které používá Claude Code
- API získalo pokročilé správy kontextu s context editing a memory nástrojem
- K dispozici jsou modely Sonnet 4.5 a Opus 4.1, Sonnet 4.5 vykazuje výrazně lepší výkon
title: Anthropic představil Claude Code 2.0 s vrácením změn a rozšířením pro VS Code
---

Společnost Anthropic právě představila aktualizovanou verzi svého nástroje pro programování Claude Code 2.0. Hlavními novinkami jsou funkce rychlého vrácení změn v kódu, rozšíření pro Visual Studio Code a nový SDK pro vývojáře agentů. Současně představila pokročilé funkce pro správu kontextu v Claude API - a navíc má nový [model Sonnet 4.5](https://www.marigold.cz/item/claude-sonnet-4-5/), který je opět o kousek lepší. 



## Klíčové novinky Claude Code 2.0

- Nový Sonnet 4.5 
- Nativní rozšíření VSCode 
- Kontrolní body ke kterým se dá /rewind
- Neustálé myšlení (snad bude fungovat) - aktivujete Tabem a je perzistentní přes seance
- čištění kontextu, když se blížíte limitu

Nejvýraznější funkcí nové verze je možnost **rychlého vrácení změn** do kontrolního bodu pomocí příkazu `/rewind` nebo klávesové zkratky Esc+Esc. Tato funkce umožňuje vývojářům okamžitě zrušit poslední změny provedené umělou inteligencí, což výrazně zrychluje iterativní vývoj. Do téhle doby byla předchozí práce ztracena, nebo jste si museli commitovat do Gitu a vrátit se přes Git. 

K dispozici je také nový příkaz `/usage` pro sledování spotřeby tokenů.

Claude Code 2.0 přinesl přepracované terminálové rozhraní a hlavně nové rozšíření pro Visual Studio Code. Vývojáři tak mohou pracovat s Claude přímo ve svém oblíbeném integrovaném vývojovém prostředí, aniž by museli přepínat mezi aplikacemi. Rozšíření je dostupné v [oficiálním marketplace VS Code](https://code.visualstudio.com/). Vypadá to moc pěkně, ale ještě jsem na něj nepřešel. 

Podle prvních zkušeností uživatelů je nová verze rychlejší při generování odpovědí a umožňuje paralelní volání nástrojů a agentů. Zatímco Claude pracuje na ladění kódu, může současně požádat o povolení k načtení webové stránky nebo spuštění dalších úloh.

## Claude Agent SDK pro vývojáře

Anthropic současně představil [Claude Agent SDK](https://anthropic.com/engineering/building-ai-agents-claude-code-sdk), který poskytuje vývojářům přístup ke stejným základním nástrojům, systémům správy kontextu a oprávněním, které pohánějí Claude Code. SDK umožňuje vytváření vlastních agentů s pokročilými schopnostmi správy kódu a automatizace vývojářských úloh.

SDK obsahuje všechny komponenty potřebné pro vytvoření robustních agentů, včetně správy souborového systému, spouštění příkazů a integraci s vývojářskými nástroji. Vývojáři tak mohou vytvářet specializované agenty pro konkrétní úlohy jako testování, refaktoring nebo nasazení aplikací.

## Pokročilá správa kontextu v API

Claude API získalo dvě zásadní funkce pro správu kontextu - context editing a memory nástroj. Context editing automaticky odstraňuje zastaralý kontext při dosažení limitů tokenů, zatímco memory nástroj ukládá informace mimo okno kontextu pro dlouhodobé použití.

Tyto funkce demonstroval Anthropic na příkladu hry Catan, kde Claude buduje databázi strategií protivníků a průběžně aktualizuje zastaralé informace. Agenti tak mohou zvládat delší a složitější úlohy bez ztráty důležitých informací z předchozích fází práce.

Správa kontextu rozšiřuje možnosti agentů v těchto oblastech:
- Automatické čištění zastaralého kontextu při přiblížení k limitům tokenů
- Ukládání informací mimo kontextové okno pro dlouhodobé využití
- Udržování konzistentních znalostí během dlouhotrvajících úloh

Kompletní dokumentace je k dispozici na [docs.claude.com](https://docs.claude.com/en/docs/build-with-claude).

## Změny v dostupných modelech

Claude Code 2.0 nyní nabízí pouze modely Sonnet 4.5 a Opus 4.1, přičemž byl odstraněn dříve dostupný model Opus v plánovací verzi. Podle uživatelských zkušeností vykazuje Sonnet 4.5 výrazně lepší výkon než předchozí verze a často převyšuje i model Opus 4.1 v programovacích úlohách.

Model Sonnet 4.5 přináší vylepšenou schopnost pochopení kontextu, rychlejší generování kódu a lepší práci s komplexními projekty. Pro většinu vývojářských úloh se tak stává preferovanou volbou před výkonnějším, ale pomalejším modelem Opus 4.1.

Claude Code je dostupný prostřednictvím příkazové řádky a představuje klíčový nástroj Anthropic pro segmenti vývojářů, kde konkuruje podobným řešením od OpenAI a dalších poskytovatelů jazykových modelů. Aktualizace posiluje pozici Claude v oblasti automatizace programování a správy kódu.