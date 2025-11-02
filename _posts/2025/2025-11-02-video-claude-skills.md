---
author: Patrick Zandl
categories:
- AI
- Claude Skills
- Claude
- Anthropic
layout: post
post_excerpt: Claude Skills od Anthropicu jsou nesmírně mocný nástroj pro zjednodušení a automatizaci práce prostřednictvím AI. Jenže když si čtete návody, zní to strašně složitě. Ve videu vám ukážu, jak na to - všechnu namáhavou práci za vás udělá AI... 
summary_points:
- Video ukazuje, jak jednoduše vytvořit svůj vlastní Claude Skill s pomocí AI.
- Vysvětluje rozdíl mezi Skill a tradičními makry – Skills rozvíjejí znalosti modelu místo pevných instrukcí.
- Ukázkový Skill automatizuje zápis údajů z faktur do Excelové tabulky na Google Disku.
- Claude Skills podporují napojení na různé nástroje a služby, včetně Google Workspace a externích API.
- Tvorba Skills nevyžaduje programování, stačí definovat požadavky v přirozeném jazyce.
- Skills výrazně usnadňují automatizaci opakovaných úloh a přizpůsobení prostředí uživateli.
title: "Video: vytvořte si svůj první Claude Skills"
thumbnail: https://www.marigold.cz/assets/claude-skills.webp
---

Claude Skills od Anthropicu jsou nesmírně mocný nástroj pro zjednodušení a automatizaci práce prostřednictvím AI. Jenže když si čtete návody, zní to strašně složitě. Ve videu vám ukážu, jak na to - všechnu namáhavou práci za vás udělá AI... 

<iframe width="560" height="315" src="https://www.youtube.com/embed/vSPfE5RMbdc?si=1bzpdf5gS0p6rfT7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Původně jsem chtěl video udělat především jako průvodce, kde se díváte hlavně na software, ale úvodních pár minut nakonec budete koukat na mne, teprve pak, až si vysvětlíme, co všechno Skills mohou a nemohou, se ponoříme do nitra Claude. 

Je možné, že takto se o nových funkcích a především možnostech jejich použití zmíním častěji, v tom případě si s vizualizací videa více pohraju. 

### A o čem video je?

Dnes si řekneme něco o velmi užitečné fuknci Skills, kterou najdeme v AI prostředí Claude od společnosti Anthropics. Název mohli přeložit jako Dovednosti, poangličtěně skilly. 

Dovednosti bychom mohli přirovnat k makrům třeba ve Wordu, čili k předpřipraveným funkcím, které stačí zavolat a ony provedou nějakou akci, ve Wordu třeba vyčistí formátování textu. Jenže přirovnání k makrům je intuitivní, nicméně technicky nepřesné.  Skills jsou spíše vrstvou znalostí než zásobníkem předpřipravených postupů. Zatímco klasická makra v programovacích jazycích nebo kancelářských aplikacích představují předdefiniované sekvence příkazů, Skills fungují jako kontextuální znalostní báze, která doplňuje rozhodovací proces jazykového modelu při řešení úloh o další podstatné informace. Nejsou to spustitelné skripty ani uzavřené funkce - jsou to spíše "expertní konzultační dokumenty", které model čte a interpretuje před zahájením práce. 

Zásadní rozdíl oproti makrům spočívá ve způsobu jejich aplikace. Makro zcela předvídatelně přetváří vstup na výstup podle pevného algoritmu, zatímco Skill dodává modelu oborovou znalost, kterou ten spojuje s okolnostmi konkrétního požadavku uživatele. Model po načtení Skillu stále provádí vlastní úvahu, reasoning. Například při vytváření prezentace docx skill neřídí každý krok jako makro, ale poskytuje znalost o tom, jak správně strukturovat XML hierarchii dokumentu, jak zacházet s formátovacími styly, nebo jak zacházet s nestandardními případy při sledování změn. Výsledné chování vyvstává ze spojení instrukční základny Skillu, obecných schopností modelu a specifických požadavků uživatele. Pokud bychom hledali bližší přirovnání, Skills jsou pojmově blíže k "za běhu načítaným znalostním modulům" než k tradičním makrům, jak je známe třeba právě z Wordu.

Claude Skills jsou speciální dokumenty s odbornými postupy, které model načte právě ve chvíli, kdy potřebuje rozšířit své schopnosti v určité oblasti - třeba při práci s dokumenty Word nebo tabulkami Excel. Jedná se o soubory ve formátu Markdown obsahující destilované osvědčené postupy a pracovní toky, které jsou načítány za běhu pomocí nástroje pro čtení souborů před samotným řešením úkolu. 

Tento přístup obchází nutnost dotrénování modelu a umožňuje rychlou iteraci nad specializovanými doménami znalostí. Skills fungují jako orchestrační vrstva nad nesourodým ekosystémem nástrojů - od základních operací se soubory přes prostředí pro spouštění příkazů shellu až po sofistikované integrační protokoly. Filozofie jejich designu spočívá v explicitním oddělení deklarativních znalostí ("jak správně strukturovat PPTX prezentaci") od imperativních schopností (samotná manipulace se soubory), tedy oddělení a zároveň kooperace mezi znalostmi a vykonávaným kódem.
Skills mohou využívat veškeré nástroje a schopnosti, které má systém k dispozici. To zahrnuje jak vestavěné možnosti jako vstup/výstup ze souborového systému, spouštění procesů, tak externí integrační protokoly. MCP servery jsou plně podporovány a representují primární vzor integrace pro služby třetích stran. Mohu tak používat třeba  napojení na vývojářskou platformu Cloudflare, správu mediálních aktiv v Cloudinary či propojení se Spotify. Důležité je, že Skills rovněž mohou využívat OAuth-zabezpečené konektory pro ekosystém Google Workspace, konkrétně API Gmailu pro získávání zpráv a analýzu vláken konverzací, API Google Disku s možností sémantického vyhledávání v plném textu, a API Kalendáře včetně agregace volných časových bloků napříč více kalendáři. Tato integrace probíhá transparentně s korektní správou autentizačních tokenů a izolací oprávnění.
V praxi Skills demonstruje zajímavou věc: různé nástroje se vzájemně doplňují a společně vytváří složitější funkce. Například skill pro dokumenty Word kombinuje knihovnu python-docx pro manipulaci s objektovým modelem dokumentu s potenciálním voláním konektoru Gmailu pro extrakci obsahu emailů, následovaným operací nahrání na Disk. Skills nejsou izolované kontexty provádění, ale mohou volat další skills v řetězci závislostí (například skill pro grafický design může delegovat úkoly na skill s možností renderování PDF). 

Architektura celého systému je navržena jako rozšiřitelná - vedle již hotových veřejných skills (docx, xlsx, pptx, pdf) existuje mechanismus pro uživatelsky definované skills, což umožňuje uživatelům jednoduše automatizovat pracovní postupy. 

Pojďme se tedy na jednu takovou automatizaci podívat, protože z toho, co jsme vám tu povídal můžete mít dojem, že se skills vytvářejí hodně složitě. Ano, samozřejmě je můžete definovat a programovat ručně, jenže proč je nenechat vytvořit umělou inteligenci podle vašeho zadání. To za prvé. 

Za druhé hlavní výhodou skills je jejich naprosté přizpůsobení problémům a zvyklostem uživatele, což dělá poněkud problematickým najít dostatečně obecný ukázkový příklad. Mám už vytvořenou celou řadu skillů, které používám, ale jsou na moje specifické problémy a vždycky mi dělá potíže najít nějaký zajímavý příklad. Tak si zkusíme jeden problém definovat na ukázku. Mě relativně často přicházejí faktury emailem. Rád bych každou fakturu zapsal do Excelové tabulky a měl v tom trochu pořádek. A přesně na to je skill ideální. 

> **Prompt:** 
> Vytvoř skill, který analyzuje nahranou fakturu a údaje z ní uloží jako aktualizace do xlsx na google drive.

