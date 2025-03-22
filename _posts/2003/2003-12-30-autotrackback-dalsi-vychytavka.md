---
ID: 768
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/autotrackback-dalsi-vychytavka

  '
post_date: 2003-12-30 15:30:00
post_excerpt: ''
published: true
summary_points:
- TrackBack je málo používaná funkce na českých webech.
- Autor vytvořil AutoTrackBack, jednodušší automatický systém logování odkazů.
- AutoTrackBack zobrazuje odkazy pouze z přímých odkazů na zprávy Marigolda.
- AutoTrackBack má omezení, zobrazuje se jen po kliknutí na "Zalinkovat".
title: "AutoTrackBack – další vychytávka"
---

<p>
Funkce TrackBack je na československých weblozích (?) málo obvyklá, znám asi jen dva nebo tři servery, co ji používají. Nicméně jde o zajímavou funkci - ke každému příspěvku, spotu,&#160;lze automaticky přiřadit odkaz, že na tento příspěvek ze svého webu odkazujete. A čtenář se tak dozví, co si o tomto tématu myslí další blogeři. </p>

<p>
Původně jsem chtěl implementovat TrackBack funkci tak, jak je dokumentovaná, jenže TrackBack musí podporovat redakční (weblogerské) systémy a to jen málokdo má. U nás nejrozšířenější systémy to nemají a update Bloguje.cz stojí na tom, že Artur má doma nepoužitelné ADSL a není skrze něj schopen protlačit soubory na server. Kdyby Telecom věděl, za co všechno může :)</p>

<p>
No, abych to zkrátil, naprogramoval jsem si trošku jednodušší systém, který je hlavně plně automatický a <STRONG>nazval jsem ho AutoTrackBack</STRONG>. Systém loguje weby, z nichž se někdo dostal na zprávy Marigolda a tyto odkazy vypíše, jen odkazy z agregátorů zpráv a z vyhledávačů vyhazuji, protože to asi nikoho moc nezajímá (a pokud ano, tady je moje <A href="/from.html">test stránka</A>, která vypisuje za poslední dva dny všechny referery na Marigolda). </p>

<p>
Má to samozřejmě svá omezení: </p>

<UL>
<LI>autor příspěvku musí odkazovat přímo na zprávu, tedy na link, která mu udává ten oranžový odkaz Zalinkovat pod každou právou. Při linkování přímo na titulku Marigolda to logicky nefunguje, protože nelze zjistit, jakou zprávu kdo chtěl linkovat. </LI>
<LI>zpětý odkaz dovede čtenáře na URL webu, z něhož bylo kliknuto. V případě mnoha weblogů to bohužel je titulní stránka, protože na ní je plný výpis textu, z něhož si čtenář kliknul a dostal se na marigolda (chápete doufám tuto větu :)</LI>
<LI>AutoTrackBack se nedozví o odkazu, na který ještě nikdo nekliknul.</LI>
<LI>Odkazy se nezobrazují na titulce, tam by to administrátoři Genesis asi velmi těžce nesli, AutoTrackBack se zobrazuje jen po kliknutí na Zalinkovat. Například <A href="http://www.marigold.cz/zprava.html?id=26366">zde je to vidět</A>, jak to vypadá, na spot už někdo odkazuje. </LI></UL>
<p>
Pokud se to osvědčí či neosvědčí, zapracuji podle toho klasický TrackBack systém. Hloupé na tom je, že o telco je tu naprosté minimum weblogů, takže velké počty odkazů nečekám. Ale pokud někoho zajímají souvislosti a jiné názory, snad mu to pomůže. </p>