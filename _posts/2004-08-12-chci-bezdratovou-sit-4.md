---
ID: 1247
title: Chci bezdrátovou síť! (4)
author: Noname
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/chci-bezdratovou-sit-4
published: true
post_date: 2004-08-12 16:30:36
---
	<div class="rightbox"><img src="/wp-content/uploads/cache/20040812-PtMP diagram.jpg" alt="Zobrazení venkovní PtMP sítě" width="204" height="200" /></div><p>
V minulém díle jsme se věnovali hot-spotům, a hlavně jsme konečně začali probírat jednotlivé typy bezdrátových sítí, co potřebujete k jejich vytvoření a kolik vás to bude stát. Minule jsme zvládli jen interní sítě, dnes se vrhneme na venkovní sítě.</p>

<h3>3. Venkovní sítě</h3>
<p>
V první řadě vysvětlím, co si představuji pod pojmem venkovní bezdrátová síť. Jedná se o propojení dvou a více počítačů (či sítí), které nejsou umístěny v jednom objektu (patře), ale jsou od sebe vzdáleny typicky stovky metrů až jednotky kilometrů a typickým znakem je venkovní anténa. V této sekci tedy nebudu probírat řešení „počítač doma, notebook na zahrádce&#8221;, vysvětlili jsme si jej v předchozí kapitole. Nemyslím tím ani sítě typu GPS, GSM a podobně. A pozor - v této kapitole <strong>nebudu</strong> probírat klasické bezdrátové připojení k internetu (jen jako vedlejší část), mírně se totiž od propojení sítí liší, nicméně základ je velmi podobný - na zájemce o bezdrátový internet se dostane zítra.</p>
<p>
<em>Poznámka: omlouvám se za pozdější uvedení tohoto dílu - jak pochopíte po otevření článku - trvalo mi napsání tohoto dílu přes deset hodin. Tím se omlouvám také za délku článku, měl jsem cukání jej rozdělit do dvou, ale to už byste mě ukamenovali ;-). V článku se míchá řešení pro profi sítě i pro řešení sousedské sítě, technologie spolu totiž souvisí, tak se v tom snad neztratíte.</em></p>

<!--more--><p>
Jaké je tedy využití bezdrátových venkovních sítí? Proberme typické příklady:</p>

<ul>
<li><strong>Firma Marigold</strong> má svou pobočku <u>na dohled</u>, <u>pár set metrů daleko</u>, ráda by propojila <u>sítě</u>, aby všichni zaměstnanci byli členové jedné workgroupy (viděli se v okolních počítačích) a aby <u>nemuseli pronajímat </u>do každé budovy drahé <u>připojení k internetu</u>. Variantní řešení - to samé ale ještě navíc propojit svou <u>telefonní ústřednu</u>, aby bylo volání mezi centrálou a pobočkou zdarma</li>
<li><strong>Firma Geralt </strong>má takové pobočky <u>dvě</u> a ještě má pár <u>zaměstnanců</u>, kteří by mohli pracovat půlku týdne z domova a tak by <u>ušetřila za prostory</u>, čas atd.</li>
<li><strong>Pepa Novák</strong> má kamaráda <strong>Honzu</strong>, se kterým by rád <u>pařil po síti hry</u>, kamarád je ale bohužel v protějším baráku. Výhodou by byla možnost využít Honzova <u>připojení k internetu</u>, o náklady by se <u>podělili</u>.</li>
<li><strong>Lojzovi </strong>se jejich nápad strašně líbí, chtěl by se propojit s nima (<u>vidí na Pepu</u>), rád by se připojil i <strong>Pavel</strong>, který ale <u>vidí jen na Lojzu</u>.</li>
</ul>
<p>
To jsou typické scénáře, samozřejmě je zde nekonečno možných variant, ale jistě časem poznáte sami jak na ně. Teď ale mírně odbočím od řešení těchto scénářů a vysvětlím vše důležité okolo.</p>
<div class="rightbox"><img src="/wp-content/uploads/cache/20040812-PtMP.jpg" alt="PtMP" width="232" height="184" /></div><div class="leftbox"><img src="/wp-content/uploads/cache/20040812-PtP.jpg" alt="PtP" width="146" height="186" /></div>
<h4>Topologie sítě</h4>
<p>
U bezdrátových sítí existují dvě základní fyzické topologie sítě - <strong><u>PtP</u></strong> (Point-to-Point - dvoubodový spoj) a <strong><u>PtMP</u></strong> (Point-to-Multipoint - jeden na všechny, řešení typu hvězda). Pak jsou různé hybridy (poslední příklad), případně i řešení <strong>PtP jde řešit v podstatě jako PtMP s jedním klientem</strong>.</p>

<h4>Viditelnost</h4>
<p>
Několikrát jsem v uvedených scénářích naťuknul téma „viditelnost&#8221;. <strong>Pro bezdrátové sítě je totiž velmi důležité, aby oba body (PtP) na sebe viděly, respektive (PtMP) aby všichni klienti viděli na centrální bod</strong>. Tím „viděním&#8221; je myšleno nejen, že pouhým okem (dalekohledem) vidíte z místa, kde by byla umístěna anténa jednoho klienta na místo antény druhého, ale je to složitější.</p>
<p>
Radiové vlny se totiž nešíří jako laserový paprsek, vyzařovací schéma je podobné ragbyovému míči (viz obrázek), směrem do středu se zóna rozšiřuje a je to přísně dáno fyzikálními zákony. V této zóně by pokud možno neměly být žádné překážky - budovy, stromy a podobně (rapidně klesá dosah).</p>
<div class="rightbox"><img src="/wp-content/uploads/cache/20040812-fresnel.jpg" alt="Fresnelova zóna" width="227" height="90" /></div><p>
<em>Tato zóna šíření se nazývá <strong>Fresnelova</strong> (čte se prý Frenelova) zóna (FZ). Je jich více, nejdůležitější je pro nás 60% z první FZ. Výpočet je relativně jednoduchý poloměr toho míče, a tedy nejvyšší vzdálenost (v metrech) mezi středem a krajem je 60%×17.3×odmocnina(D/4f) kde D je vzdálenost v km, f je frekvence v GHz. Tohle samozřejmě nemusíte znát, ale měli byste mít představu - na frekvenci používanou 802.11b (2,4 GHz) je to vychází:</em></p>

<ul>
<li><em>1 km <strong>3,4m</strong> 60% 1. FZ 0,6×17,3×ODMOCNINA(1/(4×2,4))</em></li>
<li><em>2 km <strong>4,7m</strong> 60% 1. FZ 0,6×17,3×ODMOCNINA(2/(4×2,4))</em></li>
<li><em>3 km <strong>5,8m</strong> 60% 1. FZ 0,6×17,3×ODMOCNINA(3/(4×2,4))</em></li>
<li><em>4 km <strong>6,7m</strong> 60% 1. FZ 0,6×17,3×ODMOCNINA(4/(4×2,4))</em></li>
<li><em>5 km <strong>7,5m</strong> 60% 1. FZ 0,6×17,3×ODMOCNINA(5/(4×2,4))</em></li>
</ul>
<p>
Tedy na 1 km spoj potřebujete zajistit, aby bylo vidět na protější bod a aby bylo ještě minimálně 3,4 metrů okolo volno (experti prominou mírné zjednodušování v zájmu čtenářstva). Obecně vzato čím více tím lépe (to není zcela pravda, překážky v sudých FZ jsou pozitivní, ale to už jsme trochu jinde).</p>
<p>
Jestliže to splňujete jen částečně, můžete to také vyzkoušet, lepší je ale např. dát anténu výš (na stožár) tak aby byla 1. FZ tak jak má být. Když opravdu přímá viditelnost není, nejjednodušší řešení je retranslace (zítra).</p>

<h4>Technické řešení</h4>
<p>
Malinko jsem už zabrousil k vlastní instalaci, zde je čas na důležitou poznámku - <strong>výstavba venkovních sítí není zcela jednoduchá</strong>, firma musí na takové instalace mít povolení od majitele domu a někdy i stavebního úřadu,  techniky školené na výškové práce, školení na silnoproud, na hromosvody atd.</p>
<p>
Domnívám se, že <strong><u>svépomocí by si to měl řešit maximálně jedinec na svém baráčku</u></strong>, jinak byste to měli nechat někomu s papíry. Neodborná instalace může znamenat zranění, zničení střechy či opláštění budovy, pokuty od stavebního úřadu, zničení ochranné funkce hromosvodů a potažmo zodpovědnost za případné vyhoření atd.</p>

<h4>Profesionalita</h4>
<p>
S tím souvisí samozřejmě profesionalita provedení a výsledná kvalita řešení (<u>spolehlivost</u>), vyšší nároky na ní budou mít zřejmě firmy v prvních dvou příkladech. Navíc - jestliže tyto firmy toto řešení koupí od dodavatele/operátora, který jim zároveň dodává např. internet a/nebo hlas, potom cena této instalace je samozřejmě v ceně a vyplatí se tak plánovat takové akce najednou. Ve finále může firma <strong>šetřit už od prvního dne</strong>, přechodem na jiného operátora se jim ani nemusí změnit telefonní čísla (number portability).</p>

<h4>Výběr technologie</h4>
<p>
S požadavky na profesionalitu řešení také vyvstává otázka výběru technologie. Jak jsem psal - řešení venkovních sítí dle standardů 802.11 pro vnitřní sítě je řešení krajně neprofesionální. Je ale nejlevnější. Pro firmu, která ale ztrácí miliony za hodinu, když by vypadlo spojení mezi jejich pobočkami, či když by se jim do toho někdo naboural, je to většinou volba nešťastná. Když si Pepa s Honzou jeden den nezahrají, tak se nic nestane, naopak budou mít čas zajít si na pivo ;-)</p>
<p>
<strong>Možná řešení se rozdělují</strong>:</p>

<ol>
<li><strong><u>podle topologie</u></strong> - dvoubodové (PtP) a vícebodové (PtMP). Dvoubodové spoje jsou obecně lepší z hlediska bezpečnosti (jste tam jenom vy dva a nikdo jiný se nemůže připojit), mívají větší kapacitu, bývají full-duplexní (přenášejí najednou v obou směrech). Pro přenos hlasu jsou PtMP systémy řádově dražší, pro přenos pouhých dat tomu bývá naopak.</li>
<li><strong><u>podle technolologie</u></strong> - radiové v bezlicenčním pásmu (2,4 GHz, 5,8 GHz, u PtP pak 10,5 GHz), v licenčních pásmech (3,5 GHz, 26 GHz, u PtP pak různé frekvence od 18 - 38 GHz) a nesmíme zapomínat u PtP spojů ani na optická (laserová) pojítka</li>
<li><strong><u>podle plánovaných služeb</u></strong> - potřebujete propojení analogových ústředen (G703)? Potřebujete přenášet čistě data? Nebo chcete kombinaci? A nebo je to jen na internet a stačí malá propustnost, ale je třeba hodně klientů?</li>
<li><strong><u>podle „profesionality&#8221;</u></strong> - tj. ceny, spolehlivosti atd.</li>
</ol>
<p>
První co tedy musíte vybrat je <strong><u>topologie</u></strong>, a není to tak úplně jednoduché jak se na první pohled zdá:</p>

<ul>
<li>Firma Marigold zřejmě podle popisu potřebuje řešení <strong>PtP</strong>. Ale co když bude chtít za rok připojit i druhou pobočku? Z PtP systémů na PtMP nejde nějak „upgradovat&#8221;, buď musíte koupit další PtP linku, tj. z jedné střechy budete koukat na dva směry, nebo musíte PtP „vyhodit&#8221; (prodat či použít jinde) a přejít na PtMP.</li>
<li>Firma Geralt podle popisu může chtít <strong>PtMP</strong> řešení, ale může se z důvodů kapacity a bezpečnosti rozhodnout připojit každou pobočku zvlášť PtP spojem (zejména jestli chtějí i propojit ústředny) a zaměstnance připojit levným <strong>PtMP</strong>.</li>
<li>Pepa s Honzou nejspíše z důvodu ceny využíjí <strong>levné PtMP</strong>, umožní jim to v budoucnu připojit i Lojzu (a obezličkou - viz dále) i Pavla.</li>
</ul>
<p>
Podle <strong><u>technologie</u></strong> to bývá jednodušší - když budou totiž něco kupovat zmíněné firmy, obrátí se na partnery a ty jim řeknou co je u nich možné. Domácí uživatelé zase téměř vždy sáhnou po Wi-Fi.</p>
<p>
Podle služeb je to také snadné, to víte předem. Jenom upozorňuji, že přenos IP hlasu je z tohoto pohledu brán jako přenos dat, nicméně pro něj je důležitá <strong>spolehlivost</strong> (zpoždění, jitter). Nemá-li ještě firma koupena ústřednu (či má starší typ), může <strong>ušetřit i miliony</strong> (a získat mnohé neběžné funkce) tím, že si ji <a href="http://www.contactel.cz/contactel_forum/profil.htm">vůbec nekoupí, ale pronajme u operátora</a>.</p>
<p>
A opět <strong>profesionalita</strong> a <strong>cena</strong> jdou ruku v ruce s profesionalitou zákazníka a jeho potřebami a závislosti na zvoleném řešení. Možnostem se budeme věnovat za chvíli.</p>

<h4>Cenové kalkulace</h4>
<p>
Tyto všechny kalkulace budou hodně orientační - pro venkovní instalace totiž záleží na místních podmínkách, jaké použijete antény, stožáry, zda-li pořídíte rozvaděč atd.</p>
<p>
<em>Situace 1. Firma Marigold má svou pobočku na dohled, pár set metrů daleko, ráda by propojila sítě, aby všichni zaměstnanci byli členové jedné workgroupy (viděli se v okolních počítačích) a aby nemuseli pronajímat do každé firmy drahé připojení k internetu. Variantní řešení - to samé ale ještě navíc propojit svou telefonní ústřednu, aby bylo volání mezi centrálou a pobočkou zdarma</em></p>

<ul>
<li><strong><u>Doporučené řešení</u></strong> - obraťte se na dodavatele internetu či poskytovatele hlasu, případně udělejte výběrové řízení pro výběr nového společného poskytovatele těchto služeb. Tato firma vám no nainstaluje a bude se vám starat o nutnou údržbu - když vy byste poslali na střechu nějakého svého zaměstnance bez potřebných certifikátů, tak si koledujete o kriminál. Navíc řešení přes operátora může být i levnější (nebo alespoň nemusí vyjít dráž - tento operátor nakupuje u dodavatelů někdy i o desítky procent levněji než byste koupil něco vy (větší objem) a se jeho více náklady v tomto schovají.<br/>Jde-li vám ale čistě o propojení poboček, bývá výhodně než na ISP/Telco <strong>obrátit se přímo na firmy, které se zabývají montáží</strong> (i pro ty ISP/Telco) - <a href="http://www.vanco.cz/">Vanco</a>, <a href="http://www.coprosys.cz/">Coprosys</a>, <a href="http://www.ges.cz/">GES</a>, &#8230;</li>
<li>Možné technologie jsou tedy <strong>PtP</strong> spoje, firma by měla sáhnout po řešení <strong>v licencovaných pásmech</strong>, nebo alespoň <strong>10,5 GHz</strong>, kde není tak rušno. Pro nižší záruku, ale podstatně nižší cenu lze doporučit i PtP v pásmu <strong>5,8 GHz.</strong> Na krátké vzdálenosti vychází velmi zajímavě i řešení pomocí <strong>optických pojítek</strong>.</li>
<div class="rightbox"><img src="/wp-content/uploads/cache/20040812-nera.jpg" alt="Nera Wireless" width="127" height="137" /></div>
<ul>
<li><strong><u>Řešení v licencovaných pásmech</u></strong> nabízí rychlosti v řádech megabitů až 155 megabit Full-Duplex, včetně i G703 portů (analogová telefonie), dosah je až několik desítek kilometrů. Ceny se pohybují od 400 tisíc do 2 milionů, ročně pak platíte 10-100 tisíc ČTÚ za pronájem frekvence. Výrobce (<a href="http://www.nera.no/">Nera</a>, <a href="http://www.siemens.com/">Siemens</a>, <a href="http://www.ericsson.com/">Ericsson</a>) vám pomůže vybrat montážní firma</li>
<li><strong><u>Propojení v pásmu 10,5 GHz</u></strong> nabízí rychlosti 2-10 Mbit Full-Duplex, nabízí i hlasové porty. Tato frekvence je volná jen v ČR (do roku 2010), dosah je max. cca. 30 km. Ceny začínají na cca. 200 tisících včetně montáže, výrobce (<a href="http://www.svm.cz/">SVM</a>, <a href="http://www.conves.cz/">Conves</a>, <a href="http://www.miracle.cz/">Miracle</a>, &#8230;) vám opět poradí montážní firma.</li>
<li><strong><u>PtP produkty pro pásmo 5,8 GHz</u></strong> nabízí rychlosti od 2 do 1000 Mbit, Full i Half Duplex, některé typy mají i možnost G703 portů, dosah se kvůli výraznému omezení vyzářeného výkonu v ČR pohybuje mezi stovkami metrů a 2 km. Ceny se pohybují od 50 tisíc do 1,5 milionu Kč. Koncem roku by mělo být povolen vyšší vyzářený výkon na podobné frekvenci a je tedy pravděpodobné, že příští rok budou na trhu i jiné produkty s vyššími dosahy a příznivějšími cenami. Výrobci <a href="http://www.proxim.com/">Proxim</a>, <a href="http://www.alvarion.com/">Alvarion</a>, <a href="http://www.trangobroadband.com/">Trango</a>, <a href="http://www.motorola.com/">Motorola</a>&#8230;)</li>
<li>Často zapomínaná technologie jsou <strong>optická pojítka</strong>, nabízejí rychlosti od 10 do 1000 Mbit (některá nabízí i analogové porty), dosah je od 150 metrů do 5 kilometrů. Ceny začínají už na 40 tisících a končí na cca. 1 milionu.  Pro zajímavost, <a href="http://www.laserbit.net/products.php?pname=PICO">100 Mbit Full Duplex Ethernet laserové pojítko na 150 metrů v profi provedení</a> se dá sehnat u <a href="http://www.anixter.cz/">distributora</a> za 40 tisíc plus daň. Výrobci <a href="http://www.laserbit.net/">LaserBit</a>, <a href="http://www.cbl.cz/">CBL</a> &#8230;</li>
</ul>
</ul>
<p>
<em>Sitace 2. Firma Geralt má takové pobočky dvě a ještě má pár zaměstnanců, kteří by mohli pracovat půlku týdne z domova a tak by ušetřila za prostory, čas atd.</em></p>

<ul>
<li>Tato firma by se opět měla <strong>obrátit na montážní firmu</strong>, která to udělá. U dvou poboček může být ještě stále zajímavé využít <strong>2× PtP linku</strong> s pobočkami a pro připojení zaměstnanců využít <strong>PtMP</strong> řešení ať už přes Wi-Fi či v pásmu 5,8 GHz. U více poboček pak je důležité, jestli opravdu všechny na sebe vidí, jak jsou daleko a jestli je potřeba i hlas, potom by se mohla zvážit nějaká kvalitní PtMP technologie, zřejmě v pásmu 5,8 GHz (případně licencované 3,5 GHz pásmo, jestli je to v daném místě možné - poradí montážní firma).</li>
<ul>
<li>Řešení <strong>PtP</strong> spoje by bylo tedy stejné jako v předchozí situaci, jen by byly 2 (každý může být samozřejmě řešen jinak, dle potřeb konkrétní pobočky, vzdálenosti apod.)</li>
<li>Levnější bude <strong>PtMP řešení v pásmu 5,8 GHz</strong>. Rychlosti jsou od 64 kbit po 30 Mbit, dosahy jsou v tuto chvíli do max. 2 km. Ceny se pohybují mezi 30-70 tisíci za přístupový bod včetně antény, od 10 tisíc Kč výše za hardware pro domácího uživatele, 20-30 tisíc Kč za techniku pro připojení kanceláře. Propojení ústředen pomocí G703 ale není možné.</li>
<li>Existuje i <strong>PtMP pro pásmo 2,4 GHz</strong>, které nabízí podobné možnosti jako předchozí skupina, za ceny přibližně stejné, výhodou je větší dosah (max. 5 km legálně), nevýhodou podstatně větší rušení v tomto pásmu.</li>
<li>Může být zajímavé připojit pobočky pomocí dražší technologie (PtMP či PtP), a pro zaměstnance zřídit zvláštní přístupový bod, např. i Wi-Fi (řešení viz Pepa s Honzou)</li>
</ul>
</ul>
<p>
<em>Situace 3. Pepa Novák má kamaráda Honzu, se kterým by rád pařil po síti hry, kamarád je ale bohužel v protějším baráku. Výhodou by byla možnost využít Honzova připojení k internetu, o náklady by se podělili.</em></p>

<ul>
<li>Tohle je asi konečně něco, co zajímá větší část čtenářů (omlouvám se za zdlouhavý „úvod&#8221;), ale myslím, že stojí za to znát všechny možnosti.</li>
<li>Samozřejmě v těchto situacích bývá <strong>nejdůležitějším kritériem cena</strong>, proto se zřejmě rozhodnou pro Wi-Fi propojení (PtMP s jedním klientem), umožní jim to pak připojit i další kamarády. Kdyby ale pro nějakou fakt hustou hru potřebovali full-duplex stomegabit, nejzajímavější by asi pak bylo řešení pomocí výše uvedeného optického pojítka.</li>
<li>Jsou-li oba kluci opravdu kousek od sebe (100m) a perfektně si vidí okna u svých počítačů, potom stačí, když oba koupí nějakou USB síťovou kartu a dají ji na okno (tj. Ad-hoc síť), pozor ale na bezpečnost, opět bych doporučoval na jednu stranu dát AP (např. onen včera zmíněný <a href="http://www.wifishop.cz/inshop/shop.asp?ItemID=20990">Asus WL-330</a>)</li>
<li>Složitější je to ale, budete-li potřebovat anténu (dosah potom až cca. 5 km při splnění povolení), potom totiž musíte do svého rozhodování o vhodném prvku započítat i to, zda-li má možnost připojení externí antény. USB zařízení s výstupem na externí anténu jsou totiž zbytečně drahé, výhodnější tedy je jít do <a href="http://www.wifishop.cz/inshop/shop.asp?Level=76">PCI karet</a> nebo to externího <a href="http://www.wifishop.cz/inshop/shop.asp?Level=79">Ethernetového klienta</a>.</li>
<ul>
<li><strong><u>Doporučený typ PCI</u></strong>: <a href="http://www.wifishop.cz/inshop/shop.asp?ItemID=21140">Zyxel ZyAIR B-320</a> - funguje i na starších počítačích s PCI verze 2.1, příznivá cena 918 Kč vč. DPH. Konektor RSMA</li>
<li>Nebo můžete využít <strong><u>akční nabídky</u></strong> - balíčku karty D-Link DWL 510, 8 dBi směrové antény (dvě proti sobě stačí tak na 0,5-1 km link) a 3m propojovacího kabelu, <a href="http://www.wifishop.cz/inshop/shop.asp?ItemID=21055">dohromady za 2090 Kč s DPH</a>, tj. asi o 500 Kč levněji, než když byste to kupovali zvlášť.</li>
<li><strong><u>Doporučený typ Ethernet klient</u></strong>: zcela jasně <a href="http://www.wifishop.cz/inshop/shop.asp?ItemID=21091">OvisLink WL-1120</a> - je totiž nejlevnější (1831 Kč s DPH), ale hlavně funguje nejen jako klient pro 1 počítač (na to pozor u jiných ethernet klientů), ale můžete za něj <strong>připojit i síť</strong>, může fungovat i jako <strong>AP</strong> a podporuje <strong>WDS</strong> (viz dále). Má <strong>dva Ethernet porty</strong>, jeden můžete připojit tedy třeba do DSL routeru, ke druhému připojit svůj počítač a na bezdrát pak kamarády. Konektor RSMA</li>
<li><strong><u>Doporučený přístupový bod</u></strong>: opět bych šel do uvedeného <a href="http://www.wifishop.cz/inshop/shop.asp?ItemID=21091">OvisLinku 1120</a>. Existuje sice o 100 Kč levnější D-Link DWL-700, ale půlka jich u mě končila reklamovaných a nepodporuje WDS - never more.</li>
</ul>
<li><strong><u>Toto nejsou ale konečné náklady</u></strong> (vyjma případu koupě akčního balíčku) - ještě je třeba koupit propojovací kabel (stovková položka) a hlavně vybrat anténu. Anténám se budeme věnovat v příštím díle (už takhle je tento strašně dlouhý). Další položky mohou být bleskojistky, stožáry, koaxiální kabely, rozvaděče, prodlužovačky atd.</li>
</ul>
<div class="leftbox"><img src="/wp-content/uploads/cache/20040812-thumbsup.jpg" alt="Lojza má fakt radost!" width="171" height="256" /></div><p>
<em>Situace 4. Lojzovi se jejich nápad strašně líbí, chtěl by se propojit s nima (vidí na Pepu), rád by se připojil i Pavel, který ale vidí jen na Lojzu.</em></p>
<p>
Tohle je mírně netradiční řešení, nicméně zejména proto, že o něm mnoho lidí neví a chtěl bych na něm i ukázat, k čemu se může hodit WDS.</p>
<p>
<em><strong>WDS </strong>- Wireless Distribution Systém - fičura, která umožňuje propojování až 6 přístupových bodů bezdrátově mezi sebou na jednom kanále s klienty. Už jsme si totiž řekli, že u 802.11b je možný buď bod Infrastructure (AP vůči klientům) nebo Ad-hoc (klient vůči klientovi), ale až do nástupu WDS nebylo možné <strong>propojit AP mezi sebou</strong>. Takhle můžete mít AP (s WDS), na něj napojeno 5 jiných AP (s WDS), a na ně třeba zase připojené další AP (s WDS) a na každý z těch AP mít připojené ještě klienty. Velmi výrazně se sice zhoršuje propustnost, ale pro domácí uživatele a případ jako tento je tato fičura ideální.</em></p>

<ul>
<li>Řešení bude jednoduché - Lojza a Pepa budou mít AP s podporou WDS - doporučuji už dvakrát zmíněný <a href="http://www.wifishop.cz/inshop/shop.asp?ItemID=21091">OvisLink 1120</a>. Nastaví se mezi nimi WDS spojení. Na Pepu se pak bude připojovat ještě Honza (pomocí kteréhokoliv klienta viz výše), na Lojzu se bude připojovat Pavel (opět pomocí kteréhokoliv klienta). Lojza jen bude muset zajistit, aby jeho anténa „koukala&#8221; jak na Pepu, tak na Pavla - buď všesměrovkou, nebo může pomocí anténního rozbočovače/slučovače připojit k AP dvě antény.</li>
</ul>