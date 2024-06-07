---
ID: 1242
title: Chci bezdrátovou síť! (2)
author: Noname
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/chci-bezdratovou-sit-2
published: true
post_date: 2004-08-10 09:38:16
---
	<div class="rightbox"><img src="/wp-content/uploads/cache/20040810-Outdoor Wi-Fi.jpg" alt="Venkovní síť" width="239" height="153" /></div><p>
V této kapitole se budeme věnovat bezdrátovému „newspeaku&#8221;, slovům, která nezasvěcení nemusí chápat.</p>

<h3>2. Co je to bezdrátová síť (Wi-Fi, hotspot, freenet, wireless, 802.11 &#8230;)</h3>
<p>
Na některé otázky z nadpisu této části odpověděla už předchozí kapitola, takže jen menší opakování:</p>

<ul>
<li><strong>Bezdrátová síť</strong> = <strong>Wireless</strong> = síť kde je místo drátů (Ethernetu) využíváno &#8220;bezdrátů&#8221;, pojítek využívající radiových vln k přenosu signálu. V naprosté většině případů u komunitních sítí se pod pojmem bezdrátová síť rozumí <strong>Wi-Fi</strong> (pracuje v <strong>bezlicenčním pásmu 2,4 GHz</strong>). V širším slova smyslu se pod pojmem bezdrátová síť myslí sítě ve <strong>vyhrazených frekvenčních pásmech</strong> (u nás zejm. 26 GHz - FWA) a také <strong>PtP </strong>(dvoubodové) <strong>spoje</strong> řešené buď radiově (nejčastěji v pásmu 10,5 GHz, či v placených pásmech typicky 18-36 GHz) a nebo pomocí <strong>optického</strong> (laserového) <strong>pojítka</strong>.</li>
	<li><strong>Wi-Fi</strong> - označení produktů dle <strong>802.11b</strong>, které by mělo být interoperabilní (kompatibilní, čili schopné komunikovat i se zařízeními jiných výrobců). Je to zhruba 90% všech bezdrátových produktů dle <strong>IEEE 802.11b</strong>, přesto je mnoho zejména velmi levných tzv. &#8220;taiwanských&#8221; značek, které se zde často prodávají a přesto nesplňují Wi-Fi podmínky. <em><u>První rada</u> - Kupujte jen výrobky, které mají logo Wi-Fi, je to jistější!</em></li>
</ul>
<p>
Pro vysvětlení dalších termínů musím už zabrousit hlouběji.</p>

<!--more--><p>
Jednu záležitost jsem totiž neřekl a je IMHO zásadní pro pochopení spousty věcí a mnoho lidí to neví - <strong>standard 802.11 (.a, .b, .g, .h &#8230;) je standard pro vnitřní sítě!</strong> Tedy všechny produkty podle tohoto standardu jsou vyvinuty pro provoz ve vnitřní prostorách a <strong>pro provoz ve venkovním prostřední nejsou uzpůsobeny - optimalizovány</strong>.</p>
<p>
Ač se to na první pohled nezdá, tato skutečnost je opravdu zásadní. <strong>V ČR se pod bezdrátovými sítěmi myslí zejména venkovní sítě</strong>, ve světě jde ale naprostá většina (&gt;90%) do vnitřních sítí.</p>
<p>
<em>Tento jev není nijak záhadný - cenová politika Českého Telecomu a jeho monopol na trhu last-mile zapříčinily, že nástup ADSL byl v ČR o několik let opožděn a běžná cena za to, co je ve světě považováno minimum, aby se tomu dalo říkat broadband - 256 kbit - dosahovala výše průměrného měsíčního platu, a dovolit si to mohly jen větší firmy. Pro domácnosti žádná flat-fee volba neexistovala (a vyjma ADSL stále neexistuje).</em></p>
<p>
<em>Proto se objevilo řešení - místní podnikatel (ISP) si koupil pevnou linku, např. 512 kbit za 15 tisíc a postavil na to bezdrátový přístupový bod s anténou. Na něj připojil třeba 5 firem, každé účtoval 4 tisíce, firmám to jelo běžně okolo 200-300 kbit (overbooking 1:5), podnikatel měl v této modelové (ale velmi běžné) situaci 25% &#8220;vejvar&#8221;. Spokojenost na všech stranách (vyjma ČTc).</em></p>
<p>
<em>Postupem času se tato řešení dostala i do residenčního trhu - místo jedné firmy připojil podnikatel panelák, v kterém třeba 10 lidí chtělo internet. Mezi sebou je zasíťoval klasicky kabeláží, dal tam hub za 1000 Kč a připojil je k síti, každému z nich účtoval pak třeba 500 Kč.</em></p>
<p>
<em>Takto vzniklo mnoho firem (sám jich znám zhruba 500), některé třeba jen s 5 zákazníky, některé s několika tisíci zákazníků. Samozřejmě slušná firma navyšovala kapacity a tak když neměla 5 zákazníků, ale třeba 20, tak už připojila např. 2 Mb/s. 2 Mb/s s overbookingem 1:20 je u telecomu s 3 miliony zákazníků ještě dnes exkluzivní záležitost za 10 tisíc Kč (bez garancí kvality), malý místní podnikatel s 20 zákazníky koupí 2 Mb/s linku za 20 tisíc a tak onen 2 Mb/s/1:20 může nabízet už za tisícovku (plus marže). A když bude mít zákazníků 100, může nabízet stejnou službu třeba jen za pětistovku.</em></p>
<div class="leftbox"><img src="/wp-content/uploads/cache/20040810-infrastructure.jpg" alt="Schéma Infrastructure mód" width="291" height="171" /></div><p>
To jsem ale hodně odbočil, zpět k bodu bodu &#8220;<strong>vnitřní síť</strong>&#8221;. Jak už jsem psal, většina používaných sítí používá Wi-Fi produkty, tj. produkty pro vnitřní sítě. Ve standardu specifikované topologie jsou 2:</p>

<ol>
<li><strong>Infrastructure</strong>: síť typu hvězda, uprostřed sítě je umístěn <strong>přístupový bod (AP)</strong>, k němu se připojují klienti</li>
	<li><strong>Ad-hoc</strong> (<strong>Peer-to-Peer</strong>): síť bez AP, <strong>klienti</strong> komunikují vůči sobě navzájem.</li>
</ol>
<p>
<strong>Předpokládané užití je tedy uvnitř budov:</strong></p>

<ul>
<li><strong>Máte doma např. notebook a desktop počítač?</strong> Žádný problém, v obou máte Wi-Fi a můžete přenášet data. Nebo si pořídíte AP, připojíte ho na váš DSL modem (jestli to už není dohromady), a oba (více) počítače sdílejí linku k internetu a navzájem svá data.</li>
	<li><strong>Máte zahradu?</strong> Žádný problém, s Wi-Fi AP a notebookem můžete pracovat klidně tam, nemusíte tahat kabely, jste stále on-line.</li>
	<li><strong>Máte konferenci</strong> a chcete účastníkům nabídnout vaši prezentaci? Zapněte si Ad-hoc mód na vašem notebooku a nechte ostatní si vaše materiály stáhnout.</li>
	<li><strong>Sídlíte v historické budově</strong> a nesmíte vrtat kabely do zdí a lišty se vám hnusí? Bezdrát to vyřeší.<br/>Přestěhovali jste se a potřebujete okamžitě pracovat? S Wi-Fi mohou všichni zaměstnanci pracovat okamžitě, není třeba pokládat kabely.</li>
	<li><strong>Vyhořela (byla vytopena) vaše firma?</strong> Ještě že mají všichni zaměstnanci notebooky - prostě si sednete kamkoliv, zapojíte AP (k internetu) a už můžete kooperovat a zákazníci to ani nemusejí poznat.</li>
	<li>&#8230;.</li>
</ul>
<p>
Tohle byl nejčastější způsob využití ve světě, proto tyto standardy/produkty se vyznačují několika <strong>vlastnostmi, které omezují použití ve venkovních sítích</strong>:</p>
<p>
<strong>Klientská zařízení jsou typicky vybavena jen USB, PCI či PCMCIA rozhraním</strong>. Klientských zařízení vybavených Ethernetem je relativně málo, a nebo jsou určena jen pro připojení jediného počítače (MAC adresy). Teď už to jde, ale před dvěma lety něco najít, to byla hrůza. To je zásadní hlavně pro připojování firem - musí se pořídit ještě router.</p>
<p>
V podstatě všechna zařízení mají jen <strong>vnitřní provedení</strong>, tj. nic co byste mohli dát na déšť, je třeba umístit jej do rozvaděče, nebo použít dlouhý koax, který zhoršuje parametry. Tato omezení nejsou dané přímo standardem, ale majoritním trhem a ztěžují (zdražují) instalaci.</p>
<p>
<strong>Zařízení předpokládají, že jsou užívána vevnitř a používají protokoly, které jsou optimalizovány pro vnitřní sítě</strong>. Toto je omezení standardu - používá se protokol <strong>CSMA/CA</strong>, který zjednodušeně funguje tak, že zařízení na nosné frekvenci poslouchá, zda-li vysílá jiné zařízení, a jestliže ne, tak může začít vysílat samo. Jenže - když se klientská zařízení nevidí, což je 99% všech venkovních sítí, potom může zasílat i jiné klienské zařízení ve stejnou dobu a dojde ke <strong>kolizi</strong> a musí se začít vysílat znovu. Čím více klientů (či jejich větší vytížení), tím více problémů a už pár procent kolizí může znamenat díky funkcionalitě TCP/IP <strong>nefunkčnost sítě jako celku</strong>.</p>
<p>
Protože i ve vnitřních sítích může docházet k případům, že se klienti navzájem nevidí, je zde volitelná možnost zapnout na přístupovém bodě používání jiného protokolu - <strong>RTS/CTS</strong>. Tak se každý před odesláním rámce zeptá protějšku, zda-li může vysílat, protějšek pošle potvrzovací rámec který pro ostatní klienty znamená &#8220;teď mlčte, mluví někdo jiný&#8221; a klient může vysílat. Tento protokol je až na výjimky nutností pro všechny venkovní bezdrátové sítě (<strong>hledejte RTS/CTS, Medium reservation nebo Hidden Station</strong>), ovšem kvůli větší režii více zatěžuje síť, maximálně využijete přibližně 20% celkové kapacity! Proto se u tohoto režimu nastavuje číselná hodnota (typicky 400-500 byte, podle vážnosti problému), jak velký musí být paket, aby byl poslán ještě CSMA/CA (protože čím delší paket, tím déle se přenáší a tím větší pravděpodobnost, že bude zarušen). Tento mód není podporován ad-hoc sítěmi (nemají řídící AP). <em><u>Rada druhá</u> - ruce pryč od venkovních ad-hoc sítí!</em></p>
<p>
Další omezení jen zkratkovitě - u <strong>vnitřních sítí chcete, aby všichni komunikovali stejnou - maximální rychlostí</strong>, <strong>u venkovních</strong> byste chtěli dát jednomu zákazníkovi 256 kbit, druhému 512, třetímu ještě něco jiného, a to v podstatě <strong>není možné</strong> (řeší se to ořezáváním na routerech, což je ale polovičaté řešení, síť stále jede na maximu, a navíc to stojí další peníze), u <strong>venkovních sítí se také přenášejí typicky podstatně menší pakety oproti vnitřnímu Ethernetu</strong>, vnitřní sítě musí být robustně chráněny oproti odrazům, které venku v podstatě neexistují (a tedy plýtvá se pásmem) atd.</p>
<p>
Zbývají mi zodpovědět ještě dva dotazy - „<strong>freenety</strong>&#8221; se říká některým Wi-Fi sítím, které nabízejí připojení zdarma (typicky ale jen nějak omezeně, např. na 64 kbit). Pakliže to je jen obchodní model - &#8220;základ zdarma, vyšší stupeň za peníze&#8221;, potom má určitě smysl, je jich ale jen pár, není to totiž tak jednoduché provozovat (oddělit). Model, který je čistě zadarmo nechápu - vždy jsou nějaké náklady, nějaký reklamní či jiný synergický efekt je spíše u hotspotů (viz dále), takže to většinou znamená problémy, pozdější zavedení plateb, nekvalita, &#8230;</p>
<p>
Bezdrátové <strong>hot-spoty</strong> jsou zvláštní kategorií, kterou si nechám na příště.</p>
