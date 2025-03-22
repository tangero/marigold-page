---
ID: 2082
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/novy-marigoldi-design

  '
post_date: 2007-02-22 13:56:18
post_excerpt: ''
published: true
summary_points:
- Marigoldův dočasný design byl vylepšen autorem s pomocí Japana a CSS expertů.
- Po čtyřech měsících od přechodu na nový systém byl upravený design nasazen.
- Problémem zůstává zub v logu a hlavičce způsobený hyperportálovou lištou.
- Autor se pokouší pomocí CSS posunout obrázek pozadí, ale zatím neúspěšně.
title: "Nový Marigoldí design"
---

Že Nonameho design Marigolda byl dočasný, bylo veřejné tajemství. Veřejným tajemstvím také bylo, že dočasnost se může protáhnout na řadu let. Takže jsem na tom trochu zapracoval a za pomoci Japana a dalších CSS dobrodinců dopracoval rozpracovaný design určený pro nasazení na Marigoldovi. Čtyři měsíce po přechodu na nový systém bylo na čase. 

Drobné zádrhele jsou tu stále. Budu je časem ladit, momentálně mne nejvíce vadí ten zub v logu a hlavičce stránky, který vznikl přidáním naší "hyperportálové lišty". Kdybyste někdo věděli, co s tím, dejte vědět, metoda pokus omyl zatím nezabírá. Domníval jsem se, že se mi podaří pomocí CSS posunout ten obrázek pozadí trochu dolů, aniž bych ho musel editovat v editoru, ale asi ne. Zkouším konstrukci zhruba v tomto stylu, jenže ono to nějak nefunguje: 

<code>body {
	margin: 0;
	padding: 0;
	background: url('http://www.marigold.cz/wp-content/themes/marigold/css/pozadi.png') repeat-x left;
	background-position: 20px top;
	font-family: 'Trebuchet MS','Lucida Grande', Arial, sans-serif;
	text-align: left;
	font-size: small;
	font-weight: normal;
}</code>

Jen tak na okraj. Vím, že to není nejhezčí webový design. Ale udělal jsem si ho já, což při mém pracovním vytížení a praktickém povědomí o CSS hraničí se zázrakem :)