---
author: Patrick Zandl
categories:
- AI
- Anthropic
- Claude Code
- vývojářské nástroje
layout: post
post_excerpt: Anthropic představil systém pluginů pro Claude Code, který umožňuje přidávat vlastní příkazy, agenty a automatizační nástroje přímo do vývojového prostředí. Jak na ně?
summary_points:
- Anthropic uvedl systém pluginů pro Claude Code, který rozšiřuje možnosti tohoto nástroje pro agenturní programování
- Pluginy přidávají vlastní příkazy, specializované agenty, háčky pro automatizaci a servery MCP pro napojení externích služeb
- Vývojáři mohou pluginy instalovat z tržišť příkazem /plugin install nebo vytvářet vlastní konfigurace pro týmovou spolupráci
- Komunita již vytvořila stovky pluginů dostupných na platformách jako aitmpl.com a v repozitářích na GitHubu
- Systém podporuje automatickou instalaci pluginů na úrovni repozitáře pro konzistentní týmové prostředí
- Pluginy pracují s Claude Sonnet 4.5 a dalšími modely rodiny Claude, rozšiřují kontrolní body a další nedávné funkce
thumbnail: https://www.marigold.cz/assets/claude-code-plugins.webp
title: Claude Code má nově rozšiřující pluginy
---

Společnost Anthropic doplnila svůj nástroj Claude Code o systém pluginů, který vývojářům umožňuje přizpůsobit si agenturní programovací prostředí podle vlastních potřeb. Nová funkcionalita přináší možnost instalace předpřipravených rozšíření nebo tvorby vlastních komponent pro automatizaci vývojových procesů.

Claude Code je nástroj pro agenturní programování, který funguje přímo v terminálu nebo vývojovém prostředí. Umožňuje vývojářům zadávat úkoly přirozeným jazykem a Claude následně provádí změny v kódu, spouští testy nebo vytváří committy. Systém pluginů tuto základní funkcionalitu rozšiřuje o čtyři hlavní typy komponent.

## Struktura a komponenty pluginů

Pluginy se skládají z několika základních stavebních bloků. Prvním jsou vlastní příkazy neboli slash commands, které představují textové instrukce ve formátu Markdown. Tyto soubory definují, jak má Claude reagovat na konkrétní příkaz. Například plugin může obsahovat příkaz `/review`, který provede kontrolu kódu podle specifických kritérií projektu.

Druhým typem komponent jsou specializovaní agenti. Jedná se o definice osobností Claude s konkrétním zaměřením. Agent může být například nastaven jako bezpečnostní auditor, který systematicky prochází kód a hledá zranitelnosti, nebo jako frontend vývojář zaměřený na React a TypeScript. Každý agent má vlastní styl komunikace a prioritizuje specifické aspekty vývoje.

Třetí komponentou jsou háčky neboli hooks, které automaticky spouštějí akce v určitých okamžicích vývojového procesu. Háček může například spustit testovací sadu po každé změně kódu nebo provést kontrolu formátování před vytvořením commitu. Háčky se konfigurují pomocí souboru `hooks.json` v adresáři pluginu.

Poslední typ tvoří servery MCP neboli Model Context Protocol. Tyto servery umožňují napojení Claude Code na externí nástroje a služby. Pomocí MCP lze například integrovat databáze, API nebo vývojářské nástroje jako GitHub, GitLab či Jira. Konfigurace MCP serverů probíhá přes soubor `.mcp.json`.

## Instalace a správa pluginů

Systém pracuje s konceptem tržišť neboli marketplaces, což jsou katalogy dostupných pluginů. Vývojář může přidat tržiště příkazem `/plugin marketplace add` a následně procházet dostupné pluginy interaktivním menu nebo je instalovat přímo příkazem `/plugin install název-pluginu@název-tržiště`. Po instalaci je třeba restartovat Claude Code pomocí příkazu `/reset`.

![Instalace Pluginů v Claude Code](https://www.marigold.cz/assets/claude-code-plugins.webp)

Pro ověření správné instalace slouží příkaz `/help`, který zobrazí seznam všech dostupných příkazů včetně těch z nově nainstalovaných pluginů. Příkaz `/plugin` pak otevírá menu pro správu pluginů, kde lze jednotlivé pluginy aktivovat, deaktivovat nebo odinstalovat.

Významnou funkcí je možnost konfigurace pluginů na úrovni repozitáře. Vývojový tým může do souboru `.claude/settings.json` v kořeni projektu zapsat, která tržiště a pluginy mají být automaticky dostupné. Když pak členové týmu označí adresář projektu jako důvěryhodný, Claude Code jim automaticky nainstaluje všechny potřebné pluginy. Tím se zajistí konzistentní vývojové prostředí pro celý tým.

## Vývoj vlastních pluginů

Vytvoření vlastního pluginu začíná strukturou adresářů. V kořeni pluginu se nachází adresář `.claude-plugin` obsahující soubor `plugin.json` s metadaty pluginu - název, popis, verzi a informace o autorovi. Vedle něj pak vývojář vytváří adresáře pro jednotlivé komponenty podle potřeby: `commands/` pro vlastní příkazy, `agents/` pro specializované agenty, `hooks/` pro automatizační háčky a `.mcp.json` pro integraci externích nástrojů.

Pro testování pluginu během vývoje se používá místní tržiště. Vývojář vytvoří adresář obsahující testované pluginy a v něm soubor `.claude-plugin/marketplace.json`, který definuje metadata tržiště a seznam pluginů. Toto lokální tržiště pak lze přidat do Claude Code standardním příkazem a následně z něj instalovat pluginy stejným způsobem jako z veřejných zdrojů.

Při ladění pluginů pomáhá příkaz `/plugin validate`, který kontroluje strukturu pluginu a upozorní na chyby v konfiguraci. Dokumentace doporučuje testovat jednotlivé komponenty odděleně - nejprve příkazy, pak agenty a nakonec háčky. Pokud plugin nefunguje podle očekávání, je třeba ověřit, že adresáře s komponentami jsou umístěny přímo v kořeni pluginu, nikoliv uvnitř adresáře `.claude-plugin`.

## Dostupné zdroje pluginů

Komunita vývojářů již vytvořila několik platforem s pluginy pro Claude Code. Platforma [aitmpl.com](https://www.aitmpl.com/plugins) nabízí přes 400 komponent včetně agentů, příkazů, nastavení, háčků, MCP serverů a kompletních šablon projektů. Tento projekt vznikl jako faktický správce balíčků pro ekosystém Claude Code. Uživatelé mohou procházet komponenty podle kategorií nebo použít vyhledávání podle klíčových slov a technologií.

Na GitHubu existuje repozitář [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code), který obsahuje kurátorovaný seznam příkazů, souborů CLAUDE.md a pracovních postupů. Další významný projekt [claude-code-plugins](https://github.com/roygabriel/claude-code-plugins) od vývojáře Roy Gabriel přináší sadu 24 profesionálních příkazů optimalizovaných pro modely Claude Opus 4 a Sonnet 4. Tyto příkazy se zaměřují na běžné vývojářské úkoly jako formátování kódu, správu commitů nebo automatické testování.

Projekt [claude-code-templates](https://github.com/davila7/claude-code-templates) od Daniela Avily poskytuje nástroj příkazové řádky pro instalaci kompletních vývojových prostředí. Pomocí jediného příkazu lze nainstalovat sadu agentů, příkazů a integrací určených pro konkrétní typ projektu. Nástroj také nabízí diagnostické funkce pro kontrolu konfigurace Claude Code a monitoring využití během programování.

## Integrace se současnými funkcemi

Systém pluginů spolupracuje s nedávno představenými funkcemi Claude Code. Kontrolní body neboli checkpoints automaticky ukládají stav kódu před každou změnou a umožňují rychlé vrácení dvojím stisknutím klávesy Escape nebo příkazem `/rewind`. Tato funkce se hodí zejména při experimentování s rozsáhlými refaktoringy nebo implementaci nových funkcí.

Podagenti neboli subagents umožňují delegovat specializované úkoly. Zatímco hlavní agent pracuje na frontendu, podagent může paralelně vytvářet backendové API. Háčky spouštějí akce v konkrétních okamžicích vývojového procesu, například spuštění testů po změně kódu. Úlohy na pozadí neboli background tasks udržují dlouhotrvající procesy jako vývojové servery aktivní bez blokování práce Claude Code na dalších úkolech.

Tyto funkce dohromady vytvářejí prostředí pro autonomní práci agenta na složitých vývojářských úkolech. Vývojář může delegovat širší úkoly s vědomím, že má kontrolu nad průběhem díky kontrolním bodům a že může kdykoliv vrátit změny zpět.

## Technické aspekty

Pluginy pracují jako instrukce ve formátu Markdown nebo JSON, které Claude Code interpretuje při spuštění příkazu nebo aktivaci háčku. Příkazy používají popisný jazык v první osobě ("Pomohu vám analyzovat kód a opravit importy"), což vytváří dojem spolupráce spíše než vykonávání příkazů. Tento přístup podle dokumentace vede k lepším výsledkům, protože model lépe reaguje na konverzační styl.

Agenti využívají stejný princip - definice agenta obsahuje popis jeho role, odbornosti a stylu práce. Když vývojář aktivuje konkrétního agenta, Claude přijme tuto personu a přizpůsobí své odpovědi a rozhodování podle zadané specializace.

MCP servery vyžadují samostatnou instalaci a konfiguraci externího softwaru, který Claude Code kontaktuje pro získání dat nebo provedení akcí. Například MCP server pro GitHub umožňuje Claude Code číst issue, vytvářet pull requesty nebo procházet historii commitů bez nutnosti manuálního zadávání příkazů git.

Systém pluginů konzumuje vstupní tokeny - každý plugin přidává svůj kontext do komunikace s modelem. Proto dokumentace doporučuje aktivovat pouze pluginy, které jsou aktuálně potřebné, a pravidelně používat příkaz `/clear` pro vyčištění historie konverzace.

## Budoucí vývoj

Anthropic uvolnil Claude Agent SDK, které vývojářům poskytuje přístup ke stejným nástrojům, systémům správy kontextu a oprávněním, jaké používá samotný Claude Code. SDK umožňuje vytváření vlastních agenturních aplikací pro specifické případy použití - od finanční compliance přes kybernetickou bezpečnost až po ladění kódu.

Komunita již začala experimentovat s pokročilými kombinacemi pluginů. Vývojáři vytvářejí komplexní pracovní postupy spojující více agentů s různými specializacemi, kteří spolupracují na jednom projektu. Jiní se zaměřují na integraci Claude Code s podnikovými nástroji a vytvářejí MCP servery pro proprietární systémy.

Dokumentace nabízí několik směrů pro další využití systému pluginů. Pro uživatele pluginů doporučuje procházet komunitní tržiště a experimentovat s různými kombinacemi nástrojů. Vývojářům pluginů radí začít jednoduchým příkazem a postupně přidávat složitější komponenty. Vedoucím týmů pak navrhuje nastavit automatickou instalaci pluginů na úrovni repozitářů a vytvořit pravidla pro schvalování a bezpečnostní kontrolu pluginů.

Oficiální dokumentace systému pluginů je dostupná na [docs.claude.com/en/docs/claude-code/plugins](https://docs.claude.com/en/docs/claude-code/plugins). Vývojáři mohou diskutovat o pluginech a sdílet zkušenosti na Discord serveru Claude Developers.