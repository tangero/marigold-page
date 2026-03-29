---
slug: 'spanelsko-blackout'

audio_url: null
author: Patrick Zandl
categories:
- Energie
- Energetika
- Green Deal
date: 13.5.2025
summary_points:
- ENTSO-E vydalo předběžnou zprávu o blackoutu.
- Kmitání v síti začalo před polednem a přetrvávalo.
- V 12:32:57 vypadlo 2,2 GW fotovoltaiky v Extramaduře.
- Primární příčinou bylo překročení napěťových a impedance limitů.
thumbnail: https://www.marigold.cz/assets/putin-jistic.jpg
title: ⚡️ Vyšetřování blackoutu ve Španělsku a Portugalsku den za dnem (update 13.5.)
---

Co nového ve vyšetřování španělského blackoutu? [ENSOE-E uvolnilo první předběžnou zprávu](https://www.entsoe.eu/news/2025/05/09/entso-e-expert-panel-initiates-the-investigation-into-the-causes-of-iberian-blackout/), ale úplně nejvíc jasno z ní není, proto jsem také informace pár dní neaktualizoval, jen bychom naprázdno propírali hypotézy nebo padali do logických pastí. 

Časovou osu jsem teď nicméně nedoplnil o data  [z podcastu Frauenhofer Institutu](https://www.youtube.com/watch?v=ElDQr8Vueyw), který má vlastní měření v několika bodech a jeho data i úvahy lze brát za věrohodné. V přehledu jsou data označena jako (FRA).

Co z časové osy plyne? Pořád více méně slyšíme stejný příběh, jehož počátek úplně nevíme. Krátce po poledni pokračuje kmitání ve španělské přenosové síti, které jsme viděli už dopoledne. Probíhají první pokusy o tlumení této oscilace, ale kmitání přetrvává. Pak máme desetiminutové okno, z něhož nejsou publikována žádná data. Jen víme, že v 12:32:57 dochází k okamžitému výpadku cca 2,2 GW výkonu fotovoltaických elektráren v oblasti Extramadura (a údajně 1 GW v oblasti Andalusie). O pět vteřin dříve podle jedné zmínky (neuvedené v oficiálním soupisu ENTSO-E) došlo přepětí na rozvodně Araňuelo a Majadas - údajně až 6 %, což je dost - ale toto číslo není oficiálně potvrzeno.. Pokud chcete bít po hlavě obnovitelné zdroje, nemusíte číst dál.

Ve skutečnosti je velmi důležité, proč k odpojení tohoto výkonu došlo. Hypotéza "mlátíme OZE po hlavě" říká, že došlo k náhlé nadvýrobě na FTV a tím došlo k odpojení. Jenže to by se muselo opravdu fofrem vyjasnit počasí. V oblasti Extramadura bylo jasno už dlouho a k takovým změnám nedochází ani rychle, ani snadno. Navíc meteorologové to popřeli. Krom toho takové předpovědi má operátor gridu v předstihu a buďto operátor nebo meteorologové by museli udělat velkou chybu. Jistě, mohly nastat i další události, které způsobují spuštění nadnapěťové ochrany měničů: mohlo dojít k přebytku jalového výkonu, rychlému odpojení velké zátěže, špatně seřízenému OLTC atd. To vše jsou chyby v nastavení.

### Autonomní oblast Extramadura

Řekněme si něco k autonomní oblasti Extramadura. Sám jsem ji musel najít na mapě, je to jihozápad Španělska na hranici s Portugalskem a je to jako oblast největší čistý exportér elektřiny. Instalovaný výkon je kolem 12 GW (cca desetina Španělska), naprostou většinu exportuje. Polovinu dělá fotovoltaika, 17% jaderka v Almarazu, 20% vodní a přečerpávací elektrárny, 3% jsou solárně-termální elektrárny, zbytek je vítr, kogenerace atd. Ze seznamu vidíte, že točivých zdrojů má Extramadura obecně dostatek, jenže v tento den tomu bylo jinak.

Pro náš příběh je podstatné propojení Extramadury dále do Španělska, kde hlavním propojovacím bodem je rozvodna Aranuelo nedaleko jaderky Almaraz. Nezkoušejte ji najít na mapě, je součástí fotovoltaického parku Iberdroly, který mimochodem má bateriové úložiště. A sice není prostorově velká, ale je zásadní a je nejdůležitější energetickou křižovatkou západního Španělska. Vyvádí elektřinu z jaderky Almaraz (2 GW), obsluhuje fotovoltaiky a další zdroje v oblasti a dělá primární jalovou regulaci pro severní Extramaduru. Tzn. má na starosti cca 6 GW transformované nebo přímo přepojované kapacity. A především směřuje elektřinu do oblasti Madridu, včetně průmyslu.

Jak mohlo vzniknout lokální přepětí v Aranuelu? Nejpravděpodobnější variantou je, že došlo ke spuštění ochranného odpojení votovoltaických měničů, což zvýšilo oscilaci v síti a větrné parky Andalusie vyhodnotily oscilaci jako napěťový kolaps a také se odpojily. Následně se odpojila linka Španělsko-Francie (ať již na pokyn operátora nebo automaticky, to se šetří) a kaskádovitě následovaly další zdroje prakticky už "v jednom okamžiku".

Jenže jak se síť mohla takto rozkývat? V oblasti jsou dva hlavní vyrovnávací prvky, statický kompenzátor v Cedillo a jalová regulace v jaderce Almaraz měla teoreticky výkyv kompenzovat nebo rozložit tak, aby nedošlo k okamžitému, současnému odpojení. Proč se tak nestalo, je zatím nevysvětleno: podle nepotvrzené informace kompenzátor v Cedillu nezafungoval správně a v jaderce Almaraz měl být odstavený jeden blok kvůli výměně paliva (tedy celkem 3 ze 7 bloků jaderek byly mimo síť). Abychom si to uměli představit: kompenzátor se mohl sepnout s mírným zpožděním a naopak problém v síti krátkodobě zhoršit, na což mohly reagovat binárně nastavené ochrany fotovoltaik jako na lokální přepětí. Ale dost spekulacím. Na situaci se navíc negativně podepsal přetrvávající export elektřiny do Portugalska i Francie.

Druhou variantou je rychlá změna točivého výkonu mezi extramadurskou a madridskou oblastí přenosové soustavy, což místní regulátory nemohly absorbovat. Tady by se nabídlo "náhlé odpojení" fotovoltaik, ale to by spíše síť stabilizovalo a na prvotní příčinu úplně nevypadá. Opět: spekuluje se o nevhodném pokynu REE nebo jeho chybném provedení k snížení výkonu paroplynové elektrárny v oblasti Sevilly, čímž by se myslela dva roky stará paroplynovka Kryštofa Kolumba v Huelvě o 391 MW.

Jak vidíte, možností je celá řada a ve skutečnosti velmi záleží na tom, proč se co stalo. Může jít o technickou chybu, nevhodný zásah dispečera sítě či - jak se také spekuluje - na nepřeprogramované ochrany, které nejsou aktualizované na změny poměrů v síti.

V zásadě je podle těchto údajů nejpravděpodobnější, že šlo o kombinaci pomalu rostoucího kmítání mezi dvěma přenosově oddělenými oblastmi, lokálních napěťových špiček a následných ochranných zásahů relé, které vyřadily klíčové vedení. Zatímco dříve padaly podezření na „výpadek OZE“ nebo „kyber-útok“, video i oficiální zprávy společně potvrzují, že **primární spouštěč** bylo **překročení napěťových a impedance-limitů** v kombinaci s nízkou tlumicí kapacitou sítě.


Časová osa:

-   12 : 03 CET Vysokofrekvenční oscilace ≈ 0,63 Hz detekována ve frekvenčním záznamu Malaga i Freiburg, amplituda roste po dobu čtyř minut _(FRA)
-   12 : 12 – 12 : 23 Roste frekvenční rozdíl mezi Pyrenejskou a Evropskou sítí o 0,217 Hz. Spektrální analýza PMU Freiburg potvrzuje koherentní kmitání mezi Pyrenejským poloostrovem a střední Evropou _(FRA)_   
-   12 : 19 – 12 : 21 První pokus o tlumení oscilace dokumentován v předběžné chronologii ENTSO-E. Ochrany AVR a FACTS zařízení zkrátily amplitudu, kmitání přetrvalo. AVR je regulátor v elektrárnách, který hlídá konstantní napětí generátoru. FACTS je „elektronický tlumič“ napěťových výkyvů na dálkovém vedení, který na pokyn operátora nebo automaticky bleskově vyrovná přepětí či podpětí, aby se síť nerozkývala.  
-   12 : 32 : 52 lokální přepětí 6 % na rozvodně Aranuelo (nepotvrzeno!)   
-   12 : 32 : 57 Ze sítě vypadává zhruba 2,2 GW fotovoltaiky v regionu Extremadura, současně cca 1,0 GW větrná Andalusie; potvrzeno v předběžné chronologii ENTSO-E.  
-   12 : 33 : 18 – 12 : 33 : 21 Frekvence iberské podzóny klesá na 48,0 Hz; aktivováno podfrekvenční odlehčení zátěže UFLS (cca 2 GW), aktivovány frekvenční ochrany měničových zdrojů (zdroj ENTSO-E).
-   12 : 33 : 21 Impedance-relé vypínají všech šest 400 kV vedeních ES–FR pro nadkritický fázový úhel (potvrzeno ENTSO-E) - tím okamžitě v síti roste nadvýroba a přestává existovat možnost stabilizace importem z Francie.  
-   12 : 33 : 24 Totální kolaps synchronismu na Pyrenejském poloostrově, výkon v provozu je cca 0,4 GW.  
-   12 : 33 – 12 : 34 Fázový rozdíl Malaga–Freiburg integrovaný z frekvence dosahuje ≈ 90°, což je limit stabilního přenosu _(FRA)_   
-   12 : 44 start "ze tmy" přečerpávací vodní elektrárny Alcántara; první 400 kV koridor ES–FR pod proudem (oficiální ENTSO-E)    
-   13 : 04 Sestavena druhá linie ES–MA; začlenění hydroelektráren, následně CCGT.
-   18 : 36 Synchronizace první 220 kV vazby ES–PT.   
-   21 : 35 Synchronizace jižní 400 kV ES–PT.
-   29 / 4 00 : 22 Portugalská přenosová soustava v normálním stavu; 04 : 00 Španělsko.

> Níže pod touto sekcí najdete zprávy k události ze dne incidentu a z dalších dní, kdy jsem situaci sledoval. 


--

### 🇪🇸⚡️ 5.5. - Španělsku hrozil blackout několik dní

Po zajímavé stopě se pustil Reuters. Ten zdokumentoval několik výpadků z dní předcházejících blackoutu. V týdnech před pondělním kolapsem zaznamenala soustava několik menších poruch a experti opakovaně upozorňovali na narůstající nestabilitu a na to, že soustavu může rozhodit jak nedostatek výkonu, tak ale i její přebytek, což hrozilo zejména s růstem slunečních dní a tím s růstem produkce elektřiny, zatímco teploty byly ještě nízké na to, aby lidé masivně zapínali klimatizace. 



Interní experti i REE v ročních zprávách upozorňovali na rostoucí nestabilitu kvůli souběhu malých zdrojů OZE a nedostatku dat z nich. REE z nich totiž nemá online data (či near-real-time data) o jejich produkci a pouze ji v reálném čase predikuje podle počasí, nemá ani vliv na připojení těchto zdrojů do sítě a jejich odpojení. 
Experti ENTSO-E také upozorňovali na nedostatečné plánování chystaného vyřazování jaderných reaktorů ze sítě s tím, že už plánovaná výměna paliva v reaktoru Almaraz II může být problém. Reaktor byl odpojen od sítě 20 . 4. 2025 a přešel do horkého odstávkového stavu. Práce podle harmonogramu pokračovaly i během blackoutu.
Dne  22. dubna se objevily nápadné přepětí v síti a výpadky řízení, které odstavily vysokorychlostní vlaky a rafinérii Cartagena, což mělo být a zřejmě i bylo první vážné varování, problémy s v různé míře intenzity projevovaly až do 28.4.2025, kdy v 12:31 došlo k blackoutu na Pyrenejském poloostrově. Přesná souslednost výpadku je nicméně stále předmětem šetření. 

Síť je nyní stabilní, nouzový stav byl zrušen. Vyšetřovací panel ENTSO‑E má plná data a nejpozději do 10 .5. slíbí první technický verdikt. Do té doby se čeká především na výsledek francouzského testu ochranných relé, který má objasnit, proč se Pyreneje odpojily prakticky v jednom okamžiku - a v kterém okamžiku to bylo. Nové informace nicméně posilují verzi systémového selhání, tedy neschopnosti REE řídit dynamicky se vyvíjející situaci v síti kvůli nedostatku dat a regulačních mechanismů. 



---

### 3.5. 2025

Vyšetřování španělského blackoutu pokračuje, už se neobjevují žádné další podstatné informace. Stále není zřejmá přesná souslednost začátku, tedy zda za výpadek mohl nějaký zdroj, nebo nějaká událost v přenosové síti - čili kde kaskáda kolapsu začala. A zrovna tohle je hodně důležité. 

Zatím pouze docela přesně víme, k čemu to vedlo, ale ne, jak to začalo - a nápravná opatření se podle toho budou výrazně lišit. V pátek proběhlo velké setkání, kde REN a REE předložily předběžné zprávy, ale nic podstatného z nich neuteklo, prohlášení po schůzce opakují jen již známé věci.

Ne každý je z detailního vyšetřování nadšený. Španělská vláda si vyžádala od Iberdroly, Endesy, Repsolu aj. „černé skříňky“ měničů a blokových ochran.   Kdyby se nemohly najít, což se v takových situací stává, tak premiér Sánchez "nevylučuje sankce při neodevzdání". Slušně vynadáno dostává španělský provozovatel přenosové soustavy REE (Red Eléctrica). Je již mnoho důkazů proto, že síť byla nestabilní již v pondělí dopoledne, REE nepřikročil k větší regulaci, ačkoliv mohl a zřejmě i měl. Kromě toho se ukazuje, že jej řada institucí upozorňovala již dříve, že nemají síť v dobré kondici. Tím hlavním varujícím byl právě  ENTSO‑E, asociace operátorů přenosových sítí a operátor evropského gridu CESA. Akcie REE se propadly o 7 % - a nelibost premiéra Sáncheze jde zřejmě hodně tímto směrem, protože ať už byla příčina kdekoliv, bylo na zodpovědnosti REE si takovou věc do sítě pustit s patřičnými parametry nebo přijmout patřičná opatření. 

To také znamená, že se houpe křeslo s šéfkou REE Beatriz Corredor, někdejší ministryní pro bydlení za sociálně-demokratickou stranu PSOE. Beatriz Corredor prohlásila, že nic takového se nebude opakovat a aby dodala svým slovům i technickou váhu, od úterka REE výrazně změnilo skladbu produkce elektřiny. Snížilo podíl fotovoltaiky a zvyšuje podíly produkce z točivých zdrojů (paroplynovky a uhlí). Část elektřiny také dobírá z jiných sítí, zejména Francie. Jako preventivní opatření portugalská ministryně životního prostředí Maria da Graça Carvalho oznámila, že Portugalsko “preventivně přestalo importovat elektřinu ze Španělska”. Dále zdůraznila potřebu více přečerpávacích vodních elektráren a bateriových úložišť v budoucnu, jakož i posílení propojení s Francií.

Čili zatím vyčkáváme na oficiální výsledky, nicméně je už zřejmé, že trámy k ukřižování jsou připraveny. 


---

Za včerejšek mnoho novinek nebylo. Všichni zúčastnění po pondělním šoku pomalu najíždějí na informační disciplínu, která je v tomto případě užitečná, protože se ven nedostávají izolované zprávy, které lze snadno dezinterpretovat. Už dnes je jasné, že situace je velmi komplexní a nelze to vyřídit stylem "někdo hodil bombu do rozvodny". 

🇪🇸💡 1.5.2025: Jak pokračuje vyšetřování pyrenejského blackoutu?

Pro mě je také nepříjemné to, že sice se pořádají setkání s médii, z nich ale nevycházejí žádné oficiální zprávy, weby REN/REE mají jen prohlášení, že se to stalo a že to řeší, novinky nepředávají. Takže tyhle zprávy nabírám z médií a tam je často sdělení překroucené, zamlžené, protože pisatel nebyl energetik a v tomto případě na detailu záleží. 



První velkou novinkou je, že jsem se dostal k datům z vnitřní sítě nízkého napětí ve vteřinovém rozlišení. Neumožňuje to vypátrat lépe příčinu, ale je vidět, že první problémy byly v rozvodné síti již dopoledne (což už bylo známo dříve), někdy po 9 hodině začalo na hladině nízkého napětí oscilovat napětí až o 11V, což rozhodně není obvyklé, obvyklá bývá jednotková oscilace. Navíc se zvyšovala amplituda kmitů, byly četnější, pak se před polednem situace stabilizovala. To sedí k informacím o tom, že oscilovala frekvence na přeshraničním pyrenejském připojení, k tomuhle jevu dochází na hladině nízkého napětí, když se "přetlačují" toky ze dvou velkých sítí. Jenže taky v řadě dalších případů, takže z toho nededukujme mnoho.  Dlouhé, pomalu sílící kmity nicméně naznačují nedostatečně tlumenou soustavu (málo setrvačnosti / tlumicích výkonů). Znamená to, že síť byla nestabilní několik hodin před blackoutem a dispečeři si toho museli být vědomi, zjevně se zásahy snažili síť stabilizovat. 
Pomalý rozjezd oscilací také spíše vylučuje terorismus, to by muselo jít o dobře cílené a synchronizované útoky. 

Z oficiálních vyjádření také víme, že došlo ke dvěma vážným problémům předcházejícím blackoutu. REE uvedlo, že šlo přerušením dodávek elektřiny a zatímco se španělská síť dokázala zotavit z první události, ředitel Eduardo Prieto uvedl, že druhá byla mnohem ničivější a vyústila v přerušení dodávek elektřiny z francouzské sítě a „masivní dočasné odpojení“. Zatím nebylo oznámeno, o co šlo, některé zvěsti říkají, že v prvním případě vypadla fotovoltaika o cca 3 GW někde v Extremaduře, v druhém o 1 GW větrníků v Andalusii. Oficiálně to ale potvrzeno není. 

Extremadura je fotovoltaické srdce Španělska, ale největší FTV parky zde mají max 600 MW, většinou jsou kolem 200 MW, na 3 GW výkonu by jich musela vypadnout zhruba desítka, což znamená, že jde o systémový incident, ne o náhodný nezvládnutý výpadek.  Například jsou všechny FTV napojeny na stejnou páteřní trasu 400 kV Almaraz - Guillena přes čtveřici rozvoden. Proto je důležité bedlivě stanovit časovou mapu  a tím se dobrat k tomu, zda se synchronně vyply FTV parky, nebo je odpojily ochrany rozvoden či 400 kV linky, protože všechny tři jevy mají jiné řešení. Podobně je to s větrníky v Andalusii.

Čili jsme zase u toho. Čekáme na závěry probíhajícího šetření ENTSO-E a přesnou časovou osu, přičemž další tisková konference snad už s detaily, má být 2.5. 

Jedna věc je vtipná, všichni už si kryjí záda. REE upozornilo, že na systémovou nestabilitu sítě upozornilo ve své letošní únorové zprávě (tedy několik let poté, co jim to samé říká ENTSO-E coby šéf eurosítě). 

Jinak pro zlepšení hospodské debaty: samozřejmě existují setrvačná a elastizující řešení i pro FTV a větrníky. Nemusí to být nutně baterie, ale třeba synchronní kompenzátory, flywheely nebo intertia boosty pro větrné turbíny. Řešení je celá řada, nemusíte kvůli tomu nutně vydlabat vrcholek kopce a napustit ho vodou, jenže když si to do sítě neobjednáte, tak to nemáte. 

🚗 Pyrenejská rozvodná síť byl prostě nadupaný sportovní kabriolet, do kterého se daly kvůli úspoře brzdy z Felačky a v zatáčce v Pyrenejských serpentinách se to prostě vyklopilo. Buďto zakážeme výrobu sportovních vozů, nebo do nich značneme dávat odpovídající brzdy, moc víc nad tím nevymyslíme...

...okračování zítra asi odpo, až budou venku zprávy...  

---

3️⃣🇪🇸⚡️ 30.4.2025 Co nového se španělským blackoutem?

Jak vypadá situace kolem španělského blackoutu energetické sítě? Včera se téměř vše vrátilo do normálu, zapomeňte na novinové titulky "budou se vzpamatovávat týden" - kromě specifických věcí už je (v energetice) vše v normálu. Nicméně probíhá šetření. Co víme nového? No, pokud už sami máte jasno, tak dál nečtěte, protože jasno moc není. 


V zásadě byla opuštěna myšlenka gallopingu jako JEDINÉHO SPOUŠTĚČE, tedy že šest 400 kV linek přes Pyreneje do Francie odpojily ochrany kvůli nadměrnému pohybu vedení vinou proudění vzduchu. Zdá se, že k pohybu došlo, ale ten nebyl jedinou či přímou příčinou odpojení linek. Atmosférická situace nebyla nijak extrémní. Nicméně ještě probíhá vyhodnocování měření. 

Už se ale spíše uvažuje o špatně nastaveném firmware ochran, protože RTE potvrdila, že se používají stejná nastavení, jako u linky 400 kV v Lotrinsku, která se loni planě odpojila. 

Dnes bohužel není úplně veřejně jasné, zda k odpojení linek došlo PŘED nebo PO zlomové události, tedy jak moc velký vliv jejich přerušení mělo a zda nebylo spouštěčem blackoutu. 

V každém případě již nyní je zřejmé, že došlo k celé souhře událostí, mezi něž bych neváhal přidat španělský čurbes. 

Především je třeba říct, že nemáme všechna podkladová data, sice scanuju všechna patřičná média, ale v nich se objevují zprávy útržkovitě a často manipulativně. Například ten galloping, ukázalo se, nebylo oficiální vyjádření portugalského REN, ale rychlý osobní názor jednoho z dispečerů, které bylo v médiích oseknuto tak, že to vypadalo jako oficiální postoj.  Stejně tak v deníku el Pais se objevila data z jednoho slide určeného pro krizové jednání vlády, které ukazovaly na konkrétní problém, jenže se později ukázalo, že v prezentaci šlo o dva slajdy a na tom prvním byl zachycený začátek události, který všemu dával jiný kontext. Za třetí se ukázalo, že jeden z důležitých logů měl posunuté časové razítko o skoro dvě minuty, protože neměl přesný čas, což na interpretaci dat vrhalo jiné světlo.  Proto nutně s daty opatrně a nedělat unáhlené závěry. 

Pojďme si zrekapitulovat, co víme.  

Kolaps španělské přenosové soustavy byl extrémně rychlý a rozsáhlý. Během pouhých pěti sekund došlo ke ztrátě přibližně 15 gigawattů (GW) elektrického výkonu. Tato ztráta představovala zhruba 60 % okamžité celostátní poptávky po elektřině v daném okamžiku. Okamžitá poptávka ve Španělsku dramaticky poklesla z úrovně přibližně 26 000 - 27 500 megawattů (MW) na hodnoty blížící se 15 000 MW , přičemž v nejnižším bodě dosáhla pouhých 10 480 MW. Tato bezprecedentní rychlost a rozsah ztráty výkonu byly klíčovými faktory, které vedly k následnému kaskádovému selhání a rozpadu sítě. 

Tohle víme vcelku jistě. Nyní je otázkou, co tu ztrátu 15 GW v síti způsobilo. 

Podle první teorie to byl výpadek linek přes Pyreneje, zatím z neznámých příčin, kterých mohlo být více (kyberútok se tady zatím stále spíše neuvažuje). Při přerušeném exportu do Francie by frekvence sítě ve španělsku vyletěla nahoru (a v EU dolů) a fotovoltaické a větrné elektrárny v rozmezí 8 sekund odpojily od sítě něco jako 15-30% výkonu. Tento pokles je okamžitý, nemá prakticky žádnou elasticitu, čímž dostane frekveci pod 50 Hz a při poklesu pod 49,5 Hz se odpojily tři plynové bloky a všechny jaderné elektrárny. Ochrana zátěže následně odpojuje část odběratelů, cca 3 GW. Takhle se mohl nasbírat propad o těch 15 GW. Situaci nepomohlo to, že v dlouhodobé odstávce byl jaderný blok Vandellos 2 a v údržbě JE Trillo (čili běží dvě JE) a také to, že náhradní zdroje, které měly okamžitě nastartovat, nastartovaly mírně později, než měly. PVE Alcántara se přifázovala +110 s po oddělení a CCGT Cartagena dodal prvních 250 MW dokonce až +7 min, přičemž první dodávky měla dát už za dvě minuty. Na vině byl možná tlak plynu, ale to už je nepotvrzené.  

Podle druhé teorie (zveřejněné REE) došlo k propadu výroby na dvou španělských elektrárnách zatím z neznámého důvodu, což (a to už je interpretace) spolu s dalšími faktory jako špatný firmware a galloping nebo rozhodnutí ochrany evropské sítě vedlo k rozpojení linky a kaskádě tak, jak bylo popsáno výše. 

Proč se odpojily dva velké zdroje ze sítě, není zatím jasné - tady není ani náznak a počkal bych na data. V Česku se to nicméně hodilo na tuto verzi a prý to měla způsobit výroba z OZE, což není příliš pravděpodobné. 

Jak se nezávisle prokáže, co bylo první, zda výpadek linky nebo zdrojů? Vcelku jednoduše: pokud frekvence stoupla na 50 Hz, znamená to převis výroby v síti, což napovídá na odpojení linky (která exportovala 5 GW do Francie). Pokud naopak frekvence klesla, tak nejprve vypadly zdroje. Bohužel přesnější grafy a časy nebyly publikovány a z veřejně dostupných dat je rozlišení malé (bavíme se o 4 sekundách rozdílu!). Zatím jediná data z údajné interní zprávy  RTE cituje článek Euronews, podle nějž frekvence na kontinentální (francouzské) straně vyskočila asi na 50,20 Hz a během několika sekund se vrátila k nominálu. Grafy z kontinentální sítě ukazují, že k výpadku 5 GW (což odpovídá pyrenejské lince) vypadlo ve 12:31 a začínají nabíhat regulace ve zbytku Evropy, které situaci v Evropě dostanou během tří minut zcela pod kontrolu. Bohužel veřejné zdroje o španělské produkci elektřiny jsou agregované na pět minut, takže lze jen potvrdit, že mezi 12:30 a 12:35 došlo ke ztrátě minimálně 11 GW produkce a to nám nepomůže...    

Zavržené jsou zaručené zprávy o výbuchu španělské rozvodny Sentmenat - nenese žádné takové známky. 

Vysvětlení s primárním výpadkem linky by lépe vysvětlovalo, proč vypadly točivé zdroje, ale zase zůstává nejasné, proč vypadla linka, zatímco primární výpadek zdrojů lépe vysvětlí odpojení linky a zase není jasné, proč by vypadlo tolik zdrojů. 
Budeme si tedy muset počkat, až se objeví více dat. 

Hlavní poznatky, kterými si můžeme být jisti, jsou zatím dva (a na oba byli REE/REN upozorňovány dříve): 
1. chybí lepší propojení do Evropy, mělo by být spíše dvojnásobné až trojnásobné, teď je Pyrenejský poloostrov energeticky spíše ostrov a Evropa mu nemůže moc pomoci. 
2. Jsou potřeba další rychlostartující úložiště typu baterie. 

---

### Pokračování z 29.4.2025

Záhy po publikování informací o rozpadu energetické sítě na pyrenejském poloostrově se začaly šířit teorie, kdo za to může. Rusko či jiní teroristé nebo snad Green Deal? Pojďme se s tím vyrovnat. 

Za prvé je potřeba říct, že vyšetřování probíhá, incident dostal nejvyšší klasifikaci ICS-3, což znamená mezinárodní odborné vyšetřování, které je na začátku. Nyní jsou více-méně jisté technické příčiny, které si zrekapitulujeme. A zároveň se nenašla kybernetická stopa, i k tomu se dostanu. 

- ENTSO-E (to je evropské sdružení všech provozovatelů přenosových soustav) potvrdila ztrátu více jak 10 GW během 5 s (v tiskové zprávě REE se psalo 15 GW), což je obrovsky mnoho, na to žádná síť není dimenzována. V energetické síti se spotřeba musí rovnat výrobě a jsou zálohy, ale ne 15 GW. 
- REE a REN (provozovatelé a dispečeři přenosových soustav ve Španělsku a Portugalsku) stále pracují s hypotézou „induced atmospheric vibration“ (galloping) na svazkových vedeních přes Pyreneje; ochrany prý vedení preventivně odpojily, čímž se poloostrov izoloval
- v okamžiku poruchy tvořily točivé zdroje jen ≈44 % výroby; vysoký podíl FVE a VtE urychlil pád frekvence. Točivé zdroje mohou do určité míry zbrzdit "pád soustavy", protože "absorbují" pád frekvence, oproti tomu fotovoltaika se v případě problémů okamžitě odpojuje a to síť naopak může destabilizovat. 
Internetem putují "zvěsti" o podivnostech v britské síti nebo o odpojení kabelu Viking Link mezi Dánskem a Británií, jenže data ničemu takovému nenasvědčují a ani patřičné instituce k tomu nic nevydaly, čili to vypadá na kachnu. 

Problém může být v tom "ochrany odpojily vedení". Podle analýzy SCADA logů se nezdá, že by do dálkově servisovatelných prvků někdo přistupoval, přesto je čistě hypoteticky možné, že někdo našel nějakou kombinaci postupů, jimž vyvolal kaskádovité odpojování. Někde jsem četl názor, že přeci stačí vzít klacek a vedení přes Pyreneje rozhoupat, aby hrozilo jeho zkratování. To jistě stačí, když vezmete asi stometrový klacek a nevadí vám ta trocha popálenin, kdy vás do nemocnice odvezou v krabičce od bot. A jelikož k mechanickému poškození (typu exploze) nedošlo, zatím se pracuje s tezí, že ochrany reagovaly příliš agresivně, než že by je k tomu někdo či něco donutilo. Ale uvidíme, tady je na závěry brzy a z pražské kanceláře rozhodně.

Co se děje teď?

- Španělsko oznámilo, že od půl sedmé našeho času pokrývá 99 % celostátní poptávky a všechny hlavní uzly vysokého napětí jsou pod napětím  .
- Portugalsko již včera informovalo o napájení 85 z 89 stanic; poslední venkovské okruhy se budou připojovat v průběhu dneška  .
- Nouzové linky Francie - Katalánsko a Maroko - Andalusie zůstávají otevřené, aby pomohly s vyrovnáním výkonu během startu tepelných elektráren 
- Doprava: Z kolejí bylo evakuováno více jak 35 000 cestujících, metro v Madridu a Lisabonu zprovoznilo první linky až dnes ráno  .
- Letiště: Madrid-Barajas i Barcelona-El Prat fungovaly na záložních okruzích; terminály zůstaly osvětlené, ale došlo ke zrušení více jak 400 letů  .
- Telekomunikace: mobilní sítě jely v nouzovém režimu na baterie — operátoři vyzvali uživatele ke střídmému volání, což prý úplně neklapalo, ranní interview na ČRo s reportérkou ze Španělska rušily výpadky.
- Veřejný pořádek: Španělsko rozmístilo 30 000 policistů; král Filip dnes vede zasedání Národní bezpečnostní rady  .
- Francie a Německo slíbily pomoc s mobilními bateriovými kontejnery a rychlými plynovými turbínami, pokud by přišly další vlny horka  .
- Velkoobchodní cena elektřiny v Iberian Market (OMIE) krátkodobě zhouply, ale už se stabilizují na day ahead průměru 6 €/MWh - problém byl spíš v dopravě elektřiny, než v její výrobní ceně a cenové výkyvy jsou malé. 

Takže závěr? 

Na závěry je brzy. Terorismu nenasvědčuje zatím nic. Ani tomu neruskému (to už by se někdo hlásil s požadavky), ani tomu ruskému (to už by Rusko nabízelo pomoc). Jenže to je také první rychlý pohled a mohlo to jistě být jinak. Logy nelžou, ale mohl je někdo uklidit. Ostatně, konspirátoři předpokládají, že teroristé po sobě poprvé pořádně uklidili stopy (což Rusové nedělají, proč někoho terorizovat, když není jasné, kdo vám dal přes pusu). 

Přesto vám sem jeden ilustrační obrázek dám 😎

![Putin si hraje s jističem](/assets/putin-jistic.jpg)

A ten Green Deal? Jistě, kdyby měla pyrenejská síť více točivých zdrojů, mohla dopadnout nějak lépe - jak moc, to se teprve nasimuluje. Ale kdyby měla balanční zdroje, jako jsou baterie, také by to ustála jinak. Na slunném jihu dávají FTV a větrníky velký smysl z hlediska produkčních cen a místní operátoři byli dlouhodobě upozorňováni na to, že tomu musí svoji síť přizpůsobit. Green Deal s nedodržením zásad diverzifikace nemá mnoho společného. 

Elektřina už prakticky všude svítí, ale skutečná „detektivka“ právě teď začíná.  Podrobné záznamy z ochran a phasor PMU teprve ukážou, zda vedla řetěz selhání opravdu kombinace „rozkmitaných“ pyrenejských linek a nízké setrvačnosti, nebo se v poslední chvíli přidalo ještě něco dalšího.

---

## Zpráva z 28.4.2025: 

Podle provozovatelů REE a REN došlo v 11:33 WES-T k „el cero“ – úplnému výpadku energetické soustavy na Pyrenejském poloostrově. Extrémní teploty v centrálním Španělsku způsobily neobvyklé kmitání 400 kV vedení. Ochrany postupně odpojily více linek a generátorů, až se Pyrenejský poloostrov oddělil ("islandoval", přešel do ostrovního provozu) od zbytku kontinentální sítě.

V izolované oblasti pak frekvence klesla ještě hlouběji, část elektráren se odpojila a následovalo masivní zatmění (blackout) Španělska, Portugalska a části jihozápadní Francie.  ￼

### ⚡️ Blackout: co se 28. 4. 2025 stalo ve Španělsku a Portugalsku?

Podívejme se na událost v grafu. Z něj je vidět, že pokles byl v nejostřejším místě jen 0,15 Hz. Pojďme si to vysvětlit pro zájemce o energetiku... 

Proč na kontinentu „spadlo“ jen 0,15 Hz?
- Po odpojení Iberského poloostrova ztratila zbytek Evropy čistý export ~4–5 GW ze Španělska (obě země měly v poledne vysokou výrobu ze solárních a větrných zdrojů).
- Tato ztráta se okamžitě promítla do grafu jako −150 mHz.
- Primární regulace ve zbytku Evropy (turbíny, baterie, HVDC linky) během sekund začala výkon zvyšovat, čímž frekvenci zastavila u ≈ 49,85 Hz a během tří minut ji vytáhla zpět nad 49,9 Hz.
- Díky rychlé reakci a dostatečné setrvačnosti se kontinentální síť neodstavila – v grafu vidíte jen krátký, ale prudký zářez.

![Graf frekvence v eurogridu](/assets/hz-net.png)

Co vidíme v grafu
- Osa y (Frekvence): nominál evropské synchronní sítě je 50,00 Hz.
- Tři křivky (žlutá = průměr, černá = maximum, šedá = minimum) ukazují, jak se frekvence mezi ≈ 11:55 a 13:00 CEST pohybovala v různých měřicích bodech propojené soustavy.
- Až do ≈ 12:30 se frekvence vlnila v běžném koridoru ±20 mHz (49,98–50,02 Hz).
- V 12:31–12:34 nastal prudký pád až na ≈ 49,85 Hz – to je odchylka −150 mHz.
- Vzápětí se frekvence díky primární regulaci a automatickým zálohám vrátila k 50 Hz; kolem 12:45 už je systém opět stabilní.

Co takový pokles znamená

Frekvence se sníží, když odběr náhle převýší výrobu (nebo když se naopak od sítě odpojí část výrobních kapacit). V evropské soustavě stačí nerovnováha ~30 GW / Hz; −0,15 Hz tedy odpovídá zhruba 4–5 GW náhle chybějícího výkonu.

Důsledky na Pyrenejském poloostrově
- Izolovaná Iberská soustava přišla o možnost importů z Francie, které by krátkodobě pomohly stabilizaci. Protože odběr převýšil dostupnou vlastní výrobu, frekvence spadla výrazněji (pravděpodobně < 49 Hz).
- Ochrany odpojily další zdroje i zátěže, aby chránily zařízení, což se navenek projevilo rozsáhlým blackoutem (vlaky, metro, letiště, domácnosti).
- Obnova musela probíhat postupně, aby se zamezilo dalšímu kolapsu napětí a frekvence.  ￼

Takže ve stručnosti: 

- Z pohledu zbytku Evropy šlo o „pouhou“ ztrátu ~5 GW → pokles frekvence o 0,15 Hz, rychle vyrovnaný zálohami.
- Z pohledu Španělska a Portugalska to znamenalo ztrátu propojení, hluboký propad frekvence a následný blackout.

Taková událost názorně ukazuje, jak citlivá je moderní síť: i malá odchylka frekvence na kontinentu může signalizovat dramatické dění v jedné jeho části, a proč je klíčové mít dostatek rychlých regulačních zdrojů a chytré ochrany.

PS: je to samozřejmě můj neodborný názor založený na tom co k tomu vyšlo