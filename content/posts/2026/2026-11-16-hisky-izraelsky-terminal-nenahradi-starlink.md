---
title: 'HiSky: izraelský terminál, který má Ukrajině vykrýt výpadky Starlinku'
slug: hisky-izraelsky-terminal-nenahradi-starlink
author: Patrick Zandl
categories:
  - Ukrajina
  - Satelitní komunikace
summary_points: []
thumbnail: /assets/HiSky_ Satelitní spojení v terénu.png
audio_url: ''
hide: false
---

_Dá se poslat dron tisíc kilometrů do Ruska přes satelitní spojení s rychlostí vytáčeného modemu z devadesátek? Dá. Prý to Ukrajina dělá s terminály izraelské firmy HiSky. Starlink to nahradit nemůže, ale ve válce, kde je potřeba držet iniciativu, to určité možnosti skýtá. Pojďme je prozkoumat._ 

***

## Proč se o tom mluví právě teď

Mezi 14. a 24. říjnem 2026 Ukrajina narazila na omezení Starshieldu, vojenské verze Starlinku. Elon Musk pak napsal, že SpaceX službu na Ukrajině přiškrtil, protože ukrajinská armáda údajně porušila podmínky použití a nasazovala civilní Starlink k útočným úderům dronů. Kyjev odmítl, že by cokoliv porušil a vyjádřil značnou nespokojenost (mírně řečeno). Serhij Beskrestnov (přezdívka „Flash“), radiotechnik a poradce prezidenta Zelenského, upozornil, že drony s civilním Starlinkem mají na Ukrajině rychlostní strop 70 až 90 km/h a nad Ruskem vůbec nefungují (zdroj: [AP](https://www.adn.com/nation-world/2026/10/25/ukraine-disputes-elon-musks-claim-that-its-military-violated-starlinks-terms-of-service/)). Komerční Starlink tedy na hluboké údery použít nejde,.

Podle ISW kleslo během omezení Starshieldu procento sestřelených ruských proudových dronů ze 77 na zhruba 74 % (zdroj: [ISW přes Cybernews](https://cybernews.com/news/starshield-ukraine-drones/)). Malé číslo, ale dostatečné k tomu, aby si v Kyjevě všichni uvědomili, jak moc visí na jednom americkém dodavateli.

Do toho 6. listopadu přišly ruské vojenské kanály s tvrzením, že Ukrajina pro hluboké údery přešla na terminály izraelského výrobce HiSky (zdroj: [Militär Aktuell](https://militaeraktuell.at/en/?p=155831)). O dva dny později to rozvedl ruský web TopWar (zdroj: [Digital Today](https://www.digitaltoday.co.kr/en/view/123712/ukraine-finds-starlink-alternative-in-israel)) a z ruských Telegramů se zpráva rozběhla dál, mimo jiné přes čínsky psaný účet na X, jehož vlákno vidělo přes 78 tisíc lidí (zdroj: [X](https://x.com/AZOV2014__/status/2122204227204440144)). Podle ruských zdrojů se měl ve vraku ukrajinského dronu najít terminál SmartLITE Sirius 16×16 (zdroj: [Informat](https://informat.ro/en/international/ukraine-abandons-starlink-for-long-range-drones-147627)). Beskrestnov to podle ruského serveru Techora nepotvrdil ani nevyvrátil (zdroj: [Techora](https://techora.ru/news/ogranichenie-starlink-hisky-predlagaet-svyaz-dlya-2026-11-09)).

Tolik k důkazní situaci: nasazení HiSky na Ukrajině zatím stojí na ruských zdrojích a nikdo ho nezávisle neověřil. Technika samotná je ale dobře zdokumentovaná a o ní se dá mluvit s jistotou. Můžeme se tedy zamyslet nad tím, zda by přechod na HiSky či jiný podobný systém něco změnil. 

***

## Co je HiSky

[HiSky](https://hiskysat.com/) je izraelská firma založená v roce 2015. Za ní stojí Šachar Kravitz (dnes CEO), Jaron Šachar a Moti Litočevski, lidé z izraelské obrany, zpravodajských služeb a telekomunikací (zdroj: [Militär Aktuell](https://militaeraktuell.at/hisky-statt-starlink-ukraine-drohnen-angriffe/)). Mezi investory patří ST Engineering iDirect (singapurský výrobce satelitních modemů, v roce 2021 vložil 30 milionů USD) a SDF, investiční rameno emirátského zbrojního holdingu Tawazun (zdroj: [MWC Barcelona](https://www.mwcbarcelona.com/exhibitors/27353-hisky)). Britská dceřiná firma hiSky UK čerpala peníze z programu ARTES Evropské kosmické agentury a britské vesmírné agentury (zdroj: [hiSky](https://hiskysat.com/?p=3560)).

Firma nemá vlastní konstelaci. Provozuje virtuální satelitní síť (SVNO, analogie virtuálního mobilního operátora): pronajímá si kapacitu na cizích geostacionárních satelitech a přes ni vede vlastní protokol. Na webu se chlubí logy SES, Intelsatu nebo Hughes, ruské zdroje zmiňují Eutelsat a OneWeb (zdroj: [Digital Today](https://www.digitaltoday.co.kr/en/view/123712/ukraine-finds-starlink-alternative-in-israel)) - čili obvyklí podezřelí v oboru. Jediný vlastní satelit Ella1 byl čtyřjednotkový CubeSat postavený firmou Spire, vypuštěný v listopadu 2023 jako demonstrace přepínání mezi geostacionární a nízkou dráhou (zdroj: [hiSky](https://hiskysat.com/?p=3857), [Nanosats.eu](https://www.nanosats.eu/sat/lemur-2-ella1)). V dubnu 2025 plánovaně shořel v atmosféře.

Zajímavý je vývoj značky. Ještě před pár lety se produkt jmenoval Smartellite a prodával se na sledování vozových parků, zemědělské senzory a hlasové volání z mobilu přes satelit. Dnes se řada jmenuje SmartLITE, web mluví o „bezpečné komunikaci a řízení malých bezpilotních platforem s dlouhým doletem“ a o nasazení u „elitních obranných složek“. Vyrábět se má podle rakouského Militär Aktuell v Itálii (zdroj: [Militär Aktuell](https://militaeraktuell.at/hisky-statt-starlink-ukraine-drohnen-angriffe/)). Z IoT krabičky se během pár let stal vojenský produkt, a to bez velkých změn v hardwaru. Pojďme se spolu podívat do útrob té krabičky. 

***

## Co terminál umí

Srdcem všech terminálů je plochá elektronicky řízená fázovaná anténa (phased array, anténa složená z mřížky malých prvků, která natáčí svazek elektronicky bez pohyblivých dílů) a modem v jedné krabičce.

| Terminál | Pásmo | Anténa | Rychlost přes GEO | Rychlost přes LEO | Hmotnost / příkon |
| --- | --- | --- | --- | --- | --- |
| SmartLITE Vega 8×8 Ka | Ka (Tx 27,5–30 GHz) | 64 prvků | 7–100 kbps (špičkově) | 0,5–4 Mbps | 1,4 kg / do 55 W |
| SmartLITE Vega 8×8 Ku | Ku | 64 prvků | nízké jednotky až desítky kbps | \- | \- |
| SmartLITE Sirius 16×16 Ku | Ku | 256 prvků | až 2 Mbps (údaj z roku 2024) | desítky Mbps (plán) | rozměr cca 29 × 60 cm |

Údaje jsou z datových listů výrobce a tiskové zprávy z února 2024 (zdroj: [datový list Vega 8×8 Ka](https://hiskysat.com/wp-content/uploads/2026/03/HISKY-SmartLITE-8x8-Ka-1.pdf), [TalkSatellite](https://talksatellite.com/EMEA2621.html)). U Siria výrobce veřejně neuvádí příkon ani hmotnost. Militär Aktuell uvádí pro rodinu rozsah 7 až 2 000 kbps přes geostacionární satelity.

Pro vojenské použití jsou podstatné ještě tři další věci. Šifrování AES-256 je volitelné. Přijímač se podle datového listu zasynchronizuje se satelitem do 50 milisekund, což je důležité pro rychle se pohybující dron. A hub (pozemní řídicí uzel) i správu sítě lze provozovat na vlastním hardwaru zákazníka, takže armáda si může postavit suverénní síť, kde data nejdou přes servery výrobce. To je přesně ta vlastnost, kterou u Starlinku Ukrajina postrádá: tam vypínač drží někdo jiný.

***

## Proč malá anténa na geostacionární dráze znamená pomalé spojení

Geostacionární satelit visí 36 000 km nad rovníkem, zhruba šedesátkrát dál (pardon, výš) než Starlink. Signál slábne s druhou mocninou vzdálenosti, takže malý terminál musí s výkonem i rychlostí šetřit.

Druhý problém je méně známý a pro HiSky klíčový. Malá anténa má široký svazek. Geostacionární satelity přitom stojí na oblouku nad rovníkem dva až tři stupně od sebe, takže široký svazek osvítí i sousedy. Mezinárodní telekomunikační unie proto stanovuje přísné limity na výkon, který smí terminál vyzářit mimo osu. Klasická odpověď, popsaná v řadě patentů na terminály s malými anténami, je rozprostřené spektrum (spread spectrum): signál se rozetře do širokého pásma, takže hustota výkonu na jeden hertz klesne pod limit. Cena za to je nízká přenosová rychlost. HiSky na tom postavil celý obchodní model, jak sám píše: přenos nízkých datových rychlostí přes geostacionární satelity v pásmech Ka a Ku.

Třetí věc je zpoždění. Cesta operátor - pozemní stanice - satelit - dron a zpět telemetrie znamená přes 140 000 km. Jen za šíření signálu to dělá okolo půl sekundy na povel a odpověď, v praxi i se zpracováním spíš 0,6 až 0,8 s. Starlink má desítky milisekund.

Z toho plyne jasné omezení: přes HiSky nejde pilotovat dron s živým obrazem. To ostatně připouštějí i zdroje, které o nasazení informují. Rumunský Informat píše, že terminál umožňuje drony jen přesměrovat na cíl, nikoli je vizuálně řídit (zdroj: [Informat](https://informat.ro/en/international/ukraine-abandons-starlink-for-long-range-drones-147627)).

Stačí to? Pro dron s dlouhým doletem zřejmě ano. Moje hrubá kalkulace: telemetrie (poloha, výška, stav paliva a systémů) má stovky bajtů a posílá se jednou za pár sekund, to je řádově 1 kbps. Povel ke změně trasy nebo cíle se vejde do pár set bajtů. I nejslabší terminál s 10 kbps má rezervu. Komprimovaná fotka o 20 kB by přes 50 kbps putovala zhruba tři sekundy. Operátor tedy může v závěru letu dostat několik snímků, video ne.

***

## Neviditelný? Napůl

Čínské vlákno na X tvrdí, že nízká rychlost v kombinaci s úzkým svazkem fázované antény dělá terminál odolný proti detekci elektronického průzkumu a imunní vůči pozemnímu rušení (zdroj: [X](https://x.com/AZOV2014__/status/2122205185313472638)). První polovina má reálný základ, druhá je přehnaná.

**Detekce.** Rozprostřený signál s nízkou spektrální hustotou se ztrácí v šumu, tedy přesně to, co výzkumníci nazývají komunikace s nízkou pravděpodobností odhalení (LPD). Akademická literatura se tomu věnuje intenzivně, například [studie z letošního roku na arXivu](https://arxiv.org/abs/2601.06110) počítá, jak tvarovat svazek terminálu mířícího na geostacionární satelit, aby ho pozorovatelé na zemi nezachytili. HiSky to v marketingu prodává heslem „Private. Invisible.“ Fyzika mu tady dává za pravdu: terminál vysílá nahoru úzkým svazkem a pozemní odposlech zachytí jen postranní laloky.

**Rušení.** Tady je to složitější. Anténa fázované mřížky umí potlačit příjem ze směrů mimo svazek, NASA to [už v roce 2018 zkoumala](https://ntrs.nasa.gov/citations/20180004885) právě pro řízení dronů přes Ku a Ka pásmo. Jenže signál z geostacionárního satelitu dorazí k dronu extrémně slabý a rušička na zemi je o 36 000 km blíž.

A pak je tu geometrie: nad Volgogradem nebo Jaroslavlí vychází geostacionární satelit podle mého odhadu jen 19 až 33° nad obzorem, tedy kolem spodní hranice 30°, kterou pro Vegu 8×8 Ka uvádí datový list, a svazek antény se tak sklání k pozemním rušičkám. To by vysvětlovalo tvrzení TopWaru, že terminál reálně funguje jen nad okupovaným územím a v příhraničí, i když stejně dobře může jít o to, kam míří svazek pronajatého satelitu.

***

## Achillova pata visí nad rovníkem

Starlink má tisíce satelitů a terminál mezi nimi přeskakuje. Geostacionární satelit je jeden, nehybný a všichni vědí, kde je. Rusko to umí využít a dělá to.

Eutelsat a SES už v roce 2024 vystopovaly rušení svých satelitů do okupovaného Krymu a Kaliningradu. Osm evropských zemí si kvůli tomu letos stěžovalo u OSN (zdroj: [Kyiv Independent](https://kyivindependent.com/european-nations-urge-un-action-against-russian-satellite-sabotage-media-reports/)). Rusko mezinárodním regulátorům otevřeně sdělilo, že evropské komerční satelity pomáhající Ukrajině považuje za legitimní cíl rušení (zdroj: [Kyiv Independent](https://www.yahoo.com/news/russia-says-european-satellites-aiding-211635375.html)). A ruské „inspekční“ satelity Luč-1 a Luč-2 se podle Financial Times od roku 2023 přiblížily nejméně k sedmnácti evropským geostacionárním satelitům, pravděpodobně kvůli odposlechu (zdroj: [RAND](https://www.rand.org/pubs/commentary/2026/03/how-russia-is-intercepting-communications-from-european.html)).

Rušit transpondér geostacionárního satelitu je technicky jednodušší než rušit tisíce terminálů na dronech. Stačí dostatečně silný vysílač mířící na satelit a umlčíte všechny terminály v jeho svazku najednou. Proti tomu se dá bránit přeskakováním mezi více satelity a operátory, což HiSky jako virtuální operátor teoreticky umí. Kolik takových satelitů má pro Ukrajinu k dispozici, nevíme.

Ukrajina tedy závislost na Muskovi vymění za závislost na tom, jak dlouho evropské satelity vydrží ruské rušení. Lepší než nic, ale sázka na jistotu to není.

***

## Srovnání se Starlinkem

|  | Starlink / Starshield | HiSky SmartLITE |
| --- | --- | --- |
| Dráha | nízká (cca 550 km), tisíce satelitů | geostacionární (36 000 km), pronajatá kapacita; LEO jen v plánu |
| Rychlost | 50 až přes 250 Mbps | jednotky kbps až 2 Mbps |
| Zpoždění | desítky ms | 0,5 s a víc |
| Živé video z dronu | ano | ne |
| Kdo drží vypínač | SpaceX | provozovatel sítě, hub může mít zákazník u sebe |
| Odolnost proti rušení | vysoká, terminál přeskakuje mezi satelity | závisí na odolnosti transpondéru a geometrii |
| Detekovatelnost | běžná | nízká díky rozprostřenému spektru |
| Omezení na Ukrajině | rychlostní strop 70–90 km/h, nad Ruskem nefunguje (civilní verze) | známá nejsou |

***

## Co to znamená pro bojiště

**Hluboké údery.** Ukrajinské drony s dlouhým doletem letí stovky kilometrů po předem naprogramované trase. Satelitní spojení u nich slouží k tomu, aby operátor věděl, kde dron je, a mohl změnit cíl, když se situace změní. Na to HiSky stačí a rychlostní strop, který brání použití civilního Starlinku, tu neplatí. Pokud ruské zprávy sedí, Ukrajina tím získala kanál, který jí nikdo v Kalifornii nevypne.

**Údery ve vlnách.** Zajímavější než slibovaná přesnost je taktika, kterou popisuje ruský milblogerský kanál Dněvnik Razvědčika. Podle něj Ukrajina posílá drony ve vlnách a ty další přesměrovává za letu podle toho, jak dopadly první. Když první dvojice zasáhne, roj za ní míří na nádrže, krakovací jednotky nebo rozvodny. Kde drony mizí předčasně, tam zjevně stojí protivzdušná obrana, a zbytek ji obletí. Na tohle nepotřebujete video, stačí telemetrie. Dron, který přestane vysílat přesně nad cílem, nejspíš zasáhl. Dron, který zmizí o třicet kilometrů dřív, narazil na obranu. Pár kilobitů za sekundu a půlsekundové zpoždění tu nevadí. Technicky je to představitelné, ale doložit to samozřejmě nemůžeme.

Samotný kanál je anonymní, prodává reklamu a o sobě píše, že zveřejňuje „subjektivní myšlenky“. Vedle HiSky tam najdete i tvrzení, že incident s drony v Lipsku zorganizovaly samy německé tajné služby (zdroj: [TGStat](https://tgstat.ru/channel/4IxhJe5NIcI1OGVi)). Zbytek příspěvku odpovídá: zázračná izraelská technologie od „bývalých šéfů Mossadu“, kterou „naše prostředky elektronického boje nepotlačí“, a Trump, který „ztratil kontrolu nad ukrajinskými údery“. Pro ruské publikum je to pohodlnější vysvětlení, než přiznat přetíženou protivzdušnou obranu. Kanál navíc tvrdí, že terminál nad Ruskem nemá žádná geografická omezení. Ruský TopWar o týden dřív psal pravý opak.

**Údery na rafinerie.** Ověřit se dají jen samotné útoky. Od 30. října do 7. listopadu Ukrajina zasáhla sedm rafinerií za devět dní: Novokujbyševsk, Ufu, Kstovo, Jaroslavl, Rjazaň, Afipskij a Saratov (zdroj: [Militär Aktuell](https://militaeraktuell.at/en/?p=155831)). Předtím téměř dva týdny žádný útok na rafinerii hlášen nebyl (zdroj: [Kyiv Post](https://www.kyivpost.com/post/88981)). Časově to sedí s obdobím po sporu o Starlink, a právě na tom ruské kanály staví. Časová shoda ale nic nedokazuje.

Ruské i čínské zdroje tvrdí, že díky HiSky drony zasahují přesněji a rafinerie hoří „na desítkách míst najednou“. Ověřené záběry ukazují skromnější obraz. V Kstovu monitorovací kanály odhadovaly požár na dvou destilačních jednotkách a visbreakeru (zdroj: [Euromaidan Press](https://euromaidanpress.com/?p=430778)), v Jaroslavli geolokace našla dvě ohniska (zdroj: [Kurs.com.ua](https://kurs.com.ua/en/novost/1476198-droni-nanesli-udar-po-odnomu-iz-krupneishih-npz-v-rossii-genshtab-podtverdil-porazhenie)). Hlavně ale Moskva u jaroslavlského útoku hlásila 124 dronů (zdroj: [United24](https://united24media.com/war-in-ukraine/ukraine-hits-giant-russian-refinery-again-moscow-claims-124-drones-joined-the-raid-24028)), nejvíc v jednom náletu na tuto rafinerii za celý rok. Víc zásahů nejjednodušeji vysvětlí víc dronů v jedné vlně. Přesnost navíc dělá navedení v posledních kilometrech, tedy inerciální navigace, satelitní navigace odolná proti rušení, rozpoznávání cíle kamerou na palubě. Do toho se spojení o desítkách kbps s půlsekundovým zpožděním přímo neprojeví.

**Stíhání Šáhedů.** Pod čínským vláknem se kdosi ptá, jestli by izraelské terminály pomohly záchytným dronům proti ruským proudovým Šáhedům, které létají přes 400 km/h. Nepomohly. Interceptor řízený operátorem potřebuje živý obraz a minimální zpoždění, tedy přesně to, co geostacionární spojení nedá. Tady Ukrajina na Starshieldu visí dál, což ukázal i pokles úspěšnosti během říjnových omezení.

**FPV a frontová linie.** Beze změny. Krátký dosah řeší rádio, optické vlákno a Starlink na zemi.

**Diverzifikace.** Ukrajina vyvíjí s partnery i vlastní geostacionární terminál UASAT GEO (zdroj: [Supercluster](https://www.supercluster.com/editorial/the-race-to-find-starlink-alternatives-to-control-battlefield-drones)). HiSky tak zapadá do širší snahy rozložit satelitní spojení mezi více dodavatelů. Z bezpečnostního hlediska je to rozumné bez ohledu na to, jak skončí spory s Muskem.

**Rusko jde stejnou cestou.** Ironií je, že Rusové po odstřižení od Starlinku udělali totéž. Od jara na frontu hromadně dodávají terminály Spirit-030, které pracují se speciálním geostacionárním satelitem a vystačí si s anténou o průměru 30 centimetrů místo dřívějších devadesáti. První kus zničili v dubnu piloti 414. brigády bezpilotních systémů „Madyarovi ptáci“ a Beskrestnov od té doby vyzývá ukrajinské operátory, ať si těchto antén všímají (zdroj: [Razom](https://razomua.media/en/news/politika/antena-30-sm-zamist-90-rosiya-masovo-veze-na-front-novyy-suputnykovyy-terminal-pislya-vtraty-starlink)). Obě strany tedy přesouvají část provozu na geostacionární dráhu. Pomalejší, snáz rušitelnou, zato pod vlastní kontrolou.

***

## Co si z toho odnést

HiSky je technicky solidní, ale skromná věc: krabička původně navržená pro posílání dat z traktorů a kamionů, která se ukázala jako vhodná pro dron, jemuž stačí občas říct „leť jinam“. Řekl bych, že to je přesně ten typ zlepšování, který se v takovéhle válce uplatňuje. Nikdo nečeká zázraky, ale funguje to s dostupnou kapacitou a bez rozmarů jednoho miliardáře.

Starlink to nenahradí. Na živé video, záchytné drony a cokoli rychlého nemá kapacitu ani zpoždění, a geostacionární satelity jsou pro ruské rušičky snadný terč. Ověřit lze dnes jen to, že Ukrajina v posledních týdnech zasahuje ruské rafinerie v nebývalém tempu. Že za tím stojí izraelské terminály, je hypotéza ruských Telegramů, kterou dál šíří čínské účty a anonymní kanály s „vysoce postavenými zdroji“. Technicky dává smysl, hlavně pro řízení vln dronů podle telemetrie. Než ji někdo potvrdí z ukrajinské strany nebo z ohledaných vraků, berme ji s rezervou.

A jedna poznámka na okraj: Technický popis stojí na datových listech, podáních u americké FCC, patentech a obecné literatuře o malých satelitních terminálech. To u firem, které prodávají armádám, není nic neobvyklého, více zdrojů není. 

***

_Stav k 16. listopadu 2026. Informace o nasazení HiSky na Ukrajině pocházejí z ruských zdrojů a nebyly nezávisle ověřeny. Výpočty elevace jsou autorův odhad pro ilustraci._
