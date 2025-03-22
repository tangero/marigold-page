---
ID: 1054
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/update-a-upgrade-o-ibm-a-nucleusu

  '
post_date: 2004-05-26 11:14:00
post_excerpt: ''
published: true
summary_points:
- Autor si pořídil nový notebook IBM R50 s lepším displejem a WiFi.
- Starý redakční systém Genesis nahrazuje novým Nucleus kvůli robustnosti a administraci.
- Nucleus vyžaduje složitější konfiguraci designu oproti Genesis šablonám.
- Autor plánuje migraci dat do Nucleusu a učí se PHP pro úpravu databází.
title: Update a upgrade (o IBM a Nucleusu)
---

<p>
Zastávám fordovskou zásadu, že nezáleží na značce notebooku, pokud je to IBM. Včera se mi podařilo úspěšně zajistit nový IBM R50, jímž nahrazuji dosluhující R31 - a chrochtám si blahem. Půl giga paměti, displej o rozlišení 1400 bodů, takže už se na něj opravdu vejde všechno, co bych potřeboval vidět. A toho místa na disku, paráda. K tomu displeji - což je moje klíčové místo každého notebooku - oproti R31 je citelně kontrastnější a samozřejmě lepší. Chrochty chrochty. Kromě toho je v notebooku Centrinu a tedy i WiFi 802.11b, což se hodí, protože jsem nedávno v kufříku zlomil svoji PCMCIA WiFi kartu. A také bluetooth, ještě ho rozchodím a budu megaspokojen. Takže dneska mimo běžné práce kopíruju data ze starého na nový notebook, instaluju programy a vůbec si nový notebook uživám. Dovedete si představit pět hodin práce na baterky? Já snad dneska půjdu pracovat do Františkánské zahrady na místní WiFi od WideNetu :)</p>

<p>
Obrovskou WiFi výhodou IBM je konstrukce antény - ta je napasovaná do displeje (doufám, že i v mém modelu), takže například i v práci chytám tři cizí WiFi sítě z okolních kanceláří. Asi jim udělám bezpečnostní prověrku :) A další výhodou je, že mi chodí NetStumbler i s Centrinem, v což jsem původně ani nedoufal. </p>

<p>
Abych těch upgrade neměl najednou málo, už nějakou dobu pracuji na migraci Marigolda z Genesis na nějaký free redakční systém. Udělal jsem si výběrové řízení a vypadá to na Nucleus, který jsem chvilku testoval na obětním serveru a včera nainstaloval <A href="http://new.marigold.cz/" target=_blank>na ostrý server</A>. Jak vidno, design teprve po večerech ladím, času ale není mnoho, protože licence Genesis 4 free se ruší a stávající hosting je záhodno opustit. Genesis je sice báječný systém, ale na weblog mých potřeba zbytečně robustní - z asi dvaceti položek menu používám pravidelně dvě, výjimečně dvě další, jenže titulka Genesis po zalogování má asi 300 Kb a trvá to, než se mi všechno nahraje. Navíc administrace je maxibezpečná přes HTTPS a certifikát, čímž je nepoužitelná z většiny malých zařízení, zatímco Nucleus ji má jen přes HTTP a bez certifikátu. A navíc jsem si řekl, že se naučím něco nového. </p>

<p>
Zajímavé je srovnání <STRONG>Genesis a Nucleusu</STRONG>. Berte mne jako mírně deformovaného, Genesis používám léta, Nucleus tři týdny. </p>

<p>
<A href="http://hulan.info/blog/item/nucleus-cms-extreme-edition-3-0-rc" target=_blank>Nucleus </A>se pro konkrétní záměry konfiguruje podstatně složitěji, než <A href="http://www.genesis2.cz/" target=_blank>Genesis</A>. Zatímco v Genesis si můžete vzhled naprosto libovolně změnit v rámci "šablony", kde si parametrizujete značku tak, aby dělala, co potřebujete, Nucleus za tím účelem má hned tři instance a tři místa, kde musíte něco měnit. Především jsou tu <EM>Skiny</EM> a <EM>Template</EM> - pořád si pletu, co je k čemu a jako na potvoru vlezu do menu toho druhého, když něco dělám. Jedním upravujete vzhled okolí stránky a druhým zase vnitřek - konkrétní vzhled odkazu na kometáře, detail článku atd. Původ tohoto rozdělení jest mi záhadou a jeho smysl mi uniká, ačkoliv Radek Hulán mi to nějak vysvětloval, spíše mi přišlo, že už je na to zvyklý, než že by to mělo nějaký důvod. A když ještě pořád nejste spokojeni, musíte sáhnout přímo do konfigurace <EM>pluginu</EM>. Plugin je zhruba totéž, co v Genesis značka, jenže narozdíl od Genesis nejsou pluginy konfigurovatelné parametry přímo v rámci šablony, ale konfigurují se přes web . Jak obsáhle, záleží na autorovi, většinou (co jsem koukal) je ta konfigurace přes web hodně oškubaná, takže když chcete plugin přizpůsobit svým záměrům přesně, musíte kromě web administrace šáhnout do PHP kódu pluginu a upravit si to ve zdrojáku. U Nucleusu si můžete plugin sami naprogramovat, když víte jak, což v Genesis sami nemůžete, neb ho nijak na server neuložíte - v Genesis se normálně k úrovni zdrojáku a PHP nedostanete.</p>

<p>
Na druhou stranu, pokud potřebujete nějaký design a nechcete ho měnit, Nucleus už několik vzhledů obsahuje - Genesis přichází jako <EM>tabula rasa</EM>. Jenže já chci vzhled po svém, takže mám s čím si hrát. Chcete příklad? Podívejte se na new.marigold.cz - k tomu, abych správně (=dle svého) zobrazil Poslední komentáře (menu vpravo) musím sáhnout až do zdrojáků pluginu. Není to moc složité, prostě jsem tam nahradil jednu HTML značku jinou, kterou jsem chtěl - jenže v Genesis stačilo upravit šablonu, kterou jsem designoval celou stránku. V jednom případě to není tak hrozné, ale takových věcí potřebuju upravit hromadu. Ano, asi by to šlo z části&#160;přeskinovat pomocí CSS, ale to už je zase o něčem jiném... </p>

<p>
Srovnávat Nucleus s Genesis samozřejmě nejde, pokud se bavíme o provozu větších serverů. Nucleus nemá žádnou podporu pro cache, minimální podporu týmové práce a nula u dokument workflow a hromadu takových věcí, bez které se u velkého serveru zahrabete po krk do problémů.&#160;Vzhledem k rozsahu redakce Marigold.cz (1&#160;ks člověka)&#160;a vzhledem k návštěvnosti, mne to tížit nemusí. Tož uvidíme, jak si s konverzí poradím, protože to nejlepší teprve přichází. Vycucat všechny zprávy z marigolda a zkusit je nacpat do Nucleusu. Pak teprve bude mít smysl ladit design, když se mi to náhodou podaří... :) Jo, jedna věc mne ještě láká - že bych se s Nucleusem konečně trochu naučil PHP. Protože například databázi WiFi hotspotů a Přehled WiFi techniky bych musel naprogramovat v PHP, uživatelské databáze&#160;v Nucleusu jsou zatím moc jednoduché. Ale napsat v PHP příkaz na vypsání dat z databáze do web stránky snad nebude tak složité, jdu si koupit knihu a přijít, jak na to :)</p>