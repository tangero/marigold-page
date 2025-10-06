---
author: Patrick Zandl
categories:
- AI
- Testování
- Playwright
- Microsoft
- Automatizace
layout: post
post_excerpt: Nástroj Playwright od Microsoftu integruje AI agenty pro plánování, generování a opravu testů. Cílem je zefektivnit proces automatizovaného end-to-end testování webových aplikací.
summary_points:
- Microsoft integruje AI agenty do svého open-source nástroje Playwright
- Tři agenti – Planner, Generator, Healer – automatizují tvorbu a údržbu testů
- Planner analyzuje aplikaci a vytváří testovací plán v Markdownu
- Generator převádí plán na spustitelný testovací kód
- Healer se pokouší autonomně opravit selhávající testy
- Funkcionalita je dostupná od verze Playwright v1.56
title: "AI agenti v Playwright: Automatizace tvorby a oprav testů"
---

Open-source nástroj pro automatizované testování webových aplikací [Playwright](https://playwright.dev/), za kterým stojí společnost Microsoft, představil ve verzi 1.56 novou funkci nazvanou Agenti. Jedná se o sadu tří specializovaných AI nástrojů, jejichž účelem je zefektivnit celý životní cyklus testu: od počátečního návrhu přes generování kódu až po následnou opravu. Cílem je snížit množství manuální práce potřebné k tvorbě a údržbě sady automatizovaných testů.

Funkce se skládá ze tří samostatných komponent, které lze používat jednotlivě nebo v navazujícím procesu. Každý agent plní specifickou úlohu v procesu automatizace testování.

| Agent | Vstup | Výstup | Účel použití |
| :--- | :--- | :--- | :--- |
| **Planner (Plánovač)** | URL webové aplikace | Soubor `plan.md` | Analýza uživatelského rozhraní a vytvoření strukturovaného plánu testovacích scénářů. |
| **Generator (Generátor)** | Soubor `plan.md` | Testovací soubory (`*.spec.ts`) | Převod textového plánu na spustitelný testovací kód v syntaxi Playwright. |
| **Healer (Léčitel)** | Selhávající test | Upravený testovací soubor | Automatická oprava testu, který selhal z důvodu menších změn v aplikaci (např. změna selektoru). |

Já jsem zatím Playwright používal ponejvíce přes MCP, kdy se testy daly volat přímo z Claude Code. Playwright Agents (Planner, Generator, Healer) a Playwright MCP jsou ovšem dvě paralelní cesty, jak Microsoft integruje AI do svého testovacího frameworku. Zatímco MCP se zaměřuje na to, aby AI agenti mohli interaktivně ovládat prohlížeč, Playwright Agents se soustředí na komplexní generování a správu testovacích souborů.

### Komponenty a pracovní postup

**1. Planner (Plánovač)**

Prvním nástrojem v řetězci je Planner. Jeho funkcí je prozkoumat webovou aplikaci na zadané adrese a na základě analýzy její struktury a interaktivních prvků vygenerovat testovací plán. Tento plán je uložen do textového souboru ve formátu Markdown a obsahuje popis jednotlivých testovacích scénářů rozdělených do logických celků. Uplatnění nachází především při zahájení testování nové aplikace nebo její nové části, kdy dokáže rychle vytvořit základní sadu testů k pokrytí klíčových funkcí.

**2. Generator (Generátor)**

Generator navazuje na práci Plannera. Jako vstupní data používá Markdown soubor s testovacím plánem a na jeho základě vytváří konkrétní soubory s testovacím kódem pro Playwright. Tento proces převádí lidsky čitelný popis kroků, jako je "klikni na tlačítko Přihlásit" nebo "vyplň pole Jméno", na skutečný kód s lokátory a asercemi. Tímto způsobem výrazně urychluje přechod od návrhu testu k jeho implementaci.

**3. Healer (Léčitel)**

Poslední komponentou je Healer, který se zaměřuje na údržbu existujících testů. Jeho úkolem je analyzovat selhávající testy a pokusit se je autonomně opravit. Typickým příkladem je situace, kdy se v aplikaci změní identifikátor tlačítka nebo jiného prvku, což způsobí selhání testu, protože lokátor již není platný. Healer se v takovém případě pokusí najít nový, správný lokátor a upravit testovací kód. Jeho schopnosti jsou však limitovány na jednodušší opravy a nedokáže řešit komplexní chyby v logice aplikace nebo testu.

### Technická implementace

Pro využití agentů je nutné nejprve provést jejich inicializaci v projektu pomocí příkazu `npx playwright init-agents --loop=vscode`. Tento krok vygeneruje potřebnou konfiguraci. Součástí procesu je i vytvoření takzvaného "seed" souboru (výchozí soubor). Ten slouží k definici počátečního stavu aplikace před každým testem, například pro nastavení přihlášeného uživatele pomocí stavu uloženého v souboru `storageState.json` nebo pro přípravu testovacích dat pomocí fixtures. Tím je zajištěna konzistence a opakovatelnost testovacího prostředí.

Celý pracovní postup v praxi může vypadat následovně:
1.  **Inicializace a konfigurace**: Spuštění `init-agents` a úprava výchozího souboru pro nastavení testovacího prostředí.
2.  **Generování plánu**: Spuštění Plannera s cílem analyzovat aplikaci a vytvořit `plan.md`.
3.  **Generování testů**: Použití Generatora pro transformaci `plan.md` na spustitelné testovací soubory.
4.  **Spuštění a údržba**: Spuštění vygenerovaných testů. V případě selhání se lze pokusit o automatickou opravu pomocí Healera.

Nástroj Playwright Agents představuje krok směrem k větší automatizaci v procesu zajišťování kvality softwaru. Nejedná se o plnohodnotnou náhradu testovacího inženýra, ale spíše o asistenta, který může urychlit rutinní úkoly, jako je tvorba základních testovacích scénářů a oprava křehkých testů. Efektivita, zejména v případě Healera, bude silně závislá na konkrétní aplikaci a typu problému. Podrobnější technické informace a postupy jsou dostupné v [oficiální dokumentaci Playwright](https://playwright.dev/docs/test-agents).