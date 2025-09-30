---
author: Patrick Zandl
categories:
- AI
- Anthropic
- Claude
- LLM
- Cloudflare
layout: post
post_excerpt: Anthropic vydal aktualizaci modelu Claude Sonnet 4.5 s experimentální funkcí Imagine, která vytváří aplikace v reálném čase podle interakce uživatele, plus rozšíření Claude for Chrome.
summary_points:
- Claude Sonnet 4.5 dosahuje 49% úspěšnosti na SWE-bench Verified a dokáže udržet soustředění na složité úlohy přes 30 hodin
- Experimentální funkce Imagine vytváří kód aplikací průběžně podle toho, jak s nimi uživatel interaguje
- Rozšíření Claude for Chrome umožňuje provádět akce v prohlížeči včetně práce s dokumenty a e-maily
- Model vykazuje výrazné zlepšení v doménově specifických znalostech podle expertů z financí, práva a medicíny
- Nové Claude Agent SDK umožňuje vývojářům vytvářet vlastní agenty na bázi technologií použitých v Claude Code
- Funkce pro vytváření souborů je nyní dostupná všem placeným uživatelům, rozšíření pro Chrome se postupně zpřístupňuje
title: Nový Claude Sonnet 4.5 s experimentální funkcí Imagine
---

Anthropic představil Claude Sonnet 4.5, novou verzi svého jazykového modelu, která podle společnosti přináší výrazné zlepšení zejména v oblasti práce s programovacím kódem. Součástí vydání je experimentální funkce Imagine, která generuje aplikace v reálném čase podle interakce uživatele, a rozšíření Claude for Chrome pro automatizaci činností v prohlížeči.

## Výrazné zlepšení v kódování

Claude Sonnet 4.5 dosahuje 49% úspěšnosti na benchmarku SWE-bench Verified, což představuje zlepšení oproti předchozí verzi Claude Sonnet 4, která dosahovala 38,8%. Benchmark SWE-bench Verified testuje schopnost modelů řešit skutečné problémy ze softwarových projektů na platformě GitHub. Model tak podle výsledků testů překonává konkurenční modely včetně GPT-4o, Gemini 2.0 Flash Thinking i o1-preview.

![Graf porovnání výkonu modelů na SWE-bench](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8338066c/images/swe-bench-verified-chart.png)

V praktickém použití to znamená, že model lépe rozumí struktuře kódu, dokáže identifikovat chyby a navrhovat jejich řešení. Podle Anthropic je model schopen pracovat s rozsáhlými kódovými bázemi a udržovat konzistenci napříč více soubory. Anthropic uvádí, že model dokáže udržet soustředění na složité úlohy po dobu přesahující 30 hodin, zatímco výkonnější model Opus 4 zvládá zhruba sedm hodin.

Při testování podle Anthropic jako jediný model v historii společnosti dokázal vytvořit funkční verzi webové stránky Claude.

## Experimentální funkce Imagine

Novou experimentální funkcí je Imagine with Claude, která generuje kód aplikací průběžně podle toho, jak s nimi uživatel pracuje. Tato funkce je zatím dostupná pouze pro předplatitele Max. Na rozdíl od standardního přístupu, kdy model napíše kompletní kód předem, Imagine vytváří jednotlivé části aplikace dynamicky v reakci na akce uživatele.

Demonstrace ukázala prompt “Imagine William Shakespeare’s computer”, na který Claude vytvořil interaktivní počítač, jaký by mohl používat Shakespeare. Aplikace se otevírá přímo v rozhraní Claude a umožňuje s ní pracovat. Když uživatel klikne na položku menu, Claude v danou chvíli vygeneruje příslušný kód, což umožňuje prohlížet Shakespearův počítač v reálném čase.

![Ukázka režimu Extended Thinking](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8338066c/images/extended-thinking.png)

Anthropic tuto funkci popisuje jako software, který se sám vytváří v reakci na potřeby uživatele. Jde o naznačení směru, kterým by se mohly aplikace ubírat - nemusely by být předem naprogramované, ale dokázaly by reagovat přesně na to, co uživatel potřebuje.

## Nový režim rozšířeného uvažování

Součástí aktualizace je funkce Extended Thinking, která umožňuje modelu věnovat více času složitějším úlohám. Při aktivaci tohoto režimu model nejprve interně analyzuje problém, než poskytne odpověď. Tato funkce je určena pro úlohy jako ladění složitého kódu, tvorbu obchodních strategií nebo řešení vícekrokových matematických problémů.

Extended Thinking pracuje tak, že model prochází delším procesem uvažování před formulací odpovědi. Uživatel vidí průběh tohoto procesu a následně finální výstup. Režim se zapína ručně přepínačem v rozhraní a spotřebovává více tokenů než standardní režim.

## Integrace s platformou Cloudflare Workers

Významnou novinkou je přímá integrace s platformou [Cloudflare Workers](https://workers.cloudflare.com/), která umožňuje vytvářet a nasazovat webové aplikace přímo z rozhraní Claude. Uživatelé mohou popsat, jakou aplikaci potřebují vytvořit, a Claude vygeneruje funkční kód, který se následně automaticky nahraje na infrastrukturu Cloudflare.

Cloudflare Workers je platforma pro provoz kódu JavaScriptu na serverech Cloudflare po celém světě. Výhodou tohoto řešení je rychlé nasazení bez nutnosti spravovat vlastní servery. Integrace s Claude umožňuje vytvářet aplikace využívající databáze D1, úložiště R2, key-value databázi KV nebo systém Hyperdrive pro připojení k externím databázím.

Pro využití této funkce je nutné propojit účet Cloudflare s Claude. Aplikace vytvořené tímto způsobem běží na infrastruktuře Cloudflare a podléhají jejím limitům a cenovým podmínkám. Bezplatná verze Cloudflare Workers umožňuje 100 tisíc požadavků denně.

## Rozšíření Claude for Chrome

Anthropic rozšiřuje dostupnost [rozšíření Claude for Chrome](https://www.anthropic.com/news/claude-for-chrome), které bylo spuštěno koncem srpna nejprve pro předplatitele Max. Nyní získávají přístup další uživatelé ze seznamu čekatelů. Rozšíření umožňuje modelu provádět akce v prohlížeči Chrome jménem uživatele po udělení příslušných oprávnění.

Demonstrace ukázala, že Claude for Chrome dokáže navigovat v aplikacích jako Google Docs a Gmail, sbírat informace, vytvářet a aktualizovat dokumenty a odesílat e-maily. Model tak může autonomně pracovat s webovými aplikacemi podle pokynů uživatele.

Podle Anthropic se zlepšily možnosti modelu využívat počítač ve srovnání s předchozí verzí Sonnet 4. Společnost také zdůrazňuje, že nový model je bezpečnější a lépe sladěný s očekáváním uživatelů, s redukovaným výskytem problematického chování jako je podlézavost, klamání, touha po moci nebo tendence podporovat bludy.

## Rozšířená podpora nástrojů

Claude Sonnet 4.5 přináší rozšířenou podporu pro práci s kalendářem a připomínkami. Model dokáže vytvářet, upravovat a mazat události v kalendáři a spravovat připomínky. Tyto funkce vyžadují udělení přístupu k příslušným aplikacím v operačním systému.

Vylepšena byla také práce se soubory. Model dokáže zpracovávat dokumenty ve formátu PDF, tabulky Excel a CSV soubory. U souborů Excel zachovává informace o formátování, vzorcích a stylech buněk. Při zpracování dat z tabulek model automaticky detekuje strukturu a dokáže provádět agregace, filtrování a vytváření vizualizací.

Anthropic také přidal podporu pro vytváření a spouštění kódu přímo v konverzacích s Claude, včetně možnosti vytvářet dokumenty, tabulky a prezentace. [Funkce pro vytváření souborů](https://www.anthropic.com/news/file-creation) je nyní dostupná všem placeným uživatelům, zatímco dříve byla vyhrazena pouze pro předplatitele Max.

## Claude Code a nové SDK pro agenty

Nástroj Claude Code nyní podporuje kontrolní body, které umožňují uživatelům uložit průběh práce a v případě potřeby se vrátit k předchozímu stavu. Claude agenti mohou pracovat delší dobu na složitějších úlohách.

Pro vývojáře je k dispozici nové [Claude Agent SDK](https://www.anthropic.com/news/claude-agent-sdk), které podle Anthropic představuje stavební bloky použité při vývoji Claude Code. Toto SDK umožňuje vývojářům vytvářet vlastní agenty postavené na technologii Claude a napomáhá při dalších programovacích projektech.

## Vylepšení v doménových znalostech

Podle Anthropic experti z různých oblastí včetně financí, práva, medicíny a vědecko-technických oborů zjistili, že Claude Sonnet 4.5 vykazuje výrazné zlepšení v doménově specifických znalostech a schopnosti uvažování ve srovnání s předchozími modely.

## Technické parametry

Model podporuje kontextové okno 200 tisíc tokenů a maximální výstup 8 tisíc tokenů. Podle Anthropic dosahuje kratší doby odezvy než předchozí verze a podporuje vyšší počet požadavků za minutu. Konkrétní hodnoty závisí na typu předplatného.

Pro vývojáře je model dostupný přes API s identifikátorem `claude-sonnet-4-5-20250929`. Cena za použití API zůstává stejná jako u Claude Sonnet 4 a činí 3 dolary za milion vstupních tokenů a 15 dolarů za milion výstupních tokenů. Pro srovnání, výkonnější Claude Opus 4 stojí 15 dolarů za milion vstupních tokenů a 75 dolarů za milion výstupních tokenů.

## Dostupnost a ceny

Claude Sonnet 4.5 je dostupný zdarma s omezeními na počet zpráv. Bezplatná verze umožňuje vytvářet artefakty a používat základní funkce, Extended Thinking však vyžaduje předplatné. Placené předplatné Claude Pro za 20 dolarů měsíčně nabízí vyšší limity na počet zpráv a přístup ke všem funkcím včetně Extended Thinking a integrace s Cloudflare.

Pro firmy je k dispozici předplatné Claude Team za 30 dolarů na uživatele měsíčně, které přidává sdílené projekty, centralizovanou správu a vyšší limity. Enterprise verze s individuální cenou nabízí dedikovanou podporu, SLA a možnost nasazení v privátním cloudu.

Model je dostupný prostřednictvím webového rozhraní na adrese [claude.ai](https://claude.ai), mobilních aplikací pro iOS a Android a vývojářského API. Integrace s Cloudflare vyžaduje aktivaci v nastavení a propojení účtu.​​​​​​​​​​​​​​​​