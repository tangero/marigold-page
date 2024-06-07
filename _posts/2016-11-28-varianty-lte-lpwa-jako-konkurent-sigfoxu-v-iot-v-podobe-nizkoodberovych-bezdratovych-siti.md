---
ID: 3356
title: 'Varianty LTE LPWA jako konkurent Sigfoxu v&nbsp;IoT v&nbsp;podobě nízkoodběrových bezdrátových sítí'
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/varianty-lte-lpwa-jako-konkurent-sigfoxu-v-iot-v-podobe-nizkoodberovych-bezdratovych-siti
published: true
post_date: 2016-11-28 19:57:50
---
<p>V Česku se prosazuje hlavně Sigfox coby síť pro přenosy stavových informací Internetu věcí, protože tu má charismatické a tlačící lidi s T-Mobile v zády, ale ve světě není situace zdaleka tak jednoznačná. Sigfox patří mezi jednu z vůdčích firem, jenže ostatní brousí jako ohaři. I u nás mají České Radiokomunikace síť LoRa a jistá váhavost O2 má své důvody. Tím prvním je skutečnost, že firma má zrovna fofr obhájit před majitelem obchodní výsledky a nemůže se pouštět do větších samostatných akcí, vytěžuje ji akvizice pro O2TV a nové lukrativní naleziště s názvem Smart Cities. Ale docela takhle to není, protože O2 vidí budoucnost v LTE “Nule” - tedy v zařízeních Category 0 v Release 12 a dalších návazných technologiích. Abychom se zorientovali, podívejme se, kam kráčí LTE v oblasti <strong>LPWA, Low Power Wide Area</strong>, jak se tyhle technologie souhrnně nazývají. </p>


<!--more-->

<h3>LTE pro IoT</h3>
<p>Tak především je dobré znovu připomenout, že LTE už dávno není jedna modulační technologie a jedna frekvence. Vlastně nikdy nebyla. Je to chumel frekvencí, modulací a přístupů k rádiovému spektru, často velmi odlišných. Už jen v rádiu jde o rozpětí 450 MHz až 5,2 GHz a pravděpodobně ještě výše. Zařízení mohou používat ty frekvence, modulace a přístupy, které jsou pro konkrétní použití nejvhodnější a je jasné, že rychlý datový stream nemá ty samé vlastnosti a nároky, jako dávkové a stručné přenosy telemetrických dat. A protože budoucnost má být v čistě mezistrojové komunikaci, která se v terminologii 3GPP nazývá MTC (Machine Type Communication) nebo M2M - Machine to Machine, tak i pro ni je potřeba nalézt provozní optimum a již nyní je zřejmé, že nevyhoví jeden způsob všem. </p>

<h3>Kategorie v LTE Release 12 a Release 13</h3>
<p>Předposlední stabilní specifikací byla Release 12, která specifikuje čtrnáct provozních kategorií zařízení LTE (Release 14 jich předpokládá cca 20, <a href="http://niviuk.free.fr/ue_category.php">přehled zde</a>). Pro nás je zajímavá Category 0 míněná jako kategorie komunikace pro Internet věcí. Na obrázku je vidět, jaké má parametry v porovnání s předchozí Cat 1 v Release 8, jejímž hlavním problémem byla relativně vysoká cena modemů a žravost, jakou u IoT nevyvážila ani vysoká rychlost přenosu a plně duplexní přenos. </p>

<p><img title="lte-iot-rel.png" src="https://www.marigold.cz/wp-content/uploads/lte-iot-rel.png" alt="Lte iot rel" width="599" height="308" border="0" /></p>

<p>Hlavní důvody nižší komplexnosti LTE Rel-12 Cat. 0 se promítají do výrazně nižší ceny, která má klesnout ještě více u Release 13. Tam se projeví především nižší šířka obsluhovaného pásma, existuje i vysloveně úzkopásmová (NB - narrow band) verze se 180 KHz pásma, což se velmi příznivě projeví jak ve výrobní ceně, tak ve výdrži zařízení a jeho poruchovosti, přičemž rychlost do 200 Kb/s je pro stavový přenos informací ještě vcelku dostatečná. Značnou výhodou Narrow Band verze (NB-LTE nebo někdy též Cat-M2, ale to nejsou oficiální označení) je také skutečnost, že může pracovat nejenom na vyhrazené frekvenci, ale i v doposud nevyužívaném guard-band (hraničním pásmu) a dokonce může být provozováno na překryvné (respektive podkresové) frekvenci v rámci existujícího LTE bloku, takže neukusuje z potřebné frekvence. </p>

<p>Všechny tři funkční režimy ilustruje následující obrázek:</p>

<p><img title="lte-iot-mode.png" src="https://www.marigold.cz/wp-content/uploads/lte-iot-mode.png" alt="Lte iot mode" width="599" height="185" border="0" /></p>

<ul>
<li><strong>Inband mode</strong> znamená, že v rámci frekvence využívané pro LTE je užit minimálně jeden rádiový blok (tedy minimálně 200 KHz) pro LTE-NB. </li>
<li><strong>Guardband mode</strong> znamená, že doposud volné hraniční pásmo oddělující dvě odlišně používané LTE frekvence (například dvěmi operátory) nyní vyplní LTE-NB. </li>
<li><strong>Standalone Mode</strong> znamená provoz LTE-NB v rámci frekvence užívané jiným, než LTE systémem, například v rámci GSM. Zde se výhodně projeví fakt, že 200 KHz je stejná šířka pásma, jakou používá jeden kanál GSM. </li>
</ul>
<p>Obě kategorie M1 a NB-IoT prošly schválením v rámci Release 13 v létě 2016 a výrobci s nimi tedy již mohou počítat. V současné chvíli jsou dostupné čipové sady Qualcommu MDM9206 v rámci řady MDM9x07, které podporují CatM1 a jsou rozšiřitelné v budoucnu upgradem na NB-IOT, podobně slibují i další výrobci křemíku. Již několik dodavatelů hlásí pokusné dodávky a několik operátorů také pokusné provozy (berme to s rezervou, to znamená, že to leží někde na stole v baráku a vedle jediný dvě mašinky, co se k tomu sehnaly).</p>

<p>To ale není spravedlivá odpověď na naši otázku pozice LTE v LPWA světě a IoT. LTE je již nyní velmi komplexní záležitost a ukazuje se, že pro jednoduché úkoly to může být smrtící. Proto jednou z úprav, ke kterým v rámci LTE dochází, je také autonomní provoz, oproštění se od rozsáhlého datového pozadí velké mobilní sítě a přiblížení se jednoduchému fungování rádiových sítí v provopočátcích. To vychází vstříc vývojářům, kteří chtějí něco rychle naprototypovat, ozkoušet zájem trhu a teprve později si hrát s vyšší robustností, bezpečností atd. Je to ostatně přirozená obrana proti LoRa/Sigfox, které na to jdou právě z té druhé strany, ze strany přirozené jednoduchosti, neboť jsou sítěmi, které nabízejí jen to, co potřebujete a vlastně nic navíc. Díky tomu je možné tlačit dolů ceny hardware, což je aspekt v branži Internetu věcí nesmírně důležitý. </p>

<p>Tady je pár zásad, které v rámci své vize Massive IoT propaguje Ericsson:</p>

<p> </p>

<p><img title="ericsson-massive-iot.png" src="https://www.marigold.cz/wp-content/uploads/ericsson-massive-iot.png" alt="Ericsson massive iot" width="500" height="178" border="0" /></p>

<p>Takhle si to představuje uBlox (v zásadě to samý)</p>

<p><img title="ublox-massive-mtc.png" src="https://www.marigold.cz/wp-content/uploads/ublox-massive-mtc.png" alt="Ublox massive mtc" width="500" height="242" border="0" /></p>

<p> </p>

<p>Ostatní tomu říkají opatrněji Massive MTC, ale hlásí se k podobným zásadám.  </p>

<h3>Jak na tom bude LTE vůči Sigfoxu, LoRa a dalším?</h3>
<p>To teď není tak snadné říct. LTE je zatím pro IoT dost těžká váha, zatímco Sigfox zatím často příliš lehká váha. LTE musí ustoupit ze svého výkonu (a tím i ceny, komplexnosti, náročnosti), zatímco Sigfox musí posílit, pokud nechce být niche technologií pro specifické účely. V tomto ohledu před sebou oba (a také LoRa a další) mají kus cesty. </p>

<p>LTE dnes představuje celkem 43 různých frekvencí a ne všude jsou dostupné. I když dnes koupíte nějaký prototyp NB-LTE a budete na něm chtít postavit své řešení, neseženete NB-LTE síť, ve které byste jej provozovali a do budoucna budete mít problémy právě s těmi různými frekvencemi. V Sigfoxu je to s frekvencemi podstatně jednodušší, ale zase složitější je to tam s roamingem. Pokud budete chtít dělat globální řešení, nebude to se Sigfoxem tak elegantní jako v LTE.</p>

<p>Pokud se teď urgentně potřebujete rozhodnout, záleží právě na té urgentnosti. Chytit se Sigfoxu, LoRa a dalších, kteří již existují a doufat, že vydrží, případně budou stíhat další vývoj, nebo počkat na masivnější a standardní LTE, kterému to ale ještě chvíli potrvá, než bude připravené na trhu?  Dobrá porovnávací technologická tabulka pro jednotlivé technologie <a href="http://www.cnx-software.com/wp-content/uploads/2015/09/LPWAN_Comparison_Table.png">je zde</a>, můžete se zkusit zorientovat. Není tu ale žádná univerzální rada. Pokud chcete být rychle na trhu, Sigfox vypadá na nejlepší volbu nyní, ale buďte připraveni jej opustit, kdyby nešel dostatečně rychle kupředu, tedy buďte platformově nezávislí. </p>

<p>Na trhu bude záležet na tom, jak se velkým operátorům, kteří dnes mají na LTE monopol, bude dařit obchodně. Zatímco evangelizační fáze trhu, kdy se oslovují dynamicky se rozvíjející firmy schopné rychle svou technologii portovat a propojit na LPWA velkým operátorům vůbec nejde, jde jim naopak dobře marketingový tlak a působení na velké nadnárodní firmy. Ty zase nejsou nejdynamičtější a o okamžitém přínosu Internetu věcí nejsou přesvědčeny, takže budou zřejmě vyčkávat. Situace bude zřetelnější až v tu chvíli, do té doby jde o pusté spekulace. </p>

<p>K pozornosti doporučuji následující dokumenty (PDF):</p>

<ul>
<li><a href="https://www.ericsson.com/res/docs/whitepapers/wp_iot.pdf">Ericsson: Cellular networks for Massive IOT</a></li>
<li><a href="http://www.3gpp.org/news-events/3gpp-news/1766-iot_progress">Stránka 3GPP věnovaná posunům v sítích pro IoT a jednotlivým technologiím</a></li>
<li><a href="http://www.3gpp.org/images/presentations/3GPP_Standards_for_IoT.pdf">3GPP presentace stávajících 3GPP technologií pro IOT</a></li>
<li><a href="https://arxiv.org/pdf/1606.04171.pdf">A Primer on 3GPP Narrowband Internet of Things (NB-IoT)</a></li>
</ul>