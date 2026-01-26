---
author: Patrick Zandl
categories:
-  AI
-  Anthropic
-  Claude Code
-  Vývojářské nástroje
layout: post
post_excerpt: Claude Code přechází od jednoduchých Todo seznamů k plnohodnotným Tasks s podporou závislostí, persistence a spolupráce napříč sessions a subagenty.
summary_points:
-  Claude Code nahrazuje Todo seznamy novým systémem Tasks s podporou závislostí a koordinace práce
-  Tasks jsou uloženy v souborovém systému a umožňují spolupráci mezi více sessions a subagenty
-  Změna reaguje na rostoucí autonomii modelu Opus 4.5, který lépe udržuje kontext při dlouhodobé práci
-  Tasks lze sdílet pomocí proměnné prostředí CLAUDE_CODE_TASK_LIST_ID
-  Jak přesně Tasks fungují a jak je používat
title: 🗒️ Claude Code přechází od TODO seznamů k plnohodnotným Tasks
---

  
Anthropic přechází u Claude Code od Todo seznamů k plnohodnotným Tasks. Změna přináší podporu závislostí mezi úkoly, persistenci napříč sessions a koordinaci práce při využití více instancí AI agenta současně.

A moje shrnutí a pár postřehů si můžete pustit i na videu:

  

<iframe  width="560"  height="315"  src="https://www.youtube.com/embed/UYiO97d4YvY?si=nFWvVWjTypp8DvD9"  title="YouTube video player"  frameborder="0"  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"  referrerpolicy="strict-origin-when-cross-origin"  allowfullscreen></iframe>

## Důvody změny architektury

  

Původní systém TodoWrite Tool se ukázal jako nedostatečný s nástupem modelu Opus 4.5. Ten disponuje výrazně lepší schopností běžet autonomně po delší dobu a udržovat si přehled o stavu práce. Podle týmu Anthropic model u menších úkolů již nepotřeboval explicitní nástroj pro správu seznamu činností - sám si dokázal pamatovat, co je třeba udělat.

  

Problém nastal u složitějších projektů. Uživatelé začali Claude Code využívat pro dlouhodobější úkoly, které přesahovaly jedno okno kontextu nebo jednu session. U takových projektů existují závislosti mezi úkoly, blokující faktory a potřeba koordinace při práci napříč více instancemi. Sám jsem na to narážel - po zakompresování kontextu se mi stalo, že začal "zapomínat" co je třeba udělat. Přitom bylo vidět, že Opus 4.5 je radikálním zlepšením a ačkoliv likviduje limit tokenů rychleji, než Sonnet, téměř úplně jsem na něj přešel. Ovšem omezení kontextového okna se tady nedá okecat...

  

Thariq Shihipar z Anthropicu označil tento posun jako "unhobbling" - odstranění omezení, která bránila Claudovi využít jeho nové schopnosti. Typický příklad evoluce nástrojového vybavení AI agentů v reakci na rostoucí schopnosti základních modelů.

  

## Architektura systému Tasks

Tasks představují novou abstrakci pro koordinaci mnoha kusů práce napříč projekty. Klíčové vlastnosti:

**Závislosti a metadata**: Claude může vytvářet Tasks s definovanými závislostmi na jiných úkolech. Tato struktura lépe odpovídá reálnému fungování projektů než lineární seznam Todo položek.

**Persistence v souborovém systému**: Tasks jsou uloženy v  `~/.claude/tasks`, což umožňuje více subagentům nebo sessions na nich pracovat současně. Když jedna session aktualizuje Task, změna se propaguje do všech aktivních sessions pracujících se stejným Task List.

**Sdílení napříč instancemi**: Task List lze nastavit pomocí proměnné prostředí:

```bash
CLAUDE_CODE_TASK_LIST_ID=groceries claude

```

Tento mechanismus funguje i pro  `claude -p`  a AgentSDK, což umožňuje konzistentní práci s úkoly napříč různými způsoby spuštění.

## Inspirace z komunity

Anthropic explicitně zmínil inspiraci z komunitních projektů, konkrétně [Beads](https://github.com/steveyegge/beads) od Steva Yeggeho. Beads je framework pro koordinaci AI agentů, který rovněž pracuje s konceptem úkolů a jejich závislostí. Ale nejrůznějších projektů a Skillů na zpracování tasků se v poslední době objevilo mnoho a je logické, že CC takové řešení integroval.

## Tasks do hloubky

Systém Tasks funguje na principu čtyř základních operací, které Claude volá automaticky podle kontextu konverzace. Uživatel tyto operace nemusí explicitně vyžadovat - stačí popsat, co chce udělat, a Claude si potřebné nástroje zavolá sám.

### Vytváření a správa úkolů

Když uživatel zadá komplexní požadavek typu "přidej autentizaci uživatelů s email/heslem a OAuth", Claude automaticky rozloží práci do Tasks s jasně definovanými závislostmi. Například:

-   Úkol 1: Prozkoumat současnou implementaci sessions
-   Úkol 2: Navrhnout JWT implementaci (blokován úkolem 1)
-   Úkol 3: Implementovat JWT autentizaci (blokován úkolem 2)
-   Úkol 4: Aktualizovat chráněné routy (blokován úkolem 3)

Claude při tvorbě Tasks určuje, které úkoly na sobě závisí, a zajišťuje, že práce začne v logickém pořadí. Nemůže začít implementovat autentizační routy, dokud není hotová databázová vrstva.

### Vizuální sledování průběhu

Terminál zobrazuje aktuální stav všech úkolů:

```
Tasks (2 hotovo, 2 probíhá, 16 otevřených) · ctrl+t pro skrytí
■ #3 Dokončení prvního návrhu (staff-writer)
■ #8 Licencování obrázků (photo-editor)
□ #4 Fact-checking (fact-checker) > blokováno #3
□ #5 Věcná redakce (senior-editor) > blokováno #3

```

Symboly ✓ značí dokončené úkoly, ■ probíhající práci a □ čekající úkoly. Symboly ⚠ upozorňují na blokaci - úkol nemůže začít, dokud nejsou splněny jeho závislosti.

### Jak fungují závislosti

Dependency management představuje klíčovou inovaci celého systému. Když Claude definuje, že úkol 3 je blokován úkoly 1 a 2, znamená to: "Úkol 3 nemůže začít, dokud nejsou oba úkoly 1 a 2 označeny jako hotové."

Systém toto vynucuje automaticky. Není možné "omylem" začít s prací, která vyžaduje něco nedokončeného. Jakmile se úkol 3 dokončí, všechny úkoly, které na něm závisely, se automaticky odblokují a stávají se dostupnými pro zpracování.

Tato logika funguje i u paralelních závislostí. Pokud úkol 6 čeká na dokončení úkolů 4 a 5, které sami mohou probíhat současně, úkol 6 se odblokuje až po dokončení obou předpokladů.

### Přiřazování agentům a paralelní práce

Claude může rozdělit práci mezi více subagentů, které běží současně. Každý agent dostane přiřazenou roli - například "backend-dev", "fact-checker" nebo "senior-editor" - a pracuje na úkolech, které mu patří.

Když Claude spawne (vytvoří) nového agenta, předá mu instrukci ve stylu: "Jsi fact-checker. Podívej se na seznam úkolů, najdi ty, které jsou přiřazené tobě, a dokončuj je. Když začneš, označ úkol jako probíhající. Když skončíš, označ ho jako hotový."

Agent pak sám volá nástroje pro zobrazení seznamu Tasks, filtruje si ty své, aktualizuje jejich stav a provádí potřebnou práci. Všechny agenty čtou a zapisují do stejného seznamu úkolů bez konfliktů.

Claude může spustit více agentů najednou - například fact-checkera, editora a test runner současně. Všichni tři pracují paralelně na svých přiřazených úkolech a koordinují se přes sdílený Task List.

### Typy agentů podle účelu

Claude volí typ agenta podle povahy práce:

**General Purpose**  - univerzální agent schopný číst, zapisovat, editovat a spouštět příkazy. Používá se pro většinu implementační práce.

**Bash**  - specializovaný agent s přístupem pouze k terminálu. Rychlý a zaměřený na spouštění příkazů - git operace, testy, build procesy.

**Explore**  - průzkumný agent s read-only přístupem k codebase. Nelze nim nic měnit, ale rychle odpovídá na otázky typu "kde je implementováno X" nebo "jak funguje Y". Claude může specifikovat úroveň důkladnosti - "quick", "medium" nebo "very thorough".

**Plan**  - plánovací agent, také read-only, ale zaměřený na návrh implementační strategie před začátkem práce. Používá se pro rozmyšlení přístupu bez rizika změn v kódu.

Důvod pro různé typy je rychlost a bezpečnost. Spuštění testu přes Bash agenta je rychlejší než přes plnohodnotného General Purpose agenta. Průzkum neznámého kódu přes Explore agenta nemůže nic omylem rozbít.

### Volba modelu pro agenty

U každého spawnovaného agenta lze specifikovat, který model Claude použije:

-   **haiku**  - rychlý a levný, pro jednoduché úkoly
-   **sonnet**  - vyvážený, pro běžnou programátorskou práci
-   **opus**  - plný výkon, pro komplexní rozhodování a víceúrovňové uvažování

Pravidlo: Haiku pro spouštění příkazů a jednoduché průzkumy, Sonnet pro implementaci střední složitosti, Opus pro architektonická rozhodnutí a nuancované problémy. Toto lze kodifikovat v CLAUDE.md souboru nebo ve Skills.

### Persistence napříč sessions

Standardně Tasks přežívají kompaktaci kontextu v rámci jedné konverzace. Když se konverzace prodlužuje a část kontextu je sumarizována, stav úkolů zůstává zachován.

Pro persistenci mezi zcela oddělenými sessions existují dvě možnosti:

**Per terminal session**: Spuštění s explicitní proměnnou prostředí:

```bash
CLAUDE_CODE_TASK_LIST_ID="muj-projekt" claude

```

**Project settings**: Úprava souboru  `.claude/settings.json`:

```json
{
  "env": {
    "CLAUDE_CODE_TASK_LIST_ID": "billion-dollar-saas"
  }
}

```

Druhá varianta zajistí, že Tasks přetrvají mezi kompletně oddělenými konverzacemi. Spustíte novou session a seznam úkolů je stále k dispozici.

Tasks jsou fyzicky uloženy jako JSON soubory v  `~/.claude/tasks/<list-id>/`, což otevírá možnosti pro zálohu, verzování v gitu nebo externí nástroje pro čtení a zápis stavu úkolů.

### Praktické příklady použití

**Jednoduchý lineární projekt**: "Přidej tlačítko pro odhlášení do navigační lišty"

Claude vytvoří tři úkoly:

1.  Přidat tlačítko logout do NavBar komponenty
2.  Implementovat API volání pro logout (blokováno úkolem 1)
3.  Otestovat logout flow (blokováno úkolem 2)

Jasná lineární posloupnost bez možnosti začít testování dříve než je implementace hotová.

**Středně složitý projekt s průzkumem**: "Přepiš autentizační systém ze sessions na JWT"

Claude začne průzkumnými úkoly, které mohou běžet paralelně (prozkoumání současné implementace sessions, research JWT best practices). Teprve po jejich dokončení může začít plánování. Implementační úkoly čekají na dokončení plánu. Testování čeká na dokončení implementace.

**Necode příklad - plánování svatby**: Tasks fungují i mimo programování. Když uživatel řekne "pomoz mi naplánovat svatbu", Claude vytvoří strukturu závislostí: rezervace místa může začít hned, stanovení data čeká na potvrzení místa, pozvánky čekají na datum a seznam hostů, sběr odpovědí čeká na rozeslání pozvánek, finální seating plan čeká na odpovědi a informace o kapacitě stolu od cateringu.

Claude dokáže rozložit složitou práci a udělat ji přehlednou a zvládnutelnou.

## Kdy Tasks používat

Tasks dávají smysl pro:

-   Vícekrokovou práci (3+ kroky)
-   Cokoliv se závislostmi mezi úkoly
-   Práci, která může trvat přes více sessions
-   Komplexní refaktoring nebo nové funkce
-   Delegování práce více agentům

Tasks přeskočit pro:

-   Rychlé jednorázové dotazy
-   Jednoduché úpravy v jednom souboru
-   Cokoliv, co zvládnete na jedno zavolání

## Kontext v architektuře AI agentů

Změna od Todo na Tasks ilustruje širší problematiku kontextového řízení AI agentů. Podle diagramu typů kontextu pro AI agenty existuje šest základních kategorií: instrukce, příklady, znalosti, paměť, nástroje a výsledky nástrojů.

Tasks spadají do kategorie krátkodobé paměti (Short-term Memory), konkrétně do části "State" - stav systému zahrnující kroky uvažování a průběh práce. Zároveň ale Tasks mají vlastnosti dlouhodobé paměti (Long-term Memory) typu procedurální - instrukce přetrvávající napříč sessions.

Právě tato hybridní povaha - kombinace stavového sledování v rámci session a persistence napříč sessions - je klíčová inovace. Tradiční Todo seznamy fungovaly primárně jako krátkodobá paměť vázaná na jednu konverzaci. Tasks přidávají vrstvu persistence a koordinace, která umožňuje práci na rozsáhlejších projektech.

## Důsledky pro praxi

Příchod Tasks představuje posun v tom, jak vývojáři mohou Claude Code používat. Místo nástroje pro rychlé jednorázové úkoly se stává platformou schopnou řídit delší projekty s možností:

-   Rozdělit práci mezi více subagentů, kde každý má jasně definovaný úkol
-   Pokračovat v práci napříč různými sessions bez ztráty kontextu
-   Definovat blokovací závislosti mezi úkoly
-   Sledovat průběh projektu perzistentně v souborovém systému

Ukládání do  `~/.claude/tasks`  otevírá prostor pro další nástroje postavené na této infrastruktuře. Komunita může vytvářet vlastní utility pro vizualizaci, reporting nebo integraci s jinými systémy pro správu projektů.

## Kritické zhodnocení

Tasks představují logickou evoluci, která ale přináší nové otázky. Persistence v souborovém systému je jednoduchým řešením, které má ale své limity - jak systém škáluje při desítkách současně běžících Task Lists? Jak se řeší konflikty při současné editaci stejného úkolu?

Anthropic v oznámení neuvádí detaily o synchronizačních mechanismech nebo řešení konfliktů. Broadcasting změn do všech aktivních sessions zní elegantně, ale v praxi může vést k _race conditions_ nebo nekonzistentnímu stavu při výpadcích konektivity.

Další otázkou je míra autonomie - dokáže Claude efektivně rozhodovat o prioritizaci Tasks a jejich závislostech, nebo bude vyžadovat časté lidské intervence? To se ukáže až při reálném používání na složitějších projektech.

Jedním z praktických omezení je to, že Claude dostává kompletní seznam všech Tasks. U dlouhodobých projektů to znamená nutnost archivovat nebo čistit dokončené úkoly, aby seznam nezahlcoval kontext. Ale také to znamená, že je tu prostor pro zlepšování a rychlou reakci, když se Tasks chytnou - a to Anthropic umí. 

Tasks jsou dostupné okamžitě, vývojáři mohou začít experimentovat ihned. Jde o významný stavební kámen pro umožnění Claudovi pracovat na komplexnějších projektech. 