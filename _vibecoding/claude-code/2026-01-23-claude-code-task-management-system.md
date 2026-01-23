---
author: Patrick Zandl
categories:
- AI
- Anthropic
- Claude Code
- Vývojářské nástroje
layout: post
post_excerpt: Claude Code přechází od jednoduchých Todo seznamů k plnohodnotným Tasks s podporou závislostí, persistence a spolupráce napříč sessions a subagenty. 
summary_points:
- Claude Code nahrazuje Todo seznamy novým systémem Tasks s podporou závislostí a koordinace práce
- Tasks jsou uloženy v souborovém systému a umožňují spolupráci mezi více sessions a subagenty
- Změna reaguje na rostoucí autonomii modelu Opus 4.5, který lépe udržuje kontext při dlouhodobé práci
- Tasks lze sdílet pomocí proměnné prostředí CLAUDE_CODE_TASK_LIST_ID
- Anthropic označuje změnu jako "odhobblování" Clauda pro využití nových schopností modelů
- Inspirace přišla z komunitních projektů včetně Beads od Steva Yeggeho
title: Claude Code přechází od Todo seznamů k plnohodnotným Tasks
---

Anthropic přechází u Claude Code od Todo seznamů k plnohodnotným Tasks. Změna přináší podporu závislostí mezi úkoly, persistenci napříč sessions a koordinaci práce při využití více instancí AI agenta současně.

A moje shrnutí a pár postřehů si můžete pustit i na videu:

<iframe width="560" height="315" src="https://www.youtube.com/embed/UYiO97d4YvY?si=nFWvVWjTypp8DvD9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Důvody změny architektury

Původní systém TodoWrite Tool se ukázal jako nedostatečný s nástupem modelu Opus 4.5. Ten disponuje výrazně lepší schopností běžet autonomně po delší dobu a udržovat si přehled o stavu práce. Podle týmu Anthropic model u menších úkolů již nepotřeboval explicitní nástroj pro správu seznamu činností - sám si dokázal pamatovat, co je třeba udělat.

Problém nastal u složitějších projektů. Uživatelé začali Claude Code využívat pro dlouhodobější úkoly, které přesahovaly jedno okno kontextu nebo jednu session. U takových projektů existují závislosti mezi úkoly, blokující faktory a potřeba koordinace při práci napříč více instancemi. Sám jsem na to narážel - po zakompresování kontextu se mi stalo, že začal "zapomínat" co je třeba udělat. Přitom bylo vidět, že Opus 4.5 je radikálním zlepšením a ačkoliv likviduje limit tokenů rychleji, než Sonnet, téměř úplně jsem na něj přešel. Ovšem omezení kontextového okna se tady nedá okecat...

Thariq Shihipar z Anthropicu označil tento posun jako "unhobbling" - odstranění omezení, která bránila Claudovi využít jeho nové schopnosti. Typický příklad evoluce nástrojového vybavení AI agentů v reakci na rostoucí schopnosti základních modelů.

## Architektura systému Tasks

Nový Task Management System je dostupný ve verzi Claude Code 2.1.16 a vyšší (v době psaní článku byla nejvyšší verze 2.1.17 s minoritní aktualizací), čili aktualizujte. 

Tasks představují novou abstrakci pro koordinaci mnoha kusů práce napříč projekty. Klíčové vlastnosti:

**Závislosti a metadata**: Claude může vytvářet Tasks s definovanými závislostmi na jiných úkolech. Tato struktura lépe odpovídá reálnému fungování projektů než lineární seznam Todo položek.

**Persistence v souborovém systému**: Tasks jsou uloženy v `~/.claude/tasks`, což umožňuje více subagentům nebo sessions na nich pracovat současně. Když jedna session aktualizuje Task, změna se propaguje do všech aktivních sessions pracujících se stejným Task List.

**Sdílení napříč instancemi**: Task List lze nastavit pomocí proměnné prostředí:

```bash
CLAUDE_CODE_TASK_LIST_ID=groceries claude
```

Tento mechanismus funguje i pro `claude -p` a AgentSDK, což umožňuje konzistentní práci s úkoly napříč různými způsoby spuštění.

## Inspirace z komunity

Anthropic explicitně zmínil inspiraci z komunitních projektů, konkrétně [Beads](https://github.com/yegge-labs/beads) od Steva Yeggeho. Beads je framework pro koordinaci AI agentů, který rovněž pracuje s konceptem úkolů a jejich závislostí. Ale nejrůznějších projektů a Skillů na zpracování tasků se v poslední době objevilo mnoho a je logické, že CC takové řešení integroval. 

## Kontext v architektuře AI agentů

Změna od Todo na Tasks ilustruje širší problematiku kontextového řízení AI agentů. Podle diagramu typů kontextu pro AI agenty existuje šest základních kategorií: instrukce, příklady, znalosti, paměť, nástroje a výsledky nástrojů.

Tasks spadají do kategorie krátkodobé paměti (Short-term Memory), konkrétně do části "State" - stav systému zahrnující kroky uvažování a průběh práce. Zároveň ale Tasks mají vlastnosti dlouhodobé paměti (Long-term Memory) typu procedurální - instrukce přetrvávající napříč sessions.

Právě tato hybridní povaha - kombinace stavového sledování v rámci session a persistence napříč sessions - je klíčová inovace. Tradiční Todo seznamy fungovaly primárně jako krátkodobá paměť vázaná na jednu konverzaci. Tasks přidávají vrstvu persistence a koordinace, která umožňuje práci na rozsáhlejších projektech.

## Důsledky pro praxi

Příchod Tasks představuje posun v tom, jak vývojáři mohou Claude Code používat. Místo nástroje pro rychlé jednorázové úkoly se stává platformou schopnou řídit delší projekty s možností:

- Rozdělit práci mezi více subagentů, kde každý má jasně definovaný úkol
- Pokračovat v práci napříč různými sessions bez ztráty kontextu
- Definovat blokovací závislosti mezi úkoly
- Sledovat průběh projektu perzistentně v souborovém systému

Ukládání do `~/.claude/tasks` otevírá prostor pro další nástroje postavené na této infrastruktuře. Komunita může vytvářet vlastní utility pro vizualizaci, reporting nebo integraci s jinými systémy pro správu projektů.

## Kritické zhodnocení

Tasks představují logickou evoluci, která ale přináší nové otázky. Persistence v souborovém systému je jednoduchým řešením, které má ale své limity - jak systém škáluje při desítkách současně běžících Task Lists? Jak se řeší konflikty při současné editaci stejného úkolu?

Anthropic v oznámení neuvádí detaily o synchronizačních mechanismech nebo řešení konfliktů. Broadcasting změn do všech aktivních sessions zní elegantně, ale v praxi může vést k _race conditions_ nebo nekonzistentnímu stavu při výpadcích konektivity.

Další otázkou je míra autonomie - dokáže Claude efektivně rozhodovat o prioritizaci Tasks a jejich závislostech, nebo bude vyžadovat časté lidské intervence? To se ukáže až při reálném používání na složitějších projektech.

Tasks jsou dostupné okamžitě, vývojáři mohou začít experimentovat ihned. Jde o významný stavební kámen pro umožnění Claudovi pracovat na komplexnějších projektech, jehož reálná hodnota se projeví v následujících týdnech při adopci komunitou.