---
ID: 691
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/wap-vyhledavani-ceskych-hotspotu-hotovo

  '
post_date: 2003-11-25 10:22:00
post_excerpt: ''
published: true
summary_points:
- Marigold a.s. spustila WiFi Hotspot Finder pro vyhledávání WiFi sítí v ČR.
- Služba je dostupná přes web marigold.cz/hotspoty a WAP na marigold.cz/wap.
- Funkce SelfFind umožňuje uživatelům vybrat město pro vyhledání hotspotů.
- WAP rozhraní má opravené problémy s délkou zpráv, ořezává je na 1300 znaků.
title: "'WAP vyhledávání českých hotspotů hotovo"

  '
---

<p>
Nejprve formou oficiální tiskové zprávy</p>

<p>
Společnost Marigold a.s. (NYSE:<A href="http://finance.yahoo.com/q?s=MAR&amp;d=t" target=_blank>MAR</A>) oznámila spuštění služby WiFi Hotspot Finder (tm) pro český trh. Díky této službě může každý zájemce o připojení do WiFi sítě zjistit lokalitu, v níž se nachází hotspot s WiFi konektivitou. Služba je dostupná nejenom přes webové rozhraní (<A href="http://www.marigold.cz/hotspoty">marigold.cz/hotspoty</A>), ale také pro mobilní telefony vybavené technologií WAP a to na adrese marigold.cz/wap. </p>

<p>
<EM>&#8222;Naše služba disponuje unikátní technologií nazývanou SelfFind (tm), díky níž jsme schopni automaticky detekovat o kterou lokalitu má uživatel zájem tím, že ji uživatel vybere v menu,&#8220;</EM> říká technický ředitel služby Patrick Zandl. <EM>&#8222;Tím dáváme uživateli veliké možnosti flexibility a více radosti ze života,&#8220;</EM> dodává.</p>

<p>
Nyní jak je to bez korporátního píár jazyka :) </p>

<p>
Včera večer jsem s pomocí četných rad, za něž děkuji (především Broňajzovi) upravil tu chybku ve výběru měst. Ukázalo se, že Genesis má funkci na překódování slova do tvaru vhodného pro předání metodou GET a tato funkce fungovala, stačilo si jen projít dokumentaci ke Genesis :) Takže to nyní funguje tak, že si vyberete ze seznamu město, v němž chcete najít hotspoty (funkce SelfFind :) a ono vám je to vypíše &#8211; jedině Praha je rozdělena na části podle čísla městské části, v Praze je toho hodně a asi by se vám z centra nechtělo jet na Černý most. Doufám, že nebudou problémy s délkou decku ve wapu (=stránka se nenačte), pokud ano, hlašte je.</p>

<p>
Také jsem wap rozhraní zpřístupnil i přes adresu <STRONG>marigold.cz/wap</STRONG> &#8211; původní adresa s koncovou .html funguje nadále. Opravil jsem problémy s délkou decku při čtení delších zpráviček a to tak, že je ořezávám na 1300 znaků a ke zbytku se zatím nedostanete. Posun na další části udělám příště, musím si kvůli tomu nainstalovat už WAPové SDK, protože WML je tak pitomý jazyk, že vyžaduje naprosto rigidní zápis a já nejsem schopen na jednoduchém simulátoru chybky nacházet, bere to dost času zjišťovat, kde jsem co prohodil a pokopal. </p>

<p>
Snad se vám bude mobilní seznam hotspotů hodit &#8211; pokud máte WiFi kartu a občas byste si rádi někde vybrali poštu a nevíte kde, jistě přijde vhod podívat se, kde je nejbližší přípojný bod. </p>

<p>
Někdo mi navrhoval, abych přidal k jednotlivým provozovatelům hotspotů diskusi, není to zlý nápad, udělám to příležitostně. </p>