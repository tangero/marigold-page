---
author: Patrick Zandl
categories:
- AI
- Cursor
- Nástroje pro vývoj
layout: post
post_excerpt: Cursor přidal režim Plan, který umožňuje AI navrhovat změny kódu před jejich realizací. Novinka cílí na větší projekty a komplexnější úpravy.
summary_points:
- Cursor představil nový režim Plan pro plánování změn v kódu před jejich implementací
- Režim umožňuje AI navrhnout úpravy napříč více soubory a konzultovat je s vývojářem
- Funkce cílí na větší projekty, kde přímé úpravy kódu mohou být riskantní
- Plan mode využívá pokročilé modely jako Claude Sonnet 4.5 nebo GPT-4.5 Preview
- Nástroj nabízí dvoustupňový proces - návrh změn a jejich následné provedení
- Přístup k režimu Plan mají uživatelé placených tarifů Pro a Business
title: Cursor přidal režim Plan pro konzultaci změn kódu s AI
---

Vývojové prostředí Cursor rozšířilo své možnosti o [režim Plan](https://cursor.com/blog/plan-mode), který mění způsob interakce AI s kódem. Místo okamžitých úprav systém nejprve navrhne změny a teprve po schválení vývojářem je provede.

## Jak režim Plan funguje

Režim Plan přidává do pracovního postupu mezikrok mezi zadáním požadavku a realizací změn. Vývojář zadá úkol, AI analyzuje kódovou základnu a vytvoří plán úprav. Ten zahrnuje seznam dotčených souborů, popis navrhovaných změn a odůvodnění jednotlivých kroků. Vývojář pak může plán upravit, doplnit instrukce nebo jej rovnou schválit k provedení.

Cursor doporučuje režim Plan především pro složitější úkoly zasahující více souborů. Podle týmu je vhodný zejména v situacích, kdy vývojář potřebuje kontrolu nad rozsahem změn nebo když AI nemá dostatek kontextu pro přímou implementaci.

## Technické parametry

Režim Plan využívá pokročilé jazykové modely - Claude Sonnet 4.5 nebo GPT-4.5 Preview (OpenAI o1). Tyto modely dokážou pracovat s větším kontextovým oknem a komplexnějšími úkoly než standardní režim úprav.

Funkce je dostupná pro uživatele tarifů Pro a Business. Zdarma lze režim Plan použít dvakrát denně, placené tarify nabízejí padesát použití měsíčně. Překročení limitu je možné za příplatek.

## Srovnání s konkurencí

Přístup Cursoru odpovídá trendu v AI nástrojích pro vývoj. Windsurf od Codeium nabízí podobnou funkci Cascade, která rovněž umožňuje schvalování návrhů před implementací. Aider, open-source alternativa, pracuje s konceptem “architect mode” pro návrh změn.

Režim Plan také připomína workflow AI agentů, kde systém nejprve vytvoří plán akcí a teprve po schválení je provede. Tento přístup snižuje riziko nechtěných změn v produkčním kódu.

## Praktické využití

Cursor uvádí konkrétní scénáře použití. Režim Plan se hodí při refaktoringu rozsáhlých částí kódu, implementaci nových funkcí zasahujících více modulů nebo při úpravách, kde AI potřebuje dodatečné instrukce. Méně vhodný je pro rychlé opravy chyb nebo drobné úpravy v jednotlivých souborech.

Vývojáři mohou v režimu Plan také klást upřesňující otázky před provedením změn. Systém pak upraví plán podle nových informací.​​​​​​​​​​​​​​​​