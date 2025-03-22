---
ID: 2113
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/u-novych-google-analytics-se-nemuzu-dohledat-par-funkci

  '
post_date: 2007-06-11 06:14:51
post_excerpt: ''
published: true
summary_points:
- Nové Google Analytics postrádají detailní report Entrance Paths, zobrazují jen deset
  nejčastějších cest.
- Textový export dat do HTML pro snadné kopírování do Excelu v nových Analytics chybí.
- Funely, zobrazující cesty uživatelů, v nových Google Analytics chybí, Goals je nenahradí.
- Autor hledá sofistikovanější alternativy Google Analytics, například eMerite nebo
  ClickTracks.
title: U nových Google Analytics se nemůžu dohledat pár funkcí
---

Mějte mne za zkostnatělého, ale novým Google Analytics nemůžu nějak přijít na chuť. Ty starý byly sice ošklivější, ale v těch nových prostě nevím, jak se doklikat na data, která v těch starých byla na pár kliknutí. 

Google Analytics jsou skvělý nástroj pro lidi, kteří holdují číslíčkům, což já jsem. A jsou mocné, pokud se v nich mocně orientujete. Starou verzi jsem znal po slepu. V nové to buďto neumím najít, nebo to tam není a jelikož přístup do staré verze asi brzy zmizí, bude mi ouvej. 

Rozumějte. Základní data presentují nové Analytics pohodlněji a přehledněji, než ty staré. Jenže základní data jsou na povšechný přehled a detailní analýzy z nich neuděláte. 

<h3>Dodrbané Entrance Paths</h3>
Prvním reportem, který mi dělá starost, je Entrance Paths, tedy cesta, jíž putují lidé po vstupu na váš web. Na Marigoldu je mi to fuk, ale na Streamu jsou to důležitá čísla. Teoreticky bych se z nich měl dozvědět, jaké navigační prvky a jak lidé využívají. 
<!--more-->

Problém je, že v nových sestavách to graficky je sice hezčí, ale vypisuje se mi pouze dalších deset nejpoužívanějších stránek,  na které lidé odešli. K těm všem zbývajícím netuším, jak se dostat a kdybyste to někdo věděli, podělte  se o to se mnou prosím - ani export nezafungoval, vždy vytáhne jen těch deset. Přes starou sestavu to samozřejmě jde. 

<a href="http://www.marigold.cz/wp-content/google-analytics.png"><img src="http://www.marigold.cz/wp-content/_google-analytics.png" width="450" height="332" alt="Google Analytics Entrance Paths - nelze listovat" title="Google Analytics Entrance Paths - nelze listovat"  /></a>

Lze také namítnout, že právě k tomuhle je funkce Site Overlay. Namítnout to můžete, ale není to zcela pravda - tahle sestava je vhodná jen pro málo se měnící stránku, protože nebere oblasti, ale bere konkrétní URL. Takže když v nějaké oblasti máte často se měnící URL (což u zpravodajských serverů bývá typické), je vám Site Overlay na nic, využívanost jednotlivých oblastí titulní stránky serveru nespočítá. Na to musíte ručně natáhnout Entrance Paths do Excelu a chvilku laborovat se sčítáním url, která začínají podobně. 

Na co taková analýza vůbec je? Třeba se u nás diskutovalo o tom, že lidé nevědí, co jsou tagy a že bychom je měli zrušit. Připomínku samozřejmě vznesl někdo, kdo si průzkum udělal na třech svých kamarádech, což rozhodně nebyli ajtíci. A tak jsem se ponořil do Analytics a namítl, že lidé možná nevědí, co to je, ale je to jeden z nejpoužívanějších prvků navigace a že deset procent lidí opouští titulku Streamu přes tagy.  

<h3>Textový export pro Excel</h3>

Když už jsme u exportu dat, chybí mi původní textová sestava, která data zobrazila textově v HTML stránce. Z ní se totiž data pohodlně dala zkopírovat přes copy - paste do Excelu. Pravda, lze je uložit jako CSV a pak načíst, je to ale méně pohodlné. Škoda toho.

Proč musí člověk u Analytics bádat s Excelem? Analytics sice umí data sbírat a základně je vyhodnocovat, větší vyhodnocení si musí dělat stejně člověk sám. Například samotná analýza návštěvnosti. Neznám software, který by se obtěžoval s trochou statistické analýzy a GA nejsou výjimkou. Regresní křivku si musíte modelovat v Excelu, ačkoliv to není nic, co by webová stránka nezvládla. Lineární regrese je přitom ideální k rozpoznávání trendů. Jak poznáte, že vám návštěvnost roste? Když jsou čísla vyšší, než starší čísla? No, to dá rozum. Jenže co když se do návštěvnosti promítají různé kampaně, víkendy, svátky a vy analyzujete denní návštěvnost? Pak musíte po lineární regresi sáhnout, abyste data zpacifikovali a viděli v nich nějaký věrohodný trend. Nebo jsem sám, kdo si to myslí?

<h3>Funely nenahradí Goals</h3>

Poslední mrzutost u nových GA, jsou chybějící funely. Tedy - ony nebyly ani původně, takže se neztratily, jen jsem doufal, že naopak přibudou. Funely jsou cesty, jimiž lidé procházejí po webu. Je důležité vědět, jakým způsobem se lidé po webu pohybují, jak se schovají. Zase namítnete, že nějaké funely v GA jsou a nebo že mám používat Entrance Paths, které jsou k tomu přímo určeny. To je pravda - jenže Entrance Paths mi neumožní data zobecnit. Tahle sestava mi říká, kolik lidí z titulní stránky odešlo na který konkrétní článek. Já ale spíše potřebuji vědět, kolik lidí z titulní stránky odešlo na články obecně, což umím omezit přes URL, do GA se mi to ale zadat nepodařilo. Můžete si nastavit Goals, ale to je něco trochu jiného, navíc jste omezeni na tři goals. Existují přitom software, které umožňují zgrupovat URL například tak, že všechna URL, v nichž se vyskytuje /clanek/ a /zprava/ hodí do skupiny Články a pak vám řekne počet a procentáž lidí, kteří na tutu skupinu odešli. Bohužel jsou to serverové software, které mi tu nikdo nekoupí, takže hledám webové sestavy. Kdybyste někdo věděl, jaký webreportovací soft to umí, dejte vědět - i si ho zaplatím, cožpak o to. 

Goals nejsou funely, i když se tak použít dají pro případ nouze, jenže můžete použít jen čtyři Goals. Goals je pevně stanovená cesta, kterou musíte projít, aby se něco stalo, například abyste koupili zboží. Sestava Goals webmasterovi řekne, kolik lidí celým procesem prošlo a případně, kdy z něj vypadli. Z toho webmaster pozná, kde ho tlačí bota - pokud mu nápadně moc lidí vypadne při povinné registraci do nákupního košíku, asi by na ní měl zapracovat. Funel je oproti tomu sestava obsahová a jen řekne, kterými trasami se lidé pohybují. Goals používám k tomu, abych sledoval, kolik lidí uploaduje video nebo se registruje. Jistě, že to v konečném důsledku vidím v administraci Streamu, ale nevidím například to zajímavé číslo, že jen 34% lidí, kteří přijdou na stránku uploadu videa, opravdu nějaké video nahrají. 

Takže: znáte nebo používáte jiné měření návštěvnosti, které mají sofistikovanější úroveň, než GA? Hlavně nemluvte o Navrcholu, NetMonitoru nebo Toplistu, to jsou opravdu velmi základní služby, které mi proti GA nedají nic navíc. Spíše mi jde o aktuální zkušenosti s <a href="http://www.emerite.cz">eMerite</a>, <a href="http://www.clicktracks.cz/">ClickTracks</a> nebo s nějakými zahraničními placenými službami.