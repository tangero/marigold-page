---
ID: 2861
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/mezera-na-trhu-dynamicke-cms-pro-staticke-stranky

  '
post_date: 2014-04-03 09:26:32
post_excerpt: ''
published: true
summary_points:
- Firma řeší přípravu statického anglického webu bez dynamických prvků.
- Statické stránky budou uloženy na Amazon S3 pro snadné zvládnutí zátěže.
- Hledá se webové CMS pro více uživatelů s možností generování statických stránek.
- Stávající řešení jsou buď lokální, nebo závislá na Dropboxu, což není ideální.
title: 'Mezera na trhu: dynamické CMS pro statické stránky'
---

<p>Řešíme ve firmě přípravu anglického webu. Tak nějak jsme se shodli, že pro naše potřeby presentace, kde každá stránka je jiná, nejsou potřeba žádné dynamické prvky jako diskuse (však je to firemní web) atd, případně se vkládají beztak přes javascript, je nejlepší udělat stránky statické. A když statické, tak je uložit na Amazon S3, odkud se pohrnou v libovolné zátěži. Jenže přišel problém, jak to rozumně obsloužit. A vypadla mi tím zajímavá mezena na trhu. </p>


<!--more-->

<p>Abych to upřesnil. Já vím, že existuje řada static webpage generátorů, které si na lokále instalujete, ony vám pomáhají udržovat patičky, hlavičky jednotné, mají šablonovací systémy a na závěr vaší práce vygenerují statickou stránku. Přehled takových nástrojů <a href="http://staticsitegenerators.net">najdete zde</a>. Jenže já si nechci na lokále instalovat dost nepřehledné programy ovládané z příkazové řádky. Pro Mac existuje ještě desktop software <a href="http://cactusformac.com">Cactus for Mac</a>. To už je mnohem lepší, ale pořád jednouživatelské, nikoliv ideální. </p>

<p>Co by se líbilo mě: webové CMS, kde se registruju, zaplatím pár doláčů za web a ono to více uživatelům umožní připravovat a editovat stránky pomocí CMS podobně, jako třeba Wordpress. A pak se stiskne tlačítko, nebo po schválené editaci, se vygeneruje statická verze a ta se nahraje na S3 nebo přes FTP na cílový web jako statická stránka. K mému překvapení jsem nic takového nenašel. Existuje celá řada služeb, které to umí na lokále, viz výše, pár služeb se snaží vytvořit něco tím způsobem, že si na Dropboxu píšete texty a ono je to jednou za čas slízne a vypublikuje, jenže tam nebývá velká variabilita vzhledu, navíc je to nepraktické pro více uživatelů, závyslé na Dropboxu a krom toho o publikování se stará strana, které věřím co do výkonu méně, než Amazonu. </p>

<p>Základní aspekty takového systému jsou (soudím):</p>

<ul>
<li>web administrace (hostovaná, netřeba instalovat, ale zato s placením za službu :)</li>
<li>šablony</li>
<li>podpora více uživatelů s alespoň mírným workflow (tedy někdo, kdo i schvaluje, někdo, kdo jen edituje)</li>
<li>běžná struktura - homepage, rubriky a k nim příslušné podstránky, články (blog)</li>
<li>vygenerování statického webu a publikace přes FTP/S3. </li>
</ul>
<p>Když něco takového někde najdete, dejte vědět do komentářů. </p>

<p>A proč na to nechci nějaké CMS jako GetSimple nebo Wordpress? Protože ty se musí instalovat a udržovat - a S3 je nepodporuje, ta hostuje jen statické soubory. </p>

<p>PS: Pokud se divíte, proč statické stránky, tak ty se docela vracejí do módy, minimálně ve firemních instalacích. A zejména ve spojení s cloudovým webhostingem jsou zajímavé pro zahraniční firmy, kterým se tu a tam návštěvnost firemního webu vyhoupne přes limit jejich hostingu a kde S3 je fest zajímavá alternativa. </p>