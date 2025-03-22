---
ID: 2962
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/mqtt-a-docker-jako-korist-pro-internet-veci-z-konference-thingmonk

  '
post_date: 2014-12-04 16:04:56
post_excerpt: ''
published: true
summary_points:
- Michal, Vlasta a Vojta navštívili londýnský ThingMonk, hackerskou akci zaměřenou
  na Internet věcí.
- Docker, původně neznámá technologie, se díky ThingMonku posunul do mainstreamu.
- MQTT protokol od IBM je využíván pro efektivní komunikaci mezi IoT zařízeními.
- Británie aktivně podporuje IoT skrze vládní iniciativy pro rozvoj digitální ekonomiky.
title: "MQTT a Docker jako kořist pro Internet věcí z konference ThingMonk"
---

<p>Tento týden Michal s Vlastou a Vojtou vyrazili na akci ThingMonk do Londýna, tím je minula krásná ledovka na Moravě, ale zase si užili poněkud hackerskou akci věnovanou hlavně Internetu věcí, tedy *ajotám* - IoT. <a href="http://thingmonk.com">ThingMonk</a> je fajnová akcička mimo korportání konferenční mainstream a levotočivé inspirativní slámomlaty jako je TEDx. Zaměřuje se na *bleeding edge* technologie, což je takový překladatelský oříšek, nazval bych to technologie krev a mlíko, kdy nevíte, jestli převáží krev a na technologii vykrvácíte, nebo mléko a hezky se napapkáte. Zjednodušeně řečeno, jde o setkání lidí, kteří dělají s technologiemi tak novými, že Root o nich napíše za rok aktualitu. No a tam kluci vyrazili.</p>


<!--more-->

<p>Už vloni to bylo inspirativní, tehdy se tu hovořilo o neznámé technologii <a href="http://www.docker.com">Docker</a>, což je taková fantasmagorická ptákovina, která nemůže na nic být. Zjednodušeně řečeno (exprti prominou) je Docker takový kontajner na software: naházíte do něj software včetně všech nastavení a pak ho vybalíte tam, kde ho chcete mít. Jak by řekl průměrně zdatný komentátor, blbost. A nám se takové blbosti hodí. Tahle například k tomu, že si očekujeme, jak je na tom výkon našeho cloudu a pokud se nám zdá, že by chtěl trochu potunit, přihodíme další server a z Dockeru na něj vybalíme to, co je potřeba, aby tam bylo. Všechno běží automaticky, otevření i uzavření serverové pozice se udá v zásadě ihned a technici to poznají na konzoli, já na měsíčním výpisu z účtu. Paráda, která v Česku na nic není, protože proč byste v Česku měli něco v cloudu, tady vám na celorepublikové noviny na webu stačí vykešovaný wordpress.</p>

<p>Za ten rok se Docker obrovsky posunul - když jsme po něm začali pokukovat, byl to půl roku starý projekt, letos v září na DockerConu už to byl zralý a výborný produkt, dnes už je to skvělé prostředí, které se spoluprací s velkými cloudovými hráči stává téměř mainstreamem. Jednu věc nám umožňuje moc hezky: komodizovat výdaje za cloud. Pokud se nám zachce, vezme si své saky-paky a pomocí Dockeru je přesuneme jinam.</p>

<p>Docker byla kořist z loňského ThingMonku (ten jsme sledovali jen telemostem), letos jsou to hlavně poznatky o bezpečnosti v MQTT. To je komunikační protokol mezi “ajotami”, který tlačí IBM <em>(to jméno asi neznáte, ale dejte na mě, to jsou chytrý kluci z Ameriky a ještě o nich uslyšíme)</em>. MQTT je protokol na efektivní výměnu krátkých stavových zpráv, něco jako ICQ pro M2M. My jsme s ním začali vloni pod Androidem na Quelu, teď ho posouváme do veškeré naší infrastruktury, od čehož si slibujeme větší otevřenost a kombinovatelnost s jinými produkty, ale také větší robustnost a škálovatelnost v zátěži. Všechno je věc firmware naší gateway. Apropos, k bezpečnosti - veškerá komunikace u nás na nových gateway je end to end šifrovaná, což je v oblasti IoT světlá výjimka. Čímž se dostáváme k tomu, že vlatně všechno krom rádiového protokolu je na naší infrastruktuře standardní a propojitelné. Rádio je proprietární proto, že nebylo po ruce žádné standardní, levné a výkonné. </p>

<p>Příjemné je vidět, že nejsme nějaká česká firmička na okraji technovývoje. Spíš naopak, máme hodně praktických zkušeností s věcmi, které se jinde teprve teoreticky používají, naši kluci si o tom na rovinu povídají s autory těch technologií a po té nerdovské stránce je to fajn.</p>

<p>Zajímavý je také odlišný přístup. V Británii, kde ThingMonk probíhá, se do IoT ostře obouvá místní vláda, která v tom vidí příležitost, jak tlačit moderní pracovní místa a digitální ekonomiku. Mají tu “digitálního ministra”, který má moderní technologie v popisu práce a už dávno tím nemyslí výstavbu skladů pro eshopy. Digitální ministr se zde <a href="http://www.v3.co.uk/v3-uk/news/2371855/uk-must-ride-the-internet-of-things-wave-urges-digital-minister">nedávno rozhorloval</a>, že Británie musí v Internetu věcí přidat a být na špičce. Má pro to řadu dobrých důvodů, mimo jiné i ten, že Británie začíná mít problémy se zajištěním dostatku elektřiny a jedním z úsporných plánů je nasazení chytrých technologií na bázi IoT, které pomůžou šetřit, od nejrůznějších Inhome displejů a monitoringů spotřeby, které ostatně za tím účelem připravujeme, přes automatizace spotřeby a rozvodů elektřiny až po cokoliv, co ještě nemá ani jméno. Ale dalším dobrým důvodem pro tlačení IoT je touha po tom, aby se Británie držela na špici technologického vývoje. A tak má Británie masivní vládní podporu zahrnující soutěže, aktivní vládní účast v nejrůznějších akcelerátorech a startupových školičkách a také fondy podpory. A taky dostatek positivních příkladů.</p>