---
author: Patrick Zandl
categories:
- AI
- OpenAI
- GPT-5
- Codex
- vývojové nástroje
layout: vibecoding-default
post_excerpt: OpenAI uvedlo model GPT-5 s výrazně lepšími schopnostmi programování a nižší chybovostí. Součástí je Codex CLI pro lokální vývoj a cloudový Codex pro paralelní zpracování úloh.
summary_points:
- GPT-5 dosahuje 74,9% úspěšnosti na SWE-bench oproti 69,1% u modelu o3
- Codex CLI umožňuje lokální běh programovacího agenta přímo v terminálu
- Model generuje o 80% méně faktických chyb než předchozí verze
- Dostupný pro všechny úrovně předplatného včetně bezplatných uživatelů
- Cena API začíná na 0,05 USD za milion vstupních tokenů u varianty nano
- Podpora paralelního volání nástrojů a strukturovaných výstupů
title: OpenAI představuje GPT-5 v rámci Codex CLI
---

OpenAI spustilo [nový jazykový model GPT-5](https://www.marigold.cz/item/openai-gpt-5/), který představuje významný posun v oblasti programování a spolehlivosti. Model je dostupný ve třech velikostech prostřednictvím rozhraní API a integrován do vývojových nástrojů Codex. Společně s modelem firma zpřístupnila lokální nástroj Codex CLI a cloudovou verzi Codex pro paralelní zpracování programovacích úloh. Pojďme se na tyto novinky podívat podrobněji. 

## Výkonnostní parametry a srovnání

Model GPT-5 dosahuje na benchmarku SWE-bench Verified, který hodnotí schopnost řešit reálné programovací úlohy, skóre 74,9 procent. To představuje zlepšení oproti modelu o3 se skóre 69,1 procent. Na benchmarku Aider Polyglot pro práci s různými programovacími jazyky dosahuje 88 procent úspěšnosti. Pro srovnání, model Claude Opus 4.1 od společnosti Anthropic dosahuje na SWE-bench Verified 74,5 procent, zatímco Gemini 2.5 Pro od Google DeepMind 59,6 procent.

V oblasti matematiky model dosahuje 94,6 procent na testu AIME 2025 bez použití externích nástrojů. Na multimodálním benchmarku MMMU pro porozumění obrazu a textu získává 84,2 procent. V medicínských otázkách na HealthBench Hard dosahuje 46,2 procent správných odpovědí s mírou halucinací pouhých 1,6 procent.

Zásadní zlepšení přináší model v oblasti faktické přesnosti. Při testování na benchmarcích LongFact a FactScore generuje o 80 procent méně faktických chyb než model o3. S aktivovaným webovým vyhledáváním na anonymizovaných produkčních datech obsahují odpovědi o 45 procent méně faktických chyb než u modelu GPT-4o.

## Codex CLI pro lokální vývoj

[Codex CLI](https://github.com/openai/codex) představuje open-source nástroj příkazového řádku, který běží lokálně na počítači vývojáře. Nástroj umožňuje generování kódu, jeho úpravy a spouštění v izolovaném prostředí přímo z terminálu. Zdrojový kód nikdy neopouští lokální prostředí, pokud se uživatel nerozhodne jej sdílet.

Instalace vyžaduje jediný příkaz `npm install -g @openai/codex`. Nástroj podporuje multimodální vstupy včetně textu, snímků obrazovky a diagramů. Vývojáři mohou volit mezi třemi režimy schvalování změn podle požadované míry kontroly nad prováděnými úpravami.

Pro přihlášení stačí použít účet ChatGPT Plus, Pro nebo Team. Systém automaticky vygeneruje a nakonfiguruje potřebné API klíče. Uživatelé s předplatným Plus a Pro získávají po dobu 30 dnů kredity ve výši 5 respektive 50 dolarů pro využití API.

Ve výchozím nastavení nástroj používá model o4-mini pro rychlé uvažování, lze však specifikovat jakýkoliv model dostupný v Responses API včetně GPT-5. Nástroj oficiálně podporuje systémy macOS a Linux, podpora Windows je experimentální a může vyžadovat WSL2.

## Cloudový Codex pro paralelní zpracování

[Cloudová verze Codex](https://openai.com/codex/) pracuje jako programovací agent schopný zpracovávat více úloh současně. Každá úloha běží v samostatném izolovaném cloudovém prostředí s předem načteným repozitářem. Systém dokáže psát nové funkce, odpovídat na otázky o kódové základně, opravovat chyby a připravovat pull requesty.

Přístup k nástroji je integrován do postranního panelu ChatGPT. Nové programovací úlohy se zadávají psaním promptu a kliknutím na tlačítko "Code". Pro dotazy na existující kódovou základnu slouží tlačítko "Ask". Dokončení úlohy obvykle trvá mezi 1 až 30 minutami podle složitosti. Průběh zpracování lze sledovat v reálném čase.

Codex poskytuje ověřitelné důkazy o provedených akcích prostřednictvím citací terminálových logů a výstupů testů. Po dokončení úlohy systém provede commit změn ve svém prostředí. Vývojář může výsledky zkontrolovat, požádat o další revize, otevřít GitHub pull request nebo přímo integrovat změny do lokálního prostředí.

Nástroj lze řídit pomocí souborů AGENTS.md umístěných v repozitáři. Tyto textové soubory podobné README.md obsahují instrukce pro navigaci v kódové základně, příkazy pro spouštění testů a informace o standardních postupech projektu.

## Cenová struktura a dostupnost

Model GPT-5 je dostupný ve třech velikostech s následujícím cenovým modelem:

| Varianta | Vstupní tokeny (za 1M) | Výstupní tokeny (za 1M) |
|----------|------------------------|-------------------------|
| GPT-5 | 1,25 USD | 10 USD |
| GPT-5 mini | 0,25 USD | 2 USD |
| GPT-5 nano | 0,05 USD | 0,40 USD |

Modely podporují parametry API `reasoning_effort` a `verbosity`, vlastní nástroje, paralelní volání nástrojů a vestavěné nástroje včetně webového vyhledávání, vyhledávání souborů a generování obrázků. Dostupné jsou také funkce pro úsporu nákladů jako cache promptů a Batch API.

V ChatGPT je GPT-5 postupně zpřístupňován všem uživatelům včetně bezplatné verze. Uživatelé Pro získávají neomezený přístup k GPT-5 a navíc přístup k variantě GPT-5 Pro s rozšířeným uvažováním. Uživatelé Plus mohou model používat jako výchozí pro každodenní dotazy s výrazně vyšším limitem využití než bezplatní uživatelé. Po vyčerpání limitu bezplatní uživatelé automaticky přecházejí na GPT-5 mini.

## Technické vlastnosti a integrace

Model GPT-5 generuje o 50 až 80 procent méně výstupních tokenů než model o3 při zachování nebo zlepšení výkonu napříč schopnostmi včetně vizuálního uvažování, agentického programování a řešení vědeckých problémů na postgraduální úrovni. Trénování proběhlo na superpočítačích Microsoft Azure AI.

Při práci na programovacích úlohách model proaktivně dokončuje ambiciózní úkoly bez nutnosti schvalování jednotlivých kroků. Během zpracování úlohy vypisuje plány, aktualizace stavu a souhrny mezi jednotlivými voláními nástrojů. Dokáže vytvářet komplexní aplikace z jediného promptu včetně esteticky propracovaných webových stránek a her.

Model codex-1, optimalizovaná verze o3 pro softwarové inženýrství, byl trénován pomocí posilovaného učení na reálných programovacích úlohách. Generuje kód, který odpovídá lidskému stylu a preferencím pro pull requesty, přesně dodržuje instrukce a iterativně spouští testy až do úspěšného dokončení.

## Iniciativa pro open source projekty

OpenAI spustilo iniciativu s rozpočtem 1 milion dolarů na podporu open source projektů využívajících Codex CLI a další modely společnosti. [Granty jsou udělovány až do výše 25 000 dolarů](https://openai.com/codex/) v kreditech API. Žádosti jsou posuzovány průběžně.

Projekt Codex CLI je aktivně vyvíjen jako open source. Společnost začleňuje příspěvky od komunity. Vývojáři mohou otevírat diskuse nebo hlásit problémy přímo v [GitHub repozitáři projektu](https://github.com/openai/codex).