---
ID: 1764
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/jdeme-do-zpravodajskeho-designu

  '
post_date: 2005-08-12 08:27:32
post_excerpt: ''
published: true
summary_points:
- Mobil server začínal jako odkazovník na nezávislé sekce, nikoliv jako zpravodajský
  web.
- Čtenáři Mobil serveru brzy požadovali centralizaci odkazů na aktualizované články.
- Inspirováni News.com zavedli zpravodajský design s perexy článků na titulní stránce
  v roce 1997.
- Diskusní fóra pod články zavedl Mobil server v roce 1997, inspirován CGI scriptem.
title: "Jdeme do zpravodajského designu"
---

<p>Jak už jsem řekl, design Mobil serveru v prvních měsících neměl se zpravodajským vzhledem nic do činění, titulní stránka byla odkazovníkem na samostatné, jednoduše vedené rubriky. Nebylo to samoúčelné, původně jsme server chápali jako spojení nezávislých stránek, navíc jsme vůbec nepočítali s nějakým zpravodajstvím. Pouze jsme hodlali udržovat seznamy telefonů, přehled operátorských služeb a jejich ceníky, tedy všechno to, co operátoři ani výrobci mobilů na internetu v té době neměli. Každý z nás tří tedy měl na starosti svoji „sekci“ a tam si řádil po libosti. Jenže už krátce po neoficiálním startu v listopadu 96 a ještě silněji po tom oficiálním v lednu 97 se ukázalo, že tohle uspořádání není šťastné. Lidem se nechtělo procházet nezávisle na sobě aktualizované sekce a protože si všimli, že každá z těch sekcí se aktualizuje minimálně jedou týdně, chtěli, abychom odkazy na aktualizace centralizovali.
</p>

<!--more--><p>Nejdříve jsme se to pokusili ošulit a Petr nainstalova na server nějaký script, který zjišťoval, kdy byly které stránky upraveny a automaticky je řadil podle data modifikace. Jenže ani to nebylo to pravé ořechové, protože když jsme opravili nějaký překlep nebo zaktualizovali maličkost, ihned se to na výpisu tohoto scriptu projevilo. </p>

<p>Rozhodli jsme se poohlédnout, jak to řeší ve světě. Abychom předešli podezření, že jsme padlí na hlavu a proč jsme hned od počátku nepoužili klasický zpravodajský styl, rád bych předeslal, že na přelomu let 1996/7 nebylo vůbec jasné, CO je to ten klasický zpravodajský styl. Různé servery to řešily různě a to diametrálně odlišně. Asi nejrozšířenější řešení bylo použití sekce ve stylu „What´s New“ – tedy odkaz na titulní stránce, který vás navedl na posledně přidané články, tedy prakticky stejné řešení, jaké jsme použili i my. Titulní stránka odkazovala tedy na nejrůznější sekce a na novinky, sama ale přehled novinek a posledních článků neobsahovala.  </p>

<p>Jiné servery novinky na webu vůbec nepublikovaly a rozesílaly je výhradně emailem, takže web jim vlastně sloužil jen pro registraci k odběru emailových zpráv. V Čechách toto řešení používal L. Zajíček pro rozesílání News on Net – rozesílal je emailem a na bajt.cz se najít nedaly nebo jen nepravidelně. </p>

<p>Další servery pro publikování používaly PDF – a to ať už formou dokumentů stažitelných na webu, tak objednávaných emailem. Zde bylo hlavním motivem snaha o zachování grafické jednoty, řada publikací totiž nenáviděla na internetu fakt, že nebylo možné přesně ovlivnit, jak dokument v tom kterém prohlížeči a nastavení systému vypadal. Na tohle nebyli z novin zvyklí – článek v novinách vypadal stejně v LA jako v NY. </p>

<p>Některé nejmodernější servery používaly poutání článků přímo z titulní stránky – abych byl přesnější, šlo zejména o <a href="http://www.news.com">News.com</a> patřící společnosti CNET a také konkurenční ZD News. To byla v českém pojetí přímo hypermoderna, protože to už jste museli předpokládat, že každý týden ne-li každý den bude něco nového, aby se vyplatilo to poutat přímo z titulní stránky. Navíc to nabourávalo dosavadní vnímání internetu jako doplňkového média k papírovým titulům. Podobný systém použil pro své Invexové vydání na podzim roku 1996 server Živě, jenže ten pak prakticky odumřel a byl aktualizován sporadicky. </p>

<p><b>Takhle vypadal News.com v prosinci 1996</b></p>

<p><center>
<img src="/wp-content/uploads/20050812-newscom.jpg" alt="News.com" width="500" height="599" />
</center></p>

<p>Ani v USA, ani na českém internetu nebyl tento design (tedy na titulce perexy článků a odkazy na plné verze) nijak vítězící. Příkladem byl Neviditelný pes, který používal plný výpis článků na titulní stránce, tedy dnes bychom řekli formu blogu.</p>

<p><b>Takhle vypadal Neviditelný pes v roce 1997</b></p>

<p><center>
<img src="/wp-content/uploads/20050812-neviditelnypes.jpg" alt="Neviditelný pes 1997" width="500" height="433" />
</center></p>

<p>Tento přístup nám byl nejsympatičtější, ale měl dva problémy: ponejprv by bylo složité jej udržovat technicky, protože všechny stránky se v té době dělaly ručně a znamenalo by to vytvářet dvě kopie textu – jednu na titulní stránku a jednu do patřičné rubriky. To nám nepřišlo příliš komfortní. Druhým zádrhelem byla rychlost běžného připojení k internetu. V roce 1996 byla většina uživatelů vybavena stěží modemy o rychlosti 14,4 Kb/s, dvojnásobná rychlost byla spíše výjimkou a jiné rychlosti spíše exotikou nebo akademickou sítí. Přišlo nám, že by se lidem příliš velká stránka nelíbila a navíc články na Mobil serveru měly delší životnost, než politické komentáře na Neviditelném psovi – alespoň jsme si to říkali. </p>

<p>Rozhodli jsme se tradičně pro kompromis a to hned trojí. Zaprvé jsme zavedli v první polovině roku 1997 emailové zpravodajství nazvané Mobil News. Chodilo jednou týdně emailem a zahrnovalo zpravodajství ze zahraničí, tedy co se kde děje nového, kdo jaký kontrakt podepsal v rozsahu tak jednoho odstavce plus odkazy na nejzajímavější články z vydání na webu.  </p>

<p>Za druhé jsme zavedli rubriku Obsah, tedy odkaz na výpis posledně aktualizovaných či přidaných článků – obdobu Whats new a zrušili jsme ji až někdy v roce 1998 při přechodu na systém Genesis. </p>

<p>A do třetice jsme se rozhodli pro zpravodajský design na bázi News.com. Jednak proto, že News.com pro nás byl tradičně velkým vzorem a také proto, že jsme s tímto schématem stránky měli dobré zkušenosti z Media serveru. </p>

<p>Náš vztah k News.com byl dlouhodobě zaznamenáníhodný. Nejdříve to byl jen můj veliký vzor, pak jsem se při jedné konferenci seznámil s jedním z šéfů tohoto serveru a často jsme si psali a vyměňovali názory na to, jak má zpravodajský server vypadat. Dokonce to došlo tak daleko, že jsme se pohádali o to, zda mají na serveru být diskuse nebo nemají. News.com je prostě odmítal používat s tím, že čtenáře zajímá názor redaktora, tedy článek – a nikoliv nějaké tlachání čtenářů. Já jsem oponoval, že čtenáři mohou mít zajímavé doplňující informace. Jenže názoru Cnetu dávalo za pravdu to, že v té době kam až moje paměť sahá žádný významný zpravodajský server diskuse ve článcích nepoužíval. Pokud, tak nabízel zvláště diskusní server, ale diskuse přímo ve článku? To bylo něco nemyslitelného.</p>

<p>Jak pro nás bylo obvyklé, rozhodl jsem se pro test na našich čtenářích. Chvilku jsem hledal, až jsem na CGI-resources naše script v PERLu, který jsem nahrál na server, aniž bych se zeptal Fufa, našeho administrátora. Chápal jsem, že by z mého pokusu nebyl happy. Šlo samozřejmě o diskusní script, který do stránek vložil okénko pro diskusi s výpisem příspěvků a možností vložit nový. Psala se polovina roku 1997 a hned první den bylo pod článkem asi dvacet diskusních příspěvků, z nichž řádově pětici jsem považoval za slušně hodnotné. Script měl jednoznačný úspěch. Večer si mého scriptíku všiml Fuf a když se mu stabilizovaly životní funkce, celý ho přepsal, aby se pomocí toho scriptu nedala alespoň modifikovat neoprávněně titulní stránka, naštěstí na to za tu dobu nikdo nestihl přijít. Dostal jsem sice vynadáno, ale diskuse ve článcích se staly úspěchem. Lidé se nás poprvé mohli přímo pod článkem nebo recenzí zeptat na to, co je zaujalo, mohli reagovat mezi sebou i bez nás. Mohli nás směřovat někam k tomu, co je zajímalo, i když diskuse o ničem a anonymní nadávky se nám samozřejmě časem nevyhnuly. Koncem roku 1997 vzniká v USA Slashdot.org, který si bere diskuse a komentáře ke článkům jako hlavní konkurenční výhodu oproti News.com a o další rok později News.com podlehl a komentáře také přidal, byť velmi nenápadně a aby se neřeklo. Diskuse záhy doplnilo i Živě a další pomalu vznikající české zpravodajské servery. </p>

<p>Další rozvoj diskusí na Mobil serveru přišel až v roce 1998 s novou verzí redakčního systému zvanou Genesis 2. Ta již diskuse přímo integrovala, po pravdě řečeno hlavně proto, že Fuf se stále více osypával z toho perlového bastlu, jímž se diskuse řešily dosud. Navíc ten perlový script se staral o stále vyšší a vyšší zátěž serveru. Nové diskuse pod články jste si mohli přidávat na serveru do sledované složky, nechat posílat do emailu, vypisovat podle data, podle témat, různě řadit a vyhledávat v nich. Jediné, co Fuf zásadně odmítal, byla možnost, aby čtenáři svoje diskuse také zakládali a k tomu se nenechal dokopat nikdy – cokoliv, kde si uživatel mohl něco sám založit z web rozhraní, bylo pro Fufa bezpečnostní noční můrou, o které nechtěl slyšet. </p>

<p>Rok 1998/9 byl také na dlouho posledním rokem, kdy se něco zajímavého se zpravodajstvím a diskusemi na českém internetu pohnulo. Zatímco ostatní servery je začaly zavádět, my jsme v Mobilu pracovali na tom, že povýšíme čtenářské názory a diskusní příspěvky v podstatě na roveň redakčních článků. Samozřejmě, v závislosti na jejich pisateli. Zcela nová koncepce se chystala několik let, protože mělo jít jak o architekturální změny redakčního systému, tak o pečlivě budovanou koncepci hodnocení autorů komentářů, změnu jejich grafické presentace i způsobu řazení. Slashdot něco podobného představil koncem roku 1999 a měl s tím obrovský úspěch, který jsme chtěli následovat. </p>

<p>V největším utajení měl přerod na zcela novou koncepci Mobil serveru proběhnout v roce 2001, nebo spíše v průběhu 2002. Vzniklo několik grafických koncepcí a ještě jsem ani nevytvořil zadání pro programátory, jenže už bylo jasné, že je řada jiných prioritních problémů a že většinu času stejně utopím v nečem jiném. Žádná změna se nekonala a s mým odchodem v roce 2003 zůstala i definitivně zapomenuta. Až v roce 2005 přišel alespoň s hodnocením diskusních příspěvků server Root.cz (přebral systém Slashdotu) a v polovině roku 2005 velmi zjednodušeně a řekl bych nedokonale také server Novinky.</p>

<p>Také koncepce zpravodajského serveru zůstala od poloviny roku 1997 prakticky beze změny. Zatímco do poloviny 1997 jsme se ještě drželi rozdělení titulní stránky podle tématických okruhů, poté jsme již všechny články řadili sestupně dle data bez ohledu na rubriku. Tento systém se osvědčil nejvíce, jenže po roce 2000 jsme začali cítit, že by tento systém potřeboval změnu. Problém Mobil serveru totiž byl v tom, že začal mít stále více a více článků, denně na něm vycházela desítka materiálů s různou „časově trvalostní hodnotou“. Proč měla aktualita platná jeden-dva dny odsouvat recenzi nebo popis nové technologie? </p>

<p><center>
<b>Mobil server do května 1997</b><br/>
<img src="/wp-content/uploads/20050812-mobil-early97.gif" alt="Mobil server do poloviny 1997" width="500" height="375" />
</p>

<p><b>Mobil server od května 1997</b> (porovnejte s designem News.com - inspirovali jsme se, dokonce vzájemně)<br/>
<img src="/wp-content/uploads/20050812-mobilserver97.jpg" alt="Mobil server od poloviny 1997" width="500" height="546" />
</center></p>

<p>Provizorně jsme to vyřešili rozštěpením serveru do několika částí. Vzniklo Palmare.cz věnované PDA, vznikl software.mobil.cz s přehledem software a manuálů pro mobily a zejména vznikla koncepce Profi.mobil.cz – personalizovaného mobilního portálu, kde by se sledovalo, co čtete a nabízely se vám relevantní materiály. Dokonce jsme jej i vytvořili, i když bez personalizace a s tím, že protěžoval materiály dlouhodobé hodnoty. Na tento server jste přišli jednou za týden a četli jste jen podstatné materiály jako technické návody, recenze, technologické novinky a přehled obchodních novinek. I když jsme server vytvořili, nikdy jsme ho nepropagovali a ani o něm nenapsali, chtěl jsem počkat, až doděláme personalizaci. Nikdy jsme ji nedokončili, po vstupu Mafry do Mobil serveru byly nakonec jiné starosti, než jsem doufal a Profi.mobil.cz nám už nikdy nepomohl zachránit profesionální lidi z telekomunikací jako naše čtenáře. </p>

<p>Pokud se za zpravodajským designem ohlédnu, jsem rád, že se nám hned od počátku podařilo manévrovat dlouhodobě správným směrem, i když jsme samozřejmě v roce 1997 nemohli počítat s tím, že jednou budeme mít patnáct redaktorů na hlavní pracovní poměr. Koncepční změny, které podle mne musely přijít po roce 2001, aby respektovaly posuny a změny ve vnímání Mobil serveru čtenáři i změnu role telekomunikačního zpravodajství a telekomunikačního webu se bohužel nikdy neuskutečnily a Mobil server jako největší konglomerát českého technického zpravodajství nakonec ztratil hybnost. Změny se nedaly uskutečnit jen silou vůle jednotlivce a jeho vizí. </p>

<p>Selhal jsem v tom, svoji vizi prosadit v rámci velké vydavatelské skupiny. A po mém odchodu z Mobil Media / Mafra v roce 2003 se nenašel ani nikdo jiný, kdo by změny prosadil. Na serverech Mobil Media a nakonec i na serverech iDNESu tedy prakticky od roku 1999 nedošlo k žádné podstatné změně, vyjma rozsahu zpravodajství. A to byl ten problém - servery zůstaly nepřehledné.
</p>