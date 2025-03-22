---
ID: 2018
author: Vreco
layout: post
oldlink: 'https://www.marigold.cz/item/ztracene-procesory-pozarni-poplach-a-dalsi-bojovky-z-instalace-serveru

  '
post_date: 2006-10-06 10:49:00
post_excerpt: ''
published: true
summary_points:
- IBM servery dorazily do Opatovické, ale nevešly se do dveří.
- Řidič náklaďáku servery převezl do TTC, kde je ručně vyložili.
- Při instalaci serverů chyběly RAM, procesory a dva disky.
- SuperHosting servery vybalil a nainstaloval přes noc do racků.
title: Ztracené procesory, požární poplach a další bojovky z instalace serverů
---

<p><b>Vreco píše:</b> Když nám do Opatovické dorazilo osmnáct nových našlapaných černo-modrých skříní od IBM v objemově cca 10x větších obalech, netušili jsme, že netrpělivě očekávaný okamžik se změní ve dvoudenní bojovku. Ačkoliv náklaďák přepravní společnosti se do Opatovické vměstnal, palety jasně naznačily, abychom nepočítali s tím, že by prošly dveřmi. Přemluvili jsme tedy notně přinasraného řidiče (po telefonu jsem ho mírně odbyl s tím, že nevím, proč by kvůli pár serverům byl potřeba vysokozdvižný vozík a ať vydrží minutu, že zrovna zatáčím do Opatovické), aby nám servery transportoval do TTC, které je naší první a do budoucna primární serverovou lokalitou. Přiznávám, faux pas s náklaďákem v centru Prahy byla naše chyba, předtím jsme servery kupovali po 1-2 kusech dle potřeby a z IBM nám je vozili Oktávkou, takže nás nenapadlo, že tentokrát toho budou rovnou dvě palety. </p>

<p>Řidič dorazil do TTC druhý den. Vyhnul se zaparkovaným autům, aniž by na to kterékoliv z nich pamatovalo hůře než poškrábaným lakem, a zacouval do zadního dvora. Marně hledal rampu, žádná nebyla. A protože nebylo ani čelo ani vysokozdvižný vozík, nezbylo nic jiného, než cca půl tuny serverů vyskládat ručně. Práce na půl hodinky pro řidiče a čtyři silné chlapy (tj. nás). Podepsali jsme převzetí zásilky, dostali dodací list a začali stěhovat servery a hromadu krabic s příslušenstvím do výtahu (servery chodí zvlášť, disky jsou zabaleny zvlášť, další „víceprocesory“ a „vícepaměti“ mají také každý svou vlastní krabičku). Ještě že nákladní výtah v TTC uveze 1 tunu, nafouknout jej ovšem nelze. Naplnili jsme ho po okraj, někteří se naložili s ním, méně šťastní museli budovu obíhat a schody vybíhat po svých.  </p>

<p>Serverovna je v TTC ve druhém patře a zrovna ve středu tam technici prováděli kontrolu systémů. Když viděli plný výtah IBM serverů, zajiskřily jim oči a ochotně nám pomohli se stěhováním. Byť to na TTC není vzácnost, protože hned vedle nás jsou tři řady racků Seznamu, který staví také téměř výhradně na IBM. Dlouho jsme si ale neužívali, začalo totiž dohadování, jestli máme všechno. Nejprve přišly na řadu disky. IBM nám je dodalo pod různýma názvama a part-numberama a Franci se začal děsit, jestli je vše OK. Když se mi ho podařilo uklidnit a všechno nám vyšlo, zjistili jsme při prvním rychlém rozbalování krabic, že nám chybí cca 40 GB RAM a čtyři Xeon procesory. Zkontrolovali jsme vše s dodacím listem a volali do IBM.  </p>

<p>V IBM začali zjišťovat, proč to k nám nedorazilo, my jsme zapózovali pro film (foto vyšlo na Marigoldu) a dohodli se s šéfem SuperHostingu, který nám poskytuje prostor a síťové zázemí, že servery přijdeme nainstalovat zítra a určitě nechceme, aby nám to dělali oni, protože se těšíme, až budeme moct na jeden den vypnout a manuálně si seskládat to modro-černé lego. V půl druhé v noci nám Zdeněk (Cendra, šéf <a href="http://www.superhosting.cz">SuperHostingu</a>) poslal SMS s tím, že servery jsou vybalené a naskládané v racku. Tedy ve dvou, do jednoho se nevešly. Když jsem to ráno četl, napsal jsem mu, že je mrtvý muž. Franci už ho přede mnou stihl varovat v noci, takže mobil měl přesměrovaný na hot-line.  </p>

<p><img src="/wp-content/uploads/cache/20061006-IMG_3079.jpg" alt="Ke hraní nám zbyl jediný počítač, do kterého Franci málem nenasytně nacpal 16 GB RAM" width="500" height="551" />
</p>

<!--more--><p>Druhý den ráno jsem nabral Bobyho (náš servisák), Franciho a krátce po osmé jsme dorazili do TTC. Servery byly, až na jeden, opravdu krásně vyskládané v racku, zapojené do IP zásuvek a hned ze startu jsme dostali varování, že byť nejsou v ostrém provozu, odebírá jeden rack (15 serverů) 16A a půlka druhého 10A. Uklidnili jsme Honzu, který se Zdeňkem absolvoval noční montáž, že část serverů budeme zhruba za měsíc přesouvat do druhé lokality (od začátku stavíme na n+1 nejen v rámci jedné serverovny, ale i co se lokalit týče) a holkám jsme nainstalovali dostatek pamětí. Holkám proto, že tak jako za starého Mobil serveru mají naše servery po určité logice ženská jména. A tak jako za Mobil.cz dýchala jako první Diana se Sarah, i v naší master serverovně bude srdcem systému Diana a Sarah.  </p>

<p><img src="/wp-content/uploads/cache/20061006-IMG_3096.jpg" alt="Franci zapojuje do sítě databázi a webovku" width="500" height="333" /></p>

<p>Následovala drobná mravenčí práce se správným doskládáním serverů, síťováním, instalací atp. Do toho jsme zjistili, že nám někde chybí dva disky – servery byly osazeny přesně podle návrhu, ale náhradní disky nikde. Protože jsme předchozí den měli obsáhlou debatu o počtu disků a hádku, je-li jich dost, byli jsme si jisti, že disky dorazily. SuperHosting má naštěstí ve své části serverovny kamery, které monitorují a archivují veškeré dění v poměrně vysoké kvalitě obrazu, takže jsme po cca dvou hodinách studování záznamu přišli na to, že disky opravdu nedorazily. Opět jsem žhavil IBM, kde už z nás byli nešťastní. Naštěstí mezitím volali ze Servodat, což je distributor, který nám disky dodával, že spediční firma veškeré chybějící balíčky našla a jestli jí řeknu, co nám ještě chybí, má pro nás i dva další. Řekl jsem, že jsou to dva disky a překvapivě jsem měl pravdu. Na otázku, jak je možné, že zboží zafóliované na paletě se ocitne mimo ochrannou fólii se nám dostalo zajímavé odpovědi: protože ty krabice (paměti, disky, procesory) byly malé, složené nahoře na paletě a ta byla moc vysoká a nevešla se do náklaďáku (nějaká novější Avie s plachtou, co s ní jezdí „rychlejší bráchové blesku“), řidič fólii rozříznul a krabice tam naházel ručně, aby se mu to tam vešlo. Akorát nám je pak jaksi zapomněl předat. </p>

<p>Sotva jsme se uklidnili, rozezvučelo se serverovnou nepříjemné pískání. „To jsou jen UPS. Jó kdyby blikal ten červený maják, musíš utíkat pryč, po pěti vteřinách by všude začal stříkat tekutý dusík na hašení,“ informoval nás Honza ze SuperHostingu. „Za pět vteřin nemůžeš stihnout utéct,“ strachoval se Boby. „Stačí, když se nadechneš, to pak ke dveřím doběhneš,“ uklidnil ho Honza. Pískání skončilo, aby pár desítek vteřin na to začala řvát ohlušující siréna, kterou doprovázely blikající majáčky. Protože si Boby šel mezitím zakouřit na chodbu, aby nemusel to pískání poslouchat, mysleli jsme si, že si zapálil už dřív a alarm spustil on, naštěstí nás uklidnili technici TTC se slovy, že jen testují systém a hasící nádoby jsou odpojené.</p>

<p><img src="/wp-content/uploads/cache/20061006-IMG_3155.jpg" alt="Požární alarm v TTC a majáček blikající za zbylými krabicemi" width="500" height="333" /></p>

<p>Dvoudenní bojovka nakonec dobře dopadla. Půl tuny serverů jsme úspěšně složili v serverovně, disky, paměti a procesory nám doputovaly do kanceláří (to už se do dveří vešlo) a Francimu se poměrně bez problémů podařilo servery nainstalovat. Až na jeden, který nespolupracoval hned od startu, a proto jsme ho rovnou předali IBM on-site servisu. Snad to funguje tak dobře, jak nám jejich obchodníci slibovali. Teď už nás čeká jen nakrmit server daty dostatečně atraktivními na to, aby přilákaly statisíce návštěvníků - a my budeme moci v lednu k IBM znovu na nákup.
</p>

<p><b>Update 9.10.2006:</b> IBM servis funguje opravdu skvěle, všechny servery už fungují bezvadně. :-)</p>

<p><img src="/wp-content/uploads/cache/20061006-IMG_3075.jpg" alt="Plný rack serverů (pohled zezadu)" width="500" height="673" />
</p>