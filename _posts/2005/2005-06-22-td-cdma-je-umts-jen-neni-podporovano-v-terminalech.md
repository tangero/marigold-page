---
ID: 1690
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/td-cdma-je-umts-jen-neni-podporovano-v-terminalech

  '
post_date: 2005-06-22 08:54:00
post_excerpt: ''
published: true
summary_points:
- TD-CDMA je standardizačními orgány od roku 1998 považováno za integrální součást
  UMTS.
- Výrobci mobilních telefonů TD-CDMA nepodporovali, protože by to zdrželo nástup UMTS.
- FDD je v UMTS používáno pro okruhově spínaná data a klasický přenos dat.
- TD-CDMA umožňuje asymetrické přenosy dat, ale má problémy s řízením výkonu a synchronizací.
title: "TD-CDMA je UMTS. Jen není podporováno v terminálech."
---

<p>Vznikl s tím trochu zmatek. Je ta nová technologie, kterou bude T-Mobile nasazovat, UMTS nebo ne? Já s oblibou říkám, že pokud se hovoří o 3G, lze prohlásit cokoliv a je to pravda. Taktéž v tomto případě nelze zcela jasně stanovit, co je a co není pravdivé tvrzení. Faktem je, že dle názoru standardizátora patří TD-CDMA od roku 1998 integrálně do rodiny UMTS standardů jako druhá duplexní technologie k FDD, k frekvenčnímu duplexu. Rovněž v technických specifikacích 3GPP, který práci na UMTS standardu převzal, figuruje TD-CDMA jako součást standardu. Z toho můžeme neomylně vyvodit, že TD-CDMA ve skutečnosti je UMTS. </p>

<p>Výrobci mobilních telefonů ale usoudili jinak a podporu TD-CDMA do svých terminálů nezařadili. Důvod byl jednoduchý a prostý, nikdo je do toho netlačil a patlat se s TD-CDMA by zdrželo nástup terminálů pro UMTS o další dva roky. Z toho bychom mohli rovněž spravedlivě usoudit, že tato technologie tedy není součástí UMTS. Co je větší pravda - realita nebo teorie standardu? Na to není jednoznačná odpověď.</p>

<h4>Jak je to s duplexy v UMTS?</h4>
<p>Když jsem před lety začínal s UMTS standardem, dost mne mátlo, že první věta každého textu o UMTS začínala tím, že UMTS předepisuje jak frekvenční, tak časový duplex. Dále v textu se ale už nikdy o časovém duplexu nehovořilo. Z toho jsem získal dojem, že časový duplex je nějak tajemně skryt pod frekvenčním duplexem a mátlo mne to. Později se ukázalo, že knihy pouze téma TD-CDMA mazaně vynechávaly. Pro přenos okruhově spínaných dat se v UMTS používá výhradně frekvenční duplexace z mnoha důvodů, jež považuji za dobré. Rovněž klasický přenos dat ať již v provedení klasické Release 99 nebo HSDPA je realizován na FDD, frekvenčním duplexu. Jenže v době tvorby standardu se přemýšlelo o tom, že pro výrazně asymetrické přenosy dat není frekvenční duplex vhodný. Důvod je nasnadě - frekvenční duplex nabízí symetricky stejnou kapacitu pro download jako pro upload a pokud potřebujete kapacitu přerozdělovat asymetricky, jako třeba v případě přístupu k internetovému obsahu, kde více stahujete než odesíláte, máte probém. Nedostává se vám kapacita na downlinku, zatímco kapacita uplinku přebývá. </p>

<p>U TDD je tomu jinak. Celá komunikace probíhá na jedné frekvenci a základnová stanice pouze "zmlkne" na časový úsek, kdy očekává vysílání z mobilky. A samozřejmě opačně mobilka mlčí po časový úsek, kdy očekává vysílání základnové stanice. Celý tento komunikační rámec TDD má definovanou délku 10 ms a je rozdělen do patnácti časových úseků, slotů - každý o trvání 0,667 ms (podobně to známe u GSM). Aby se předešlo problémům s interferencemi, má v sobě každý časový slot na konci ještě hraniční periodu, po kterou už mobilka/základnovka nevysílá. Dva z těchto timeslotů jsou určeny pro signalizaci na downlinku (jeden pro broadcast a druhý pro obecnou signalizaci), jeden na timeslot je pro signalizaci směrem k základnovce, tedy na uplink. Zbývá dvanáct timeslotů pro data.  </p>

<p>Rozdíl mezi FDD a TDD vidno z obrázku</p>

<p><img src="/wp-content/uploads/20050622-tddfdd.jpg" alt="TDD a FDD vícenásobný přístup" width="400" height="352" /></p>

<h4>Výhody a nevýhody TDD</h4>
<p>Výhody i nevýhody jsou zřejmé. Hlavní výhodou je, že pokud spravíme mobilku o tom, že by měla mlčet častěji, můžeme ihned a dynamicky změnit objemy dat tekoucích k mobilce v neprospěch těch tekoucích od mobilky do základnové stanice. Ergo dokonalá možnost asymetrie, protože teoreticky lze vypnout odesílání dat z mobilky úplně po dobu, kdy mobilka nepotřebuje do sítě data odesílat a naopak mobilce lze přiřadit celou kapacitu sítě. Teoreticky. </p>

<p>Prakticky vznikají problémy, z nichž bych jako nejvážnější zmínil řízení vysílacího výkonu a vlastní interference. Vše totiž funguje kolosálně, pokud je v síti jedna mobilka a jedna základnovka, což je sice dnes typická konfigurace TD-CDMA sítí (viz Optus v Sydney), ale není to udržitelný obchodní model. Horší je, jakmile přidáme základnovky a mobilky. Ponejprv je třeba, aby mobilka i základnovka pregnantně věděla, kdy smí a nesmí vysílat, k čemuž jí slouží řídící kanál, příkladmo Shared Channel Control Channel (SHCCH). Podruhé je třeba důsledně řídit vysílací výkon jak základnových stanic, tak mobilek a to tak, aby se nerušily. Velmi snadno může vzniknout situace, kdy by mobilka komunikující s jednou základnovou stanicí překřičela jinou mobilku ve své blízkosti, která už ale komunikuje s jinou základnovou stanicí. Řešení tohoto problému není zrovna jednoduché a IP Wireless bývá často napadáno, že se s řízením vysílacího výkonu nevyrovnalo zrovna nejlépe. </p>

<p>Dalším problémem je synchronizace. Mobilky i základnovky musí vědět, kdy maji vysílat a kdy mají poslouchat, protože jinak by se zarušily. K tomu je nutná časová synchronizace. Lze použít časovou synchronizaci přes satelitní systémy jako GPS nebo přes distribuci času v síti skrze nadřazené základnové stanice. V problémech můžeme pokračovat - například kolísání vyzařovacího diagramu, kdy posun mobilek v prostoru spolu s odrazy a tedy působením dopplerova efektu ovlivňuje signálovou skladbu na základnové stanici. </p>

<p>Právě pro možnost asymetričnosti provozu se o TD-CDMA v UMTS uvažovalo a proto se i také prosadilo, ačkoliv větší roli zřejmě v prosazení hrálo lobby operátorů vlastnících patenty k této technologii. Ostatně právě TDD technologie je ta, která v UMTS sítích měla zajistit rychlosti až 2 Mb/s, tak často s oblibou u UMTS uváděné jako maximální rychlost. Jenže proto se také TDD předpokládala pro malé vzdálenosti od základnové stanice, řádově do 4 km a pro málo se pohybující uživatele, v zásadě pro městské aglomerace, kde může být infrastruktura hustěji. Stávající rychlosti UMTS 384 Kb/s založené na FDD jsou něco úplně jiného.</p>

<h4>Modifikace u IP Wireless</h4>
<p>K technologii IP Wireless je třeba ještě jedno dodat. Jejich technologie TD-CDMA se sice v základních aspektech shoduje s definicí UTRAN TDD (tedy TD-CDMA specifikace zahrnutá do UMTS normy), ale v řadě detailů se odlišuje. Jen díky tomu také IP Wireless může nabízet vyšší sdílené rychlosti na sektor, než jsou zmíněné 2 Mb/s; IPW propaguje dvoj i trojnásobek). To ale také automaticky znamená, že pokud se objeví mobilní telefony UMTS podporující i TDD, nebude je možné v síti IP Wireless použít na plné rychlosti a otázka je, zda vůbec (propagační materiály naznačují, že ano - jenže duální FDD/TDD sítě nikde nejsou rozvinuty, takže nelze ověřit). Je také ale pravda, že IPW se snaží své dodatky protlačit do UTRAN TDD, jak je s tím úspěšná, mi není známo - ale v normě o tom nic není. Vzhledem k tomu, že většina infrastrukturních výrobců spoléhá spíše na úpravy  FDD vedoucí do  HSDPA končin (<a href="/item/high-speed-downlink-packet-access-hsdpa">blíže o HSDPA zde</a>), nejsou tyto snahy asi chápány příliš vážně - ale to je jen můj soukromý názor. </p>

<p>Na závěr je třeba dodat, že v posledních letech (vlastně v 3G sítích) už přestalo být důležité, které rodiny standardů jsou si či nejsou příbuzné - důležité je, jak to výrobci doflikují do mobilů. A ti se samozřejmě snaží, když čují zajímavý trh. Pokud se T-Mobile se svým TD-CDMA chytí a bude mít statisíce uživatelů (tedy zejména pokud by to implementoval v jiných částech Říše, zejména těch německy hovořících), jistě by se našel výrobce, který by radostně kývnul na objednávku půlmilionu terminálů s podporou TDD. Že bychom se s nimi setkali v nejbližších patnácti měsících na našem trhu ovšem považuji za velmi nepravděpodobné - ani IP Wireless / UT Starcom přes všechny sliby vzorový 3G terminál nemá.</p>

<p>PS: Problematika TD-CDMA a TDD versus FDD v UMTS sítích je samozřejmě mnohem složitější, než jsem zde v rychlosti, zjednodušeně a z hlavy zkusil načrtnout, bohužel se tomu zatím žádný server nevěnoval, takže se musíte spokojit s tímto nebo na Amazonu nakoupit příslušnou literaturu. Ze srdce mohu doporučit knihu z dílny Artech House, <a href="http://www.diesel-ebooks.com/cgi-bin/item/1580537634">TDD-CDMA for Wireless Communications</a> (tady je i PDF), odkud jsem také vykradl obrázek nebo novější a skvělou <a href="http://www.amazon.com/exec/obidos/tg/detail/-/0470861045/ref=pd_bxgy_img_2/102-8640934-0896913?v=glance&amp;s=books">Wideband TDD: WCDMA for the Unpaired Spectrum</a>, autor Prabhakar Chitrapu. Po stránce technické je <a href="http://www.mobilmania.cz/Profi/AR.asp?ARI=110323">stručná výjimka zde</a> na MobilManii. A <a href="http://www.telnet.cz/index.php?ID=445">UMTS TDD Rity Pužmanové</a>.
</p>