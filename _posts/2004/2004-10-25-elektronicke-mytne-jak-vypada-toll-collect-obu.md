---
ID: 1372
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/elektronicke-mytne-jak-vypada-toll-collect-obu

  '
post_date: 2004-10-25 17:30:00
post_excerpt: ''
published: true
summary_points:
- Toll Collect využívá OBU, krabičku s GPS/GSM pro digitální mýtné.
- OBU se montuje do kamionu a sleduje jeho polohu na dálnici.
- GPS rušičky a souběžné komunikace způsobovaly problémy systému.
- Toll Collect zavedl kontrolní místa pro ověření funkčnosti OBU.
title: Elektronické mýtné – jak vypadá Toll Collect OBU
---

<p>
Když jsem tu <a href="/item/digitalni-mytne-jsem-jeste-nepochopil">minulý týden psal</a> o elektronickém / digitálním mýtném, dostal jsem řadu reakcí. Nejvíce mne zaujalo to, co psal v komentářích Marko Zekič a z čeho jsem získal nástin dojmu, že kamion je rozšiřitelný o další přídavné karty podobně, jako počítač vybavený například PCMCIA, tedy že nebude problém vsunout u kamionu do slotu Toll Collect kartu, která se spojí s palubním počítačem a bude využívat jeho výpočetní kapacitu. Za následek by to mělo to, že by takové zařízení nemělo příliš mnoho smyslu krást. </p>

<p>
Věnoval jsem pozornost německému Toll Collectu po technické stránce jen zběžnou, takže mi to přišlo jako překvapující, zásadní informace o velmi mazaném řešení. Jenže pak mi to začalo být podezřelé - tak mazaná řešení se neobjevují příliš často, navíc vím zcela bezpečně, že kamiony, které jsem viděl (a které používají naše špedice, že Jardo :), žádné sloty na rozšiřující karty nemají. A tak jsem se šel podívat, jak Toll Collect mašinka ve skutečnosti vypadá. </p>

<p>
Především se ukázalo, že žádné univerzální využívání slotů v kamionu nepřipadá u Toll Collect v úvahu ani kdyby tam byly. Toll Collect ve své plně digitální podobě nabízí OBU - On Board Unit. Tedy krabičku s embedded počítačem, GPS a GSM modulem. Tato krabička se namontuje do kamionu, anténa pro GPS/GSM se vyvede ven a krabičce se přiřadí konkrétní auto. Pokud auto s OBU jede po dálnici, pozná se podle GPS polohy, že jede po dálnici a až z ní sjede (resp vyjede ze zpoplatněného úseku), předá OBU informaci o délce trasy přes GSM do centrály Toll Collect. Jak přesně to funguje, vidíte na obrázku. </p>

<p>
<img src="/wp-content/uploads/1/20041025-tollcollect.jpg" alt="Jak funguje Toll Collect" width="550" height="251" /></p>

<p>
Jak vypadá přesně OBU, vidíte na obrázku (Grundig výrobek), zatím jsem dohledal dva výrobky a to od firmy Siemens a firmy Grundig. Rozdíl je prakticky jen v provedení - Siemens se montuje na palubní desku, zatímco Grundig se montuje do DIN přihrádky, jako rádio. Toll Collect tvrdí, že své OBU dostanou kamiony zdarma, zůstává však majetkem Toll Collectu.</p>

<div class="rightbox"><img src="/wp-content/uploads/1/20041025-grundig-tollcollect.jpg" alt="Grundig OBU Toll Collect" width="397" height="143" /></div>
<p>
Nepodařilo se mi ale dohledat technické specifikace OBU - tedy jakým procesorem a pamětí jsou vybaveny. Není ale už pochyb o tom, že jde o klasický malý počítač. Jsem zvědav, kdy se objeví první hacky a mody pro něj&#8230; </p>

<p>
Vtipné jsou problémy německého Toll Collectu. Záhy se totiž ukázalo, že po zpoplatněné dálnici můžete snadno jet i v okamžiku, kdy jedete po nějaké sousední souběžné komunikaci, což může být v německu častý jev. GPS má totiž problémy s přesností a Toll Collect tedy zabudoval do systému také odečet tachometru a gyroskop. Jenže je tu další problém - objevují se nabídky na GPS rušičky, které Toll Collectu znemožní získat kvalitní polohu přes GPS. Asi nepřekvapí, že rušičky jsou původem polské provenience a čekalo se, že polské kamiony se jimi mohutně vybaví. </p>

<p>
Toll Collect i na tohle nakonec reagoval právě zavedením zhruba 300 kontrolních míst, kde je přes infraport na každé OBU zjišťováno, zda je s ní všechno v pořádku a zda zná svoji polohu. </p>

<p>
Inu, vypadá to na dlouhý boj o elektronické mýtné. Doporučuji přečíst také <a href="http://www.economist.com/science/tq/displayStory.cfm?story_id=2724381">článek v The Economist</a>. Myšlenka psát kilometráže do pasů je sice méně elegantní, méně technicky účinná a potřebující práci lidí, nevyžaduje ale žádné velké počáteční náklady a nakonec u nás je práce levnější, než nějaké On Board Unit. Inu, drahá a nevyzkoušená technika za naše peníze - úředníkům se to rozdává&#8230; :(</p>

<p>
Stránky <a href="http://www.toll-collect.de">Toll Collectu jsou zde</a>.
</p>