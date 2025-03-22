---
ID: 1543
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/motorola-a-jeji-hsdpa-uplne-jina-kava

  '
post_date: 2005-02-18 07:04:00
post_excerpt: ''
published: true
summary_points:
- Motorola předvedla HSDPA s reálnou rychlostí 9,6 Mb/s na jeden sektor.
- Deset klientů streamovalo video, MP3 a prohlíželo web s latencí 50-70 ms.
- Motorola karta D1100 zvládá HSDPA 3,6 Mb/s, dostupná bude ve čtvrtém kvartále.
- Road testy HSDPA dosahovaly 2,3 Mb/s při rychlosti 50 mil/h ve městě.
title: "Motorola a její HSDPA – úplně jiná káva"
---

<p>Včera jsem na výstavišti chtěl kromě nějakých firemních věcí skouknout i HSDPA u Ericsson a Motoroly. Nejdříve jsem se vypravil do Motoroly, na stánku měli hezké powerpoint demo a kartu Motorola D1100 s podporou HSDPA, jenže mne upozornili, že HSDPA demo zde není. Ukázalo se, že pro operátory a další hóch nóbl společnost je všechno k vidění kousek za výstavištěm, i nelenil jsem, otočil jsem cedulku press aby kompromitující nápis nebyl vidět a dorazil jsem na ono místo  (nebylo to lehké najít, ale podařilo se).</p>

<p>Motorola zde měla pronajatý asi sedmipatrový barák nacpaný BTSkami, jednačkami a vší možnou i nemožnou technikou. Hosteska s překvapením konstatovala, že nemám sjednanou schůzku, já jsem se zatvářil něco na způsob, že zítra chci začít stavět síť na HSDPA a batoh na zádech mám nacpaný dolary, nakonec se omluvili, že žádný obchodník na mne nemá čas a že si budu muset vystačit s technikem. Vystačil a velmi dobře. </p>

<p>Hned z kraje se musím přiznat, že HSDPA od Motoroly mi přišlo jako úplně jiná káva, než co mi ukazovali číňani a Nortel a už jsem také pochopil paniku toho chlápka z Nortelu, když zjistil, že se mu lámeme do command lajny.</p>

<p>Článek je trochu delší, s pár fotkama, tak jsem ho rozdělil a je třeba kliknout pro pokračování.
</p>

<!--more--><p>Motorola měla ve svém ukázkovém centru rozchozené HSDPA na indoor NodeB (viz fotka) – maličká krabice (asi jako od banánů), která sama o sobě utáhla HSDPA na 9,6 Mb/s. Těch necelých deset Mb/s je zatím hranice Motoroly na jeden sektor, ale prý budou upgradovat až na těch 14 Mb/s. </p>

<p><img src="/wp-content/uploads/20050218-P1000407.jpg" alt="Indoor NodeB pro HSDPA od Motorola" width="450" height="327" /></p>

<p>Na tuto Node B bylo připojeno deset demo klientů, kterým se z ovládacího panelu daly přiřazovat různé testovací role, například kolik z nich má streamovat video, kolik z nich sosá MP3, kolik browsí či stahuje poštu atd. Co se děje u jednotlivých klientů bylo vidět na plazmách, takže se stačilo v místnosti rozhlédnout a viděli jste, že streamování videa opravdu funguje a není to žádná potěmkinovka. Na další konzoli bylo vidět aktuální a špičkové rychlostní zatížení všech deseti klientů, dalo se okamžitě sledovat, jaký je load na NodeB a v síti obecně. Viz další obrázek.</p>

<p><img src="/wp-content/uploads/20050218-P1000403.jpg" alt="Monitoring rychlosti přípojných klientů" width="450" height="256" /></p>

<p>Nastavili jsme celou síť do režimu, kdy byla plně vytížená přenosy a kdy NodeB musel provádět reshaping pásma, aby nějak ukáznil klienty dožadující se vyšší kapacity, než jakou mělo NodeB k dispozici. Pak jsem pustil ping  a technik Motoroly nehnul ani brvou. Měl proč být v klidu – latence se v síti pohybovala mezi 50-70 ms (při klasickém pingu na hraniční element za radiovou sítí) se střední hodnotou na 62 ms. V tom okamžiku jsem z té stanice stahoval video na rychlosti přes 2,3 Mb/s. Opravdu impozantní výsledek. </p>

<p>Zeptal jsem se, jak je možné,  že Motorola dosahuje polovičních čísel, než Nortel. Bylo mi osvětleno, že Nortel se domnívá, že k nasazení HSDPA do sítě bude stačit softwarový upgrade, zatímco Motorola se domnívá, že k obsluze rychlostí desetinásobných oproti původnímu WCDMA záměru bude potřeba posílit hrubý procesorový výkon připadající na NodeB tak, aby nedocházelo ke zbytečným zdržením na straně NodeB. </p>

<p>Motorola také vystavovala kartu D1100, která zvládá HSDPA na 3,6 Mb/s; dost rozdíl oproti 1,8 Mb/s, které nabízí Qualcomm čipset a na něm postavená karta Sierra Wireless. Podle Motoroly bude karta dostupná ve čtvrtém kvartále letošního roku a spolu s ní i 3G Motorola telefony podporující HSDPA. </p>

<p>Uživatelský dojem z Motorola HSDPA byl jen ten nejlepší. Z konzole odpovídaly internetové servery velmi rychle a bez znatelné prodlevy (jak latence hluboko pod 100 ms slibuje), technik Motoroly uměl bez zaváhání zodpovědět i záludnější dotazy a zanechal příznivý dojem. Dokonce se pak pochlubil i několika koncepty, které Motorka vyvíjí – například modulem pro výrobce plazma/LCD displejů, který zacvaknete do displeje a vyberete si film, který si chcete přes HSDPA stáhnout. Moc fajné – vyzkoušeli jsme zastreamovat si ho na plazmu a bylo to fakt dobré. </p>

<p><img src="/wp-content/uploads/20050218-P1000404.jpg" alt="Testovací telefon..." width="450" height="293" /><br/>
<i>Na obrázku vidíte "testovací HSDPA telefon" - to abychom se v něm mohli rochnit po libosti...</i></p>

<p>Na závěr jsem se podíval na road testy HSDPA, kdy testovací mobil jezdil v autě a zkoušelo se, co HSDPA vydrží při průjezdu městem. Při rychlosti 50 mil/h (víc se báli kvůli pokutě, nedalo se kvůli zácpě a na dálnici došel signál z testovací základnovky) spadla rychlost na 2,3 Mb/s – což bylo pořád velmi slušné. </p>

<p><b>Co dodat: pořádně udělané HSDPA rulez :)</b></p>

<p>PS: Protože jsem chtěl stihnout letadlo a u Motorky už jsem se zdržel, nedostal jsem se na to demo Ericssonu a nakonec ani Nokia, nakonec jsem ale obnovil svoji pokulhávající důvěru v smysl HSDPA, takže to ani nemělo smysl (protože o tom, co se kde nakoupí, já už rozhodovat nebudu).
</p>