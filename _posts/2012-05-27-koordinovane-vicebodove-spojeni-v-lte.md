---
ID: 2416
title: 'Koordinované vícebodové spojení v&nbsp;LTE'
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/koordinovane-vicebodove-spojeni-v-lte
published: true
post_date: 2012-05-27 21:42:10
categories: [3G, Mobilní sítě]
---
<p>Jednou z uvažovaných novinek pro vysokorychlostní datové mobilní přenosy v bezdrátových sítích je takzvané<em> “koordinované vícebodové spojení”</em>, anglicky <strong>Coordinated MultiPoint (CoMP)</strong>. Jde o další cestu, jakou by se mohly bezdrátové sítě dobrat vyšší rychlosti i efektivity (rychlostní i kapacitní).</p>

<!--more-->

<p>Nejdříve trocha kontextu. Dnešní technologie zrychlování dat na rádiu jdou několika směry, především zjednodušením architektury sítě a přiblížením rozhodujících prvků sítě co nejblíže k uživatelskému terminálu - tedy zhusta k základnové stanici, aby data neputovala tam a zpět přes řadu síťových prvků, které data zpomalí. Zde už koordinace v rámci LTE dosáhla optima, přes nějž bude těžké se posunout, ačkoliv ani tyto cesty nejsou zavřeny - zlepšování má podobu nejrůznějších femto, piko a nanocell, ale také přesunu řady úkolů na mobilní stanici. <br /><br />Druhou variantou je nejrůznější balení větších částí rádiového spektra pro jednu mobilku. Zatímco klasické UMTS počítalo s pětimegahertzovou šířkou komunikačního kanálu, LTE se nestydí ani za dvacet či dokonce čtyřicet a více MHz a to klidně přes několik frekvenčních pásem. Zřejmou nevýhodou tohoto přístupu je hojné drancování baterky mobilky nárůstem potřebného výpočetního výkonu a baterka se stává úzkým hrdlem dnešních zařízení. Druhou, méně zřejmou, ale od toho odvozenou nevýhodou, je nutnost rozsáhlé integrace čipových sad mobilek. Čipové sady musí obsluhovat několik (nezřídka více jak desítku) rádiových pásem, musí koordinovat dělbu dat mezi ně a to s ohledem na spotřebu. K zefektivnění tohoto postupu pak přicházejí různé záležitosti typu složených antén, formování rádiového paprsku a podobné workaroundy, které mají způsobit, že se dotyčná rychlodatující mobilka nestane jedinou takovou v rámci buňky.<br /><br />To vše ponecháme dnes stranou. Podíváme se na přístup, který je uvažován jak pro LTE-Advanced, tak pro WiMax a který je rozpracován v podobně 3GPP Release 11 v rámci <a href="http://www.3gpp.org/ftp/tsg_ran/TSG_RAN../TSGR_53/Docs/RP-111117.zip">RP-111117</a>. Což obojí znamená, že s koordinovaným vícebodovým spojením se v praxi stěží potkáte na barcelonském výstavišti, natož v LTE síti a v Česku … darmo mluvit... <br /><br />Koordinované vícebodové spojení v LTE-Advanced jde na záležitost zrychlování dat jinak. Poprvé (fakticky) může mobilka využívat zdroje z více radiových zdrojů. Až doposud panoval vcelku odůvodněný úzus, že mobilní stanice je připojena právě k jedné základnové stanici či buňce a její zdroje využívá. Pokud se chce připojit k jiné, musí provést handover, předání spojení. Své důvody to mělo - šlo o rádiově jednoduchou a čistou věc, kterou s výpočetní kapacitou mobilek a nakonec i základnovek na přelomu tisíciletí nešlo řešit o mnoho jinak.<br /><br /></p>
<h2>Problém rychlosti na hranici buňky</h2>
<p>V CoMP může mobilka komunikovat s více (zatím uvažujme dvěma) přenosovými body, záměrně neříkám základnovými stanicemi, což osvětílme později. Proč by to mělo být zajímavé? Pokud je mobilka dostatečně blízko základnové stanici, není potíž dosáhnout vysokých přenosových rychlostí, ale se vzdáleností přenosová rychlost padá dolů. Plné rychlosti DC (dual carrier, provoz na dvou přenašečích) jako je 42 Mb/s v downlinku, jsou dosažitelné spíše stovky metrů od základnové stanice, jakmile je mobilka spíše kilometry, klesá rychlost zásadně. Problém je odvozen od značného zašumění na rozhraní dvou buněk v případě, že faktor frekvenčního znovuvyužití se blíží či je roven jedné. A typické užití UMTS/LTE je právě s N=1, tedy situace, kdy všechny buňky používají stejnou frekvenci. Jelikož typický operátor nemívá více, jak tři základní kanály v jednom frekvenčním pásmu (tedy po 5MHz šířky), není ani pro mnoho jiných konfigurací prostor. <br /><br />To nám mimochodem dává docela důstojnou odpověď na otázku, jak to, že reálné přenosové rychlosti v českých mobilních sítích jsou tak truchlivé - základnové stanice nejsou tak hustě, uživatelé se velmi často pohybují v rámci cell-edge problému a zle to vydýchávají. Pro představu, jak velký je problém, připomeňme požadavky na LTE-Advancer v rámci TR 36.913, kde se předpokládá třicetinásobná dostupná průměrná přenosová rychlost oproti rychlosti dostupné na okrajích buněk. <br /><br />Zašumění na krajích buněk (označované jako cell edge problem) se řeší různě. Jednou z možností je FFR, fraction frequency reuse, jenže to už z principu nabourává N=1, další možností jsou pak větší změny v architektuře. A elegantním řešením je právě CoMP. CoMP těží z toho, že většina inteligence sítě se postupem doby od časů legacy 3G (Release 99) přesunula k základnovým stanicím eNodeB a dokonce v posledních návrzích se uvažuje o atomizaci eNB na subčást RRE - Remote Radio Equipment, vzdálené rádiové vybavení. <br /><br />Použití CoMP zvyšuje efektivní přenosovou rychlost využitelnou mobilkou a to o mnoho desítek procent. Teoreticky. V praxi hodně záleží na tom, jak bude systém dotažený a který z přístupů se využije. <br /><br />Existují dvě základní varianty CoMP, které se liší způsobem distribuce dat a především tím, zda jsou data dostupná najednou z více rádiových zdrojů v síti: Koordinované plánování a formování paprsku (CS/CB) a Společné zpracování (Joint Processing), které má dvě subvarianty: DCS a JT, přičemž každá má své výhody a nevýhody. <br /><br /><strong>Coordinated Scheduling/Coordinated Beamforming čili Koordinované plánování a formování radiového paprsku</strong> - označovaný též zkratkou CS/CB obnáší model, kdy odesílaná data jsou dostupná pouze na obslužných buňkách - tady se využívá koncept RRE. Nelze tedy CoMP provozovat mezi dvěmi eNodeB, ale v rámci prostoru (buněk) obsluhovaných jedním eNodeB. Řízení provozu a formování radiového paprsku směrem k uživateli se dělá s ohledem komunikaci s mobilkou ze dvou buněk. Asi tušíme, že to přináší značnou režii na zpracování matic pro formování paprsku. <br /><br /><strong>JT neboli </strong></span><strong>Joint Transmision, Spřažený přenos</strong>, obnáší simultánní odesílání dat do mobilky ze dvou buněk, přičemž mobilka obdržený signál buďto skládá, nebo kombinuje na přijímači. <br /><br /><strong>Dynamická volba buňky, DCS - dynamic cell selection</strong>, je druhou variantou Společného zpracování, kdy jsou data dostupná na více buňkách. V tomto případě jsou data sice vysílána z více zdrojů, ale mobilka vyhodnotí ten nejlepší a ten použije. Čím se to liší od handoveru? Hlavně rychlostí, kdy mobilka zkrátka použije ta lepší a rychlejší data, k faktickému předání spojení na jiné eNodeB neproběhne.<br /></span></p>
<p>
<div style="text-align: center;"><img src="http://www.marigold.cz/wp-content/uploads/lte-comp.jpg" border="1" alt="Lte comp" width="566" height="600" /><br /><em>Ilustrační obrázek pochází z NTT DoCoMo Technical Journal Vol. 12</em></div>
</p>
<p>Hlavní faktický rozdíl mezi Společným zpracováním a CS/CB schématem je v tom, že v případě JP je potřeba optická síť propojující buňky, jinak nejde datové toky udržet na požadovaných hodnotách. To stojí peníze. JT umožní vyšší výkon, ale také má vyšší náklady na přenosovou páteřní síť. Je to něco za něco. <br /><br />To jsme hovořili o downlinku. V uplinku používá CoMP faktu, že je k dispozici několik geograficky oddělených antén, takže může přijímat signál z mobilky na více místech a vybrat ten nejlepší, co se rušení týká - nebo se dokonce pokusit jej rekonstruovat. Jasnou výhodou je, že v tomto případě může být technologie použita bez nutnosti změn na straně mobilky - té je jedno, kolik buněk ji poslouchá, důležité pro ni je, kolik s ní komunikuje. <br /><br />Sečteno a podtrženo, koordinované vícebodové spojení je jedním z horkých kandidátů na zrychlování LTE sítí, osobně jej považuji za významnější zlepšení, než třeba HetNet, protože adresuje problém, který zkrátka je významný a to výkon na okrajích buněk. <br /><br />Jenže už z hrubého popisu jasně cítíme, že tu jsou velké “výzvy”. Když odpočteme problémy se zpracováním matic pro beamforming, jež obnášejí požadovaný vyšší výpočetní výkon, připočtěme si hlavně obrovský dopad na páteřní a propojovací sítě takového LTE. Nejenom, že dochází k přenosům redundantních bloků dat (tedy je požadována kapacita), ale hlavně koordinace mobilky a eNodeB/RRE přes interface S1 obnáší značné nároky na nízkou latenci, jinak nemá vyhodnocování optimálního způsobu distribuce dat vůbec smysl. <br /><br />K tomu připočtěme problémy synchronizace, kdy jednotlivé kooperující eNodeB/RRE musí být velmi přesně frekvenčně i časově synchronizovány a to za hranici, jaká se dnes považuje za nutnou a hned máme další potíž. <br /><br />Tak a to je pro dnešek všechno.<br /></p>
<p> </p>