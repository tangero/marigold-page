---
ID: 2189
title: Ale ano, SMS jízdenku lze obelstít
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/ale-ano-sms-jizdenku-lze-obelstit
published: true
post_date: 2008-01-03 16:58:58
categories: [Mobilní sítě, MHD]
---
<p>Na jedné vánoční párty se mi chlubil vývojář aplikace pražských SMS jízdenek, že to mají tak chytře vymyšlené, že to nelze obejít. Zdvořile jsem se usmál té sebevíře a namítl, že obejít lze všechno a je to jen o vůli toto obejít. Prý ne, prý to nejde obejít.</p>


<p>Takže si postavme modelový příklad, jak lze pražskou SMS jízdenku obejít (je to jen modelové řešení s četnými pozdravy dotyčnému):</p>


<!--more-->

<p>Máme jeden centrální telefon s aplikací, která každých 90 minut objedná jednu SMS jízdenku. Máme skupinu zákazníků, kteří platí provoz tohoto telefonu. Všichni tito zákazníci znaji telefonní číslo tohoto telefonu. V případě kontroly nahlásí revizorovi svůj telefon jako vybitý (pokud ho chce vidět) a uvedou mu telefonní číslo tohoto telefonu. Revizor ověří terminálem platnost SMS jízdenky a ta je záhy potvrzena jako validní, protože skutečně validní je a revizor nemá jak ověřit, že cestující toto číslo nemá při sobě a jízdenku sdílí s ostatními.</p>

<p>Trocha matematiky: při platnosti jízdenky za 26 Kč po dobu 90 minut potřebujete 416 Kč denně na SMS jízdenky. Pokud uvážíme měsíc o 31 dnu, potřebujeme cca 13 000 Kč na SMS jízdenky, abyste pokryli 24 hodinový interval. Při ceně měsíční jízdenky 550 Kč (v Praze) potřebujete minimálně 24 lidí, kteří se budou na akci spolupodílet, pravděpodobně ale alespoň dvojnásobek, aby se jim to všem rentovalo, studenti mají navíc jízdenku levnější.</p>

<p>Optimalizace: SMS jízdenky lze kupovat na různé zvýhodněné prepaid kupony. Lze také platit jen v dobu 5-24 hodin, kdy jezdí metro. Atd atd.</p>

<p>Obrana: ne právě snadná, leč myslitelná. Bylo by potřeba přidat příznak, že revize této jízdenky byla provedena v jiné lokalitě, dotyčný se bude bránit, že dostat se metrem z Anděla na Černý most za pět minut je jeho osobní problém. Variantou je povinnost předložit číslo ke kontrole, což ale začnou řvát ti, jimž se mobil opravdu vybije. Prostě mne nenapadá komfortní vychytání této možnosti.</p>

<p>Dopravnímu podniku zbývá doufat, že se to nikomu nevyplatí organizovat. Udělat to pro pět kamarádů je něco jiného, než shánět padesátku důvěryhodných lidí, s nimiž by někdo jízdenku takto sdílel.</p>

<p>Ale řešení to je :)</p>
