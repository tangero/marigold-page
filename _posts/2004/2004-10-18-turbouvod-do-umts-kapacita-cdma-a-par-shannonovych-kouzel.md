---
ID: 1362
author: Patrick Zandl
categories:
- UMTS
- 3G
- Turboúvod do mobilních sítí
layout: post
oldlink: 'https://www.marigold.cz/item/turbouvod-do-umts-kapacita-cdma-a-par-shannonovych-kouzel

  '
post_date: 2004-10-18 07:42:00
post_excerpt: ''
published: true
summary_points:
- Kapacita sítě definuje počet simultánních uživatelů a souvisí s rychlostí.
- Shannonova teorie určuje maximální kapacitu kanálu dle šumu, signálu a šířky pásma.
- CDMA využívá kódové rozprostření do spektra, široký kanál a nízký poměr signál/šum.
- UMTS s 5 MHz kanálem má teoretickou kapacitu 20 Mb/s, reálně méně.
title: 'Turboúvod do UMTS: Kapacita, CDMA a&nbsp;pár Shannonových kouzel'
---

<p>
Minule jsem slíbil, že se konečně dostaneme k tomu, proč a jak zrychlit data v UMTS síti. Lhal jsem, asi nedostaneme. Dneska se ještě trochu podíváme na problematiku kapacity v radiových sítích. Proč? Protože kapacita a rychlost jsou spojené nádoby. </p>

<p>
Začněme polopaticky: kapacita sítě je vlastně počet uživatelů, jejichž komunikace může být považována za simultánní. S tou simultánností to samozřejmě je trochu problém, protože ta komunikace nemusí být z technického hlediska simultánní (což třeba časový duplex), měla by se ale tak jevit uživateli.
</p>

<!--more--><p>
Podívejme se na to, jaké faktory kapacitu v radiových (víceuživatelských) sítích ovlivňují:</p>

<ul>
<li>	požadovaná čistá chybovost pro konkrétní aplikaci po dekódování a dopředná korekce chyb (FEC)
<li>efektivita modulace (v bps/Hz)
<li>režie pro kódování
<li>techniky vícenásobného přístupu (FDMA,TDMA,CDMA,SDMA,OFDM atd)
<li>diverzita (časová, prostorová, kódová, frekvenční atd)
<li>režie pro ohraničující pásma, časy atd. 
<li>hard a soft handovery v síti, respektive jejich režie
<li>směrové a všesměrové antény
<li>automatické řízení výkonu jak na dopředném, tak na zpětném kanále. 
<li>Inteligence systému v oblasti dynamického přidělování zdrojů, která respektuje měnící se požadavky na služby. Příkladmo DPA – dynamické přidělení paketu. 
</ul>
<p>
Jak vidíme, je to podobný sled faktorů, jaké jsme si uvedli jako směrodatné pro rychlost radiové sítě – až na to, že zde jsme podrobněji rozvedli faktory, které se projevují právě na straně radiového rozhraní. </p>

<p>
Nyní si dáme maličko zbytné matematiky – můžete ji samozřejmě nahradit slepou vírou ve výsledné tvrzení. </p>

<h4>Shannon - Hartleyova teorie</h4>
<p>
Pro vyjádření kapacity se v telekomunikacích již od pravěku (konkrétně rok 1948.) používá takzvaná Shannonova teorie <i>(ano. Claude Shannon je praotec úřednických šanonů, protože jeho práce na poli kapacity zasahovala prakticky do všech způsobů přenosu dat. A jeho <a href="http://www.vesmir.cz/clanek.php3?CID=5988">životopis zde</a>)</i>. Shannonova teorie vyjadřuje kapacitu kanálu C v bitech za sekundu pro kanál, na němž kromě užitečného signálu působí také bílý aditivní gaussovský šum (označovaný jako AWGN). Takový kanál nepochybně nemá nekonečnou kapacitu, neboť zmíněný šum na kanálu nedovolí rozlišit na straně přijímače jemnější změny zpracovávaného signálu, než je vlastní úroveň šumu. Shannon - Hartleyova teorie pak umožňuje vyjádřit maximální <b>kapacitu kanálu</b> jako:</p>

	<blockquote><p>
C = W log 2 (1+S/N) <i>[bitů/s]</i></p>
</blockquote>
<p>
Kde S je střední výkon signálu na vstupu přijímače, N je střední výkon šumu v patřičném pásmu a W je šířka kanálu v Hz. </p>

<p>
Kapacita kanálu je tedy ovlivňována výkonem šumu, signálu a šířkou pásma. </p>

<p>
Normovanou kapacitu kanálu bychom tedy odvozeně mohli vyjádřit jako </p>

	<blockquote><p>
C/W <i>[bits/s/Hz]</i>  =  log2(1+S/No . W) </p>
</blockquote>
<p>
Kde No je spektrální výkonová hustotu šumu v Hz a W je šířka kanálu v Hz. </p>

<p>
Ze vzorců vyplývá několikero poučení. Především ten, rychlost přenosu je přímo úměrná šířce pásma a pravděpodobnost chyb je nepřímo úměrná poměru S/N tedy poměri signál / šum <i>(anglicky značené jako SNR, signal – noise ratio)</i>. Dále z něj zjistíme,  že normovaná kapacita kanálu C/W je závislá na jediné proměnné a to na normované šířce pásma W. </p>

<p>
Pokud je normovaná šířka pásma pod hodnotou 1, klesá rapidně i normovaná kapacita kanálu C/W, avšak poměr signál-šum se výrazně zvyšuje. </p>

<p>
Takto pracují úzkopásmové (narrowband) telekomunikační systémy, tedy ty &#8220;klasické&#8221; komunikační systémy. Poměr signál/šum je > 1, používá se tedy vysoký vysílací výkon a malá šířka pásma. </p>

<p>
Pokud se normovaná šířka pásma W dostane nad hodnotu 1, je poměr signál/šum < 1. To má jeden neblahý dopad: na straně přijímače totiž není možno získat přenášenou informaci jednoduchým poslechem radiového signálu. Z toho důvodu tradiční komunikační technologie tento typ přenosu zcela opomíjely.</p>

<p>
<img src="/assets/20041018-normalizovanasirkapasma.jpg" alt="Fuj, ten obrázek ale vypadá..." width="400" height="274" /> </p>

<p>
Časem se ale ukázalo, že vhodným kódováním a následným dekódováním lze informace velmi výhodně přenášet, protože při velkých šířkách pásma se normovaná kapacita kanálu velmi blíží teoreticky dosažitelnému maximu (1,44). Informací lze navíc do takto širokého kanálu najednou rozmístit více – používá se takzvané rozprostření do spektra. A tím jsme se dostali k samé podstatě CDMA – CDMA je vlastně kódové rozprostření do spektra využívající širokého kanálu a poměru signál / šum < 1. </p>

<p>
CDMA je nejmladší variantou radiokomunikačních multiplexů – po multiplexu frekvenčním a časovém (FDMA a TDMA). Jeho výhodou je kromě velmi vysoké přenosové kapacity také vysoká odolnost proti rušení, ať již přirozenému nebo úmyslnému. </p>

<h4>Jak je to konkrétně v UMTS</h4>
<p>
Pokud bychom do Shannonova vzorce dostadili konkrétní hodnoty pro UMTS, kde je šířka kanálu 5 MHz, snadno zjistíme, že maximální kapacita dle Shannona je 20 Mb/s. Vzhledem k tomu, že samotné UMTS dnes definuje podle Release 99 rychlosti do 2 Mb/s, chápeme asi, že určitý prostor k dalšímu vylepšování zde stále je.</p>

<p>
Také vidíme, proč se UMTS rozhodlo pro využití šířky pásma 5 MHz oproti jiným CDMA systémům (CDMA2000 používá 1,25 MHz) – chtělo časem vytěžit co nejvyšší přenosovou kapacitu a šířka 5 MHz byla považovaná za ještě technicky snadno a mobilně realizovatelnou. </p>

<p>
Je třeba říci, že Shannonova limitu se v praxi nedosahuje, od toho je to ostatně limit. Zlepšováním modulace se k němu ale můžeme trochu blížit. </p>

<p>
Pro příklad předpokládejme šířku kanálu 1 MHz a 16QAM modulaci, která má modulační efektivitu 4 bps/Hz, pokud ale odpočteme různé režie, dostaneme se zhruba na 3 bps/Hz. To na 1 MHz kanálu dělá maximální kapacitu 3 Mb/s. Takovýto kanál bychom dále mohli rozdělit například přes TDMA pro deset uživatelů, takže každý by měl vyhrazenou rychlost 300 Kb/s. Tato kalkulace ovšem předpokládá, že poměr S/N na jednotlivých mobilkách je adekvátní pro dosažení přiměřené chybovosti po dekódování a korekci chyb. Se zvoleným vysílacím výkonem a ziskem antény to znamená limit ve vzdálenosti, na kterou služba může být poskytována. Nic překvapivého… </p>

<p>
Pokud bychom zvolili efektivnější modulační schéma, například 64QAM s modulační efektivitou 6 bps/Hz, dostaneme se na vyšší rychlosti, snížíme ale také dosah, po který tyto rychlosti mohou být poskytovány, protože je potřeba větší odstup signálu od šumu, aby byla dosažena patřičný poměr chybovosti. Čím efektivnější je modulační schéma, tím náchylnější a citlivější je také k chybovosti na lince.  Povšimněte si tedy, že jednotlivé zvyšování rychlostí probíhá jak u GPRS, tak u EDGE změnou modulačních schémat, přičemž každá taková technologie nabízí několik modulačních schémat, aby byla schopna volit takové, které odpovídá stavu přenosové trasy mezi mobilkou a základnovou stanicí, zejména tedy odstupu signál / šum. </p>

<p>
Výsledek tohoto článku: prakticky jsme si ukázali, že rychlosti nabízené v UMTS sítích jsou na zlomku svých teoretických limitů a tak lze přenosové rychlosti zvyšovat. Existují pro to rovněž vhodné nástroje jako jsou modulační schémata a dostatečná šířka pásma, je třeba je ale podporovat dostatečně výkonným hardware v mobilkách, aby byl mobil schopen patřičnou modulaci (založenou na stále složitějším matematickém vzorci) zvládnout v reálném čase. </p>

<p>
Na závěr jen doufám, že jsem vzorce příliš nepomotal, přepisoval jsem je asi desetkrát mezi českými a anglickými verzemi a nejrůznějšími variantami :(
</p>