---
audio_url: http://www.marigold.cz/audio/2024-07-14-jak-programovat-s-ai.mp3
author: Patrick Zandl
categories:
- AI
- "Umělá inteligence"
layout: post
post_excerpt: "S umělou inteligencí se programování stalo dostupným  i lidem, kteří programovat neumí. V tomto článku se podíváme na to, jak vyvíjet aplikace s pomocí AI, když sami programovat neumíte."
thumbnail: https://www.marigold.cz/assets/prgramovani-s-ai.png
title: "Návod na programování s AI, když programovat neumíte"
---

  
  

Minule jsme si řekli, [jak pomocí umělé inteligence psát lepší články, zprávy a texty](/item/jak-psat-clanky-s-pomoci-umele-inteligence-ai/). AI změnila ještě další věc. Najednou mohou programovat i neprogramátoři. A na to se dnes podíváme. Článek tedy není určen pro programátory ke zvyšování jejich produktivity, ale neprogramátorům, kteří občas potřebují vytvořit nějaký program.

  

Programování má oproti mnoha jiným tvůrčím postupům zásadní nevýhodu: něco o tom musíte vědět. Pokud si otevřete vývojové prostředí, musíte tušit, jak za sebe skládat příkazy a dokud to neuděláte správně, nic nefunguje. Když budete chtít psát nebo kreslit, tak možná nenapíšete nebo nenakreslíte nic extra hezkého, ale nějak to bude fungovat. U programování ne - buďto víte, jak na to, nebo neuděláte ani prd.

  

To ale AI mění. Pokud si předplácíte ChatGPT nebo Claude, můžete nechat umělou inteligenci vytvořit za vás i velmi rozsáhlé programy. Začít je samozřejmě lepší drobnějšími scripty a trochu se s celou věcí seznámit.

  

Pojďme se podívat, jak na to.

  

**Za prvé je potřeba si ujasnit, co chcete vytvořit.** Rozhodně nepředpokládejte, že vám AI vygeneruje na jeden prompt weby rozsahu Facebooku. To za prvé. Za druhé je dobré něco o vývoji a provozu webů vědět, samozřejmě čím více, tím lépe, ale každý základ se hodí. Za třetí, uvažujte o AI jako o zkušenějším kolegovi, po kterém můžete ledasco chtít, ale musíte mu to dobře vysvětlit.

  

Proces tvorby programu s AI je proces iterativní. Máte vstup - tedy základní východisko a podmínky, z nichž se vychází. Pak máte výstup - tedy to, co chcete dostat a jak to má vypadat. A mezi tím je ta magie, který bývá laikům ukradená a kterou teď doufáme, že pořeší umělá inteligence.

  

Vezmeme si nějaký příklad. Například já používám pro logování projektů systém, kdy si napíšu, co jsem udělal a za to s hashem název projektu či práce. Například “Objednám nový server #marigold". To si píšu do Excelu. Nově chci mít webovou službu, kam si za prvé toto poznamenám, za druhé si mohu všechny tyto poznámky vypsat. Je to relativně jednoduchá aplikace pro náš příklad programování s AI.

  

**Takže si ujasněme zadání pro tuto aplikaci:**

- data se zadávají přes webový formulář ve formátu libovolného krátkého textu a mohou obsahovat hashtag, tedy slovo začínající znakem #

- tato data lze vypisovat podle data a také výpis omezit na určitý hashtag

- jelikož jde o web službu přístupnou z internetu, bude vhodné data zpřístupnit jen přihlášenému uživateli

  

A to je vlastně celé zadání našeho projektu. Záměrně oškubané, což by mi zkušený projekťák oprávněně vytknul, ale později si ukážeme, proč.

  

Předpokládejme, že si platíte ChatGPT, ale postup bude podobný i pro jiné nástroje jako Claude. V ChatGPT ovšem máte výhodu, můžete použít GPT. Najděte v sekci Prozkoumat GPT nástroj nazvaný [*Code Copilot*](https://chatgpt.com/g/g-5qFFjp0bP-code-copilot), to je skvěle přizpůsobený nástroj pro podporu programování. Vložme zhruba tento prompt:

  

> Ahoj, potřebuji vytvořit webovou aplikaci. Aplikace by měla umožnit registraci a přihlášení uživatele. Přihlášený uživatel může do textového vstupního pole zadat text, který se uloží. Ukládá se včetně data a času zadání. Další stránka umožňuje vypsat všechny zadané texty vevolitelnem časovém rozmezí a třídit je podle hashtagu. Další stránka vygeneruje cloud hashtagů včetně četnosti použití. Očekávám, že služba bude málo využívaná. Jaký programovací jazyk a postup považuješ pro toto zadání za nejvhodnější? Rád bych, aby vznikl čitelný kód a pomohl jsi mi vybrat hosting, kde budu moci jednoduše tento kód nasazovat, vše bude čitelné a pochopitelné pro začátečníka. Rád bych, aby hosting byl zdarma, případně placený dle četnosti použití. Nejdříve mi udělej souhrn tvých doporučení pro programovací jazyk a pro hosting, popiš mi výhody a nevýhody.

Code Copilot (CC) nabídne, abyste řešení realizovali v Pythonu, pro backend použili framework Flask a Jinja2 pro frontend. Tady se hodí, když víte, o co zhruba jde, my si to vysvětlovat nebudeme.

  

> ### Doporučení pro programovací jazyk a framework
> 
>   
> 
> **Jazyk:** Python
> 
> **Framework:** Flask (pro backend) a Jinja2 (pro frontend šablony)
> 
>   
> 
> #### Výhody:
> 
> -  **Jednoduchost:** Python je jazyk známý svou čitelností a snadným učením, což je ideální pro začátečníky.
> 
> -  **Flask:** Je lehký webový framework, který je jednoduchý na použití, umožňuje rychlé prototypování a poskytuje flexibilitu při
> vytváření aplikace. Flask je velmi dobře dokumentovaný, což usnadňuje
> vývoj a řešení problémů.
> 
> -  **Široká podpora:** Python a Flask mají velkou komunitu a množství knihoven, které mohou zjednodušit práci (například pro správu
> uživatelů, práci s databázemi, nebo generování grafů a cloudů slov).
> 
> -  **Flexibilita:** Flask je velmi modulární, což umožňuje snadnou integraci s různými databázemi (např. SQLite pro jednoduché nasazení)
> a front-end frameworky.
> 
> -  **Učitelnost:** Python má jednoduchou a čitelnou syntax, což z něj činí skvělou volbu pro výuku a pochopení webového vývoje.
> 
>   
> 
> #### Nevýhody:
> 
> -  **Výkon:** Flask není tak výkonný jako jiné plně vybavené frameworky, jako je Django nebo Node.js, ale pro málo využívanou
> službu by to neměl být problém.
> 
> -  **Méně funkcí:** Flask neposkytuje tolik vestavěných funkcí jako robustnější frameworky (např. Django), což znamená, že některé funkce
> budete muset implementovat sami.
> 
>   
> 
> ### Doporučení pro hosting
> 
>   
> 
> **Hostingová platforma:** Heroku
> 
>   
> 
> #### Výhody:
> 
> -  **Jednoduché nasazení:** Heroku nabízí snadné nasazení aplikací přímo z GitHubu nebo přes příkazový řádek, což je vhodné pro
> začátečníky.
> 
> -  **Zdarma:** Heroku nabízí bezplatný plán, který je vhodný pro malé a málo využívané aplikace. Placené plány jsou dostupné pro větší
> škálování.
> 
> -  **Podpora pro Python:** Heroku má vestavěnou podporu pro Python a Flask aplikace, což umožňuje snadnou integraci a nasazení.
> 
> -  **Databáze:** Heroku nabízí integrovanou podporu pro PostgreSQL databáze, což vám poskytuje škálovatelnou a spolehlivou databázi přímo
> na platformě.
> 
>   
> 
> #### Nevýhody:
> 
> -  **Omezené zdroje na bezplatném plánu:** Bezplatný plán Heroku má omezení v počtu hodin spuštění aplikace za měsíc a nemusí být vhodný
> pro aplikace s vysokým provozem nebo velkou databází.
> 
> -  **Spouštění po nečinnosti:** Aplikace nasazené na bezplatném plánu mohou po nečinnosti usnout a po opětovném spuštění mohou mít pomalejší
> odezvu.
> 
>   
> 
> ### Alternativní možnosti
> 
>   
> 
> -  **Vercel nebo Netlify:** Tyto platformy jsou zaměřené hlavně na front-end, ale mohou být použity i pro full-stack aplikace pomocí
> serverless funkcí. Jsou rovněž velmi přátelské k začátečníkům a mají
> bezplatné plány.
> 
> -  **Render:** Alternativa k Heroku, která nabízí podobné možnosti nasazení s jednoduchým uživatelským rozhraním a bezplatnými plány.
> 
>   
> 
> ### Souhrn
> 
>   
> 
> Doporučuji použít Python s Flaskem pro vývoj vaší webové aplikace.
> Tento přístup vám poskytne čitelný a flexibilní kód, který je snadno
> pochopitelný pro začátečníky. Pro hosting bych doporučil Heroku,
> protože nabízí jednoduché nasazení a bezplatný plán vhodný pro menší
> projekty.
> 
>   
> 
> **a.** Chcete pokračovat s implementací backendu aplikace pomocí Flasku?
> 
> **b.** Mám vám pomoci nastavit projekt a připravit kód pro základní funkčnost, jako je registrace uživatelů a ukládání textů?

CC také doporučí platformy pro hostování Pythonu, navrhuje použít Heroku, alternativně Vercel, Netlify nebo Render, všechno jsou velmi validní volby. Ale jak to, že nám neodporučil třeba Amazon AWS nebo MS Azure, když na ně všude jsou reklamy? Zeptejme se:

  

> Proč jsi mi nedoporučil AWS, Azure nebo Google Cloud?

CC odpovídá, že jde o velmi komplexní platformy, které bude pro začátečníka obtížné nastavit. Heroku, Vercel, a podobné platformy jsou zaměřené na jednoduchost a uživatelskou přívětivost, což je vhodné pro projekty s nižšími nároky a pro uživatele, kteří nechtějí řešit složitou konfiguraci. Což mohu potvrdit, nastavit AWS / Azure je pro začátečníka zdlouhavé. Mimochodem, Claude tuto výhradu poskytla hned na ten první prompt. To, že jsme začátečníci, jsme AI poskytli v úvodním promptu a ihned jsme si definovali, že pro nás jednoduchost nasazování bude důležitá.

  

Ještě se můžeme doptat, jak je to s hostingy v Česku (dostávám doporučení na Active 24, Wedos a Stable, vše relevantní) - ale správně mi AI připomíná, že bych se v takovém případě měl orientovat na virtuální privátní server, který je cenově nákladnější a už si vyžaduje zkušenosti s administrací.

  

Dejme tedy na první dopoučení a pojďme si ujasnit, jaký bude další pracovní postup, abychom si všechno nastavili:

  

> Jaké by jsi mi doporučil pracovní workflow pro vývoj této mojí aplikace? Použiji tedy python a Heroku a můj počítač používá MacOS.

CC i Claude nám vcelku shodně (s rozdílnou mírou detailu) radí, jak dále postupovat.  Nejprve bychom si měli rozchodit lokální vývojové prostředí, tedy instalovat Python, Flask a nějaký editor zdrojového kódu - doporučuje se nám přímo co a jak. To je ten důvod, proč jsme do promptu uvedli, z jakého operačního systému budeme pracovat. AI nám nyní přímo nabízí příkazy pro příkazovou řádku nebo software vhodný pro tento operační systém (odpověď je tentokráte z Claude).

> Pro vývoj vaší aplikace v Pythonu s nasazením na Heroku a s použitím
> macOS bych doporučil následující workflow:
> 
> 1. Nastavení vývojového prostředí:
>    - Nainstalujte Python (pokud již nemáte): Použijte Homebrew nebo stáhněte z python.org
>    - Nainstalujte Git pro správu verzí
>    - Nainstalujte editor kódu (např. Visual Studio Code nebo PyCharm)
> 
> 2. Vytvoření projektu:
>    - Vytvořte nový adresář pro projekt
>    - Inicializujte Git repozitář: `git init`
>    - Vytvořte virtuální prostředí: `python -m venv venv`
>    - Aktivujte virtuální prostředí: `source venv/bin/activate`
> 
> 3. Nastavení Flask aplikace:
>    - Nainstalujte Flask: `pip install flask`
>    - Vytvořte požadavky: `pip freeze > requirements.txt`
>    - Vytvořte základní strukturu Flask aplikace
> 
> 4. Vývoj:
>    - Pracujte na funkcionalitách postupně
>    - Používejte Git pro průběžné ukládání změn:
>      ```
>      git add .
>      git commit -m "Popis změn"
>      ```
>    - Testujte lokálně: `flask run`
> 
> 5. Nasazení na Heroku:
>    - Nainstalujte Heroku CLI: `brew tap heroku/brew && brew install heroku`
>    - Přihlaste se k Heroku: `heroku login`
>    - Vytvořte Heroku aplikaci: `heroku create nazev-aplikace`
>    - Vytvořte Procfile pro Heroku
>    - Nasaďte aplikaci: `git push heroku main`
> 
> 6. Kontinuální vývoj a nasazování:
>    - Pokračujte ve vývoji lokálně
>    - Testujte změny
>    - Commitujte změny do Gitu
>    - Nasazujte na Heroku: `git push heroku main`
> 
> 7. Monitorování a ladění:
>    - Sledujte logy: `heroku logs --tail`
>    - Používejte Heroku dashboard pro monitoring
> 
> Doporučuji také:
> - Používejte `.gitignore` soubor pro vyloučení nepotřebných souborů z Gitu
> - Zvažte použití nástrojů pro automatické formátování kódu (např. Black)
> - Implementujte unit testy pro klíčové funkce
> 
> Chcete, abych vám ukázal, jak začít s tímto workflow vytvořením
> základní struktury projektu?

  

Pokud něčemu nerozumíme, můžeme se AI rovnou zeptat. Třeba:

  

> Jak si na MacOS nainstaluji Git pro správu verzí?​​​​​​​​​​​​​​​​

  

A dostane se mi potřebných detailů.

  

Po nějaké době, kdy následujeme pokyny AI bychom měli být docela slušně vybaveni. Máme lokální vývojové prostředí, takže aplikaci můžeme vyvíjet a testovat přímo na svém počítači. Máme rozchozený verzovací systém, takže máme dobrou kontrolu nad tím, jak kód vytváříme a můžeme jej ve vhodnou chvíli nasadit “na produkci” - čili poslat na Heroku a tam jej zviditelnit do světa.

  

Teď už jsme si ujasnili, co chceme a jak budeme postupovat. V tomto okamžiku je důležité “kontextové okno”, tedy fakt, že moderní LLM modely udrží v paměti dluhé texty předchozí konverzace. Díky tomu už můžeme zadat jen jednoduchý prompt k tomu, aby nám AI vygenerovala aplikaci tak, jak jsme si ji navrhli:

  

> Vytvoř mi zdrojový kód aplikace a detailně pro začátečníka popiš, co kde mám nastavit a kam uložit, aby kód při nasazení fungoval.

AI nyní popíše strukturu souborů, tedy kam co máte uložit a pak vám vypíše obsahy těch souborů. Teď přichází zdlouhavá klikací chvíle, kdy musíte pomocí Copy&Paste přenést texty (nejlépe přes to nainstalované vývojové prostředí) do vašeho počítače a naukládat je tam, kde máte adresář projektu v GITu. A teď přichází chvíle, kdy si aplikaci můžete otestovat na lokálním počítači. Jenže, jak? Zeptejme se AI:

  

> Jak aplikaci otestuji na mém lokálním počítači používajícím MacOS?

Dostanete popis, jak aplikaci otestovat ve svém prostředí a počítači. Velmi snadno se stane, že první spuštění aplikace z nějakého důvodu neproběhne. V tom případě se na konzoli objeví chybová hláška. Tu zkopírujte a promptujte:

  

> Dostal jsem toto chybové hlášení: a copy&paste text chyby či výpis z logu

V tomhle je AI dost flexibilní, můžete jí zkopírovat i velmi dlouhý chybový log a ona se zorientuje. Vysvětlí vám, kde došlo k chybě a navrhne úpravu, kterou musíte provést.

  

Až aplikaci odladíte, nasadíte ji na Heroku a opět vyzkoušíte, i zde může dojít k chybám. Opět chybový log konzultujete s AI.

  

Asi už vidíte, kde je hlavní problém. Neustálé kopírování zdrojového kódu z odpovědi AI do vývojového prostředí. Naštěstí většina AI vám kód hezky naformátuje a nabídne tlačítko pro jednoduché přenesení textu do clipboardu, ale stejně je to opruz. Bylo by lepší, kdyby AI uměla tento výstup rovnou napojit třeba na Github či do vašeho GITu, ale to zatím nejde, musíte každý soubor jeden po druhém ukládat.

  

> Tipy:
>  - Někdy vám AI doporučí udělat konkrétní opravu v kódu, například jen přepsat kus funkce. Pokud to v kódu zvládnete najít, udělejte to, pokud ne, řekněte jí, ať vám dá celý opravený kód. Jindy zase podlehnete pokušení v kódu něco opravit sami, třeba texty - v takovém případě to AI řekněte, protože až bude příště opravovat kód, o vašich úpravách by nevěděla.
>  - Pokud něčemu nerozumíte, nechte si to od AI vysvětlit, zeptejte se.

  

Jak vidíte, postup není na první pohled zcela vhodný pro vývoj rozsáhlých aplikací. 

Jak byste měli postupovat dále s rozvojem vaší aplikace? Zpřesňovat a rozšiřovat zadání. Tak například si můžete přát, aby aplikace doplnila stránku, na níž budou vypsané hashtagy podle četnosti použití. Můžete si přát doplnit vzhled aplikace o Material UI společnosti Google nebo cokoliv jiného. Ale je to krok za krokem. Nechtějte v jednom úkolu změnit jak UI, tak přidat novou stránku. Nejdříve jedno, pak druhé. 

V jednu chvíli se vám také může stát, že přesáhnete kontextové okno a AI vám z úlohy vyloučí něco, co jste již dříve měli vyřešené, nebo to vyřeší znova a jinak. Například mi sice vytvoří CSS s definicí stylu, ale úpravy v HTML kódu mi nechá pro staré CSS. Tady se hodí zkušenost s programováním, kdy sami odhalíte podstatu chyby, znovu do AI nahrajete všechny dotčené soubory a necháte jej vše opravit. Takové Claude 3.5 má kontextové okno na cca 200 tisíc tokenů, 

Snadno se vám v Claude také může stát, že narazíte na limit dlouhých zadání a budete si muset odpočinout. Limit je v Claude závislý na zátěži a vašem tarifu, obecně mi třech-čtyřech hodinách aktivního "párového programování" dávám pauzičku 😇

Tímto přístupem můžete vytvořit i poměrně rozsáhlé aplikace, nebojte se to vyzkoušet!
