---
slug: “karpathy-llm-knowledgebase”
author: Patrick Zandl
categories:
- AI
- LLM
- produktivita
- znalostní management
layout: post
post_excerpt: “Andrej Karpathy zveřejnil návod jak používat AI jinak – ne na psaní kódu, ale na budování osobní znalostní báze. 82 000 záložek za čtyři dny říká, že lidi tohle chtějí. Tady je překlad, kritický rozbor a praktický návod jak začít.”
summary_points:
- “Karpathy přestal používat AI hlavně na kód a místo toho ho používá na kompilaci osobní wiki z markdown souborů”
- “LLM průběžně indexuje zdroje, píše články, propojuje koncepty a odpovídá na dotazy – člověk jen přináší zdroje a otázky”
- “Systém běží na třech vrstvách: raw (zdroje), wiki (LLM-generovaná), schema (CLAUDE.md s pravidly chování)”
- “82 000 záložek za čtyři dny ukazuje, že lidi tuhle myšlenku chtějí – ale zatím nevědí jak začít”
- “Karpathy následně zveřejnil idea file — nový formát sdílení, kde nesdílíte kód, ale myšlenku, a agent si implementaci postaví sám”
- “Komunita už za den vytvořila desítky implementací — od Go binárky přes Claude Code skill po voice-first verzi přes Telegram”
title: “Karpathy přišel na to, jak používat AI jinak. A má pravdu.”
---

Andrej Karpathy — člověk, který stál u zrodu GPT — zveřejnil minulý týden Twitter příspěvek, který si za čtyři dny záložkovalo přes 82 000 lidí. Třináct milionů zobrazení. To není virální hype. To je něco, co lidi zasáhlo, protože to pojmenovává něco, co sami cítí, ale neuměli to říct. Pointa? Jak používat LLM k budování znalostní databáze?

## Co Karpathy říká

Stručně: přestal používat AI hlavně na kód. Místo toho ho používá na budování osobní znalostní báze. Pojdme to okopirovat, protože je to dobré. a rozvest, protože je kam...

Konkrétní postup:

1. Sbírá zdroje — články, papery, repozitáře, datasety, obrázky — do adresáře `raw/`
1. LLM z toho průběžně „kompiluje” wiki: kolekci `.md` souborů s články, shrnutími a zpětnými odkazy
1. Wiki uživatel prohlíží v Obsidianu
1. Když má otázku, ptá se LLM agenta — ten prohledá wiki a odpovídá
1. Výstupy (markdown, slideshowy, grafy) se archivují zpět do wiki — každý dotaz znalostní bázi rozšiřuje

Jeho wiki na jedno téma má teď ~100 článků a ~400 000 slov. Bez RAG, bez vektorové databáze. Jen flat adresář `.md` souborů v Obsidianu. Tady se zadrhavam já, mám článku cca 50000, zejména k 3GPP normám.

## Proč to rezonuje

Karpathy pojmenoval problém, který má každý, kdo se seriózně zabývá nějakým tématem:

**Informací je příliš mnoho. Čas na jejich zpracování příliš málo.**

Klasické řešení bylo: záložky, Notion, Roam, Obsidian, mind mapy. Ale to všechno vyžaduje, abyste sami psali, organizovali, propojovali. To je dost práce.

Karpathyho pohled je jednoduchý: LLM tu práci udělá za vás. Vy přinášíte zdroje a otázky. LLM kompiluje, organizuje, propojuje, píše.

Posun je zásadní: z AI jako nástroje na psaní nebo kódování na **AI jako osobního knihovníka a analytika**.

## Co říká komunita

Na příspěvek reagovalo přes 2 000 lidí. Zajímavé je, co říkají:

**„To dělám taky”** — překvapivě velká část odpovědí. Jeden člověk krmí přepisy svého YouTube kanálu do podobného systému a dotazuje se před každým novým videem, aby se neopakoval. Jiný to aplikuje na product feedback od zákazníků. Lex Fridman potvrdil, že používá podobný setup a nechává si generovat interaktivní HTML vizualizace, které si pak bere na dlouhé běhy s voice módem.

**„Není to jako NotebookLM?”** — několik lidí srovnává s Google NotebookLM nebo Claude Projects. Rozdíl je klíčový: Karpathyho systém je váš, offline, rozšiřitelný a LLM aktivně strukturu udržuje a rozvíjí, ne jen odpovídá na dotazy.

**Technická kritika** — část komunity upozorňuje na reálné problémy: markdown je čitelný pro lidi, ale ne vždy pro agenty. Jakmile se výstupy zapisují zpět do wiki, chyby se mohou kumulovat. Při větším objemu dat flat soubory přestanou stačit.

Karpathy to sám přiznává: „Myslím, že je tu prostor pro úžasný nový produkt místo hacky sbírky skriptů.”

## Idea file — nový formát sdílení

Dva dny po původním příspěvku Karpathy zveřejnil [podrobný gist na GitHubu](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), který celý koncept rozšiřuje. Ale zajímavější než obsah je formát. Karpathy to nazývá „idea file” — dokument navržený tak, abyste ho zkopírovali a vložili do svého LLM agenta. Agent si z toho postaví konkrétní implementaci sám.

To je meta-insight: **v éře agentů nesdílíte kód, sdílíte myšlenku.** Kód si každý vygeneruje sám, přizpůsobený vlastním potřebám. Za den po zveřejnění se v komentářích objevilo přes deset hotových implementací — od Go binárky přes Claude Code skill po voice-first verzi přes Telegram.

### Co gist upřesňuje

Gist formalizuje tři vrstvy, které tweet jen naznačoval:

1. **Raw** — zdrojové dokumenty. Immutable — LLM z nich čte, ale nikdy je nemodifikuje. Tohle je váš zdroj pravdy.
1. **Wiki** — LLM-generované markdown soubory. Shrnutí, entity, koncepty, srovnání. LLM tuhle vrstvu vlastní celou — vytváří stránky, aktualizuje je, udržuje křížové odkazy.
1. **Schema** — konfigurační soubor (`CLAUDE.md` pro Claude Code, `AGENTS.md` pro Codex), který říká LLM jak se chovat. Jaké konvence dodržovat, jak pojmenovávat soubory, co dělat při ingestu, jak odpovídat na dotazy. Tahle vrstva v původním tweetu chyběla a přitom je klíčová — je to rozdíl mezi disciplinovaným wiki správcem a generickým chatbotem.

Karpathy taky ostře pojmenovává rozdíl oproti RAG: v klasickém RAG systému se znalosti přeodvozují při každém dotazu — LLM pokaždé znovu hledá a skládá fragmenty. Nic se nekumuluje. Wiki je naproti tomu „persistent, compounding artifact” — znalosti se zkompilují jednou a pak se udržují aktuální. Křížové odkazy už existují. Rozpory už byly označeny. Syntéza odráží všechno, co jste kdy přečetli.

### Co přidává komunita v komentářích

Gist má přes 60 komentářů a řada z nich přidává reálnou hodnotu.

**Produkční zkušenosti.** Jeden tým, který systém provozuje napříč několika doménami, doporučuje klasifikovat zdroje před extrakcí — padesátistránková zpráva potřebuje jiný přístup než dvoustránkový dopis. Navrhují také pravidlo „každý task produkuje dva výstupy” — odpověď pro vás a aktualizaci wiki. Bez tohoto pravidla znalosti mizí do historie chatu. Doporučují také dát indexu explicitní token budget a definovat šablony podle typu entity — jiná šablona pro osobu, jiná pro událost, jiná pro koncept.

**Voice-first capture.** Brazilský vývojář Paulo Souza běží verzi přes Telegram a Whisper — nahrává hlasové poznámky za chůze, Whisper přepisuje, LLM klasifikuje a směruje do wiki. Přes 70 hlasových záznamů zkompiloval do 100 wiki uzlů a několika publikovaných článků. To řeší capture bottleneck — nemusíte sedět u počítače, abyste přidávali zdroje. Důležité pravidlo, které zavádí: LLM je stenograf, ne ghostwriter — každá věta musí být odvoditelná z toho, co člověk skutečně řekl. Mezery dostávají `[TODO: ...]` značky, ne vymyšlený obsah.

**Flat soubory nestačí.** Polský vývojář upozorňuje, že jakmile máte stovky stránek a chcete se ptát „co jsem přidal minulý týden o X”, index jako soubor přestane stačit. Jeho projekt Binder ukládá data do transakčního logu v SQLite a markdown soubory generuje jako view — index není soubor udržovaný ručně, ale dotaz, který je vždy aktuální.

**Kumulace rozporů.** Japonský komentátor varuje, že hlavní příčinou degradace kvality wiki není objem dat, ale kumulace rozporů — a navrhuje architekturu, která je řeší autonomně. To potvrzuje, že Karpathyho „linting” není volitelný doplněk, ale nutná součást systému.

##  Kde to drhne

Systém je elegantní, ale má reálná omezení, o kterých se méně mluví.

**Ruční přidávání zdrojů** — Karpathy přiznává, že každý zdroj přidává ručně, jeden po druhém. Při 100 článcích to zvládnete. Při 1 000 začínáte mít problém. Voice-first varianta přes Telegram je zatím nejpřesvědčivější řešení capture bottlenecku, ale i ta vyžaduje disciplínu. špatné je , když máte historii poznámek jako já ...

**Škálování** — 400 000 slov bez RAG zatím funguje. Sám říká „při této malé škále”. Při milionech slov context window nestačí a budete potřebovat přesně tu fancy infrastrukturu, které jste se chtěli vyhnout. Karpathy v gist doporučuje [qmd](https://github.com/tobi/qmd) — lokální search engine pro markdown s hybridním BM25/vektorovým vyhledáváním — jako řešení pro větší wiki.

**Kvalita kompilace** — LLM při kompilaci dělá rozhodnutí o tom, co je důležité a co ne. Bez vašeho dozoru se mohou drobné nepřesnosti kumulovat. „Health checks” které Karpathy zmiňuje jsou nutnost, ne volba. Jak upozorňuje jeden z komentátorů v gist: LLM umí syntetizovat bez citací a vy si toho nevšimnete, dokud se nepodíváte. Pravidlo „cituj zdroj u každého tvrzení” patří do schema souboru.

**Verzování** — tohle Karpathy v tweetu nezmiňoval, v gist už ano — wiki je git repo, verzování máte zdarma. Po každém LLM průchodu commitnete, a když se něco rozbije, máte diff. Nemusíte reviewovat každý commit, ale namátkový pohled na změny jednou za čas vás ochrání před kumulací halucinací.

**Syntéza versus porozumění** — jeden z nejhlubších komentářů přichází od esejisty, který srovnává Karpathyho systém s Luhmannovou kartotékou (Zettelkasten). Karpathyho systém řeší údržbu znalostní báze, ale neřeší syntézu — osobní reformulaci, která je mechanismem porozumění, ne neefektivitou. Doporučení: použijte LLM wiki na průzkum a mapování terénu, ale vlastní argumentaci a závěry pište sami.

Ale tyhle výhrady jsou detaily. Jádro myšlenky je správné.

## Jak to zkusit sami — prakticky

Nejrychlejší cesta: zkopírujte [Karpathyho idea file](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) a vložte ho do Claude Code nebo Cursoru. Agent vám pomůže postavit strukturu přizpůsobenou vašim potřebám — přesně k tomu je idea file navržený. Pokud chcete víc kontroly, tady je ruční postup:

### Struktura

```
~/knowledge/
├── raw/           # zdrojové články, PDF, obrázky (immutable)
├── wiki/          # LLM-generované .md články
├── output/        # analýzy, srovnání, reporty
└── CLAUDE.md      # schema — instrukce pro LLM jak kompilovat wiki
```

### Ingestion — jak dostat zdroje dovnitř

Tohle je skutečný bottleneck celého systému a Karpathy ho podceňuje. Realistické možnosti:

- **MarkDownload** (rozšíření pro Chrome/Firefox) — uloží webovou stránku jako `.md` jedním kliknutím přímo do zvoleného adresáře
- **Obsidian Web Clipper** — totéž, ale rovnou do Obsidian vaultu. Karpathy doporučuje nastavit si hotkey pro stažení obrázků lokálně, aby LLM mohl pracovat i s vizuálním obsahem
- Pro PDF: knihovna `marker` nebo `docling` na extrakci textu, ale počítejte s občasným ručním dočištěním
- Nejjednodušší varianta: řekněte Claude Code ať si článek stáhne sám — `claude "Stáhni článek z [URL] do raw/ a zpracuj do wiki"`

### Kompilace — klíčový krok

Tady nastupuje LLM. Pokud používáte Claude Code, workflow vypadá takto:

```bash
claude "Zpracuj nové soubory v raw/, aktualizuj wiki a index"
```

Claude Code pracuje přímo se souborovým systémem — čte `raw/`, vytváří a aktualizuje soubory ve `wiki/`, udržuje index. Alternativně funguje Cursor, Codex nebo jakýkoli jiný nástroj, který dá LLM přístup k adresáři.

Klíčové je ale napsat kvalitní `CLAUDE.md` — schema soubor s instrukcemi, jak má LLM wiki strukturovat. **Tohle je 80 % hodnoty celého systému.** Definujte v něm formát článků, jak pojmenovávat soubory, jak propojovat koncepty, co dělat s protichůdnými informacemi. Příklad:

```markdown
# Knowledge Base

## Struktura
- raw/ obsahuje zdrojové materiály (markdown, PDF, obrázky) — nikdy je nemodifikuj
- wiki/ obsahuje zpracované články, jeden koncept = jeden soubor
- wiki/index.md je hlavní rozcestník s kategoriemi a jednořádkovými shrnutími
- output/ je pro analýzy, srovnání, reporty

## Pravidla pro wiki články
- Každý článek začíná YAML frontmatter (title, tags, sources, updated)
- Sekce: Shrnutí, Detail, Související články, Zdroje
- Odkazy na jiné články: [[název-článku]]
- Pokud zdrojová data si protiřečí, zapiš obě verze a označ konflikt
- U každého tvrzení uveď zdroj — nikdy nesyntetizuj bez citace

## Kompilační workflow
1. Zkontroluj raw/ na nové nebo změněné soubory
2. Pro každý nový zdroj: extrahuj klíčové koncepty
3. Pro každý koncept: aktualizuj nebo vytvoř wiki článek
4. Aktualizuj index.md
5. Zapiš changelog do output/changelog.md
```

### Dotazování

```bash
claude "Projdi wiki/ a odpověz: jaké jsou hlavní rozdíly mezi X a Y?"
claude "Na základě wiki/ vytvoř srovnávací tabulku, ulož do output/"
```

Výstupy z `output/` můžete archivovat zpět do wiki — přesně jak to dělá Karpathy. Každý váš dotaz znalostní bázi rozšiřuje. Tohle je princip „každý task produkuje dva výstupy” — odpověď pro vás a aktualizaci wiki.

### Linting — tohle nepřeskakujte

```bash
claude "Projdi wiki/, najdi články bez zdrojů, protichůdná tvrzení
a témata zmíněná ale bez vlastního článku.
Výstup zapiš do output/health-report.md"
```

Pravidelné health checks jsou nutnost, ne luxus — bez nich se rozpory a nepřesnosti kumulují. Jeden uživatel v gist komentářích nastavil automatický noční lint přes naplánovaný prompt — wiki se tak „opravuje sama”.

### Nástroje pro větší wiki

Jakmile wiki přeroste desítky článků a index přestane stačit:

- **[qmd](https://github.com/tobi/qmd)** — lokální search engine pro markdown s hybridním BM25/vektorovým vyhledáváním a LLM re-rankingem. Má CLI i MCP server, takže ho LLM může používat jako nativní nástroj. Karpathy ho doporučuje v gist.
- **Obsidian Dataview plugin** — pokud LLM přidává YAML frontmatter (tagy, data, počty zdrojů), Dataview z toho generuje dynamické tabulky a přehledy
- **Obsidian graph view** — nejlepší způsob jak vidět tvar wiki — co je propojené, co jsou huby, co jsou sirotci

## Proč je to důležité

Karpathy nepopsal nový nástroj. Popsal nový způsob myšlení o AI.

Dosud jsme AI používali reaktivně: máme problém, AI pomůže vyřešit. Karpathy navrhuje proaktivní přístup: nechte AI průběžně budovat vaši znalostní infrastrukturu, abyste byli připravení na otázky, které ještě nemáte.

To je rozdíl mezi člověkem, který hledá v Googlu, a člověkem, který má osobního výzkumného asistenta, jenž pro něj celé měsíce čte, organizuje a syntetizuje.

Karpathy sám přirovnává myšlenku k Vannevaru Bushovi a jeho konceptu Memex z roku 1945 — osobnímu, kurátorovanému úložišti znalostí s asociativními stezkami mezi dokumenty. Bush měl vizi blíž k téhle wiki než k tomu, čím se stal web. Část, kterou nedokázal vyřešit, bylo kdo tu údržbu bude dělat. LLM to řeší.

Lidé zjevně tuhle myšlenku chtějí realizovat. Zatím to ale většina z nich nedělá — protože nevědí, jak začít.

Pokud chcete začít dnes: zkopírujte [Karpathyho idea file](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), vložte to do Claude Code a řekněte „postav mi znalostní wiki na téma X”. Nebo to udělejte ručně — založte si adresář, nainstalujte si MarkDownload, přidejte 10–15 článků, napište `CLAUDE.md` s pravidly kompilace. Celé to zabere odpoledne — a uvidíte, jestli vám ten způsob práce sedí, dřív než budete investovat do čehokoliv složitějšího.