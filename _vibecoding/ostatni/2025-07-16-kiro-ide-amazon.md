---
author: Patrick Zandl
categories:
- AI
- IDE
- Kiro
- AWS
- Amazon
- vývojové nástroje
- automatizace
layout: post
post_excerpt: Amazon představil Kiro, vývojové prostředí s autonomními AI agenty pro specifikační vývoj. Používá modely Claude a konkuruje nástrojům jako Cursor a Windsurf. CEO Andy Jassy věří, že má potenciál transformovat vývoj software.
sw: kiro
summary_points:
- Kiro je nové AI vývojové prostředí od Amazonu s vlastní doménou a brandingem
- Vzniklo z malého týmu v AWS a používá Claude Sonnet 4 a 3.7 od Anthropic
- Konkuruje nástrojům jako Cursor, Windsurf a GitHub Copilot s autonomními agenty
- Zaměřuje se na specifikační vývoj na rozdíl od Amazon Q Developer
- Bude součástí Q Developer Pro subscription a má vlastní cenové tarify
- Demo projekt "Spirit of Kiro" měl 95% kódu generovaného Kiro
title: Amazon představil vlastní autonomní vývojové AI prostředí Kiro
thumbnail: https://www.marigold.cz/assets/kiro-dev.png
---

Amazon představil [Kiro](https://kiro.dev), nové vývojové prostředí založené na autonomních AI agentech, které se zaměřuje na řešení problémů současného "vibe coding" - rychlého generování kódu pomocí AI bez důkladného plánování. Nástroj se liší od stávajícího Amazon Q Developer tím, že využívá specifikační vývoj a autonomní agenty pro komplexní úkoly, čímž se dostává do přímé konkurence s populárními řešeními jako Cursor, Windsurf nebo GitHub Copilot.

![Kiro vypadá tak, jak byste čekali](/assets/kiro-dev.png)
_Kiro vypadá tak, jak byste čekali, jako mírná předělávka VS Code s doplněným chat oknem, tedy vlastně podobně, jako konkurenční Cursor a jiní..._

Podle CEO Amazonu Andyho Jassyho má Kiro _"šanci transformovat způsob, jakým vývojáři stavějí software"_. Nástroj vznikl z malého týmu v rámci AWS, ale v neobvyklém kroku pro Amazon má vlastní doménu a branding - název Amazon se neobjevuje v hlavním oznámení a souvislost s technologickým gigantem signalizuje pouze AWS logo v patičce webu. Také přihlášení do produktu jde i přes Google a Github účet, Amazon Developer ID je jen jednou z variant. 

## Odlišnost od Amazon Q Developer

Zatímco Amazon Q Developer se zaměřuje na dokončování kódu a chat-based asistenci, Kiro využívá autonomní AI agenty, které mohou samostatně pomáhat s dokončováním a dokumentováním projektů. Podle zdrojů z Amazonu je "Kiro univerzální agentní IDE pro vývojáře pro práci s jakoukoli platformou podle vlastního výběru", na rozdíl od Q Developer, který je omezenější v podpoře third-party IDE a je omezen na VS Code, JetBrains, Eclipse a Visual Studio.

Kiro bude během preview období k dispozici zdarma všem uživatelům a později se stane součástí Q Developer Pro a Pro+ subscription. Uživatelé budou moci používat oba nástroje současně, což podporuje Q Developer Pro subscription začínající na 19 dolarů měsíčně na uživatele.

## Technologie postavená na Claude

Kiro používá jako výchozí jazykové modely Claude Sonnet 4 od společnosti Anthropic s možností použití Claude Sonnet 3.7 jako další varianty. Prostředí je postaveno na otevřeném zdrojovém kódu Code OSS, což umožňuje vývojářům zachovat stávající nastavení VS Code a používat kompatibilní rozšíření Open VSX.

Nejedná se o klasickou službu AWS - vývojové prostředí nevyžaduje AWS účet a uživatelé se mohou přihlásit prostřednictvím Google, GitHub, Builder ID nebo AWS SSO. Podle Nathana Pecka, AWS vývojového evangelisty pro AI, je cílem poskytnout Kiro "jedinečnou identitu mimo AWS" pro přitažení vývojářů používajících jiné platformy.

## Specifikační vývoj jako základ

Klíčovým dodlišením pro Kiro je model specifikačního vývoje, který vede proces od návrhu k implementaci. Jednoduchý příkaz jako "přidej systém recenzí" spustí řetězec AI asistovaných výstupů, které zahrnují uživatelské příběhy s akceptačními kritérii v EARS notaci (Easy Approach to Requirements Syntax).

Proces začíná automatickým rozbalením požadavků z jediného příkazu - Kiro vygeneruje uživatelské příběhy pro zobrazení, vytváření, filtrování a hodnocení. Každý uživatelský příběh obsahuje akceptační kritéria pokrývající okrajové případy, které vývojáři typicky řeší při implementaci základních funkcí.

Na základě schválených specifikací Kiro analyzuje existující kódovou základnu a vytváří technický návrh zahrnující diagramy datových toků, definice rozhraní, databázová schémata a API koncové body. Technický návrh eliminuje dlouhé diskuse o požadavcích a poskytuje jasnou představu o architektuře systému před implementací.

## Hooks pro automatizaci v pozadí

Hooks fungují jako automatizace spouštěné při událostech jako ukládání nebo vytváření souborů. Tyto nástroje se chovají jako zkušený vývojář zachycující věci, které vývojář přehlédne, nebo dokončují šablonové úkoly na pozadí. Podobnou funkci [představil nedávno také Claude Code](https://www.marigold.cz/vibecoding/claude-code/2025-07-01-claude-code-hooks/).

Hooks dodávají automatickou kontrolu kvality bez zpomalování individuálních vývojářů:
- Při uložení React komponenty automaticky aktualizují testovací soubory
- Při úpravě API koncových bodů obnovují README dokumentaci
- Před potvrzením změn kontrolují kód na úniky přihlašovacích údajů
- Při vytváření nových komponent ověřují dodržování principů jako Single Responsibility Principle

Hooks zajišťují konzistenci napříč celým týmem - každý těží ze stejných kontrol kvality, kódovacích standardů a bezpečnostních validací.

## Multimodální rozhraní a rozšiřitelnost

Kiro podporuje multimodální vstupy, což umožňuje vývojářům zadávat text, diagramy a různé kontextové elementy pro přesnější výsledky. Vývojáři mohou například nahrát obrázek UI designu nebo fotografii architektonické tabule a Kiro ji použije k vedení implementace.

Prostředí podporuje Model Context Protocol (MCP) pro připojování externích nástrojů, agentský chat s kontextovými poskytovateli souborů, URL a dokumentů, a pravidla řízení pro přizpůsobení a omezení chování agentů napříč kódovou základnou.

## Konkurenční prostředí a positioning

Kiro vstupuje do stále více přeplněného ekosystému AI asistovaného vývoje, kde několik prominentních IDE a agentů soutěží o pozornost vývojářů. Představení přichází několik dní poté, co Google oznámil najímání zaměstnanců AI kódovacího startupu Windsurf v rámci technologické licenční dohody za 2,4 miliardy dolarů.

Amazon podle zpráv interně zvažuje formální adopci nástroje Cursor na základě poptávky od svých vývojových týmů. Business Insider poprvé reportoval o Kiro v květnu 2025 na základě uniklých dokumentů, což naznačuje, že projekt byl v přípravě několik měsíců před oficiálním oznámením.

## Demo projekt Spirit of Kiro

Pro demonstraci schopností Kiro v reálném kontextu Amazon vydal kompletní demo projekt nazvaný "Spirit of Kiro" - open-source crafting hru. Projekt slouží jako praktický příklad použití Kiro během celého vývojového cyklu, přičemž více než 95% kódové základny hry bylo vygenerováno promptováním Kiro.

## Ceny a dostupnost

Kiro je během preview období dostupné zdarma všem uživatelům včetně předplatitelů Amazon Q Developer. Po skončení preview bude k dispozici ve třech cenových tarifech:
- Bezplatná verze s 50 agentními interakcemi měsíčně
- Pro tarif za 19 dolarů na uživatele měsíčně s 1000 interakcemi
- Pro+ tarif za 39 dolarů na uživatele měsíčně s 3000 interakcemi

Uživatelé placených plánů budou moci nakupovat další interakce za 0,04 dolaru každou, ale fakturace za překročení musí být explicitně povolena. Agentní interakce zahrnují jakékoli přímé vyvolání Kiro agentů - jako zahájení specifikace, spuštění hook nebo odeslání chat promptu.

## Budoucnost autonomního vývoje

Podle AWS je Kiro součástí širší vize usnadnění tvorby software připraveného pro podnikové prostředí, eliminace technického dluhu a zachování institucionálních znalostí. Název "Kiro" pochází z japonštiny a znamená "křižovatka", což symbolizuje místo, kde se tradiční vývoj setkává s AI akcelerací.

Nástroj reflektuje interní inženýrské praktiky Amazonu a je navržen tak, aby pomohl vývojářům škálovat od malých nápadů k robustním, produkčně připraveným systémům. Počáteční reakce komunity byly smíšené, ale vývojáři ocenili důraz na specifikace, hooks a strukturu ve srovnání s nástroji jako Claude Code a Cursor.

**Shrnutí klíčových funkcí:**
- Autonomní AI agenti pro komplexní vývojové úkoly na rozdíl od simple code completion
- Specifikační vývoj s EARS notací pro jasné definování požadavků
- Event-driven hooks pro automatizaci kontrol kvality a údržby kódu
- Multimodální vstupy včetně diagramů a architektonických schémat
- Model Context Protocol pro rozšíření externími nástroji
- Nezávislost na AWS s vlastním brandingem a přihlašovacími možnostmi