---
ID: 1446
title: Chci bezdrátovou síť (6.3)
author: Noname
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/chci-bezdratovou-sit-6-3
published: true
post_date: 2004-12-15 13:10:00
---
	<p>
Tento článek navazuje na <a href="/item/chci-bezdratovou-sit-6-1">úvodní kapitolu retranslací</a> a na předchozí kapitolu věnovanou <a href="/item/chci-bezdratovou-sit-6-2">pasivním retranslacím</a>. Pro pochopení mnohých termínů z této části musíte bezpodmínečně znát termíny jako WDS, AP, ad-hoc, Klient atd. vysvětlené v <a href="http://www.marigold.cz/?query=chci%2Bbezdr%C3%A1tovou%2Bs%C3%AD%C5%A5&amp;amount=0&amp;blogid=1">předchozích částech seriálu</a>.</p>

<h4>Aktivní retranslace</h4>
<p>
Aktivní retranslace jak už název napovídá využívá na retranslačním bodě další aktivní prvek (prvky). Ten přijme signál z bodu A, a pak jej zpracuje naprosto normálně, jako by byl sám klient, tj. očistí jej od šumu, byl-li frame přijat s chybou, je zažádáno o přeposlání, aniž by se signál dále posílal. Je-li vše v pořádku, signál je pak poslán dál buď druhým rozhraním (má-li aktivní prvek více rozhraní), stejným rozhraním (pomocí WDS, nebo režimem více klientů na jednom AP — viz dále) a nebo přes Ethernet na další bezdrátový aktivní prvek a z něj pak posláno na bod C.</p>
<p>
Způsobů řešení aktivní retranslace je mnoho, každý má své výhody a nevýhody, zkusíme si je shrnout.</p>
<div class="rightbox">
<h5>Aktivní retranslace s 1 AP</h5>
<img src="/wp-content/uploads/cache/20041215-activretr1.gif" alt="Aktivní retranslace s jedním AP" width="250" height="157" /></div>
<h5>AP režim s jedním centrálním prvkem</h5>
<p>
Tento způsob je vhodný pro nejlevnější a nejsnazší řešení na menší vzdálenosti a s menší propustností. De-facto se jedná o standardní síť s přístupovým bodem (Infrastructure — viz předchozí díly seriálu), se dvěma klienty, na každé straně (A a B) jeden. Jak víte, není možné spojit bezdrátově dva přístupové body (vyjma režimu WDS, viz dále). Klienty tak musí být zařízení označované jako &#8220;bezdrátový klient&#8221; či &#8220;klientský adaptér&#8221; (wireless client), ať už třeba box s <a href="http://www.wifishop.cz/inshop/scripts/set.asp?Level=79">Ethernet rozhraním</a>, tak třeba jen přes <a href="http://www.wifishop.cz/inshop/scripts/set.asp?Level=78">USB</a> či <a href="http://www.wifishop.cz/inshop/scripts/set.asp?Level=76">PCI kartu</a> připojený počítač. Jako klienta můžete ale použít i <a href="http://www.wifishop.cz/inshop/scripts/set.asp?Level=63">AP, který podporuje klientský režim</a> (stává se tím vlastně běžným klientským adaptérem s Ethernet rozhraním). Na tento prvek je pak napojena <a href="http://www.wifishop.cz/inshop/scripts/set.asp?Level=81">směrová anténa</a> libovolného typu s dostatečným ziskem. Protože spoje s retranslacemi se většinou dělají pro páteřní linky či pro movitější klienty, i zde bych doporučoval použít plné paraboly, které se dostaly na cenu srovnatelnou s ostatními typy antén, přitom ale s výrazně kvalitnějšími parametry danými technologickým řešením (viz <a href="/item/chci-bezdratovou-sit-5-2">díl 5.2 tohoto seriálu</a>)</p>

<!--more-->	<p>
Přístupový bod může být kterýkoliv <a href="http://www.wifishop.cz/inshop/scripts/set.asp?Level=63">bezdrátový bridge</a> nebo <a href="http://www.wifishop.cz/inshop/scripts/set.asp?Level=64">bezdrátový router</a>. Na něj je připojena buď jedna anténa (<a href="http://www.wifishop.cz/inshop/scripts/set.asp?Level=82">všesměrová</a> či <a href="http://www.wifishop.cz/inshop/scripts/set.asp?Level=83">sektorová</a>, tak, aby její vyzařovací diagram obsahoval body A i C) a nebo můžete použít dvě <a href="http://www.wifishop.cz/inshop/scripts/set.asp?Level=81">směrové antény</a>, které propojíte pomocí <a href="http://www.wifishop.cz/inshop/scripts/detail.asp?itemId=20346&amp;level=86">anténního slučovače</a> — v tom případě ztratíte sice 3 dB, ovšem výsledná dosažitelná vzdálenost bývá větší (všesměrové i sektorové antény mají malý zisk)</p>
<p>
Komunikace probíhá zcela jasně z prvku v bodě A, na prvek v bodě R, na něm se data obrátí a putují stejným rozhraním nazpátek. Z toho vyplývají výhody i nevýhody tohoto řešení</p>

<ul>
<li>výhodou je cena řešení, potřebujete jen jeden aktivní prvek, máte menší náklady na elektriku, rozvaděč atd. </li>
	<li>částečnou výhodou je rychlost zpracování u velmi malého počtu požadavků — pomalejší než u pasivní retranslace, ale rychlejší než u aktivní se dvěma prvky, kde se musí pakety převést přes Ethernet </li>
	<li>s nárůstem provozu ovšem výrazně stoupají prodlevy a klesá propustnost, každý paket je totiž poslán stejným rozhraním, tj. v době, kdy byl poslán jeden fragment, musí vysílací stanice čekat, než jej centrální prvek pošle stejným rozhraním druhé stanici a teprve potom může vysílat další fragment </li>
	<li>výhodou je i velmi snadný přechod na variantu s dvěma aktivními prvky v případě, že je vyžadována větší propustnost, bez velkých utopených nákladů </li>
	<li>jako výhodu lze považovat i to, že je využíván jen jeden frekvenční kanál </li>
	<li>spolu s body A a C se mohou připojovat i klienti, ovšem nelze jim pak přidělit vlastní segment a mohou způsobovat neplechu (dá se řešit prvky s podporou VPN) a ještě více zpomalují síť. Lepší je v tom případě připojit na Ethernet navíc AP vyhrazený čistě pro klienty. </li>
	<li>můžete na AP snadno připojit Ethernet kabel a poskytnout tak Internet v budově, kde je retranslace. </li>
</ul>
<div class="rightbox">
<h5>Aktivní retranslace s více prvky</h5>
<img src="/wp-content/uploads/cache/20041215-activretr2.gif" alt="Aktivní retranslace s více centrálními prvky" width="250" height="157" /></div>
<h5>AP režim se 2 aktivními prvky</h5>
<p>
Tento způsob je velmi podobný předchozímu co se týče podoby, výrazně se ale liší svými vlastnostmi a bývá nejčastějším způsobem řešení retranslace. Při tomto řešení není na retranslačním bodě jeden aktivní prvek, ale dva, které jsou propojeny Ethernetem. Existovaly i prvky se dvěma nezávislými bezdrátovými rozhraními — známé jsou AP-1000 a AP-2000, ty ale nejsou k sehnání a hlavně nemají díky klesající ceně význam. Jediný zajímavý je v tomto ohledu <a href="http://www.wifishop.cz/inshop/scripts/detail.asp?itemId=21082&amp;level=63">AP-4000</a>, který je sice pekelně drahý, zato má neskutečné množství funkcí, nejlepší citlivost na příjem co znám, a možnost provozovat dvě (a díky VPN funkcionalitě třeba sto) nezávislé sítě standardů 802.11b, 802.11a a 802.11g na dvou bezdrátových rozhraních.</p>
<p>
Ale zpět k tématu — každá dvojice prvku v koncovém bodě a prvku na retranslačním bodě (A → R a B → R) tvoří samostatnou síť (vlastně standardní Infrastructure síť s jedním klientem). Je tedy možné mít v centru jak <a href="http://www.wifishop.cz/inshop/scripts/set.asp?Level=79">klientské Ethernet adaptéry</a> (a na krajích AP), tak adaptéry na krajích a uprostřed přístupové body, tak i &#8220;cik-cak režim&#8221; AP → <b>klient → AP</b> → klient (tučně je retranslační bod). Záleží na celkové topologii sítě a na dalších následujících prvcích, zvykem bývá umístit více problematické prvky co nejblíže poskytovateli (aby nemusel jezdit daleko v případě problémů), tj. první AP umístí u sebe a druhý většinou ke klientovi (který jej může na zavolání restartovat).</p>
<p>
V klientském centru jsou pak vždy dvě <a href="http://www.wifishop.cz/inshop/scripts/set.asp?Level=81">směrové antény</a> (existuje možnost i jedné a spojení přes slučovač, ale využívá se toho jen velmi sporadicky).</p>

<ul>
<li>cena řešení je mírně vyšší než předchozí řešení, ale ne tolik, aby to byla nevýhoda </li>
	<li>každý paket putuje postupně přes všechny prvky, nenastává tam žádné čekání, síť je tedy relativně rychlá </li>
	<li>vesměs se používají dva frekvenční kanály (případně jeden a odlišná polarizace), pakliže ale vyzařovací diagramy nezasahují do sebe (pozor na zadní a boční vyzařování u špatných antén typu síto či yagi), je možné použít i jeden frekvenční kanál a polarizaci </li>
	<li>spolu s body A a C se mohou připojovat i klienti, ovšem nelze jim pak přidělit vlastní segment a mohou způsobovat neplechu (dá se řešit prvky s podporou VPN) a zpomalují síť. Lepší je v tom případě propojit centrální prvky přes switch (mají-li jen jeden Ethernet port) a do něj připojit navíc AP vyhrazený čistě pro klienty </li>
	<li>můžete na AP snadno připojit Ethernet kabel a poskytnout tak Internet v budově, kde je retranslace </li>
</ul>
<div class="rightbox">
<h5>Aktivní retranslace s WDS</h5>
<img src="/wp-content/uploads/cache/20041215-activretr3.gif" alt="Aktivní retranslace s využitím WDS" width="250" height="157" /></div>
<h5>AP režim s využitím WDS</h5>
<p>
Tento druh aktivní retranslace je analogický k prvnímu řešení, také využívá jen jeden centrální prvek, ovšem na rozdíl od něj i na krajích (alespoň jednom) je AP. Tyto AP jsou pak propojeny bezdrátově pomocí &#8220;wireless distribution system&#8221; (viz předchozí díly seriálu).</p>

<ul>
<li>cena řešení je obdobná předchozím řešením, WDS jsou dnes vybaveny již téměř všechny prvky. Úspora ale může být při vícenásobných retranslacích (viz následující kapitola) </li>
	<li>rychlost zpracování bývá pomalejší než předchozí varianty, WDS je značný žrout </li>
	<li>výhodou je i velmi snadný přechod na variantu s dvěma aktivními prvky v případě, že je vyžadována větší propustnost, bez velkých utopených nákladů </li>
	<li>musí být v celé WDS síti využit jen jeden frekvenční kanál (tj. když za sebou budete mít hada z pěti sériově WDS propojených AP, celá tato síť bude využívat jednu frekvenci). </li>
	<li>lze propojit jen 5 AP na jiný AP pomocí WDS režimu (kvůli propustnosti se ale nedoporučují více než 2) </li>
	<li>spolu s body A a C se mohou připojovat i klienti, kteří jsou na vlastním segmentu, i tak ale zpomalují síť. Lepší je v tom případě připojit na Ethernet navíc AP vyhrazený čistě pro klienty. </li>
	<li>můžete na AP snadno připojit Ethernet kabel a poskytnout tak Internet v budově, kde je retranslace. </li>
	<li>můžete mít v celé síti jen jeden prvek, síť je tedy snadno spravovatelná </li>
</ul>
	<h5>Další možné topologie a závěr</h5>
<p>
Probral jsem tři nejčastější řešení, zbytek jistě zvládnete sami. Můžete využít i ad-hoc (peer-to-peer) režimu bez přístupových bodů (viz přechozí části seriálu), rozhodně bych to ale z bezpečnostních a managovacích důvodů nedoporučoval. Potřebujete-li udělat řešení přes více retranslací, potom můžete mít na každém druhé retranslaci první způsob a na ostatních druhý (tj. klient → <b>AP</b> → <b>klient + AP</b> → klient — tučně jsou zvýrazněny retranslace, klient + AP znamená, že jsou propojeny Ethernetem), nebo můžete využít čistě druhého řešení (tj. klient → <b>AP + klient</b> → <b>AP + klient</b> → AP nebo AP → <b>klient + klient</b> → <b>AP + AP</b> → klient a nebo jiná kombinace) a nebo i WDS režimu (AP → <b>AP (WDS)</b> → <b>AP (WDS)</b> → klient).</p>
<p>
Potřebujete-li z některého bodu síť rozvětvit, můžete připojit na Ethernet rozhraní další bezdrátový prvek a postupovat analogicky dál, nebo využít opět WDS režimu a připojit další AP a nebo vytvořit topologii tak, aby byl v daném bodě AP (jak vidno z předchozí ukázky, přehazovat to lze libovolně), a pak můžete na daný AP připojit dalšího Ethernet klienta.</p>
<p>
To je vše, co mě k problematice retranslací napadá, máte-li jakékoliv dotazy, dejte vědět v diskusi a zodpovím tam, nebo aktualizuji článek či napíšu pokračování.</p>
