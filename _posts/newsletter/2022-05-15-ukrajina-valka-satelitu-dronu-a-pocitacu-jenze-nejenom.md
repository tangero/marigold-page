---
author: Patrick Zandl
categories:
- Patrickův newsletter
- Apple
- AI
- Sociální sítě
- Mobilní technologie
- Internet
- Česko
- EU
- Automotive
date: '2022-05-15'
layout: post
original_newsletter: 'Patrickův newsletter #47: Internetizace války na Ukrajině a
  Muskova šaráda s Twitterem'
summary_points:
- Ukrajina využívá automatizovaný systém řízení dělostřelecké palby s rychlou koordinací
  a přesností.
- Starlink poskytuje Ukrajině klíčové satelitní připojení pro armádní komunikaci a
  koordinaci palby.
- Ukrajinská armáda získává informace o cílech z cizích zpravodajských služeb, GIS
  ART a crowdsourcingu.
- Moderní válka se internetizuje, klade důraz na online propojení, automatizaci a
  decentralizaci řízení.
title: Ukrajina -  Válka satelitů, dronů a počítačů. Jenže nejenom.
---

Není to tak dávno, co jsem chtěl psát o válce mezi dvěma zeměma, jejichž jméno jsem zapomněl, _něco jako Azerbajdžán a Arménie_ 😈. Na té válce bylo zajímavé především masivní použití dronů. Vojenští stratégové se rozplývali, jak důležité bylo zapojení dronů. [Dobrý český článek najdete zde](https://www.czdefence.cz/clanek/delostrelectvo-versus-drony). Napsat jsem o tom tehdy nestihl. Jednak proto, že věrohodných informací ze skutečného pozadí bylo pramálo a pak také proto, že pořád ještě nebylo signifikantní, jak se mění to, čemu říkáme paradigma. 

Na Ukrajině ta obrovská změna je vidět a protože mírně vidím do ajťáckého zákulisí, něco si k tomu řekneme. Je to důležité, i když pokud nejste vojenský stratég nebo výrobce hi-tech, tak to pro vás je spíše fakultativní informace. 

Ještě, než v únoru začala invaze na Ukrajinu, zaútočili hackeři na satelitní síť KA-SAT provozovanou společností Viasat. KA-SAT je vysokorychlostní satelitní síť pokrývající Evropu a Blízký a Střední Východ a úplně nejdříve nebylo zřejmé, proč by na ni někdo zaútočil. Nejhlasitěji si stěžoval operátor německých větrníků, kterým hack (blokující satelitní modemy) znemožnil dálkové ovládání. Chvíli to vypadalo, s ohledem na výpadek 5000 větrníků a celkovou jejich kapacitu v řádu gigawattů, že šlo o útok na stabilitu německé přenosové sítě, že to bylo takové varování. Ale to byl první tip, který se ukázal mylný. Daleko spíše (potvrzeno samozřejmě není nic) útok směřoval na komunikační backend systému řízení palby ukrajinského dělostřelectva. Jeho radarové a polní systémy jsou totiž propojeny přes KA-SAT. Cílem útoku bylo odříznout ukrajinskou armádu od koordinace palby. 

### Řízení dělostřelecké palby

Řekněme si pár informací k tomu, jak systém řízení dělostřelecké palby funguje, military nadšenci odpustí, že to vezmu ve zkratce a se značným zjednodušením. Řízení dělostřelecké palby funguje "jednoduše". Radarová vozidla a radarové letouny v terénu zjistí pozici, odkud střílí nepřítel a jeho polohu předají vlastnímu dělostřelectvu, které opětuje palbu. Vtip je v tom, že se celá záležitost musí odehrát rychle a přesně. Rychle proto, že cizí dělostřelectvo zpravidla nečeká, až ho někdo vypátrá a průběžně mění pozici, aby se samo nestalo cílem. Přesně proto, že je důležitý přímý zásah, dělostřelecké granáty účinně likvidují vše v okruhu několika desítek metrů, ale za touto hranicí už tolik nepůsobí. 

Pracovní režim samohybných houfnic jakožto moderní verze dělostřelectva je tedy principiálně jednoduchý. Přes komunikační síť přijdou pozice pro palbu řídící počítač, obsluha houfnice vybere ideální terénní pozici, zastaví, během několika jednotek až desítek minut (kolik, to se liší podle toho, jak moderní houfnici mají) se připraví k palbě a systém automaticky, nebo obsluha manuálně zahájí palbu. Odpálí salvu, co nejrychleji se zabalí a přesunou, než nepřítel palbu opětuje. 

Co je zjevně podstatné, je minimalizace těch časů. Nejmodernější samohybné houfnice jako je francouzský [CAESAR koupený Českou armádou](https://www.armadninoviny.cz/houfnice-caesar-pro-armadu-ceske-republiky.html), umí pracovat automaticky, čili posádka zaparkuje, připraví systém do palebné polohy a systém si sám nabere palebná data a pálí. Po odpalu 7-10 střel posádka změní polohu a vše se opakuje. S ohledem na to, že CAESAR odpálí několik (až 6) střel za minutu a usadí je s přesností na 10 metrů při palbě na vzdálenost 20-40 km dle střeliva, může systém neustále dynamicky měnit polohu. O něco delší jsou časy u houfnic, které vyžadují externí přepravu, ale americké M777 umí pětičlenná posádka připravit k palbě během tří minut a za stejnou dobu ji zase připravit k přesunu. Ve výsledku to znamená, že moderní houfnice setrvá v pozici maximálně deset minut, předchozí modely houfnice jako Dana spíše půl hodiny a starší sovětské houfnice spíše kolem hodiny. Údaje berte s rezervou, různé zdroje se liší a záleží na mnohém, od terénu, přes vycvičenost posádky, až po používanou munici a její logistiku. 

Proč je to důležité? Inu, dělostřelectvo je letectvem chudých a ve skutečnosti králem bojiště. Střela z houfnice stojí o dva řády méně, než raketa. A řada moderních zbraní stojí více, než obstarožní socialistické zbraně, které mají ty moderní zničit. Takový sovětský obrněný transportér stojí méně, než velká část samonaváděcích zbraní "vystřel a zapomeň", které ho mají zničit. Takže mít kvalitně fungující dělostřelectvo je důležité, pokud chcete válku ekonomicky zvládnout. 

Ukrajina si pro řízení palby vyvinula několik pomocných systémů. Jeden z nich například bere koordináty cílů a podle pohybu vlastních zbraňových systémů rovnou zadává střelecké dispozice zbraním, které se mohou dostat co nejdříve do nejlepší palebné pozice. A jelikož podle vojenské doktríny k vyřízení jednoho cíle je potřeba použít dělostřeleckou baterii, tedy osm houfnic, tento "Uber pro dělostřelce" dá do kupy zbraně, které mohou zahájit palbu, aniž by ovšem jejich posádky o sobě nutně věděly a tvořily onu baterii, ale aby ve výsledku měly stejnou palebnou sílu. Koordinaci palby zajišťuje systém a tak je cíl ohromený tím, že na něj z výšky dopadají projektily a on s tím nemůže vůbec nic dělat. Co je podstatné? Maximální automatizace, vše běží online. 

Ukrajinská armáda dnes používá tři základní zdroje o cílech. 

  * Tím prvním jsou informace zahraničních zpravodajských služeb a satelitní snímky, které Ukrajina dostává vlastně v reálném čase. 

  * Druhým zdrojem je software GIS ART pro dělostřelectvo, což je moderní cloudový software, který ukrajinská firma vyvíjí pro všechny, kdo potřebují pracovat s geografickými a mapovými podklady v reálném čase. Je vlastně jedno, jestli je to nástroj pro řízení sanitek nebo dělostřelectva. Tak si ho pořídila i místní armáda. 

  * Třetím zdrojem je crowdsourcing ve formě internetové aplikace. Ten vznikl nejdříve jistou improvizací, kdy bojové jednotky přes síť Telegram prosily majitele dronů o fotky území, na které chtěly zaútočit. Záhy tak vznikla aplikace, do které lze posílat požadavky a dobrovolníci pomocí foto dronů doletí na místo a nafotí situaci, kterou další dobrovolníci i profesionálové z armády pomáhají analyzovat. On takový dron DJI má dolet několika kilometrů a velmi kvalitní fotky, takže pro okamžité ověření situace a přesné zacílení je ideální. Navíc je to snadné na obsluhu, vojáci posílají požadavky přes Telegram a zpět jim přijde odkaz na fotky. 




Tím prvním jsou informace zahraničních zpravodajských služeb a satelitní snímky, které Ukrajina dostává vlastně v reálném čase. 

Druhým zdrojem je software GIS ART pro dělostřelectvo, což je moderní cloudový software, který ukrajinská firma vyvíjí pro všechny, kdo potřebují pracovat s geografickými a mapovými podklady v reálném čase. Je vlastně jedno, jestli je to nástroj pro řízení sanitek nebo dělostřelectva. Tak si ho pořídila i místní armáda. 

Třetím zdrojem je crowdsourcing ve formě internetové aplikace. Ten vznikl nejdříve jistou improvizací, kdy bojové jednotky přes síť Telegram prosily majitele dronů o fotky území, na které chtěly zaútočit. Záhy tak vznikla aplikace, do které lze posílat požadavky a dobrovolníci pomocí foto dronů doletí na místo a nafotí situaci, kterou další dobrovolníci i profesionálové z armády pomáhají analyzovat. On takový dron DJI má dolet několika kilometrů a velmi kvalitní fotky, takže pro okamžité ověření situace a přesné zacílení je ideální. Navíc je to snadné na obsluhu, vojáci posílají požadavky přes Telegram a zpět jim přijde odkaz na fotky. 

**Satelitní síť pro digitální bojiště je nutná**

A tady jsme u zádrhelu. Na to, aby to fungovalo, je potřeba kvalitní mobilní připojení, přičemž s klasickou pozemní infrastrukturou nelze počítat. A to byl ten důvod, proč ruští hackeři vyřadili z provozu terminály KA SAT - měla je pronajatá i ukrajinská armáda. A proto také Rusko první dny postupovalo tak rychle (na dnešní poměry). Pro Ukrajinu byla koordinace palby bez satelitního připojení obtížná. 

Pak ale Ukrajina požádala o pomoc Elona Muska - přes Twitter, za velké pozornosti médií - a pravděpodobně i jinak. A Elon Musk poslal obratem pět tisíc satelitních terminálů, které během pár dní dorazily na Ukrajinu. A ta na ně ihned napojila svou armádu. Dnes jich má deset tisíc.

A tím se dostáváme k roli Starlinku a společnosti SpaceX. Samozřejmě i se Starlinkem si chtělo Rusko vyřídit své účty prostřednictvím hackerů a hned od počátku dodávek terminálů připouštěl Musk, že největší starost a práci firmě teď dává ochrana sítě a zásahy proti hackerům. Firma velmi rychle přes over-the-air update upravila přenos mezi terminálem a satelitem tak, aby se jej Rusku nepodařilo zarušit. Starlink se dnes používá také jako náhrada zničené civilní komunikační infrastruktury, kdy je instalován jako páteřní propojení mobilní sítě. Nokia dokonce upravila firmware základnových stanic tak, aby lépe fungovaly se Starlinkem. [Obsáhlý článek o tom mají na Wired](https://www.wired.com/story/starlink-ukraine-internet/). 

Rusko proti Starlinku nebojuje jen pomocí hackerů - celosvětově se objevila na proruských a pročínských médiích [řada článků](https://eurasiantimes.com/china-deeply-alarmed-by-spacexs-starlink-capabilities-usa/) o tom, jak Starlink je nebezpečný, protože narušuje dosavadní svrchovanost státu nad vlastním územím. A jak je Starlink strategickým vojenským projektem, který umožňuje americké armádě dominanci na bojišti, neboť Starlink se nedaří ovládnout ani zarušit jiným státům. Nu, je to tak - třeba satelitní síť Iridium přežila hlavně proto, že si ji platila americká armáda pro své použití v terénu a Starlink má na americkou armádu také své vazby. 

Pravda je, že Starlink se od jiných, především výlučně vojenských technologií, liší prudkostí svého vývoje. Většina vojenských proprietárních systémů je stará mnoho let a investuje se do nich pramálo, v Rusku navíc s obrovskou korupcí. Nenabízejí to pohodlí dané okamžitým promítáním výsledků výzkumů do produktu, jako je tomu v případě produktu, který se komerčně prodává na velmi kompetitivním trhu. Starlink musí být atraktivní pro koncové klienty jednoduchou obsluhou i cenou, což jsou aspekty, které ocení i armáda. Snahy vytvářet různé vojenské mesh sítě většinou nedopadly, bylo to drahé, někdo to neschválil atd. Starlink se prodává dobře - a válka na Ukrajině je pro něj excelentní reklamou. 

Válka se tak internetizuje. Nejde o to, že fotografie jsou digitální, ale že se přechází na výhody internetového konceptu, tedy plně online propojení, automatizaci rozhodování a řízení pomocí chytrých algoritmů a koordinaci pomocí téhož. Ukrajinské dělostřelectvo nemusí pálit z osmihoufnicové baterie, aby účinně zasáhlo cíl. Jejich "Uber pro dělostřelectvo" upozorní rozptýlené jednotky ve vhodných pozicích, že mají začít pálit a dodá koordináty. Nepřítel je pak zaskočený tím, že palba probíhá z mnoha stran a není kam uniknout, navíc rozptýlená palba i znesnadňuje obranu leteckou podporou. 

Na závěr se zastavím u třetího zdroje informací: crowdsourcingu. Na Ukrajině vznikla záhy po vypuknutí války aplikace umožňující jednotkám žádat o fotky z dronů, které dodávají dobrovolníci. Mohou se tak zpřesnit existující starší informace nebo tak lze vyhodnotit nové místo. Opět je to jednoduché, stačí v aplikaci či přes Telegram poslat souřadnice a rychle víte, kdy se tam dostane dron a kdy budou snímky. I tady je to podobné, jako si objednat taxi přes Uber. 

Těmi třemi metodami jsou kombinované informace neustále aktuální, umožňují kontinuální sledování situace a během málo desítek minut je zřejmá větší změna. Takto ve středu Ukrajina zlikvidovala pět desítek tanků a bojové techniky a údajně přes 1000 ruských vojáků při přechodu na řece Siverskyi Donets. Ženista vytipoval místo, kde je nejlepší řeku přejít, to sledovaly hlídky a drony. V momentě, kdy rusáci dorazili a postavili ponton, je rozstřílelo dělostřelectvo. 

Takže co jsou klíčové momenty?

1️⃣ odolná satelitní datová síť umožňující vysokorychlostní přenosy v polních podmínkách

2️⃣ vysoce mobilní (a decentralizované) dělostřelectvo s maximálně automatizovaným řízením palby - vojáci přijedou, postaví houfnice, ze sítě naberou koordináty, rychle odpálí malé desítky střel a než je někdo objeví, přesunou se. 

3️⃣ systém pro náběr a vyhodnocení dat z velmi heterogenních zdrojů plus tým, který vyhodnocení provádí

4️⃣ drony, pro snímkování klidně i civilní - a spolupráce desítek nadšenců pro jejich ovládání

Česká armáda žádný takový systém ještě nedávno neměla a nevím, jak moc se to změnilo s nákupem houfnic CAESAR. A jakkoliv to všechno vypadá jako internetové a technologické blouznění, ve skutečnosti taková integrace systémů naplňuje moderní vojenskou zásadu "udeř a zmiz". Co je tam ovšem podstatné, je ono kvalitní spojení. Bez něj by nic takového nefungovalo a bez něj by decentralizace úderu i jeho okamžité a co nejvíce automatizované zadání i vyhodnocení bylo nemyslitelné. To je ten důvod, proč je nyní Starlink považovaný za rozhodující faktor pro moderní válku. Ovšem bacha na to: bez těch houfnic, dělostřelectva, raket, bomb a letadel, by to bylo k ničemu, protože nakonec rozhoduje to, jak dobře palba vyčistí terén, na který se pak přesune pěchota. Bez toho to nejde - v tom je koncepce války neměnná už mnoho století. 

Sláva Ukrajině. 

PS: Rakouská armáda má fajn videokanál, kde rozebírá taktiku na Ukrajině. Pokud umíte základně německy, [dejte si to](https://www.youtube.com/watch?v=QJiuc4KWmQo&list=PL6Udnt8OH5-tuFBuYigic6mYE6_TfCqV7&index=11). 

* * *