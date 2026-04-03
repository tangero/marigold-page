---
slug: 'blackout-cesko'

audio_url: null
author: Patrick Zandl
categories:
- Energie
- Energetika
- ČEPS
thumbnail: https://www.marigold.cz/assets/spojka-energetika.jpg
title: "Aktualizace 16.7.: ⚡️⚫️ Jaké je skutečné pozadí blackoutu v Česku?"
---

ČEZ se včera (15.7.2025) vyjádřil k tomu, proč se 4.7.2025 odpojila hnědouhelná elektrárna Ledvice, což byl jeden z hlavních důvodů, proč v části Česka nešla elektřina. Podle mluvčího ČEZu v kritickou chvíli došlo ke skokovým požadavkům, kdy kotel měl přejít v krátkém sledu z 350 MW na nulu a pak rychle zpět na 150 MW, čímž se dostal mimo technická minima a ochrana kotle jej odstavila. Ledvice se podle mluvčího Kříže staly "obětí situace", když jako největší výrobce v oblasti reagovaly na prudké výkyvy parametrů sítě po přerušení vodiče. Certifikovaný rozsah šestého bloku je přechod z 600 MW na 60 MW, ne do nuly s opakovaným rychlým startem. Menší fluidní blok 4 pokračoval v regulaci v ostrovním režimu až do cca 11:59, kdy další událost v síti způsobila jeho vypnutí. ČEZ tím dokládá, že Ledvice jako celek nebyly „zdrojem“ kaskády, ale reagovaly na síťové jevy. Po výpadku byl ledvický výkon (částečně) nahrazen plynovou výrobou ČEZ v Počeradech, aby se stabilizovala lokální bilance. ([iRozhlas](https://www.irozhlas.cz/ekonomika/cesky-blackout-vysetruje-expertni-panel-evropskych-provozovatelu-siti-zprava-ma_2507150600_jaf))

Tvrzení ČEZu ovšem zatím stále není podpořeno publikovanými daty. Pro vyšetřování jsou zásadní data z DCS, distribučního řídícího systému, který řídí a dohlíží na veškeré technologické uzly elektrárny (Ledvice myslím používají Siemens SPPA-T3000). V tom není potřeba hledat nic divného, data DCS bude analyzovat expertní panel a pravděpodobně se ani nikdy nepublikují, protože jejich analýza a interpretace je složitá. V každém případě bez toho, že by se nezávislí experti podívali na to, jak skutečně došlo k odstavení Ledvic, nelze brát vyjádření ČEZu za úplně směrodatné. Nastavení ochran je komplexní záležitost a zatím to stále vypadá tak, že komunikace mezi Ledvicemi a dispečinkem nefungovala optimálně a je otázkou, kde ležela prvotní příčina. Teprve díky datům z DCS se dá přijít na to, zda to byly Ledvice, kdo reagoval na zmatek v síti, zda chyba nebyla v dispečinku přenosové sítě nebo zda nereagovaly ochrany Ledvic příliš "ostře". 

ČEPS vyloučil nadlimitní přetížení před poruchou i vliv přeshraničních „německých“ přetoků. Dovozy z Německa byly mírně nad plánem, ale v běžném rozmezí. Soustava s takovými hodnotami standardně pracuje. Tvrzení Andreje Babiše, že příčinou byly přetoky, je tedy nesmyslné. 

V tuto chvíli panuje odborný konsensus (tj. názor lidí, co tomu rozumí): souběh několika technických poruch, nikoli jediný spouštěč. Pád vodiče V411 sám o sobě by soustavu neposlal mimo bezpečné hranice, pokud by nedošlo k téměř souběžnému výpadku Ledvice B6, následnému přetížení (a vypnutí) V208 a poruše ve větvi V401 / Krasíkov. Nyní se řeší přesné pořadí výpadků a to, jak tomu příště zabránit. 

---

**Aktualizace 10.7.2025:** ČEPS měl tiskovou konferenci k výpadku. Upřesnila se časová osa, aktualizuji tu moji zde. Druhá důležitá informace: na Lince V411 byla už jedna závada vloni v listopadu. Tehdejší havárie byla opravena externí firmou (1.–3. 12. 2024). Kus lana testoval Kloknerův ústav ČVUT – parametry „vyhovující“. To znamená, že vodiče byly v pořádku, nebyly poškozeny žádným způsobem přetěžování. To jde proti verzi "můžou za to přetoky", ČEPS dnes vyloučil nadlimitní proud. Ochrany ani DTR nehlásily alarmy. Zajímavé ale je, že lano se poškodilo ve stejném úseku. V každém případě běží termovizní kontroly. Předběžná zpráva vyšetřovacího týmu výpadku (ČEPS + ERÚ + VUT Brno) má být zveřejněna do konce července 2025. Nejsou žádné indicie o tom, že by šlo o sabotáž či zásah třetí osoby. Na co se čeká? Detailní log ochrany bloku Ledvic B6 – ČEZ má dodat do půlky července. ČEPS dnes potvrdil, že bez paralelního odpojení Ledvic by se soustava nerozpadla. Primární příčina bude tedy někde v reakci ochrany Ledvic na situaci v síti, bude se zkoumat, zda situace odůvodnila reakci ochrany Ledvic. 

Následují informace publikované 9.7.

---

Dalo by se říct, že to mohlo být téměř nezaznamenané škobrtnutí přenosové sítě, kdyby spolu se severovýchodem Čech nevypadl 4.7.2025 i kus Prahy. Toho už si všechna média všimla. Co se ve skutečnosti stalo, jak špatná je situace a jak hysterická je u nás debata o energetice?

> 🇪🇸 Problematikou [blackoutu ve Španělsku jsem se podrobně zabýval zde](/item/spanelsko-blackout-kdo-za-to-muze/).

### Časová osa českého blackoutu 4.7.2025 (aktualizace 10.7.)

1.  **11:51:06** – na stožáru č. 35 u Kličína na přenosové trase V411 padá jeden vodič troj-svazku; odpojovací relé vypíná vedení. Přesný důvod pádu je předmětem vyšetřování, oficiálně bylo ale oznámeno, že šlo o mechanické poškození. Jak k němu došlo, se šetří. K tomu se ještě vrátíme
    
2.  **11:52:48** – náhlé přerozdělení výkonu zatěžuje V430, V412 a 220 kV vazby; napěťový pokles o cca 4 % v severní části. Ochrany bloku číslo 6 elektrárny Ledvice (660 MW) během zlomku sekundy odpojují tento blok od přenosové sítě. Výkon v oblasti klesá. ČEPS 10.7. uvedl, že došlo ke ztrátě cca 300 MW; původně se uvádělo 660 MW, což je nominální výkon Ledvic. Proč to bylo méně, není jasné.
 
        
3.  **11:59:44** – dispečer vypíná V208 (přetížení) a současně o tři sekundy později vypadává linka V401 a rozvodna Krasíkov.

    
4.  **12:00 – 12:05** – vznik dvou ostrovů, bez napětí 9 rozvoden (Malešice, Chodov, Bezděčín, Týnec, Čechy Střed, Opočínek, Neznášov, Výškov, Chotějovice). Je tak oficiálně potvrzen počet devíti vypadlých rozvoden. 

5. **12:24** - opětovné zapnutí trasy V208, řízený rozjezd
    
6.  **cca 14:00** - dodávka do Prahy a hlavních uzlů zprovozněna (oživeníelektřiny pro koncové zákazníky záleží na distribučních společnostech)
    
7.  **14:50** – znovuspojení ostrovů na 400 kV, obnoveno všech devět rozvoden.
    
8.  **22:15** – provizorně opravena V411; vedení v polovičním výkonu.
    
 _**Poznámka k časové ose:** jde o oficiální časovou osu, moje dřívější rekonstrukce časové osy z doby před publikováním oficiální časové osy je v archivu na Githubu._   

Jde o vcelku "banální situaci", která se do značné míry očekávala. Přenosová trasa V411 pochází z šedesátých let, prošla částečnou rekonstrukcí v polovině devadesátých let, jenže přenosová trasa nebyla zdvojena, což neodpovídá významu této trasy.

![Obrázek padlého lana na stožáru u Kličína](https://www.marigold.cz/assets/v411-stozary.png)

_Obrázek padlého lana na stožáru u Kličína tak, jak jej zaznamenala Česká televize [ve své reportáži](https://www.ceskatelevize.cz/porady/1097181328-udalosti/225411000100705/cast/1126176/)._

Již deset let je na to upozorňováno a trase je označována za rizikovou, její rekonstrukce ale byla stále odsouvána. Ačkoliv projekt „[V411/811 zdvojení](https://portal.cenia.cz/eiasea/download/RUlBX09WNDE1MV9kb2t1bWVudGFjZURPQ18xMDk5NjIzMTkzOTgzMDUwMTIxLnBkZg/OV4151_dokumentace.pdf)“ byl pořízen již v roce 2016, EIA získal v roce 2019, [společné povolení](https://mpo.gov.cz/assets/cz/rozcestnik/uredni-deska/stavebni-urad/2022/11/MPO-638242_21_433-_-SU-Verejna-vyhlaska---spolecne-povoleni.pdf) pak 2022, kdy současně schvaluje umístění stavby v území (funkce územního rozhodnutí) a provedení stavby (funkce stavebního povolení). Podle MPO se začal výběr zhotovitele soutěžit shodou okolností v květnu 2025. To by znamenalo dokončení v roce **2027**.

**Proč je V411 tak významná?**

Linka totiž propojuje rozvodnu [Výškov u Loun](https://cs.wikipedia.org/wiki/Rozvodna_V%C3%BD%C5%A1kov) a [rozvodnu Hradec](https://cs.wikipedia.org/wiki/Rozvodna_Hradec_u_Kadan%C4%9B) (neplést s Hradcem Králové!).

[Rozvodna Hradec u Kadaně](https://allforpower.cz/rozvody-energii/sedesat-let-transformovny-hradec-u-kadane-538) má v české energetické soustavě velmi důležitou roli. Kromě severní linky do Německa (2x400kV linka do německého Röhrsdorfu) je na ni totiž napojena elektrárna Tušimice i Prunéřov a další přenosové linky dále do Česka. Rozvodna je také vybavena transformátory PST, které mohou zabraňovat přetokům do české přenosové sítě z Německa.

![Na mapě vidíte rozvodnu Hradec a Výškov včetně jednoduchého propojení 411.](https://www.marigold.cz/assets/rozvodny-hradec-vyskov.jpg)

_Na mapě vidíte rozvodnu Hradec a Výškov včetně jednoduchého propojení 411. Celá [mapa přenosové sítě k dispozici zde](https://www.ote-cr.cz/cs/statistika/elektrizacni-soustava-cr.png)_

Proč říkám, že příběh je vcelku banální? Pád starého vodiče na V411 spustil řetězec dalších, samostatných ochranných zásahů (Ledvice, V208, Krasíkov), které v souhrnu odpojily devět rozvoden a až 2,7 GW zátěže. Výpadek rozvodny Krasíkov oddělil od české přenosové soustavy ostrov severní části Čech, který následně zkolaboval. Zbytek sítě se náhle z nedostatku výkonu (výpadek cca 500 MW) dostal do velkého přebytku (cca 1500 MW) a hrozil blackout. **Jen díky přeshraničním spojením se podařilo tento přebytečný výkon vyvézt pryč a zabránit tak celkovému kolapsu sítě.** A jen díky tomu se podařilo během necelé hodiny připojit většinu vypadlého území zpět.

Nejpravděpodobnější prapříčinou provotníhá pádu vodiče na lince V411 je **mechanická vada svorky/vodiče**, případně urychlená letitým zatížením. Co z toho přesně, se vyšetřuje.

![Mapa postižené části sítě](/assets/147345_mapa-postizene-casti-ps.jpg)

### 🇩🇪 Mohou za to přetoky z Německa? Ne, spíše spojka!

Bezprostředně po oznámení havárie se po internetu rozběhly spekulace. S první se vytasil lobbistický podcast Vysoké napětí, který na X.com bez čehokoliv dalšího publikoval data o přetocích energie do Česka, čímž neodůvodněně podnítil hysterické reakce směřované na "německé přetoky".

Jaká je skutečnost? Přenosy a přetoky energií DE-CZ jsou dlouholetým aranžmá evropské energetiky. Česku propojovací linky umožňují export elektřiny do Německa, kde ji prodáváme, Německu opačně prodej elektřiny do Česka na sjednoceném energetickém trhu. Přetokem se ale nerozumí prodej, nýbrž fakt, že elektřina, která se spotřebovává jinde v Německu (či Rakousku) se přenáší přes českou přenosovou síť. I za to se ovšem platí, jde o mechanismus [Inter-TSO Compensation](https://www.acer.europa.eu/electricity/infrastructure/inter-tso-compensation-monitoring). Ten kompenzuje provozovatelům přenosových sítí ztráty a opotřebení sítě způsobené **všemi** přeshraničními toky, tedy i neplánovanými smyčkami (přetoky). ČEPS je čistý příjemce, podle výročních zpráv jde v posledních letech o částky 300-500 mil Kč. Existují i další mechanismy, které více či méně přímo hradí náklady na přetoky včetně dotace EU na PST v Hradci, umožňující přetoky limitovat.

Ve skutečnosti propojení Česka s jinými státy zachránilo v pátek Česko od rozsáhlejšího výpadku, pravděpodobně i od totálního blackoutu. [Ředitel ČEPS potvrdil](https://archiv.hn.cz/c1-67759460-cesku-pri-vypadku-elektriny-pomohl-picasso-a-nemecko-hrozila-ztrata-vsech-rozvoden-a-totalni-blackout), že náhlou nadvýrobu v některých částech sítě vyřešil okamžitý export elektřiny do okolních států.

Ačkoliv tedy přetoky z Německa byly nominálně vysoké, ČEPS je nepochybně vyhodnotil jako v pořádku - v opačném případě by je limitoval ([jak plyne z četných vyjádření](https://archiv.hn.cz/c1-67758510-kdyby-hrozilo-pretizeni-z-nemecka-ceps-to-zastavi-rika-o-vypadku-sedlak-ze-svazu-moderni-energetiky)). Stejně tak tvrzení, že přetoky "spálily linku" nejsou realistické. Jako každá linka i V411 má svou ochranu, která by ji měla odpojit, než by k něčemu takovému došlo. A je sice pravda, že hliník trpí na žíhání, které snižuje jeho odolnost namáhání, už při poměrně nízkých teplotách (100-150 °C), ale z toho důvodu má lano vodiče ACSR Bison ocelové pozinkované jádro v poměru počtu drátů 4:1, tedy na 54. hliníkových pramenů je 7 drátů pozinkované oceli v jádru. Ocel má více jak desetinásobnou pevnost v tahu oproti hliníku, to je také důvod, proč je v jádru lana. U vodičů ACSR je **vysoce nepravděpodobné, že by došlo k poškození samotným dlouhodobým přetížením linky, které by způsobilo její "utavení"** – proudové ochrany i dispečer odstaví linku dávno předtím, než by teplota jádra překročila kritickou hranici. Ta se u oceli pohybuje nad 350 °C. Samotné ocelové jádro udrží celý svazek i v případě, že hliníková lana jsou poškozená.

K čemu dojít může, je souhra dlouhodobých poškození, kdy dojde k částečnému zažíhání hliníku, poškození zinkové vrstvy a třeba proniknutí soli do lanového svazku, ale to jsou extrémní případy - například v českých podmínkách pronikání soli nehrozí. Co je spíše myslitelné, je pád spojky. Ve „vodičové“ terminologii je **spojka** trubková, dvoudílná lisovaná objímka, která v poli **pevně, elektricky a mechanicky** spojí dva konce ACSR lana. Po desítkách let ji mohou ohrozit chybná montáž, koroze jádra nebo únava, a právě její selhání patří k nejčastějším příčinám pádů vodičů na velmi vysokém napětí. ČEPS proto nyní **reviduje všechny lisované spojky** na 400 kV trasách z 60.–80. let a měří je termovizí a magnetickou sondou.

![Takhle vypadá spojkování kabelů lisovanou kompresní spojkou, která umožní navázat dva bubny lana. Důležité je správne slisování](https://www.marigold.cz/assets/spojka-energetika.jpg)

_Takhle vypadá spojkování kabelů lisovanou kompresní spojkou, která umožní navázat dva bubny lana. Důležité je správne slisování._

Důvody, proč server Vysoké napětí obvinil ČEPS ze zanedbání povinností správce přenosové soustavy, nejsou jasné, žádné důkazy pro to neměl a spíše půjde o nějaké zákulisní půtky.

### 🤷‍♂️ Jak je možné, že k takové sérii incidentů došlo?

Zajímavé není ani tak to, proč se přetrhl jeden kabel - to se stává a pokud nejde o systémové pochybení, musí se s tím počítat. Proto se také energetické systémy plánují jako N-1 - tedy tak, aby ztráta jednoho významného prvku nespustila kaskádu. Jenže to je právě to, co se v tomto případě zřejmě stalo. Po pádu lana odpojila ochrana šestý blok Ledvic a tím ze sítě vyřadila 660 MW. Jen pro pořádek: Ledvice patří ČEZu a mají dva funkční hnědouhelné bloky, 4 blok 110 MW a právě šestý nejmodernější blok zprovozněný v roce 2017. Proč jej ochrana odpojila, má ČEZ zjistit do poloviny července. Stát se to nemělo a značně to zkomplikovalo situaci - v rychlém sledu totiž vypadly dvě další přenosové trasy. Čtyři závažné závady ve dvou minutách, to už normální není. S napětím čekáme na to, jak to objasní zprávy ČEZ a ČEPS!

Právě proto je důležité, aby došlo k prošetření a co nejširšímu vyhodnocení závad. V případě, že linku V411 skutečně poškodily okamžité vysoké přetoky z Německa, by šla celá věc za ČEPSem, který o míře přetoků rozhoduje a který by tedy také špatně vyhodnotil potřebu rekonstrukce linky V411 nebo měl špatně nastavené ochrany. To se ale dnes ale nezdá pravděpodobné a ČEPS to vylučuje, ačkoliv jej z toho lobby média obvinila. Pravděpodobnější je vadná či unavená kabelová spojka, jejíž kondici nadměrné zatížení neprospělo, ale toto nebylo jedinou příčinou. Navíc pád jednoho kabelu neměl způsobit tak rozsáhlý výpadek, takže bude potřeba důsledně vyšetřit a rozhodnout, co s tím.

### 😩 Česká energetická debata v režimu hysterie

Česká energetická debata je dlouhodobě hysterická vůči změnám, ke kterým na energetickém trhu dochází. Do jisté míry nikoliv bezdůvodně: kdysi to nějak fungovalo a je škoda, že to takhle už dlouhodobě fungovat nebude a musíme to měnit. Jenže změna je neoddiskutovatelná a nedá se jí vyhnout, uhlí prostě došlo, jádro má své problémy, kvůli kterému není univerzálním řešením a OZE se staly součástí energetického mixu. Hysterii v Česku podněcují lobbystická média jako zmíněné Vysoké napětí, jehož redakce kdysi přímo patřila pod Daniela Křetínského, majitele Energetického a průmyslového holdingu (=hnědouhelných dolů a elektráren) a jehož názory nadále zastává a hájí. To byl pravděpodobně také důvod, proč se dotyčné médium snažilo pozornost svést na obnovitelné zdroje a Německo, místo toho, aby si všímalo problémů, jaké nadělalo okamžité odpojení hnědouhelného bloku.

Hloupé je, že v tomto hysterickém režimu prakticky nejde najít žádnou shodu. Veškerá rozhodnutí se dělají silově, s ohledem na jednostranný užitek. Role obnovitelných zdrojů v energetické infrastruktuře je démonizována, není zohledňován fakt, že mohou mít svou stabilizační roli, ta je naopak popírána, ačkoliv technické možnosti tu jsou.

Druhým českým problémem je **neefektivní režim výstavby energetických staveb**. Schvalování nových energetických staveb i rekonstrukcí těch stávajících se táhne léta, pravděpodobně to zdrželo i rekonstrukci trasy V411. Od roku 2024 existuje [Dopravní a energetický stavební úřad (DESÚ)](https://desu.gov.cz/), který měl problém vyřešit tím, že se bude soustředit jen na dopravní a energetické stavby. Jenže úřad, který mimo jiné převzal činnost třeba Drážního úřadu či Úřadu pro civilní letectví, se dlouhodobě potýká s nedostatkem lidí. Na přelomu letošního roku měl podle rozpočtu 135 systemizovaných míst, ale obsazená byla stovka, v květnu 2025 už DESÚ uvádí **252 obsazených míst** (systemizace 279) – a stále se potýká s nedostatkem lidí, protože na něj byla přesunuta celá řada agend, jako je posuzování vlivu na veřejné zdraví, které z názvu tolik neplynou.

Důvody, proč DESÚ nemůže sehnat lidi? Prozaické: nekonkurenceschopné platy v branži. Jako specialista na energetické či dopravní stavby si v soukromém sektoru vyděláte dvojnásobek. Výsledek? Řízení neběží zdaleka tak svižně, jak si vláda představovala. Idea nového úřadu byla dobrá, výsledek zatím ne tolik dobrý. Bez lidí to prostě nejde.

### 🎬 Závěrem

Zatímco u bitcoinové aféry ministra Blažka šlo o "prkotinu", která představuje jen morální poselství o tom, jak přistupovat k výnosům z trestné činnosti, v tomto případě jde o něco velmi vážného. Dlouhodobě se kojíme nadějí, že máme nejlepší přenosovou soustavu na světě a že v energetice jsme borci, ze kterých by si Německo mělo brát příklad, kdyby Němci měli dost rozumu. A pak pošle pětinu republiky do tmy jedna blbá spojka? Není to ve skutečnosti tak, že už nejsme schopni držet v provozu ani to, co je podstatné, jako je energetická infrastruktura a dělá nám problém nastavení a vymáhání pravidel i tam? Jak to, že nejsme schopni povolovat ani stavby, které považujeme za životně důležité? Není to ve skutečnosti tak, že naše energetická infrastruktura je místy dosti obstarožní a nevěnujeme se jí tak, jak by měnící se dynamika spotřeby elektřiny vyžadovala?

Nejsme v mnohem větším problému, než je dvouhodinový výpadek?