---
ID: 2259
author: Patrick Zandl
categories:
- Mobilní sítě
- Ufon
- CDMA
layout: post
oldlink: 'https://www.marigold.cz/item/servisni-menu-telefonu-ubiquam-u-400

  '
post_date: 2008-07-15 12:09:37
post_excerpt: ''
published: true
summary_points:
- U:fon má občas mizerný zvuk, pravděpodobně kvůli primitivnímu audiokodeku.
- Servisní menu Ubiquam U-400 se aktivuje kódem 8247826 (UBIQUAM).
- Ec/Io udává kvalitu signálu, pod -10 indikuje nezdravou síť.
- Další servisní menu se aktivují kódy 343587 a 343586.
title: Servisní menu telefonu Ubiquam U-400
---

Dal jsem se v posledních dnech do zkoumání toho, proč má U:fon někdy tak mizerný zvuk. Původně jsem si toho nevšiml, nejsem natolik citlivý, abych takové věci bezpečně rozeznával a ani prostředí, kde telefonuju, nebývá akusticky ideální. Ale pak se ta plechovost místy nedala přehlédnout.

K šetření (které ještě neskončilo, ale podezření je na primitivní audiokodek) jsem potřeboval aktivovat si servisní menu telefonu. Bylo potřeba chvíli pátrat, protože Ubiquam U-400 nepatří zrovna mezi světově nejprodávanější modely, nakonec pomohli lidi z ruského SkyLinku, kterým pár těchto kousků straší v síti a navíc je telefon podobný modelu U-200, co do firmware. A protože u nás se o servisním menu telefonu asi mnoho nenapsalo (se vzácnou výjimkou <a href="http://www.gsmweb.cz/blog/2008/06/30/ufonuv-mobil-sledovani-site">GSMwebu</a>), uděláme si malé shrnutí.


<!--more-->

<h3>Field Test Mode Ubiquam U-400</h3>

<img src="http://www.marigold.cz/wp-content/uploads/ufon-servismenu.jpg" alt="Ubiquam U-400 service menu" border="1" width="250" height="290" align="right" />Prvním zajímavým rozšířením telefonu je vstup do servisního menu pro sledování sítě. To vyvoláte zadáním kódu ##8247826 (pro lepší zapamatování je to ##UBIQUAM na klávesnici telefonu. Netřeba nijak odesílat, po vyťukání kódu se objeví samo servisní menu, viz obrázek. 

Stručný popis: <strong>CH</strong> je kanál (vždy kanál 505). <strong>SCI</strong> je Slot Cycle Index, ten určuje, jak často se telefon "probudí", aby zjistil, zda nepřichází hovor (zatím nastaveno 1, druhý nejrychlejší čas). <strong>SID</strong> je System ID a <strong>NID</strong> je Network ID, u nás obojí jedna. <a href="http://www.ifast.org/SIDtables.htm">SID</a> se používá pro zjištění, zda se telefon nachází ve vlastní síti a v rámci povolené oblasti, NID unikátně identifikuje síť. U nás zjevně bezpředmětná čísla, s jinou sítí v témže pásmu telefon těžko zkoliduje. 

<strong>PC</strong> je identifikace, že telefon poslouchá na pilotním kanálu (běžný stav), prakticky se zde může objevit ještě EX (není signál) nebo SC (synchronizační kanál, málokdy).  

Důležitá je veličina <strong>Ec/Io</strong>, tedy poměr přijímaného signálu z pilotního kanálu (to je to <em>Ec</em>) vůči celkové úrovni spektrální hustoty (to je ono <em>Io</em>, tedy vůči součtu signálů ostatních buněk). Číslo se udává v dB, je záporné a čím více se blíží nule, tím je lepší "slyšitelnost" pilotního kanálu, tím lepe se telefonuje. Jakmile se s touto hodnotou dostanete pod -10, indikuje to nezdravou síť, je slyšet příliš mnoho provozu, který ruší. Vyhodnocování Ec/Io si zaslouží zvláštní článek, jestli na něj zbude čas, dáme se do toho, protože podle toho, jak jsem Ec/Io sledoval, trpí Ufon problémy mimo jiné právě v tom, že často zasahuje signál pilotního kanálu jednotlivých buněk příliš do oblasti ostatních buněk. A to i přes to, že těch buněk nemá zase tolik ani v Praze. Nicméně se zvukem to tolik nesouvisí a zásadní to rozhodně není. 

Rx je síla přijímaného signálu (ze základnovky), Tx je síla vysílaného signálu (z mobilky). Hodnoty v dBm jako záporné, čím blíže k nule, tím lépe, přes stovku už si moc nezavoláte, ale záleží také na poměru Ec/Io. 

Bat je zůstatková kapacita baterie ve mně neznámé veličině, nezkoumal jsem to. 

<strong>NoCNV</strong> znamená, že  neprobíhá konverzace. Pokud si zavoláte, objeví se <strong>FER:</strong> a číslo. FER je Frame Erasure Rate, tedy poměr vymazaných (vyhozených) rámců oproti přijatým rámcům. Počítat se může logicky jen za hovoru, kdy rámce přijímáte. čím méně, tím lépe, do dvou procent no stress, to je běžný provozní problém. 

<strong>PN je Pseudo Noise Offset, PN Offset</strong>, tedy unikátní identifikátor toho, na čem visíte, zhruba něco na způsob kanálu v GSM, akorát to funguje jinak :). V síti se PN může opakovat, ovšem hodně daleko od sebe, aby se stejná PN nepotkaly v mobilu najednou (takže reuse faktor závisí na síle pilotního kanálu, citlivosti zařízení, ztrátách signálu atd) a jde o stabilní veličinu, měnit ji je podobná radost, jako měnit kanály. Celkem je 512 možností PN. Zjednodušeně řečeno je PN Offset zpoždění vůči síťovému času (UCT) aplikované na náhodnou sekvenci PN Short Code v rámci základnové stanice. PN Offset na pilotním kanálu zajišťuje, aby signál z jedné buňky nekolidoval se signálem z jiné buňky (tak vidíte, že to není kanál ale skoro jako by byl).  

Toť všechno, co Field Test mode na U-400 prozradí, použitý hlasový kodek zde není. Škoda. Nezapomeňte si ho znovuzadáním kódu vypnout, protože když je zaplý, blbne signalizace. 

<h3>Další servisní menu</h3>
<img src="http://www.marigold.cz/wp-content/uploads/ufon-factorytest.jpg" alt="Ubiquam U-400 Factory test" border="1" width="250" height="280" align="right" />
Další servisní menu souvisí s nastavením telefonu a kontrolou jeho nastavení. Ty už rozebírat nebudu, zkuste si to sami, nezměňte si hlavně kontrast displeje k nečitelnosti. Zadejte <strong>##343587</strong> pro NAM Test menu a <strong>##343586</strong> pro Debug Factory Test.  Channel naštěstí změnit nejde, to by vám telefonování poněkud otrávilo. FTM je Factory Test Mode, když si ho zapnete, telefon odstavíte, naštěstí to jde vypnout. FTM je určeno pro ladění telefonu a vzhledu UI, vám asi na nic. 

Se zbytkem si hrajte, na své riziko samozřejmě. 

<em>PS: omluva za kvalitu fotek, foceno iPhone a bez velkého experimentování... </em>