---
ID: 2391
title: 'Za tajemstvím notifikací v&nbsp;iOS5 a&nbsp;vývoje architektury mobilních operačních systémů'
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/za-tajemstvim-notifikaci-v-ios5-a-vyvoje-architektury-mobilnich-operacnich-systemu
published: true
post_date: 2011-06-09 11:34:00
categories: [Apple, iPhone]
---
Je chvíle, tak se podívejme na to, jak Apple řeší šlamastiku s absentujícím dashboardem a co je nového v notifikacích na iOS5.
Především, androidisti si zvykli mi podsouvat v komentářích, že jim cpu Apple jako jediné řešení. Nikoliv. Každý prosím, nechť si používá, čeho jest mu libo. Máme tu pět velkých mobilních operačních systémů (iOS, Android, WP/WM, RIM a Symbian), hromadu malých, takže snad si vybere každý. Já se jen snažím vysvětlit, proč zmíněná řešení použil Apple a co v nich vidím za positiva. To, že Apple nepovoluje všechno, co technologie umožňuje, je logická daň za požadavek, který na platformu má, co se výdrže a odezvy zařízení týká. A zdá se, že řada lidí to oceňuje, logicky ale ne všichni. Ti mohou sáhnout po jiném zařízení. Vysvětlit něco se znalostí pozadí není totéž, jako něco bezhlavě propagovat. Pokud to nechápte, jděte <a href="http://www.disney.com">prosím sem, tu vám bude dobře</a>.   

<img src="http://www.marigold.cz/wp-content/uploads/notifications-center-240788.png" alt="notifications-center-240788.png" border="0" width="386" height="377" align="right" />Ke stejnému kroku sahá řada dalších výrobců. Stojí za to si povšimnout, že ačkoliv velká část mobilních telefonů je vybavena přisvětlovací diodou u fotoaparátu, jen velmi málo telefonů umožňuje tuto diodu rozsvítit trvale a používat ji jako baterku. Ačkoliv by to uživatelé pravděpodobně někdy ocenili a technicky je to triviální věc. Důvod? Ona taková Cree ledka sosá akumulátor dost slušně. Ale to si necháme zase někdy na jindy včetně zkazek, že se vám zdá, že Android/iOS/Symbian telefon vašeho kolegy vydrží zrhuba stejně, jako váš iOS/Symbian/Android. 

<h2>Notifikace iOS versus Android</h2>

Řekl jsem, že notifikace iOS jsou diametrálně jinak udělané, než u Androidu. Opět to není vidět na první pohled. V čem? iOS narozdíl od Androidu má za sebou backend servery, které zprostředkovávají notifikace z internetu. V Androidu může notifikaci poslat jen běžící lokální aplikace, nebo to musí vývojář řešit po svém (a od verze 2.2 pro úplnost dodám, je tu C2DM). Na iOS je to naopak uděláno proto, aby si aplikace mohla registrovat požadavek (naslouchání na novou IM zprávu třeba), uklidila se z paměti a až přijde notifikace, aby se mohla obnovit do původního stavu s notifikací, což dělá dojem, že aplikace multitaskuje.

A to je také důvod, proč se Apple s notifikacemi nějakou dobu potýkal. Už za současného stavu, kdy jsou v iOS4 notifikace často na prd, neboť se „ztrácí“ (neexistovala historie), se jich poslalo 100 miliard. Bylo třeba naškálovat servery a serverové řešení, protože se smysluplnnou historií notifikací se dá čekat, že provoz exploduje.  To, že je notifikace umístěna v horním řádku jako na Androidu, je logické – Apple zde umisťuje notifikační zprávy jako ikonky zmeškaných hovorů již od počátku, ještě v době, kdy Android neexistoval. Hovořit v tomhle případě o opisování je dobrý příklad fanatismu – notifikace v horním řádku mají mobilní telefony již od pradávna, měl ji už můj první Benefon v NMT síti. 

<h2>Notifikace versus Dashboard</h2>

Technický rozdíl mezi notifikací a dashboardem? Z hlediska spotřeby vcelku podstatný. Notifikace zprávu přijímá, dashboard se dotazuje. Dotazovat se, znamená cyklicky, tedy s větší spotřebou. Přijmout zprávu znamená, dostat jen informaci o změně. Zase, jde o procenta baterie a to není málo. 

Když jsem tedy mluvil o tom, že Apple pojme dashboard po svém, stalo se. Jen formou notifikací – jsou trvale přítomné na locknuté iOS5 obrazovce a umožňují i příjem zpráv z internetu formou push notifikací, tlačených, nikoliv vyžádaných zpráv. Což otevírá zajímavé možnosti bez nutnosti mít paměť zaplněnou běžícími programy. 

<img src="http://www.marigold.cz/wp-content/uploads/lock-screen-notifications-240408.png" alt="lock-screen-notifications-240408.png" border="0" width="386" height="348" align="right" />
Tím také neříkám, že tenhle přístup Apple v iOS se musí dlouhodobě osvědčit, zatím ale vypadá jako progresivní. Rozhodnout se pro něj nemusíte, můžete si vybrat svobodně jiný systém a hlasovat nohama. Není ale bez zajímavosti, že podobné notifikace používá i BlackBerry a nakonec od Android 2.2 via <a href="http://android-developers.blogspot.com/2010/05/android-cloud-to-device-messaging.html">Cloud to Device Messaging</a> i Google. 

<h2>Mobilní operační systémy</h2>

Pokud bych měl shrnout své osobní dojmy, Apple se nechal z velké části zdržet svým cloudovým řešením, které má dále posunout jeho prodej digitální hudby – serverová řešení mu nejdou tak dobře, jako Google. Tento backend handicap nyní snad srovnal a může dále škálovat funkce, která na cloudu závisí. A je třeba si všimnout, že jak Android, tak iOS, jsou na cloudu stále více závislí, mnohem více, než RIM Blackberry a citelně více, než Windows Phone. I u WP ovšem vývoj zřetelně jde tímto směrem. 

Je stupidní, dohadovat se, kdo od koho opisuje. Za prvé je inspirace a vylepšování jiných řešení hnacím motorem vývoje, za druhé základní směr byl udán a zatím se nepodařilo najít jiný směr vývoje mobilních operačních systémů, než ten, který právě probíhá. Tedy, pokud se nechcete vrátit k vizi Windows CE a snaze transformovat Windows XP na mobilní telefony. Tímhle směrem kráčí Google i Apple a i ostatní. Apple vsadil na „řízenou kvalitu“, tedy na to, že upřednostňuje přívětivost, odezvu a výdrž před otevřeností, Google naopak vsadil na otevřenost. Obě firmy v poslední době slevují ze svých pozic, protože vidí, že trh to umožňuje či vyžaduje. Google zavádí omezení, Apple otevírá více možností. Proč, to je zase jiné téma.