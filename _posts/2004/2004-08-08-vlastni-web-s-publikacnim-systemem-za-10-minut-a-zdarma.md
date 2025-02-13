---
ID: 1238
author: Noname
layout: post
oldlink: 'https://www.marigold.cz/item/vlastni-web-s-publikacnim-systemem-za-10-minut-a-zdarma

  '
post_date: 2004-08-08 23:16:13
post_excerpt: ''
published: true
summary_points:
- Webové stránky lze tvořit jednoduše pomocí publikačního systému s administračním
  rozhraním.
- Webzdarma.cz nabízí bezplatný prostor s podporou MySQL a PHP pro publikační systémy.
- BLOG:CMS vyžaduje registraci na Webzdarma.cz, stažení systému a jazykového balíčku.
- Instalace BLOG:CMS zahrnuje nahrání souborů, vyplnění údajů a úpravu práv souborů.
title: Vlastní web s&nbsp;publikačním systémem za 10 minut a&nbsp;zdarma
---

<div class="rightbox"><img src="/wp-content/uploads/cache/20040808-vlastni-web1.jpg" alt="Publikační systém za 10 minut" width="138" height="101" /></div><p>
Chcete-li mít vlastní webové stránky (blog), můžete je vytvářet v zásadě dvěma způsoby &#8211; jednoduše a složitě.</p>

<ul>
<li>Můžete si nainstalovat nějaký software pro tvorbu HTML stránek, udělat nějaký vzhled, vybrat server a tam to nakopírovat a pak kdykoliv chcete přidat další stránku, tak znovu použijete tento software a opět vše upravíte &#8211; napíšete vlastní stránku, dáte jí vzhled, zeditujete ostatní stránky, aby na tu novou odkazovaly. Vyžaduje to také určité znalosti HTML, protože občas vytvoří editory z nějakého důvodu stránku, která se nechce v některých prohlížečích zobrazit, případně potřebujete vlastnosti, které daný editor neumí.</li>
<li>A nebo na to můžete jít jinak &#8211; vezmete publikační systém, nahrajete jej na web a pak už jakékoliv změny děláte v jednom administračním rozhraní, které po vás žádné hlubší znalosti nebude vyžadovat a přidávání nových článků zvládne naprosto každý &#8211; stačí jej jen napsat a kliknout na tlačítko, o vše ostatní se postará publikační systém.</li>
</ul>
<p>
Pro většinu lidí bude druhá varianta jednodušší a přesto s ní budou dosahovat profesionálnějších výsledků. Věřím, že většina z čtenářů tohoto serveru by to zvládla sama, pro ty ostatní jsem připravil jednoduchý návod, včetně zřízení domény pro vaše stránky zdarma.</p>

<!--more--><h3>Výběr</h3>
<p>
Jak už jistě víte, server Marigold běhá na informačním systému BLOG:CMS od <a href="http://hulan.info/">Radka Hulána</a>, proto byl výběr vhodného publikačního "software" velmi snadný ;-).</p>
<p>
Horší to bylo s výběrem vhodného poskytovatele prostoru, který by podporoval MySQL a PHP (podmínka pro informační systém) a nabízel jej zdarma (resp. za umístění reklamy na vašich stránkách). Ve světě je takových poskytovatelů minimálně <a href="http://www.free-webhosts.com/free-mysql-database.php">několik stovek</a>, u nás jsem našel v podstatě jen jediného, ostatní buď přestali prostor nabízet novým zájemcům, vybírají si jen určité projekty, či vyžadují alespoň registraci domény druhé úrovně. Pro účely testu to ale stačí, v případě, že se budete chtít publikováním zabývat vážněji, jistě pro vás nebude problém zaregistrovat se i kdekoliv jinde, případně si zaplatit za provoz na vlastní doméně.</p>

<h3>Registrace</h3>
<p>
Nejdříve si musíte zaregistrovat vlastní prostor, pro účely testu jsem vybral poskytovatele na <a href="http://www.webzdarma.cz/">www.webzdarma.cz</a>. (viz výše). Registrace je velmi snadná &#8211; na jejich stránkách vyplníte registrační formulář, kde si vyberete i adresu pro vlastní doménu třetího řádu. K dispozici je celá řada domén, namátkou mysteria.cz, aktualne.cz, prodejce.cz, kvalitne.cz, vyrobce.cz atd., vaše adresa tedy může být např. vasejmeno.prodejce.cz (v mém testu noname.aktualne.cz) či cokoliv jiného si zvolíte.</p>
<p>
Následně potvrdíte souhlas s obchodními podmínkami, vyplníte obrázkový kód a váš e-mail, na nějž vám přijde mail s odkazem na potvrzení registrace (jednou mi přišel za několik hodin, při posledním testu za pár vteřin). Tam vyplníte další údaje &#8211; účel stránek a zejména heslo pro administraci vašeho webu (a přístup na FTP).</p>
<p>
Poslední co zde musíte udělat je povolit databáze na vašem serveru - přihlaste se v administraci (pozor, uživatelské jméno je celá vaše adresa, tedy např. noname.aktualne.cz). Zvolte v horním menu Nastavení a dále Nastavení MySQL, a povolte databáze a napište heslo, kterým k nim budete přistupovat.</p>

<h3>Instalace BLOG:CMS</h3>
<p>
Nyní si stáhněte poslední verzi publikačního systému (t.č. blogcms.3.2.4.donald.trump.zip) a rozbalte jej. Bohužel, Radek Hulán již nenabízí na svém serveru přímo českou verzi svého publikačního systému, nicméně si můžete stáhnout jazykový balíček, který větší část systému přeloží, najdete jej <a href="http://sourceforge.net/project/showfiles.php?group_id=66479&amp;package_id=67871">na stránkách projektu Nucleus</a>. Stažený soubor czech.php potom umístěte do adresáře \nucleus\language rozbaleného systému.</p>
<p>
Máte-li Windows 98 a vyšší, měli byste mít na ploše ikonku Místa v síti (My Network Places). Přidejte si nový FTP server, který jste si založili (v mém případě je to <a href="ftp://noname.aktualne.cz/">ftp://noname.aktualne.cz</a>). Na tento server zkopírujte všechny rozbalené soubory a nyní můžeme konečně přistoupit k vlastní instalaci publikačního systému.</p>
<div class="leftbox"><img src="/wp-content/uploads/cache/20040808-vlastni-web2.jpg" alt="Blog CMS - install.php" width="203" height="130" /></div><p>
Do prohlížeče napište adresu vašeho serveru a odkaz na soubor install.php (tj. v mém případě <a href="http://noname.aktualne.cz/install.php">http://noname.aktualne.cz/install.php</a>). Zde vyplňte prázdná políčka: uživatelské jméno a heslo k databázi a název MySQL databáze (viz poslední odstavec předchozí kapitoly), pole Needs to be created nezaškrtávejte (založili jste před chvílí). Pole URL and directories je předvyplněné, zde nic nemusíte měnit. A jako poslední krok vyplníte uživatelské jméno a heslo, pod kterým budete přistupovat do systému, váš e-mail a název webu (blogu). Potvrďte tlačítkem Install BLOG:CMS a jestli jste vše udělali správně, vyskočí na vás potvrzovací obrazovka.</p>
<p>
Zde jste informování, že váš server běží, ale že nyní musíte smazat dva soubory &#8211; install.php a install.sql a u souboru config.php, že musíte změnit uživatelská práva. To vše provedete v Místech v síti &#8211; uživatelská práva nastavíte jednoduše tak, že zvolíte pravým tlačítkem myši na souboru Vlastnosti a nastavíte práva tak, že vlastník, skupina i uživatelé budou mít pouze právo Číst a potvrdíte (máte-li jiný operační systém, musíte použít příkaz chmod, jestli jej váš systém obsahuje, nebo použít FTP klient s podporou tohoto příkazu).</p>

<h3>Administrace</h3>
A to je vše! Váš server už nyní běží, můžete jej vyzkoušet (např. <a href="http://noname.aktualne.cz/">http://noname.aktualne.cz/</a>) a můžete se přihlásit i do administrace, která je na adrese vašeho serveru v sekci Nucleus (<a href="http://noname.aktualne.cz/nucleus">http://noname.aktualne.cz/nucleus</a>). <div class="rightbox"><img src="/wp-content/uploads/cache/20040808-vlastni-web3.jpg" alt="Váš nový server" width="282" height="208" /></div>Zde v prvé řadě zvolte Global settings a jestliže jste v jednom předchozím kroku správně nakopírovali soubor czech.php, budete mít možnost změnit Default language na Czech a přeložit tak velkou část administračního rozhraní. <div><p>
Bohužel ale není změněno vše, musíte projít i volby Templates (Šablony), zejména šablony default a detailed a přeložit co se dá. Dále pak ve volbě Skins (všechny zejména ve skupině default) a Extra skin (zejména footer a header, kde změníte META značky). Budete-li mít přesto jakékoliv problémy, ve <a href="http://forum.blogcms.com/">fóru</a> se můžete klidně zeptat (česky) a většinou během chvilky máte odpověď. </p>
<p>
Věřím, že systém je natolik intuitivní, že po chvíli prohlížení jednotlivých sekcí pochopíte k čemu co slouží. Snad jen ještě že v Home / Název_blogu / Nastavení můžete m.j. vytvářet i kategorie na vašem serveru, do kterých pak budete moci přidávat vaše články. Ty se přidávají snadno &#8211; zvolíte z menu New Item / Název blogu a na nové stránce jen vyplníte nadpis, perex,  tělo článku a potvrdíte.</p>
<p>
Samozřejmě je také důležité, aby váš server nevypadal jako všechny ostatní, toho dosáhnete úpravou šablon, skinů a případně i CSS souborů a volbou pluginů. To už ale nechám na vás.</p>
<p>
Chcete-li vidět vše v akci, můžete zkusit zmíněný server <a href="http://noname.aktualne.cz/">http://noname.aktualne.cz/</a>. Uživatelské jméno do <a href="http://noname.aktualne.cz/nucleus">administračního rozhraní</a> je &#8222;noname&#8220;, heslo je prostě &#8222;heslo&#8220; (prosím neměňte jej, aby to mohli vyzkoušet i ostatní).</p>
<p>
P.S.: Tento článek nepsal Patrik (je na dovolené), takže případné nadávky směřujte na mě ;-). Není to také reklamní článek, nemám nic společného ani s Blog:CMS ani s webzdarma.cz, prostě nic lepšího (za ty peníze ;-) ) osobně neznám, vaše nápady uvítám v diskusi.</p>
</div>