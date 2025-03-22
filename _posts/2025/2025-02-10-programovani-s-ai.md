---
audio_url: null
author: Patrick Zandl
categories:
- AI
- programování
layout: post
post_excerpt: Ještě před rokem se o tom mluvilo, před půl rokem tomu programátoři
  nevěřili a zkoušeli to. A dnes už je to realita. Jak si mohou neprogramátoři vytvořit
  svoji aplikaci?
summary_points:
- 'AI nástroje umožňují programování i neprogramátorům – generují kód na základě
  popisu, skrývají složitosti.'
- 'Podrobné zadání je klíčové – AI potřebuje přesné instrukce pro kvalitní výsledky.'
- 'Nástroje jako Replit, Tempolabs, Cursor AI – nabízejí různé možnosti od prototypování
  po komplexní vývoj.'
- 'Ceny jsou založeny na spotřebě tokenů – rychle rostou s intenzivním používáním.'
thumbnail: https://www.marigold.cz/assets/ai-programovani.jpg
title: Programování s AI pro neprogramátory -  už je to tady!
---

Programování pro neprogramátory je svatý grál počítačů. A zdá se, že už je opravdu tady. Díky AI vzniklo několik nástrojů, které už se nesoustředí na to, že programátorům našeptávají pokračování příkazu nebo opravují chyby v kódu. Moderní nástroje zdrojový kód vytvářejí celý ze zadání a některé už jej dokonce i před uživatelem skrývají. Programovat může nyní „skoro každý“. Jak na to?

Nejprve se zastavme u slova „skoro každý“. Znamená to, že programovat mohou lidé, kteří jsou schopni definovat, co a jak má jejich program dělat. Řada nástrojů láká na to, že do promptu zadáte „Vytvoř mi klon Instagramu“ a ono to udělá kopii Instagramu. Jenže, když odmyslíme od otázky, proč by někdo měl používat kopii Instagramu, takhle jednoduché to není.  Ve skutečnosti potřebujete podstatně detailnější zadání, aby výsledek práce k něčemu byl.

Tento článek není pro pravověrné programátory, ti si nad tímto směrem jen odplivnou. Jak by se jejich skillům debugingu assembleru mohlo rovnat nějaké AI. A skutečně: špičkový kód nástroje z února 2025 ještě nenapíšou. Ale šéf OpenAI Sam Altman prohlašuje, že již dnes ve firmě testují AI, která kóduje jako jeden z nejlepších programátorů na světě a do konce roku budou mít k dispozici verzi, která bude úplně nejlepší ([zdroj](https://officechai.com/ai/an-ai-will-be-the-worlds-best-programmer-by-the-end-of-2025-openai-ceo-sam-altman/). Věřím tomu, že bude - ještě před rokem takové nástroje teprve vznikaly, pokrok je tu obrovský. 

Pro koho je tedy Programování s AI? Především pro lidi, kteří by potřebovali udělat nějaký „prográmek“ - od jednoduchého scriptu, až po nejrůznější webové aplikace včetně webových stránek. Příklady? Tak například jsem se chtěl podívat na to, kolik obce platí za některé služby. Vlastně to má jednoduché řešení, všechno si mohu najít v databázích a v Excelu spočítat. Pro pár obcí, pro větší množství by mě to nebavilo dělat. Řešení s AI? Za prvé si s AI celou věc probereme. AI mi okamžitě napovídá, že by bylo nejlepší data vyčítat z Monitoru státní pokladny přes API. A rychle se od návrhu posouváme k tomu, že AI naprogramuje volání API, zjistí potřebná data, uloží je do databáze, k nim získá počty obyvatel a přepočítá získaná data na počty obyvatel. Jako neprogramátor bych sám nic takového neudělal a cena vývoje takového software jsou spíše vyšší desítky tisíc, pokud nejste zkušený programátor, který si to spíchne za dva víkendy (jenže fakturační cena jednoho takového dne programátora je právě ta desítka tisíc)...

Jak na něco takového? 

Podíváme se dnes na několik nástrojů, které slouží k programování s AI:
- [Cursor AI](https://www.cursor.com/)
- [Tempolabs AI](https://www.tempolabs.ai/) 
- [Replit](https://replit.com/)
- [Bolt New](https://bolt.new/)   
- [Windsurf AI](https://codeium.com/windsurf)

Za každý z těchto nástrojů musíte zaplatit, i když je tu nějaký malý demoprovoz možný zdarma. Ale s ním si nástroj opravdu jen osaháte, nenaprogramujete nic. A jednou upozornění: nástroje jsou v prudkém vývoji, takže jejich nabídka funkcí se mění, údaje jsou platné k 10.2.2025. 

**Mimochodem, jak je to s češtinou?** Většinou jsme pracovali komicky: já jsem zadání definoval česky, všechny nástroje mu bezproblémů rozuměly, ale odpovídaly mi zpravidla anglicky, nebo tu česky, převážně však anglicky. 

### Replit Agent - kód už nemusíte vidět

Začneme s [Replit](https://replit.com/). Ten to ve svojí mobilní aplikaci (zkoušel jsem jej jen na iPadu) dotáhl tak daleko, že uživatele vlastně ani nepustí ke zdrojovému kódu. Ale pokud si zaplatíte verzi Replit Agent, je vývoj velmi autonomní. Vyzkoušel jsem si naprogramovat Trump Tracker, tedy web, který načítá RSS z důležitých zpravodajských serverů, grupuje články podle tématu a vytváří každodenní přehled o tom, co Trump v jaké oblasti činnosti dělá. Na Replit Agent je příjemné to, že si je schopen sám odchytat nejrůznější chyby, takže na obrazovce vlastně jen sledujete, jak si po zadání úlohy povídá sám se sebou a ještě se omlouvá, že k chybě došlo. Replit Agent je novinka posledních dní, sám jsem jej nestihl příliš využívat, kredity zdarma jsem vyčerpal příliš rychle, takže velký dojem jsem si nestihl odnést. Snad krom té jednoduchosti a odloučenosti od zdrojového kódu, který se v jiných aplikacích ještě před vašimi zraky míhá. Jestli vás to ne/uklidní, ve webové aplikaci Replitu přístup ke zdrojovému kódu stále je, i když se do něj nemusíte tlačit. Tradiční rozhraní Replit Agent nabízí vlevo chatovací okno s Agentem, vpravo vidíte náhled aplikace, kterou můžete rovnou testovat. 

Replit umožňuje také pohodlný „deploy“ - tedy nasazení aplikace na produkční server, pokud si ji nechcete provozovat sami. 

Platební systém není zrovna přehledný: v zásadě si kupujete měsíční kredity, přičemž povídání s Assistantem (neumí tolik odstínit od kódu) stojí 5 centů za dotaz s Claude 3.5 Sonnet nebo 0,25$ za vytvoření „checkpointu“ s Agentem, tedy za dotvoření nějaké části funkce. Jak se to ale počítá, není snadné nastudovat. 

Replit Agent je velmi pohodlná, ale také nejdražší varianta. Ale proti denní mzdě programátora to není nic závratného!

### Replit Agent přehledně

- Nabízí AI asistenta pro generování kódu na základě popisů
- Umožňuje rychlé vytváření prototypů aplikací
- Poskytuje vestavěný chat pro diskuzi a zpětnou vazbu během vývoje
- Pro neprogramátory může být výhodou možnost vytvářet aplikace bez hlubokých znalostí kódování

![Replit Agent](/assets/replit-trumptracker.png)

### Tempolabs AI vs Bolt New- webové vývojové prostředí

[Tempolabs AI](https://www.tempolabs.ai/)  je skvělé vývojové prostředí, které je kopií Visual Studio Code, což je v branži „průmyslový standard“. V současné době umí pracovat s REACT/Vite kódem, další jako Node.js se chystají, ale to neprogramátorům asi nic moc neřekne. 

Tempu řeknete, jakou aplikaci chcete stavět a společně k ní uděláte PRD - dokument definující požadavky na produkt. Zde si popíšete, jak se aplikace má chovat, co z ní má vypadnout a naopak se do ní dostat. Na základě tohoto vygeneruje Temp design webu a postupně na něj napojuje funkce. Když chcete nový čudlík, tak myší ukážete, kde má být, vyberete, jak má vypadat a popíšete přes prompt, co má dělat. I zde máte v prohlížeči kompletní preview, takže se můžete podívat, jak vaše webová aplikace vypadá a funguje. A můžete se připojit na Github a rovnou ji poslat přes Github na svůj server (Cloudflare, Vercel, jak si co nastavíte). 

S Tempolabs jsem strávil hodně času a je to nástroj, který mě nadchnul. Je pravda, že vám příliš předkládá zdrojový kód, zatímco se snaží, abyste měli málo důvodů do něj sahat. Oproti Replitu vám ukáže kód, který doporučuje nahradit a navrhne vám, jak jej nahradit a vy jen stisknete Apply a je hotovo. Zatímco Replit Agent už o kódu příliš nemluví, Tempo se snaží ještě vypadat jako nástroj pro vývojáře. I když bych řekl, že i ono tuhle vizi záhy opustí, protože za měsíc práce s Tempem jsme do zdrojového kódu hrabal jen výjimečně. 

Ceny: platíte za miliony zkonzumovaných tokenů. Půl milionu máte zdarma, za 30 dolarů získáte 25 milionů tokenů. Při celodenní práci jsem toto množství vyčerpal za týden vývoje, při kterém jsem udělal tři aplikace. Můžete si připlatit za další tokeny, za 350 dolarů měsíčně jste bez limitu.

V Tempu jsem naprogramoval [Progressor](https://progressor.work) - trvalo mi to jeden večer to rozchodit, další tři večery jsem to trochu šperkoval. Jen jsem zatím nenapsal, k čemu to je, což je trochu chybička, musím to napravit :) Je to nástroj k zapisování toho, co jste za den udělali. Vždycky, když něco udělám, napíšu si tu jednu větu do Progressoru a pak se kdykoliv mohu podívat, kdy jsem co dělal... 

Přímou konkurencí k Tempu je [Bolt New](https://bolt.new/) . Mírně jiné rozhraní, v němž přepínáte mezi výstupem aplikace a jejím zdrojovým kódem, takže se zdrojákem nemusíte příliš tížit, pokud nechcete. 

#### Tempolabs AI přehledně

- Poskytuje vizuální editor kódu, který usnadňuje úpravy i neprogramátorům
- Umožňuje generování kompletních pohledů pomocí jednoduchých AI promptů
- Integruje AI pro generování vysoce kvalitního React kódu
- Vhodný pro designéry, kteří chtějí vytvářet UI bez nutnosti programování

![Tempolabs AI](/assets/tempolabs-progressor.png)

#### Bolt New přehledně

- Umožňuje vývoj full-stack webových aplikací přímo v prohlížeči
- Nabízí intuitivní uživatelské rozhraní pro snadné používání
- Poskytuje AI-řízené prompty pro usnadnění procesu kódování
- Vhodný i pro neprogramátory díky snadnému rozhraní a AI asistenci

![Bolt New](/assets/bolt-trumpboard.png)


### Cursor AI - AI vývojové prostředí jako samostatná aplikace 

[Cursor AI](https://www.cursor.com/) je samostatná aplikace ke stažení. Je to klasické IDE - tedy vývojové prostředí, opět vychází z Visual Studio Code. Její AI okno budete chvíli hledat (neprozradím, hledejte!) - pak už funguje podobně, jako Tempolabs, jen pro vlastní ladění si musíte spustit server na svém počítači. Cursor řekne, jak na to, ale je s tím trocha času trápení navíc. Cursor také narozdíl od Tempa nemá žádnou podstatnou podporu vývoje designu, když se netrefí do toho, co chcete, tak máte smůlu a musíte si rovnou sáhnout do kódu. 

Zmatečná jsou dvě okna pro AI, jedno se jmenuje Chat a druhé Composer. V Chatu byste měli jen teoreticky probírat věci kolem aplikace, Composer už slouží k zadávání pokynů pro vývoj kódu, ale není to přesně rozlišené a je to matoucí. Navíc si v okně Composer můžete aktivovat Agenta, který vám pomůže kód odladit tím, že si z konzole přebírá chybové výstupy, ale nefunguje to vždy. 

[Cursor AI](https://www.cursor.com/) je vhodný v případě, že už něco malého o vývoji software víte a tedy chápete, jak by mohlo probíhat ladění. Nejsou to rozsáhlé požadavky, ale pokud máte k počítačům odstup, už pro vás Cursor AI nebude. 

Pro takové ty hobby programátory je naopak skvělý tím, že umožňuje vytvořit Cursor Rule - tedy soubory, které popisují vše důležité kolem vašeho projektu, například způsob, jakým má být formátován zdrojový kód nebo si zde můžete uložit popisy API, ke kterým má program přistupovat a Cursor je použije. Stejně tak sem můžete popsat designové zásady atd. 

Také Cursor se umí navázat na Github a obecně se s ním pracuje velmi dobře. Samostatný klient má své výhody a nevýhody, oproti Tempo především musíte instalovat podporu pro běh programů, které vyvíjíte, ale zase můžete rychleji testovat na lokálním disku. 

Cenová politika je také komplikovaná: za 20 dolarů měsíčně získáte 500 rychlých dotazů a bez omezení ty pomalejší. Rychlé dotazy jsou Claude Sonnet 3.5, tedy ten, který velmi dobře funguje, zdarma je třeba model o3, který funguje pro programování významně hůře. Můžete si vybrat i jiné modely, dokonce pracovat přes vlastní API klíč. Za 20 dolarů měsíčně dostanete 10 milionů tokenů a můžete programovat. A jak se Bolt liší od Tempo? Bolt New se více soustředí na komplexní vývojové prostředí, zatímco Tempolabs AI klade důraz na vizuální aspekty a rychlé prototypování. Tempo například umí integrovat Figma prototypy, oba již umí pracovat se SQL databází Supabase, oba jsou v prudkém procesu vývoje, takže každý týden přidávají nějakou novou funkci. Osobně jsem si více sednul s Tempo, protože se přímo napojuje na Github, který je součástí mého pracovního worflow, ale to může mít Bolt záhy taky. 

#### Cursor AI přehledně

- Vyniká v kontextovém porozumění kódu a adaptivní asistenci
- Nabízí intuitivní rozhraní s rychlou odezvou.
- Umožňuje snadné úpravy kódu pomocí přirozeného jazyka
- Pro neprogramátory může být výhodou možnost editace kódu bez přímého zásahu do zdrojového kódu

![Cursor AI](/assets/cursor-ai-odpady.png)

### Windsurf AI

[Windsurf AI](https://codeium.com/windsurf) jsem osobně nezkoušel. Má to být variantou na  Cursor AI, jde tedy o samostatný software. Umožňuje spolupráci více lidí a je také zaměřený na kód. Sada funkcí mezi Cursor AI a Windsurf AI se úplně nepřekrývá, můžete si je oba porovnat, jak vám který sedne.  Pozornosti se v poslední době dostává právě především Cursoru a ten se prudce vyvíjí, takže pokud sáhnete po Cursoru, neměli byste sáhnout vedle. 

### Jak dál s vibe coding?

Pro programování s AI se začíná razit pojem Vibe Coding - to jen tak na okraj. Teď je úžasná chvíle, kdy začít. Zkuste si vyvinout malou aplikaci, tím dostanete do rukou nákladovou stránku věci, protože účtování podle tokenů není zrovna snadno pochopitelné. Obecně vzato se vám totiž účtují slova, která se odešlou do umělé inteligence a zase se z ní přijmou. Jenže to by bylo snadné, vaše zadání má pár slov, i ten zdrojový kód není moc dlouhá. Ve skutečnosti se ale posílají neustále tam a zpět nejrůznější související kódy jako zdrojáky, které by měla AI vidět, když hledá chybu, pak taky nejrůznější ladící výstupy atd. Milion tokenů je rychle v čudu. 

Přesto byste do toho měli pár desítek dolarů investovat a vibe coding si vyzkoušet. Začněte s Tempo Labs - jejich nástroj je nejvíce přímočarný. Někdy příště si řekneme, jak s Tempo nejlépe začít.