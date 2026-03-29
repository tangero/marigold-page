---
slug: 'claude-code'

date: 2025-03-22
hide: true
order: 1
title: Claude Code je AI asistent pro vývoj přímo v terminálu
sw: claude
---

[Claude Code](/ai/claude-code/) je nástroj od společnosti Anthropic, který přináší obrovský náskok a zkušenost jejího jazykového modelu Claude Sonnet přímo do vývojářského prostředí. Jde o  CLI nástroj (tedy běžící v příkazové řádce)  integrovaný do terminálu, který umožňuje vývojářům spolupracovat s AI při každodenní práci s kódem. Ale nebojte se slov CLI ani příkazová řáda, prostě si povídáte s "chatbotem" a necháte jej, aby realizoval vaše zadání ke zdrojovému kódu. Jen ho zavoláte z Terminálu, což mu dává řadu možností a také to důstojně vynechává představu, že se sami budete hrabat ve zdrojáku, jako to naznačuje [Cursor nebo Copilot ve VS Code](/item/programovani-s-ai/). 

Stáhnout si [Claude Code můžete zde](https://ai-claude.net/code/) (macOS 10.15+, Ubuntu 20.04+/Debian 10+, Windows via WSL)

__Co konkrétně se v tomto článku dozvíte?__ 
* Obsah
{:toc}

## Jak [Claude Code](/ai/claude-code/) funguje

[Claude Code](/ai/claude-code/) je postaven jako terminálová aplikace, která umožňuje konverzaci s AI asistentem Claude, ale na rozdíl od webové verze má přístup k vašemu lokálnímu vývojovému prostředí. To znamená, že může:

- Číst a analyzovat soubory ve vašem projektu
- Provádět Git operace
- Navrhovat a implementovat změny v kódu
- Vytvářet nové soubory a skripty
- Pomáhat s debugováním a řešením problémů

Celý nástroj funguje v kontextu vašeho projektu, což umožňuje Claude porozumět vaší kódové základně a poskytovat relevantnější pomoc. Také to má ale nástrahy, protože posílání "kontextu", tj. všech souvisejících kódů hodně zatěžuje LLM a zaplatíte si to. A tím se **dostáváme k bodu placení**, který trochu odbudeme. [Claude Code](/ai/claude-code/) se platí, pro jeho použití se musíte přihlásit do služby Claude a dostatečně si ji naplnit alespoň 5 dolary plus DPH. Bez platební karty se neobejdete. A cena se platí podle tarifu Claude Sonnet, tedy za odeslané a vygenerované [tokeny](/ai/tokeny-versus-slova/). Počítejte s tím, že [Claude Code](/ai/claude-code/) je vlastně docela drahý v kontextu jiných nástrojů. Hodně plýtvá kontextem, díky čemuž má ale také výrazně lepší výsledky. Počítejte s tím, že jednoduchý script vás vyjde na dolary, denní velmi intenzivní práce může stát i třeba dvacet dolarů...

Co je výhoda? Můžet s Claudem mluvit česky, rozumí vám. Bude odpovídat také převážně česky, některé drobnosti dá anglicky. 

Na obrazovce vidíte, jak všechno funguje:

![Claude Code použité na Marigold.cz](/assets/claudecode-marigold.png)

Spustím Terminál, přejdu do adresáře, kde mám projekt a nyní si mohu poroučet, co se s ním má dělat. Tento web je staticky generovaný, funguje přes Github Pages a Jekyll, jenže už dávno si nové věci neřeším sám, ale nechávám si to vyvíjet právě přes AI. Jenže to má své problémy. Například teď jsem si nechal udělat script, který opravil nadpisy článků, ve kterých byly někdy paznaky. Jenže při tom udělal jiný problém. Ten nyní chci po [Claude Code](/ai/claude-code/) upravit, když mu říkám: __Potřebuji projít všechny soubory v adresáři _posts a podadresářích s koncovkou .md ... __

Claude rekapituluje, co bude dělat a pak se hned pouští do řešení. Rozhodne se, že k tomu použije již existující soubor, aniž by se podíval, k čemu ten soubor slouží a přemastí mi jeho funkci. Což by bylo nepříjemné, kdyby to nebyl starý už nepoužívaný script. Ale je to typický příklad toho, že se [Claude Code](/ai/claude-code/) musí dost jasně říkat, co a jak má udělat. Mimo jiné jej na začátku musíte instruovat, jestli takové věci může nebo nemůže provést sám, bez zeptání se (já pro tento případ nastavil, ať to sází bez mého schválení). Ale to už je ta vyšší dívčí, na kterou se podíváme někdy příště. 

Teď se ještě pojďme věnovat teorii... 

## Podporované jazyky a typy projektů

[Claude Code](/ai/claude-code/) je navržen jako univerzální nástroj pro vývojáře a podporuje široké spektrum programovacích jazyků a typů projektů:

Přesto si dáme jedno upozornění na začátek, trochu jsem se s tím sám trápil. Code je určený na to, abyste jím zadávali příkazy pro programovacího agenta. Pokud chcete sami spouštět programy, které vytvoří, musíte si otevřít další okno Terminálu. Code sám sice může programy spouštět, to je ale jen pro ladící účely, kdy agent Code ověřuje, zda všechno udělal správně. Pro vaše samotné testování je potřeba si vše pustit z jiného okna.  

### Programovací jazyky

[Claude Code](/ai/claude-code/) má silnou podporu pro většinu populárních jazyků včetně:
- **JavaScript/TypeScript** - kompletní podpora včetně moderních frameworků
- **Python** - plná podpora pro Python 3.x a běžné knihovny
- **Java/Kotlin** - dobré porozumění objektovému kódu a Android vývoji
- **C/C++** - schopnost analyzovat a navrhovat úpravy v komplexních codebases
- **Go** - dobrá podpora pro idiomatický Go kód
- **Rust** - rozumí konceptům ownership a borrowing
- **Ruby** - včetně Rails a dalších frameworků
- **PHP** - od malých skriptů po rozsáhlé aplikace
- **C#/.NET** - dobrá podpora pro ekosystém .NET
- **Swift** - včetně iOS/macOS vývoje

### Typy projektů

[Claude Code](/ai/claude-code/) je efektivní napříč různými typy projektů:

- **Backend aplikace** - API, mikroslužby, serverové aplikace
- **Frontend vývoj** - React, Vue, Angular a další JS frameworky
- **Mobile development** - nativní aplikace pro iOS a Android
- **DevOps** - skripty, konfigurace, CI/CD pipelines
- **Data Science** - analýza dat, ML modely, jupyter notebooks
- **Embedded systémy** - s určitými omezeními u velmi specifického hardwaru
- **Desktop aplikace** - multiplatformní i nativní aplikace
- **Game development** - včetně herních enginů jako Unity

Ačkoliv Claude Code zvládá všechny uvedené oblasti, jeho efektivita může kolísat podle specifičnosti domény a komplexity projektu. Nejsilnější je v oblastech web developmentu, backendových systémů a obecného programování.

## Klíčové funkce Claude Code

### Kontextové porozumění

Claude Code automaticky shromažďuje kontext z vašeho projektu, aby mohl poskytovat odpovědi a návrhy relevantní pro vaši kódovou základnu. Dokáže navigovat strukturou souborů, analyzovat závislosti a pochopit architektonické vztahy.

### Práce s kódem

- **Analýza kódu**: Identifikace potenciálních problémů, vysvětlení složitých částí kódu
- **Refaktorizace**: Návrhy na zlepšení struktury kódu s ohledem na osvědčené postupy
- **Implementace**: Tvorba nových funkcí na základě specifikací
- **Testování**: Pomoc při vytváření testů pro existující kód

### Integrace s vývojovým procesem

Claude Code se integruje do existujícího workflow vývojáře:

- **Git integrace**: Práce s větvemi, commity a pull requesty (můžete mu říct lidsky, on příkaz navrhne a provede)
- **Práce na projektech**: Schopnost řešit tickety a issues (doporučuju vyzkoušet, díky GIT integraci toho pořeší opravdu slušně dost)
- **Podpora dokumentace**: Generování a aktualizace dokumentace (další dobrá vychytávka, já si od něj nechávám sjet, co nového v kódu u mých vývojářů a jak dobře to udělali a zadokumentovali)

### Interaktivita a autonomie

Na rozdíl od tradičních asistentů pro programování může Claude Code vést dialog, ptát se na doplňující informace a pracovat iterativně. Lze nastavit různé úrovně autonomie - od pouhého navrhování změn po jejich automatickou implementaci. S tím doporučuju poněkud opatrně, protože v takovém případě první, co se vám logicky stane je, že Claude Code něco špatně pochopí, přemastí vám kód a ještě ho automaticky commitne na Github, odkud se to nasadí na produkci a už se vezete... 

## Použití v praxi

Claude Code se mi osvědčuje v široké paletě scénářů. Tak například: 

### 1. Onboarding do nového projektu

Když začínáte pracovat na existujícím projektu, Claude Code může výrazně zkrátit čas potřebný k pochopení kódové základny:

```
claude "Vysvětli mi architekturu tohoto projektu a hlavní toky dat"
```

Můžete také požádat Claude o:
- Identifikaci klíčových komponent a jejich interakce
- Vytvoření mapy závislostí mezi moduly
- Vysvětlení historických rozhodnutí v kódu (pomocí git historie)
- Shrnutí účelu a funkcionality konkrétních souborů nebo adresářů

Pro větší projekty je užitečné říct Claudovi, aby "přemýšlel" o struktuře. Používám anglický výraz think hard, který uvádí dokumentace Antrhopicu, používat nějakou formu "usilovně přemýšlej" mi přijde divné, think hard rozumí a funguje to, takže směska angličtiny a češtiny funguje dobře. Stejně tak tak code base - kódová základna :

```
claude "Analyzuj code base a think hard o tom, jak jednotlivé části spolupracují"
```

### 2. Řešení komplexních problémů

Při řešení složitých úkolů můžete využít Claude jako sparring partnera:

```
claude "Potřebuji implementovat autentizaci pomocí OAuth2. Můžeš mi pomoci navrhnout řešení?"
```

Claude Code dokáže:
- Navrhnout různé architektury řešení problému
- Identifikovat potenciální výzvy a rizika jednotlivých přístupů
- Generovat prototypový kód pro ověření konceptu
- Nabídnout postupný plán implementace

Pro komplexní problémy využijte možnost rozšířeného myšlení:

```
claude "Potřebujeme zlepšit výkon naší databázové vrstvy. Přemýšlej hlubocels o možných optimalizacích a zlepšeních"
```

### 3. Automatizace rutinních úkolů

Claude Code je ideální pro automatizaci opakujících se úloh:

```
claude "Najdi všechny funkce bez jednotkových testů a vytvoř pro ně základní testy"
```

Mezi další rutinní úlohy patří:
- Refaktorizace kódu podle aktuálních best practices
- Aktualizace dokumentace podle změn v kódu
- Konverze mezi formáty (např. z JSON na TypeScript typy)
- Standardizace formátování a stylu kódu

Pro maximální efektivitu využijte režim auto-accept:

```
claude "Přidej JSDoc komentáře ke všem veřejným funkcím v src/utils" [SHIFT+TAB pro auto-accept]
```

### 4. Učení a prohlubování znalostí

Claude Code může sloužit jako osobní mentor přímo při práci s kódem:

```
claude "Vysvětli mi, jak funguje tento algoritmus v sorting.js a proč je implementován takto"
```

Claude může:
- Vysvětlit neznámé koncepty nebo vzory použité v projektu
- Navrhnout alternativní implementace s vysvětlením výhod a nevýhod
- Doporučit relevantní materiály k dalšímu studiu
- Vytvářet cvičení a výzvy pro procvičení specifických dovedností

Pro efektivní učení požádejte Claude o kontextové vysvětlení:

```
claude "V tomto projektu vidím použití návrhového vzoru Observer. Vysvětli mi jeho implementaci na konkrétních třídách v našem kódu"
```

## Instalace a začátek práce

Claude Code lze nainstalovat pomocí npm:

```
npm install -g @anthropic-ai/claude-code
```

Po instalaci stačí v kořenovém adresáři vašeho projektu spustit:

```
claude
```

Tím se spustí interaktivní terminálové rozhraní, kde můžete začít konverzaci s Claudem v kontextu vašeho projektu.

Uvidíte zobáček, který indikuje, že můžete zadávat své požadavky. Pokud začínáte od nuly, můžete začít formulovat svůj požadavek, pokud jste v adresáři, kde už nějaký svůj projekt máte, hodí se dát /init - tím prozkoumáte stávající projekt a vygenerujete k němu shrnutí do souboru claude.md. 

> 💡 POZOR: rozhodně nezačínejte pracovat s Claude v nějakém svém ostrém a cenném projektu. Bez určitých zkušeností se vám relativně snadno stane, že vám "přemastí" zdrojáky, která byste chtěli nechat tak, jak jsou.  Začněte experimentovat s prázdným projektem

Jak Claude Code používat lépe a intenzivněji si řekneme někdy příště.