---
ID: 2952
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/energomonitorovanky-stul-ze-dveri-a-sesti-prepravek

  '
post_date: 2014-09-26 13:56:24
post_excerpt: ''
published: true
summary_points:
- Energomonitor se přestěhoval do vily bývalého majitele skláren Salomona Reicha ve
  Valašském Meziříčí.
- Firma využívá nábytek z bývalého Českého Telecomu, který sloužil i pro rozjezd Stream.cz.
- Energomonitor řeší software, hardware a výrobu, přičemž detaily spotřebují nejvíce
  pracovních kapacit.
- Firma se účastní European Utility Week v Amsterodamu, kde představí svou expozici
  energetické veřejnosti.
title: 'Energomonitorovánky: stůl ze dveří a&nbsp;šesti přepravek plus další novinky'
---

<p>Energomonitor jsme ve Valašském Meziříčí přestěhovali. Z náměstí do vily bývalého majitele skláren Salomona Reicha. Jen tak mimochodem, ve Valmezu se dá ubytovat v Reichově vile, jenže to není ta opravdová, kde bydlel, jen ji myslím vlastnil - v té, kde bydlel, sídlí teď Energomonitor.</p>



<p>Do přízemí se nastěhovali kluci od krabiček, už se tam namontovala i antistatická podlaha, do patra zase programátoři. Součástí kouzla je nábytek. Původně jsme nezvládli převést všechny stoly a na poradu chyběl prostor, to kluci promptně nahradili dveřma posazenými na šest přepravek.</p>



<p>Současná nábytková výbava má za sebou také kus historie: nábytek si původně nakoupil Český Telecom, jenže ho zrovna přebrala Telefonica a vyhazovala lidi i stoly, takže jsme si je nakoupili a rozjížděli jsme na nich mimo jiné Stream.cz. </p>


<!--more--><p>No a pak ležely nějakou dobu ve skladu a teď se na nich rozjíždí Energomonitor. Na fotce je kávové zákoutí. Ještě jsme neměli zavedený internet, ale káva musela být. Lepší komitovat z domova či po mobilu, než nemít kafe… Mimochodem, stabilní připojení od Internextu by se mělo instalovat teprve tento týden, do té doby se jelo na provizorním rádiu. </p>

<p><img title="IMG_20140908_095552.jpg" src="http://www.marigold.cz/wp-content/uploads/IMG_20140908_095552.jpg" alt="Kavárenské zákoutí" width="600" height="338" border="0" /></p>

<p>Ve firmě je ke dvaceti lidem a kamarádi se občas ptají, co tam tolik lidí dělá. Český zvyk internetových firem o jednom až třech lidech je zjevně hodně zakotvený. No, své důvody to má. Kromě software na webu a na backendu se řeší také hardware a připravuje se jeho výroba, kromě toho se snažíme ten software promyslet a domyslet. Jenže právě ty detaily spotřebují nejvíce práce a spálí nejvíce lidských kapacit. A je snadné se na tom zadrhnout. Počátkem letošního roku jsme zvolili strategii, kdy se funkce dostrká do stádia, kdy je zhruba z poloviny tak ovladatelná a přítulná, jak bychom si představovali. Pak se potichu nasadí na server, kde si jí všimnou největší šťouralové a ozvou se. Na nich se otestuje, co zlepšit, mezi tím se dodělá verze na nějakých 70-80%, na kterou upozorňujeme i další zákazníky. Pak se zjistí, že běžným uživatelům to stejně moc nevyhovuje, takže nejsme na 80%, ale zpět na padesáti a předělává se to znovu. Do toho se zjistí, že takhle to v energetice nelze použít z nějakého zajímavého důvodu a jsme po dvou update zase na pouhých 50 % a iterace pokračují.</p>

<p>Takový jednoduchý příklad, abyste věděli, jak to funguje:<strong> sledování vyčerpání záloh za elektřinu.</strong> Za elektřinu se platí měsíční zálohy, které v ideálním případě v ročním součtu představují to, kolik byste za rok zaplatili. Pokud se netrefíte, vznikají přeplatky (to je lepší případ) nebo nedoplatky, kdy musíte doplatit nějakou částku. Asi by se tedy hodilo nebohému uživateli dávat na vědomí, že spotřebovává více elektřiny, než jak se při stanovení záloh počítalo a že pravděpodobně bude muset doplácet tolik a tolik. To by byla fajn služba pro uživatele, mohl by se na to připravit a nepřišla by mu jednorázová složenka na dvanáct litrů. Asi nějak takhle v podobě protypového wireframe:</p>

<p><img title="wireframe-zalohy.png" src="http://www.marigold.cz/wp-content/uploads/wireframe-zalohy.png" alt="Zálohy" width="523" height="163" border="0" /></p>

<p>Vezměme tedy naměřená data a vynásobíme je poměrnou dobou z ročního zúčtovacího období, získáme číslo, kolik bude zákazníka stát roční spotřeba. Tu porovnáme s jím zadanou výší záloh a upozorníme jej na rozdíl. Až potud je to jednoduchá úloha a takhle nějak jsme to měli v prvním prototypu (jen jako odhad roční spotřeby). Takhle nějak by to mohlo vypadat, jenomže z návrhu není moc patrné, jak je to se zbývající dobou, to byla nevýhoda tohoto prototypu:</p>

<p><img title="zalohy-energomonitor.png" src="http://www.marigold.cz/wp-content/uploads/zalohy-energomonitor.png" alt="Ukazatel záloh" width="600" height="175" border="0" /></p>

<p>Jenže se taky ukázalo, že rozdíly spotřeby elektřiny mezi jednotlivými měsíci jsou docela veliké, takže kdo se řídil podle odhadu spotřeby sestaveného v zimních měsících, ten se musel hodně vyděsit. Řešením je použít nějakou křivku, ta v energetice má dokonce jméno: typový diagram dodávky (TDD). A vypadá nějak takhle (hodnot na ose Y si nevšímejte).</p>

<p><img title="tdd.png" src="http://www.marigold.cz/wp-content/uploads/tdd.png" alt="typový diagram dodávky" width="600" height="286" border="0" /></p>

<p>Takže následovala další iterace úvah, kdy se zhruba následující křivka zahrnovala jako proměnná do spotřeby. Záhy se ukázalo, že TDD jsou napasované na tarif spotřeby, takže by bylo ze zákazníka ještě vhodné vytáhnout tarif, což jsme stejně chtěli, protože to se u elektřiny může hodit. Jenže TDD jsou konstruované někdy na přelomu 80. a 90. roku, takže odběrové diagramy zachytily nástup elektrického topení, ale nepobraly už trend klimatizací, které naopak jsou u našich klientů dost rozšířené. Zjednodušeně řečeno, klesá počet natopených dní a roste počet dochlazených dní.</p>

<p>Řešení bylo dvojí. Vytvořit vlastní typové diagramy založené na párování energetických profilů našich klientů, což by bylo nesmírně pracné a obecně tedy blbost. A za druhé, nějak to do pilotního provozu ofejkovat a doplnit nějakými hausnumerickými konstantami, které se pokusí z TDD křivky udělat něco použitelného, což vypadalo jako rozumný přístup.</p>

<p>V další iteraci testování se rychle ukázalo, že hausnumerické výsledky nejsou přesvědčivé a příliš často je uživatel konfrontován se špatným výsledkem. Nicméně jsme si říkali, že za tu cenu je to aspoň něco. A při testování pro energetického partnera se ukázalo, jakou cenu takové řešení má. Pramalou. Respondenti řvou, že je to buďto zbytečně děsí a mají tendenci volat na infolinku a řešit navyšování záloh, nebo řvou, že je to včas neupozorní, ačkoliv ten nedoplatek nakonec mají.</p>

<p><strong>Původně to byl jednoduchý úkol</strong>, u něhož zadání znělo: změř měsíční spotřebu, vynásob ji dvanácti, odečti od toho roční zálohy a číslo napiš uživateli. Co na tom můžou ti pablbové kutit tak dlouho, mohl by se zeptat náš zákazník.</p>

<p>No, teď se to změnilo v úkol: sleduj odběrovou křivku všech zákazníků a seskup je podle tvaru odběrové křivky. Snaž se křivku prodloužit na dvanáct měsíců podle zákazníků, kteří jsou již více měsíců s námi. Toto rozřazení do skupiny pravidelně kontroluj, opakuj a teprve nad tímto rozřazením prováděj dopočet na rok podle zprůměrované a očištěné odběrové křivky. Z toho zase vyplivni to samé jedno číslo a to napiš uživateli.</p>

<p><em>A teď mi řekněte, proč tam to jedno číslo nemáme, když je to vlastně tak jednoduché… </em></p>

<p>Na další fotce je Jirka, šéf projektů, který proměňuje náš flipchart se seznamem priorit na téměř interaktivní tabuli :)</p>

<p><img title="IMG_20140922_134850.jpg" src="http://www.marigold.cz/wp-content/uploads/IMG_20140922_134850.jpg" alt="Jirka fotí tabuli" width="600" height="338" border="0" /></p>

<p>Tož takovými věcmi se bavíme. Kromě toho se v listopadu účastníme největší oborové akce <a href="http://www.european-utility-week.com">European Utility Week</a> v Amsterodamu, pořídili jsme si tam mikrostáneček tři na čtyři metry (tři dny stojí tolik, jako roční nájem baráku ve Valmezu) a teď pilujeme, jak budeme vypadat. Zatím asi nejlepší návrh motivu expozice bohužel veletržní správa zamítla jako ilegální, takže budeme muset udělat něco konzervativnějšího, ale sami jsme vůbec zvědavi, co nám takový veletrh přinese. Je to odborný veletrh, orientovaný na lidi z energetiky a pro nás je to vlastně první masová ukázka odborné veřejnosti.</p>

<p>Tolik také k občasným dotazům, proč se neúčastníme startupových akcí a rušného startupového života vůbec. Tím, jak jsme letos <a href="http://www.lupa.cz/clanky/byvaly-vrcholovy-manazer-firmy-cez-investoval-do-projektu-energomonitor/">v klidu doplnili množinu investorů</a> a teď se snažíme obsloužit a doplnit pool zákazníků, což v energetice má dlouhou lhůtu obsluhy, není na takové věci ani moc času, ani moc přesvědčení o tom, že by nám něco přinesly, než článek v médiu, které naši čtenáři stejně nečtou a kontakty ve světě, v němž naši zákazníci moc nejsou. Ale až chvíle času zbude, zkusíme vyrazit, protože já si pořád říkám, že když kolem těch startupových akcí je tolik rozruchu, určitě to na něco bude. To jen ostatní kolegové jsou na pochybách, ale to ještě neviděli tričko, které jsem si z jedné takové přinesl!</p>

<p>A protože kromě software připravujeme i novou generaci hardware a rádi bychom ji už vyráběli v Česku, je o legraci postaráno. Připravit celý hardware do výroby a zařídit to, je slušný záhul i pro zkušené lidi jako Ondra a Pepa, kteří vědí, jak na to. Já už jsem si přidal sen v pořadí. Pokud se nám podaří vrátit výrobu do Česka, tak další metou je, vyvážet to do Číny ... :)</p>

<p>Držte palce a kdyby se vám do Amsterodamu chtělo vyrazit, ozvěte se, pošleme vám vstupenky zdarma...</p>

<p>PS: Až se dodělají kanceláře, uděláme nějakou fotosession, ať vidíte, jak si žijí startupy, kde design kanceláří je méně podstatný, než jejich práce. Upřímně: netuším, kde na to startupy berou tolik času, patlat se s designem kanceláří, už jen komunikace s architektem by nás zavrtala, neřku-li, kdyby si to člověk dělal sám. Takže zatím budeme dělat web, ať je na něm to množství lidí za nějakou chvíli konečně vidět. </p>