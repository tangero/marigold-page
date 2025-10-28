---
author: Patrick Zandl
categories:
- AI
- GitHub
- Copilot
- Microsoft
layout: post
post_excerpt: GitHub představil Agent HQ, platformu pro orchestraci vývojářských agentů od Anthropic, OpenAI, Google a dalších přímo v prostředí GitHub s jednotným řízením.
summary_points:
- GitHub uvádí Agent HQ jako otevřený ekosystém pro správu vývojářských agentů přímo v platformě GitHub
- Agenti od Anthropic, OpenAI, Google, Cognition a xAI budou dostupní v rámci předplatného GitHub Copilot
- Mission Control funguje jako jednotné řídicí centrum napříč GitHub, VS Code, mobilem a příkazovou řádkou
- VS Code získává režim plánování a podporu MCP registru pro připojení nástrojů jako Stripe nebo Figma
- GitHub Code Quality přináší kontrolu kvality kódu zaměřenou na udržovatelnost a technický dluh
- Řídicí panel ukazuje metriky využití Copilot napříč organizací
title: GitHub uvádí Agent HQ, platformu pro správu vývojářských agentů
---

GitHub oznamuje Agent HQ, novou vrstvu, která má sloužit jako sjednocující prostředí pro práci s vývojářskými agenty. Platforma spojuje agenty od různých dodavatelů do jednoho ekosystému, kde je možné je řídit pomocí známých principů Gitu, tj. pomocí žádostí o začlenění změn a evidování úkolů. Agenti budou dostupní v rámci placeného předplatného GitHub Copilot.

Tady musím říct, že článek vychází z oficiálních informací, sám jsem ještě neměl možnost službu vyzkoušet, nepoužívám Copilota. 

## Otevřený ekosystém pro agenty

GitHub staví Agent HQ na myšlence, že budoucnost vývoje spočívá v orchestraci specializovaných agentů, kteří provádějí složité úkoly paralelně. Platforma má v následujících měsících získat přístup k agentům od Anthropic, OpenAI, Google, Cognition a xAI. První dostupný agent je OpenAI Codex, který mohou uživatelé Copilot Pro+ používat ve VS Code Insiders již tento týden.

Základní principy práce se nemění - vývojáři stále pracují s Gitem, žádostmi o začlenění změn a evidováním úkolů. Použít lze jak GitHub Actions, tak vlastní výpočetní prostředí. Agent HQ staví nad těmito základy další vrstvu možností.

## Mission Control jako řídicí centrum

Jádrem Agent HQ je Mission Control, jednotné řídicí centrum, které funguje napříč platformami. Není to samostatné místo, ale konzistentní rozhraní v prostředí GitHub, VS Code, mobilní aplikaci i příkazové řádce. Vývojář může vybrat agenty, přidělit jim práci paralelně a sledovat jejich postup z libovolného zařízení.

Mission Control nabízí několik nových možností:

Nové ovládací prvky větví poskytují podrobnou kontrolu nad tím, kdy se má spustit průběžná integrace a další kontroly pro kód vytvořený agenty. Funkce identity umožňují řídit, který agent provádí úkol, a spravovat přístupy a pravidla stejně jako u jakéhokoli jiného člena týmu. Mission Control je také ve VS Code, takže vývojář má jednotný přehled o všech agentech běžících ve VS Code, v příkazové řádce Copilot nebo na GitHubu.

## Plánování a vlastní agenti ve VS Code

VS Code získává režim plánování (Plan Mode), který spolupracuje s Copilotem a pokládá upřesňující otázky při tvorbě postupu pro řešení úkolu. Poskytnutí kontextu předem zlepšuje výsledky Copilotu a pomáhá odhalit mezery nebo nedostatky projektu ještě před psaním kódu. Po schválení plánu jej Copilot začne provádět, ať už lokálně ve VS Code, nebo pomocí agenta v cloudu.

Pro jemnější kontrolu je nyní možné vytvořit vlastní agenty ve VS Code pomocí souborů AGENTS.md. Tyto soubory pod správou verzí umožňují nastavit pravidla, například "použij tento zapisovač logů" nebo "použij testy řízené tabulkou pro všechny obsluhy". Tím se ovlivňuje chování Copilotu bez nutnosti opakovaného zadávání pokynů.

VS Code je jediný editor, který podporuje plnou specifikaci MCP (Model Context Protocol). Nový GitHub MCP Registry je dostupný přímo ve VS Code. Vývojáři mohou objevovat, instalovat a aktivovat MCP servery jako Stripe, Figma nebo Sentry jediným kliknutím. Při řešení specializovaného úkolu je možné vytvořit vlastní agenty v GitHub Copilot s vlastním systémovým pokynem a nástroji.

## Pro jaké úkoly je Agent HQ určen

Agent HQ se zaměřuje na několik kategorií vývojářských úloh. Hlavním využitím je orchestrace více specializovaných agentů, kteří pracují současně na různých částech projektu. Vývojář může rozdělit velký úkol mezi různé agenty podle jejich specializace a sledovat postup všech paralelních prací z jednoho místa.

Platforma je určena pro rutinní vývojářské práce - psaní kódu podle specifikace, úpravy a refaktoring existujícího kódu nebo opravy chyb identifikovaných při kontrolě. Režim plánování pomáhá při tvorbě postupů řešení před začátkem kódování, identifikaci mezer a chybějících rozhodnutí v projektu nebo návrhu implementace s upřesňujícími otázkami.

Praktický příklad využití může vypadat následovně: vývojář potřebuje přidat platební bránu do webové aplikace. V režimu plánování nejprve projde s Copilotem kroky implementace - integrace API, zpracování chyb, zabezpečení, testy. Po schválení plánu může přidělit jeden úkol agentovi pro vytvoření základní integrace se Stripe (pomocí MCP serveru pro Stripe), druhému agentovi pro implementaci zpracování chyb a třetímu pro psaní testů. Všechny tři agenty sleduje z Mission Control, zatímco se sám věnuje jinému projektu. Když agenti dokončí práci, Code Quality automaticky zkontroluje dopad na udržovatelnost kódu ještě před lidským přezkoumáním.

Agent HQ také podporuje integraci externích nástrojů přes MCP - propojení s platformami jako Stripe, Figma nebo Sentry pro specializované úkoly vyžadující konkrétní nástroje nebo API. V oblasti kontroly kvality nabízí automatickou kontrolu kódu před lidským přezkoumáním, posouzení dopadu změn na udržovatelnost a spolehlivost nebo řešení technického dluhu.

GitHub v oznámení nezmiňuje, pro jaké úkoly Agent HQ není vhodný. Nejasné zůstává například, jak dobře agenti zvládají netriviální architektonická rozhodnutí, nebo jak se vyrovnají s doménovými znalostmi specifickými pro konkrétní projekt, které nejsou nikde zdokumentovány.

![Přidání zvýrazněn syntaxe](https://www.marigold.cz/assets/copilot-agent.webp)

## Kontrola kvality a metriky

GitHub Code Quality, nyní ve veřejné testovací verzi, poskytuje viditelnost, správu a hlášení napříč organizací pro systematické zlepšování udržovatelnosti, spolehlivosti a pokrytí testy u každého repozitáře. Rozšiřuje bezpečnostní kontroly Copilotu o posouzení dopadu na udržovatelnost a spolehlivost měněného kódu.

Do pracovního postupu agenta Copilot je přidán krok kontroly kódu, takže Copilot získá počáteční kontrolu a vyřeší problémy ještě před tím, než vývojář kód uvidí. Problém, který GitHub řeší, spočívá v tom, že schválení při kontrole kódu ne vždy znamená zdravý kód - kontrola může projít, ale kód stále může vést k technickému dluhu.

Pro organizace je k dispozici řídicí panel metrik Copilot ve veřejné testovací verzi. Ukazuje dopad Copilotu a klíčové metriky využití napříč celou organizací. Správci podniků získávají řídicí rovinu pro správu přístupu k umělé inteligenci, včetně agentů a MCP. Mohou nastavovat bezpečnostní pravidla, protokolování auditu a spravovat přístup na jednom místě. Správci podniků také mohou řídit, kteří agenti jsou povoleni, definovat přístup k modelům a získat metriky o využití Copilotu v organizaci.

## Kontext podle GitHubu

GitHub zdůrazňuje, že Agent HQ není o shromažďování nástrojů, ale o integraci agentů do existujícího pracovního postupu. Platforma má 180 milionů vývojářů a roste nejrychleji v historii - nový vývojář se připojuje každou sekundu. Osmdesát procent nových vývojářů používá Copilot během prvního týdne.

Agent HQ se má stát odpovědí na roztříštěnost současné krajiny umělé inteligence, kde je výkon rozdělen mezi různé nástroje a rozhraní. GitHub chce zajistit, aby nová éra spolupráce byla výkonná, bezpečná a bezproblémově integrovaná do důvěryhodného pracovního postupu.

Více informací o Agent HQ je dostupných na [blogu GitHub](https://github.blog/news-insights/company-news/welcome-home-agents/).
