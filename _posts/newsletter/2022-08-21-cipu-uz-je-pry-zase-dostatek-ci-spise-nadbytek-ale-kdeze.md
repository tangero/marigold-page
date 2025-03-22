---
author: Patrick Zandl
categories:
- Patrickův newsletter
- Apple
- AI
- Mobilní technologie
- Startupy
- Česko
- EU
- Automotive
date: '2022-08-21'
layout: post
original_newsletter: 'Patrickův newsletter #53: Moje Stezka Českem. Čipů už je prý
  zase dostatek či spíše nadbytek? Ale kdeže... '
summary_points:
- Čipů nadbytek se týká hlavně procesorů pro osobní počítače, nikoliv celého trhu.
- Specializované čipy, mikrokontrolery a zákaznické obvody stále vykazují nedostatek
  a vysokou poptávku.
- Zakázkové čipy (SoC, ASIC) rostou nejrychleji, ovlivňují i pokles čínských výrobců
  mobilů.
- Výroba čipů je složitá, drahá a vyžaduje státní podporu, Applied Materials má stále
  vysoké objednávky.
title: "Čipů už je prý zase dostatek či spíše nadbytek? Ale kdeže..."
---

I do českých médií probublala velmi optimistická zpráva Bloombergu, podle níž začíná být čipů na trhu nadbytek a očekává se pokles poptávky. Tak vznikla vlna optimismu, který - nutno říci - je značně nadhodnocený a založený na špatném chápání souvislostí. Pokud o tom více nepotřebujete vědět, tak ve zkratce: čipů je stále pro většinu použití nedostatek, roční dodací lhůty jsou běžné. Dostatek je procesorů pro osobní počítače. Pokud chcete zákaznický procesor, třeba svůj návrh, stoupáte si ve výrobě do velmi dlouhé fronty. 

My se uvedeme do širšího obrazu. Optimismus pramenil ze špatné interpretace jinak běžného ohlášení predikcí u tří významných výrobců čipů. Intel, Nvidia a Micron Technology ve finančních výsledcích uvedli, že očekávají pokles poptávky, Nvidia ji dokonce vyčíslila na 40 %. Po bezprecedentním růstu posledních dvou let by tedy přišel obrovský propad na čipovém trhu. 

Jenže jde o ten kontext. Všechny tři společnosti se soustřední na výrobu polovodičů pro běžné počítače. Intel dělá procesory CPU pro stolní a přenosné počítače, právě ho opouští Apple. Nvidia dělá GPU, grafické procesory pro grafické karty, které se hojně používají při těžbách kryptoměn. A Micron se soustředí na výrobu polovodičových pamětí, je tedy přímo svázán s trhem klasických počítačů, kde se používají DRAM, SSD nebo NAND paměti. 

Na trhu osobních počítačů je pokles právě nyní velmi zřetelný. V průběhu pandemie lidé potřebovali notebooky a počítače pro homeoffice, pro děti na školu a tak dále. Jenže pandemie ustoupila, lidé se vrací do kanceláří, bojí se recese a nemají dojem, že koupit nový počítač je nějak zvláště potřebná investice. Inovační cykly osobních počítačů se prodlužují, neboť kromě nových her není na nárůst výkonu žádné zvláštní použití. A když jsme u Nvidia, tu kromě toho trápí zhoršení kurzu kryptoměn, jenž snižuje zájem o těžbu a tedy nákup nových Nvidia čipů pro takové to malé domácí těžení. A také optimismus v případě Etherea, jež čeká přechod na Proof of Stake, což změní současnou spotřebu procesorů paralelizujících jednoduché výpočty. 

### Nejsou to jen procesory pro osobní počítače

Jenže svět čipů nejsou dávno jen osobní počítače. Vlastně se dělí do čtyř hlavních segmentů. 

Tím prvním jsou právě **výkonné univerzální procesory CPU** , které vyrábí především Intel a AMD, kde trh skutečně klesá. Podle organizace Mercury Research klesl odbyt procesorů pro stolní počítače ve druhém čtvrtletí 2022 na nejnižší úroveň téměř za 30 let. 

Druhou oblastí jsou **čipy specializované** na určité typy výpočtů, především pak grafické procesory GPU. Ty jsou velmi vázané na odbyt osobních počítačů, inovaci ve hrách a stavu optimismu kryptoměnové scény. I tam je pokles očekávatelný. 

Třetí oblastí jsou **jednočipy, mikrokontrolery (MCU)** určené pro řízení jednoduchých zařízení, například v automotive průmyslu. Bez jednočipů auto neumí řídit vstřikování paliva a dneska už ani stáhnout okénka. Těchto jednočipů bývaly v autech jednotky, dneska už ale velké stovky - jde sice o levné čipy, ale poptávka po nich roste a jelikož se vyrábějí především na starších linkách, výrobní kapacity pro ně se příliš nerozšiřují. Právě v této oblasti je stále značný převis poptávky nad nabídkou. Analog Devices (dodavatel automotive) uvádí, že počet jejích nevyřízených objednávek stále roste za stabilních cen. Její letošní "nejhorší čtvrtletí" se vyznačovalo 72% růstem tržeb. Podobně jsou na tom i další dodavatelé jako NXP Semiconductors a STMicroelectronics. 

Čtvrtou oblastí jsou nejrůznější **zákaznické obvody dnes nazývané SoC (Systems on a Chip) nebo ASIC (application-specific integrated circuit)**. V prvním případě SoC jde o čip, který integruje vše potřebné - včetně pamětí i třeba síťových rozhraní a grafiky). ASIC je navržený přímo pro konkrétní aplikaci, stále častěji i pro konkrétního klienta. Do této skupiny se řadí také ARMové procesory, ačkoliv technicky jde o mikrokontrolery - dnes jsou totiž mnohem spíše dodávány jako SoC s doplněnou pamětí, grafickým procesorem a síťovými rozhraními. 

Pro firmy, které kupují specializované čipy a ne procesory do desktopů, je situace nadále vážná. V tu samou dobu vydané prognózy Cisco udávají nedostatek čipů pro výrobu síťových prvků jako hlavní omezení.

Podstatné je, že mezi těmito kategoriemi se nedá výrobně snadno přecházet. Někdy to bolí, někdy to nejde vůbec. Hi-end univerzální procesory se dělají ve velkých sériích, kde je stěžejní výnosnost a zaběhlost procesu a také rozlišení (nanometry technologie). Naopak rychlost zavádění není tak nutná - série se pojede dlouho. Oproti tomu zákaznické procesory se musí zavádět rychle a to i na úkor výtěžnosti, i proto jsou první série taktovány níže. A mikrokontrolery se vyrábí dlouho, cena rozhoduje, zato lze použít staré linky i 300 nm, které se pro jiné procesory už dávno nehodí. 

### Trh zákaznických čipů dnes rychle roste

Je přitom potřeba si říct, že právě oblast zákaznických procesorů je dnes nejrychleji rostoucí. Většina dnešních mobilních telefonů používá nějakou formu SoC, začasté vyrobenou na míru konkrétnímu odběrateli. Takhle změna na trhu procesorů je také důvodem poklesu čínských výrobců mobilů. Podle výzkumné společnosti IDC zaznamenala Čína ve druhém čtvrtletí 14,7% pokles dodávek mobilních telefonů. Společnosti Xiaomi, Vivo či Oppo zaznamenaly prudký pokles prodeje. Za část může čínská zero-covid politika a opatrnost nakupujících, ale také nasycenost místního trhu, který v posledních letech horem-dolem do zákazníků rval 5G, na něž ale mnoho klientů z cenových důvodů přejít nechce, služby 4G jim přijdou dostatečné. 

Posledním důvodem je redukce počtu výrobců mobilních telefonů v Číně. Dříve totiž bylo pro "garážové výrobce" velmi jednoduché si poskládat mobilní telefon podle svého, nakoupili jste jednotlivé díly včetně procesorů, pamětí a baseband modemů, hrkli na desku, dali tomu fancy logo a bylo. Jenže v době, kdy se kvůli výkonu, spotřebě i celkovému řešení všechno řeší formou zakázkového SoC, je složité vytvořit svůj vlastní návrh takového SoC a dostat jej do výroby. Kromě toho USA v poslední době limitují přístup čínských firem k EDA software, který se k návrhům pokročilých čipů používá. EDA software amerických společností Cadence, Synopsys a Mentor Graphics (koupená 2017 německým Siemensem)—ovládají přes 70% trhu EDA software a vlastně 100% trhu pro návrh a simulaci velmi pokročilých SoC. Řada menších čínských společností přišla o jednoduše použitelné komponenty a protože neměla vlastní pokročilý vývoj, nakonec z trhu vysublimovaly. Zatímco v roce 2018 měli menší výrobci shrnutí ve statistikách jako _"others"_ třetinu čínského trhu mobilních telefonů, počátkem letošního roku to bylo již jen 11 % a to přes ústup Samsungu a Motoroly z trhu. 

Pokud si situaci zrekapitulujeme, neděje se nic, co se nedalo čekat. Klesá zájem o univerzální čipy určené pro osobní počítače, ať již o procesory, grafické procesory nebo DRAM paměti. Trh se saturoval. To jsou ty první dvě množiny čipů. 

Naopak o čipy pro spotřební elektroniku, strojírenství, automotive průmysl je pořád velký zájem a dlouhé pořadníky, nicméně kapacity se tu průběžně navyšují a v nejbližších dvou letech ještě skokově narostou o nově připravované fabriky. 

Důležitá je ta čtvrtá skupina čipů, která doposud patřila mezi specifická a neprobádaná území, jimiž vládlo převážně TSMC. Zásadní dovedností totiž je rychle nastavit výrobní linku na zákaznický design a vyrobit v dostatečné kvalitě a výtěžnosti požadovanou várku zákaznických procesorů. Což není legrace - většina fabrik nový procesor zavádí do výroby mnoho týdnů a to je důvod, proč nerady vyrábějí zákaznické procesory. 

> Polovodiče jsou ze své podstaty nejsložitější věci, které lidé vyrábějí, a vlastně nic jiného se jim složitostí nevyrovná. Výroba jednoho čipu trvá od začátku do konce více než 20 týdnů a spousta této práce je atomárně přesná. Jen "žárovky", které se používají k osvětlení destiček pro fotolitografické kroky, jsou nesmírně složitá zařízení velikosti autobusu, z nichž každé stojí až 100 milionů dolarů. Fungují tak, že vystřelují drobné kapičky cínu a přesně je zasahují laserem, aby generovaly přesně správnou frekvenci světla, které pak kaskádovitě prochází téměř atomárně přesnou konfigurací optiky, aby se maximalizovala rovnoměrnost. Kapičky cínu jsou ve skutečnosti zasaženy dvakrát, přičemž první pulz vytvoří oblaka, která účinněji přemění energii druhého laseru na potřebné světlo. A ve skutečnosti mají některá zrcadla střední kvadratické odchylky subatomární. 

Polovodiče jsou ze své podstaty nejsložitější věci, které lidé vyrábějí, a vlastně nic jiného se jim složitostí nevyrovná. Výroba jednoho čipu trvá od začátku do konce více než 20 týdnů a spousta této práce je atomárně přesná. Jen "žárovky", které se používají k osvětlení destiček pro fotolitografické kroky, jsou nesmírně složitá zařízení velikosti autobusu, z nichž každé stojí až 100 milionů dolarů. Fungují tak, že vystřelují drobné kapičky cínu a přesně je zasahují laserem, aby generovaly přesně správnou frekvenci světla, které pak kaskádovitě prochází téměř atomárně přesnou konfigurací optiky, aby se maximalizovala rovnoměrnost. Kapičky cínu jsou ve skutečnosti zasaženy dvakrát, přičemž první pulz vytvoří oblaka, která účinněji přemění energii druhého laseru na potřebné světlo. A ve skutečnosti mají některá zrcadla střední kvadratické odchylky subatomární. 

Dlouhá léta byl hnacím motorem pokroku procesorů takzvaný [Moorův zákon](https://cs.wikipedia.org/wiki/Moorův_zákon), jenž předvídal zdvojnásobení počtu tranzistorů a tím i výkonu procesoru každých 18 měsíců. A s tím si vystačil každý, kdo výpočetní výkon v jakékoliv podobě potřeboval. Jenže v poslední době se "běžným" postupem naráží na fyzikální hranice konstrukcí, takže si procesory obecně vypomáhaly triky, jako je přidání více jader procesoru nebo právě vyčleněním specializovaných procesorů - od grafických, přes umělointeligenční, až po speciálně navržené obvody SoC či ASIC. A ty jsou právě dnes ve středu zájmů - firmy mají zájem si je navrhnout, vyhnout se drahým univerzálním procesorům, vyházet nepotřebné části, optimalizovat je na to, co mají dělat a zároveň udržet spotřebu i velikost na uzdě. Tento trend je tak zřejmý, že i Intel bude takovou službu nabízet, včetně toho, že jeho konstruktéři pomohou doladit návrh procesoru i jeho uvedení do výroby. 

Jestli je Moorův zákon u konce s dechem, zatím jisté není a bylo by to na samostatné dlouhé povídání. Patrickův zákon ovšem stanovuje, že každé dva roky se zdvojnásobí počet lidí, kteří konec Moorova zákona neomylně předvídají. Podle mě tu s námi ještě nějakou dobu bude. 

Tak a to je zhruba celé. Tím jsme si vysvětlili, proč trh s procesory už dávno není jednolitým trhem, ale do čtyř hlavních skupin rozvrstveným mnohamiliardovým průmyslem, přičemž dění v jedné skupině trhu se nutně nemusí propisovat do druhé skupiny. Ono totiž vzít linku vyrábějící dnešní procesory Intel Pentium a začít na nich vyrábět jednočipové Atmely, dost dobře nejde - bylo by to neskutečné plýtvání prostředky. 

Do tohoto zmatku započítejme i incentivy, které do trhu výroby čipů přináší Čína, USA a Evropská unie a kde právě zjednodušující novinové články tyto úrovně rozdílů ve výrobě nejsou schopné zohlednit. Pak se nám nezdá zcela zřejmé, proč se určité způsoby podpory volí a zda to má smysl. V každém případě pro Evropu má velký smysl doinvestovat navýšení kapacit čipového průmyslu pro jednočipy používané zejména v automobilovém průmyslu. Stejně tak, jako je stěžejní vybudovat dostatečné výrobní kapacity pro články ukládající energii (záměrně nespecifikuji technologii), ale to už je jiné téma. 

Je důležité připomenout, že fabriky na výrobu čipů jsou nesmírně drahé provozy za desítky miliard dolarů s tím, že většinu této částky musí splatit během prvních pěti až sedmi let. V podstatě se tak do hry vkládají státní garance, ať již přímé, nebo formou závazných příslibů objednávek od automobilek pod státním vlivem, které umožní rychlou alokaci soukromého kapitálu na výstavbu čipových fabrik.

**Chcete happy end?**

Společnost Applied Materials, největší výrobce strojů na výrobu čipů minulý týden prohlásila, že stále dostává více objednávek, než je schopna splnit. Proč je nedokáže splnit? Protože sama nedokáže sehnat dostatek čipů na výrobu linek pro výrobu čipů... 

Tak a to je pro tentokráte vše. Líbil se vám newsletter? Dejte mu lajk nebo ho doporučte svým kamarádům… 

[Share Patrickův Newsletter](https://zandl.substack.com/?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _Hezký start do nového týdne přeje_

 _Patrick Zandl_

PS: Newsletter byl rozeslán na 2389 odběratelů.