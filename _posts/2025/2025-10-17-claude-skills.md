---
author: Patrick Zandl
categories:
- AI
- Anthropic
- Claude
- automatizace
- vývoj softwaru
layout: post
post_excerpt: Anthropic představil Claude Skills - modulární systém pro rozšíření schopností AI asistenta o specializované úlohy pomocí strukturovaných složek obsahujících instrukce, skripty a zdroje.
summary_points:
- Claude Skills umožňují vytvářet specializované agenty pomocí složek s instrukcemi a kódem
- Využívají techniku postupného odkrývání pro efektivní správu kontextu
- Dostupné pro uživatele placených plánů Pro, Max, Team a Enterprise
- Skripty běží v sandboxovaném prostředí bez zatížení kontextového okna
- Dovednosti lze sdílet mezi různými prostředími Claude včetně API a Claude Code
- Alternativa k projektům pro jednodušší opakované úlohy s dynamickým načítáním
title: Claude Skills: Nová cesta k specializovaným schopnostem umělé inteligence
thumbnail: https://www.marigold.cz/assets/claude-skills.webp
---

Anthropic představil novou funkci nazvanou [Claude Skills](https://www.anthropic.com/news/skills), která příjemně rozšiřuje způsob, jakým lze přizpůsobovat schopnosti umělé inteligence Claude pro specializované pracovní úlohy. Skills čili Dovednosti představují modulární systém složek obsahujících instrukce, skripty a zdroje, které Claude načítá pouze v případě potřeby. Tato architektura umožňuje transformaci obecného asistenta na specializovaného odborníka pro konkrétní pracovní postupy, aniž by došlo k přetížení kontextového okna modelu.

Začnu osobní zkušeností. Sám jsem si zvykl si řadu materiálů zpracovávat specializovanými prompty a abych si je nemusel nikde archivovat a aby je AI nezapomněla, dával jsem si tyto prompty do Projektů. Prompt jsem spouštěl klíčovým slovem Pracuj, když jsem byl ve složce Projektu. Nyní mohu tentýž doplňkový prompt spouštět přímo jako Dovednost a dokonce je mohu míchat. Je to usnadnění, sice to není zásadní, ale řekl bych, že postupem doby budeme příjemně odkrývat, jak moc to zjednodušuje práci s Claude. Takže se na to všechno podívejme podrobněji. 

## Technická architektura a postupné odkrývání

Nejprve technikálie, jak to funguje. Jádrem funkce Claude Skills je technika nazvaná [postupné odkrývání](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) (progressive disclosure). Místo načtení všech informací najednou do kontextového okna modelu Claude postupuje ve třech fázích. Nejprve skenuje pouze metadata - název a popis každé dostupné dovednosti, což zabírá pouhých několik desítek tokenů. Pokud identifikuje relevantní dovednost pro daný úkol, načte hlavní instrukční soubor SKILL.md obsahující podrobné pokyny. V poslední fázi přistupuje k dodatečným zdrojům jako jsou skripty nebo referenční dokumenty pouze tehdy, když je skutečně potřebuje pro splnění úkolu. Šetří to dostupný kontext, tedy množství zpracovávaných dat (a to má vliv na limity či na cenu) a je to rychlejší. 

Každá dovednost je organizována jako adresář v souborovém systému. Povinnou součástí je soubor SKILL.md začínající hlavičkou ve formátu YAML s metadaty:

```yaml
---
name: Zpracování PDF
description: Extrakce textu a tabulek z PDF souborů, vyplňování formulářů, spojování dokumentů. 
             Použijte při práci s PDF soubory nebo když uživatel zmíní PDF, formuláře nebo extrakci dokumentů.
version: 1.0
---
```

Popis dovednosti může mít maximálně 1024 znaků a musí obsahovat informaci o tom, co dovednost dělá a kdy by měla být použita. Samotné tělo souboru pak obsahuje podrobné instrukce v jazyce Markdown, které Claude následuje při provádění úkolu.

## Tři typy obsahu v dovednostech

Dovednosti mohou obsahovat tři základní typy obsahu, každý s jiným účelem a načítáním:

**Instrukce** tvoří dodatečné soubory Markdown obsahující specializované postupy a pracovní toky. Tyto soubory poskytují flexibilní vedení pro různé scénáře použití dovednosti.

**Spustitelný kód** zahrnuje skripty v jazycích Python nebo JavaScript, které Claude spouští přes bash příkazy. Důležité je, že samotný kód se nikdy nenačítá do kontextového okna - pouze výstup skriptu spotřebovává tokeny. To činí skripty mnohem efektivnějšími než generování ekvivalentního kódu modelem za běhu.

**Zdroje** představují referenční materiály jako schémata databází, dokumentaci API, šablony nebo příklady. Claude k těmto souborům přistupuje pouze když jsou explicitně zmíněny v instrukcích.

Architektura založená na souborovém systému přináší několik výhod. Dovednosti mohou obsahovat desítky referenčních souborů bez jakékoli penalizace kontextu, pokud nejsou použity. Pokud úloha vyžaduje pouze specifické schéma, Claude načte pouze tento jeden soubor, zatímco zbytek zůstává v souborovém systému bez spotřeby tokenů.

![Claude Skills - jak se spouštějí](/assets/claude-skills.webp)
_Jak se Claude Skills konfigurují_

## Praktické využití a firemní nasazení

Společnost [Rakuten](https://venturebeat.com/ai/how-anthropics-skills-make-claude-faster-cheaper-and-more-consistent-for), japonský e-commerce gigant, využívá Skills (měla funkci v předstihu) pro transformaci finančních operací, které dříve vyžadovaly manuální koordinaci mezi několika odděleními. Podle Yusuke Kajiho, generálního manažera pro AI v Rakuten, "co dříve trvalo celý den, nyní dokážeme splnit za hodinu."

Platforma pro správu obsahu [Box](https://www.anthropic.com/news/skills) integrovala Skills pro práci s firemními dokumenty. Yashodha Bhavnani, vedoucí AI v Box, uvádí: "Skills učí Claude, jak pracovat s obsahem Box. Uživatelé mohou transformovat uložené soubory na prezentace PowerPoint, tabulky Excel a dokumenty Word, které odpovídají standardům jejich organizace - ušetří tak hodiny práce."

Notion, populární nástroj pro správu znalostí, ocenil předvídatelnější výsledky s menší potřebou ladění promptů. Tato zpětná vazba ukazuje na hlavní výhodu Skills - konzistenci výstupů při opakovaných úlohách.

## Vytváření vlastních dovedností

Anthropic poskytuje několik způsobů vytváření dovedností. Nejjednodušší je využití vestavěného "skill-creatoru" přímo v rozhraní Claude, který umožňuje interaktivní vytváření dovedností pomocí konverzace. Pro pokročilejší uživatele je k dispozici [Claude Skills Cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/skills) s příklady a šablonami.

Při vytváření vlastních dovedností je důležité dodržovat několik zásad:

- Začít jednoduše s základními instrukcemi v Markdown před přidáním komplexních skriptů
- Zahrnout příklady vstupů a výstupů v souboru SKILL.md pro lepší pochopení očekávaného výsledku
- Verzovat dovednosti pro snadné sledování změn a možnost návratu k předchozím verzím
- Testovat postupně po každé významné změně místo vytváření komplexní dovednosti najednou

## Rozdíl mezi Skills a projekty

Zatímco projekty Claude poskytují statické pozadí znalostí, které jsou vždy načteny při spuštění chatu v rámci projektu, Skills nabízejí specializované procedury, které se aktivují dynamicky podle potřeby. Projekty jsou vhodné pro trvalý kontext jako firemní směrnice nebo technickou dokumentaci projektu. Skills naproti tomu excelují v opakovaných, dobře definovaných úlohách jako generování reportů, analýza dat nebo vytváření dokumentů podle šablon.

Klíčový rozdíl spočívá v přenositelnosti - zatímco projekty jsou vázány na konkrétní konverzační prostředí, Skills fungují napříč všemi prostředími Claude včetně webové aplikace, Claude Code a API. To umožňuje vytvořit dovednost jednou a použít ji všude, kde tým pracuje s Claude.

## Bezpečnostní aspekty a omezení

Anthropic důrazně [varuje před instalací dovedností z nedůvěryhodných zdrojů](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview). Dovednosti mohou obsahovat spustitelný kód, což představuje potenciální bezpečnostní riziko. Před použitím dovednosti z méně známého zdroje je nutné důkladně zkontrolovat všechny soubory, věnovat pozornost závislostem kódu a vloženým zdrojům jako jsou obrázky nebo skripty.

Pro firemní zákazníky jsou k dispozici administrativní kontroly, které umožňují spravovat přístup na organizační úrovni. Administrátoři mohou povolit nebo zakázat přístup k funkcím Skills a monitorovat vzorce používání. I když je funkce povolena na úrovni organizace, jednotliví uživatelé musí stále explicitně souhlasit s jejím použitím.

## Dostupnost a cenová politika

Claude Skills jsou dostupné uživatelům placených plánů:

- **Claude Pro**: 20 dolarů měsíčně (17 dolarů při ročním předplatném) pro jednotlivce
- **Claude Team**: 30 dolarů na osobu měsíčně (25 dolarů ročně) s minimem 5 uživatelů
- **Claude Max** a **Enterprise**: individuální cenová nabídka

Za samotné používání Skills se neplatí žádný dodatečný poplatek, ale pokud dovednosti provádějí volání API nebo spouštějí komplexní skripty, stále se účtují standardní poplatky za tokeny podle použitého modelu Claude.

## Srovnání s konkurenčními řešeními

Skills představují přímou konkurenci pro nedávno oznámený [AgentKit od OpenAI](https://winbuzzer.com/2025/10/17/anthropic-challenges-openai-with-skills-making-its-claude-ai-a-more-capable-workplace-agent-xcxwbn/) a další nástroje pro vytváření agentů. Zatímco OpenAI se zaměřuje na komplexní vývojářský toolkit, Anthropic vsadil na jednoduchost a přenositelnost. 

Unikátní kombinace postupného odkrývání, skládatelnosti a možnosti zahrnout spustitelný kód odlišuje Skills od konkurenčních platforem. Zatímco jiné systémy vyžadují, aby vývojáři vytvářeli vlastní infrastrukturu, Skills umožňují komukoli - technickému i netechnickému - vytvořit specializované agenty pouhým organizováním procedurálních znalostí do souborů.

Simon Willison, známý vývojář a komentátor AI technologií, [označil Skills za možná větší průlom než Model Context Protocol](https://simonwillison.net/2025/Oct/16/claude-skills/): "Očekávám kambrickou explozi Skills, která způsobí, že letošní spěch kolem MCP bude vypadat jako procházka růžovým sadem." (ne, nevím, co znamená kambrická, ale asi to bude pochvala!)

## Budoucnost specializovaných agentů

Claude Skills představují zajímavý posun od obecných konverzačních schopností k spolehlivým, přizpůsobitelným agentům schopným následovat specifické pracovní postupy. Tato změna odráží širší trend v odvětví umělé inteligence, kde se pozornost přesouvá od vytváření stále výkonnějších modelů k vytváření praktických nástrojů pro každodenní firemní použití. A tady je právě problém, jak udělat rozhraní, které bude pro uživatele pochopitelné, přičemž Skills jsou na zajímavé cestě - jsou vlastně dodatečným a podmíněným promptováním, se kterým uživatelé nějakou zkušenost mají. 

Pro české firmy představují Claude Skills příležitost k vytvoření vlastních dovedností respektujících lokální specifika, legislativu a obchodní zvyklosti. Možnost verzování a sdílení dovedností v rámci týmu nebo organizace umožňuje postupné budování firemního know-how v podobě znovu použitelných modulů.

Technologie Skills je teprve na začátku své cesty. Anthropic již pracuje na zjednodušených pracovních postupech pro vytváření dovedností a schopnostech nasazení v rámci celé organizace. To usnadní distribucí dovedností napříč týmy a vytvoření skutečně specializovaných AI agentů přizpůsobených konkrétním potřebám každé organizace.