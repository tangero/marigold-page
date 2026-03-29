---
slug: 'nadeje-roku-procesory-risc-v'

author: Patrick Zandl
categories:
- Patrickův newsletter
- Apple
- Google
- Microsoft
- AI
- Internet
- Startupy
- IoT
- Česko
- Automotive
date: '2023-02-12'
original_newsletter: "Patrickův newsletter #63 \U0001F916 Naděje roku: procesory RISC-V
  a hromada AI novinek"
summary_points:
- AI potřebuje procesory, kde dominuje ARM, ale RISC-V představuje otevřenou alternativu.
- RISC-V je otevřená architektura ISA, umožňující přizpůsobení a sdílení návrhů procesorů.
- RISC-V nachází uplatnění v IoT a průmyslu, kde se snižuje závislost na operačních
  systémech.
- Kniha Stevena Pinkera "Lepší andělé naší povahy" zkoumá důvody poklesu násilí ve
  společnosti.
title: \U0001F9D1‍\U0001F4BBNaděje roku -  procesory RISC-V
---

V minulém vydání jsme si řekli, že technologií roku 2023 bude umělá inteligence, AI. A pokud jste četli moji knihu Mýty a naděje, tak jste jistě postřehli, že za klíčovou technologii pro AI a svět obecně považuji i procesory. AI se bez procesorů neobejde, jenže svět je nyní tak zvláštně rozdělen. Velkým vládcem procesorového světa je rodina ARM. Může se to nějak změnit? Může něco převzít roli ARM procesorů podobně, jako to tyto procesory udělaly Intelu? Nebojte se, pokusím se o tom napsat pár informací, které vás zaujmou i v případě, že jsou vám procesory šumák. Protože to bude business, vliv a politika. 

Několik mandatorních informací. Co jsou to procesory RISC-V? Jsou to procesory založené na otevřené architektuře instrukční sady (ISA). Vznikly v roce 2010 na kalifornské univerzitě v Berkeley, dnes ji kontroluje mezinárodní sdružení RISC-V International, v jejíž prospěch se původní autoři vzdali všech práv. Sdružení dnes řídí jeho členové a základní myšlenkou i hnacím motorem je "komunismus" - tedy sdílení architektury. A to i přes to, že si můžete koupit komerčně licencovaná jádra procesorů RISC-V. Paradox? Kdeže. 

Procesory RISC-V jsou otevřenou alternativou k procesorům ARM. Otevřená architektura instrukční sady (ISA) znamená základ, tedy společné návrhy jednotlivých důležitých částí procesorů, které ovšem nevytvářejí dostatečné možnosti obchodního odlišení. Návrh a údržba těchto částí vyžaduje spoustu času a to je důvod, proč si firmy navrhující procesory volí jednu z existujících platforem, dnes nejčastěji ARM - mají k dispozici technický podvozek a také jistotu široké softwarové podpory, na to si nalepí to svoje, čím prodává: vzhled, chování, výkon a samozřejmě logo ...🙂 Právě otevřenost RISC-V znamená možnost si všechno snadno přizpůsobit, využít existujících základů a pohybovat se v rozsáhlém ekosystému. Zjednodušeně řečeno lze RISC-V považovat za Linux světa procesorů. 

Existuje nějaká šance, že by do světa procesorů na místo ARM pronikla další rodina procesorů? No, je to velmi obtížné a zdlouhavé; stejně jako jsme řekli v roce 1995 o platformě Wintel – bylo to nemyslitelné.

RISC-V má především jednu podstatnou nevýhodu, která u ARMu nepřichází v úvahu a která je podstatou jeho otevřenosti. Jednotlivé procesory RISC-V totiž mezi sebou nemusí být vzájemně kompatibilní, neboť návrháři mohou změnit vlastně všechno. Proto se sdružení RISC-V International rozhodlo ratifikovat a zmrazit ISA na minimu, které musí všechny procesory označené RISC-V splnit. Ve skutečnosti ale neexistuje žádný donucovací mechanismus, který by rozdílným implementacím ISA bránil. Ano, přední návrháři procesorů RISC-V jako jsou Andes, SiFive nebo CodaSIP ratifikované ISA dodržují, jenže s větším či menším důrazem na detaily, které pálí zrovna je. Ve výsledku zdaleka ne všechen kód bude mezi jednotlivými procesory různých výrobců přenositelný bez úprav. A kdo ty úpravy bude dělat? 

Ještě před pár lety by to byla stopka. Kdopak by asi donutil Microsoft, aby překompiloval svá Windows na nové modely RISC-V? Nikdo! Jenže už ho taky nikdo nenutí. Velká část reálně běžícího software je více závislá na cloudech a internetu, pokud si s nimi procesor poradí, má vyhráno. To také znamená, že význam operačního systému se radikálně snížil, vlastně stačí portovat nějaké vhodné Linuxové distribuce či dokonce embedded systémy podporující napojení na internet a je vyhráno. Však také řada RISC-V procesorů se používá v Internetu věcí (IoT) či průmyslu pro nejrůznější sběry dat - a tam Windows na nic opravdu nepotřebujete. 

Je sice pravda, že se objevilo několik návrhů operačního systému Internetu věcí, ale jejich využitelnost byla malá. Šlo o (z pohledu IoT) těžkotonážní systémy, které toho podporovaly zbytečně moc. Zatímco senzorům sluší jen odesílání dat třeba přes MQTT, hraničním zařízení zase potřebují příjem a lehké zpracování dat, než je posunou směrem do centra či spíše do cloudu. Přizpůsobení jednoúčelových systémů se zde bere jako samozřejmost. 

Tady je silná parketa RISC-V procesorů. Jsou efektivní, variabilní a především mají nyní lepší tah na branku i obchodně. ARM totiž silně škobrtnul: v hýčkající náruči Softbanku ztratil motivaci získávat nové klienty, neboť jeho licenční politika nové klinty znevýhodňovala. A pro některé staré klienty se v době uvažované akvizice společností Nvidia stal neatraktivním, ba potenciálním konkurentem. A tak se po dlouhé době začaly objevovat vážně míněné procesorové startupy založené právě na RISC-V a směřované především do světa Internetu věcí, průmyslu a zpracování dat. Tam se dalo čekat, že zákazníci sáhnou raději po nezávislé platformě, než po majetku Nvidia, která ve zpracování dat konkuruje kdekomu. A fakt, že o nyní, o skoro dva roky později je transakce pro nesouhlas regulátorů odpískána, na tom již mnoho nezmění. Škoda byla nadělána. A bokem si ponechme situaci v Číně. Ta se snaží zaujmout vedoucí roli na poli procesorů, přičemž nadělat potíže ARMu a mít vlastní platformu, na kterou mají vliv, by se Číně hodilo. Jenže to vůbec nemusí být RISC-V, ozývají se hlasy, že Čína vytváří vlastní ISA, jakkoliv těžké to je. Právě pro účely automotive, sběru dat a IoT. 

Považuji za nepravděpodobné, že by velké procesorové společnosti jako třeba Qualcomm nebo Marvell hromadně přecházely od ARMu k RISC-V. Už jen portace vývojových a testovacích nástrojů by byla nesmírně nákladná a dlouhotrvající. Je ale jisté, že i tyto firmy budou vytvářet rodiny RISC-V procesorů ve své nabídce jak pro vedlejší projekty, tak pro zákazníky, kteří si budou přát vyhnout se ARMu. 

Na trhu se toho s RISC-V děje hodně. Koncem loňského roku se potvrdilo, že Google má Android portovaný na RISC-V a také Apple začal tuto architekturu používat pro některé doplňkové funkce. Koncem roku 2022 bylo prodáno více jak deset miliard procesorových jader RISC-V, což není málo (ale taky to není moc). 

Existují také vážně míněné pokusy dostat RISC-V procesory do datacenter a udělat z nich moderní serverové procesory. To je ještě jiná liga, než vytvořit procesor posouvající nasbíraná data někam do cloudu. Zatím nejvážnějšími uchazeči jsou společnosti Ventana Micro Systems, Tenstorrent, Rivos a Akeana. Nejsou to ořezávátka, i když jejich jména asi znát nebudete, pokud nejste fajnšmekři: ale například Ventana má za sebou návrh prvního 64bitové jádro ARM. Ventana Veyron VT1 je ve vysokých konfiguracích zcela srovnatelná například s AMD Genoa a poráží Intel Ice Lake i Sapphire Rapids. Něco z toho se dá už i objednávat pro domácí experimenty, jako jsou desky [HiFive Unmatched](https://www.sifive.com/boards/hifive-unmatched), ale tyhle desky jsou založené na levných verzích RISC-V procesorů. 

Vývoj na poli procesorů bude nesmírně zajímavé sledovat. Mimochodem, společnost Codasip má kořeny (a vývojové centrum) v Česku a jeho šéf Karel Masařík je také členem technického řídícího výrobu organizace RISC-V International ([článek v E15](https://www.e15.cz/byznys/technologie-a-media/brnensti-vyvojari-cipu-tezi-z-boju-usa-a-ciny-dodavaji-intelu-i-vyrobci-kamer-1385611)). 

### 📒Kniha měsíce? Steven Pinker: The Better Angels of Our Nature

Pro mě je to objev měsíce, i když je to kniha stará deset let. Napsal ji kanadský experimentální psycholog a kognitivní vědec Steven Pinker, jmenuje se [Lepší andělé naší povahy: Proč násilí klesá](https://en.wikipedia.org/wiki/The_Better_Angels_of_Our_Nature). A vypráví přesně o tom, o čem je název - o důvodech a příčinách, proč násilí ve společnosti dlouhodobě klesá. Bohužel zatím nevyšla česky, i když ji zřejmě chystá vydat Academia. Pinker tvrdí, že násilí, včetně kmenových válek, vražd, krutých trestů, týrání dětí, krutosti vůči zvířatům, domácího násilí, lynčování, pogromů a mezinárodních a občanských válek, se v různých časových měřítcích a v různém rozsahu snížilo. Pinker považuje za nepravděpodobné, že by se změnila lidská povaha. Podle něj je pravděpodobnější, že lidská přirozenost zahrnuje sklony k násilí a také protitendence, které jim čelí, "lepší anděly naší přirozenosti". Samozřejmě dostal od mnohých naloženo. Archeolog David Wengrow shrnul Pinkerův přístup k archeologické vědě jako "moderního psychologa, který si vymýšlí za pochodu"... V každém případě za přečtení to stojí. V češtině vyšla Pinkerova navazující kniha [Osvícenství tady a teď](https://www.academia.cz/osvicenstvi-tady-a-ted-obhajoba-rozumu-vedy-humanismu-a-pokroku--pinker-steven--academia--2022). Jenže Academia ani v roce 2022 není schopna vydat ji v elektronické podobě. Hamba jim😞

Nakonec jsem si koupil anglické verze a nechal si je přeložit Deeplem ...