---
ID: 1729
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/mysterium-jmenem-xmax-aneb-na-tenhle-zazrak-ma-umrit-wimax-i-3g

  '
post_date: 2005-07-19 08:17:33
post_excerpt: ''
published: true
summary_points:
- xMax je technologie konkurující WiMaxu, využívající subgigová pásma pro přenos dat.
- Technologie xMax využívá úzkopásmový kanál pro synchronizaci a širokopásmový signál
  pro data.
- xMax používá velmi nízký vysílací výkon, což vyvolává pochybnosti o funkčnosti.
- xG slibuje předvedení xMaxu v září 2005, ale komerční nasazení je nejisté.
title: "Mystérium jménem xMax (aneb na tenhle zázrak má umřít WiMax i 3G)"
---

<div class="rightbox"><img src="/wp-content/uploads/20050719-xgtech.gif" alt="xG Technology" width="66" height="67" /></div><p>V poslední době se i českým internetem prohnala vlna zájmu o technologii xMax společnosti xG Technologies. Článek vyšel <a href="http://www.palmserver.cz/clanek.php3?show=2849">na Palmserveru</a>, zmínka v Inside, na <a href="http://www.zive.sk/h/Bleskovky/AR.asp?ARI=113666">slovenském Živě</a>. xMax má být konkurent pro WiMax,  který v dostupném radiovém spektru protlačí megabitové rychlosti do plochy desítek kilometrů čtverečních. Sleduji tuhle technologii po očku už nějakou dobu a zatím jsem ji vždy měl za něco, co má z pár investorů vylákat penízky a skupině vykuků zajistit spokojené živobytí. I když bych se rád nechal příjemně překvapit. Ale vysvětlím, proč. Ostatně, firma vody rozvířila hlavně díky tomu, že FCC vydalo povolení k experimentálním živým testům, což si laici rádi překládají jako podporu xMaxu. </p>

<p>Předně je nepříjemné, že na <a href="http://www.xgtechnology.com/">webu  xG Technologies</a> najdeme jen velmi málo technicky orientovaných materiálů, většinou jen abstraktní srovnání. Nejvíce informativní jsou odstavce jako: </p>

	<blockquote><p>Unlike other wireless technologies that move as much power as possible from the carrier into the information-bearing sidebands, xMax does just the opposite, placing more than 99 percent of its power within a narrowband carrier while keeping its sideband energy at micro-power levels.  Typically –60dB to –100dB below the carrier, xMax’ unique information-bearing sideband, dubbed xG Flash SignalTM, can be as much as 100,000 times below the FCC’s “Part 15” regulations.</p>
</blockquote>
<p>xMax je na první pohled podobný technologii UWB, technologii širokorozprostředného pásma. Zatímco UWB je ale určeno pro frekvenční pásma mezi 3 a 10 GHz, xMax má operovat v pásmech 400 – 1000 MHz, tedy subgigových pásmech. To by znamenalo velikou výhodu a také se to často zmiňuje, subgigová pásma mají podstatně lepší radio propagaci a signál jak lépe prostupuje překážky, tak doběhne dále. </p>

<p>V čem jsou si tedy UWB a xMax podobní? Především v tom, že oba využívají faktu, že za určitých podmínek lze vysílat signál na již používaném pásmu, aniž bychom ovlivnili původní signál. Česky bych tomu říkal něco jako signálový podkres. Tato hranice podle FCC leží někde u -41 dBm/MHz – tato hranice také tvoří takzvaný „FCC Part 15 limit“ – podkresovou hranici. </p>

<p>Proč UWB nepoužívá subgigové pásmo? Inu proto, že v subgigovém pásmu při použití UWB přeci jen docházelo ke zhoršení signálu podkreslovaných radiových sítí, což se jejich majitelům nelíbilo a především u VKV vysílačů s tím byly problémy. </p>

<p>xMax tenhle problém obchází tak, že většinu vysílacího výkonu směřuje do velmi úzkého frekvenčního spektra, které se dostane vysoko nad podkresovou hranici. Označení velmi úzké přitom zde znamená cca 6 kHz, tedy šířku úzkého hlasového kanálu, mimo šířku tohoto kanálu už je vysílaný signál rozprostřený do pásma širokého na obě strany cca 6 MHz ale také až 50 MHz (nevím, zda tím rozpětím jsou myšleny konstrukční verze, potenciální možnosti nebo jen chyby, oficiální dokumentace chybí). To by v praxi znamenalo, že xMax obsadí až 100 MHz šířky pásma, ačkoliv nad sebou nechá běžet klasické rádiové služby. Na obrázku zhruba tak vidíte, jak vypadá xMax v porovnání s UWB a dalšími technologiemi. </p>

<p><center>
<img src="/wp-content/uploads/20050719-xgobrazek.gif" alt="xMax technologie a ostatní" width="400" height="187" />
</center></p>

<p>A nyní finta: xMax nepoužívá onen úzkopásmový kanál pro vysílání přenášených dat, ale pouze jako jakýsi synchronizační kanál, nosná vlna. Pomocí této nosné vlny se synchronizují vysílače s přijímači tak, aby každý věděl, co kdy má dělat a čekat. Samotná data se přenášejí po onom širokopásmovém signálu (xG jej zve Flag Signal). Signál xMaxu je tedy úzký v čase a široký ve frekvenci – stejně, jako UWB. Používá se širokopásmová pulzně poziční modulace, čili data se zakódovávají jako časová prodleva mezi jednotlivými pulzy, tedy zhruba stejně, jako když mlátíte trubkou do ústředního topení ve snaze přenášet zprávu morseovkou. K tomu jen dodám, co říkal Carlo Kopp: <em>Pulse Position Modulation (PPM) was experimented with but never found serious commercial uses.</em></p>

<p>Díky tomu může být přenos dat zajištěn extrémně nízkým vysílacím výkonem na straně uživatelského terminálu. Pro větší vzdálenosti (kilometrové) jde o 0,5 až 1 mW, pro vzdálenosti v řádu stovky metrů o 0,5 pW (jojo, pikowatt). A tady je právě ten chyták. Jak dostat signál z přirozeného šumu pozadí, když je pod jeho hranicí? O to se má postarat takzvaný WPF -  Wavelet Pass Filter (je mi líto, český překlad neznám). A to je ta černá skříňka, protože jak ten by to mohl dělat, mi není jasné. Kontaktoval jsem prezidenta xG Joe Bobiera a ten mi osvětlil, že jde o součást jejich intelektuálního vlastnictví a tedy je z pohledu ostatních zatím WPF černou skříňkou. Pro fungování systému na tak nízkých vyzářených výkonech je to přitom evidentně nejpodstatnější část a až potud bylo vše jasné a uvěřitelné. Horší je to s představou, jak z pikowattových výkonů dokáže WPF vylovit data…  </p>

<p>Společnost xG slibuje, že v září 2005 předvede přenos na rychlosti 40 Mb/s s pokrytím cca 30 km od základnové stanice, přičemž bude využit menší než wattový vyzářený výkon a v subgigovém pásmu nedojde k zarušení ostatních frekvencí – použije se pásmo 900 MHz, což je v USA pásmo ISM, u nás by asi operátoři dost prskali. </p>

<p>Tož se budeme těšit. Jestli se jí to opravdu povede, bude to velmi zajímavé. Ostatně, xG nehodlá sama zařízení vyrábět, ale podobně jako Qualcomm spíše licencovat dalším stranám, takže vyvíjí pouze referenční design. V každém případě má xMax do komerčního nasazení ještě dále, než WiMax, ještě ani nevěřím, že to bude fungovat, ani neproběhly ostré testy, natož aby to už někdo alespoň přislíbil vyrábět. Prý bude jednou drtit WiMax i 3G. Tak uvidíme...
</p>