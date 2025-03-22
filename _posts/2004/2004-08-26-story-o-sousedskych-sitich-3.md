---
ID: 1276
author: Michal Krsek
layout: post
oldlink: 'https://www.marigold.cz/item/story-o-sousedskych-sitich-3

  '
post_date: 2004-08-26 14:54:47
post_excerpt: ''
published: true
summary_points:
- Autor zkoumal dostupné CZFree.Net AP v okolí obce pomocí antén.
- Autor navrhl rozsáhlý plán se třemi anténami pro zakruhování a tranzit.
- Komunikace s CZFree komunitou ohledně autonomního systému byla komplikovaná.
- Pro směrování bude použit Linux s minimálním softwarem a starší hardware.
title: "Story o sousedských sítích (3.)"
---

<p>
Dnes se podíváme na druhý případ, jehož cílem je zapojit malou obec do CZFree.Net. Tedy přesněji řečeno zajistit, aby rodiče přítelkyně meli přístup k Internetu z domácího počítače a já měl přístup k Internetu u venkovního bazénu (když tam zavítám s notebookem nebo iPAQem). Stejně jako v předchozích dílech se nejdříve podíváme, co se již stalo (narozdíl od ostatních kauz zde nastala i sociální interakce s poskytovatelem). </p>
<p>
Nejdříve jsem nahlédl do <a href="http://www.czfree.net/mapa">mapy CZFree.Net</a>, zda je někde v okolí nějaké funkční AP. Protože jich pár v okolí (do čtyř kilometrů) bylo, vylezl jsem na střechu (respektive se vyklonil z vikýře) a projel okolí 10 dBi anténou. V okolí bylo asi pět sítí, bohužel žádná z nich nevypadala, že patří CZFree.Net. Nezbývalo, než opatřit lepší anténu (se ziskem 24 dBi) a zkusit to znovu. Byla to větší opičárna, protáhnout sebe i anténu vikýřem, ale ne nadarmo jsem měl v dětství lego. </p>
<p>
Hurá, objevily se čtyři AP, které měly v SSID kus textu, který indikoval, že jde o APčka, která patří CZFree.Net. Dvěma nejnadějnějším (nejsilnější signál) jsem napsal hned, zároveň napsal do příslušného vlákna <a href="http://czfree.net/forum">diskuse CZFree.Net</a>, že zamýšlím připojit dotyčnou ves (tedy především skorotchána). Jedním z oslovených byl provozovatel WiFi sítě ve vedlejší vsi, která není připojena do CZFree.Net. Zároveň jeden z provozovatelů AP projevil zájem zakruhovat infrastrukturu CZFree.Net v dané oblasti přes moje AP. </p>
<p>
Protože jsem maximalista a žádná špatnost mi není cizí, po chvíli přemýšlení jsem vymyslel megaplán, kdy místo jedné směrové antény na střeše tam budou tři (dvě na zakruhování CZFree.Net a jedna jako tranzit pro sousední ves). Zároveň se pochopitelně nehodlám vzdát síťové konektivity u bazénu. Takže na střeše budou čtyři antény. </p>
<p>
Celý článek kromě dalšího popisuje sociální komunikaci mé osoby s lidmi v CZFree.Net, proto by neměl být zobrazován před dvaadvacátou hodinou ...</p>

<!--more--><p>
Vzhledem k tomu, že jsem již několikrát viděl směrovací tabulky CZFree.Net (a nebyl to povzbuzující pohled), nabyl jsem dojmu, že nejlepší bude pořídit pro tyhle dvě vesnice vlastní autonomní systém. Jedině při nasazení externího směrování (v Internetu realizované protokolem BGP-4) zajistíte, že máte směrovací tabulky ve stavu, který Vám vyhovuje.</p>
<p>
S tímto požadavkem jsem narazil. Místní CZFree komunita (jmenovitě místní gubernátor společně s duchovním vůdcem přípojného bodu, ke kterému povede jeden ze spojů) měli svoji hlavu. V ní je bohužel autonomní systém spojen s přidělením adresním prostorem /16 a rolí gubernátora (přehled gubernií najdete například na <a href="http://www.simandl.cz/stranky/czfreenet/as/as.htm">webu jednoho z gubernátorů</a>). Po výměně invektiv (na sprostá slova naštěstí nedošlo) jsme byli na začátku. Přičemž je zajímavé, že jsme se nedokázali domluvit ani na základních termínech - evidentně místní komunita nepronikla k best current practices v Internetu. Kolo sice již vymysleli, ale že může mít loukotě, jim zatím nedochází. </p>
<p>
Problém jsme nakonec vyřešili v sociálním zařízení <a href="http://www.bobovadraha.cz/">bobová dráha</a> (samozřejmě v části hospoda). Po předchozím oťukávání (hlas od vedlejšího stolu: "Jo, tak tohle je ten oook. Panebože, ten má děsný názory.") jsme, mírně povzbuzeni alkoholem, dospěli do stádia, kdy jsme uzali, že komunikace na odborné úrovni je nemožná. Musím se pochlubit, že jsem ustoupil jako první, díc, že teda pojedu vůči zbytku CZFree.Net pouze ospf a stanu se tak součástí gubernie (vymínil jsem si ovšem, že kdyby mi chodit na směrovač nějaký hnůj, tak přejdeme na externí směrování). Je třeba přiznat, že po další rundě uznala i druhá strana, že jejich expanze se někde musí zastavit a že hranice mohly vést přes "mojí ves". Zároveň jsme dohodli připojení na jeden z bodů (který ovšem změnil místo vysílání, takže bude potřeba znova "proměřit" viditelnost). </p>
<p>
Druhý den jsem APčko zanesl do výše zmiňované mapy (bylo mi vyčítáno, že nejsem na mapě, ale nechtěl jsem, aby skorotchánovi někdo bušil na vrata s tím, že chce připojení - skorotchán by na dotyčného mohl vzít vidle nebo na něj poštvat kocoura) a domluvili jsme přidělení adresního prostoru v gubernii. </p>
<p>
Zároveň jsem požádal skorotchána, aby připravil na půdě (dřevěnou) krabici, do které vrzneme technologii a konzoli na antény. Když jsem po týdnu dorazil, ukázal mi luxusní krabici zvíci poloviny racku, položenou na hambalkách (pokud si správně pamatuju naázev příčných trámů, které udržují rozvor krovů). Takže místo máme. Teď pracuje na ukotvení konzole na antény (kus trubky, nahoře zaslepené). Abychom nedělali více děr do střechy, chceme vést všechny čtyři kabely od čtyř antén vnitřkem trubky. Ví někdo, nakolik se to bude rušit?</p>
<p>
Ještě k vybavení. Predpokládám, že tranzitní trasy ukončím v PCčku. V tomto  PC budou tři XI626 karty (duchovní vůdce mi napsal, že nemá cenu uvažovat o 802.11g kartách) a jedna či dvě normální síťovky. PC je dostatečně výkonné na to, aby zvládlo odsměrovat to, co přijde (je to nějaký AMD Duron - já vím, topí, ale to PC mi prostě leží doma a proč pořizovat něco jiného). Vlastní pokrytí bazénu (a zbytku vesnice) bude realizováno hardwarovým AP Orinoco 1000 (není poslední výstřelek techniky, ale účel myslím splní). PC bude s APčkem  propojeno přes malý 100 Mb/s no name hub (který jsem kdysi kdesi koupil) a společně s připojením počítače rodičů (via 100 Base TX) vytvoří "půdabackbone". </p>
<p>
Na PC poběžím nejakou distribuci Linuxu. Děkuji za tipy na distribuce, které jste mi poslali v diskusi k poslednímu článku. Jelikož potřebuji, aby na PC běžel pouze směrovací démon (<a href="http://bird.network.cz/">Zebra</a>/<a href="http://www.quagga.net/">Quagga</a> nebo zkusím pochopit <a href="/item/story-o-sousedskych-sitich-1">BIRD</a>), ssh a bind (snmp pouze zvažuji), nepotřebuji žádná okénka. Minimalistický přístup říká, že ideální by byla nějaká distribuce, která se vejde do pár desítek MB a použití compactflash (upgrade dělat výměnou té CF), maximalistická říká, že potřebuji plnohodnotnou distribuci, kde si budu upgrade démonů kompilovat sám. Přičemž rozhodně nechci žádnou exotickou distribuci, jejíž podpora skončí měsíc po nasazení.</p>
<p>
Tím jsme odbyli dění, které se událo do včerejška, dnes mi dorazila zásilka z Vanca, o které byla řeč v <a href="javascript:void(0);/*fckeditortemplink*/">prvním pokračování</a> seriálu. Doufám, že se tentokrát povedlo Vancu vystavit fakturu na správnou adresu (která je jiná než adresa doručovací). Pokud je zásilka kompletní, měl bych v průběhu příštího týdne pohnout s první i druhou kauzou. Stay tuned ...</p>