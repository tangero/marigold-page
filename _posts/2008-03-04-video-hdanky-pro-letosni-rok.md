---
ID: 2207
title: Video HDanky pro letošní rok
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/video-hdanky-pro-letosni-rok
published: true
post_date: 2008-03-04 10:55:01
categories: [Video, Média]
---
Letošní rok bude ještě více rokem videa, než ten loňský. Soudí tak nejenom zahraniční odborníci, ale vposledku i tuzemský tisk, který asi nepřehlédl vzestup návštěvnosti Streamu. Nu a pokud se podíváte na odhady provozu soudící, že Youtube.com dělá až 40% provozu na celosvětovém internetu, začínají být úvahy o HD videu zajímavé i pro síťaře samotné. HD video znamená čtyřikrát větší kvalitu obrazu oproti klasickému SD (či po televizácku PALu), což znamená také podstatně větší soubory a tím i podstatně větší provoz. Představa, že by Youtube přešel na HD kvalitu, je tedy ze síťařského hlediska jistě zajímavá. 
<!--more-->
Nejdříve trocha rekapitulační teorie. Internetovému videu dominuje momentálně Flash a dva jeho hlavní kodeky: Sorenson Spark používaný Youtube a o něco kvalitnější VP6 dodávaná On2. Ani VP6 už dnes nepatří mezi první ligu kodeků, ale co naděláte - jejich penetrace 95% počítačů je něco, s čím je třeba počítat a kouzlem Flashe také je fakt, že videopřehrávač posíláte na dálku jako součást HTML stránky, nemusí si ho uživatel instalovat. V čem jsou rozdíly? Sorenson Spark byl první Flash videokodek, dnes na něj existuje řada kódovacích utilit zdarma a dá se potunit tak, aby to bylo slušně koukatelné na rozlišení 320x240 bodů, jež Youtube používá. VP6 je výrazně lepší a dá se s ní pustit i do větších kouzel, ovšem v závislosti na vaší důvěře ve vaši internetovou přípojku, jeho použití je ale také dražší a jen za licence by Youtube propálilo jmění. Stream si jeho použití může dovolit díky řádově menšímu množství videí, které takto zpracovává. 

Youtube používá bitrate pro své soubory cca 320 Kb/s, rozlišení 320 x 240. Stream jde na 360 x 288 bodů rozlišení, což nebyla snaha předhonit Youtube, ale použít standardnější rozlišení pro televizní zařízení v evropské normě, tedy půl PAL. Ocení uživatelé neširokoúhlých videokamer. Hlavním rozdílem je u Streamu bitrate, která významně rozhoduje o kvalitě výsledného videa, ta je u nás na cca 500 Kb/s, protože jsme se snažili tlačit video ke koukatelnosti i ve fullscreen režimu. 

Dalšími hráči na poli video kodeků je třeba se zatím zabývat spíše teoreticky, WMV ve svých všech možných formách je od šitózní (ty prastaré) po excelentní technologii (ty nové) a není vůbec pravda, že je to uzavřený svět Microsoftu. Pracujeme ve Streamu s WMV pro živé přenosy, kde se osvědčuje více, než Flash a žádný Windows server na to nepotřebujeme. Fakt ale také je, že s WMV se nekouzlí tak snadno, jako s Flashem a v době, kdy všichni experimentují s tím, jak zpeněžit video, se právě na Flashi tahle kouzla  experimenty dělají lépe. Možná je to jen o zvyku, o dostupnosti nástrojů a učící křivce, ale faktem je, že snaha překreslit ovládací tlačítka WMV playeru podle našeho gustra se míjí účinkem, jenž by nás uspokojil. A co je hlavní: WMV funguje fajně na Windows/MSIE, obstojně na Macku, ale blbne na Firefoxu a na Linuxu je s ním kříž. Jistě, dá se to řešit, ale tohle úsilí, přijde mi (a nejenom mně) je zatím hodno jiných věcí. 

Velký comeback se podařil MPEG-4/H.264. Ano, je to sice standard, ale k čemu standard, když ho největší hráči nepoužívají (prosazuje se spíše v uzavřených IP sítích, než na netu obecně). Kromě Apple, který H.264 používá všude ve svých produktech jako standard (schováno do Quicktime rozhraní, přičemž Quicktime si lidé pletou s kodekem pro video, ve skutečnosti je to framework pro práci s videem používající právě H.264), si ostatní dávali na čas. H.264 nepřehrajete ve Windows  XP bez doinstalace kodeku. Na Linuxu je podpora zvána x.264 a zatím stále dle externích referencí není nijak skvělá (mějme na paměti, že H.264 má řadu profilů).

<h3>Flash MovieStar</h3>

A do toho přišla MovieStar. To je kódové jméno verze Flash pluginu, které zvládne přehrávat video v H.264 - což znamená, že místo Sorensonu/VP6 můžete používat video ve formátu H.264. A to je excelentní zpráva, protože tím se dostáváte v obecně rozšířeném prostředí Flashe k velmi kvalitnímu kodeku. Aby Adobe trochu mírnilo nadšení, tak podporu nezavedlo hned do Flash verze 9, ale do druhé nebo třetí revize této verze (značené tedy 9.0.2). Což se jistě všem dobře pamatuje a je to poznat i na tom, že weby se neshodnují v tom, která revize to je. Přitom, když odmyslím ActionScript 3 v čisté devítce, byl H.264 nejvýznamnějším update, jenže z hlediska uživatele je viditelnější, než ten ActionScript 3. Co naděláte, i tak díky za ty dary. 

Vtip H.264 ve Flashi tkví v tom, že podporuje i HD profil a díky ActionScript 3 také hardwarovou akceleraci dekomprese obrazu na grafické kartě. Což činí video v HD kvalitě o 720 řádcích věc koukatelnou i na dnešních noteboocích vybavených Celeron procesory, tedy žádnými nepřiměřenými děly. Na plné HD 1080p už přeci jen počítejte s tím, že Dual Core uživíte a stáhněte si topení v pokoji, při dvouhodinovém filmu procesor menší obývák vytopí obstojně. 

<h3>HD ráj</h3>

A tu jsme u toho, proč HD dostává pro letošní rok tolik příznivých predikcí. Je dostupné v masově nejpoužívanější technologii Flashe skrze průmyslový standard, můžete si s ním hrát v WMV i přes DRM a pak tu máme DivX. Zrovna toho se ale nedávno týkala slušná rána, když výrobce DivXu zavřel zcela znenadání minulý týden svůj projekt Stage6 zaměřený na kvalitní video. 

<a href="http://www.stage6.com">Stage6</a> byl něco jako Youtube, až na to, že kvalita videa byla propastně (a kladně) rozdílná. Na jednu stranu to bylo použitím firemního DivX pluginu a kodeku, na druhou stranu také bitrate byla trojnásobná. Proč šlo Stage6 ke dnu? Názory se různí, protože projekt byl navštěvovaný a i když si na účty od ISP vydělat zatím nemohl, investoři by se jistě našli. Prý také našli, ale pokus vydělit Stage6 z mateřské firmy dopadl krachem, který stáhl celý web sebou (<a href="http://www.techcrunch.com/2008/02/26/serious-drama-and-lots-of-stupidity-behind-stage6-shutdown/">podrobně rozebráno zde</a>). Už se ale šušká, že díky zpruzeným a odešlým vývojářům možná obživne <a href="http://www.newstage6.com">jinde a jinak</a>. Uvidíme. Podstatné je, že Stage6 byl jeden z prvních projektů, který systematicky šlapal do HD videa na webu, s ním stojí za zmínku snad jen Vuze od Azureusu. 

Proč je HD tak zajímavé? Nu, v Americe proto, že HD kvalitou se pokusí dodavatelé filmů dorovnat krok s místními televizemi, které zhusta HD používají. A v Evropě, potažmu v Česku?

Tady je to s HD infantilní. HD zdrojů je minimum, HD přehrávače se prodávají minimálně (pár tisícovek Blue-Ray plus HD-DVD) a tak to chvíli vypadalo, že situaci vytrhne HD vysílání Novy přes satelitní CS Link. Chyba lávky, koncem ledna to Nova zabalila bez udání smysluplného důvodu. Insideři v tom vidí novácké hrátky na televizním trhu, outsideři konec použitelného českého HD zdroje pro draže nakoupené placaté panely. 

Tady je důvod, proč by HD bylo v nějaké formě zajímavé pro internetové televize: byla by to možnost, jak nakrmit HD ready / Full HD televize, jichž je u nás už nahusto a jejichž majitelé se těšili, že si užijí Nova Cinema v HD a teď zjišťují, že skočili Rumunům na to, že mají špek. Vyhlídka pustit si něco v HD kvalitě, by stála za to laborovat na chvíli s propojením TV a počítače. 

To je to, proč na Streamu s HD nějakou chvíli pokusujeme s úspěchem, který by se technologicky dal označit za velmi pokročilý. Problém je spíše na poslední straně drátu - nedostatek HD zdrojů. Zatímco HD technologii lze označit za připravenou, kapacita připojení u řady uživatelů je dostatečná a zejména zákazníci UPC mohou být vysmátí a také uživatelé by nějaké to HD skousli jak technicky (mají na to výbavu), tak psychicky (prostě by se jim to líbilo), tak je problém s videi. Těch pořízených v HD kvalitě je málo. Někteří producenti už pragmaticky točí v HD, řada z nich na to ale ještě nepřešla plně (mají v HD třeba jen hrubý materiál nebo ani to ne). Navíc HD je mor pro amatérské tvůrce. Ne snad, že by nebyly levné HD kamery a střihové programy už si s HD taky poradí, cožpak o to. Ale standardní video milosrdně skrývalo chyby, jichž se filmaři dopouštěli, zatímco HD je naopak zvýrazní. Ne nadarmo se ve světě pornografie začalo pro HD video zhusta používat rozmazávání obrazu - dívat se na osmnáctiletou pannu v detailu, u níž je zřetelná pomeračnová kůže třicátnice, do diváka nenaladí. 

Používat HD na zprávy se nám zdá (vzhledem k jejich určení pro přehrávání v okénku) poněkud overkill, ale některé pořady by se už v HD snesly. Zkusíme, uvidíme. Předpoklady jsou jedna věc, zájem lidí druhá. Ale takové Peklo v HD, to by mohla být slušná sranda. 

S HD pokusuje i česká <a href="http://www.hdtv1.cz">HDTV1.cz</a>, ovšem problém stejný: nedostatek slušného materiálu, zato se můžete kouknout, jestli to váš počítač a linka utáhne, šíří to v 720p/2 Mb/s. 

<h3>HD řečí čísel</h3>

Z HD se budou radovat hlavně operátoři kvalitních sítí. UPC má při slovech HD úsměv od ucha k uchu, protože při provozu HD videa je poněkud signifikantní rozdíl mezi optickou sítí a WiFi páteří bastličů. Sloane se svou páteří nejinak. Jen přo představu v praxi: poslední čtyřicetiminutový díl Pekla měl ve Flashi/VP6 velikost 150 MB. Kdyby šel do HD 720p, tak bychom ho narvali do 1,7 Mb/s bitrate, což je v H.264 docela ušlá kvalita. Dostali bychom se někam na 500-600 Mb. 

Jestliže jsme včera ve špičce a v součtu všech uzlů vygenerovali přes NIX při premiéře posledního dílu <a href="http://peklo.stream.cz/">Pekla s Landou</a> cca 5 Gb/s, tak bychom s HD videem šli na cca. 10-2 Gb/s (ne všechen provoz dělalo Peklo, které by bylo v HD kvalitě). NIX by se ani nezadýchal, jen by zvýšil svůj rekord - ostatně, tomu včerejšímu rekordu 38,4 Gb/s Peklo s Landou také výrazně pomohlo. A také většina klasických poskytovatelů jako UPC, O2, Telekom Austria či ČD by jen zaznamenali rekordní provoz v síti, což by možná nějaký technik zmínil na meetingu jako perličku. Majitelé menších sítí, kde je hnacím motorem WiFi, by už ale problémy pocítili. Hloupé na tom je, že výpadky by šli na vrub Streamu, protože "internet přeci běžel". A to je to, proč s HD třeba ještě opatrně...

<h3>VP6-S taky bojuje</h3>
Kdo by rád zůstal ve hře, je On2 se svým VP6. To doplnilo o nový profil VP6-S, který umožní provoz HD videa na Flash verzích MovieStar a výše, tedy stejně, jako H.264. Výhodou má být nižší nároky na procesor vykoupené mírně horší kvalitou obrazu. Pozor na to: nároky na procesor v případě HD není radno podceńovat, protože nezapomínejte, že v paměti má uživatel ještě prohlížeč a plugin Flashe, dost možná řadu dalších programů jako Outloogk atd. To všechno žere strojový čas, což u jednoúčelových dekodérů přítomných ve specialiovaných přehrávačích nebývá. Jenže když se HD obraz trhne, tak je to zpravidla připsáno poskytovateli zdrojového obrazu, ne tomu, že vaše mašina mele z posledního a málokoho dnes napadne poshazovat programy nebo dokonce taby prohlížeče jen proto že by rád kouknul na HD video. 

Moje praktická zkušenost s VP6-S ovšem taková nebyla - Flash s H.264 se na první pohled tvářil méně vytíženě, než s VP6-S, ale měřil jsem to jen přes panel Windows a Macka, speciální utilitu na to jsem nenašel, takže s tím ještě budu laborovat. V každém případě je výběr dobrý... 

<h3>A co ti druzí? Nu, jsou druzí...</h3>

Banálně vzato, ostatní zatím třeba sledovat, ničeho více. DivX nutí k instalaci Playeru (je součástí oficiálního kodeku), Quicktime je dobrý, ale hlavně Apple řešení, pod Windows ho používá málokdo, podle mne i proto, že Windows verze je docela vlezlá a drze sedí v Tray, i když není důvod. RealVideo je už spíš praktickou demonstrací toho, kam monopolní choutky Microsoftu dostrkají nepohodlné, když soud nepřijde dostatečně rychle. 

Lidi mi občas vynadají, že nezmíním Theoru jako open-source video kodek. Tak abych ji zmínil jednou a definitivně: je to srajda, kterou kdysi milostivě uvolnilo právě On2 jako roaylty-fee-free videokodek pro open source hnutí. Theora je odvozena od VP3, dnes už dědečka srovnatelného s H.261 - a už z číslování videno, že to není žádný zázrak. Podařilo se ji sice vylepšit, ale kvalit konkurenčních kodeků nedosahuje a i o její otevřenosti si myslím své. Kdyby nebylo povyku kolem jejího konkrétního zařazení do HTML jazyka, pes by po ní neštěkl. A právem. 

On2 se s videokodeky snaží dál, představilo VP7, které je lepší, než VP6, copak o to - ale není ve Flashi, což stírá hlavní (a jak kritici rádi říkají, tak i jedinou) výhodu VP6. A Microsoft zatím tlačí své kodeky, takže je veselo. 

Na co si ale zvykněte, je koncovka MKV u videa. Jde o takzvaný Matrioška formát (Matroska po anglicku), tedy způsob kontainerování, balení videa a k němu příslušících informací do jedné obálky. Nově se prosazuje právě hlavně pro HD filmy a vytlačuje AVI, protože umožňuje lépe a přehledněji balit všechno najednou dle výběru, více zvukových i titulkových stop. A je to otevřený formát. Samozřejmě kodek videa nevyřeší, je to jen obálka, ale naráží se na ni stále častěji, tak je dobře vědět, o co jde. 

<h3>Závěr?</h3>

Není... nic není u konce a boj probíhá dále na všech frontách, takže to berme spíše jako rekapitulaci k dnešnímu dni. A jako poznámku, že HD na českému internetu nic nebrání. Jen si ověřte, co vaše připojení a výkon vašeho počítače :)