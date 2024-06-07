---
ID: 1128
title: 'WiFi nezávislé na napájení &#8211; akumulátory a&nbsp;solární panely'
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/wifi-nezavisle-na-napajeni-akumulatory-a-solarni-panely
published: true
post_date: 2004-06-06 15:17:45
---
<p>
Potřebujete rozeběhnout WiFi i v oblasti bez elektrické energie? Musíte zřizovat repater v místě, kde není napájení? Přestřelit vrcholek kopce nebo mít mobilní hotspot?
</p>

<!--more--><p>
Nedávno jsem dostal zajímavý odkaz na stránku, kde někdo popisuje svůj <a href="http://www.mjleonard.pwp.blueyonder.co.uk/index.html">Wireless Backpack Repeater</a>. Jak vidno z obrázku, jde o normální Linksys  router WRT54G napájený z akumulátoru a vybavený všesměrovou anténou. Firmware Linksysu byl upraven Sveasoftem na podporu WDS, takže router se připojil na nejbližší přípojný bod a zároveň distribuoval signál přes WDS pro ostatní klienty, kteří neměli tak dobrou anténu, aby se na přípojný bod připojili sami. Jak fikané pro nějaké výpravy mobilních geeků&#8230; </p>

	<div class="leftbox"><img src="/wp-content/uploads/20040606-hotspot_mobilni.gif" alt="Wireless Backpack Repeater" width="130" height="250" /></div><p>
Tím mi ale přišlo na mysl napsat něco málo o WiFi technice nezávislé na elektrické síti. Ona to totiž nemusí být praktický věc jen pro sraz několika wifi potrhlíků, může to být často i jediná cesta, jak propojit lokality jinak nepropojitelné. </p>

<p>
Představte si například, že lokality, které chcete propojit, odděluje kopec. Takových případů i v Praze najdete hodně. Signál se odrazem nedostane, hodil by se nějaký repeater nebo něco takového. Najdete budovu či stavbu, na kterou by se takový repeater dal umístit, víte, že s pomocí WDS se to dá udělat velmi jednoduše a cenově efektivně, jenže co s tím. V budově vám majitel nedal svolení připojit se do jeho napájení, případně jste považovali za efektivnější po něm ani nepátrat a prostě mu tam techniku umístit. Nebo také potřebujete &#8222;přestřelit&#8220; kopec, který vám stojí v cestě a kde jste si našli hezké místečko na repeater, jenže jako na potvoru tam chybí elektrická zásuvka&#8230;  </p>

<p>
Řešení existuje v nezávislém napájení. Učinil jsem s ním kdysi pár zkušeností a ačkoliv nejsou tak komplexní, jak bych si přál, ostatní kdo na to narazili, mne snad doplní. </p>

<p>
Především je potřeba vybrat pro funkci repeateru zařízení s co nejmenším odběrem. Stará vyřazená čtyřiosmšestka v tomto ohledu nevyhovuje vůbec a my jsme sáhli po Linksys WRT54G (jako člověk s tím BackPack Repeaterem). Důvod je na snadě &#8211; je to poměrně výkonné a levné zařízení, ve kterém lze rozchodit WDS a navíc má poměrně malý odběr. Pokud se podíváte do specifikace, Linksys si odebírá 1 A při 6V, přičemž vyžaduje stejnosměrné napájení v rozsahu 4-27V, firemní síťový napáječ dodává 5V. Interní měnič toto napětí konvertuje na 3,3V,  takže máme poměrně široký rozsah napájení, který můžeme Linksysu nabídnout. </p>

<p>
Prostým vzorcem odvodíme, že příkon Linksysu je 6W, což jsme ověřili v praxi, kdy měřák ukázal, že v klidovém stavu se jeho příkon pohybuje mírně pod 5,4W a při vysílání kolem 5,6W. </p>

<p>
Nyní se musíme zamyslet, jak s napájením. Pokud chcete router/repeater napájet jen dočasně, například právě do takového BackPacku, jako je ten na obrázku, stačí vzít akumulátor, přičemž nejčastěji asi dostanete nějaký s jmenovitým napětím 6V a podívat se, kolik ampérhodin (Ah) nabízí. Ten na obrázku bude mít takových 10 Ah, je tedy schopen nabízet 6V/1A po dobu 10 hodin &#8211; což je přesně to, co pro napájení repeateru potřebujete. Pokud vám stačí těch deset hodin, jste za vodou, i když dlužno říci, že v praxi počítejte spíše s 8 hodinami, olověné akumulátory by se neměly vybíjet na doraz, ale jen na zhruba 80% - u jiných to nevadí. Samozřejmě nemusíte používat olověné akumulátory, ale jiné levné se v těchto kapacitách nedělají, tužkové NiCd/NiMH akumulátory  byste museli řadit sério-paralelně a potřebovali byste jich tři desítky, abyste se dostali na podobnou kapacitu. A to není cenově zrovna to pravé. U Lithiových článků je cena ještě horší. Ceny olověných akumulátorů potřebné kapacity se u nových pohybují od 2000 Kč, ale seženete jistě i něco staršího. Jen bych doporučil podívat se na provozní podmínky a zejména provozní teploty, protože v zimě by mohl mít akumulátor problémy se zamrzáním. </p>

<h3>Solární články</h3>
	<div class="rightbox"><img src="/wp-content/uploads/20040606-hotspot_solar.jpg" alt="Hotspot se solárním napájením" width="400" height="500" /></div><p>
Se solárními články je situace mírně komplikovanější, zejména pro to, že samotné je použít nelze. Solární články poskytují slušné napájení, jenže když zajde slunce, dojde i napájení. Je tedy nutno je kombinovat s akumulátory a solární energií akumulátory dobíjet. Kromě solárního panelu a akumulátoru je ještě potřeba regulátor chránící akumulátor před hlubokým vybitím nebo přebíjením. Regulátory se prodávají za ceny od 1000 Kč. </p>

<p>
Samotný solární panel je docela drahá věc, v našem případě ale nebudeme potřebovat naštěstí nijak velký. Pokud vezmeme, že k napájení Linksysu stačí příkon 6W a uvážíme provozní režim 12/12 hodin &#8211; tedy 12 hodin světla, 12 hodin na akumulátor, dostáváme se k požadavku na 12 W výkonu panelu (aby kromě napájení repeateru ještě i nabíjel akumulátor na noc). Doporučuji zhodnotit světelné podmínky v místě, kde budete panel montovat a poohlédnout se po nejbližším vyšším panelu, tedy například 15W. </p>

<p>
Pokud je mi známo, jediný český výrobce panelů je firma <a href="http://www.solartec.cz">Solartec</a>, která za 4000 Kč s DPH nabízí panel s výkonem 13W, což je pro naše potřeby dostatečné. Samozřejmě se lze podívat i jinde, dovozců je u nás povícero a někteří již rovnou dodávají celou &#8222;ostrovní sadu&#8220;, tedy nabíječku, solární panel, regulátor a akumulátor. Tyto sady se prodávají za ceny kolem 10 000 Kč ve složení vhodném pro naše účely. </p>

<p>
Dlužno vzít též v úvahu, že panely lze zapojovat stejně, jako baterie, tedy do série nebo paralelně případně kombinovaně a tím navýšit jejich výkon. A také fakt, že u solárního panelu se jako samozřejmost předpokládá nasazení venku, takže jsou voděodolně konstruovány, horší to bývá s odolností proti nárazu. Doporučuji volit panely s hliníkovým rámem, lépe se s nimi pracuje.</p>

<p>
Aplikace solárních panelů není levný špás &#8211; vidíme, že sestava nezávislého napájení se pohybuje kolem 10 000 Kč, k tomu je potřeba přidat její zajištění proti zlodějům, tedy kovářskou práci a samozřejmě cenu samostatného repeateru. Jenže co naplat, jsou lokality, kde se bez solárního napájení obejdete jen špatně. </p>

<h3>Kde ušetřit</h3>
<p>
S šetřením je to problém. Solární energie má zatím stále vysoké pořizovací náklady a ušetřit se dá snad jen na tom, že akumulátor i solární panel pořídíte z nějakého výprodeje a nabíječku s regulátorem <a href="http://www.hw.cz/docs/nabijeni/nabijeni_1.html">si postavíte sami</a>. </p>

<p>
Poměrně pitomým nápadem, jak ušetřit, je snaha rozhlédnout se po hotových výrobcích a ty se pokusit přizpůsobit. Mluvím tady například do těch zahradních lampičkách prodávaných v zahradnických potřebách. Lampičky mají solární panel a akumulátor. Napadlo nás to také &#8211; zakoupili jsme je velmi výhodně (byly polámané), vypreparovali jsme je a zjistili jsme, že bude třeba zapojit jich celou řadu. To nebylo to nejhorší. Jejich technické parametry byly dost benevolentní, takže i když jsme to spočítali dobře, tak nám uprostřed noci došla šťáva. A ještě ke všemu bylo potřeba vyndat ven světelný spínač, protože jinak se repeater napájel pouze v noci. </p>

<p>
Ve výsledku bych spíše než šetřit doporučil trochu utrácet &#8211; panely s vyšším výkonem a baterie s vyšší kapacitou zabrání tomu, že hotspotu v prostředku noci dojde šťáva. Na druhou stranu naše zkušenost je taková, že šťáva dojde většinou pár hodin před svítáním, kdy už i ti největší nadšenci do internetu to berou jako dobrý signál k odchodu do hajan &#8211; a s kuropěním vyjde slunce a s ním začne fungovat panel. </p>

<h3>Na závěr</h3>
<p>
Každá drahá věc láká &#8211; a s hotspoty je to totéž. Umisťujte je co nejméně přístupně, protože se solárním panelem jsou docela služně viditelné. Dejte všechno do bytelných kovových schránek, aby se to blbě kradlo. Zkontrolujte si také, v jaké pozici na panel dopadá nejdelší dobu světlo. A pokud je vám panel obzvláště milý a na dostupné lokaci, vyplatí se pouvažovat o tom, že byste jej rozšířili o mobilní telefon s monitoringem stavu a polohy. Ale to už je zase další povídačka a další  investice, s tím už by se cena vyšplhala na celkových 30-40 tisíc za takovou lokaci. </p>

<p>
Pamatujte na to, že i solárnímu panelu s akumulátorem může dojít proud a hotspot vypadne. Mějte ho nastavený tak, aby se mohl rozeběhnout při obnovení napájení bez vašeho přičinění. </p>

<p>
Je to hodně peněz? Pokud hotspot jednou zrušíte, panel můžete použít na chatě či doma k napájení televize zadarmo&#8230;
</p>
