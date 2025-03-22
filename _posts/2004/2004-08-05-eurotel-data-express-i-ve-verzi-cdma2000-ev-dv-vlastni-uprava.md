---
ID: 1234
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/eurotel-data-express-i-ve-verzi-cdma2000-ev-dv-vlastni-uprava

  '
post_date: 2004-08-05 08:14:00
post_excerpt: ''
published: true
summary_points:
- GTran modem s Eurotel Data Express aktivován a funkční s průměrnou rychlostí 3-400
  Kb/s.
- VoIP telefonie přes Data Express (Softphone, SIP, Fayn, H.323) fungovala i při souběžném
  odesílání dat.
- Nestabilita modemu způsobuje problémy, například pády notebooku při vybití baterie,
  řešením jsou nové ovladače.
- Data Express se prodává velmi rychle, zájem zákazníků předčil očekávání Eurotelu.
title: Eurotel Data Express i ve verzi CDMA2000 EV-DV (vlastní úprava)
---

<p>
Včera jsem se zmocnil jednoho modemu GTran a aktivace Eurotel Data Express, doma jsem všechno instaloval na svém notebooku dle přiloženého návodu a ejhle, všechno fungovalo na první zátah. Tedy až na to, že doma nemám v obýváku stabilní signál a bylo třeba připojit tu prutovou anténu, která opravdu výrazně pomáhá. </p>
<p>
Nerad bych se opakoval ve chvále a informacích, které zní odevšud jinud. Ano, jede mi to rychle jako z praku, průměrně kolem 3-400 Kb/s a i mně ta rychlost v průběhu stahování samotného kolísá. Na velká slova o rychlosti je ale zatím docela brzo. Průměrný ping se pohybuje kolem 140-160 ms a toto zpoždění je velmi stabilní, pingal jsem hodinu a v podstatě jsem se mimo tyto hodnoty nedostal, vyjma zaváhání cílového serveru. </p>
<p>
Zajímavý byl <em>pokus s přechodem na EV-DV, tedy Data Voice.</em> Zkusil jsem totiž VoIP telefonii přes Data Express. Nejdříve Softphone a SIP protokol, pak Fayn a jeho H.323 - obojí šlapalo bez problémů, dokonce jsem při tom měl nahozený Overnet a linka se poprala s tím, že odesílal data do internetu rychlostí tak 4 KB/s při telefonování. Bohužel jsem neměl sluchátka, takže reprodutkory mikrofonu trochu vazbily, ale to byla chyba mé sestavy. A v případě X-Lite (SIP program) jsem si bohužel nějak vypnul mikrofon a pořád nemůžu přijít na to, jak ho dát zpět (ne, není to ztlumení ve Windows), takže mne protistrana neslyšela. MaLér o našich pokusech <a href="http://www.maler.cz/index.php?id=142">informuje zde</a>.</p>
<p>
Pitomá je ovšem nestabilita. Od lidí z Eurotelu jsem se dozvěděl seznam triků, takže jsem již věděl, že modem se nebude nabíjet poté, co spustíte GTran program a že nabíječku je třeba připojit ještě před tím. Také jsem věděl, že vypnutí modemu pro slabé baterky může shodit nějaké staré notebooky. Moje dva měsíce stará IBM R50 to ale také nepřežila a vypnutí modemu při vyčerpání baterií ji shodilo do Blue screen. Problém byl v tom, že modem se snažil upozornit notebook, že by měl přejít do Power Save režimu a notebook s XP to nějak nerozdýchává, protože ho modem neupozorňuje zrovna korektně. Měla by to spravit nová verze ovladačů. Ku stažení u Eurotelu. </p>
<p>
Další fintou je, že se mi modem nedaří zapnout, když je připojený k vypnutému notebooku. Je třeba nejdříve zapnout notebook, nebo odpojit kabel z modemu a zapnout jej. Ale to už je, řekl bych, maličkost.</p>
<p>
Finta se současným zapojením modemu a jiného síťového připojení, kdy najednou modem shodí spojení, mne postihla rovněž, nicméně jsem ji záměrně evokoval. Vskutku CDMA nemá rádo, když mu do sítě běží paket s jinou zdrojovou adresou, než jakou CDMA síť přidělila. Bohužel dostupná literatura je k tomuto velmi skoupá na informace a z několika zmínek pouze soudím, že síť si domyslí, že uživatel ukončil spojení, maje jinou adresu a aby šetřila zdroje, ukončí spojení i na své straně. Nicméně na tomto vysvětlení netrvám, literatury přímo k EV-DO je velmi poskrovnu v mé knihovničce :( Lze to ošetřit firewallem, Radek Hulán slibuje, že postup dá na svůj weblog, ostatně i on zde <a href="http://hulan.info/blog/item/eurotel-cdma-prakticke-zkusenosti-a-srovnani-s-gprs">recenzuje CDMA</a>.</p>
<p>
Na Root.cz najdete <a href="http://www.root.cz/clanek/2334">mini How-To pro Linux</a>. Modem je veskrze standardní seriové zařízení, takže jde rozchodit pomocí AT příkazů, jejichž <a href="http://www.eurotel.cz/public/5f/97/e0/f7/43578_56824_ATprikazy.pdf">seznam je zde</a> (v PDF). Jen mám mírné podezření, že modem je akorát standardní Qualcomm čipová sada osazená na desce a k tomu čtveřice konektorů (kromě USB, napájení a antény je tu ještě konektor pro GPS, jenž je k ničemu). Pardon, ještě displej - celkové provedení ale nic moc a problémy s ovladači tedy nejsou zrovna nejmenší. O digitálním podpisu pro XP si ovladače mohou nechat jen zdát. </p>
<p>
Pravdou ale také je, že když se vyhnete těmto nástrahám, funguje Data Express opravdu jako datový expres. Pro stahování web stránek je zcela porovnatelný s pevnolinkovým připojením jako je UPC Chello, protože web stránky se holt už o moc rychleji při vyšších rychlostech připojení nestahují v poměru k režii protokolu a jejich vykreslení, poznat je to samozřejmě při stahování souborů. Žádnou online hru jsem nezkoušel, žádnou nemám, takže nevím, jak to bude pro hraní...</p>
<p>
Poznámka na závěr: stejně rychle, jako Data Express funguje, se také prodává. Eurotel včera konstatoval, že zájem předčil jejich očekávání, přesná data ale zatím po jednom dni říci nechtěl. Z prodejen vím, že se CDMA prodává velmi dobře, v některých prodejnách dokonce vyprodali už první den a museli se nechat znovu zavážet. Prý mají zájem hlavně noví zákazníci. Snad to není jen kumulovaný zájem a bude to zájem trvalý, protože služba zatím vypadá opravdu moc hezky. </p>
<p>
<strong>Marigoldí </strong><a href="http://www.marigold.cz/forum/viewforum.php?id=6"><strong>diskusní fórum o CDMA je zde</strong></a><strong>.</strong></p>