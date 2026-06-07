---
slug: 'claude-cowork-kompletni-pruvodce'
date: 2026-06-07
title: 'Claude Cowork: Kompletní příručka'
thumbnail: https://www.marigold.cz/assets/claude-cowork-kompletni-pruvodce.png
sw: claude
categories:
- AI
- Claude
- Claude Cowork
post_excerpt: 'Claude Cowork přenáší agentní schopnosti Claude Code do desktopového prostředí Claude.ai, které zvládne každý. Dostanete agenta, který pracuje přímo s vašimi soubory — místo asistenta, kterému v každé konverzaci opakujete totéž.'
summary_points:
  - Cowork přenáší agentní schopnosti Claude Code do desktopového prostředí pro všechny uživatele
  - Klíčový rozdíl oproti Chatu je autonomní práce se soubory ve vaší složce bez opakování kontextu
  - Správná struktura projektu s CLAUDE.md a oddělenými Skills rozhoduje víc než chytrý prompt
  - Cowork je stále research preview s omezeními pro regulované provozy a bez cloudové synchronizace
---

Claude Cowork přenáší schopnosti agentního Claude Code do desktopového prostředí Claude.ai, které zvládne každý. Za těch několik měsíců, co jsou dostupné, jsem prošel všemi stádii: od netečnosti "k čemu by to asi tak bylo", přes čisté nadšení "to je boží", až po nynější rutinní používání "že jsem to předloni nepoužíval? blbost". 

Rozdíl mezi Claude Chat a Cowork? Místo abyste Coworku pokaždé znovu vysvětlovali kontext, dostanete agenta, který pracuje přímo s vašimi soubory. Ve vaší složce. Pojďme si vysvětlit, jak funguje a jak může pomoci i vaší práci!

## Co Cowork je a kde sedí mezi ostatními režimy Claude

Když Anthropic v lednu 2026 spustil Claude Cowork, popsal ho jako „Claude Code pro zbytek vaší práce". Pro běžného uživatele Claude.ai je to trochu kryptická formulace, takže si ji vysvětlíme.

Claude Code umožnil vývojářům říct AI „tady je složka s kódem, udělej to sám". Cowork přináší stejný princip všem ostatním – marketérům, analytikům, manažerům, asistentkám, výzkumníkům. Dostanete agenta, který pracuje s vašimi soubory, místo asistenta, kterému v každé konverzaci opakujete totéž. Kterému pořád dokola přikládáte nějaké soubory. 

Kde tedy Cowork sedí mezi třemi režimy Claude:

**Chat** je konverzace. Vy řídíte každý krok, Claude plní jednu žádost za druhou. Hodí se na jednorázové otázky, brainstorming a situace, kdy chcete nad věcí přemýšlet spolu s Claude. Režim Otázka - Odpověď.

**Cowork** je delegování. Zadáte úkol, Claude si vytvoří plán, postupně ho plní a vy zkontrolujete výsledek. Přistoupí do složky na vašem počítači, čte soubory, vytváří nové, upravuje existující. Pracuje asynchronně – zadáte zadání, odejdete a vrátíte se k hotové práci, která prošla přes několik kroků. Včetně třeba toho, že můžete zadat parametry splnění úkolu. 

**Code** je pro vývojáře, kteří chtějí precizní kontrolu přes terminál či přes IDE.

Čili jednoduše řečeno: **Chat na přemýšlení s Claude, Cowork na delegování práce Claudovi, Code na jeho kódování.**

Ve skutečnosti je tedy zvládnutí Claude Cowork hranice mezi povídání si s AI a mezi tím, práci na něj přehodit. 

### Jak to technicky funguje

Cowork běží v izolovaném virtuálním stroji (VM) přímo na vašem počítači. To má dvě praktické konsekvence. Zaprvé bezpečnost: Claude vidí jen složky, ke kterým mu dáte přístup, zbytek systému zůstává mimo dosah. Zadruhé lokálnost: vaše soubory neopouštějí počítač a historie Cowork se ukládá lokálně, ne na serverech Anthropic.

U složitějších úkolů Cowork nasazuje paralelní sub-agenty. Každý pracuje na své části ve vlastním kontextovém okně, takže zpracování padesáti souborů může proběhnout výrazně rychleji než sekvenčně.

### Kde běží a kolik stojí

Cowork je dostupný v desktopové aplikaci Claude pro macOS i Windows. Na webu ani přímo v mobilu neběží, ale z telefonu můžete desktopovou relaci ovládat vzdáleně přes funkci Dispatch.

Cenové tarify? Za 20 USD měsíčně Cowork obsahuje, ale s nízkými limity – agentní úlohy spotřebovávají mnohem víc kapacity než běžný chat, takže při intenzivní práci narazíte dost rychle. Za 20 USD je Cowork spíš demo. Max 5× za 100 USD a Max 20× za 200 USD nabízejí pětinásobnou, respektive dvacetinásobnou kapacitu. Team a Enterprise přidávají admin kontrolu pro firmy. Všechny plány mají identické funkce Cowork a liší se výhradně v tom, kolik práce stihnete, než narazíte na limit, který se resetuje každých pět hodin. 

Na Team nebo Enterprise plánu může vlastník distribuovat pluginy napříč organizací přes plugin marketplaces. Pluginy jsou balíky, které sdružují skills, slash commands a konektory a mění Claude z obecného asistenta na specialistu pro konkrétní funkci. Samotné Skills jdou sdílet taky – na Team a Enterprise plánech se v adresáři objevuje záložka „Your organization", která ukazuje skills sdílené napříč organizací, jak ty centrálně poskytnuté vlastníkem, tak ty, které kolegové sdíleli org-wide. Admin navíc dostává org-specifické marketplaces, privátní GitHub repozitáře jako zdroje pluginů, provisioning po uživatelích a auto-install. 

Pro rozhodování platí jednoduchá matematika: pokud vám Cowork ušetří pět hodin měsíčně a vaše hodinová sazba je 1 000 Kč, Max plán se vyplatí. Začněte ale na Pro a ověřte si přínos na reálných úkolech, než budete platit víc.

## Co Cowork umí a Chat ne

### Pracuje s vašimi soubory přímo

V Chatu přiložíte soubor ručně do každé konverzace. V Coworku ukážete na složku jednou a Claude do ní pak autonomně přistupuje, když má dojem, že je potřeba. Zajímavé je, že Cowork čte jak názvy souborů, tak jejich obsah. Pozná, že obrázek pojmenovaný IMG_4521.png je ve skutečnosti faktura ze Stripe, a zařadí ho správně, aniž byste mu to říkali.

Typický první experiment, na kterém uvidíte, jak Cowork přemýšlí: úklid složky se staženými soubory. Cowork umí najít duplicity podle obsahu, hromadně přejmenovat soubory podle konvence, archivovat staré soubory s logem o tom, co kam přesunul, sloučit roztroušené CSV do jednoho Excelu se správnými hlavičkami nebo vyčistit rozbitý datový export.

**Příklad z marketingu.** Složka `projekty/klient-ABC/` obsahuje briefy, výstupy z kampaní a zápisy ze schůzek. Řeknete „připrav měsíční report pro klienta ABC". Cowork si sám najde relevantní soubory, propojí data a vytvoří draft reportu, aniž byste mu cokoli přikládali.

![Jak zadávat úkol Claude Coworku?](https://www.marigold.cz/assets/claude-cowork-schema.png)

### Pamatuje si, jak chcete pracovat

Tady je potřeba uvést na pravou míru rozšířený mýtus. Po internetu koluje tvrzení, že stačí do složky hodit pár .md souborů a Claude je „čte před každým promptem". Mechanismus existuje, ale funguje konkrétněji, a u technicky přesného článku se hodí ho popsat správně.

Cowork dědí systém automatické paměti a načítání souboru `CLAUDE.md` z Claude Code jako instrukční bázi projektu, kterou si načítá vždy na začátku sezení. To, co Anthropic v rozhraní nazývá „folder instructions" nebo „project instructions", je pod kapotou právě tento soubor. Claude ho navíc může během práce sám aktualizovat.

Kontext se přitom skládá do vrstev, které se čtou v určitém pořadí: globální personalizace platná napříč Chatem, Code i Coworkem, globální instrukce Cowork, instrukce projektu a teprve pak konkrétní úkol. Specifičtější vrstva přebíjí obecnější – pokud máte globálně „piš formálně" a v projektu „piš neformálně", vyhraje projektová instrukce. Vrstvu globálních instrukcí Cowork nastavíte v Settings → Cowork. Je to trvalý prompt platný napříč všemi projekty – patří do něj věci, které platí vždy (jazyk výstupů, kam ukládat, kdy se ptát přes AskUserQuestion), zatímco specifika firmy patří do `CLAUDE.md` konkrétního projektu.

Automaticky se načítá `CLAUDE.md` a vrstva folder instrukcí. Když si vedle toho založíte třeba `brand_voice.md`, Claude ho přečte, když na něj během práce narazí nebo když ho na něj odkážete přímo v `CLAUDE.md`. Proto se vyplatí mít v `CLAUDE.md` explicitní řádek typu „před generováním obsahu přečti brand_voice.md".

Praktická sada souborů pro každý projekt: do `CLAUDE.md` patří stručná identita firmy, základní pravidla (formát data, měna, jazyk, konvence pojmenování souborů) a odkazy na další soubory. Do `about_company.md` podrobný popis firmy, produktů a zákaznických segmentů. Do `brand_voice.md` tón komunikace s ukázkami reálných textů a se slovy, kterým se vyhýbáte. Do `working_rules.md` pravidla pro výstupy, formáty a složkovou strukturu. A jak se o nich Cowork dozví? Inu, právě tak, že do CLAUDE.md přidáte větu: „Před generováním jakéhokoli textového obsahu přečti a dodržuj references/brand_voice.md" - atd. 

Soubory nemusíte psát od nuly. V úkolu řekněte: *„Polož mi sérii otázek o mé firmě, mém komunikačním stylu a pracovních preferencích a z mých odpovědí sestav soubory CLAUDE.md, brand_voice.md a working_rules.md."* Výsledek pak zkontrolujte a doplňte konkrétní příklady, protože Claude má tendenci formulovat věci obecněji, než je užitečné. A samozřejmě, po určité době nechte Clauda váš styl aktualizovat podle toho, jak se vyvíjí!

Jeden návyk se vyplatí osvojit hned: držte tyhle soubory štíhlé a informačně husté. Cowork je čte před každým úkolem, takže nabobtnalý `CLAUDE.md` nebo firemní profil na dvacet stran ukrojí z kontextového okna dřív, než se vůbec pustí do práce. U příliš dlouhých souborů má navíc Claude tendenci přestat číst pečlivě a jen je volně sumarizovat. Pravidlo: do paměťových souborů patří vzorce a pravidla, ne syrové přepisy a historie. Když soubor narůstá, nechte si ho zhustit.

#### Projekty: trvalý workspace, ne jen složka

Od jarní aktualizace 2026 nemusíte projekt držet jen jako složku s `CLAUDE.md`. Cowork má vlastní Projekty přímo v aplikaci – pojmenovaný workspace, který spojuje tři věci: vlastní složku, vlastní instrukce a paměť omezenou na daný projekt (scoped memory). Řeknete „podívej se na minulý týdenní report" a Claude ví, který to byl, aniž byste ho přikládali – ale jen uvnitř tohoto projektu, do zbytku vaší práce to neprosakuje. Tahle izolace paměti je záměrná. Projekt založíte třemi způsoby: od nuly, importem staršího projektu z Claude.ai, nebo obalením složky, kterou už máte.

Jak to souvisí s `CLAUDE.md` z předchozí kapitoly: instrukce projektu, které nastavíte v rozhraní Projektů, jsou tatáž vrstva folder instrukcí. Projekty k tomu jen přidávají perzistentní paměť a plánování a dávají tomu rozhraní.

### Plánuje automatické úkoly

Příkazem `/schedule` nastavíte, co má Cowork dělat pravidelně – každé ráno, každý týden, ve zvolených dnech. Tahle funkce v klasickém Chatu neexistuje.

**Příklad z HR analytiky.** „Každé pondělí ráno vezmi exporty z ATS systému v téhle složce a připrav přehled nových kandidátů za uplynulý týden ve formátu XYZ." Stačí nastavit jednou. Háček: počítač musí být zapnutý a aplikace Claude Desktop otevřená, jinak úloha čeká. Jistě, v Claude Code můžete mít úlohy i v cloudu, ale v Coworku je to závislé na virtuálním prostředí a na datech, které má jen váš lokální počítač, takže zatím prostě počítejte s tím, že pro automaticky plánované úkoly musí váš počítač běžet. Cowork na to má i přepínač - zabránit jeho usnutí...

### Rozkládá složité úkoly sám

Když v Chatu zadáte složitý úkol, Claude postupuje krok po kroku a čeká na vaše potvrzení. Cowork si vytvoří interní plán, plní ho a ptá se jen tam, kde to opravdu potřebuje. Paralelní zpracování přitom šetří čas: v testech Karoliny Zieminski zpracování deseti souborů paralelně místo jednoho po druhém zkrátilo třicetiminutové čekání na zhruba čtyři minuty. Můžete o to požádat i explicitně: *„Použij sub-agenty a zpracuj těchto 50 přepisů paralelně. Vytáhni témata a pak je shrň."*

## Jak správně delegovat

Skoro nikdo nedeleguje dobře napoprvé. Buď dáme instrukci natolik vágní, že by zmátla i baristu, nebo v panice předáme přístup k celé složce Dokumenty.

Pokud mohu doporučit, dávejte Coworku odpovědi na tři otázky, na které si odpovíte před každým úkolem: 
1. Jak má vypadat „hotovo"? 
2. Jaký kontext Claude potřebuje? 
3. Jaká omezení nedokáže Claude uhodnout?

Z toho plyne struktura promptu o čtyřech částech – cílový stav, kontext, omezení a výstup. Místo „ukliď mi složku Downloads" tedy:

```
Cílový stav: Složka ~/Downloads obsahuje jen soubory za posledních 7 dní.
Zbytek je roztříděný do ~/Sorted/fotky, ~/Sorted/dokumenty a ~/Sorted/ostatni.

Kontext:
V Downloads je teď asi 187 souborů, sahají měsíce zpátky.
Převažují .jpg, .pdf a .zip.

Omezení:
Nic nemaž, soubory jen přesouvej.

Výstup: Až budeš hotový, vytvoř krátký what-moved.md s přehledem, kolik souborů šlo kam.
```

K tomu několik tipů, které stojí za osvojení. Vždy si vyžádejte change log (`what-changed.md`), ať můžete zpětně zkontrolovat každé rozhodnutí Claude. První běh otestujte na neostrých datech, ať vidíte, jak Claude vaše instrukce interpretuje, bez rizika. Při syntéze přes více souborů žádejte trasování zdrojů, tedy ať Claude u každého tvrzení uvede název souboru, ze kterého čerpal. A sledujte spotřebu v Settings > Usage, ať nenarazíte na limit uprostřed úkolu.

Osvědčená struktura pracovní složky vypadá u Zieminski takto: `thoughts/` pro neuspořádané poznámky, `ideas/` pro nápady k rozpracování, `todo/` pro soubory ke zpracování, `outputs/` pro nové výstupy Claude, `done/` pro hotové úkoly a `references/` pro read-only kontext, kam patří právě `CLAUDE.md`, `branding.md` nebo `change-log.md`. Ale nemusíte si ji hned zakládat, prostě až budete mít dojem, že je třeba uložit soubory ke zpracování, tak Coworku řeknete, že je má ukládat do `todo/`. 

## Praktické příklady podle profese

### Marketing a komunikace

| Úkol | Chat | Cowork |
|------|------|--------|
| Měsíční report | Přiložíte data ručně, požádáte, zkopírujete výstup | Claude vezme soubory ze složky, propojí s online daty, uloží draft |
| Repurposing obsahu | Jeden blogpost = jeden výstup, pak znovu | Vzorec definujete jednou (blog → LinkedIn + newsletter + příspěvek na X), Skill ho aplikuje na každý nový článek |
| Analýza konkurence | Kopírujete URL po jedné | Claude systematicky projde seznam a uloží strukturovaný výstup do tabulky |

Konkrétní prompt na vyzkoušení: *„Vezmi tento text a najdi 3 nejsilnější samostatné myšlenky. Pro každou vytvoř scénář (max 60 sekund, konverzační tón, optimalizováno pro LinkedIn video). Výstup ulož jako video-scenare.md."* A nezdá se vám výsledek? Řekněte Coworku, co má zlepšit a opravit. 

### Výzkum a analytika

Cowork vyniká na opakujících se úkolech, kde tvar práce zůstává stejný a mění se obsah. Popis vzorce jednou a Cowork ho aplikuje na padesát souborů stejně snadno jako na jeden.

Máte složku s třiceti zákaznickými průzkumy v PDF. V Chatu byste je procházeli jeden po druhém. V Coworku řeknete: *„Pro každý dokument ve složce vytvoř syntézu podle šablony X a ulož výsledky do synthesis-report.docx: exec summary na jednu stranu, klíčová témata s přímými citacemi a názvy zdrojových souborů, rozpory mezi zdroji a nezodpovězené otázky. Cílová skupina: vedení. Tón: formální."*

### Administrativa a organizace

Malé firmy bez IT oddělení (cestovní ruch, poradenství, realitní kanceláře) nasazují Cowork na propojení se sdílenou složkou a generování odpovědí na opakované dotazy podle šablon. Stačí ukázat na správnou složku a jednou popsat vzorec.

Příklad na triáž e-mailů: *„Projdi e-maily za posledních 7 dní. Roztřiď je na urgentní, vyžadující odpověď a pro informaci. Vytvoř triage.md s přehledem každého e-mailu (odesílatel, předmět, kategorie, navržená akce). U zpráv, které potřebují jen potvrzení, připrav drafty odpovědí – ulož jako koncepty, neodesílej."*

### Finance a reporting

Zpracování dokladů je vděčný scénář: *„Načti účtenky ve složce [název]. Vytvoř expense-tracker.xlsx pro sledování rozpočtu: datum, dodavatel, kategorie, částka. Přidej vzorce pro součty podle kategorií a podmíněné formátování pro položky nad [částka]."*

## Skills, Slash Commands a vestavěné nástroje

Skill je opakovatelný workflow zabalený do jednoho příkazu. Když workflow jednou funguje, řekněte Coworku „zabal, co jsme právě udělali, do Skillu" a příště ho zavoláte jediným promptem. Nejsnáz se Skills tvoří přes vestavěný Skill Creator (spouští se automaticky), který se vás vyptá na záměr a vygeneruje správně strukturovaný soubor.

Důležité ponaučení: nevytvářejte jeden obří Skill na všechno. Výsledky jednoho velkého Skillu byly výrazně horší. Lepší je chunkovat workflow do menších specializovaných bloků. Například používejte oddělené Skills na psaní – jeden pro celkový hlas, jeden pro korporátní texty, jeden pro newsletter – takže Claude nikdy nesplete, pro koho píše.

Skills se navíc načítají přes progressive disclosure: nejdřív jen metadata (kolem 100 tokenů), plné instrukce teprve když jsou potřeba. Patnáct zapnutých Skills proto nezahltí průběžně kontextové okno, protože Claude si bere jen to relevantní. Skills sdílejí kontextový rozpočet kolem 2 % kontextového okna, takže pokud Claude začne zapomínat, že nějaký Skill existuje, je to nejspíš tím.

Cowork přichází s vestavěnými Skills pro pdf, docx, pptx, xlsx a canvas-design. Načítají se automaticky, když daný formát vyžádáte, a fungují bez nastavování. A hromadu si jich také můžete doinstalovat, například pro finanční či právní analýzu. 

Vedle Skills, které pracují na pozadí, jsou tu Slash Commands jako ruční zkratky – `/summarize` zhustí dlouhé vlákno, `/translate` přeloží, `/rewrite` přepíše odstavec do jiného tónu. Drží vás v jednom toku práce bez přepínání nástrojů.

## Jak začít: první hodina s Cowork

1. **Vytvořte složku pro projekt.** Ne Dokumenty ani Plochu, ale dedikovanou složku. Přístup udělte jen k ní – to je vaše bezpečnostní hranice.
2. Popište, jak chcete pracovat: jazyk výstupů, formáty dokumentů, co může Claude dělat samostatně a kde má čekat na potvrzení. Nechte ho tak vytvořit `CLAUDE.md`. Nebo tak začněte pracovat a později si nechte `CLAUDE.md` vygenerovat. On si Claude o vás a vašich pracovních postupech už dost pamatuje, pokud ho používáte často. 
3. **Začněte jednodušším úkolem.** Neskákejte rovnou na plně automatizovaný workflow. Projděte úkol s Coworkem jednou ručně, ať vidíte, jak přemýšlí a kde potřebuje korekci.
4. **Vytvořte první Skill.** Když workflow funguje, zabalte ho do Skillu. Příště stačí jeden prompt.

## Kdy Cowork nepoužít a na co si dát pozor

Cowork spaluje tokeny rychleji než Chat, protože platíte za plánování na pozadí a autonomní kroky. Pravidlo: jednorázová otázka nebo brainstorming patří do Chatu, opakovaná práce s vašimi soubory do Coworku, psaní kódu do Code.

Spotřebu zbytečně zvyšují tři chyby. První je příliš mnoho aktivních konektorů. Každý zabírá místo v kontextu, i když ho úkol nevyžaduje. Druhá je míchání témat v jednom okně, protože Claude pak načítá celou historii konverzace, i když ji nepotřebuje pro splnění úkolu. Po 30 až 45 minutách nebo při změně tématu otevřete nový úkol. Třetím problémem je konverzační zpracování dat: sto faktur nenechte číst jednu po druhé, ale požádejte o Skill, který je zpracuje hromadně.

Pak jsou tu limity, které hype články obvykle vynechávají. Cowork je stále research preview, takže se funkce mění bez varování. Pro firmy je podstatné, že aktivita v Coworku se nezachycuje v Audit Logs, Compliance API ani Data Exports, a že Anthropic Cowork nedoporučuje pro HIPAA, FedRAMP a regulované provozy. Lokální ukládání historie je výhodou pro soukromí, zároveň znamená, že neexistuje cloudová záloha a relace zatím nejde sdílet s kolegou. Dokonce ani nejde snadno Cowork konverzace přenést z jednoho počítače na druhý, musíte kopírovat selektivně složky bez jakékoliv podpory od Coworku (migrace z Mac na nový Mac ovšem přenese vše).

Bezpečnostní pozornost si zaslouží externí Skills stahované z GitHubu. Pokud je v .md souboru skrytá instrukce mimo deklarovaný účel (prompt injection), Claude ji může vykonat na vašem stroji s oprávněními, která jste mu dali. Postup *„vlož Skill do chatu a zeptej se, jestli je bezpečný"* nestačí, protože sofistikovaný útok Claude rozpoznat nemusí. Každý externí Skill si přečtěte celý ručně a hledejte instrukce, které nesouvisejí s jeho účelem – přístup k jiným složkám, odesílání dat, mazání souborů.

A počítejte s tím, že Cowork je preview i ve spolehlivosti. Uživatelé reportují občasné problémy s otevíráním souborů a situace, kdy Cowork místo akce navrhne „použijte terminál". V takovém případě je Claude Code přesnější nástroj.

Jakmile také začnete Cowork více používat, začne být poněkud nepřehledný. V historii konverzací se začnou hromadit automaticky pojmenované konverzace a vyhledávání ne vždy pomůže. Zaveďte si strategii přidávání emoji na začátek názvu konverzace a konverzace přejmenovávejte podle skutečného tématu, například přidávejte jméno firmy či projektu, jíž se týká. 

## Synchronizace dat

Už jsme si řekli, že data v Coworku běží lokálně, takže rozpracované konverzace se nesynchronizují přes cloud, ačkoliv na jiném počítači používáte stejný účet. Řešení tu pár je: můžete používat sdílený disk typu Google Drive nebo synchronizaci přes Github, která je elegantní, pro textové soubory kvalitní. Ani pak ovšem nesynchronizujete konverzace, pouze vstupní a výsledné soubory, můžete si tak ale vytvořit pracovní postupy, se kterými vás to nebude zatěžovat. 

## Shrnutí

Cowork dává smysl ve chvíli, kdy přestanete přemýšlet o Claude jako o chatbotovi a začnete mu zadávat práci. Architektura přitom rozhoduje víc než chytrý prompt: solidní struktura projektu, smysluplný `CLAUDE.md` a oddělené Skills udělají pro kvalitu výstupu víc než sebelepší jednorázová formulace.

Praktický první krok: nainstalujte Claude Desktop, vytvořte si dedikovanou složku a pusťte Cowork na jeden reálný úkol. Úklid složky se staženými soubory nebo přehled z hrstky faktur bohatě stačí, abyste viděli, co nástroj umí.

---

### Kam dál

- [Get started with Cowork](https://support.claude.com/en/articles/13345190-get-started-with-cowork) – oficiální průvodce Anthropic
- [Schedule recurring tasks in Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork) – plánované úlohy
- [Assign tasks to Claude from anywhere](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork) – Dispatch
- [Cowork: Claude Code power for knowledge work](https://claude.com/product/cowork) – produktová stránka
- [Karolina Zieminski: 50+ Tested Tips on Plugins, Skills, Sub-Agents, and Memory](https://karozieminski.substack.com/p/claude-cowork-guide-plugins-memory-sub-agents-tips) – nejkompletnější komunitní průvodce

*Zdroje: oficiální dokumentace Anthropic, produktová stránka Cowork a komunitní testy. Data ověřena červen 2026.*
