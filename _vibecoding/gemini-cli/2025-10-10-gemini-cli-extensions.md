---
author: Patrick Zandl
categories:
- AI
- Google
- Gemini CLI
- vývojářské nástroje
- srovnání
layout: post
post_excerpt: Google uvedl systém rozšíření pro Gemini CLI, který umožňuje integraci externích nástrojů. 
summary_points:
- Google spustil systém rozšíření pro Gemini CLI, který propojuje terminál s externími nástroji a službami
- Rozšíření obsahují integrované návody neboli playbook, servery MCP, kontextové soubory a vlastní příkazy
- Platformu používá přes milion vývojářů s velkoryse nastaveným bezplatným limitem 60 požadavků za minutu
- Startovní partneři zahrnují Dynatrace, Elastic, Figma, Harness, Postman, Shopify, Snyk a Stripe
- Na rozdíl od Claude Code pluginů má Gemini CLI otevřenější model bez nutnosti schvalování rozšíření společností Google
- Google vytvořil vlastní sadu rozšíření pro Cloud Run, GKE, Firebase, Flutter a další služby ekosystému
title: Google představil rozšíření pro Gemini CLI a otevřel platformu vývojářům
---

Společnost Google rozšířila funkcionalitu svého nástroje Gemini CLI o systém rozšíření (extensions), který vývojářům umožňuje propojit terminál s externími nástroji bez nutnosti přepínání kontextu. Novinku představila tři měsíce po spuštění tohoto nástroje pro agentní programování, který podle Google používá více než milion vývojářů.

![Gemini CLI extensions hero image](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/GeminiCLI_Expand_Hero.width-200.format-webp.webp)

Gemini CLI je opensourcový agentní nástroj pro terminál, který přináší možnosti modelu Gemini přímo do vývojového prostředí. Pracuje s modelem Gemini 2.5 Pro s kontextovým oknem jednoho milionu tokenů a nabízí bezplatný přístup s limitem 60 požadavků za minutu a tisíc požadavků denně. Nástroj spustila společnost Google v červnu tohoto roku jako konkurenci Claude Code od Anthropic a dalším agentním programovacím nástrojům.

## Architektura a komponenty rozšíření

Rozšíření pro Gemini CLI představují předpřipravené integrace, které připojují nástroj k externím službám. Každé rozšíření obsahuje integrovaný návod neboli playbook, který okamžitě učí model, jak efektivně používat nové nástroje. Vývojář získá funkční výsledky již při prvním použití bez složité konfigurace.

Technicky vzato rozšíření balí několik typů komponent do jednotné struktury. První komponentou jsou servery MCP neboli Model Context Protocol, které zajišťují připojení k externím nástrojům a službám. Protokol MCP vytváří jednotné rozhraní mezi modelem a různými zdroji dat či funkcionalitou.

Druhou komponentou jsou kontextové soubory, typicky ve formátu GEMINI.md nebo jiných uživatelských formátech. Tyto soubory poskytují modelovi specifické instrukce a pravidla pro práci s daným nástrojem. Google zde navázal na standard, který představila komunita vývojářů pracujících s agentními nástroji.

Třetí typ tvoří vyloučené nástroje neboli excluded tools. Tato funkce umožňuje zakázat vestavěné nástroje nebo nabídnout alternativní implementace. Poslední komponentou jsou vlastní příkazy neboli custom commands, které zapouzdřují složité prompty do jednoduchých příkazů začínajících lomítkem.

Instalace rozšíření probíhá příkazem `gemini extensions install` s uvedením URL na GitHub nebo lokální cestou. Systém automaticky načte konfiguraci rozšíření při spuštění Gemini CLI a sloučí ji s nastavením pracovního prostoru. Při konfliktech mají přednost nastavení konkrétního projektu.

## Ekosystém partnerů a dostupná rozšíření

Google spustil [stránku rozšíření pro Gemini CLI](https://geminicli.com/extensions/), kde vývojáři najdou rostoucí katalog komunitních, partnerských a Google rozšíření seřazených podle popularity měřené počtem hvězdiček na GitHubu. Platforma odstartovala s osmi významnými partnery z řad průmyslových lídrů.

![Gemini CLI extension launch partners](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/extensions-partners-grid.width-100.format-webp.webp)

Společnost [Dynatrace](https://github.com/dynatrace-oss/dynatrace-mcp), která se specializuje na monitorování aplikací, poskytuje rozšíření pro získávání přehledů o výkonu aplikací, dostupnosti a analýze základních příčin přímo z terminálové řádky. Cílem je urychlit ladění aplikací.

[Elastic](https://github.com/elastic/gemini-cli-elasticsearch) připojuje vyhledávání a analýzu dat z Elasticsearch do vývojářských pracovních postupů. Rozšíření se připojuje přímo k MCP serveru hostovanému v Elastic Cloud Serverless, což umožňuje agentům pracovat s firemními daty.

Návrhářská platforma [Figma](https://github.com/figma/figma-gemini-cli-extension) nabízí možnost generovat kód z rámců, extrahovat návrhový kontext, získávat zdroje a zajišťovat konzistenci návrhového systému s kódovou základnou. Vývojáři tak mohou pracovat s návrhy přímo z terminálu.

Platforma [Harness](https://github.com/harness/mcp-server) pro kontinuální integraci a nasazení přináší možnost analyzovat data o provádění pipeline, odhalovat nákladové přehledy, detekovat vzory selhání a automaticky řešit problémy pro urychlení dodávky softwaru.

[Postman](https://github.com/postmanlabs/postman-mcp-server/blob/main/gemini-extension.json), nástroj pro práci s API, umožňuje agentním systémům přistupovat k pracovním prostorům, spravovat kolekce a prostředí, vyhodnocovat API a automatizovat pracovní postupy pomocí přirozeného jazyka.

E-commerce platforma [Shopify](https://github.com/Shopify/dev-mcp-gemini-cli) propojuje vývojářský ekosystém s nástroji pro vyhledávání dokumentace, prozkoumávání API schémat a vytváření bezserverových funkcí pro Shopify.

Bezpečnostní platforma [Snyk](https://github.com/snyk/agentic-integration-wrappers) integruje komplexní bezpečnostní schopnosti do vývojového procesu, aby zajistila bezpečnost kódu již v okamžiku jeho vytvoření. [Stripe](https://github.com/stripe/agent-toolkit/blob/main/gemini-extension.json) definuje sadu nástrojů pro interakci s platební API a vyhledávání ve znalostní bázi.

## Rozšíření vytvořená společností Google

Google vytvořil vlastní sadu rozšíření zaměřenou na integraci s ekosystémem služeb Google Cloud a vývojářskými nástroji. Pro cloudové nasazení nabízí [rozšíření Cloud Run](https://github.com/GoogleCloudPlatform/cloud-run-mcp), které umožňuje přejít z lokálního kódu na živou veřejnou URL jediným krokem.

[Rozšíření GKE](https://github.com/GoogleCloudPlatform/gke-mcp) spravuje clustery Google Kubernetes Engine od kontroly stavu uzlů po nasazování aplikací. [Rozšíření gcloud](https://github.com/gemini-cli-extensions/gcloud) poskytuje snadnou interakci s prostředím Google Cloud a [rozšíření Google Cloud Observability](https://github.com/gemini-cli-extensions/observability) pomáhá pochopit, spravovat a řešit problémy cloudového prostředí.

Pro vývojáře aplikací Google připravil [rozšíření Code Review](https://github.com/gemini-cli-extensions/code-review) pro kontrolu kódové základny a [bezpečnostní rozšíření](https://github.com/gemini-cli-extensions/security) pro detekci zranitelností pomocí umělé inteligence. [Rozšíření Google Maps Platform](https://github.com/googlemaps/platform-ai) získává informace o místech a vkládá mapy do aplikací.

[Rozšíření Flutter](https://github.com/gemini-cli-extensions/flutter) pomáhá vytvářet, sestavovat, refaktorovat, ladit a udržovat Flutter aplikace. [Rozšíření Chrome DevTools](https://github.com/ChromeDevTools/chrome-devtools-mcp) ovládá a kontroluje živý prohlížeč Chrome pro spolehlivou automatizaci, hloubkové ladění a analýzu výkonu.

[Rozšíření Firebase](https://github.com/gemini-cli-extensions/firebase) nastavuje a spravuje Firebase backend a [rozšíření Genkit](https://github.com/gemini-cli-extensions/genkit) vylepšuje uživatelskou zkušenost při vytváření aplikací poháněných generativní umělou inteligencí.

Pro práci s daty Google vytvořil [rozšíření Looker](https://github.com/gemini-cli-extensions/looker) pro zkoumání a vizualizaci obchodních dat. [Rozšíření Data Cloud](https://cloud.google.com/blog/products/databases/gemini-cli-extensions-for-google-data-cloud) umožňují vytvářet aplikace a analyzovat trendy se službami jako Cloud SQL, AlloyDB a BigQuery. [MCP Toolbox for Databases](https://github.com/gemini-cli-extensions/mcp-toolbox) připojuje k podnikovým datům snadno a bezpečně.

Pro zábavu Google přidal [rozšíření Nano Banana](https://github.com/gemini-cli-extensions/nanobanana), které generuje a upravuje obrázky přímo z terminálu.

## Technické detaily a použití

Rozšíření žijí ve struktuře adresářů, kde každé rozšíření má vlastní složku s konfiguračním souborem. Při spuštění Gemini CLI prohledá tento adresář a sloučí konfigurace rozšíření s nastavením pracovního prostoru. Parametr contextFileName ukazuje na dokumentační soubory, výchozí je GEMINI.md. Pole excludeTools blokuje specifické nástroje modelu nebo omezuje příkazy.

Vlastní příkazy rozšiřují funkcionalitu pomocí souborů TOML umístěných v podadresáři commands. Tyto příkazy následují standardní konvence pojmenování a objevují se v menu nápovědy označené názvem rozšíření. Když dojde ke kolizi názvů příkazů s uživatelskými nebo projektovými příkazy, verze z rozšíření dostane prefix s názvem rozšíření.

Když vývojář spustí příkaz, Gemini CLI konzultuje playbook a využívá kontext z prostředí jako jsou lokální soubory a stav gitu k provedení správného nástroje přesně podle záměru. Rozdíl oproti čistému MCP je v tom, že zatímco MCP poskytuje holé připojení k nástroji, rozšíření Gemini CLI obaluje základní schopnost používat nástroj vrstvou inteligence a personalizace.

Praktické použití ukazuje například rozšíření pro Cloud SQL a PostgreSQL. Vývojář může vytvořit instanci Cloud SQL příkazem pro vytvoření instance, vypsat všechny instance v projektu, získat informace o konkrétní instanci nebo vytvořit uživatelský účet včetně podpory pro standardní uživatele i Cloud IAM uživatele.

Před spuštěním Gemini CLI je třeba nakonfigurovat rozšíření pro připojení k projektu Google Cloud přidáním potřebných proměnných prostředí. Seznam nainstalovaných rozšíření zobrazí příkaz `/extensions`, seznam MCP serverů a nástrojů pak příkaz `/mcp list`.

## Srovnání s Claude Code pluginy

Systémy rozšíření pro Gemini CLI a Claude Code sdílejí společný cíl - umožnit vývojářům přizpůsobit si agentní programovací nástroje. Oba systémy používají Model Context Protocol pro připojení k externím službám a oba nabízejí možnost vytvářet vlastní příkazy a integrovat externí nástroje.

Klíčový rozdíl spočívá v přístupu k publikování rozšíření. Google zvolil plně otevřený model, kde kdokoliv může publikovat rozšíření hostované na veřejných GitHub repozitářích bez čekání na schválení nebo zapojení společnosti Google. Uživatelé instalují rozšíření manuálně z GitHub URL nebo lokálních cest.

Claude Code používá systém tržišť neboli marketplaces, kde pluginy procházejí určitou mírou kurátorství. Instalace probíhá příkazy `/plugin install` a `/plugin marketplace add`. Systém podporuje automatickou instalaci pluginů na úrovni repozitáře pro týmovou spolupráci, když členové týmu označí adresář projektu jako důvěryhodný.

Strukturálně se systémy liší v organizaci komponent. Claude Code pluginy obsahují adresáře `commands/`, `agents/`, `hooks/` a `.mcp.json` pro různé typy funkcionalita. Gemini CLI rozšíření používají jediný konfigurační soubor `gemini-extension.json`, který definuje všechny komponenty včetně MCP serverů, kontextových souborů, vyloučených nástrojů a vlastních příkazů.

Claude Code klade důraz na specializované agenty s konkrétními osobnostmi a rolemi. Vývojář může vytvořit agenta jako bezpečnostního auditora nebo frontend vývojáře s vlastním stylem komunikace. Gemini CLI pracuje spíše s kontextovými soubory a playbook, které definují, jak má model používat nástroje, bez vytváření explicitních person.

V oblasti automatizace Claude Code nabízí háčky neboli hooks, které automaticky spouštějí akce v určitých okamžicích vývojového procesu. Například háček může spustit testovací sadu po změně kódu. Gemini CLI podobnou funkcionalitu přímo nenabízí v rámci rozšíření, ale lze ji implementovat pomocí vlastních příkazů a MCP serverů.

Obě platformy podporují kontrolní body neboli checkpointing pro ukládání stavu před změnami. Claude Code umožňuje vrácení dvojím stisknutím klávesy Escape nebo příkazem `/rewind`. Gemini CLI používá příkazy `/restore` pro obnovu konkrétního kontrolního bodu.

Z hlediska integrace do vývojového prostředí má Claude Code nativní rozšíření pro VS Code v beta verzi, které zobrazuje změny v reálném čase přes postranní panel s inline diffy. Gemini CLI nabízí integraci s VS Code přes režim agenta v Gemini Code Assist, ale jedná se spíše o doplňkovou funkcionalitu než o plnohodnotné rozšíření.

Co se týče cenového modelu, Claude Code spotřebovává API tokeny podle standardního ceníku Anthropic - $3 za milion vstupních tokenů a $15 za milion výstupních tokenů pro model Claude Sonnet 4.5. Gemini CLI nabízí velkoryse nastavený bezplatný přístup s osobním Google účtem - 60 požadavků za minutu a tisíc požadavků denně. Pro profesionální vývojáře je k dispozici placená verze přes Google AI Studio nebo Vertex AI.

Komunita kolem obou nástrojů vytváří vlastní rozšíření. Pro Claude Code existují platformy jako aitmpl.com s přes 400 komponenty nebo GitHub repozitáře jako awesome-claude-code. Pro Gemini CLI Google vytvořil centrální stránku rozšíření na geminicli.com/extensions seřazenou podle popularity.

## Strategické pozadí a konkurence

Spuštění systému rozšíření pro Gemini CLI přichází v době, kdy agentní programovací nástroje získávají na významu. Dva dny před oznámením Google představil OpenAI funkci ChatGPT apps s podobným propojením na služby třetích stran. Google však zvolil diametrálně odlišný přístup než kurátorovaný model OpenAI.

Podle Ryan J. Salvy, senior ředitele produktového managementu pro vývojářské nástroje Google, představuje funkce rozšíření transformační změnu. Google sám intenzivně používá Gemini CLI pro vytváření a údržbu tohoto nástroje, přičemž produktoví manažeři pečlivě sledují vývoj.

Načasování oznámení signalizuje záměr Google agresivně získat pozornost vývojářů díky otevřenosti a rychlosti v okamžiku, kdy se nástroje umělé inteligence stávají centrem podnikových pracovních postupů. Zatímco OpenAI kontroluje, co se může integrovat s ChatGPT, Google umožňuje vývojářům publikovat integrace svobodně.

Analytici upozorňují, že Google tímto krokem staví Gemini CLI do pozice adaptabilnější a vývojářsky řízené platformy. Místo aby Google určoval, které nástroje jsou důležité, nechává toto rozhodnutí na komunitě a trhu. Počet více než milionu uživatelů po třech měsících od spuštění naznačuje, že strategie nachází odezvu.

## Budoucí směřování

Google poskytuje vývojářům [šablony](https://geminicli.com/docs/extensions/#extension-creation) a [průvodce krok za krokem](https://geminicli.com/docs/extensions/getting-started-extensions/) pro vytvoření prvního rozšíření. Platforma je plně opensourcová pod licencí Apache 2.0, což umožňuje komunitě kontrolovat kód, ověřovat bezpečnostní důsledky a přispívat vylepšeními.

Dokumentace nabízí několik směrů využití systému rozšíření. Vývojáři mohou kombinovat rozšíření, řetězit příkazy a vytvářet personalizované řetězce nástrojů přesně odpovídající jejich pracovnímu stylu. Pro streamlining osobního pracovního postupu nebo integraci firemních interních nástrojů mají nyní potřebné nástroje.

Google očekává růst ekosystému rozšíření a aktivní účast globální komunity vývojářů. Problémy lze hlásit a nápady sdílet na GitHub repozitáři projektu. Společnost vytvořila infrastrukturu pro objevování a sdílení rozšíření s transparentním řazením podle popularity.

Platforma staví na vznikajících standardech jako MCP, systémové prompty přes GEMINI.md a nastavení pro osobní i týmovou konfiguraci. Google uznává, že terminál je osobní prostor a každý si zaslouží autonomii k jeho přizpůsobení podle vlastních potřeb.

Oficiální dokumentace rozšíření je dostupná na [docs](https://geminicli.com/docs/extensions/), stránka s katalogem rozšíření na [geminicli.com/extensions](https://geminicli.com/extensions/) a kód platformy na [GitHubu](https://github.com/google-gemini/gemini-cli).