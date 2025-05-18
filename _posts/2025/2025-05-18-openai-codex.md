---
author: Patrick Zandl
categories:
- AI
- vibecoding
- programování
- OpenAI
layout: post
post_excerpt: OpenAI představila _výzkumnou preview verzi_ nového nástroje nazvaného Codex. Tedy nejde o totální novinku, Codex již byl předsaven jako aplikace Codex CLI pro příkazovou řádku, nyní jde ale o kompletnější webové rozhraní.
summary_points:
- OpenAI představila Codex jako výzkumnou preview verzi nástroje pro vývoj software.
- Codex je cloudový software založený na modelu codex-1 optimalizovaném pro generování
  kódu.
- Nástroj je dostupný pro uživatele ChatGPT Pro, Enterprise a Team s plánem rozšíření.
- Codex pracuje v izolovaném prostředí, umožňuje sledovat průběh a integrovat změny.
- AGENTS.md soubory pomáhají řídit chování Codexu v kódové základně.
- Codex dosahuje 70-75% úspěšnosti na benchmarku SWE-Bench Verified.
- OpenAI implementovala bezpečnostní opatření proti zneužití pro škodlivý software.
- Běžné použití zahrnuje refaktorizaci, psaní testů a opravy chyb.
- Codex CLI nabízí rychlejší pracovní postupy s modelem codex-mini-latest.
- Nástroj má omezení jako chybějící podpora obrázků nebo interaktivní korekce.
- OpenAI plánuje budoucí vylepšení jako hlubší integrace s GitHubem.
thumbnail: https://www.marigold.cz/assets/openai-thumbnail.png
title: OpenAI představuje Codex - agenta pro vývoj software
---

# OpenAI představuje Codex - agenta pro vývoj software

OpenAI představila "výzkumnou preview verzi" nového nástroje nazvaného [Codex](https://chatgpt.com/codex). Tedy nejde o totální novinku, Codex již byl předsaven jako aplikace Codex CLI pro příkazovou řádku, nyní jde ale o kompletnější webové rozhraní. Ačkoliv nedosahuje komplexnosti služeb jako Lovable, jde o zajímavého agenta pro vývoj software. 

Hlavní výhodou Codexu má být schopnost paralelně pracovat na mnoha úkolech. Podívejme se detailně na to, co tento nástroj přináší, jaké jsou jeho možnosti a omezení.

## Co je Codex?

Codex je cloudový software založený na modelu codex-1, což je verze modelu OpenAI o3 optimalizovaná pro softwarové inženýrství. Podle dokumentace byl tento model trénován pomocí reinforcement learning na reálných úkolech kódování v různých prostředích. Hlavním cílem bylo generovat kód, který napodobuje lidský styl psaní, přesně dodržuje instrukce a dokáže iterativně spouštět testy, dokud nedosáhne úspěšného výsledku.

![codex](/assets/codex-landing.jpg)

## Dostupnost a rozšíření

V současné době je Codex **dostupný pro uživatele ChatGPT Pro,** ChatGPT Enterprise a ChatGPT Team. OpenAI plánuje v budoucnu rozšířit dostupnost i pro uživatele ChatGPT Plus a ChatGPT Edu. Během výzkumné preview fáze mají uživatelé k dispozici "velkorysý přístup bez dodatečných nákladů" po dobu několika týdnů. Následně OpenAI plánuje zavést cenovou politiku s možností dokoupit dodatečné využití podle potřeby.

## Jak Codex funguje

Přístup k Codexu je možný přes postranní panel v ChatGPT. Uživatelé mohou zadat nové úkoly kódování zadáním promptu a kliknutím na tlačítko "Code". Pro dotazy na kódovou základnu lze použít tlačítko "Ask".

Každý úkol je zpracováván nezávisle v samostatném izolovaném prostředí, které je předem naplněno kódovou základnou uživatele. Codex může číst a upravovat soubory, spouštět příkazy včetně testů, linterů a kontroly typů. Uživatel může sledovat postup v reálném čase. Dokončení úkolu typicky trvá mezi 1 a 30 minutami v závislosti na složitosti. Po dokončení úkolu Codex provede commit svých změn ve svém prostředí a poskytne ověřitelné důkazy o svých akcích prostřednictvím citací terminálových logů a výstupů testů.

Uživatel pak může zkontrolovat výsledky, požádat o další revize, otevřít GitHub pull request nebo přímo integrovat změny do svého lokálního prostředí.

## AGENTS.md soubory

Zajímavým prvkem je možnost řídit Codex pomocí AGENTS.md souborů umístěných v repozitáři. Tyto textové soubory, podobně jako README.md, umožňují informovat Codex o tom, jak se orientovat v kódové základně, jaké příkazy spouštět pro testování a jak nejlépe dodržovat standardní postupy projektu. Podle OpenAI codex-1 vykazuje dobré výsledky i bez těchto souborů, ale jejich přítomnost může zlepšit efektivitu práce.

## Výkonnost a hodnocení

OpenAI poskytla několik měřítek výkonnosti codex-1:

- Na benchmarku SWE-Bench Verified dosahuje codex-1 přesnosti kolem 70-75%, což je významně více než o3-high (kolem 65-70%)
- Na interních SWE úkolech OpenAI dosahuje codex-1 přibližně 75% úspěšnosti, ve srovnání s o4-mini-high (70%), o3-high (67%) a o1-high (11%)

![swe](/assets/codex-swe-bench.png)

## Bezpečnost a zajištění důvěryhodnosti

OpenAI zmiňuje několik bezpečnostních opatření implementovaných v Codexu. Jde především o transparentnost, kdy uživatelé mohou verifikovat výstupy prostřednictvím citací, terminálových logů a výsledků testů. Při nejistotě nebo selhání testů agent explicitně komunikuje tyto problémy. Codex operuje v zabezpečeném izolovaném kontejneru v cloudu a během provádění úkolu má zakázán přístup k internetu - interaguje pouze s kódem poskytnutým přes GitHub repozitáře a předinstalované závislosti.

Přesto OpenAI zdůrazňuje, že je stále nezbytné, aby uživatelé manuálně kontrolovali a validovali veškerý agentem generovaný kód před integrací a spuštěním.

## Prevence zneužití

OpenAI uvádí, že implementovali opatření proti zneužití tohoto nástroje pro vývoj škodlivého softwaru:

- Codex byl trénován k identifikaci a odmítnutí požadavků zaměřených na vývoj škodlivého softwaru
- Současně by měl rozlišovat a podporovat legitimní úkoly
- OpenAI zdokonalila své politiky a začlenila přísná bezpečnostní hodnocení

Jako dodatek k dokumentaci o3 System Card byla publikována aktualizace odrážející tato hodnocení.

## Běžné případy použití

Technické týmy OpenAI již používají Codex jako součást svého každodenního pracovního postupu. Nejčastěji se používá pro refaktorizaci kódu, přejmenování proměnných a funkcí, psaní testů, vytváření základů nových funkcí, propojování komponent, opravy chyb a tvorbu dokumentace.

Vývojáři OpenAI si díky tomuto nástroji vytvářejí nové pracovní návyky jako třídění problémů v pohotovostní službě, plánování úkolů na začátku dne a delegace práce na pozadí. Mezi externí testovací organizace patří Cisco, Temporal, Superhuman a Kodiak.

![codex](/assets/Codex_Citations_02.webp)

## Aktualizace Codex CLI

Současně s uvedením Codexu OpenAI vydává menší verzi codex-1, která je verzí o4-mini optimalizovanou specificky pro Codex CLI. Tento model podporuje rychlejší pracovní postupy v CLI a je optimalizován pro dotazy a úpravy kódu s nízkou latencí.

Model je dostupný jako výchozí v Codex CLI a v API jako codex-mini-latest. Cenově je nastaven na:
- $1.50 za 1M vstupních tokenů
- $6 za 1M výstupních tokenů
- 75% sleva při cachování promptů

## Omezení a budoucí vývoj

Codex je stále v rané fázi vývoje a má několik omezení. Chybí mu možnost vstupů formou obrázků pro frontend práci, není možné korigovat agenta během jeho práce a delegování úkolu vzdálenému agentovi trvá déle než interaktivní úpravy.

OpenAI plánuje v budoucnu zavést interaktivnější a flexibilnější pracovní postupy, umožnit poskytování pokynů v průběhu úkolu, spolupracovat na strategiích implementace a posílat proaktivní aktualizace o pokroku. Dále chce vytvořit hlubší integrace s nástroji jako GitHub, Codex CLI, ChatGPT Desktop nebo systémy pro sledování problémů a CI.

## Technické parametry modelu codex-mini-latest

Codex-mini-latest je doladěná verze o4-mini specificky určená pro použití v Codex CLI:
- 200K kontextové okno
- 100K max výstupních tokenů
- Podpora "reasoning tokens"

## Něco málo osobní zkušenosti

Zkušenosti jsou zatím krátké. Zatím se ukazuje, že Codex dokáže dosti spolehlivě opravovat chyby, což by mohlo vést k plně automatizovanému procesu oprav a ušetřit značné množství času. Uživatelské rozhraní je pohodlnější, než Codex CLI v příkazové řádce, je to o dost intuitivnější a vůbec mi nechybí přehršel oken Cursoru. Jenže Cursor zatím také neodinstaluju... 

Codex není jen pasivní nástroj. Aktivně se zapojuje do pracovního procesu. Umí číst a upravovat soubory a spouštět různé příkazy, včetně testovacích nástrojů, linterů a kontroly typů. Tyto funkce pomáhají zajistit kvalitu kódu a odhalit potenciální problémy v rané fázi vývoje. Testovací nástroj funguje jako kontrola funkčnosti, linter jako nástroj pro hygienu a styl kódu a kontrola typů zajišťuje správné používání proměnných.

Dokončení úkolu s pomocí Codex obvykle trvá od 1 do 30 minut (ano, občas je to dlouhý!). Pro zajištění transparentnosti a důvěryhodnosti poskytuje Codex ověřitelné důkazy o svých akcích prostřednictvím citací z terminálových protokolů a výstupů testů.

Flexibilita je další důležitou vlastností Codex. Jeho prostředí lze do jisté míry konfigurovat tak, aby co nejvíce odpovídalo konkrétnímu vývojovému prostředí uživatele. Chování Codex lze dokonce řídit pomocí speciálního souboru agents.md umístěného v úložišti kódu.

Testování ukázalo, že Codex 1 dokáže pracovat s maximální délkou kontextu 192 000 tokenů a důsledně vytváří čistší patche připravené k okamžité integraci do standardních pracovních postupů. Přístup Codex k psaní kódu spočívá v práci v malých, cílených dávkách, které se zaměřují na konkrétní problémy.

V praxi Codex umožňuje vývojářům efektivně nastavit základy projektu a zaměřit se na implementaci aktuálních funkcí. Celkově nástroj mění způsob práce vývojářů, umožňuje jim pracovat téměř jako by byli svým vlastním týmem nebo manažerem týmu, s možností zadávat problémy a vracet se k nim po určité době.

Dalším zajímavým použitím by mohlo být automatizované opravování issues v gitu, kdy si Codex stáhne issues, navrhne opravy a odešle je zase do GITu, kde čekají na kontrolu a merge. 

## Závěr

Jak má Codex zapadat k probíhající [akvizici Windsurfu](/item/openai-kupuje-windsurf/), budou to soběžné projekty, nebo se spojí? Je Codex budoucí lídr agentického programování nebo jen další "my taky" software bez přidané hodnoty? Uvidíme... na to zatím žádné odpovědi nejsou, 