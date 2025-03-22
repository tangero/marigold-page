---
ID: 2971
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/navigace-v-bobtnajici-a-nesrozumitelne-webove-aplikaci

  '
post_date: 2015-01-05 07:30:59
post_excerpt: ''
published: true
summary_points:
- Energomonitor řeší zjednodušení složitých energetických dat pro zákazníky.
- Většina zákazníků chce šetřit peníze, ne rozumět energetickým pojmům.
- Segmentace zákazníků do šesti skupin podle motivací zlepšuje personalizaci informací.
- Používá se služba Intercom.io pro interaktivní reakce na chování uživatelů.
title: "Navigace v bobtnající a nesrozumitelné webové aplikaci"
---

<p>Nakousl jsem to na Twitteru, ale nebyl jsem mocen to ve 140 znacích vysvětlit. Jeden z hlavních UX problémů, které řešíme v <a href="http://www.energomonitor.cz">Energomonitoru</a>, je způsob zpřístupnění relativně složitých dat zákazníkům, kteří o ně vlastně ani nemají zájem. Většina zákazníků, pokud něco, chce šetřit peníze. Rozumí tedy pojmům koruna/euro, ale ne energetickým pojmům, jako je spotřeba, příkon, spalné teplo či tepelná setrvačnost atd. Někdy lze energetickou veličinu převést jednoduše na koruny, jindy ne. V řadě případů je vhodné rozumět tomu, jak původní energetická veličina funguje, protože to umožní efektivně šetřit. Například už jen takovou spotřebu nelze snadno převést na koruny. Kromě toho, že musíte znát cenu, používá řada lidí dělený tarif, kdy v určitých časových pásmech se aplikuje nižší cena. Musíte tedy vědět i to, kdy ke spotřebě došlo. A má-li zákazník efektivně šetřit, měl by vědět, jak spotřebu přesouvat do levnějšího pásma, což hodně závisí na typu spotřebičů.</p>


<p>Proto se v energomonitoru zabýváme tím, jak jednotlivé informace či funkce zpřístupňovat uživatelům a jak je v energetice “nenásilně” vzdělávat. První etapou je samozřejmě rozumně použitelný web, což je průběžná práce s ohledem na to, jak se přidávají nové funkce. Druhou byly vzdělávací emaily. Když si registrujete energomonitor, začnou vám chodit každý týden emaily s návodem, jak si zprovoznit službu či jak ji využít k úsporám. Třetí iterací je zjištění, že reakce uživatelů na tyhle emaily se dost liší. Někomu vadí (i jen fakt, že si je musí odhlásit), jiný je ignoruje, další přečte a nic z toho nepoužije, až po ty, co chtějí víc takových informací. A tak jsme si rozškatulkovali naše potenciální zákazníky do šesti skupin podle motivací k používání produktu a nyní rozvažujeme, zda má smysl se ke každé chovat nějak jinak. Z obrázku je vidět, co jsou motivace u jednotlivých skupin a k tomu se snažíme napasovat servírované informace. Geek spíše ocení tip na to, jak sledovat vypnutí televize, zatímco pro kategorii energopoor je to zbytná informace, raději by tip na nějakou úsporu, která je zase pro geeka spíše nepodstatná.</p>


<p>No a po čem jsem pátral, jsou zkušenosti odjinud. Velké servery či služby, které se snaží podstrkávat svým zákazníkům obsah přizpůsobený jejich segmentaci, tedy bez toho, že by uživatel říkal, co chce a nechce vidět. Českých serverů se to asi moc netýká s výjimkou těch největších se to myslím nevyplatí, hledal jsem, zda o tom nepublikovaly nějaké studie či presentace velké služby jako Mint, FitBit, LinkedIn, Amazon atd. Zda takový přístup, kdy nabízíte uživatelům různě viditelné funkce či je nějakým způsobem na webu i emailu tlačíte k jejich používání měl smysl a zda práce se segmentováním uživatelů se vyplatila. Proč je to pro nás zásadní? Některé funkce energomonitoru jsou jednoduché, jiné už složitější. Vidíme, že zákazník si ty funkce prokliká na začátku, ale to jim ještě moc nerozumí a už se k nim nevrací. Jenže mezi tím se s energetikou líp sžije a ty funkce by už lépe chápal. Jak ho k nim dostrkat? Jak ho naučit je používat jinak, než videotutorialem, na který se ne každý podívá?</p>

<p>Zatím jsme na začátku pokročilejšího návrhu. Implementovali jsme službu <a href="https://www.intercom.io">Intercom.io</a>, která sleduje, který zákazník co používá a umožňuje na to nějak interaktivně reagovat. Po měsíci od nasazení nové funkce můžete uživatelům, kteří ji nepoužili, ale už použili nějakou jinou funkci, poslat avízo do aplikace, ať to oprubují. Odkaz na tutorial, když vidíte, že se jim funkce nepodařila rozchodit. Intercom umožňuje hodně hraní bez velkého programování na straně serveru, což je pro nás a pro takové výzkumničení podstatné, neváže to vývojové kapacity.</p>

<p><strong>Poznámka na závěr:</strong> poradit, že aplikace má být srozumitelná, to je hezké. Má. Ale lidi energiím nerozumí, rozumět ani zpravidla nechtějí a je potřeba se s tím poprat jinak, než odkazem na studium fyziky třetího ročníku gymnázia…  Navíc je třeba brát v potaz, že celá ta věc není jen pro Česko, ale i pro jiné země, kde věci mohou fungovat mírně či dosti jinak … </p>