---
ID: 2784
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/kdyz-vyslysite-cilovou-skupinu-ktera-ji-neni-je-to-prusvih

  '
post_date: 2014-02-18 21:26:08
post_excerpt: ''
published: true
summary_points:
- Kritika je účinnější, když vychází z vlastních chyb.
- Energomonitor se zaměřuje na šetření energie pomocí online služby.
- První verze energomonitoru byla příliš složitá a neintuitivní.
- Druhá verze, "bílý web", uspěla u elektrikářů, ale ne u běžných uživatelů.
- Finální "černý web" vznikl po důkladném testování a zpětné vazbě.
- Chybou bylo naslouchání nesprávné cílové skupině.
- Poučení z chyb je klíčové pro úspěšný vývoj produktu.
title: Když vyslyšíte cílovou skupinu, která jí není, je to průšvih
---

<p>Má-li zaznít kritika, tak je nejlepší ukázat ji na vlastních pochybeních. Když jsem <a href="http://www.marigold.cz/item/lean-startup-aneb-jak-se-propivotovat-do-pekla">psal o "lean startupu"</a>, snažil jsem se vysvětlit, že jejich metodika stálého testování vlastně není metodikou, jen temným příkázáním. Což je nepříjemné ve chvíli, kdy nevíte, jak se testování a průzkumy dělají, přičemž Riesův “lean” se na ně opravdu hodně odvolává. Snadno se pak necháte svést na zcestí, protože neodhadnete, co a kdo je vaše cílová skupina či jaký je její rozměr nebo dynamika. A už vůbec nebudete schopni odvodit z reakcí, jaké bude skutečné přijetí novinky, se kterou trh nemá zkušenosti.</p>
<p>Takže k našemu příkladu...</p>


<!--more-->

<p>Energomonitor se snažíme dovést do stádia, kdy to bude nápomocný nástroj k šetření elektrické energie. Jak a proč, to teď ponechme stranou, pro účel našeho výkladu to není podstatné. Podstatné je, že taková kategorie zařízení dnes vlastně neexistuje, takže i komunikace a průzkumničení s uživateli je neustálé vysvětlování, testování, ověřování. Na jednu stranu posloucháme názory, na stranu druhou musíme sami pevně vědět, kam to chceme dovést, jinak z toho uděláme ampérmetr nebo nějaký online mrdník. Čili: celé to visí na vizi, že lidé by rádi, kdyby jim nějaká online služba říkala, co mají dělat, aby ušetřili za elektřinu, plyn či vodu, neboť oni sami netuší. A že ta služba může mít rozměr od pouhého "co kdybys vypínal světlo na chodbě", přes tradiční "změň si dodavatele", až po skutečné řízení spotřebičů, které jsou podstatné, jako kotel nebo bojler a tvrdá investiční rozhodnutí "když si zateplím barák, tak to mám za 5 let zpět, jdu do toho?".</p>
<p>Což, jak jistě chápete, je dosti široké rozpětí služeb a především přehršel informací. Nejenom těch ke zpracování, ale také těch, které musíte uživateli nějak odpresentovat. Samozřejmě nečekáme, že zrovna v případě takového zateplení vám ze služby vypadne hotový plán, na to nám dost informací chybí, ale rozhodně si myslíme, že bychom uměli alespoň v základu vyhodnotit návratnost a umožnit vám rozhodnout se, zda se tím vůbec zabývat a připravit podklady pro firmu, která vám ten návrh udělá.</p>
<p>No teď pojďme na příklad toho, jak snadné je sklouznout a dát ven službu, pod kterou se ve firmě vlastně nikdo nepodepíše.</p>
<p>Už jsem říkal, že jednoduchost je klíč a udělat něco složitého jednoduše je dost složité. Takže používáme metodu per partes a informace nehrneme na uživatele naráz, ale postupně. Ideální závěr dobrodružství s námi by měl být takový, že uvidíte semafor, na kterém svítí zelená, jako že všechno je v pořádku, jen pod tím je douška, že byste příští týden už fakt mohli odmrazit ledničku. Tolik ke grafickému provedení. Zatím se k němu neblížíme ani ... ani.</p>
<p>První verze energomonitoru vypadala nějak takhle:</p>
<p><img src="http://www.marigold.cz/wp-content/uploads/denni-graf1.png" id="blogsy-1392758727010.0806" class="" width="500" height="383" alt="Denni graf"></p>
<p>Na ní jsme postupně odlaďovali a zpřesňovali si, jak má všechno vypadat, co chceme dělat a jaký je za tím obchodní model. A pak se stalo několik věcí, jejichž analýza je i u nás ve firmě předmětem řady sporů. Tak především jsme se chystali na veletrh Ampér, kde jsme chtěli našim partnerům mezi elektrikářskými firmami ukázat novou web aplikaci energomonitoru, která by podporovala více odběrných míst, více měřených okruhů a vůbec více hraček. Jenže zároveň s tím jsme přecházeli na vlastní distribuční platformu, do té doby jsme používali pro ukládání dat službu Pachube/Cosm. Ta nám ovšem přestala vyhovovat, na naše záměry byla příliš svazující a neflexibilní.</p>
<p>Takže abychom upokojili elektrikáře, představili jsme druhou verzi - tzv. bílý web. A vypadalo to nějak takhle:</p>
<p><img src="http://www.marigold.cz/wp-content/uploads/energomonitor-bily-web.png" id="blogsy-1392758727079.161" class="" width="500" height="475" alt="Energomonitor bily web"></p>
<p>Naši vlastní uživatelé byli... povětšinou nadšeni… A účastníci veletrhu Amper rovněž. Načež se situace zamotala: služba Cosm nám poslala informaci o novém jméně a také nový ceník platný ihned. Na kterém bychom pro naprostou změnu cenové struktury (nově ne za data, ale za datový stream) prodrbali kalhoty.</p>
<p>Zdvořile jsme se otázali našeho zahraničního partnera, který na Cosmu držel v tu dobu asi pětinu účtů, zda o chystané změně věděl. Nevěděl. Vyjednali jsme si nějaký provizorní statut quo a bylo zřejmé, že je čas udělat pápá.</p>
<p>Nu a v tom všem kvaltování znovu padl zrak na naši <em>"bílou verzi"</em>. Vždyť se <strong>všem líbila</strong>, jede na naší platformě, tak ji nahodíme jako hlavní obchodní verzi, řekli jsme si. A tak se i stalo.</p>
<p>Teď už asi tušíte, v čem byl zádrhel. To je zřejmé každému soudnému člověku. Ten web je prostě hnusný maglajs, daleko ode všech našich představ a pro běžného uživatele záporné zlepšení <em>(aka zhoršení)</em>. Veškerá kladná odezva byla od profi elektrikářů, kterým vyhovovaly křivky, hnus jim byl ukradený (resp. jsou na něj zvyklí z profi řešení), vyhovovalo jim zahlcení čísly.</p>
<p>Určitou indikaci problému nám o měsíc později dali zahraniční partneři (otázkou,<em> "what the fuck is that shit"</em>) a to už i nám začalo svítat, že jsme se nechali dotlačit ke šlápnutí vedle. Rychle jsme přišli na to, že jsme se úzkou skupinkou uživatelů, na které navíc ani primárně necílíme, nechali přesvědčit, že tohle je ta pravá cesta. Přes to, že víme, že není.</p>
<p>Takže se zpět zasedlo k rýsovacím prknům a tentokráte se na to šlo pořádně. Komunikace s uživateli, na které cílíme. Vlastní UX lidé, chytří lidé kolem jako Filip Molčan and <a href="http://www.pixerience.com/energomonitor">his graphic boys Pixerience</a>. Desítky návrhů, stovky hodin, dalších šest měsíců piplání a vývoje něčeho, co nejenom parádně vypadá, ale udává tón na trhu. Tak vznikl “černý web”. Má k ideálu daleko, ale vzdálenost se zkracuje, nikoliv prodlužuje. </p>
<p><img src="http://www.marigold.cz/wp-content/uploads/energomonitor-cerny-web.png" id="blogsy-1392758727085.1548" class="" width="401" height="600" alt="Energomonitor cerny web"></p>
<p><strong>Není na závadu, chybu udělat. Na závadu je, nepoučit se z ní.</strong> Tahle chyba byla zřejmá: <strong>vyslyšeli jsme cílovou skupinu, která cílovou skupinou nebyla</strong>. Neověřili jsme si, zda je pro nás ta odezva podstatná. A nechali jsme se dodavatelem technologického řešení zaskočit.</p>
<p>&nbsp;</p>