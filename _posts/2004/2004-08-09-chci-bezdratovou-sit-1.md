---
ID: 1241
author: Noname
layout: post
oldlink: 'https://www.marigold.cz/item/chci-bezdratovou-sit-1

  '
post_date: 2004-08-09 21:41:36
post_excerpt: ''
published: true
summary_points:
- Wi-Fi sítě zažívají boom, článek je příručka pro laiky.
- NCR WaveLAN v roce 1993 byla první komerční Wi-Fi technologie.
- Standard 802.11b z roku 1999 přinesl rychlost 11 Mb/s a Wi-Fi certifikaci.
- Standardy 802.11a/g/h přinesly vyšší rychlosti a řešily regionální omezení.
title: Chci bezdrátovou síť! (1)
---

<div class="rightbox"><img src="/wp-content/uploads/cache/20040809-Wi-Fi Zone.jpg" alt="Wi-Fi Zone" width="203" height="152" /></div><p>
Bezdráty (Wi-Fi zejména) zažívají v poslední době ohromný &#8220;boom&#8221;, respektive ty, používány v komunitních sítích (více Patrikův článek &#8220;<a href="/item/veru-nevim-jak-bude-cesky-telecom-celit-lavine-komunitnich-siti">Věru nevím, jak bude Český Telecom čelit lavině komunitních sítí</a>&#8221;).</p>
<p>
S tím jak se bezdrátové sítě rozšiřují, setkávám se s tím, že se o nich dozvěděli a ptají se na ně i ti, kteří se jinak &#8220;moc nevyznají&#8221;. Proto jsem připravil nejen pro ně jakousi příručku &#8220;co to je&#8221; a &#8220;jak na to&#8221;, ale začnu raději hodně zeširoka a ne jen běžné &#8220;kupte A, B, C a dejte to na střechu&#8221;.</p>
<p>
Popis bude několikadílný, ještě nemám všechny díly připraveny, nicméně plán je to dopublikovat vše tento týden, potom leda případné náměty z publika. První kapitola je zahřívací (ale velmi důležitá pro pochopení i dalších kapitol) a jmenuje se Historie.</p>

<!--more--><p>
<em>Bezdrátová síť je obecně libovolná počítačová síť, kde je místo kabelů použita technologie, která kabely nevyžaduje (wire less). Přesnějšímu popisu se budu věnovat později, začnu ale historií.</em></p>

<h3>1. Historie</h3>
<p>
Bezdrátové sítě pro běžný trh existují v podstatě od května &#8216;93, kdy firma NCR (tehdejší součást gigantu AT&amp;T) uvedla na trh svou WaveLAN (I) technologii. Tato technologie nabízela byla čistě proprietární (žádný standard nebyl), nabízel rychlosti max. 2 Mb/s, přístupový bod (WavePOINT I) stál baťovku - 1995$, PC karta stála 695$ (dolar byl tehdy za 29 Kč) - máte-li zájem, pár bych jich možná ještě sehnal ;-). Už tehdy využívaly pásmo 2,4 GHz (jediné celosvětově bezlicenční), v Americe pak ještě pásmo 900 MHz.</p>
<p>
Téhož roku se také začalo pracovat na standardizaci bezdrátových sítí pod patronací organizace <a href="http://www.ieee.org/">IEEE</a> (AT&amp;T a zejména její Bellovy laboratoře byli a stále jsou nejmocnější skupinou v této organizaci), první standard byl hotov ale až v červenci roku 1997 a dostal název <a href="http://grouper.ieee.org/groups/802/11/main.html">IEEE 802.11</a>. Tento standard definoval tři různé fyzické vrstvy a společnou MAC vrstvu.</p>
<p>
První fyzická možnost bezdrátového přenosu bylo řešení pomocí DfIR (diffuse infrared) - rozprostřeného infračerveného světla (tj. nebylo třeba nastavení vysílače přesně na vysílač, signál se šířil všude okolo, dosah byl jednotky metrů, max. rychlost 2 Mb/s. Tento standard se ale vůbec neujal (výrobky by se daly AFAIK spočítat na prstech jedné ruky).</p>
<p>
Další dvě metody využívaly radiových vln rozprostřených v pásmu 2,4-2,472 GHz, jedna používala metodu rozprostření pomocí přímé sekvence (DSSS - signál je navzorkován na 20 MHz úsek, který je využíván a nemění se), druhá využívala řešení frekvenčních přeskoků (FHSS celé 70 MHz pásmo je rozděleno na 1 MHz kanály, frekvence jednotky pseudonáhodně &#8220;přeskakuje&#8221; po pár milisekundách po těchto kanálech). U nás byly v tu dobu nejznámější WaveLANy (tehdy už Lucent, pohrobek původního AT&amp;T, využívaly DSSS), a začaly se tu zabydlovat i BreezeNety (využívaly FHSS).</p>
<div class="leftbox"><img src="/wp-content/uploads/cache/20040809-WaveLAN.jpg" alt="WaveLAN 802.11b (rok 1999)" width="212" height="110" /></div>Rychlost byla stále dvoumegabitová, ale oproti původním NCR produktům přinesly ty nové lepší spolehlivost přenosu (osobně ověřeno), ale hlavně snížení ceny - konkrétně u WaveLANů klesla cena AP na 995$ a klienta na 495$, tedy na polovinu.<div><p>
V té době už ale bylo jasné, že rychlost 2 Mb nebude postačovat, proto už nějakou dobu se v IEEE pracovalo na vylepšení těchto standardů a to hned na dvou frontách - výzkumná skupina A se zabývala využití jiného frekvenčního pásma, výzkumná skupina B se snažila nalézt způsob jak lépe využít existujícího pásma.</p>
<p>
První svou práci dokončila skupina B a dala tak vzniknout standardu <strong>802.11b</strong> a to již roku 1999. Tento standard se už nezabýval neperspektivními technologiemi a zaměřil se pouze na DSSS. Přidal podporu dvou dalších modulačních schémat, díky kterým dokázal s využitím stejných 20 MHz dosáhnout rychlosti 11 Mb/s. Tento standard si ale vybral jednu daň - přinesl několik volitelných součástí, které mohl výrobce zvolit a tudíž zařízení podle tohoto standardu nemusela být navzájem kompatibilní.</p>
<p>
Protože by tento problém mohl zabrzdit celé odvětví, vznikla téměř okamžitě organizace <a href="http://www.weca.net/">WECA</a> (Wireless Ethernet Compatibility Alliance), která stanovila podmínky a metodiku měření, po němž udělila danému produktu známku &#8220;bezdrátová věrnost&#8221; - Wireless Fidelity - Wi-Fi (organizace WECA se později přejmenovala na Wi-Fi Alliance). Postupem času tak většina výrobků procházela testováním a tak odhadem 95% prodaných systémů dle 802.11b splňuje podmínky Wi-Fi metodiky.</p>
<p>
Nový standard přinesl ve světě opravdový boom bezdrátových sítí a ten přinesl další snižování cen - abych zůstal u stejné firmy - WaveLAN karta (později přejmenováno na ORiNOCO a pohlceno firmou Proxim), stála v době uvedení 802.11b standardu 295$, později klesla na 95$ a v roce 2002 dokonce na 49$, tedy na dvacetinu ceny před 5 lety při 5 násobném zvýšení rychlosti.</p>
<p>
Bezdrátové karty (moduly) se také začaly masově montovat do počítačů, zejména notebooků. Další historie už není tak překotná, ačkoliv je jistě důležitá pro budoucnost.</p>
<p>
V roce 2002 skončila výzkumná skupina A hlavní činnost tím, že uvedla na trh standard <strong>802.11a</strong> - standard pro bezdrátové sítě v pásmu 5 GHz. MAC vrstva je shodná s 802.11, tudíž implementace čipsetů je velmi levná, modulační rychlost je díky nové modulaci navýšena na 54 Mb/s. Bohužel ale Evropa (včetně ČR) produkty podle tohoto standardu nemohla (a v ČR ještě nemůže) používat, neboť jsou zde na pásmo 5 GHz kladeny požadavky, které nebyly v .11a zohledněny.</p>
<p>
I proto vznikly další dvě skupiny. &#8220;G&#8221; uvedla roce 2003 standard <strong>802.11g</strong>, který nabízí stejnou modulaci (a tedy i rychlost 54 Mb/s), ovšem používá běžnější pásmo 2,4 GHz a tak jsou tyto produkty prodávané úspěšně i u nás. Výhoda těchto produktů je, že jsou kompatibilní se zařízeními dle 802.11b (na rychlostech do 11 Mb/s)</p>
<p>
Skupina &#8220;H&#8221; po velkých průtazích konečně toto září uvede standard <strong>802.11h</strong>, který řeší nedostatky požadované evropským telekomunikačním úřadem a po další ratifikaci se očekává povolení a uvolnění produktů dle tohoto standardu do konce tohoto roku.</p>
<p>
Další budoucnost je zejména ve zvyšování bezpečnosti, propustnosti a kvality (zejm. se v této souvislosti mluví o WiMAX, ale o tom snad někdy jindy). Příští kapitola už je věnována praktičtějším a záživnějším záležitostem ;-)</p>
</div>