---
slug: karpathy-llm-knowledgebase
author: Patrick Zandl
categories:
- AI
- LLM
- produktivita
- znalostní management
layout: post
post_excerpt: Andrej Karpathy zveřejnil návod jak používat AI jinak – ne na psaní kódu, ale na budování osobní znalostní báze. 82 000 záložek za čtyři dny říká, že lidi tohle chtějí. Tady je překlad, kritický rozbor a praktický návod jak začít. Aktualizováno o tři měsíce vývoje – Google vydal standard OKF a vznikly první hotové produkty, se kterými se dá experimentovat hned.
summary_points:
- Karpathy přestal používat AI hlavně na kód a místo toho ho používá na kompilaci osobní wiki z markdown souborů
- LLM průběžně indexuje zdroje, píše články, propojuje koncepty a odpovídá na dotazy – člověk jen přináší zdroje a otázky
- Systém běží na třech vrstvách - raw (zdroje), wiki (LLM-generovaná), schema (CLAUDE.md s pravidly chování)
- 82 000 záložek za čtyři dny ukazuje, že lidi tuhle myšlenku chtějí – ale zatím nevědí jak začít
- Karpathy následně zveřejnil idea file — nový formát sdílení, kde nesdílíte kód, ale myšlenku, a agent si implementaci postaví sám
- Komunita už za den vytvořila desítky implementací — od Go binárky přes Claude Code skill po voice-first verzi přes Telegram
- Aktualizace po třech měsících – Google vydal Open Knowledge Format (OKF), vendor-neutrální standard, který přesně tenhle vzor formalizuje
- Vzniklo i několik hotových produktů — llmwiki.app, skilly instalovatelné jedním příkazem i enterprise varianty s grafem — takže dnes se dá experimentovat bez stavění od nuly
title: Karpathy přišel na to, jak používat AI jinak. A má pravdu.
thumbnail: https://www.marigold.cz/assets/karpathy-llm.jpg
---

Andrej Karpathy — člověk, který stál u zrodu GPT — zveřejnil minulý týden Twitter příspěvek, který si za čtyři dny záložkovalo přes 82 000 lidí. Třináct milionů zobrazení. To není virální hype. To je něco, co lidi zasáhlo, protože to pojmenovává něco, co sami cítí, ale neuměli to říct. Pointa? Jak používat LLM k budování znalostní databáze?

> **Aktualizováno v červenci 2026.** Původní text vyšel v dubnu, tři dny po Karpathyho příspěvku. Za tři měsíce přibylo dost, aby to stálo za doplnění — a novinky jsou v článku na třech místech: Google vydal standard **Open Knowledge Format** (sekce „Za tři měsíce: z myšlenky standard”), vznikly první **hotové produkty**, se kterými se dá experimentovat bez stavění od nuly (sekce „Existují už hotové produkty? Ano”), a přidal jsem úvahu **kdy má second brain vůbec smysl** a jak se liší nasazení u jednotlivce a ve firmě (sekce „Má to pro tebe vůbec smysl?”).

## Co Karpathy říká

Stručně: přestal používat AI hlavně na kód. Místo toho ho používá na budování osobní znalostní báze. Pojdme to okopirovat, protože je to dobré. a rozvest, protože je kam…

Konkrétní postup:

1. Sbírá zdroje — články, papery, repozitáře, datasety, obrázky — do adresáře `raw/`
1. LLM z toho průběžně „kompiluje” wiki: kolekci `.md` souborů s články, shrnutími a zpětnými odkazy
1. Wiki uživatel prohlíží v Obsidianu
1. Když má otázku, ptá se LLM agenta — ten prohledá wiki a odpovídá
1. Výstupy (markdown, slideshowy, grafy) se archivují zpět do wiki — každý dotaz znalostní bázi rozšiřuje

Jeho wiki na jedno téma má teď ~100 článků a ~400 000 slov. Bez RAG, bez vektorové databáze. Jen flat adresář `.md` souborů v Obsidianu. Tady se zadrhavam já, mám článku cca 50000, zejména k 3GPP normám.

> Příručka [Jak na AI ve firmách zdarma ke stažení](http://www.vibecoding.cz/prirucka/?utm_source=post&utm_medium=marigold&utm_campaign=karpathy)...

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

## Za tři měsíce: z myšlenky standard

Píšu tenhle odstavec s tříměsíčním odstupem od původního textu — a musím ho doplnit, protože se stalo něco, co Karpathy v gistu jen tušil. V citaci z jeho gistu jsem výše nechal větu „Open Knowledge Format (OKF) Import is officially coming.” Tehdy to znělo jako vzdálený příslib. Dnes je to realita.

12. června 2026 vydal **Google Cloud** (tým Data Cloud, Sam McVeety a Amir Hormati) **Open Knowledge Format v0.1** — otevřenou, vendor-neutrální specifikaci, která formalizuje přesně ten vzor, o kterém je celý tenhle článek. Google to popisuje bez okolků: OKF „formalizuje LLM-wiki vzor do přenositelného, interoperabilního formátu”.

A pointa je, že je to skoro až provokativně jednoduché. OKF bundle je **adresář markdown souborů s YAML frontmatterem**, kde jediné povinné pole je `type`. Žádný schema registr, žádná centrální autorita, žádný povinný tooling. Slovy specifikace: „když umíš `cat` souboru, umíš číst OKF; když umíš `git clone` repozitáře, umíš ho poslat dál.” Doporučená pole jsou `title`, `description`, `resource`, `tags` a `timestamp` — a producent si může přidat jakákoli další, konzument je musí tolerovat a nikdy nesmí bundle odmítnout kvůli neznámému poli.

```
sales/
├── index.md          # rozcestník (progressive disclosure)
├── log.md            # append-only changelog
├── datasets/
│   └── orders_db.md
├── tables/
│   ├── orders.md
│   └── customers.md
└── metrics/
    └── weekly_active_users.md
```

Vidíte to? Je to Karpathyho `raw/` + `wiki/` + `index.md` + `log.md`, jen s razítkem Googlu a garantovanou interoperabilitou. **Wiki, kterou si postavíte dnes podle OKF, půjde zítra otevřít cizím agentem bez konverze.** Google zároveň upravil svůj Knowledge Catalog, aby OKF bundly rovnou konzumoval a servíroval svým agentům — což je ta enterprise cesta pro firmy, které už na GCP jsou.

Pro mě je to nejdůležitější zpráva od původního tweetu. Karpathy volal po „úžasném novém produktu místo hacky sbírky skriptů”. Nedostali jsme produkt — dostali jsme **standard**, což je nakonec cennější. Standard je to, co z „hacky sbírky skriptů” dělá ekosystém.

## Kde to drhne

Systém je elegantní, ale má reálná omezení, o kterých se méně mluví.

**Ruční přidávání zdrojů** — Karpathy přiznává, že každý zdroj přidává ručně, jeden po druhém. Při 100 článcích to zvládnete. Při 1 000 začínáte mít problém. Voice-first varianta přes Telegram je zatím nejpřesvědčivější řešení capture bottlenecku, ale i ta vyžaduje disciplínu. špatné je , když máte historii poznámek jako já …

**Škálování** — 400 000 slov bez RAG zatím funguje. Sám říká „při této malé škále”. Při milionech slov context window nestačí a budete potřebovat přesně tu fancy infrastrukturu, které jste se chtěli vyhnout. Karpathy v gist doporučuje [qmd](https://github.com/tobi/qmd) — lokální search engine pro markdown s hybridním BM25/vektorovým vyhledáváním — jako řešení pro větší wiki. Přesně tady vidím řešení svého vlastního problému s ~50 000 poznámkami k 3GPP normám: **Obsidian má od února 2026 oficiální CLI se stovkou příkazů**, takže agent s přístupem k shellu s vaultem pracuje nativně — hledá, zakládá poznámky, připojuje obsah — a nemusí si celý vault tahat do kontextu. To je ta chybějící vrstva mezi „flat soubory stačí” a „musíte postavit vektorovou databázi”.

**Kvalita kompilace** — LLM při kompilaci dělá rozhodnutí o tom, co je důležité a co ne. Bez vašeho dozoru se mohou drobné nepřesnosti kumulovat. „Health checks” které Karpathy zmiňuje jsou nutnost, ne volba. Jak upozorňuje jeden z komentátorů v gist: LLM umí syntetizovat bez citací a vy si toho nevšimnete, dokud se nepodíváte. Pravidlo „cituj zdroj u každého tvrzení” patří do schema souboru.

**Verzování** — tohle Karpathy v tweetu nezmiňoval, v gist už ano — wiki je git repo, verzování máte zdarma. Po každém LLM průchodu commitnete, a když se něco rozbije, máte diff. Nemusíte reviewovat každý commit, ale namátkový pohled na změny jednou za čas vás ochrání před kumulací halucinací.

**Syntéza versus porozumění** — jeden z nejhlubších komentářů přichází od esejisty, který srovnává Karpathyho systém s Luhmannovou kartotékou (Zettelkasten). Karpathyho systém řeší údržbu znalostní báze, ale neřeší syntézu — osobní reformulaci, která je mechanismem porozumění, ne neefektivitou. Doporučení: použijte LLM wiki na průzkum a mapování terénu, ale vlastní argumentaci a závěry pište sami.

Ale tyhle výhrady jsou detaily. Jádro myšlenky je správné.

## Existují už hotové produkty? Ano — a je jich překvapivě hodně

Když jsem článek psal poprvé, odpověď zněla „postavte si to sami”. Za tři měsíce se to změnilo. Karpathyho „idea file” zafungoval přesně tak, jak měl — lidé si z něj postavili implementace a část z nich dotáhli do stavu, kdy je můžete jen nainstalovat a experimentovat. Dělím je do tří kategorií podle toho, kolik práce vás stojí.

### Skutečně hotové produkty (nainstalujete a běží)

- **[llmwiki.app](https://github.com/lucasastorian/llmwiki)** (Lucas Astorian) — zatím nejblíž tomu „úžasnému produktu”, po kterém Karpathy volal. Máte na výběr hostovanou verzi zdarma nebo self-host. Součástí je **webová aplikace** (Next.js) na prohlížení vaší osobní Wikipedie s grafem a proklikem na zdroje, **Chrome rozšíření** na clipování stránek a PDF i s highlighty a poznámkami, **MCP server** pro Claude a hlavně **noční Claude Routine**, která wiki autonomně udržuje. Chytrý detail: chytá i vaše poznámky na okraj, ne jen zdroj — takže wiki je záznam nejen toho, co jste četli, ale co jste si o tom mysleli.
- **NotebookLM** (Google) — nejdostupnější varianta, ale jiná filozofie. Umí Deep Research (sám najde zdroje na webu) i podcast režim s dvěma AI moderátory. Jenže je to pořád **dotazovací nástroj, ne kompilující wiki** — znalost se nekumuluje, systém strukturu nevlastní. Přesně ten rozdíl, který v sekci „Co říká komunita” zdůrazňuji. Dobrý na rychlý začátek, špatný jako dlouhodobá znalostní infrastruktura.
- **Mem.ai, Reflect** — komerční „second brain” aplikace s AI. Automaticky propojují poznámky, Reflect je šifrovaný a kalendářově orientovaný. Ale ani jeden nedělá to hlavní z Karpathyho vzoru — nenechá agenta vlastnit a přestavovat strukturu. Spíš kontrast než náhrada.

### Instalace jedním příkazem (pro Claude Code, Cursor, Codex)

Tohle je pro každého, kdo už s agentem pracuje a nechce nic hostovat:

- **[Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki)** — `npx add-skill Astro-Han/karpathy-llm-wiki`. Zabalí celý vzor do jednoho [Agent Skillu](https://agentskills.io): ingest → kompilace → dotazování s citacemi → lint. Funguje v Claude Code, Cursoru, Codexu i OpenCode.
- **[toolboxmd/karpathy-wiki](https://github.com/toolboxmd/karpathy-wiki)** — Claude Code skill s detached background workerem, který ingest zpracuje na pozadí, aniž vás vyruší z práce. Git-verzované, umí hlavní i per-project wiki.
- **[jlbgit/PersonalKnowledgeBaseCreator](https://github.com/jlbgit/PersonalKnowledgeBaseCreator)** — skilly `/compile-wiki`, `/ask-wiki`, `/lint-wiki` pro Cursor, Claude Code i Copilot. Autoři uvádějí 50–90 % úsporu tokenů oproti dotazování raw souborů — protože agent prochází graf `[[odkazů]]`, ne celý korpus.
- **[supachai-j/open-knowledge-format-starter](https://github.com/supachai-j/open-knowledge-format-starter)** — starter postavený rovnou nad OKF v0.1, s validátorem konformity a generátorem grafové vizualizace. Pokud chcete začít rovnou standardem, tohle je vstupní bod.

### Pro náročnější a firemní nasazení

- **[lcwiki](https://github.com/LCccode/Karpathy-wiki-graph)** — „enterprise” varianta se třemi vrstvami (články + koncepty + interaktivní graf s detekcí komunit) a chytrým inkrementálním ingestem za zhruba 10 % nákladu klasického RAG.
- **[knowledge-engine](https://github.com/nipashnp/knowledge-engine)** — dvouvrstvý most mezi lidsky čitelnou wiki a strojovou pamětí (Memvid), se sub-5ms sémantickým vyhledáváním. Memvid je volitelný — bez něj běží jako čistá wiki.
- **Obsidian implementace** ([Ar9av/obsidian-wiki](https://github.com/ar9av/obsidian-wiki), [NicholasSpisak/second-brain](https://github.com/NicholasSpisak/second-brain), claude-obsidian) — pro mě osobně nejrelevantnější větev. Díky oficiálnímu Obsidian CLI a MCP se z Obsidianu stává „IDE”, LLM je „programátor” a vaše wiki „codebase”. Přesně to řeší můj problém s historií tisíců poznámek — nemusím migrovat, agent pracuje s vaultem tam, kde je.

Co bych zkusil první, kdybych začínal dnes: **llmwiki.app** na rychlé osahání myšlenky (nejmíň tření), a paralelně některý **Agent Skill** nad vlastním adresářem, pokud už používám Claude Code. Rozhodnutí padne za odpoledne — a to je pořád pointa celého systému.

## Má to pro tebe vůbec smysl?

Než si založíš adresář, polož si nepříjemnou otázku: nebude z toho jen další hřbitov poznámek? Protože přesně tam většina pokusů skončí — lidi tam cpou obsah jako do „Googlu s extra kroky” a pak ho nikdy neotevřou. Hodnota second brainu totiž nevzniká ukládáním cizích článků. Vzniká až tím, že obsah **zpracuješ** a propojíš s vlastním myšlením.

Z toho plyne poctivé přiznání, které v návodech obvykle chybí: **pokud si dlouhodobě nic nezapisuješ, je pro tebe často rychlejší prostě googlit a zeptat se LLM.** „Typické problémy při řízení softwarového projektu” ti veřejné modely vytáhnou líp než tvoje prázdná wiki. Second brain se vyplatí tomu, kdo už s informacemi pracuje jako s materiálem — tvůrcům, vývojářům, konzultantům, výzkumníkům, manažerům. Tiago Forte, který tohle téma zpopularizoval, razí, že většina hodnoty vzniká už jen tím, že si věci zapisuješ a později je dohledáš. Propojování a syntéza jsou třešnička — ale nejdřív musí existovat co propojovat.

A tady je napojení na Karpathyho, které tu úvahu posouvá dál. Jeho wiki není „lepší Google”. Google — a dnes Perplexity, ChatGPT nebo Gemini — exceluje ve **veřejné** znalosti. Tvoje wiki řeší něco, co Google nikdy mít nebude: **tvůj** kontext. Co sis z článku odnesl, jak to souvisí s projektem před dvěma lety, co tehdy fungovalo a co ne. A na rozdíl od RAGu, který ten kontext přeodvozuje při každém dotazu znovu, wiki ho **zkompiluje jednou** a dál zhodnocuje. To je ten compounding efekt — znalost se ti hromadí rok od roku jako investice, ne jako nový search od nuly. (Ano, i ChatGPT má dnes paměť. Ale je to paměť u poskytovatele, ne tvůj vlastní, exportovatelný a agentem přestavitelný korpus.)

**A firma?** Tam je to jiný příběh — a většinou jednoznačnější. Osobní second brain je nástroj na syntézu; firemní znalostní báze je **infrastruktura**. Její hlavní přínos není v ničím osobním pohledu na věc, ale v tom, že znalosti přestávají žít v hlavách jednotlivců a stávají se majetkem firmy — rychlejší onboarding, menší závislost na konkrétních lidech, uchované „co jsme se už jednou naučili”. Největší překážka přitom není technologie (RAG přes dokumenty, meeting notes a tickety dnes umíme), ale **kultura** — donutit lidi znalosti zapisovat a sdílet. To je ale téma na samostatný článek.

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

Lidé zjevně tuhle myšlenku chtějí realizovat. Když jsem tenhle článek psal poprvé, hlavní překážkou bylo, že nikdo nevěděl, jak začít. Za tři měsíce se to obrátilo — Google vydal standard, komunita hotové produkty, a překážkou už není „jak”, ale „z čeho vybrat”. To je hezký problém. Znamená, že myšlenka přežila fázi hype a usadila se jako způsob práce.

Pokud chcete začít dnes, máte tři cesty podle chuti si hrát. Nejrychlejší: založte si účet na **[llmwiki.app](https://github.com/lucasastorian/llmwiki)** nebo nainstalujte Agent Skill (`npx add-skill Astro-Han/karpathy-llm-wiki`) a nechte hotový nástroj, ať vás provede. Vlastní cesta: zkopírujte [Karpathyho idea file](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), vložte to do Claude Code a řekněte „postav mi znalostní wiki na téma X”. Nebo to udělejte celé ručně — založte si adresář, nainstalujte si MarkDownload, přidejte 10–15 článků, napište `CLAUDE.md` (nebo rovnou OKF bundle) s pravidly kompilace. Ať zvolíte cokoli, celé to zabere odpoledne — a uvidíte, jestli vám ten způsob práce sedí, dřív než budete investovat do čehokoliv složitějšího.
