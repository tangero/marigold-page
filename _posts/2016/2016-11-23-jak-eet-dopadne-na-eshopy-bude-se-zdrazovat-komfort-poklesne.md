---
ID: 3344
title: 'Jak EET dopadne na eshopy: bude se zdražovat, komfort poklesne'
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/jak-eet-dopadne-na-eshopy-bude-se-zdrazovat-komfort-poklesne
published: true
post_date: 2016-11-23 12:15:30
---
Pár článků o tom, jak dopadne EET na eshopy, už jsem četl, většinou nebylo mnoho jistého a věci se vybarvují teprve teď, když do startu EET pro eshopy zbývají čtyři měsíce. Ve skutečnosti bude EET pro eshopy zřejmě největší oser ze všech oborů, kde evidence probíhá bez problémů (tedy s výjimkou těch, kdo šidili na daních a neevidovali).

Z povahy věci eshopy mají každou transakci zaevidovanou, což samozřejmě neznamená, že nemusí být v pokušení finančnímu úřadu ji upravovat. Jelikož ale tato je křížově ověřitelná proti dopravním službám a dodavatelům, je její “padělání” za účelem hypotetického krácení daně těžko představitelné, pokud se v tomto segmentu dějí podvody, pak v oblasti vratek DPH mezi zahraničními subjekty a největším “podvodem” bude fakt, že šéf eshopu dá svým dětem mobil, který má oficiálně ve vitríně a tudíž z něj neovedl DPH. Proto považuji jakoukoliv evidenci tržeb eshopů vůči finančímu úřadu (FU) za nesmysl a zbytečnou práci, může ale být, že nejsem s principem karuselových podvodů s DPH vůči zahraničním subjektům dostatečně obeznámen (neb v tom oboru nepodnikám).

Já se podívám hlavně na implementační dopady EET pro eshopy, které mají vlastní systém. Pokud si eshopy koupily nějaký tuzemský nástroj pro ecommerce, pravděpodobně jim bude dodán upgrade na EET za nějakou cenu a část implementačních  nákladů u nich tedy bude jiná. Pokud je o zahraniční systémy jako Magento či Shopify, budou asi v úzkých a budou napjatě čekat, zda se najde někdo, kdo vytvoří plugin. U velkých nástrojů se někdo takový najde. <!--more-->



<h3>Není jasné, jak to bude fungovat. Nebo je to divné, že takhle</h3>

Největším problémem implementace je nejasnost, co a jak se bude implementovat. Tak například dříve s mělo za to, že evidenci nepodléhají tržby platební kartou, což ministerstvo financí (minfin) jasně rozhodlo, že podléhají (důvod ponechme stranou). Jenže právní úprava, kterou minfin zvolilo, také jasně říká, že evidenci podléhají všechny platby bezhotovostním převodem, pokud jsou prováděny přes službu třetí strany, tedy třeba přes platební brány. Jejich použití je u eshopů zcela běžné. Jde zřejmě o renonc, minfin chtělo popsat situaci tak, aby nemuselo jasně říct “platební karta”, jenže ji posalo tak, jak se dá vztáhnout i na velkou část bezhotovostních plateb prováděných přes platební brány. Jak z toho vybruslí, uvidíme. 

Další otázkou je, kdy vystavit fakturu s FIK (fiskální identifikační kód), tedy kdy provést samotné zaúčtování platby a její reporting do EET. U eshopů je způsobů plateb více:
* kartou, spadá pod EET
* dobírkou, nespadá pod EET
* platba hotově při vyzdvihnutí (spadá pod EET)
* platba převodem předem na proforma fakturu (nespadá, ale při platbě přes platební bránu spadá)
* platba převodem online s vystavením faktury ihned po převodu (nespadá, ale při platbě přes platební bránu spadá) 
* PayPal, bitcoin a jiné platby přes prostředky třetích stran spadají pod EET

<h3>Vrácení zboží je další komplikace</h3>

Co u eshopů komplikuje situaci, je možnost zboží vrátit. Tehdy musí eshop již zaevidovaný doklad vystornovat respektive vydobropisovat a nahlásit do EET storno faktury. Jak se bude finančí úřad tvářit, až se tam budou denně stornovat vydané faktury, což doposud řešily eshopy v rámci účetnictví? A co je horší, jak se tohle bude dělat v reálném čase, jak zákon vyžaduje, aniž byste ohrozili bezpečnost firmy? 

V čem je problém: přijde vratka, někdo ji v systému “opraví” v EET a tím se vyznačí nárok na DPH. Hloupé je, že tohle doposud dělala jednou měsíčně kvalifikovaná osoba, účetní, která měla čas si to skontrolovat a byla náležitě poučena. Jenže příjem vratek dělají často brigádníci a rozhodně lidi bez účetního vzdělání. Když omylem udělají opravu špatně, tak zadělají svému zaměstnavateli na pořádný průšvih., ne-li na kriminál. Z EET navíc firma nemá šanci poznat, jak si stojí, neexistuje tam žádný mechanismus kontroly z hlediska firmy, takže na špatná hlášení se zřejmě přijde až aktivitou finančního úřadu. Firmy tedy budou muset investovat značné peníze do zajištění těchto hlášení, aby bylo kontrolováno, kdo opravy dělal, proč, jak mění bilanci hlášení firmy a vytvořit si systém varování. 

<h3>Každá platební metoda se obsluhuje v EET jinak</h3>

Další problém je, že každá platební metoda vyžaduje poněkud jiný postup. Při platbě kartou ihned vystavujete platební doklad s FIK, ten přikládáte k zásilce a v případě vrácení zboží děláte opravu. 

Při hotové platbě a osobním odběru (kdy vrácení zboží nemusíte umožnit) vystavujete platbní doklad s FIK a zákazníkovi ihned dáváte doklad, počítáte ale s tím, že už nedojde k vrácení zboží (je to diskutabilní, my to umožňujeme).

Dobírka jede bez EET. 

Platba převodem přes platební bránu znamená  vystavit platební doklad s FIK nebo proforma fakturu bez FIK a po zaplacení vydat doklad s FIK a počítat s možností vrácení zboží. 

V čem je další problém: zákazník se po provedení objednávky často ozve, že by chtěl něco změnit. Dříve jste byli rádi, že si chce něco dokoupit nebo ho zlomíte na dražší zboží, teď to bude potřeba opravit v hlášení EET, čili vystornovat staré a získat nový FIK. Nebo změny objednávek neumožňovat. 

<h3>A náklady jsou hlavně kvůli zmatkům nemalé</h3>

<strong>Náročnost implementace:</strong>
* o zřízení přístupu k EET lze žádat digitálně, není to online, trvá to cca tři dny a je na to děsivý úřední formulář
* rychlejší je požádat osobně na libovolném finančáku, pak něco funguje do druhého dne
* dokumentace k EET má 33 stran nesrozumitelnou úřední češtinou s hromadou ne zase tak triviálních technický požadavků

<strong>Náklady na implementaci:</strong>
* získání certifikátů cca 3 hodiny (pročíst podklady, vyplnit, donekonečna zjištovat, zda už to funguje)
* analýza podkladů 1MD
* implementace jednoduchého EET hlášení 1MD
* implementace storna/oprav 1MD
* nastavení kontrolního worflow pro opravy/storna EET 8MD
* odladění a testování 4MD
* dokumentace a podklady pro proškolení lidí ve firmě 1MD
* proškolení zaměstnanců (další náklad, není zahrnut)

<strong>Celkem mi implementace vychází v úrhnu na 132 pracovních hodin, takže na částku pohybující se v řádu 100 000 Kč.</strong> Do toho není zahrnut náklad na další podporu systému, protože se bude nepochybně průběžně měnit (už dnes se tam pořád něco mění), tedy další tisíce za měsíční provoz.  

Přidejte k tomu vyšší náklady na obsluhu zásilek, kdy jak úpravy již provedených objednávek, tak vrácení objednávek budou vyžadovat podstatně více práce, než tomu bylo dříve. Nejsou tu náklady na zaškolení zaměstnanců ani výrazně vyšší riziko kolize s finančním úřadem. 

S ohledem na to, že EET nemá podporu jiných politických stran a některé již prohlásily, že jej budou chtít zrušit, je rozumná úvaha, požadovat amortizaci EET do příštích parlamentních voleb, tedy v cca dvou až tříletém horizontu. A s ohledem na odhad, jak snížíme počet objednávek obsluhovaných přes EET, odhaduji, že většina středních eshopů bude čelit zvýšení nákladů na obsluhu objednávek podléhajících EET ve výši 10-20 Kč. To už není tak málo a je rozumné tyto náklady převést do ceny objednávky využívající platební metodu. 

V praxi způsobí EET zdražení zboží prodávaného v eshopu a snížení dosavadního zákaznického komfortu, který v Česku byl na velmi vysoké úrovni. Objednávky se budou při jakkémkoliv nestandardním postupu zdržovat, protože operátoři budou muset dělat změny s ohleem na to, co jim systém umožní vůči EET. 

Situace nepomůže ani největším eshopům. Ty sice náklady lépe rozpustí, ale riziko problémů a zvýšené náklady na obsluhu zakázky a hlavně vratky pro ně budou velmi výrazné. Paradoxně nejvíc v pohodě budou nejmenší eshopy, které jedou na krabicovém tuzemském řešení, jež získají levně a které se s EET nebudou moc párat, protože všechno vyřizuje jeden člověk, zpravidla majitel či jeho rodina (toliko názor z voleje, žádný takový eshop do detailu neznám, svítím jen do těch větších - pokud tomu hovíte, svěřte se).  

Na druhou stranu se těším, jak se s EET bude vyrovnávat Amazon a jak se bude minfin vyrovnávat s tím, jak mu Amazon na EET z vysoka prdí. 

Systém EET je nesmyslná záležitost, provedená hekticky a bez dostatečné přípravy. Jeho příprava byla naprosto nekompetentní, neboť připravující si neprovedl ani základní analýzu dopadů implementace do důležitých sektorů, natož, aby se zamýšlel nad tím, jak se problémům vyhnout. Životy EET nakonec zkomplikuje všem a její oficiálně deklarovaný přínos bude pramalý. 

Poznámka na závěr: objevily se informace, že <a href="http://zpravy.e15.cz/domaci/ekonomika/dalsi-zmena-babis-chce-vyjmout-z-eet-e-shopy-1325747">ministerstvo financí EET pro eshopy odpíská</a>. Bylo by to rozumné, už proto, že na eshopy a jejich zákazníky systém dopadne obzvláště tvrdě, aniž by byla šance zde cokoliv ze situace získat. Kromě toho část rozlobených obchodníků už hodlá zákazníkům velmi transparentně pomocí poplatku “babišovné” sdělovat, kdo za zdražení a komplikace může.