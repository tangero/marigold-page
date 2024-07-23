---
title: Jak pomocí umělé inteligence nastudovat téma a napsat lepší článek do novin
author: Patrick Zandl
post_excerpt: "Řekl jsem si, že by mohlo být zajímavé v praxi ukázat, jak použít AI pro práci. Začneme psaním, to je moje přirozené prostředí. Krok za krokem si řekneme, jak AI využít k prozkoumání tématu, sehnání informací i výstavbě dobrého článku."
layout: post
categories: [AI, Umělá inteligence]
thumbnail: https://www.marigold.cz/assets/ai-noviny.jpg

---

Řekl jsem si, že by mohlo být zajímavé v praxi ukázat, jak použít AI pro práci. Začneme psaním, to je moje přirozené prostředí. 

Poznatek první: umělá inteligence za vás nenapíše lepší článek, alespoň prozatím ne. Zapomeňte na nástroje, které za vás automaticky napíšou další větu či odstavec. To je vážně okrajová funkce, kterou použijete jen v nejhlubším záseku, když už fakt nevíte, jak začít.  Umělá inteligence vám může pomoci od řady otravné práce. Můžete se významně rychleji dostat k lepšímu výsledku. Pojďme se na to podívat krok za krokem. 

Vezměme si praktický příklad. Máte napsat klasický novinářský článek, který čtenáře uvede do problému, do nějaké konkrétní debaty. Tak například teď v politice běží jako téma „slučování obcí“, čímž se mají uspořit podstatné peníze. 

Začneme domácími úkoly, kdy si prohledáte internet a načtete si články, co k tomu vyšly. Rychle zjistíte, že o tématu se vyjadřují cca tři osobnosti, zbytek jsou přemleté komentáře. Zapíšeme si, že pokud chceme citaci, ozveme se Elišce Olšákové (STAN), protože se k tomu vyjadřuje. Komentáře v médiích obecně říkají, že se ušetří, odvolávají se na selský rozum nebo odhad NERVu, že se ušetří deset miliard Kč. Vy ale nechcete dělat komentář, chcete dělat nezaujatý článek. Takže pokračujeme. 

Druhým krokem by mělo být dozvědět se další informace o tématu. Staré postupy (projít Wikipedii a vygooglované materiály) jsou stále funkční, ale už málo efektivní. Můj tajný tip vždy bylo jít na theses.cz a najít si vysokoškolskou práci na toto téma - je dobrým a podrobným kompendiem tématu.  

Jak si postavit kostru článku? Teď je správná chvíle obrátit se na AI - já použiju [Claude 3.5 Sonnet](https://www.claude.ai), stejně se můžete obrátit na [ChatGPT](https://chatgpt.com). Zadáváme prompt:

> Jakou strukturu by měl mít a jaké informace by měl obsahovat článek o územněsprávních reformách?
	
Dostáváme zhruba takovouto odpověď:

```Markdown
Článek o územněsprávních reformách by měl mít komplexní strukturu, která pokrývá všechny klíčové aspekty tématu. Zde je návrh struktury a obsahu takového článku:

1. Úvod
   - Definice územněsprávní reformy
   - Význam a aktuálnost tématu
   - Stručný přehled hlavních bodů článku

2. Historický kontext
   - Vývoj územněsprávního členění v dané zemi/regionu
   - Klíčové reformy v minulosti a jejich dopady

3. Cíle územněsprávních reforem
   - Ekonomická efektivita
   - Zlepšení poskytování služeb
   - Demokratizace a participace občanů
   - Vyrovnávání regionálních rozdílů

4. Typy územněsprávních reforem
   - Slučování obcí
   - Vytváření meziobecních svazků
   - Změny v uspořádání vyšších územních celků
   - Přesuny kompetencí mezi úrovněmi správy

5. Proces implementace reforem
   - Legislativní rámec
   - Fáze přípravy a plánování
   - Konzultace s občany a stakeholdery
   - Časový harmonogram implementace

6. Nástroje a pobídky pro reformy
   - Finanční pobídky
   - Legislativní změny
   - Dobrovolné vs. povinné reformy
   - Přechodná opatření

7. Případové studie
   - Konkrétní příklady reforem z různých zemí
   - Analýza úspěšných a neúspěšných případů

8. Dopady reforem
   - Ekonomické dopady (úspory, efektivita)
   - Sociální dopady (kvalita služeb, spokojenost občanů)
   - Politické dopady (změny v reprezentaci, volební účast)
   - Dlouhodobé vs. krátkodobé efekty

9. Výzvy a překážky
   - Odpor k změnám
   - Technické a administrativní problémy
   - Politické a kulturní faktory

... 

Tento článek by měl obsahovat aktuální data, příklady z praxe, a měl by být vyvážený, prezentující jak výhody, tak i potenciální rizika a nevýhody územněsprávních reforem. Je také důležité zahrnout různé perspektivy - od politiků přes odborníky až po občany.
```


Tady vidíte, že navržená struktura se hodí spíše pro disertační práci, než pro běžný novinový článek. Je to dáno tím, že volně dostupné studentské školní práce jsou častými vstupní tréninkovými daty pro AI. Buďto si s tím poradíte, nebo předefinujete prompt třeba následovně: 

>  Když by mělo jít o článek do magazínu o státní správě, přičemž je zde limit 6000 znaků a měl by být čtivý a zajímavý pro poučeného čtenáře zběhlého v české státní správě, jakou strukturu navrhuješ?

```Markdown
Pro článek do magazínu o státní správě s limitem 6000 znaků, zaměřený na poučeného čtenáře zběhlého v české státní správě, bych navrhl následující strukturu:

1. Úvod (cca 500 znaků)
   - Chytlavý úvod s aktuálním kontextem územněsprávních reforem
   - Stručné nastínění hlavní teze článku

2. Historický exkurz a současný stav (cca 1000 znaků)
   - Krátký přehled klíčových reforem v ČR
   - Současná situace a aktuální výzvy

3. Mezinárodní srovnání - dva až tři zajímavé příklady (cca 1500 znaků)
   - Výběr relevantních zahraničních příkladů (např. Dánsko, Francie)
   - Stručná analýza jejich úspěchů a neúspěchů

4. Klíčové aspekty úspěšných reforem (cca 1500 znaků)
   - Ekonomické faktory
   - Politické a sociální aspekty
   - Inovativní přístupy (např. meziobecní spolupráce, digitalizace)

5. Aplikace na český kontext (cca 1000 znaků)
   - Možnosti a výzvy pro ČR
   - Konkrétní doporučení nebo návrhy

6. Závěr a výhled do budoucna (cca 500 znaků)
   - Shrnutí hlavních myšlenek
   - Podnět k zamyšlení nebo diskusi

Tipy pro zvýšení čtivosti a zajímavosti:

1. Použijte konkrétní příklady a případové studie
2. Vložte 1-2 grafické prvky (infografika, mapa) pro vizuální atraktivitu
3. Použijte podnadpisy pro lepší orientaci v textu
4. Vložte citáty odborníků nebo zajímavé statistiky
5. Zakončete článek otevřenou otázkou nebo výzvou k dalšímu přemýšlení

Tento formát umožní pokrýt klíčové aspekty tématu, přičemž zůstane dostatečně stručný a zajímavý pro cílovou skupinu čtenářů. Důraz by měl být kladen na relevanci pro českou státní správu a na praktické implikace diskutovaných reforem.

```

Dostali jsme velmi dobrou radu, kterou je možné rovnou využít. Nyní je nutné jednotlivé části osnovy začít zahušťovat článkem. I pokud jste studovali politologii či veřejnou správu, asi si nevybavujete detaily územněprávních reforem, přitom by bylo skutečně dobré malou historickou douškou článek otevřít. Nechme opět pracovat AI a zadejme jí tento prompt, přičemž připomínám, že všechny prompty dávám do jednoho chat okna, aby AI držela kontext povídání:

> Udělej mi krátký přehled klíčových územněprávních reforem v České republice, ČSSR a Rakousko-Uhersku se vztahem k tématu.
	
Prompt dává hezký průřez územněprávními reformami, z něhož je patrné, že k našemu tématu je relevantní zavedení střediskových obcí v šedesátých letech a naopak v roce 1990 obnovení obecní samosprávy. Dalším promptem se můžete ponořit hlouběji, například článek obohatit tím, jak byly změny vnímány veřejností. 

Přejděme k části mezinárodního srovnání. Pravděpodobně máte nulovou představu o tom, jak územněprávní reforma proběhla v Dánsku a Francii, takže do toho promptem:

> Jak probíhala územní reforma v Dánsku?

Dostane se vám bodového vysvětlení s tím, že dánská reforma měla dvě hlavní období, rok 1970 a rok 2007. S tím je dobré se obrátit na Wikipedii, ale to by zase bylo dobré vědět, jak se tyto reformy jmenovaly. Prompt?

> Jak se územní reforma v Dánsku roku 1970 a 2007 jmenovala?
	
Dozvíte se, že reforma z roku 1970 se jmenuje [Kommunalreformen af 1970](https://da.wikipedia.org/wiki/Kommunalreformen_(1970)) a ta z roku 2007 je [Strukturreformen](https://da.wikipedia.org/wiki/Strukturreformen). Tím snadno dohledáte dánské wiki stránky o těchto reformách a můžete je nastudovat. Je tu ale problém: Wiki nemá text v češtině a ten v angličtině je viditelně stručný. Pokud neumíte dánsky, doporučím instalovat prohlížeč Chrome a doinstalovat si plugin pro překladač Deepl - a zaplatit si jej. Stránka se vám okamžitě a luxusně čitelně přeloží, takže můžete dánské podklady nastudovat. Hned máte do svého článku několik zajímavých příkladů z dánské politiky! Podobně můžete postupovat pro Německo i Francii a jednotlivé přístupy zemí porovnat. 

Teď bychom se potřebovali dostat k nějakému nezávislému zhodnocení oněch reforem. Ideální by bylo získat studii. Takže promptujme: 

> Vypiš mi studie vyhodnocující územní reformy v Dánsku v roce 1970 a 2007. Napiš jména autorů, stručné shrnutí studie a stručnou charakteristiku autorů studie. 

Tento prompt rozšiřujeme o informace o autorech studií, protože se dá očekávat, že je nebudeme znát a bylo by rozumné orientovat se po renomovaných autorech. Claude nám vypíše několik studií, nejvíce se opakuje jméno Jens Blom-Hansen, takže poprosíme Claude o jeho další studie a z vyhledávání vidíme, že jde o renomovaného a plodného autora v oblasti veřejné správy a politologie, se zaměřením na místní samosprávu, fiskální politiku a reformy veřejného sektoru. 

Snadno si vyhledáme vyhledávačem navrhované studie tak, že do vyhledávání dáme jejich jméno. Hloupé je, že některé studie nejsou veřejně přístupné, je z nich vidět jen abstrakt, ale najdeme dostatek veřejně přístupných, které si můžeme stáhnout jako PDF. 

Teď byste si měli studie důkladně pročíst, tak za týden s tím budete hotovi. Nebo ne?  My použijeme sympatickou funkci AI Claude, do níž můžete nahrát i dlouhý text článku či celé studie. A pak se můžeme bavit o studiích. Nahrajte do Claude získané studie a promptujte třeba takto:

> Udělej mi shrnutí a vypiš závěry z dokumentu Den_danske_kommunal-_og_strukturreform_2007_Rigsar.pdf

Nyní si můžete projít shrnutí i závěry jednotlivých dokumentů a zeptat se na to, co vám není jasné. Dejte si ale velký pozor na halucinace AI, je dobré se přeptat, zda vám AI odpovídá podle zadaných dokumentů, nebo si odpověď domýšlí z jiných kontextů. Někdy vám totiž dá třeba i správnou odpověď, která ale v dokumentu není obsažena. 

Takovýmto způsobem můžete za desítky minut projít celou řadu studií a zjistíte, že klíčová zásada, pro kterou se navrhuje česká reforma počtu obcí, tedy úspora, není ve studiích vůbec prokázána. To je zajímavý závěr, je dobré si jej nechat trochu rozvést, takže promptujme:

> Jaké jsou důvody podle přiložené studie, že při územních reformách nebylo dosaženo úspor?

A dostaneme obsáhlou odpověď vypisující řadu dobrých důvodů. Krátce si je pročtěte a zjistíte, že tím hlavním je, že slučování bylo dobrovolné, stát při něm žádnou úsporu nevyžadoval, jinak by ani neproběhlo a že obce ušetřené prostředky investovaly do kvality svých nejrůznějších služeb. Pomocí promptu se můžete doptat na příklady, ty si ještě dohledat, zpravidla k nim bývají v lokálním jazyce články na webu, opět pomůže Deepl. 

Ještě se pro jistotu můžete přeptat, jestli nejsou studie, které úspory identifikovaly:

> Jsou nějaké studie, které identifikovaly úspory takové reformy?

Na závěr se můžete zeptat, jaké postupy při slučování obcí jsou tedy doporučené. A také třeba ```Jsou nějaké jiné zkušenosti s alternativami ke slučováním obcí? Jaké konkrétní?```

Claude vám nabídne některé alternativní postupy, jako je meziobecní spolupráce, metodická podpora obcí nebo přesun složitějších úkonů na centrální vládu a apeluje na dobrovolné slučování motivované finančními pobídkami. 

Podobně si můžete s AI urovnat myšlenky na všechny zbývající části článku. Nakonec, když už článek máte hotový, lze jej opět nahrát do Claude a promptovat: ```Můžeš se podívat na tento článek a říct mi, co si o něm myslíš? Chybí v něm něco, je dobře čitelný, srozumitelný a informačně vyvážený?```

Nahrávám svůj článek a dostávám hodnocení:

```
Tento článek poskytuje komplexní pohled na téma slučování obcí, zejména v kontextu České republiky a s porovnáním se zahraničními zkušenostmi. Zde jsou mé postřehy:

1. Čitelnost a srozumitelnost:
   - Článek je dobře strukturovaný a logicky členěný.
   - Používá srozumitelný jazyk a vysvětluje odborné termíny.
   - Obsahuje konkrétní příklady a čísla, což pomáhá čtenáři lépe pochopit problematiku.

2. Informační vyváženost:
   - Článek prezentuje jak argumenty pro slučování obcí, tak i proti němu.
   - Uvádí zkušenosti z různých zemí (Dánsko, Německo, Francie), což poskytuje širší perspektivu.
   - Zmiňuje jak očekávané přínosy, tak i potenciální rizika a problémy.

3. Obsah:
   - Článek pokrývá širokou škálu aspektů: ekonomické důvody, politické dopady, sociální aspekty.
   - Poskytuje historický kontext reforem v jiných zemích.
   - Nabízí alternativní řešení k úplnému slučování obcí.

4. Co by mohlo být doplněno nebo vylepšeno:
   - Více konkrétních dat o situaci v ČR, například srovnání efektivity malých a velkých obcí.
   - Hlubší analýza právních aspektů slučování obcí v českém kontextu.
   - Více informací o názorech a postojích českých občanů a politiků k této otázce.
   - Případová studie úspěšného (nebo neúspěšného) sloučení obcí v ČR, pokud taková existuje.

Celkově hodnotím článek jako informativní, vyvážený a dobře zpracovaný. Poskytuje čtenáři dobrý přehled o problematice a podněcuje k dalšímu zamyšlení nad tématem.
```

Má pravdu. Porovnání efektivity vyřeším tím, že přidávám link. Hlubší analýzu právních aspektů slučování obcí kvůli rozsahu i očekávanému čtenářstvu nedávám a názory občanů i politiků také ne. 

Tak a je to. Pomocí AI jsme provedli poměrně obsáhlý průzkum, který nám pomohl se nejenom obsáhle zorientovat v tématu jak v českém kontextu, tak i celosvětově. Prošli jsme si zajímavé příklady ze zahraničí, prostudovali studie. AI v našem případě pomáhala se strukturou článku, s jeho vyvážeností, se zdroji dat, samotný článek jsme si napsali sami, svými slovy, svým pohledem. 

> [!TIP]
> Tipy na závěr: 
> - Předplatné za AI (ať již Claude nebo ChatGPT) je nutností
> - předplatné Deeplu taky, je výrazně lepší. Budete potřebovat ještě plugin, nejlepší je do Chrome, pak Firefox a Edge, pro Safari jsou jen horší pluginy třetích stran. 
> - pro analýzu textů a studií je dobré vytvořit v Claude Projekt a do něj všechny soubory nahrát. Odpovědi pak déle trvají, ale využívají i podklady v souborech. 
> - pokud nepoužíváte Claude, zkuste ChatPDF - pro práci se soubory není ChatGPT tak dobrý. 
> - dávejte si pozor a údaje si namátkově ověřujte, protože AI vás může neúmyslně zmást. 