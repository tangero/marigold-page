---
ID: 1664
author: Michal Krsek
layout: post
oldlink: 'https://www.marigold.cz/item/story-o-sousedskych-sitich-15

  '
post_date: 2005-05-31 07:00:00
post_excerpt: ''
published: true
summary_points:
- Lokalita jedna je pro freenet mrtvá kvůli konkurenci UPC Chello.
- Lokalita dvě úspěšně vytvořila vlastní CLOUD s "zabranými" IP adresami.
- Kruhová topologie s mizernou viditelností potřebuje 100m k uzavření.
- Pětigigahertzový spoj je prozatím odložen, čeká se na verdikt ČTÚ.
title: Story o sousedských sítích (15.)
---

<p>Tak se nám to pěkně vyvíjí. <br />
<br />
V lokalitě jedna jsme tak dlouho váhali s instalací pořádné antény na
střechu, že v mezidobí začala poskytovat v té lokalitě svojí službu
Chello společnost UPC. No a přiznejme si, že poměr cena/výkon/stabilita
je u Chello na trošku jiné úrovni než u freenetu (lepší pro uživatele).
Takže tahle lokalita je z hlediska freenetu mrtvá. Aspoň bude méně
elektromagnetického smogu v centru Prahy.<br />
<br />
V lokalitě tři se nám zatím nepodařilo podniknout nic zajímavého. <br />
<br />
Zajímavý vývoj se podařil v lokalitě dvě. Skutečně se nám podařilo
udělat vlastní CLOUD. Alokaci IP adres a čísla autonomního systému jsme
po netečnosti člověka zodpovědného za koordinaci těchto aktivit
vyřešili metodou "zábor". Zajímavé bylo, že to komunita bez problémů
akceptovala. <br />
<br />
V tuto chíli pracujeme na vytvoření (dvou) kruhové topologie. K
uzavření obou kruhů chybí cca 100m. Bohužel s mizernou viditelností.
Stabilita směrování se nám výrazně zlepšíla, bohužel internetová brána,
kterou používám, zůstala v původním CLOUDu a v cestě máme jeden
zarušený spoj (a původní CLOUD zatím nereaguje pozitivně na nabídky
dalšího spoje). Vypadá to, že začnu používat bránu na druhé straně
našeho CLOUDu.<br />
<br />
Spousta lidí má spoustu chytrých rad a doporučení k nasazení
pětigigahertzového spoje. Zatím k tomu přistupujeme konzervativě,
počkáme na nějaký verdikt ČTÚ. Snažíme se také udělat nějaký slušný
monitoring infrastruktury, abychom mohli rozumně naplánovat směrování.
Momentálně používáme jako IGP OSPF (jak je ostatně zvykem ve většině
CLOUDů CZF) a externí propojení je udeláno pomocí BGP4. <br />
<br />
V původním CLOUDu došla trpělivost ještě dalšímu kusu infrastruktury.
Narozdíl od nás neklade takový důraz na CZFree.Net, takže nastavil
směrování staticky a celé to orientuje směrem k Internetu. Z CZF
používá hlavně adresní prostor ... </p>