---
ID: 2072
title: Neklid na DRM frontě
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/neklid-na-drm-fronte
published: true
post_date: 2007-02-12 22:34:41
---
<texy>Dlouho jsem toho názoru, že DRM jakožto filosofie ochrany digitální hudby, je na houby. Že hudbě spíše škodí, než prospívá. Například tím, že trestá toho nepravého: vždycky komplikuje život legálnímu majiteli spíše, než pirátovi, pokud přistoupíme na terminologii nahrávacích koncernů.

V poslední době bylo v oblasti DRM zajímavě rušno, to když publikoval svůj článek šéf Apple Steve Jobs. V něm v zásadě tvrdí totéž, když poukazuje na fakt, že zatímco CD vlastně žádnou systémovou ochranu nemají, hudba zkriplovaná do ztrátové digitální formy ji mít musí. A že to nějak nedává smysl, leč že Apple i ostatní s tím zatím musí žít.  <a href="http://www.maler.cz/index.php?id=931">Detailně informuje Malér.</a> 

Co na tom, že Jobs hájil svůj píseček, když pod dojmem několika posledních soudních útoků na applácký DRM formát FairPlay  obhajoval, proč tento formát není otevřený všem. 

Vposledku se přidal jeden z ředitelů <a href="http://www.coremedia.com">CoreMedia</a> Willms Buhse, když Jobse upozornil, že FairPlay nemusí nutně být uzavřený formát na to, aby se nedal hacknout a dokumentoval to příkladem <a href="http://www.openmobilealliance.org/">OMA DRM</a>. To se dalo čekat, CoreMedia dodává testovací tooly pro OMA a spolupracuje s Frauenhofery na jeho další podpoře. Pravdou také je, že na trhu je více jak miliarda zařízení podporujících OMA specifikaci DRM, což OMA DRM dělá nejrozšířenějším DRM. Buhseho jízlivá poznámka, že jistě i Jobs má zařízení vybavené OMA DRM se zakládá na faktu, že OMA specifikací jsou vybaveny prakticky všechny mobilní telefony podporující přehrávání hudby.

Tady vidíte, jak je statistika ošidná věc. Ačkoliv počet prodaných OMA DRM zařízení převyšuje o řád počet prodaných iPodů (miliarda versus sto milionů plus mínus), faktický vliv OMA na trh s online hudbou je vůči Apple FairPlay zanedbatelný. Je také pravda, že OMA netrpí vlastně žádným významným hackem, zatímco FairPlay už má na tapetě DVD John, ačkoliv tentokráte své know-how nenabízí gratis. Nakolik DVD John kecá, ví málokdo, ale vlastně je to fuk. 
<!--more-->

Všechny tyto výhody jsou OMA platné málo, spíše pak vůbec. Nulové využití je založeno na tom, že OMA podporují jen mobilní telefony a jen málo telefonů z té miliardy má realistickou paměť pro používání jako hudebního přehrávače a ještě méně má dostatečně příjemné ovládání. Pár Sony Ericssonů či Samsungů to nezachrání. Navíc hudbu s OMA ochranou prodávají jen zoufalí prodejci vyzváněcích melodií, kteří jsou nuceni vám prodat za 79 Kč reálný vyzváněcí tón chráněný OMA. Vtip OMA je také v tom, že jen obtížně jej implementujete na MP3 hudbu přehratelnou běžným přehrávačem, používá se obálka .ASP a ačkoliv je OMA portovaná na PC i PDA systémy, vlastně zůstala jen doménou mobilů, kde chrání ringtony. A to ještě jen některé.

<h2>OMA DRM 2.0</h2>

V průběhu letošního roku se na trh dostanou zařízení podporující novou specifikaci OMA DRM 2.0 – některé už jsou v prodeji (Nokia N91 nebo třeba Sony Ericsson W850i). Druhá verze OMA je výrazně pokročilejší, protože odděluje dodávku obsahu od jeho zabezpečení. Abychom si to přiblížili: 

Funguje to tak, že <strong>každé zařízení s OMA DRM 2.0 má vlastní DRM PKI certifikát</strong> s veřejným klíčem a odpovídajícím privátním klíčem. Každý Objekt Práv (RO – Rights Object v terminologii specifikace – prostě fajl s hudbou či filmem atd) je individiuálně chráněn pro jedno cílové zařízení zakódováním skrze veřejný klíč tohoto zařízení. Objekt Práv zase obsahuje klíč, který je použit pro rozkódování média. Dodání Objektu Práv je tedy podmíněno registrací u Propůjčovatele Práv (Rights Issuer – entita distribuující Objekt Práv). V průběhu registrace je certifikát cílového zařízení zpravidla ověřen vůči černé listině hříšníků a hacknutá zařízení mohou být vyloučena z verifikace a následného rozkódování Objektu Práv. 

OMA DRM se tím posouvá na úroveň sofistikovanějších systém používaných Microsoftem nebo Apple, je ale otázka, zda nepřichází příliš pozdě a to i když za ním stojí významné firmy, zejména mobilní operátoři. 

Český T-Mobile už do OMA šlápnul, ačkoliv ve starší verzi. Jeho právě spuštěný portál <a href="https://play.t-music.cz/">T-Music Play</a> nabízí prodej hudby ve formátu DCF, tedy DRM Content Format a PlaysForSure. DCF není nic jiného, než OMA DRM hudba zakódovaná do AAC. Slabší je to s podporou telefonů, T-Mobile uvádí podporu pár Nokií a Sony Ericssonů. Licence se posílá na telefon jako SMS zpráva (binární, takže u většiny mobilů neviditelná), právo máte na čtyři telefony a zároveň s tím jedno zařízení schopné přehrávat WMA (Microsoft DRM). Právě distribuce pravidel práv pomocí SMS byla nejčastěji oreptávaná záležitost u OMA RM 1.0.

Další, kde se DRM letos řádně propere, je letošní 3GSM kongres v Barceloně, kam jsem ke své lítosti pro naprosté pracovní přetížení letos nevyrazil. Ale nebojte, presentace dostanu, všechno pročtu a prostuduju. V mobilní hudbě a zejména mobilním videu je ještě mnoho neoraných polí, které slibují velkou žeň při setbě z bohatých venture investičních fondů a dost možná i z chudších kapes. Jen kápnout, na to pravé. 

<h2>S DRM je to jako s kuší... </h2>

Po pravdě řečeno se mi ale nejeví, že by DRM mělo být ten pravý spasitel hudby. <strong>Připomíná mi to populární historku o zákazu kuší církví v ranném středověku</strong>. Rozumějte: urozený muž si koupil za <em>veeelmi drahé</em> peníze brnění, koně, dva panoše k tomu, meč (vše v ceně dvou vesnic) a vyrazil si do války. Čímž v armádě vytvářel neporazitelný ekvivalent tanku. Jen do doby, než muže méně urozeného, ale pragmatického, napadlo zkonstruovat kuši, tedy zařízení, které na rozdíl od luku mělo takový tah na tětivě, že šípem s ocelovou špičkou prorazilo na dvě sta kroků brnění. 

Církev usoudila, že kuše je zbraně ďáblova, protože z urozeného pána dělá paňácu na odstřel. A pod hrozbou klatby zbraně zakázala. Po dalších letech se ukázalo, že zákaz jí není mnoho platen, protože běžný lapka nebo povstalec už beztak v případě prohry čekal šibenici a ne pozvánku na pobitevní párty.  Nic nepomohla ani následná poznámka svatého oficia v tom smyslu, že exkomunikace znamená vyměnit šibenici za hranici, což není zrovna pohodlnější způsob úmrtí. 

Nakonec se stále častěji stávalo, že rytířská jízda se setkávala s lidmi, kteří neměli co ztratit a volili vzdálenou exkomunikaci raději, než konkrétně blízké rozšmelcování valachy a těžkou jízdou. A tito lidé kuše používat neváhali. Nakonec zákaz kuší padl. 

O pár století později se objevil podobný problém, když se protiváhou tanku stala pancéřová pěst. Zatímco armádní stratégové se poučili a už se ani nepokoušeli panzerfaust zakázat, majors jen potvrzují pravidlo, že historie je nejmoudřejší učitelka s nejpitomějšími žáky...

S DRM je to stejné. Vypadá to jako dobrý nápad ho lidem direktivně vnutit, jenže oni nemají co ztratit. Radši si tu hudbu přepálí od souseda z CD, na kterém žádné DRM není, nebo použijí torrent a podobné služby. 

<strong>PS: A kde nakupuju hudbu já?</strong> Mám rád legální hudbu, z níž něco jde umělcům, ale obskurní české pokusy s DRM mi nejdou pod fousy. Takže nakupuju na <a href="http://AllOfMP3.com ">AllOfMP3.com</a> nebo <a href="http://MP3Search.ru">MP3Search.ru</a>. Je to legální, pohodlné a levné. Děkuji za dobrou službu, jíž rád udělám reklamu.