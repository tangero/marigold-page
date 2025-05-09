---
categories:
- Procesory
- Technologie
- Ekonomika
excerpt: Už bývám na ten příměr alergický. Na to, jak motýl v Číně mávne křídly a
  v Brazílii je z toho bouře. Ale je to dobrý a srozumitelný příměr o tom, jak provázané
  jsou i vzdálené systémy. Dnes si to ukážeme na příkladu momentálního nedostatku
  mikroprocesorů, což je klíčové téma pro všechny výrobce, od výrobců automobilů,
  až po výrobce spotřební elektroniky.
feature: true
layout: post
summary_points:
- Nedostatek mikroprocesorů omezuje výrobu automobilů.
- TSMC vyrábí většinu procesorů pro automobilový průmysl.
- COVID-19 způsobil nepředvídatelné změny v poptávce.
- Obchodní válka mezi Čínou a USA zvyšuje nejistotu dodávek.
- Americká vláda plánuje řešit nedostatek čipů exekutivním příkazem.
- Evropská unie zvažuje výstavbu špičkové továrny na mikročipy.
- Nedostatek mikroprocesorů bude trvat nejméně
thumbnail: https://mspoweruser.com/wp-content/uploads/2023/01/Intel-Core-processors.jpeg
title: Nedostatek procesorů po mávnutí motýlími křídly
---

Už bývám na ten příměr alergický. Na to, jak motýl v Číně mávne křídly a v Brazílii je z toho bouře. Ale je to dobrý a srozumitelný příměr o tom, jak provázané jsou i vzdálené systémy. Dnes si to ukážeme na příkladu momentálního nedostatku mikroprocesorů, což je klíčové téma pro všechny výrobce, od výrobců automobilů, až po výrobce spotřební elektroniky.

  
_Poznámka: tento článek byl původně součástí mého newsletteru vydaného 21.2.2021, ale stále je důležitý, tak jej uvolňuji veřejně._

Na globálním trhu jsou mikroprocesory a mikrokontrolery pro průmyslové použití všeho druhu momentálně nedostatkovým zbožím. Velké výrobní firmy jako, TMSC, ST nebo Freescale hlásí termíny dodání, takzvané leadtime, v desítkách týdnů, některé rodiny procesorů jsou vyprodané i na dva roky. Koncoví uživatelé zatím situaci nepociťují, protože zboží, ve kterém procesory vidí přímo, se to zatím tolik netýká. Intel má momentálně s výrobou jiné problémy, než nedostatek kapacit, znatelný je problém až u nových procesorů Ryzen od AMD a grafických čipů Nvidia, kde je ale nedostatkovost téměř součástí firemní kultury.  

### Automotive i spotřební průmysl musí omezovat výrobu

Kde je ale dnes problém nejvíce problém viditelný, je automobilový průmysl, takzvaný automotive. Právě procesory pro průmyslové použití, jaké vyrábí Renesas, NXP nebo ST jsou dnes nedostatkovým zbožím a jejich nedostatek ohrožuje výrobu automobilů. Audi, WV, GM, Ford a další, ti všichni omezují výrobu nebo se na omezování výroby připravují, protože čipů prostě není dostatek. Třeba Ford: počátkem února potvrdil, že musí snížit výrobu vozů o 20% a to kvůli nedostatku elektroniky. Objednávky by měl. Na měsíc proto zavírá továrnu v Německu a další omezení chystá. Výpadky autoprůmyslu mají podle odhadů letos znamenat 60 miliard dolarů v propadu obratu.  
  
K čemu automobily mikroprocesory potřebují? Čipy dnes v automobilech řídí všechno, nejde jen o palubní počítače ovládající displeje. Tak třeba takový spalovací motor. V něm se první čipy začaly objevovat koncem sedmdesátých let a s tlakem na zlepšování spalování počty rostou. V sedmdesátých letech měl spalovací motor zpravidla deset čidel vybavených řídícími mikroprocesory, o dvacet let později již více jak třicet. Mikroprocesory řídí vstřikování paliva, snímač polohy klikové hřídele, měřič teploty hlavy válce, chlazení spalovacího motoru, měřič teploty výfukových plynů, spouštěč řízení volnoběhu vzduchu, klepání motoru, snímač absolutního tlaku v potrubí (MAP), snímač hmotnostního průtoku, snímač oxidu dusíku, snímač kyslíku, snímač polohy škrticí klapky a mnoho dalšího. Ještě na přelomu tisíciletí se na ceně spalovacího motoru podílela řídící elektronika necelými dvaceti procenty, dneska tento podíl atakuje čtyřicetiprocentní hranici.  
  
Nicméně nejde jen o automotive průmysl. Například v Prusa Research musíme předělávat připravovaný výrobek, protože procesory pro něj se z týdne na týden staly nedostupné kvůli tomu, že byly vykoupeny technogigantem pro nové zařízení a rozhodnutí výrobce nechat si vybookovat výrobní kapacitu na dlouhou dobu od top firmy bylo zcela pochopitelné. Změna obnáší přepracování desky a i na testovací prototypy procesory kupujeme za pětinásobek původní ceny, přičemž nejbližší další řešení je už varianta nakoupit nejlevnější hotové zařízení, ve kterých procesor je a prostě je pro prototypy vypájet.  
  
Výpadky v dodávkách se dotýkají celého odvětví spotřební elektroniky prakticky plošně a sám Apple musel několikrát posouvat uvedení Airtagů na trh právě kvůli nedostatečným zásobám součástek, tvrdí nepodložené zvěsti. Sony nedodá dostatek Playstation na trh, protože nemá všechny součástky. A to je spotřební průmysl schopen reagovat mnohem pružněji překreslením desek na jiné procesory, zatímco automotive průmysl se kvůli interním certifikacím a spolehlivosti musí přeci jen orientovat na prověřené výrobce a dodavatele.  

### Propojený obor v režimu just-in-time

Co se vlastně stalo a co bylo tím pověstným mávnutím motýlích křídel? Právě na dnešním nedostatku součástek se ukazuje, jak je naše společnost křehká a propojená.  
  
Tak především, mikroprocesory se nevyrábějí na sklad, ale na objednávku, ve vlnách, které trvají několik (typicky 8-10) týdnů. Řada výrobců má na skladě součástky právě jen na dva tři měsíce výroby, aby snižovala kapitálové náklady – ty procesory stojí jednotky dolarů a skladování ve výrobním cyklu by výrobu zdražovalo. Objednávkové vlny v průběhu loňského roku přestaly být předvídatelné, protože na jaře 2020 řada výrobců automobilů i spotřební elektroniky omezovala výrobu. Pak naopak poptávka vlivem COVIDu šla nahoru u jiných zařízení. Lidé chtěli nové počítače, kamery, sluchátka a další věci na homeoffice, naopak se snížil prodej automobilů, změny sice nebyly v desítkách procent, ale na objemy elektroniky šlo o značné změny a přesuny mezi různými typy procesorů.  
  
Dalším problémem je způsob, jakým se mikroprocesory vyrábějí. Ve skutečnosti existuje velmi málo továren, které mikroprocesory vyrábějí a ve většině případů se jejich výroba do jedné z těchto továren outsourcuje. Dominantním hráčem na trhu je taiwanské TSMC, jehož hlavními odběrateli koncem loňského roku byla Nvidia a Apple. Nadpoloviční většina produkce TSMC byly procesory pro chytré telefony, zejména čipy pro Apple, 31% jsou hi-end čipy pro počítače a jen tři procenta pro automotive průmysl. Ještě před rokem byla tato čísla dimenzována odlišně, TSMC se prostě přizpůsobilo změně situace za pandemie. Ono je to logické, koncová prodejní cena procesorů Nvidia je ve stovkách dolarů, zatímco automotive procesory spíše v jednotkách dolarů.  
  
V TSMC přitom většinu svých čipů vyrábí jak Renesas, tak NXP i Infineon, kteří společně drží na trhu automotive mikroprocesorů osmdesátiprocentní podíl. Výrobní továrny TSMC jsou tedy zodpovědné za téměř 70% procesorů pro automobilový průmysl a změna poměrů ve výrobě automotive a hi-end procesory odvětvím zatřásla.  
  
Světová závislost na výrobě procesorů na Taiwanu je fascinující a představuje třetí jádro problému. V posledních měsících totiž Čína stupňuje svou agresi vůči Taiwanu a veřejně se spekuluje o tom, že by jej chtěla obsadit. Ponechme stranou vojenskou stránku akce. Pravda totiž je, že ani Čína, ačkoliv je považována za fabriku světa, není součástkově soběstačná a není schopná vyrábět mikroprocesory nanometrovou technologií, jako TSMC nebo třeba Samsung (tady je  [přehled továren na čipy](https://en.wikipedia.org/wiki/List_of_semiconductor_fabrication_plants)). Přitom pro veškeré vojenské i obchodní operace jsou mikroprocesory dnes klíčovou součástí, bez procesorů se neobejdou dnes ani ty nejhloupější používané bomby, natož nejmodernější rakety a drony. Získání výrobních kapacit je klíčovou podmínkou.  
  
Tak klíčovou, že Čína v průběhu loňského roku  [najala stovku někdejších zaměstnanců TSMC](https://asia.nikkei.com/Business/China-tech/China-hires-over-100-TSMC-engineers-in-push-for-chip-leadership), aby vytvořili nanometrovou výrobní linku v Číně, jenže to potvrá roky – i v Číně. A kdo ví, jak se to podaří. Zrekvírovat stojící fabriky, z nichž každá stojí miliardy dolarů, by situaci značně ulehčilo a také by to ukázalo v probíhající obchodní válce s USA, na čí straně že je vítězství.  
  
Ani USA v procesorové válce nespí. Americká vláda vloni dotlačila TSMC k tomu, aby začala stavět továrnu na mikročipy na americkém území v Arizoně, fabrika má stát dvanáct miliard dolarů a v provozu má být v roce 2024. Mimochodem to zařídil pomlouvaný Trump: považoval to za důležitou strategickou součást hospodářsko-vojenské schopnosti USA obstát v moderním světě. Právem. Dnes se v USA vyrábí 13% procesorů, neplatí tedy dosti rozšířený předpoklad, že výroba procesorů se z USA zcela stáhla. Své velké a moderní továrny zde má Intel,  [GloFo](https://en.wikipedia.org/wiki/GlobalFoundries)  či TI, pravdou ale také je, že podíl 37%, jaký USA držely v roce 1990, je dnes jen snem. Více o významu čipů pro „národní bezpečnost“ [v USA Today](https://eu.usatoday.com/story/tech/columnist/2020/07/30/why-semiconductor-chip-making-based-u-s-critical/5536083002/).  
  
Čína mezi tím své výrobní kapacity zdvihla z osmiprocentního podílu v roce 2015 na dnešních 12 procent a stále posiluje. Například již dnes je téměř jisté, že TSMC přijde o výrobu čipů pro mobilní telefony Huawei kvůli americkému embargu,  [vyrábět je bude čínská SMIC](https://www.androidheadlines.com/2020/11/huawei-chip-manufacturing-factory-shanghai-US.html). A tím se dostáváme k obchodní válce mezi Čínou a USA, která je dalším faktorem. Amerika se snaží limitovat moderní technologie dostupné Číně a tím výrazně ohrožuje schopnost čínského průmyslu produkovat hi-tech technologie, nejenom ty vojenské, ale i civilní, kde se nepokrytě jde po náskoku Číny v budování mobilních sítí páté generace 5G.  
  
Tato  **obchodní válka Číny s USA prohlubuje nejistotu a pochybnost**, jak to bude s Tchajwanem a jeho produkcí. Pokud by vypadla, například v důsledku čínské invaze, do řady průmyslových odvětví spojených s elektronikou, by to přineslo dominový efekt.  
  
Za čtvrté Čína v rámci obchodní války s USA veřejně uvažuje o limitování vývozu kovů vzácných zemin, čímž by byla postižena výroba americké vojenské techniky. Kovy vzácných zemin má Čína pod palcem z 80%, dalším solidním producentem je jen Austrálie a proto se USA snaží Austrálii pomoct v její vlastní obchodní válce s Čínou, mimo jiné i investicemi do místních dolů. Bez těchto kovů nebudou létat americké F-35, z nichž každá spotřebuje přes 400 kg na motory, elektroniku a další součásti. Amerických F-35 se přitom Čína významně bojí a snaží se dělat všechno proto, aby jejich vývoz do „vzbouřenecké provincie“ zarazila. Pro případnou dovolenkovou akci čínských vojáků by měla přítomnost F-35 ve vzdušném prostoru neblahé důsledky.  
  
Co dalšího se změnilo? Svět si zamiloval elektromobily, ty potřebují více elektroniky, jenže jiné, než ty spalovací. Místo jednoduchých senzorů jde o komplexní výpočty, větší procesory, také s větší marží – a i to limituje ochotu firem produkovat levné automotive procesory.  
  
Dalšími faktory jsou probíhající změny a akvizice v elektronickém průmyslu. Nejde jen o ty velké, viditelné, jako byl nákup ARMu firmou Nvidia za 40 miliard dolarů, které teprve jisté restrukturalizace přináší, jde především o ty méně viditelné. V únoru byl  [potvrzen nákup kontrolního balíku akcií](https://www.reuters.com/article/siltronic-ma-globalwafers-idUSL8N2KF3UF)  v předním výrobci  [waferů](https://cs.wikipedia.org/wiki/Wafer), německého Siltronicu taiwanskou firmou GlobalWafer. Wafery jsou pláty užívané pro výrobu čipů a Siltronic patří mezi nejlepší výrobce nejkvalitnějších plátů a předního hráče. Spojením s GlobalWafer tak vznikne dvojka na trhu, po japonské Shin-Etsu, jenže tím se také posiluje taiwanská pozice na křemíkovém poli a mění rovnováha na globálním mikorprocesorovém hřišti, neboť GlobalWafer nemusí být ochotna dodávat primární výrobní wafery nepřátelsky naladěným státům v rámci obchodní války se vzbouřeneckou provincií…  
  
Následkem výše uvedených bodů se firmy snaží předzásobit, do obchodů vstupují různí spekulanti a situace je pro všechny poněkud nepřehledná a stresující.

###   Očekává se exekutivní příkaz amerického prezidenta Bidena

Záležitost je tak naléhavá, že do ní vstoupil americký prezident Joe Biden, začátkem února, tedy jen krátce po uvedení do funkce. Po schůzce s šéfem Qualcommu, Corningu a dalších firem v oboru se na prezidenta oficiálně obrátila i americká Asociace polovodičového průmyslu zastupující třeba Intel, IBM nebo AMD s urgentním dopisem. Očekává se, že  [Biden v nejbližší době pověří exekutivním příkazem](https://www.cnbc.com/2021/02/18/biden-to-order-supply-chain-review-to-assess-us-reliance-on-overseas-semiconductors.html)  své týmy a průmysl, aby prověřili možnosti a našli cestu z nedostatku polovodičových součástek a dalšího kritického zboží.  
I pokud se tak stane (a už je to vcelku jisté), situace se nezlepší před druhým pololetím letošního roku, velmi pravděpodobně do jeho konce. Stavba nových továren není hned, na druhou stranu restrukturalizace výroby procesorů s americkou podporou možná je. Do astronomických výšin již vyletěly ceny „bazarových“ výrobních linek určené pro sto-nanometrové mikroprocesorové technologie, jak se nejrůznější firmy snaží oživit alespoň ty starší technologie – na řadu procesorů to stačí, není třeba hned konkurovat nejlepším postupům TSMC.

###   EU také bojuje za euro-čipy

Také pro evropský průmysl má přístup k mikročipům klíčový význam. Evropská unie, povzbuzována firmami jako Volkswagen, uvažuje o podpoře výstavby špičkové mikroprocesorové továrny, která by disponovala výrobní technologií pod 10 nanometrů, tedy jednu z nejlepších dostupných technologií. Pomoct by jí s tím mohlo TSMC nebo Samsung, tedy firmy, které tuto výrobní technologii mají zvládnutou. Zatím ale není nic potvrzeno, ani formát eurounijní podpory, snad jen ty důvody, které jsou velmi podobné důvodům americkým.  
V každém případě bude nedostatek mikroprocesorů letos značně komplikovat situaci výrobcům a tím i tlačit ceny nahoru. A situace nemá ani rychlé, ani jednoduché řešení.

Koncem května 2021 odhaduje šéf IBM, že nedostatek potrvá „roky“, Apple v interních odhadech nepředpokládá, že nedostatek procesorů skončí dříve, jak za osmnáct měsíců.