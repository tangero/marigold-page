---
audio_url: http://www.marigold.cz/audio/2024-07-14-jak-programovat-s-ai.mp3
author: Patrick Zandl
categories:
- AI
- "Um\u011Bl\xE1 inteligence"
hide: true
layout: post
post_excerpt: "S um\u011Blou inteligenc\xED se programov\xE1n\xED stalo dostupn\u011B\
  j\u0161\xEDm i lidem, kte\u0159\xED programovat neum\xED. V tomto \u010Dl\xE1nku\
  \ se pod\xEDv\xE1me na to, jak vyv\xEDjet aplikace s pomoc\xED AI, kdy\u017E sami\
  \ programovat neum\xEDte."
thumbnail: https://www.marigold.cz/assets/prgramovani-s-ai.png
title: "N\xE1vod na programov\xE1n\xED s AI, kdy\u017E programovat neum\xEDte"
---


Jak programovat s AI, když programovat neumíte

AI změnila ještě jednu věc. Najednou mohou programovat i neprogramátoři. A na to se dnes podíváme. Článek tedy není určen pro programátory ke zvyšování jejich produktivity, ale neprogramátorům, kteří občas potřebují vytvořit nějaký program. 

Programování má oproti mnoha jiným tvůrčím postupům zásadní nevýhodu: něco o tom musíte vědět. Pokud si otevřete vývojové prostředí, musíte tušit, jak za sebe skládat příkazy a dokud to neuděláte správně, nic nefunguje. Když budete chtít psát nebo kreslit, tak možná nenapíšete nebo nenakreslíte nic extra hezkého, ale nějak to bude fungovat. U programování ne - buďto víte, jak na to, nebo neuděláte ani prd. 

To ale AI mění. Pokud si předplácíte ChatGPT nebo Claude, můžete nechat umělou inteligenci vytvořit za vás i velmi rozsáhlé programy. Začít je samozřejmě lepší drobnějšími scripty a trochu se s celou věcí seznámit. 

Pojďme se podívat, jak na to.

Za prvé je potřeba si ujasnit, co chcete vytvořit. Rozhodně nepředpokládejte, že vám AI vygeneruje na jeden prompt weby rozsahu Facebooku. To za prvé. Za druhé je dobré něco o vývoji a provozu webů vědět, samozřejmě čím více, tím lépe, ale každý základ se hodí. Za třetí, uvažujte o AI jako o zkušenějším kolegovi, po kterém můžete ledasco chtít, ale musíte mu to dobře vysvětlit. 

Proces tvorby programu s AI je proces iterativní. Máte vstup - tedy základní východisko a podmínky, z nichž se vychází. Pak máte výstup - tedy to, co chcete dostat a jak to má vypadat. A mezi tím je ta magie, který bývá laikům ukradená a kterou teď doufáme, že pořeší umělá inteligence.

Vezmeme si nějaký úkol. Například já používám pro logování projektů systém, kdy si napíšu, co jsem udělal a za to s hashem název projektu či práce. Například “Objednán nový server #marigold#. A chci mít webovou službu, kam si za prvé toto poznamenám, za druhé si mohu všechny tyto poznámky vypsat. Je to  relativně jednoduchá aplikace pro náš příklad programování s AI. 

Za prvé si ujasníme, co chci:
- data se zadávají přes webový formulář ve formátu libovolného krátkého textu a mohou obsahovat hashtag, tedy slovo začínající znakem #
- tato data lze vypisovat podle data a také výpis omezit na určitý hashtag
- jelikož jde o web službu přístupnou z internetu, bude vhodné data zpřístupnit jen přihlášenému uživateli

A to je vlastně celé zadání našeho projektu. Záměrně oškubané, což by mi zkušený projekťák oprávněně vytknul, ale později si ukážeme, proč. 

Předpokládejme, že si platíte ChatGPT, ale postup bude podobný i pro jiné nástroje jako Claude. V ChatGPT ovšem máte výhodu, můžete použít GPT. Najděte v sekci Prozkoumat GPT nástroj nazvaný Code Copilot, to je skvěle přizpůsobený nástroj pro podporu programování. Vložme zhruba tento prompt:\

	Ahoj, potřebuji vytvořit webovou aplikaci. Aplikace by měla umožnit registraci a přihlášení uživatele. Přihlášený uživatel může do textového vstupního pole zadat text, který se uloží. Ukládá se včetně data a času zadání. Další stránka umožňuje vypsat všechny zadané texty vevolitelnem časovém rozmezí a třídit je podle hashtagu. Další stránka vygeneruje cloud hashtagů včetně četnosti použití. Očekávám, že služba bude málo využívaná. Jaký programovací jazyk a postup považuješ pro toto zadání za nejvhodnější? Rád bych, aby vznikl čitelný kód a pomohl jsi mi vybrat hosting, kde budu moci jednoduše tento kód nasazovat, vše bude čitelné a pochopitelné pro začátečníka. Rád bych, aby hosting byl zdarma, případně placený dle četnosti použití.  Nejdříve mi udělej souhrn tvých doporučení pro programovací jazyk a pro hosting, popiš mi výhody a nevýhody. 
	
Code Copilot (CC) nabídne, abyste řešení realizovali v Pythonu, pro backend použili framework Flask a Jinja2 pro frontend. Tady se hodí, když víte, o co zhruba jde, my si to vysvětlovat nebudeme. 

CC také doporučí platformy pro hostování Pythonu, navrhuje použít Heroku, alternativně Vercel, Netlify nebo Render, všechno jsou velmi validní volby. Ale jak to, že nám neodporučil třeba Amazon AWS nebo MS Azure, když na ně všude jsou reklamy? Zeptejme se:

	Proč jsi mi nedoporučil AWS, Azure nebo Google Cloud?
	
CC odpovídá, že jde o velmi komplexní platformy, které bude pro začátečníka obtížné nastavit. Heroku, Vercel, a podobné platformy jsou zaměřené na jednoduchost a uživatelskou přívětivost, což je vhodné pro projekty s nižšími nároky a pro uživatele, kteří nechtějí řešit složitou konfiguraci. Což mohu potvrdit, nastavit AWS / Azure je pro začátečníka zdlouhavé. Mimochodem, Claude tuto výhradu poskytla hned na ten první prompt. To, že jsme začátečníci, jsme AI poskytli v úvodním promptu a ihned jsme si definovali, že pro nás jednoduchost nasazování bude důležitá. 

Ještě se můžeme doptat, jak je to s hostingy v Česku (dostávám doporučení na Active 24, Wedos a Stable, vše relevantní) - ale správně mi AI připomíná, že bych se v takovém případě měl orientovat na virtuální privátní server, který je cenově nákladnější a už si vyžaduje zkušenosti s administrací. 

Dejme tedy na první dopoučení a pojďme si ujasnit, jaký bude další pracovní postup, abychom si všechno nastavili:

	Jaké by jsi mi doporučil pracovní workflow pro vývoj této mojí aplikace? Použiji tedy python a Heroku a můj počítač používá MacOS.
	
CC i Claude nám vcelku shodně (s rozdílnou mírou detailu) radí, jak dále postupovat. 
 
Nejprve bychom si měli rozchodit lokální vývojové prostředí, tedy instalovat Python, Flask a nějaký editor zdrojového kódu - doporučuje se nám přímo co a jak. To je ten důvod, proč jsme do promptu uvedli, z jakého operačního systému budeme pracovat. AI nám nyní přímo nabízí příkazy pro příkazovou řádku nebo software vhodný pro tento operační systém. 

Pokud něčemu nerozumíme, můžeme se AI rovnou zeptat. Třeba:

	Jak si na MacOS nainstaluji Git pro správu verzí?​​​​​​​​​​​​​​​​

A dostane se mi potřebných detailů. 

Po nějaké době, kdy následujeme pokyny AI bychom měli být docela slušně vybaveni. Máme lokální vývojové prostředí, takže aplikaci můžeme vyvíjet a testovat přímo na svém počítači. Máme rozchozený verzovací systém, takže máme dobrou kontrolu nad tím, jak kód vytváříme a můžeme jej ve vhodnou chvíli nasadit “na produkci” - čili poslat na Heroku a tam jej zviditelnit do světa. 

Teď už jsme si ujasnili, co chceme a jak budeme postupovat. V tomto okamžiku je důležité “kontextové okno”, tedy fakt, že moderní LLM modely udrží v paměti dluhé texty předchozí konverzace. Díky tomu už můžeme zadat jen jednoduchý prompt k tomu, aby nám AI vygenerovala aplikaci tak, jak jsme si ji navrhli:

	Vytvoř mi zdrojový kód aplikace a detailně pro začátečníka popiš, co kde mám nastavit a kam uložit, aby kód při nasazení fungoval. 
	
AI nyní popíše strukturu souborů, tedy kam co máte uložit a pak vám vypíše obsahy těch souborů. Teď přichází zdlouhavá klikací chvíle, kdy musíte pomocí Copy&Paste přenést texty (nejlépe přes to nainstalované vývojové prostředí) do vašeho počítače a naukládat je tam, kde máte adresář projektu v GITu. A teď přichází chvíle, kdy si aplikaci můžete otestovat na lokálním počítači. Jenže, jak? Zeptejme se AI:

	Jak aplikaci otestuji na mém lokálním počítači používajícím MacOS? 
	
Dostanete popis, jak aplikaci otestovat ve svém prostředí a počítači. Velmi snadno se stane, že první spuštění aplikace z nějakého důvodu neproběhne. V tom případě se na konzoli objeví chybová hláška. Tu zkopírujte a promptujte:

	Dostal jsem toto chybové hlášení: a copy&paste text chyby či výpis z logu
	
V tomhle je AI dost flexibilní, můžete jí zkopírovat i velmi dlouhý chybový log a ona se zorientuje. Vysvětlí vám, kde došlo k chybě a navrhne úpravu, kterou musíte provést. 

Až aplikaci odladíte, nasadíte ji na Heroku a opět vyzkoušíte, i zde může dojít k chybám. Opět chybový log konzultujete s AI. 

Asi už vidíte, kde je hlavní problém. Neustálé kopírování zdrojového kódu z odpovědi AI do vývojového prostředí. Naštěstí většina AI vám kód hezky naformátuje a nabídne tlačítko pro jednoduché přenesení textu do clipboardu, ale stejně je to opruz. Bylo by lepší, kdyby AI uměla tento výstup rovnou napojit třeba na Github či do vašeho GITu, ale to zatím nejde, musíte každý soubor jeden po druhém ukládat. 

Tipy:

Někdy vám AI doporučí udělat konkrétní opravu v kódu, například jen přepsat kus funkce. Pokud to v kódu zvládnete najít, udělejte to, pokud ne, řekněte jí, ať vám dá celý opravený kód. Jindy zase podlehnete pokušení v kódu něco opravit sami, třeba texty - v takovém případě to AI řekněte, protože až bude příště opravovat kód, o vašich úpravách by nevěděla. 

Pokud něčemu nerozumíte, nechte si to od AI vysvětlit, zeptejte se. 

Jak vidíte, postup není zcela vhodný pro vývoj rozsáhlých aplikací. 