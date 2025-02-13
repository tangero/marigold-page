---
ID: 1271
author: Michal Krsek
layout: post
oldlink: 'https://www.marigold.cz/item/story-o-sousedskych-sitich-2

  '
post_date: 2004-08-25 10:57:12
post_excerpt: ''
published: true
summary_points:
- Obec v Ústeckém kraji s osadami a 1500 obyvateli má slabou kupní sílu.
- Autor plánuje v osadách vybudovat WiFi síť s páteřními směrovými spoji.
- Pro směrové spoje autor zvažuje PC s Linuxem a hardwarová AP pro uživatele.
- Hlavní problém je nízký počet potenciálních uživatelů a financování provozu sítě.
title: Story o&nbsp;sousedských sítích (2.)
---

<p>
Včera jsme probrali první, nejjednodušší kauzu. Přeskočme teď na kauzu třetí. Třetí kauza představuje největší výzvu (americky řečeno). </p>
<p>
Obec v Ústeckém kraji (na úpatí Českého středohoří), která má kolem sebe několik osad (patří pod tu obec) vzdálených co dvou kilometrů. Obec má i s osadami nějakých 1500 lidí. Kupní síla je dost malá, takže i když je v oblasti díky INDOŠI pokrytí ADSL, neznám nikoho, kdo by si ADSL v místě pořídil. V místě jsem nebyl schopen naměřit žádnou WiFi síť (zkoušel jsem na více místech). Je tedy možné si to pěkně naplánovat a postavit podle svého.</p>

<!--more--><p>
Moje idea je postavit v každé osadě (kde bude zájem) přístupový bod a tyto body propojit směrovými spoji (tvořícími jakousi páteřní síť). V technologické rovině zatím není jasné, jak dimenzovat páteř, aby ji uživatelé nemohli přetížit (nebo aby to bylo obtížné). Budu muset v praxi vykoušet, zda má smysl pro směrové spoje nasazení 802.11g - hlavně jestli dokáží rozumnou rychlostí překlenout ony dva kilometry. </p>
<p>
Předpokládám, že bych pro směrové spoje použil PCčka (značka noname plečka) s bezdrátovými kartami a a nainstalovaným Linuxem (i když běžně používám Billova okénka, přece jen si nemyslím, že OS optimalizovaný na rychlé kreslení oken je vhodný pro směrování) - pokud máte tip na nějakou jednoduchou konkrétní distribuci, přijímám odkazy v diskusi (poslední Linux, který jsem administroval sám, byl Slackware verze tuším 1.2). Pro připojování uživatelů počítám s nějakým hardwarovým APčkem. Propojení mezi AP a PCčkem budu realizovat ethernetem (křížený kabel).</p>
<p>
V rovině adresace vidím dvě varianty. První je žádost o PI prostor (/22), druhou překlad adres. PI adresy považuji za optimální, protože při změně ISP není třeba měnit adresy. V případě překladu adres bych požádal CZFree.Net o přidělení adres z prostoru 10/8, v kterém CZFree.Net operuje. Pro směrování uvnitř sítě mohu použít ospf, při použití směrových spojů se nemusím bát, že mi někdo nakazí směrovací tabulky z veřejných AP. Pokud budu pracovat bez překladu adres s jedním ISP, je prakticky jedno, jaké směrování zvolíme (včetně statické cesty od ISP a "defaultní" cesty ze sousedské sítě). Pokud použijeme adresní prostor CZFree.Net, je cesta do Internetu vyřešena. Propojení s ostatními sítěmi v CZFree.Net by bylo realizováno pravděpodobně tunelem, a směrování (do CZFree.Net) by bylo pochopitelně založeno na BGP.</p>
<p>
Skončeme s technikou. Hlavní problém této kauzy jsou uživatelé. Nemá cenu stavět systém pro pět lidí. Proto jsem zaúkoloval sestru, aby oslovili s přítelem místní populaci. Způsob oslovení nechám na nich. S počtem uživatelů souvisí problém financování. Celkem není problém s postavením infrastruktury, ta je skutečně za pár korun. Někdo se ovšem musí o tu infrastrukturu starat (já to mohu dělat jen po omezený čas), někdo musí být schopen/ochoten vybírat peníze od uživatelů (já to nemohu být z důvodu konfliktu zájmů - živím se tím, že radím ISP a telco a nemůžu proto sám provozovat internetovou síť).  Třeba se najde nějaký dobrovolník, který skončí na úřadě práce a převezme to pod vlastní křídla.</p>
<p>
Jak je vidět, jde o běh na dlouhou trať.</p>
<p>
V dalším díle se podíváme na kauzu druhou, která je něco mezi první a třetí.</p>