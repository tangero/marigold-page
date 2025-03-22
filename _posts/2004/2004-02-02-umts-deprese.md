---
ID: 828
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/umts-deprese

  '
post_date: 2004-02-02 17:07:00
post_excerpt: ''
published: true
summary_points:
- G sítě, konkrétně Trojka, nezměnily způsob, jakým lidé používají mobilní telefony.
- UMTS sítě nejsou ekonomické, operátoři slibují rychlý internet, ale je drahý.
- IMS doména v Release 5 nepřináší výhody, ale rekonfiguraci sítě a nákup nových zařízení.
- Architektura UMTS je složitá, vyžaduje obsáhlý popis, článek by musel být kniha.
title: "UMTS deprese"
---

<p>
O víkendu mne zachvátila UMTS deprese. Dneska jsem pookřál, když jsem zjistil, že nejsem sám... Prvním depresistou byl hned po ránu Anthony Newman, redaktor InfoSyncu, když si<A href="http://www.infosyncworld.com/news/n/4549.html" target=_blank>v úvodníku </A>povzdechl otázkou, <STRONG>co je špatně s 3G</STRONG>? Kdybych měl vybrat nejdůležitější odstaveček z jeho editorialu, asi bych volil tohle: </p>

<BLOCKQUOTE dir=ltr style="MARGIN-RIGHT: 0px">
<p>
<EM>Nyní,&#160;roce 2004, má Velká Británie jednu 3G síť, Trojku, provozovanou Hutchinson Telecom. Navzdory rozsáhlé reklamě a opravdu levné nabídce udělala síť jen velmi malý dojem na mobilisty, které člověk vídá vůkol. A co hůř, nezměnila způsob, jakým uživatelé používají tyto mobilní telefony... </EM></p>
</BLOCKQUOTE>
<p>
A to je pravda. Trojka má ceny volání skoro o třetinu až polovinu nižší, než konkurence, jenže z 3G výhodn lidé používají pramálo. Newman v editorialu přináší řadu argumentů, proč podle něj uživatelé na 3G síť kašlou a nezbývá, než s tím souhlasit. </p>

<p>
<STRONG>Další depresista je Martin Cooper</STRONG>, CEO ArrayCommu, jeden z lidí, jemuž je připisován vynález mobilního telefonu. <A href="http://zdnet.com.com/2100-1103_2-5091438.html" target=_blank>Ten říká</A> <EM>"We were going to have 3G in 1999. Then 2000. Then 2001. Now carriers are talking maybe 2005. They keep moving away, because it's so far just not economical."</EM> Prostě není ekonomické lidem slibovat rychlý internet a neříct jim, že je to pěkně drahá hračka... A to není zdaleka poslední člověk, od něhož byla UMTS skepse dneska zachycena (byť tento jeho zmíněný článek je starší).</p>

<p>
<STRONG>Proč mne zachvátila UMTS deprese?</STRONG> </p>

<p>
Minulý týden jsem jednomu novináři odpovídal na jeho všetečné otázky. On vždy vytáhl nějakou marketingovou poučku nebo píárspík od operátora <EM>(jako mobilní aplikace, rychlá a levná data atd)</EM> a já jsem to uváděl na pravou míru <EM>(jako neexistují, nejsou rychlá ani levná atd)</EM>. A když jsme probrali jeho seznam, tak on takovým skleslým hlasem říká - <EM>ale k čemu tedy jsou ty UMTS sítě, když to tedy lidi nepotřebují a bohatě si vystačí s zatím výrazně spolehlivějším GSM?</EM> A to je bohužel zajímavá otázka... byla dříve slepice nebo vejce?</p>

<p>
O víkendu jsem se rozhodl napsat nějaký článek o architektuře UMTS sítí, protože všechno, co jsem v češtině našel, bylo takové strohé a <A href="http://mobil.idnes.cz/autori.html?autori_j=Petra%20Matušínová&amp;autori=247" target=_blank>Petra Matušínová svůj seriál</A> na Mobil.cz bohužel nedokončila a skončila vlastně na začátku. Když jsem v neděli přestal psát, zjistil jsem, že mám za sebou přes 40 000 znaků a hromadu obrázků, což je pro představu pětina té knihy o WiFi. Což o to, kdybych v tomto rozsahu popsal celou architekturu UMTS, dalo by se to snést, jenže já jsem probral základy architektury jádra sítě. Nic víc. </p>

<p>
I to by se dalo skousnout. Jenže hloupé taky bylo, že předtím jsem updatoval několik týdnů svoje povědomosti o UMTS z nejrůznějších knih, aby se ukázalo, že z vyšlých anglických knih se většina autorů soustředila v samotném výkladu architektury jádra sítě na doslovný přepis technické specifikace. Když jsem přes víkend ležel v těch specifikacích, pochopil jsem je. Specifikace mají tři kopy verzí a souhrn změn je na webu 3GPP&#160;ve dvou slovech :(</p>

<p>
Ono je to také veselé čtení, když vám říkají, že jádro sítě má dvě domény (=dva způsoby jak obsloužit uživatelův požadavek)&#160;- paketově spínanou (něco jako GPRS - data tečou po kouskách) a okruhově spínanou (něco jako GSM telefonát&#160;- data tečou vyhrazeným kanálem). Jejda, pak ale někoho napadlo, že to je přeci kravina to mít takhle rozdělené a že by bylo lepší mít jedinou doménu. Bum - <STRONG>Release 5 přinesla doménu zvanou IMS</STRONG> <EM>(IP Multimedia subsystem)</EM>, která je vlastně obdobou paketového přenosu, jenže s tím, že pod sebe přebírá i obsluhu okruhově spínaných služeb, tedy přenos hlasu. Samozřejmě formou VoIP a samozřejmě s nějakou napodobeninou QoS. Jenže pak nějakou osvícenou hlavu napadlo, že uživatelé vlastnící mobil podporující jen paketovou a okruhovou doménu jsou vlastně v loji, protože jejich mobil si s novým IMS neporadí. A ano, dobře tušíte, 100% UMTS mobilů nezvládá IMS. Takže místo aby IMS bylo schopno obě domény nahradit, tak se zavádí jako doména třetí a samozřejmě to přináší rekonfiguraci sítě a nákup hromady krabic, které IMS do UMTS doplní. Výsledek pro operátora jsou samozřejmě provařené peníze a minimální výhoda navíc. Ve specifikacích se o tom autoři zmiňují velmi potutelně jako <EM>"small change"</EM> - je to tak small change, jako když autu přidáte dvě kola doprostřed a křížem... Operátoři mají jediné štěstí, že IMS zatím nikdo z výrobců nezvládá nacpat ani do mobilu, ani do sítě. Nejdále je Alcatel - ten má nádherné barevné letáky, hezčí než kdokoliv jiný. Tím to taky hasne a dobře tak. </p>

<p>
Snažně jsem hledal, proč někoho nenapadlo ty okruhové služby zapouzdřit tak, že uživatelovo zařízení by mělo iluzi, že pracuje stále ve své dvojici domén, zatímco ve skutečnosti by to byla doména IMS. Až dneska mi někdo z UMTS fóra vysvětlil, že je to tehdy nenapadlo... </p>

<p>
Tím jsem se dostal k tomu, že aby se nějak rozumně vyložilo, co to je UMTS a jak funguje (kdyby fungovalo), muselo by jít o článek tak na půl milionu znaků. A to už není článek, ale pořádně tlustá kniha... :(&#160;Takže z článku sešlo...</p>