---
author: Patrick Zandl
categories:
- AI
- Microsoft
- POML
- Prompt Engineering
layout: post
post_excerpt: Microsoft představil POML, značkovací jazyk pro strukturování promptů pro jazykové modely. Řeší správu složitých promptů, integraci dat a optimalizaci formátu pro různé modely.
summary_points:
- Microsoft vydal POML, značkovací jazyk připomínající HTML pro strukturování promptů
- Řeší tři hlavní problémy: neudržitelné textové bloky, složitou integraci dat a citlivost na formátování
- Obsahuje komponenty pro role, úkoly, příklady a automatickou integraci CSV, PDF a obrázků
- Umožňuje optimalizaci formátu pro různé modely změnou jednoho atributu
- Dostupný jako rozšíření pro VS Code a SDK pro Python i Node.js
title: Microsoft představil POML, strukturovaný jazyk pro správu promptů
---

Microsoft vydal POML (Prompt Orchestration Markup Language), značkovací jazyk pro strukturování promptů určených jazykovým modelům. Nástroj má řešit problémy se správou složitých promptů v podnikových aplikacích využívajících umělou inteligenci.

POML představuje pokus o systematizaci tvorby promptů pomocí HTML-podobné syntaxe. Vývojáři mohou rozdělit prompty do komponent jako `<role>`, `<task>`, `<example>` nebo `<output-format>`. Podle Microsoftu má tento přístup zlepšit udržitelnost kódu a spolupráci v týmech.

## Tři kategorie problémů

Microsoft identifikuje tři hlavní oblasti, které POML řeší. První je problém nestrukturovaných promptů. Vývojové týmy často začínají s krátkými textovými prompty, které postupně narůstají na stovky řádků bez jasné struktury. Změny v jedné části takového promptu mohou nečekaně ovlivnit jeho fungování jinde. Systémy pro správu verzí zobrazují pouze změny textových bloků bez kontextu, co konkrétně bylo upraveno.

Druhý problém představuje integrace dat. Aplikace vyžadují zpracování různých formátů souborů - dokumentů, tabulek, odpovědí z API. Standardní přístup znamená psaní vlastního kódu pro parsování CSV souborů, extrakci textu z PDF a konverzi všech dat do formátu vhodného pro konkrétní jazykový model. Tento proces spotřebovává významnou část vývojového času.

Třetí oblast se týká citlivosti na formátování. Různé jazykové modely reagují rozdílně na stejný prompt v závislosti na jeho formátování. Claude upřednostňuje XML strukturu, modely GPT fungují lépe s markdown formátem. Některé modely vyžadují tabulková data jako CSV, jiné preferují formát oddělený svislými čarami. Vývojáři musí buď udržovat různé verze promptů pro každý model, nebo omezit použití na jediný model a tím ztratit flexibilitu.

## Struktura a komponenty

POML organizuje prompty do logických celků. Základní struktura obsahuje role definující kontext, úkoly specifikující požadavky, příklady ukazující očekávané chování a formát výstupu kontrolující strukturu odpovědi. Každá komponenta má jasně vymezený účel, což týmům umožňuje provádět změny bez narušení ostatních částí.

Jazyk zahrnuje automatickou integraci dat. Komponenta `<table>` zpracovává CSV soubory a prezentuje je ve formátu optimálním pro cílový model. Komponenta `<document>` extrahuje text z PDF dokumentů s možností specifikovat rozsah stránek. Obrázky jsou zpracovány a popsány automaticky.

POML podporuje dynamický obsah pomocí proměnných a řídicích struktur. Proměnné se dosazují za běhu, cykly generují více příkladů z kolekcí dat a podmínky přizpůsobují chování promptu podle kontextu.

Komponenty lze skládat do větších celků. Týmy mohou sdílet společné definice rolí, knihovny příkladů a formáty výstupu napříč projekty. Změny ve sdílených komponentách se automaticky projeví všude, kde jsou použity.

## Optimalizace formátu

POML umožňuje optimalizovat formát promptu pro různé modely změnou jediného atributu. Stejný logický obsah se může renderovat odlišně podle preferencí konkrétního modelu. Microsoft uvádí, že testování stejného promptu s různým formátováním napříč modely ukázalo výrazné rozdíly v úspěšnosti - od 13 % do 82 % pouze změnou strukturování informací.

Nástroj je dostupný jako [rozšíření pro VS Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-poml) poskytující zvýraznění syntaxe a automatické dokončování. SDK existuje pro [Python](https://pypi.org/project/poml/) i [Node.js](https://www.npmjs.com/package/pomljs). Dokumentace je k dispozici na [oficiálních stránkách](https://microsoft.github.io/poml/) a zdrojový kód je publikován na [GitHubu](https://github.com/microsoft/poml).

## Praktické využití

POML se hodí pro scénáře se složitou integrací dat, kdy prompty vyžadují kombinaci různých typů souborů, externích API nebo dynamického sestavování obsahu. Datové komponenty eliminují značnou část přípravného kódu.

Nástroj má smysl pro týmy, které spolupracují na tvorbě promptů. Více vývojářů může pracovat na stejných promptech s jasným rozdělením odpovědností. Správa verzí se stává čitelnější, protože změny se týkají konkrétních komponent namísto nestrukturovaných textových bloků.

Organizace podporující různé poskytovatele jazykových modelů mohou využít systém stylů pro optimalizaci podle konkrétního modelu bez udržování samostatných verzí promptů. Stejný logický prompt se automaticky přizpůsobí formátovacím požadavkům Claude, GPT nebo jiných modelů.

Pro podnikové nasazení nabízí POML možnost opakovaného použití komponent. Desítky promptů napříč projekty mohou sdílet společné definice, příklady a formáty. Systematická organizace usnadňuje správu rozsáhlých systémů založených na umělé inteligenci.

## Omezení

Pro jednoduché prompty s minimální integrací dat přidává POML zbytečnou složitost. Prostý text s dobrou strukturou funguje dostatečně. Počáteční fáze projektů, kdy probíhá rychlé experimentování s různými přístupy, může strukturovaný formát spíše zpomalovat.

Nástroj vyžaduje vstupní investici do učení syntaxe a konceptů. Tato investice se vyplatí při dlouhodobé práci se složitými prompty, nikoli při jednorázových úkolech.

Microsoft uvádí zlepšení přesnosti až o 929 % v některých případech díky lepšímu formátování promptů. Údaj o 40% snížení doby vývoje a 65% poklesu konfliktů při správě verzí pochází z interního nasazení v podnikových týmech. Tyto hodnoty závisí na konkrétní situaci a nelze je zobecnit na všechny případy použití.

Více informací o POML je dostupných v [oficiální dokumentaci](https://microsoft.github.io/poml/) a v [úložišti na GitHubu](https://github.com/microsoft/poml).