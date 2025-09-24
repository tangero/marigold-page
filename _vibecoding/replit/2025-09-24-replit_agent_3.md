---
author: Patrick Zandl
categories:
- AI
- Replit
- Agent 3
- Vývojářské nástroje
- Automatizace
- Autonomní systémy
layout: post
post_excerpt: Replit uvádí Agent 3, který je 10× autonomnější než předchozí verze. Dokáže testovat aplikace v prohlížeči, vytvářet další agenty a pracovat až 200 minut bez dozoru.
summary_points:
- Agent 3 je 10× autonomnější než Agent V2 s možností práce až 200 minut bez dozoru
- Automatické testování aplikací v reálném prohlížeči s opravami chyb
- Schopnost vytvářet další agenty a automatizace pro Slack, Telegram a další platformy
- Nový workflow pro tvorbu aplikací s volbou mezi rychlým prototypováním a full-stack vývojem
- Dostupný pro všechny uživatele včetně bezplatných účtů s novým cenovým modelem
- Proprietární testovací systém je 3× rychlejší a 10× levnější než Computer Use modely
title: Replit Agent 3 - až 200 minut samostatnosti!
---

Replit představil Agent 3, novou generaci svého autonomního vývojářského nástroje, který má být posunem směrem k plně samostatné tvorbě softwaru. Oproti předchozí verzi Agent V2 je nový systém desetkrát autonomnější a dokáže pracovat až 200 minut bez lidského zásahu

![Replit Agent 3 Testování](https://cdn.replit.com/sanity/blog/Screenshot%202025-09-10%20at%207.13.02%E2%80%AFAM.png)


## Automatické testování v reálném prohlížeči

Klíčovou novinkou Agent 3 je schopnost automatického testování vytvářených aplikací přímo v prohlížeči. Systém periodicky rozhoduje, kdy je vhodné aplikaci otestovat, a následně simuluje chování skutečného uživatele - kliká na tlačítka, vyplňuje formuláře, testuje API a datové zdroje.

![App Testing Interface](https://cdn.replit.com/sanity/blog/app%20testing.png)

Během testování lze sledovat, jak agent naviguje aplikací prostřednictvím browseru v rámci Agent panelu, kde je viditelný kurzor simulující uživatelské akce. Po dokončení testů agent poskytne souhrn nalezených problémů a automaticky je opraví. Systém dokáže dokonce testovat přihlašovací procesy u aplikací využívających Replit Auth.

Proprietární testovací systém Replitu je podle společnosti třikrát rychlejší a desetkrát levnější než srovnatelné Computer Use modely. Testování není spouštěno po každé uživatelské zprávě, ale pouze když agent vyhodnotí, že došlo k dostatečným změnám oprávňujícím test.

## Vytváření dalších agentů a automatizací

Agent 3 přináší zcela novou schopnost - může vytvářet další specializované agenty a automatizace. Uživatelé mohou na domovské stránce vybrat možnost "Agents & Automations" a následně popsat požadovaný workflow přirozeným jazykem.

![Agents & Automations](https://cdn.replit.com/sanity/blog/blog-agents.png)

Systém umožňuje vytváření různých typů automatizovaných řešení:
- Slack boty odpovídající na otázky o kódové základně prostřednictvím integrace s GitHub
- Telegram boty pro rezervaci schůzek přímo v Outlook kalendáři
- Automatizované denní e-maily shrnující úkoly z Linear
- Boty pro dotazování informací z Notion databáze
- Automatizované přípravy na schůzky s vyhledáváním informací o hostech

![Automation Dashboard](https://cdn.replit.com/sanity/blog/automation.png)

Na jedné straně workspace je standardní Agent panel, na druhé straně místo náhledu aplikace se zobrazuje administrátorský dashboard pro testování chatbota nebo workflow automatizace. Na rozdíl od běžných Replit aplikací zde není náhled - agenti a automatizace se nasazují pro použití na externích platformách.

## Zjednodušená integrace s externími službami

Agent 3 výrazně zjednodušuje napojení na externí služby jako Notion, Linear, Dropbox či SharePoint. Místo ručního vyhledávání a kopírování API klíčů agent prezentuje jednoduché UI pro ověření, které provede uživatele celým procesem připojení.

![Service Connectors](https://cdn.replit.com/sanity/blog/connectors.png)

Po dokončení ověření agent bezpečně získá potřebná oprávnění a pokračuje v automatickém budování funkcionality. Tento přístup výrazně snižuje technickou bariéru pro uživatele, kteří chtějí integrovat své automatizace s podnikovými nástroji.

## Rozšířená autonomní doba běhu

Agent 3 dokáže pracovat autonomně až 200 minut, což představuje dramatické navýšení oproti předchozím verzím. Během této doby zvládá kompletní úkoly - budování, testování a opravování aplikací s minimálním lidským dohledem.

![Autonomous Runtime](https://cdn.replit.com/sanity/blog/autonomous%20run.png)

Funkce "Max Autonomy" v beta verzi umožňuje agentovi:
- Prodloužené relace bez nutnosti uživatelského vstupu
- Vytváření a zpracovávání delších seznamů úkolů
- Monitorování vlastního pokroku během relace

Uživatelé mogeou sledovat pokrok projektu v reálném čase na domovské stránce nebo prostřednictvím live monitoringu na mobilním telefonu.

## Nový workflow pro vytváření aplikací

Replit přepracoval proces vytváření aplikací s ohledem na různé potřeby uživatelů. Nový systém nabízí dvě cesty:

![New App Creation Flow](https://cdn.replit.com/sanity/blog/new%20creation%20flow.png)

**Rychlé prototypování**: Agent nejprve vytvoří frontend pro rychlou iteraci designu a testování uživatelského rozhraní. Backend lze přidat později podle potřeby.

**Full-stack vývoj**: Kompletní aplikace se vytváří od začátku včetně backend funkcionality a databázového připojení.

Tento přístup umožňuje vývojářům vybrat si optimální strategii podle charakteru projektu a požadavků na rychlost dodání.

## Cenový model a dostupnost

Agent 3 je dostupný všem uživatelům včetně těch s bezplatnými účty. Společnost implementovala nový "effort-based pricing" model, kde se účtují "checkpointy" na základě složitosti dokončené práce.

Standardní Replit Core plán pro jednotlivce stojí 20 dolarů měsíčně při roční platbě. Podle Replitu mnoho uživatelů nevyčerpá měsíční kredit a nemusí platit nad rámec předplatného. Power uživatelé pak platí dodatečné poplatky proporcionálně k hodnotě, kterou od agenta získávají.

Cenový model vyvolal smíšené reakce - zatímco Replit zdůrazňuje efektivitu svého testovacího systému, někteří uživatelé vyjádřili obavy z nepředvídatelných nákladů. Jeden uživatel na Redditu hlásil poplatek 350 dolarů za jediný den používání.

## Konkurenční prostředí a budoucnost

Agent 3 vstupuje na konkurenční trh AI asistovaného programování, kde působí nástroje jako Cursor (oceněný na 10 miliard dolarů), GitHub Copilot od Microsoftu nebo nabídky Googlu. Replit se odlišuje důrazem na autonomii, integrované testování a možnost generování dalších agentů.

Společnost plánuje další rozšíření autonomních schopností s více integracemi, trigger-based automatizacemi a dalšími aktualizacemi. Cílem je učinit budování jakékoliv aplikace na Replitu jednodušším než kdykoli předtím.

