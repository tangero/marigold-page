---
ID: 1401
title: 'Všechny cesty k&nbsp;internetu (2)'
author: Noname
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/vsechny-cesty-k-internetu-2
published: true
post_date: 2004-11-11 17:15:48
---
	<div class="rightbox"><img src="/wp-content/uploads/cache/20041111-eduroam-logo.gif" alt="Logo eduRoam" width="230" height="100" /></div><p>
Včera jsem vám přinesl <a href="/item/vsechny-cesty-k-internetu">první článek o konferenci Všechny cesty k internetu</a>, jak jsem psal, bylo tam toho mnohem více, a tak si dnes dovolím pokračovat a zmíním další z probíraných témat a tím je mobilita v bezdrátových sítích (nejen) na evropských univerzitách.</p>
<p>
Úvodem bych měl ale noticku k CDMA. Na akci byla totiž i přednáška Eurotelu k CDMA, nicméně není to na samostatný článek. Dnes se ale objevily informce o nových vysílačích Eurotelu v tomto pásmu, například na <a href="http://www.mobilmania.cz/Bleskovky/AR.asp?ARI=108637">Mobilmanii</a> či <a href="http://digiweb.cz/?s1=i&amp;s2=9&amp;s3=0&amp;s4=0&amp;s5=0&amp;s6=0&amp;m=d&amp;a%5barea_id%5d=10053230&amp;a%5bid%5d=15196790&amp;p=i90000_d">Digiwebu</a>. O těchto záležitostech už se mluvilo začátkem minulého týdne, takže kdyby se novináři účastnili těchto přednášek, mohli by uvádět exkluzivní informace a nemuseli by opisovat tiskové zprávy. ;-)</p>
<p>
Dovolím si ale hlavně zchladit hlavy všem případným zájemcům, protože po skončení přednášky jsem se ing. Ecka zeptal, co ten velký bílý flek na mapě pokrytí od Prahy na jih, kdy že bude pokryto.</p>

<!--more--><p>
Odpověď byla, že <strong><strike>zde vlastní potřebné pásmo armáda ČR a že tam se pokrytí nedočkáme</strike></strong>. (zřejmě špatně pochopeno - viz diskuse, omouvám se) Další nemilou zprávou je změna chování CDMA ke stahování většího objemu dat, na kterou <a href="http://hulan.info/blog/?item=eurotel-cdma-ma-novou-formu-f-u-p">na svém blogu upozornil Radek Hulán</a>. Dovolím si citovat &#8220;<i>Eurotel na svém CDMA zjevně nezavedl jen omezení P2P sítí, ale zavádí normální F.U.P., kdy Vám po stažení určitého množství dat sníží rychlost i http a ftp přenosů na desetinu rychlosti původní, takže Vám CDMA jede na rychlosti GPRS nebo dial-upu.</i>&#8221;</p>

<h3>Mobilita a roaming v akademických sítích</h3>
<p>
Nadpis tohoto odstavce se shoduje se jménem přednášky, kterou měl na zmiňované konferenci Ing. Jan Fürman ze sdružení CESNET. Podnadpis &#8220;principy fungování mobility a roamingu v rámci evropských akademických sítí, autentizační mechanizmy, bezpečností aspekty a centrální autentizační infrastruktura&#8221; vám také asi nic moc neřekne, pokusím se tedy v krátkosti vysvětlit o co jde.</p>
<p>
Evropské technické univerzity si všimly rostoucího zájmu studentů o mobilní přístup do akademické sítě, mnohé z nich začaly vybudovávat bezdrátová přípojná místa již koncem minulého tisíciletí (tehdy ještě s využitím prvků dle standardu 802.11, tedy max. 2 Mb/s) — sám jsem některým tehdy hardware pro tyto sítě dodával a dělal školení.</p>
<p>
Ovšem v Evropě, více snad než v ČR je běžná spolupráce několika univerzit na různých problémech či výzkumech, studenti se tak často pohybují na půdě jiných vysokých škol a nemohli se tak donedávna připojovat do cizí sítě bez znalosti jejích přístupových údajů.</p>
<p>
To se právě mění, neboť vznikla pracovní skupina <a href="http://www.terena.nl/tech/task-forces/tf-mobility/">TERENA mobility task force</a>, která zavádí principy mobility (nejen) mezi univerzitami po celé Evropě.</p>
<p>
Byly definovány tři způsoby autentizace uživatele v cizí síti:</p>

<ul>
<li><u>Autentizace na bázi VPN</u>: spojení VPN sítí a uživatel přes tunel na domácí VPN koncentrátor dostane do své sítě — je vyhrazen samostatný segment IP adres, které slouží k tomuto účelu, řešení je relativně náročné jak na síť jako celek, tak i na počítač klienta. </li>
	<li><u>Autentizace na bázi webového formuláře</u>: známé z některých hot-spotových řešení — uživatel se po připojení přesměruje na ověřovací stránku, kde musí zadat své jméno a heslo (autentizuje se vůči centrálnímu AAA serveru) a dále má již přístup volný — tento způsob je nenáročný, přináší ovšem jen malou míru bezpečnosti </li>
	<li><u><b>Autentizace na bázi 802.1x</b></u>: to nejzajímavější a také nejpoužívanější a nejperspektivnější řešení je využití standardního 802.1x standardu s autentizačním protokolem EAP. Dále se budu věnovat tedy jen tomuto způsobu. </li>
</ul>
	<h4>Autentizace na bázi 802.1x</h4>
<div class="rightbox"><img src="/wp-content/uploads/cache/20041111-hierarchie-radius.gif" alt="Hierarchie Radius serverů" width="300" height="170" /></div><p>
Celý princip je prostý a vychází z principů Internetu — byla vytvořena hierarchická struktura Radius serverů jednotlivých organizací a států, nad tím vším je pak top-level Radius server, jak ukazuje následující obrázek.</p>
<p>
Například tedy student z ČVUT přijede do Nizozemska a chce se připojit se svým notebookem do akademické sítě místní univerzity. Nemusí se někde doprošovat o nějaký přístup, prostě stejně jako ve své domácí síti napíše v přihlašovacím okně Radius klienta (suplikant) své přihlašovací jméno (ve formátu prihlasovaci_jmeno@cvut.cz) a své vlastní heslo.</p>
<p>
Suplikant požádá místní &#8220;autentikátor&#8221; (typicky bezdrátový AP) o spojení a ten na základě svého nastavení přepošle dotaz na Radius server nizozemské univerzity, který zkontroluje, zda-li má pro daného uživatel záznam ve své vlastní tabulce uživatelů. Když nemá, přepošle požadavek na nadřízený národní Radius server. Ten se pokusí podle domény rozlišit, zda-li patří uživatel do některé z jemu podřízených Radius serverů a protože nepatří, opět přepošle požadavek výše top-level Radius serveru. Ten pozná, že uživatelské jméno končí doménovým identifikátorem .cz a tak přepošle požadavek národnímu Radius serveru .cz domény. No a ta konečně pošle požadavek Radius serveru ČVUT a ten odpoví standardním způsobem, kde potvrdí či zamítne přístup.</p>
<p>
Vypadá to velice zdlouhavě, ale je to otázka několika desítek milisekund. Samozřejmě veškerá komunikace mezi Radius servery putuje šifrovaná dvousměrným tunelem, nehrozí tak nabourání nezvaným útočníkem. V závislosti na ověřovacích údajích může klient dostat přístup např. do zaměstnanecké sítě, do sítě pro hosty a nebo na internet.</p>
<p>
V budoucnu se plánuje přechod na standard 802.11i, který přinese ještě větší zabezpečení komunikace, čeká se jen na schválení této normy a dostatečnou podporu na AP i síťových kartách uživatelů.</p>

<h4>Jak se zapojit</h4>
<p>
Uvedené řešení není něco, co by zatím jen leželo v hlavách vědátorů, ale opravdu funkční řešení (i když zatím v testovacím provozu), které funguje či alespoň horečně připravuje ve větší části Evropy (viz mapa).</p>
<div class="rightbox"><img src="/wp-content/uploads/cache/20041111-mapaeduroam.gif" alt="Mapa Eduroam v Evropě" width="555" height="538" /></div><p>
Nejedná se také o něco určeného je pro univerzity, je vítána každá organizace, připojená do sítě národního výzkumu (v Česku jsou zatím členy ČVUT FEL Praha, Technická univerzita v Liberci, Západočeská univerzita v Plzni, Vysoká škola báňská - Technická univerzita Ostrava, Univerzita Karlova v Praze, Lékařská fakulta UK Hradec Králové, VŠCHT Praha a kraj Vysočina).</p>
<p>
Samozřejmě jsou určitá pravidla roamingové politiky, které musí každý dodržovat či jejich dodržování vyžadovat po svých členech:</p>

<ul>
<li>pravidla, která musí splňovat domácí síť uživatele: </li>
	<ul>
<li>technická podpora uživatelů </li>
	<li>poskytnout ověřování svých uživatelů </li>
	<li>je zodpovědná za veškerá akce uživatelů, které ověřila, </li>
	<li>musí reagovat na ohlášení bezpečnostních incidentů, které jsou způsobeny jejími uživateli </li>
	<li>musí logovat všechny autentizační události pro potřeby případného dohledávání </li>
</ul>
	<li>pravidla, která musí splňovat hostující síť </li>
	<ul>
<li>uchovávat v logu autentizační informace, které musí na vyžádání zpřístupnit oprávněným místům </li>
	<li>musí vytvořit vlastní zásady pro použití sítě </li>
	<li>musí poskytnout autentizační služby pro hostující uživatele </li>
</ul>
</ul>
<p>
dále jsou samozřejmě pravidla pro chování uživatelů, pro autentizační proxy systém, jsou definovány i postupy řešení bezpečnostních incidentů a sankce za nedodržení pravidel.</p>
<p>
Další důležitá věc, kterou by měla instituce splňovat (ale není to striktní podmínka) je použití jednotného SSID (jména bezdrátové sítě), dle návrhu TERENA se používá &#8220;eduroam&#8221;.</p>
<p>
Organizace by také měly založit stránky s detailními informacemi o stavu sítě v dané organizaci. Ty budou v Česku odkazovány z centrálního &#8220;mobility portálu&#8221; <a href="http://www.eduroam.cz/">http://www.eduroam.cz</a>, který provozuje CESNET. Podobné stránky mají i ostatní státy, např. <a href="http://www.eduroam.nl/">Nizozemsko</a>. Mimochodem logo eduRoam vymyslel student technické univerzity v Liberci.</p>
