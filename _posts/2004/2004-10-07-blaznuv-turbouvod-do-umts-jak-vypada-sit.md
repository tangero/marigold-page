---
ID: 1349
author: Patrick Zandl
categories:
- UMTS
- 3G
- Turboúvod do mobilních sítí
layout: post
oldlink: 'https://www.marigold.cz/item/blaznuv-turbouvod-do-umts-jak-vypada-sit

  '
post_date: 2004-10-07 09:26:24
post_excerpt: ''
published: true
summary_points:
- UMTS není technický zázrak, vychází z GSM a nepřineslo revoluci.
- Jádro sítě UMTS tvoří počítače řídící síť, například routery a ústředny.
- Přístupová síť UMTS, UTRAN, využívá základnové stanice (NodeB a RNC).
- UMTS Release 99 je GSM posunuté do 3G pásma s širším kanálem.
title: Bláznův turboúvod do UMTS &#8211; jak vypadá síť
---

<p>
Pokud jde řeč o UMTS, většinou se tato síť třetí generace tváří jako technický zázrak, jako složitý a komplexní systém a jako taková je i popisována. Moudré knihy vás v patnácti kapitolách provedou nástrahami tří stovek zkratek, které obsahuje norma UMTS ve svém prvním vydání, což odradí většinu. Zkusme si ale UMTS rozebrat jinak. </p>

<p>
UMTS především není žádný technický zázrak, ačkoliv tvrzení o komplexnosti tohoto systému je pravdivé. UMTS prakticky kompletně vychází z předchozích návrhů buňkových sítí jako je GSM nebo NMT a byť to zní nactiutrhačně, dovolil bych si říci, že UMTS není žádnou revolucí. Zatímco GSM přineslo oproti NMT digitalizaci a NMT oproti nulté generaci právě tu buňkovou strukturu, UMTS ve svém prvním standardu mnoho nového nenabídlo.
</p>

<h4>Jádro sítě</h4>
<p>
Síť UMTS můžeme tedy rozdělit do dvou hlavních částí. Tou první je jádro sítě tedy core network, CN. Jádro sítě je hromada počítačů, které jsou převlečeny do nejrůznějších funkcí řízení a správy sítě, jako je autorizace uživatelů, směrování provozu v síti i mimo ni. Řekli bychom, že jde o routery, autorizační a databázové servery, ale vzhledem k tomu, že některé tyhle routery se starají ne o paketovou, ale okruhovou síť, přidržíme se u nich tradičnějšího označení &#8220;ústředny&#8221;. Ve všech nákresech struktury jádra sítě najdete ještě hromadu další techniky, ta je ale pro nás nyní nepodstatná a abstrahujme od ní, neboť se stará prakticky výhradně o autorizaci a sběr dat (zejména pro účtování).</p>

<h4>Přístupová síť a základnová stanice</h4>
<p>
Druhou částí sítě je takzvaná přístupová síť. UMTS je benevolentní standard a tak povoluje přístup přes nejrůznější druhy přístupových sítí, většinou ale dosti obskurních, jako je Hiperlan nebo satelitní připojení. V praxi je zatím použitelná jedna z nich a to UTRAN, terestrická síť v pásmu 2GHz. </p>

<p>
Přístupová síť svůj signál distribuuje prostřednictvím základnových stanic, těch stožárů, k nimž se rádiem mobilka připojuje. Jde vlastně o obdobu přístupových bodů, apéček u WiFi, s &#8220;drobnými&#8221; (a drahými) rozdíly. Základnovou stanicí pro náš účel zovu konglomerát samotné základnové stanice zvané v normě NodeB (obdoba BTS u GSM) a RNC, Ovladače radiové sítě (obdoba BSC u GSM), který se stará o soužití blízkých základnových stanic. </p>

<p>
<img src="/assets/20041007-UMTSsit.jpg" alt="architektura UMTS" />
<br /><i>Tady vidíte síť v skoro-plné kráse. My jsme si to opravdu zjednodušili. Zatímco vše vlevo jsme pojmenovali přístupovou sítí, vše vpravo od těch zkřížených čar jsme pojmenovali jádrem sítě. Zbytek zatím nemusíte nijak studovat, většinu toho ještě vykostíme příště. </i></p>

<h4>Release 99</h4>
<p>
Celá funkce UMTS je tedy zjevně stejná, jako u GSM. Mobila se přes přístupovou síť (UTRAN) připojí k základnové stanici a z ní se předá její požadavek do jádra sítě, které ho odbaví, například propojí do telefonní sítě a odezvu z telefonní sítě pošle stejnou cestou zpět. Jak easy. Snadno nazřeme, že je záhodno, aby UMTS síť měla více základnových stanic a můžeme si také odvodit, že může mít i více jader sítě, což vnese trochu vzrušení do našeho zjednodušujícího pohledu, ale zase nic zásadního to není. Handover z GSM již známe a u UMTS je to podobné, snad s tím rozdílem, že handover je v UMTS (tedy správně na UTRAN) komplexnější záležitost. Ale o tom až v momentě, kdy se to dotkne rychlého přenosu data&#8230;</p>

<p>
Tím jsme se v kostce dozvěděli, jak UMTS síť vypadá a na první pohled to je trivialitka. Pro špeky je třeba ponořit se hlouběji pod povrch, vždy při takovém ponoru ale nezapomínejme na to, že UMTS opravdu není žádný zázrak a vždy je to buďto hromada počítačů, nebo nějaký vysílač a přijímač (a věci kolem jako filtry nebo antény) - nenajdete tu žádné cyklotrony, plazmu nebo nějaký podobný div fyziky. </p>

<p>
První standard UMTS se jmenuje Release 99 (též Rel99 nebo R99) a poslední číslice má indikovat rok, kdy byl vydán. Ještě nejste zvyklí řeči mystéria, takže jste si neodvodili, že standard Release 99 byl vydán v březnu 2000, na tyhle operace s čísly si u UMTS rychle zvyknete. </p>

<p>
Release 99 je vlastně posunem GSM do 3G pásma a do širokopásmového přenosu. Zatímco GSM si vystačilo se šířkou radiového kanálu 200 kHz, jeden radiový kanál má v UMTS šířku rovných 5 MHz. Namísto TDMA se používá WCDMA s časovým nebo frekvenčním duplexem podle toho, jaké pásmo si operátor koupil a pokud byl utrácivý a koupil si pásmo pro obě, pak podle typu služby. Zjednodušeně řečeno to je celá odlišnost UMTS Release 99 od GSM Phase 2 Release 99. </p>

<h4>Kde se vzala rychlá data?</h4>
<p>
To je správná otázka – jak to, že data putují v UMTS síti rychleji, než v GSM síti po GPRS? Zjednodušeně řečeno proto, že v UMTS síti je více místa. Jak vidíme, mobilka v UMTS síti obsluhuje 25x širší pásmo, takže teoreticky může nabídnout 25x vyšší rychlost. V praxi je to samozřejmě trochu jinak, zatímco na GPRS dnešní mobily vytáhnou pro download maximálně tak 90 Kb/s, u UMTS je nejvyšší běžná rychlost 384 Kb/s. Ty 2 Mb/s, co čítáte v rozjásaných zprávách operátorů, je taková hezká teorie – to je teoretická maximální rychlost u nepohybující se stanice, která sežrala jeden sektor celý pro sebe, tedy stav, který operátoři jistě rádi vidí a podporují. Nehledě na to, že se u takové rychlosti původně ani nepředpokládalo, že  takovou rychlostí bude disponovat běžná mobilka, ta byla předpokládána pro stacionární modemy velikosti krabice od bot s napájením ze sítě, protože vysílat v tak širokém pásmu řekněme půl wattem výkonu není nic, co by baterka vašeho notebooku utáhla dlouho. </p>

<p>
Jak vidno, UMTS šlo na rychlá data metodou brutální síly, tedy rozšířením pásma, jímž mohou rychlá data proudit. Mezi tím ale do GSM sítí dorazilo EDGE se svou inovativní myšlenkou, že data by mohla proudit rychleji také tím, že by se zvýšila inteligence, s jakou jsou tato data kódována, tedy že by se zlepšily kodeky starající se o odbavování dat. Současné zvyšování rychlostí mobilních dat jde zejména tímto směrem. </p>

<h4>Zrychlujeme data</h4>
<p>
Na rychlost dat působí několik faktorů:</p>

<ul>
<li>šířka radiového kanálu kterou u UMTS už není vhodné dále zvyšovat 
</li>
<li>šířka disponibilního pásma vyhrazeného pro síť (závisí na tom, kolik operátor nakupoval a lze z jeho strany velmi dobře regulovat dalším nákupem či zahuštěním sítě)
</li>
<li>způsob kódování přenášených dat (populární od dob GPRS)
</li>
<li>prevence proti chybám při přenosu (vykradeno z bezdrátových sítí)
</li>
<li>řešení chyb při přenosu (vykradeno tamtéž)
</li>
<li>počet aktivních prvků sítě, které jsou na trase přenosu až do cílového bodu dat (příjemné dilema, co udělat s architekturou UMTS sítě, kde data putují přes 20 prvků sítě a na každém naberou 10 milisekund zpoždění vlivem kódování/dekódování. Kdyby standardizátoři četli tento turboúvod, věděli by, stejně jako víte už teď vy, že počet prvků je vhodno redukovat. Naštěstí ho nečetli, takže jim to alespoň funguje.)</li>
</ul>
<p>
Je vidět, že první dva faktory jsou dané nebo neřešitelné z hlediska UMTS standardu. Vývoj tedy kráčí ve šlépějích zbývajících čtyř bodů (no, možná mne časem napadnou další). Protože to je na delší povídání, nechám si to zase na příště, pokud mne samozřejmě s Bláznovým turboúvodem do UMTS zcela nevypískáte. Podíváme se především na to, co lze z UMTS sítě vyhodit, abychom se dostali přibližně do stavu, který tu popisuji už nyní já – proto jsem vás nezatěžoval ostatně výklady hlubší architektury, protože pohybem z Release 99 do Release 5 většinu těch krabic vypakujeme nebo zdredukujeme.</p>

<p>
Na závěr: uvědomme si také historická fakta. UMTS standard začal vznikat ještě před dokončením standardu GSM jako jeho další vývoj a většina UMTS návrhářů byla tehdy přesvědčena, že UMTS bude muset zvládnout dramatický nárůst požadavků po přenosu hlasu. To byl také problém let 97-98, kdy vznikly největší části UMTS standardu a kdy západní operátoři obtížně zvládali expanzi svých sítí přetěžovaných hlasovým provozem. Tu vyřešili kolem roku 2000, jenže to už byl UMTS prakticky standardizován a tak Release 99 není prakticky ničím více, než GSM s více prostoru pro hlas a shodou okrajových okolností i pro data. </p>

<p>
Zatímco GSM bylo v roce 1992, kdy první GSM sítě startovaly, s rychlostí dat na výši své doby (9,6 Kb/s uměly tehdy nejlepší modemy), o UMTS se to dnes říci nedá. A zdá se, že toto opomenutí vývojového trendu došlo i standardizátorům.
</p>