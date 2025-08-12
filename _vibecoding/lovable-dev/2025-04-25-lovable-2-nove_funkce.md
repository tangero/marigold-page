---
layout: vibecoding-default
title: "Lovable 2.0: Nové funkce pro AI tvorbu webových aplikací"
sw: databutton
date: 2025-04-25
---



Aplikace Lovable koncem dubna vydala očekávanou verzi 2.0 své AI platformy pro vytváření webových aplikací pomocí přirozeného jazyka. Aktualizace přináší multiplayer spolupráci, Chat Mode Agent, bezpečnostní skenování, přímou editace kódu a zjednodušené ceny. Pojďme se na novinky podívat podrobněji:

## Multiplayer spolupráce s workspace systémem

Lovable 2.0 zavádí workspace systém pro týmovou spolupráci. Pro uživatele se rozděluje na dva plány: Pro subscription pro osobní workspace s možností pozvat až 2 spolupracovníky na jednotlivé projekty, a Teams subscription podporující až 20 uživatelů ve sdíleném workspace.

Teams plán obsahuje tři role: Owners a admins mohou přidávat a odebírat uživatele, zatímco Editors mohou pouze spravovat a editovat existující projekty. Všichni uživatelé ve workspace sdílejí společný pool kreditů. Spolupracovníci na jednotlivém projektu používají kredity vlastníka projektu.

Systém je určen pro startupy a menší podnikové týmy, které potřebují centralizovanou fakturaci a synchronizaci práce na stejné aplikaci.

## Chat Mode Agent pro plánování a debugging

Chat Mode Agent představuje oddělený režim, který neprovádí přímé změny v kódu. Slouží k kladení otázek, plánování projektů a ladění chyb. Agent pracuje "agenticky" - dokáže uvažovat napříč více kroky a rozhodovat o tom, kdy prohledávat soubory, kontrolovat logy nebo dotazovat databázi.

Tato funkce odděluje konzultační činnosti od aktivní editace kódu, což umožňuje uživatelům získat rady a analýzy bez rizika nechtěných změn v projektu.

## Security Scan pro Supabase aplikace

Funkce Security Scan automaticky kontroluje bezpečnostní zranitelnosti v aplikacích připojených k Supabase databázi. Aktivuje se při publikování projektu a je dostupná pouze pro projekty využívající Supabase backend.

Lovable uvádí, že jde o první krok k zabezpečení "vibe coding" - termínu pro plné spoléhání na AI při generování kódu. Nicméně bezpečnostní komunita identifikovala kritické problémy s CVE-2025-48757, které postihují 170 z 1,645 skenovaných Lovable aplikací kvůli nesprávně nakonfigurovaným Row Level Security politikám.

## Dev Mode pro přímou editaci kódu

Dev Mode umožňuje editovat kód projektu přímo v Lovable editoru. Funkce byla zavedena několik týdnů před vydáním verze 2.0 a podle společnosti získala pozitivní ohlasy uživatelů.

Tento režim řeší problém vývojářů, kteří chtějí provádět přesné úpravy bez nutnosti exportu a importu kódu z externích editorů. Integrace s GitHub umožňuje synchronizaci změn.

## Visual Edits pro rychlé úpravy stylů

Visual Edits poskytuje grafické rozhraní pro úpravu stylů elementů bez psaní CSS kódu. Uživatelé mohou upravovat margin, padding, velikost textu, barvy a další vlastnosti prostřednictvím panelu nástrojů.

Funkce existuje několik měsíců a podle Lovable byla vylepšena pro větší robustnost. Cílí na uživatele bez hlubších znalostí CSS, kteří chtějí rychle upravit vzhled aplikace.

## Custom Domains a hosting

Lovable 2.0 integruje nákup a připojení vlastních domén přímo do platformy. Od zavedení této funkce bylo připojeno více než 10,000 vlastních domén k Lovable aplikacím.

Tato integrace eliminuje nutnost externí konfigurace hostingu a DNS nastavení, což zjednodušuje proces nasazení aplikací pro netechnické uživatele.

## Zjednodušené ceny

Cenová struktura byla upravena na dva jasné plány:
- Pro plán: flexibilní úrovně začínající na 25 dolarů měsíčně
- Teams plán: 30 dolarů měsíčně pro týmy vyžadující sdílené workspace

Předchozí komplikovaný systém plateb za zprávy byl nahrazen transparentními měsíčními poplatky.

## Technické pozadí a výkon

Lovable, původně známý jako GPT Engineer, se rebrandoval v listopadu 2024. Platforma používá React, Tailwind CSS a Vite pro frontend a integruje se s Supabase pro backend služby. Využívá modely od OpenAI, Google Gemini a Anthropic Claude Sonnet 3.7.

Společnost hlásí 30,000 platících zákazníků, 500,000+ celkových uživatelů a 85% first-month retention rate. Denně se vytváří 25,000+ nových produktů.

## Porovnání s konkurencí

**Replit** nabízí podobný přístup k AI asistovanému vývoji, ale s důrazem na tradiční programovací prostředí. Replit Agent podporuje více programovacích jazyků, zatímco Lovable se zaměřuje specificky na webové aplikace s React. Replit má silnější community features a lepší chat support, ale Lovable poskytuje uživatelsky přívětivější rozhraní pro netechnické uživatele.

**Databutton** se specializuje na Python aplikace a data science projekty, zatímco Lovable cílí na full-stack webové aplikace. Databutton má lepší integraci s machine learning workflow, ale Lovable poskytuje komplexnější frontend možnosti.

**Bolt.new** konkuruje v oblasti React komponentů, ale Lovable nabízí hlubší databázovou integraci přes Supabase a komplexnější full-stack funkcionalita.

## Bezpečnostní problémy a komunita

Výzkumníci z Replitu a bezpečnostní specialisté objevili kritické zranitelnosti v Lovable aplikacích. CVE-2025-48757 s CVSS skóre 8,26/10 umožňuje útočníkům obejít přístupová omezení pomocí modifikace HTTP požadavků.

Guardio Labs ohodnotil Lovable pouze 1,8/10 v bezpečnostních testech kvůli náchylnosti k vytváření phishingových stránek. CEO Replit Amjad Masad veřejně kritizoval bezpečnostní přístup Lovable.

Technická komunita na Reddit a Hacker News vyjadřuje obavy ohledně kvality AI-generovaného kódu a reportuje error loops během složitých debugging scenářů.


Platformě Lovable chybí komplexnější debugging nástroje a lepší kvalita generovaného kódu. Pro úspěch v enterprise segmentu bude nutné vyřešit bezpečnostní problémy a zlepšit stabilitu AI agentů při složitějších úkolech.

Lovable 2.0 úspěšně demokratizuje tvorbu základních webových aplikací, ale zůstává primárně nástrojem pro prototypování než produkční vývoj...