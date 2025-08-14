---
author: Patrick Zandl
categories:
- AI
- Google
- Gemini
- CLI
- VSCode
- MCP
layout: vibecoding-default
post_excerpt: Google vydal aktualizaci Gemini CLI s hlubokou integrací do VS Code, podporou multimodálního obsahu v MCP serverech a řadou vylepšení uživatelského rozhraní.
summary_points:
- Gemini CLI nyní nabízí nativní integraci s VS Code včetně kontextového navrhování a diff náhledů
- Přidána podpora pro multimodální obsah (obrázky, audio) ve výstupech MCP nástrojů
- Nové funkce zahrnují zpětné vyhledávání příkazů, adaptivní rozvržení terminálu a pokročilé nastavení komprese kontextu
- Vývojáři mohou nyní spravovat MCP servery přímo z příkazové řádky pomocí gemini mcp příkazů
- Aktualizace v0.1.20 přináší desítky menších vylepšení pro lepší uživatelský zážitek
- CLI nástroj od společnosti Google umožňuje práci s modely Gemini přímo z terminálu
title: Google vylepšil Gemini CLI o integraci s VS Code a multimodální podporu
---

Google vydal významnou aktualizaci svého nástroje Gemini CLI, který umožňuje vývojářům pracovat s modely umělé inteligence Gemini přímo z příkazové řádky. Verze 0.1.20 přináší zejména hlubokou integraci s editorem VS Code, rozšířenou podporu pro Model Context Protocol (MCP) servery a řadu vylepšení uživatelského rozhraní.

## Nativní integrace s VS Code

Nejvýznamnější novinkou je přímá integrace s populárním editorem VS Code. Když vývojáři spustí Gemini CLI z integrovaného terminálu VS Code, získají přístup k inteligentním návrhům založeným na kontextu aktuálně otevřených souborů. Systém dokáže analyzovat obsah editoru a poskytovat relevantní doporučení přímo v prostředí, kde programátoři běžně pracují.

Integrace zahrnuje také nativní zobrazování rozdílů (diff), které umožňuje vývojářům snadno kontrolovat a upravovat navrhované změny přímo v editoru. Tato funkce zjednodušuje workflow při refaktoringu kódu nebo implementaci nových funkcí s pomocí umělé inteligence. Pro spuštění nástroje v prostředí VS Code slouží standardní příkaz v terminálu, přičemž správu integrace zajišťuje příkaz `/ide`.

Podrobnosti o nové integraci jsou dostupné v [oficiálním blogu Google Developers](https://developers.googleblog.com/en/gemini-cli-vs-code-native-diffing-context-aware-workflows).

## Rozšířená podpora MCP protokolu

Aktualizace výrazně vylepšuje podporu pro Model Context Protocol, který umožňuje připojení externích nástrojů a služeb k jazykovým modelům. Vývojáři nyní mohou spravovat MCP servery přímo z příkazové řádky pomocí nových příkazů `gemini mcp add`, `remove` a `list`. Tato funkcionalita zjednodušuje konfiguraci a správu externích nástrojů bez nutnosti ručních úprav konfiguračních souborů.

Významnou novinkou je podpora multimodálního obsahu ve výstupech MCP nástrojů. Servery nyní mohou vracet nejen textové informace, ale také obrázky, zvukové soubory a další typy médií. Gemini CLI tyto výstupy dokáže zpracovat a zobrazit, což rozšiřuje možnosti použití u aplikací pracujících s multimediálním obsahem.

Systém také získal podporu pro MCP kořenové adresáře (MCP roots), což umožňuje lepší organizaci a správu připojených služeb. Nově jsou podporovány i servery, které poskytují pouze příkazy typu slash commands bez dalších funkcí.

## Vylepšení uživatelského rozhraní

Aktualizace přináší několik významných vylepšení pro práci s terminálem. Rozvržení CLI se nyní automaticky přizpůsobuje úzkým oknům terminálu, což zlepšuje použitelnost na menších obrazovkách nebo při práci s rozdělenými okny.

Nová funkce zpětného vyhledávání příkazů umožňuje vývojářům rychle najít dříve použité příkazy stisknutím kombinace kláves Ctrl+R v shell režimu. Tato funkcionalnost je inspirována standardními shell nástroji a výrazně zrychluje opakování častých operací.

Systém také získal pokročilé možnosti konfigurace komprese kontextu. Vývojáři mohou v konfiguračním souboru `settings.json` nastavit procentuální hranici kontextového okna, při které se automaticky spouští komprese. Toto nastavení pomáhá optimalizovat výkon při práci s velkými projekty.

## Konfigurační možnosti

Nová verze rozšiřuje možnosti přizpůsobení podle potřeb jednotlivých vývojářů. V konfiguračním souboru lze nyní deaktivovat oznámení o dostupných aktualizacích nastavením `"disableUpdateNag": true`. Tato možnost je užitečná zejména v podnikových prostředích s řízenou správou softwarových aktualizací.

Přibyla také podpora pro automatické načítání více adresářů při spuštění pomocí nastavení `"includeDirectories"` v konfiguraci. Vývojáři tak mohou definovat seznam adresářů, které se mají načíst do kontextu při každém spuštění nástroje.

Pro lepší přehlednost při kopírování kódu lze skrýt číslování řádků v blokách kódu nastavením `"showLineNumbers": false`. Tato možnost zjednodušuje sdílení kódových úryvků bez nutnosti ručního odstraňování čísel řádků.

## Technické podrobnosti

Gemini CLI je open-source nástroj dostupný na [GitHub repozitáři](https://github.com/google-gemini/gemini-cli), který umožňuje vývojářům integrovat možnosti modelů Gemini přímo do svého vývojového workflow. Nástroj podporuje práci se soubory, editaci kódu a spouštění příkazů s pomocí umělé inteligence.

Instalace nejnovější verze 0.1.20 je možná pomocí npm balíčkovacího systému příkazem `npm i -g @google/gemini-cli`. Aktualizace je doporučena všem uživatelům kvůli významným vylepšením stability a funkcionalitě.

Kromě hlavních novinek obsahuje aktualizace také desítky menších vylepšení, která zlepšují celkový uživatelský zážitek. Detailní seznam všech změn je dostupný v [diskusním vlákně na GitHubu](https://github.com/google-gemini/gemini-cli/discussions/6160).

Model Context Protocol představuje standardizovaný způsob připojení externích nástrojů a datových zdrojů k jazykovým modelům. Díky rozšířené podpoře v Gemini CLI mohou vývojáři snadněji integrovat vlastní nástroje a služby do AI-powered workflow, aniž by museli implementovat proprietární řešení.