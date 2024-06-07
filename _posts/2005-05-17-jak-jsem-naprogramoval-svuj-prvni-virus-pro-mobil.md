---
ID: 1649
title: >
  Jak jsem naprogramoval svůj první
  virus pro mobil
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/jak-jsem-naprogramoval-svuj-prvni-virus-pro-mobil
published: true
post_date: 2005-05-17 14:23:58
---
	<p>Včera jsem byl na konferenci AEC, výrobce to antivirových a jiných bezpečnostních řešení. A při té příležitosti jsem se zajímal o mobilní antiviry a následně jsem si vzpomněl na humornou historku, kterak jsem <em>"naprogramoval svůj první virus".</em></p>
	<p>Už je to mnoho let (tak rok 1998  ), dost možná to byl vůbec první virus na mobilní telefon, prosím tedy o trochu shovívavosti, protože v době telefonů s hloupým operačním systémem to nebylo tak jednoduché. Snad je můj počin promlčen…</p>
	<p>Jak je zvykem, i tento virus byl omezen pouze na určité mobilní telefony, v tomto případě na telefony Nokia.  Ty měly kdysi zajímavou funkci (nevím, zda přetrvala do dneška) – pokud jste měli zprávu v hlasové schránce, mohla jim na displeji svítit ikonka se symbolem kazety. Kdysi dávno tuhle funkci podporoval Eurotel u NMT telefonů, v GSM se ale nepoužívala, takže ikonku jste neměli šanci vlastně nikdy vidět. Finta byla samozřejmě v tom, že ikonku jste mohli aktivovat binární SMS, takže uživatel neviděl, že mu přišla SMS, jen se mu rozsvítila ikonka a zůstala trvale na displeji. </p>
	<p>Tehdy nějak jsem zjistil, jakým formátem SMS zprávy se tahle ikonka aktivuje a rozhodl jsem se realizovat svůj "virus". Vytvořil jsem script, který přes GSM modul (pamatujete Siemens M1? Vyloudili jsme je tehdy z ostravského <a href="http://www.gsmobil.cz">GSMobilu</a>) aktivoval na definovaných číslech pomocí SMS tuto ikonku a zároveň  uživatele informoval, že na jeho telefonu byl aktivován odposlech, což detekuje ikonka kazety v horní stavové řádce. Pokud se domníváte, že nemáte být odposloucháván, zašlete zdůvodnění pomocí SMS zpět odesílateli zprávy. Odesílatelem bylo zvláštní číslo v GSM modulu a protože šlo o GSM modul bez hlasové služby, tak všichni volající, co zkoušeli na něj zpět volat, dostali tehdy dosti podezřelou hlášku <em>"volaná stanice není vybavena pro tuto službu"</em>.</p>
	<p>Spustil jsem scriptík, nakrmil ho čísly a asi dvě hodiny jsem se mlátil smíchy z těch zdůvodnění, které mi lidi posílali - bylo to dojemné, jak lidi dokážou zdůvodnit, že nemají být odposloucháváni. Až do chvíle, než se Petr přišel podívat, proč mu nejede SMS brána a zjistil, že jsem mu odpojil GSM modul – dostal jsem vynadáno, GSM modul mi Péta zabavil a celý svět tak zachránil před mým virem, jenž jsem následně zastrčil hluboko do šuplíku.</p>
	<p><em>Ach ta doba mládí a činů nerozvážných :) </em>
</p>