---
ID: 2165
title: 'Zběsilá  jízda na Leopardu 2. &#8211; případ firewall a&nbsp;bezpečnost'
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/zbesila-jizda-na-leopardu-2-pripad-firewall-a-bezpecnost
published: true
post_date: 2007-11-04 11:14:57
---
Dalo by se říci, že případ bezpečnosti Leoparda se stal hvězdnou hodinou pro vcelku neznámý Heise Security, britský magazín věnovaný bezpečnosti. <a href="http://www.heise-security.co.uk/articles/98120/1">Jeho verdikt</a> <em>The Mac OS X Leopard firewall failed every test</em> obletěl svět a byl citovný všemi možnými médii. Ačkoliv vyšel už 29.10., Apple k němu, jak je zvykem, nezaujal stanovisko a nechal ho bez komentáře. Možná škoda, protože vinou nedostatku publikované dokumentace bylo dopátrání se pravdy náročnější a dodnes někteří opravdu věří tomu, že firewall Leopardu je druhé jméno řešeta. 

<!--more-->

Zaprvé je třeba říci, že firewall v Leopardu skutečně není automaticky aktivní. Co tím Apple sledoval, lze říci těžko. Na jednu stranu je pravda, že v rámci amerických ISP se firewallování klientů už docela rozmohlo, stejně tak ve firemní síti. Na stranu druhou správně nastavený firewall by neměl dělat velké potíže. Lze jistě argumentovat tím, že není v současné době známý žádný průnik po síti (krumpáč funguje vždy a jistě) do Tigra nebo Leoparda (narozdíl od XP / Vista), kde hrozí buďto průnik nebo zhroucení systému. Ale i přesto asi měl být firewall aktivní. Takže opatrnosti není dost a je vhodné si ho zapnout. 

Druhé tvrzení Heise Security, totiž že firewall Leopardu prakticky nefunguje už dnes můžeme s klidným svědomím odmítnout, zjištění odborníků z Heise Security jsou neúplná a překonaná. Ponechme stranou, že odborník je člověk z jiného města, v tomto případě jim unikla podstatná maličkost. 

<!--adsense-->

Fakt, že firewall při portscanu hlásí porty jako otevřené ještě neznamená, že nefunguje. Prostě se nějak tváří a důležité je, jak se zachová při skutečném útoku. Zjednodušeně řečeno podstatné je, že žádný zatím není znám a že ani s těmi porty to není tak heise, jak to vypadalo... 

Apple totiž v Leopardu firewall dosti podstatně změnil oproti Tigrovi. Ačkoliv je nadále používaný BSD IPFW. Apple totiž přijal za své myšlenku větší provázanosti firewallu a operačního systému. Problémem hardware firewallů je to, že většinou nemají šanci dozvědět se o charakteru přes ně běžících aplikací, než nějakou analýzou a odhadováním. Firewall integrovaný do operačního systému má šanci oproti tomu zjistit, co je to za program, který se snaží ustanovit síťovou konexi a podle toho se nějak zachovat. A to Apple využil. 

Aby nebylo tak snadné vydávat virus za jiný program, zavedl Apple v Leopardovi digitální podepisování aplikací. A to je další věc, kterou recenzenti zpravidla přehlížejí jako nepodstatnou, pro bezpečnost systému bude mít ale do budoucna velikou důležitost. Applem dodané aplikace jsou digitálně podepsané. Podpis říká, co je aplikace zač a že je její integrita neporušena. Další části systému se podle toho zařizují. Například Keychain skladující centrálně hesla vás po reinstalaci digitálně podepsané aplikace nebude znovu buzerovat otázkou, zda této aplikaci má hesla zpřístupnit, protože podle podpisu zjistí, že jde o tu samou aplikaci, jen v nové verzi. 

Stejně tak firewall podle podpisu zjistí, že aplikace je důvěryhodná (a nenapadená). Proto síťové služby jako Bonjour (utilita Zeroconfig) nebo aktualizace času ze síťového serveru běží i v momentě, kdy firewallu zadáte příkaz blokovat veškerý příchozí provoz. Firewall neblokuje provoz o kterém ví, že je v pořádku. Podle všeho jde tedy spíše o nedostatky v terminologii, než o vadu firewallu, z hlediska bezpečnosti opravdu nemá smysl blokovat služby, které jsou v pořádku. A právě tohle měl Apple vysvětlit místo toho, aby si to lidé horko-těžko zjišťovali sami. 

Právě tenhle systém dělá z firewallu v Leopardovi užitečnějšího pomocníka než z jakéhokoliv jiného firewallu. Unixoví maniaci budou zklamáni, ale ti, kdo chtějí firewall mít jako spolehlivého pomocníka, budou spokojenější. Samotného mne příjemně překvapuje, že digitálně podepsané aplikace firewallem hladce projdou. 

Otázka do pléna je, zda má dnes na firewallu smysl nastavení "Blokuj veškerý internetový provoz", což je další stížnost - Leopard firewall nic takové asi nemá. Osobně jsem používal software od Intego, který tohle nastavení má, ale nikdy jsem ho nepoužil. Když chci odpojit počítač od sítě, vypnu WiFi a odpojím kabel. Airwall mi přijde mnohem důvěryhodnější. Ale dost možná jsem něco zásadního přehlédl. 

Dlužno dodat, že tento popis firewallu se týká klientského systému. Serverový firewall funguje odlišně a tento popis na něj nemusí platit. 

Další materiály a odkazy <a href="http://securosis.com/2007/11/01/investigating-the-leopard-firewall/">k firewallu Leoparda třeba zde</a>. <a href="http://codm.genhex.org/2007/11/macosx-leopards-firewall-is-no.html">Nebo zde</a>. 

Pro hraní si s firewallem doporučuji odpůrcům příkazové řádky instalovat si zdarma GUI <a href="http://www.hanynet.com/waterroof/">WaterRoof</a>... 

<h3>První útok trojského koně? Kdeže ...</h3>

Dalším "skandálem", který se vezl na vlně popularity Leoparda byl <em>"první trojan pro Mac OS X".</em> Jeho zjevení mělo nabourat mýtus o bezpečnosti Mac OS X, alespoň podle některých médií. 

Zmíněný trojan dostal označení <strong>RSPlug.A </strong>a je ke stažení na některých pornosajtech, kde se vydává za video kodek potřebný pro přehrávání obsahu. Člověk si ho musí dobrovolně stáhnout, potvrdit výstrahu při instalaci a pak ještě zadat heslo administrátora (což se zadává jen při instalaci systémových služeb, jakou video kodek rozhodně není). Trojan nespoléhá tedy na chybu v systému, ale na nedostatek pozornosti na receptorech mezi klávesnicí a židlí. 

Několik závisticů, kteří dosud neznámému autorovi nepřáli slávu být prvním trojanistou na Mac OS X podotýkají, že prvním trojanem ve skutečnosti je albánský trojan, při němž spustíte konzoli a napíšete <strong><em>sudo rm -fr /</em></strong> -  také musíte zadat heslo administrátora. A co je na tomhle albánském viru nabízejícím hru sudoku ohavné? Prý ho obsahují všechny Mac OS X distribuce už od výrobce! To je ale skandál...

Ale vážně, trojských koňů spoléhajících na to, že uživatel bezmyšlenkovitě zadá root heslo, těch bude... Za trojského koně bych ovšem raději i nadále označoval spíše program, který se  instaluje a škodí sám bez větší interakce uživatele, jak to bylo na starých dobrých Windows, kdy vám do Outlooku přišla příloha a sama se provedla a instalovala... 

Poznámka související s firewallem: aplikace, která získá root práva, může projít i firewallem. Holt root heslo není na rozdávání... 	

<h3>Upozornění před prvním spuštěním</h3>

Jednoduchou pomůckou pro bezpečnost je upozornění před pvním spuštěním  nebo spíše před instalací, které nyní Leopard dává u nepodepsaných aplikací. Při kliku na instalační soubor jste upozorněni kdy a jakým programem jste ho stáhli. Teprve po odkliknutí se pokračuje v otevření a instalaci. 

<h3>Sandbox</h3>

Pro vývojáře a hračičky nebude bez zajímavosti implementace Sandboxu, která vychází z Systrace od Nielse Provose. Sandbox je takové bezpečné pískoviště, kde si můžete hrát s aplikacemi, u kterých nevíte, co jsou zač nebo jim chcete přistřihnout křidýlka. Můžete jim dovolit, co mohou a co nemohou, můžete je omezit, jak se vám to hodí. 

Hloupé zatím je, že kromě tří stránek nápovědy v manu není zatím k dispozici žádná dokumentace, ale snad ji Apple co nejdříve uvolní. A aplikace se jmenuje v Mac OS X Seatbelt. Pár <a href="http://codm.genhex.org/2007/10/macosx-leopard-sandbox-seatbel.html">dalších detailů zde</a>.

<h3>A pro hračičky je 10.5 ve zdrojáku</h3>

Ne celý samozřejmě ... Zdrojové kódy open-source části systému  jsou tradičně u Apple vydávány v rámci projektu Darwin, takže kdo si chce hrát, <a href="http://www.opensource.apple.com/darwinsource/10.5/">může stahovat</a>. 

Tak a to je zatím všechno, co mne napadlo :)