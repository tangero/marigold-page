---
author: Patrick Zandl
categories:
- AI
- Anthropic
- Claude Code
- vývojové nástroje
layout: post
post_excerpt: Claude Code pokračuje ve vývoji verze 2.0 s novými agentními dovednostmi, styly výstupu a vylepšeními stability pro Bedrock a Vertex AI.
summary_points:
- Agentní dovednosti umožňují Claude Code dynamicky načítat specializované znalosti z adresářů s instrukcemi a skripty
- Styly výstupu transformují základní osobnost agenta z inženýra na jakéhokoli specialistu bez ztráty nástrojů a kontextu
- Verze 2.0.1 opravila kritické problémy s výchozím modelem Sonnet 4.5 pro uživatele AWS Bedrock a Google Vertex AI
- Rozšíření pro VS Code prošlo opravami fokusování vstupu a stability na různých platformách
- Integrované nástroje ripgrep a rozšířená podpora pro Alpine Linux zlepšují výkon při práci se soubory
- Nový háček SessionEnd umožňuje automatické úklidové operace při ukončení relace
title: Claude Code rozvíjí verzi 2.0 s agentními dovednostmi a styly výstupu
---

Anthropic pokračuje ve vývoji nástroje Claude Code s řadou vylepšení navazujících na vydání verze 2.0. Aktuální verze přinášejí agentní dovednosti pro dynamické načítání znalostí, styly výstupu pro transformaci osobnosti agenta a řadu oprav stability především pro platformy AWS Bedrock a Google Vertex AI. Pojďme si to podrobněji projít. 

__Co konkrétně se v tomto článku dozvíte?__ 
* Obsah
{:toc}

## Skills: Agentní dovednosti pro dynamické načítání znalostí

Anthropic představil [agentní dovednosti](https://www.anthropic.com/news/skills) (Agent Skills), které umožňují Claude Code dynamicky načítat specializované znalosti podle potřeby úlohy. Dovednost představuje adresář obsahující soubor `SKILL.md` s metadaty a instrukcemi, případně doplněný o skripty a další zdroje.

Agent při startu načte pouze názvy a popisy všech dostupných dovedností do systémového příkazu. Když uživatel zadá úlohu, která odpovídá popisu některé dovednosti, Claude do kontextového okna načte kompletní obsah této dovednosti včetně podrobných instrukcí. Tímto mechanismem progresivního odhalování informací se do kontextu dostává pouze relevantní obsah, zatímco zbývající dovednosti zůstávají ve formě metadata.

Dovednosti mohou obsahovat skripty pro deterministické operace. Například dovednost pro práci s PDF zahrnuje předpřipravený skript v Pythonu, který extrahuje pole z formulářů. Claude spustí tento skript bez nutnosti načítat jeho kód nebo samotný PDF do kontextového okna. Díky tomu zůstává workflow konzistentní a opakovatelné.

Anthropic poskytuje předpřipravené dovednosti pro běžné úlohy jako tvorbu dokumentů Excel, PowerPoint, Word a vyplňování PDF formulářů. Vývojáři mohou vytvářet vlastní dovednosti pro své specifické případy použití. Dovednosti se instalují prostřednictvím pluginů z tržiště nebo manuálně do adresáře `~/.claude/skills`. Claude je automaticky načítá při relevanci úlohy.

Vytvoření dovednosti usnadňuje vestavěná dovednost "skill-creator", která interaktivně provede procesem - ptá se na workflow, generuje strukturu adresáře, formátuje soubor `SKILL.md` a zabalí potřebné zdroje.

## Output Styles: Styly výstupu pro transformaci osobnosti

[Styly výstupu](https://claudelog.com/mechanics/output-styles/) (Output Styles) představují mechanismus pro kompletní změnu základní osobnosti agenta při zachování všech jeho schopností. Zatímco původní systémový příkaz Claude Code směřuje agenta k roli asistenta pro vývoj softwaru, styly výstupu umožňují nahradit tuto základní orientaci jakoukoliv jinou specializací.

Co zůstává zachováno: systém projektového kontextu CLAUDE.md, kompletní sada nástrojů, delegování podagentům, integrace MCP, správa kontextu, automatizační workflow, operace se souborovým systémem a kontinuita projektu. Co se mění: systémový příkaz určující osobnost, předpoklady o doméně, prioritizace úloh, vzorce interakce a formátování odpovědí.

Odstranění předpokladů o vývoji softwaru na úrovni systémového příkazu umožňuje čistší a fokusovanější zážitek pro každou doménu. Kontextové okno není znečištěno irelevantními expertními znalostmi, což vede k lepšímu výkonu v konkrétní oblasti. Nástroj přizpůsobí své vzorce uvažování tak, aby odpovídaly způsobu myšlení v dané doméně, místo aby nutil odborníky pracovat v paradigmatu softwarového inženýrství.

Anthropic poskytuje dva vestavěné vzdělávací styly výstupu: "Explanatory" a "Learning". První klade důraz na podrobná vysvětlení, druhý strukturuje odpovědi pro postupné učení. Vývojáři mohou vytvářet vlastní styly výstupu odpovídající jejich specifickým potřebám - od finančního analytika přes marketingového specialistu po vědeckého výzkumníka.

Styly výstupu se liší od parametru `--append-system-prompt`, který pouze rozšiřuje existující chování o specializované oblasti, zatímco zachovává základní povahu asistenta pro kódování. Liší se také od podagentů, kteří představují separátní specialisty s izolovaným kontextem - styly výstupu transformují hlavního delegujícího agenta.

## Opravy stability pro cloudové platformy

Verze 2.0.1 vyšla přibližně 24 hodin po vydání 2.0.0 a řešila kritický problém s nastavením výchozího modelu Sonnet 4.5 pro uživatele AWS Bedrock a Google Vertex AI. Tyto platformy se chovaly odlišně od přímého API Anthropic způsobem, který vyžadoval cílený zásah.

Další aktualizace přinesly vylepšení pro správu modelů. Byla přidána proměnná prostředí `ANTHROPIC_DEFAULT_SONNET_MODEL` a `ANTHROPIC_DEFAULT_OPUS_MODEL` pro přizpůsobení aliasů modelů. Pro uživatele Bedrock se výchozí model Sonnet aktualizoval na Sonnet 4. Nový příkaz `/context` pomáhá diagnostikovat problémy s kontextovým oknem.

Status řádek získal indikátor `exceeds_200k_tokens`, který varuje při přibližování se k limitům kontextu. Příkaz `/cost` nyní přesně sleduje využití a status řádek zobrazuje náklady relace v reálném čase. SDK přidalo podporu UUID pro všechny zprávy a příznak `--replay-user-messages` pro ladění.

## Vylepšení rozšíření pro VS Code a stability

Rozšíření pro Visual Studio Code prošlo řadou oprav. Verze 2.0.21 řešila problém se ztrátou fokusování hlavního vstupu na Windows 11, kdy uživatel musel kliknout dvakrát, aby mohl psát do vstupu po přepnutí z jiné aplikace. Problém se nevyskytoval při přepínání mezi okny uvnitř VS Code.

Verze mezi 2.0.9 a 2.0.21 způsobily regresní chybu na starších verzích macOS 11.5.2, kde proces Claude Code padal s chybou SIGABRT. Downgrade na verzi 2.0.9 problém vyřešil. Byly také opraveny problémy s připojením IDE a diagnostikou, stabilita na Windows zahrnovala vylepšení v zacházení s oprávněními a spouštění podprocesů.

Nový háček `SessionEnd` umožňuje automatické úklidové operace při ukončení relace. To doplňuje existující `SessionStart` háček a poskytuje kompletní pokrytí životního cyklu relace.

## Vylepšení vyhledávání a podpora Alpine Linux

Claude Code nyní používá integrovaný nástroj ripgrep jako výchozí pro vyhledávání v souborech. Tento nástroj zajišťuje rychlejší prohledávání velkých kódových bází. Uživatelé mohou toto chování vypnout nastavením proměnné prostředí `USE_BUILTIN_RIPGREP=0`, pokud preferují externí implementaci.

Byla přidána podpora pro Alpine Linux a distribuce založené na musl. Toto rozšíření platformové podpory vyžaduje samostatnou instalaci ripgrep, protože Alpine používá odlišné systémové knihovny než standardní distribuce založené na glibc.

Návrhy souborů v @-mention nyní zahrnují soubory z adresáře `~/.claude/*`, což usnadňuje editaci agentů, stylů výstupu a slash příkazů. Cesty v @-mention podporují názvy souborů s mezerami. Skryté soubory se nyní objevují ve vyhledávání souborů a @-mention návrzích.

## Vylepšení pro Windows a @-mentions

Funkčnost na platformě Windows byla rozšířena o opravenou podporu vyhledávání souborů, @-mentions agentů a slash příkazů. Dřívější verze měly problémy s těmito funkcemi specificky na Windows, což omezovalo uživatelský zážitek oproti macOS a Linuxu.

Byla vylepšena kontrola oprávnění pro nástroje allow/deny a důvěryhodnost projektů. Toto vylepšení může vytvořit nový záznam projektu v souboru `.claude.json`, přičemž je doporučeno manuálně sloučit pole `history`, pokud dojde k duplicitě.

Spouštění podprocesů bylo vylepšeno tak, aby eliminovalo chyby "No such file or directory" při spouštění příkazů jako `pnpm`. Prostředí shellu bylo opraveno pro uživatele bez souboru `.bashrc`.

Byly přidány @-mentions pro agenty s automatickým dokončováním. Uživatel může napsat `@<název-agenta>` a systém nabídne dostupné agenty. Tato funkce funguje napříč platformami a usnadňuje explicitní vyvolání konkrétního podagenta.

## Specifikace modelů pro agenty a import v CLAUDE.md

Vlastní agenty nyní mohou specifikovat, který model mají používat. To umožňuje například použít Opus pro komplexní plánování v jednom agentovi, zatímco jiný agent používá Sonnet pro rychlejší iterace. Dříve všichni agenti dědili model od hlavního agenta.

Soubory CLAUDE.md získaly schopnost importovat další soubory. Přidáním `@cesta/k/souboru.md` do `./CLAUDE.md` se při spuštění načtou dodatečné zdroje. To umožňuje strukturovat projektový kontext do více souborů a organizovat ho podle témat nebo modulů, místo udržování jednoho velkého souboru.

Byla opravena rekurzivní přístup agentů k nástrojům, což zabránilo nechtěnému rekurzivnímu volání agentů. Systémové zprávy v háčcích nyní podporují varování a kontext. Příkaz `/doctor` byl vylepšen o kontext CLAUDE.md a MCP nástrojů pro samostatnou diagnostiku problémů.

## MCP a OAuth vylepšení

Konfigurace MCP serverů může nyní specifikovat vlastní hlavičky pro HTTP/SSE transport. Podpora OAuth pro MCP servery umožňuje zrušit autentizační proces stisknutím klávesy Esc. Byl přidán parametr `bot_id` pro zacházení s chybami autentizace GitHub App.

Timeout spuštění MCP serveru lze konfigurovat proměnnou prostředí `MCP_TIMEOUT`. Spouštění MCP serveru již neblokuje start aplikace, což zkracuje dobu nutnou k zahájení práce. Podpora více konfiguračních souborů umožňuje použít `--mcp-config soubor1.json soubor2.json`.

Byla opravena chyba, kdy prompt pro oprávnění MCP se nezobrazoval správně. MCP rozsah "project" nyní umožňuje přidávat MCP servery do souborů `.mcp.json` a commitovat je do repozitáře pro sdílení v týmu.

## Dostupnost a ekosystém

Agentní dovednosti jsou dostupné uživatelům plánů Pro, Max, Team a Enterprise. Vyžadují beta verzi nástroje Code Execution Tool, který poskytuje bezpečné prostředí pro jejich spuštění. Vývojáři mohou vytvářet, zobrazovat a aktualizovat verze dovedností přes konzoli Claude nebo programově přes nový endpoint `/v1/skills`.

Komunita vytvořila řadu nástrojů pro práci s Claude Code. Projekt claudekit nabízí sadu více než 20 specializovaných podagentů včetně kódového recenzenta s šestiaspektovou analýzou. ContextKit zavádí čtyřfázovou metodiku plánování a strukturované workflow. Nástroj ccoutputstyles poskytuje galerii více než 15 šablon pro úpravu stylů výstupu.

Claude Code Action pro GitHub dosáhl verze 1.0 s automatickou detekcí režimu, jednotným rozhraním pro prompty a lepším sladěním s Claude Code CLI. Rulesync automaticky generuje konfigurace pro různé agentní nástroje. Projekt Claude Squad spravuje více instancí Claude Code v oddělených workspace pro paralelní práci na různých úlohách.

Dokumentace je k dispozici na [oficiálních stránkách](https://docs.claude.com/en/docs/claude-code/). Rozšíření pro VS Code lze stáhnout z [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-code-vscode).

## Integrace se službami

Box plánuje využít agentní dovednosti pro práci s uloženým obsahem. Uživatelé budou moci transformovat soubory do prezentací PowerPoint, tabulek Excel a dokumentů Word podle organizačních standardů.

Notion využívá dovednosti k bezproblémové integraci s Claude, což urychluje cestu od otázek k akci. Canva plánuje využít dovednosti k úpravě agentů a rozšíření jejich možností, což umožní hlubší začlenění Canva do agentních workflow pro tvorbu kvalitních designů.

Příklad využití dovedností v praxi zahrnuje zpracování více tabulek, odhalování kritických anomálií a generování reportů podle stanovených procedur. Úlohy, které dříve trvaly celý den, lze dokončit za hodinu díky strukturovaným dovednostem, které kódují expertní znalosti organizace.