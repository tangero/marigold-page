---
author: Patrick Zandl
categories:
- AI
- Anthropic
- Claude
- vývoj softwaru
- GitHub
layout: post
post_excerpt: Anthropic zpřístupnil Claude Code na webu, nástroj pro automatizované programování běžící v cloudu s podporou GitHub repozitářů a izolovaných vývojových prostředí. Nově můžete s Claude Code programovat přes webové rozhraní, i ve vašem mobilu!
summary_points:
- Claude Code na webu umožňuje spouštět programovací úlohy asynchronně v zabezpečeném cloudovém prostředí
- Služba je dostupná pro Pro a Max uživatele přes claude.ai/code s přímou integrací GitHub
- Vývojáři mohou přesouvat rozpracované úlohy mezi webovým rozhraním a lokálním terminálem
- Prostředí obsahuje předinstalované nástroje pro Python, Node.js, Java, Go, Rust a C++
- Bezpečnost zajišťují izolované virtuální stroje, omezený síťový přístup a proxy pro citlivé operace
- Služba sdílí rychlostní limity s ostatním používáním Claude v rámci účtu
title: Anthropic spustil Claude Code na webu 
---

Společnost Anthropic, známá vývojem konverzačního modelu Claude, zpřístupnila novou funkci Claude Code na webu. Jde o nástroj pro automatizované programování, který běží na vzdálené infrastruktuře a umožňuje vývojářům zadávat úlohy přes webové rozhraní bez nutnosti lokální instalace. Služba je momentálně ve výzkumné beta verzi a dostupná pro předplatitele tarifů Pro a Max. 

Anthropic tak vyslyšel časté požadavky uživatelů Claude Code a také reaguje na rostoucí popularitu konkurenční služby [Droid](https://www.vibecoding.cz/articles/droid-ai-agent/).

## Způsob fungování a použití

Claude Code na webu představuje cloudovou variantu nástroje pro automatizované programování. Vývojáři se připojují přes adresu [claude.ai/code](https://claude.ai/code), kde po propojení s GitHub účtem mohou zadávat programovací úlohy. Systém následně naklonuje repozitář do izolovaného virtuálního stroje spravovaného Anthropicem, připraví vývojové prostředí a provede požadované úpravy kódu.

![Claude Code pro web](https://www.marigold.cz/assets/claude-code-pro-web.png)

Služba se hodí především pro standardizované úlohy, které nevyžadují časté zásahy programátora. Anthropic uvádí jako vhodné scénáře opravy chyb, práci na repozitářích, které vývojář nemá stažené lokálně, nebo změny v backendovém kódu, kde může systém nejprve napsat testy a následně kód, který testy projde. Funkci lze využít i pro paralelní práci na více opravách současně.

Zajímavou možností je přesun rozpracované úlohy mezi webovým rozhraním a lokálním terminálem. Vývojář může například nastartovat úlohu přes webové rozhraní během cesty a později ji převzít do svého lokálního vývojového prostředí. Stávající lokální změny se při převzetí vzdálené session automaticky uloží stranou.

## Technické prostředí a podpora nástrojů

Anthropic připravil univerzální obraz operačního systému s předinstalovanými nástroji pro nejběžnější programovací jazyky a ekosystémy. Prostředí zahrnuje Python 3.x s nástroji pip, poetry a běžnými vědeckými knihovnami, aktuální LTS verze Node.js s npm, yarn a pnpm, OpenJDK s Maven a Gradle, stabilní verzi Go s podporou modulů, toolchain Rustu s cargo a překladače GCC a Clang pro C++.

Pro zjištění dostupných nástrojů může vývojář požádat Claude Code o spuštění příkazu `check-tools`, který zobrazí seznam nainstalovaných programovacích jazyků, správců balíčků a vývojových nástrojů. Prostředí lze dále přizpůsobit pomocí tzv. SessionStart hooks, které umožňují automatickou instalaci specifických závislostí při startu session.

Konfiguraci závislostí lze provést v souboru `.claude/settings.json` v repozitáři, kde se definuje spouštěcí skript. Tento mechanismus umožňuje například automatickou instalaci balíčků přes npm nebo pip při každém spuštění nové session. Hooky mohou rozlišovat mezi lokálním a vzdáleným prostředím pomocí proměnné prostředí `CLAUDE_CODE_REMOTE`.

## Bezpečnostní opatření a izolace

Každá session běží v samostatném izolovaném virtuálním stroji, kde má Claude Code přístup pouze k aktuálnímu repozitáři. Systém nesdílí data mezi různými sessions a citlivá pověření jako přihlašovací tokeny nebo podpisové klíče se nikdy nedostanou do samotného sandboxu s Claude Code.

Pro operace s GitHubem využívá systém dedikovanou proxy službu. Uvnitř sandboxu se git klient ověřuje pomocí omezeného pověření, které proxy ověří a přeloží na skutečný přihlašovací token uživatele. Proxy zároveň omezuje operace push pouze na aktuální pracovní větev z bezpečnostních důvodů.

Síťový přístup je standardně omezený na seznam povolených domén. Všechny odchozí HTTP a HTTPS požadavky procházejí bezpečnostní proxy, která poskytuje ochranu proti škodlivým požadavkům, omezení rychlosti a filtrování obsahu. Vývojář může síťový přístup úplně zakázat nebo naopak povolit úplný přístup podle potřeb projektu.

## Povolené domény a správa přístupu

Při výchozím omezeném síťovém přístupu má systém povolený přístup k důležitým službám vývojářské infrastruktury. Seznam zahrnuje služby Anthropicu, systémy pro správu verzí jako GitHub, GitLab a Bitbucket, kontejnerové registry včetně Docker Hubu a registrů Google, Microsoft a GitHub, cloudové platformy Google Cloud, Azure a související služby Microsoft.

Dále jsou povoleny správci balíčků pro všechny podporované jazyky - npm a Yarn pro JavaScript, PyPI pro Python, RubyGems, Crates.io pro Rust, Go proxy, Maven a Gradle pro JVM jazyky, stejně jako správce balíčků pro PHP, .NET, Dart, Elixir, Perl, iOS/macOS a další. K dispozici jsou i repozitáře Linuxových distribucí, vývojové nástroje jako Kubernetes nebo HashiCorp produkty a další běžně používané služby.

U domén označených hvězdičkou je povolen přístup ke všem subdoménám. Vývojář může síťový přístup upravit přidáním nového prostředí nebo úpravou stávajícího v nastavení. Doporučené bezpečnostní postupy zahrnují princip minimálních oprávnění, pravidelný audit povolených domén a upřednostnění HTTPS před HTTP.

## Ceny a omezení

Claude Code na webu sdílí rychlostní limity se vším ostatním používáním služby Claude v rámci účtu. Spuštění více úloh paralelně spotřebovává limity úměrně počtu běžících sessions. Služba je momentálně dostupná v beta verzi pro uživatele tarifů Pro a Max, v budoucnu má být rozšířena i na prémiová místa v tarifech Team a Enterprise.

Existují určitá technická omezení. Session lze přesunout z webu do lokálního terminálu pouze pokud je vývojář přihlášen ke stejnému účtu. Služba funguje výhradně s repozitáři hostovanými na GitHubu - GitLab a další platformy nejsou podporovány pro cloudové sessions.

Pro efektivní využití Anthropic doporučuje konfigurovat SessionStart hooky pro automatizaci přípravy prostředí a instalace závislostí. Důležité je také jasně specifikovat požadavky a příkazy v souboru CLAUDE.md v repozitáři. Pokud projekt používá soubor AGENTS.md, lze jej do CLAUDE.md zahrnout pomocí odkazu @AGENTS.md pro udržení jediného zdroje pravdy.

Více informací o službě naleznete v [dokumentaci Claude Code](https://docs.claude.com/en/docs/claude-code) na webu Anthropicu.