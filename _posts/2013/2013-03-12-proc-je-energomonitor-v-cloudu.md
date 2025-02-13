---
ID: 2632
author: Patrick Zandl
categories:
- Energomonitor
layout: post
oldlink: 'https://www.marigold.cz/item/proc-je-energomonitor-v-cloudu

  '
post_date: 2013-03-12 16:46:20
post_excerpt: ''
published: true
summary_points:
- Energomonitor ukládá data do cloudu kvůli ceně, technické vhodnosti a budoucím funkcím.
- Cloud umožňuje levný hardware, dálkové aktualizace a centrální správu zařízení.
- Analýza dat v cloudu umožňuje porovnávání efektivity a automatické rady uživatelům.
- Export dat bude, ale je nutné ho upravit pro praktické využití uživateli.
title: Proč je energomonitor v&nbsp;cloudu
---

<p>Není to častá výtka obecně, ale ve skupině geeků ano: nechtějí, aby <a href="http://www.energomonitor.cz">energomonitor</a> ukládal data do cloudu, chtějí vysloveně lokální uložení dat, třeba na SD kartu, kterou si pak budou moci zpracovat. Proč je tedy energomonitor v cloudu a proč na tom nechceme nic měnit?</p>


<p>Důvody jsou tři: cena, technická vhodnost a možnosti do budoucnosti. A jsou těžko odlučitelné, protože spolu souvisí. Takže tedy:</p>


<!--more--><h3>Ad cena</h3>
<p>Aby energomonitor mohl dobře sloužit, musí být dostupný a levný. Existuje celá řada řešení, které stojí desetitisíce a právě z toho důvodu si je nekoupí každý. Věříme, že správná cena je klíč. Správná cena znamená, že technika musí být maximálně levná. Minimum paměti, minimum výpočetního výkonu. Žádná zbytečná rozhraní, nic, co by tlačilo cenu výše, než je nezbytné. Někdo nám psal, že kdybychom to postavili na Rapsberry Pi… Ano, to by jistě šlo. Stojí 35 USD, tedy 850 Kč s DPH, což by jistě dobře vyšlo. Ano i ne. Ještě byste potřebovali nějak vyřešit bezdrátový přenos dat (radiočip není v ceně) a také byste museli doplnit měřící kleště a vysílač údajů z nich (což je 1900 Kč s DPH). Všeho všudy by řešení nevyšlo nijak závratně levně, jsme zatím na 2750 Kč s DPH, to do PRODEJNÍ ceny naší sady zůstává 1250 Kč, za což je potřeba aplikaci naprogramovat, provozovat, podělit provizí partnery a prodejce a co je horší, udělat plastovou krabičku (lisovací forma na ni stojí slušný balík) a dořešit to bezdrátové spojení. Suma sumárum, nevychází to.</p>

<h3>Ad technická vhodnost</h3>
<p>Na to, že od krabičky potřebujeme spolehlivý přenos dat do internetu je to kanón na vrabce a nejenom cenově. Ale samozřejmě: pokud si to chcete naprogramovat sami, je to dobrá volba, na které se hodně naučíte (k tomu Pi taky je). V našem případě je osmibitový ATMEL s malým displejem a jednoúčelovým rádiem ideální. Například i ve spotřebě: jednoúčelové rádio má mnohem menší spotřebu a na dva "buřty" ho umíme napájet až sedm let. V místě měření tak nemusí být zásuvka, což zpravidla v českých rozvodných skříních nebývá.</p>

<p>Co je pro nás také technická vhodnost? Naše krabičky jsou dálkově aktualizovatelné a pod centrální správou. To sice uživatelům bere svobodu přestavět si je na vrtulník, ale pokud by náhodou potřebovali, aby sloužily svému původnímu určení, stane se tak bez uživatelova přičinění. Hlídáme aktualizace, provádíme potřebné změny, uživatel jen užívá. Veškeré funkce aplikace leží v cloudu a zpracovávají je naše servery (tedy přesněji servery Amazonu), díky čemuž lze použít levný hardware, který data jen zobrazuje. To všechno trochu vadí bastlířům, ale více vyhovuje lidem, kteří si měřák elektřiny koupili třeba na… měření elektřiny.</p>

<p>Jak vidíte, cena souvisí i s technickou vhodností. A ta zase s funkcemi, které chceme nabízet či už nabízíme. Především se ukazuje, že velká skupina (a vychází nám, že většina) klientů opravdu potřebuje mít data dostupná po internetu, ne přes lokální síť. Nejde jen o to, podívat se na data pobočky v jiném městě, ale třeba o to, že lidi se podívají na data v práci při pauze, když řeší něco s energetiky. Nutit je přemýšlet, zda jsou zrovna ve stejné síti, v jaké mají umístěný měřák, je zabiják aplikace.</p>

<h3>Ad budoucí funkce a rozvoj</h3>
<p>Co je ale podstatné, je chytrá analýza dat, která se otevírá teprve v cloudu. Můžeme porovnávat energetickou efektivitu jednotlivých uživatelů a radit jim, co dělat, aby jí dosáhli - tím, že je strojově porovnáváme s ostatními. A to je to hlavní, nemusíme vymýšlet rady a tipy, použijeme jen to, co již někdo používá. Rozpoznáme, že máte špatně zapojený bojler, protože už se to našemu zákazníkovi stalo. Jednou - až to algoritmicky popíšeme - vám to automaticky řekneme. Teoreticky můžeme na základě znalosti dat dělat mnohé, co pomůže odběr elektřiny ještě dále snížit a co by jednotlivě (bez cloudu) nebylo realizovatelné, protože by pro to nebyly analyzovatelné vzory.</p>

<p>Ad bezpečnost: ano, může to někdo hacknout <em>(to je konstatování faktu, že CIA to zvládne, váš soused asi těžko, trochu jsme se tomu věnovali)</em> a uvidí, jakou spotřebu jsme naměřili vteřinu za vteřinou. Neuvidí, komu, to už je jen v našemu systému, uvidí jen anonymní data (a neuvidí výchozí spotřebu, jen její inkrementy). Vyjde ho levněji, když se zajede podívat na váš elektroměr, který musí být volně přístupný z veřejného prostranství. Když bude mít štígro, uvidí ho přes Google StreetView před dvěmi lety...</p>

<p><strong>Sečteno a podtrženo: bez cloudu by energomonitor byl dražší, méně perspektivní a neuměl by to, co chceme, aby uměl.</strong> Byl by to obyčejný měřák elektřiny, jakých je na trhu desítka a stál by o řád více, tedy by byl přesně tím, co jsme postavit nechtěli (a nepostavili). Pokud takový potřebujete, můžete si ho koupit (od někoho jiného, do toho se my netlačíme). My si myslíme, že máme hodně dobrých důvodů, proč se cloudu držet - a považujeme jej za základ služby.</p>

<p>Je samozřejmě možné, že nic z toho vás netrápí. Jste člověk, který bydlí v podnájmu, elektřinu má v paušálu či nemá žádný či pramalý vliv na to, od koho se bere nebo jaká je její spotřeba. Bydlíte v malém bytě, roční účet za energie nepřevýší 20 000 Kč. Máte vlastní elektrárnu, jakoukoliv. Máte dost peněz na to, aby vám to bylo fuk a to včetně toho, že je vám fuk, když vás odrbávají, protože řešit pár desítek tisíc ročně by vás příliš nervovalo či stálo zbytečného času. Principiálně odmítáte data v cloudu, bez ohledu na jakýkoliv argument. Bojíte se ještírků. Možností je celá řada, kdy energomonitor nebude produkt pro vás. Víme o tom.</p>

<p>Pro všechny ostatní je to podle mne zajímavá alternativa. <a href="http://blog.energomonitor.cz/navstivte-nas-v-brne-na-veletrhu-amper">Přijďte se na nás podívat,</a> od 19. do 22. března 2013 na brněnském výstavišti v pavilonu P na stánku číslo 100 - serveru <a href="http://www.elektrika.cz">Elektrika.cz</a>. Tady se potkáte s energomonitorem i lidmi za ním: Pavel Štorek, Jarda Adamíra, Viktor Holý a já (jak kdo který den bude).</p>

<p><strong>PS: To není o exportu dat. </strong>Ten bude. S ním je problém spíše filosofický: data se dnes přenášejí co pár vteřin a nasypat vám XLS takových dat by vám v praxi moc nepomohlo. Potřebujeme to učesat, udělat konfigurovatelné, jenže před tím potřebujeme udělat věci, které jsou zásadní. </p>