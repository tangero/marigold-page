---
ID: 3040
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/lte-unlicenced-o-co-jde-v-pripade-lte-v-nelicencovanem-pasmu

  '
post_date: 2016-03-01 09:57:53
post_excerpt: ''
published: true
summary_points:
- Vize provozu LTE v nelicencovaném pásmu představena Qualcommem a Ericssonem v roce
  2013.
- LTE v nelicencovaném pásmu by umožnilo zjednodušení výstavby LTE pokrytí v režimu
  nanocell.
- LTE má vyšší efektivitu využití spektra než WiFi, ale může mít problémy s soužitím
  s WiFi.
- Cena a změna poměrů na trhu jsou klíčové problémy spojené s implementací LTE-U.
title: LTE-Unlicenced, o&nbsp;co jde v&nbsp;případě LTE v&nbsp;nelicencovaném pásmu
---

Vize provozu LTE v nelicencovaném pásmu je stará pět let, nakonec ji ale představil Qualcomm a Ericsson koncem roku 2013.  Od té doby se neví přesně, zda jde o myšlenku heretickou nebo spásnou. Jak tedy?

Update 12/2024: vývoj pokročil, aktualizované informace [k provozu LTE/5G v nelicencovaném pásmu jsou v tomto článku](/mobilnisite/laa-5gnr-u).

<!--more-->

<p>LTE je moderní rádiová technologie pro telekomunikační sítě pracující v licencovaném pásmu, což jí přináší řadu výhod, ale také to naráží na problémy především v nedostatku vhodných dalších pásem, tedy na problémy kapacitní. Ericsson technologii nazývá LTE-LAA, tedy License Assisted Access, Licencí asistovaný přístup.</p>

<p>Myšlenka zprovoznit LTE v nelicencovaném pásmu, především v pětigigaherzovém pásmu, by umožnila řadu věcí, především by zjednodušila výstavbu LTE pokrytí v režimu nanocell, tedy pro pokrytí v rámci domů. K tomu se dosud používaly nanocelly pracující v licencovaném pásmu, ty logicky směl dodávat jen provozovatel mobilní sítě a bylo s tím obecně dost problémů na to, aby se rozšířily. Zákazníci tím pádem používali ve firmách připojení přes WiFi, což všechny moderní telefony umožňují, až na to, že po něm zpravidla nepřenesou služby operátora, jen internet. To znamená, že zákazníci se postupně snaží vyvazovat ze služeb operátora a přesouvají se na služby třetích stran jako iMesssages, Hangout a další. Proto takový zájem operátorů o LTE-U, pomohl by této strukturální změně zabránit.</p>

<p>LTE by mělo proti WiFi celou řadu výhod. Je to dnes velmi vyspělý a dospělý ekosystém umožňující celou řadu služeb včetně kontroly QoS, dynamické změny šířky pásma, datové průchodnosti atd. Podstatnou nevýhodou může být cena a jistá závislost na operátorech, u čehož se pozastavíme později.</p>

<h3>Technologické rozdíly: vyšší efektivita využití spektra</h3>
<p>LTE je mírně efektivnější na rádiovém rozhraní než WiFi v případě, že je používáno jedno uživatelské zařízení, ale s růstem počtu uživatelských terminálů v síti výhoda vyšší efektivity LTE na rádiovém rozhraní dramaticky roste. Podle japonských studií je efektivita LTE-U oproti WiFi vyšší 1,6x, což je v rádiovém světě dost. Je to dáno lepším řízením přístupu, lepší koordinací i vyšší variabilitou přístupových metod v LTE, kdy lze použít jak frekvenční, tak časový multiplex.</p>

<p><img title="Link level Carrier Aggregation.gif" src="/assets/Link-level-Carrier-Aggregation-1.gif" alt="Link level Carrier Aggregation" width="599" height="290" border="0" /></p>

<p><em>Na obrázku je porovnání metod LTE v licencovaném pásmu, agregace WiFi a LTE v nelicencovaném pásmu. </em></p>

<p>Značnou výhodou LTE může být i schopnost přenášet data na více radiových frekvencích, kdy downlink nebo uplink může běžet už v licencovaném pásmu, to podle místní situace v rádiovém prostředí. LTE-U ovšem počítá s tím, že downlink minimálně z části běží po licencované frekvenci operátorova LTE a tedy dojde k provedení klasické autentizace přes prostředky LTE sítě. Typickým použitím LTE-U pak má být režim <strong>SDL</strong>, <em>Supplemental Down Link</em>. kdy se LTE v nelicencovaném pásmu používá jen pro příjem velkých balíků dat, pro jejich odesílání a částečně i pro příjem se používá LTE v licencovaném pásmu. Druhou variantou, která pochází také z dílny Qualcommu, má být <strong>MuLTEfire</strong>, nabízející přístup přes LTE čistě v nelicencovaném spektru. U zařízení MuLTEfire dokonce není ani potřeba SIM karta</p>


<p><img title="overview-on-mobile-broadband-technologies-23-728.jpg" src="/assets/overview-on-mobile-broadband-technologies-23-728.jpg" alt="Supplemental DownLink on LTE" width="471" height="364" border="0" /></p>

<p>Další výhodou může být mírně vyšší dosah LTE oproti WiFi ve stejném frekvenčním pásmu, což souvisí s jiným způsobem zpracování signálu a tedy lepší extrakcí informace od šumu a to i za použití MIMO.  </p>

<h3>Problém 1: soužití s WiFi</h3>
<p>Co může být zádrhel? Potenciál problematického soužití s WiFi. Na pětigigahercové WiFi vsází řada firem, které mohou LTE-U do úsměvu pěkně šlápnout, jako třeba Google, který to již udělal a postěžoval si k FCC, že LTE-U bude rušit WiFi sítě. Stejně negativistický postoj má Apple, který vidí v 5Gz WiFi především firemní sítě a do podpory telekomunikačních technologií na úkor internetových se moc nehrne. Qualcomm, Ericsson a další momentální partneři se dušují, že LTE-U bude respektovat WiFi a že to soužití bude dobré. Ostatně, pásmo 5GHz je volné a za dodržení určitých podmínek se tam může napasovat kdokoliv. Jednou z těch podmínek je aplikace LBT - tedy “poslouchej než mluvíš” - funkce, kdy před zahájením vysílání zařízení studuje provoz v pásmu a podle toho jednak vybere nejlepší frekvenční pásmo a přizpůsobí se provozu v rádiovém pásmu.</p>

<p><img title="qualcomm-making-the-best-use-of-unlicensed-spectrum-28-638.jpg" src="/assets/qualcomm-making-the-best-use-of-unlicensed-spectrum-28-638.jpg" alt="Qualcomm making the best use of unlicensed spectrum 28 638" width="500" height="281" border="0" /></p>

<p>A tady začíná problém, o kterém mluví Google. LTE má kanálový krok 100 kHz, WiFi 5 MHz a v pásmu 5GHz spíše 20 MHz. Pro uživatelský terminál (UE) nebo základnovky eNB bude problematické funkci LBT korektně zrealizovat, protože bude po svých skocích prohledávat příliš široké pásmo. Nicméně Qualcomm tvrdí, že se to zvládne, oponenti požadují další testy. Dobrá studie koexistence, ovšem <a href="http://www.lteuforum.org/uploads/3/5/6/8/3568127/lte-u_forum_lte-u_technical_report_v1.0.pdf">vytvořená LTE-U Fórem, je tady</a>.</p>

<p><img title="lteu-porovnani-wifi.png" src="/assets/lteu-porovnani-wifi.png" alt="Lteu porovnani wifi" width="599" height="493" border="0" /></p>

<p>Americký regulátor FCC povolil koncem ledna Qualcommu ve spolupráci s Verizonem provést reálné testy LTE-U ve dvou městech, podle toho bude vyhodnocen dopad na rušení WiFi.</p>

<p><img title="extending-the-benefits-of-lte-advanced-to-unlicensed-spectrum-8-638.jpg" src="/assets/extending-the-benefits-of-lte-advanced-to-unlicensed-spectrum-8-638.jpg" alt="Extending the benefits of lte advanced to unlicensed spectrum 8 638" width="500" height="281" border="0" /></p>

<h3>Problém 2: cena</h3>
<p>LTE je rozhodně dražší technologie, než WiFi a celá řada nákladů jde za patenty, část za náročnějším křemíkem a nutností napájení na pohon křemíku. Vyšších nákladů se oprávněně bojí všichni, kdo jsou na straně WiFi a připomínají, že patenty se vyrovnávají zvláště. Qualcomm s Ericssonem uklidňují, že náklady na patenty jsou zahrnuté v cenách jimi dodávaných čipových sad, což ale překvapivě neuklidnilo každého. Cena mobilů, kde bude i LTE-U se prakticky nezvýší, problém bude ale u zařízení, které se dříve spoléhaly jen na WiFi a nově by do nich přibylo i LTE-U - tam bude cena vyšší. O kolik? Nu, odhadem tak dvacet dolarů na zařízení ze začátku.</p>

<h3>Problém 3: změna poměrů na trhu</h3>
<p>Problém koexistence a ceny je veřejně na stole, podle mě je ale jen manifestací nejpodstatnější obavy, tedy té, že by mohlo dojít k diametrální změně na trhu, kde o nadvládu soupeří model střežené zahrádky provozované telekomunikačními operátory za jejich pravidel a model volného lesa postaveného na otevřenosti a nediskriminačním přístupu jednotlivých spolupracujících internetových firem.</p>

<p>Tyto dva modely se v poslední době docela sbližují, to se nedá přehlédnout, dlouho vládla střežená zahrádka, nyní se trh překlopil především díky Apple a Google do volného lesa. Jenže nástup LTE-U by mohl ledasco změnit. Řada mobilních operátorů už jede mobilní telefony formou paušálního poplatku, kdy všechno je v ceně. Zákazník už si dneska mobil kupuje především kvůli internetu, ale SMS a hlasové služby dostává zdarma k paušálu navíc, tak proč by je odmítal, proč by přecházel na Hangout či FaceTime, když hlas a zprávy jedou se všemi kompatibilně i přes operátorské služby. Tohle pronikání volného lesa do telekomunikací řádně zbrzdilo a až Messenger se SnapChatem a WhatsApp zase rozdráždil situaci. Pokud by se ale podařilo klienty postupně přetahávat i doma a ve firmách k LTE-U, tedy do operátorské sítě, mohlo by to zase váhy vychýlit. Trh přitom duopol potřebuje a z boje telekomunikačních operátorů s internetovými poskytovateli významně profituje jak cenově, tak nebývalým spektrem služeb.</p>

<h3>A to je zatím vše</h3>
<p>A to je celé, co lze o LTE-U říci. Na jednu stranu je to technologie, která za vyšší cenu nabídne vyšší kvalitu, na stranu druhou je pochybné, zda vyšší kvalitu někdo za příplatek ocení, když zavedené řešení je velmi funkční, vcelku bezproblémové a navíc nekontrolované úzkou skupinou trhu. Pravda je, že klienti si všímají, že domácí WiFi připojení s routerem, co jim stojí na stolku, je méně kvalitní a pomalejší, než dobrá LTE přípojka vzdálená kiláček vzdušnou čarou, jenže co naplat, za čtvrt hoďky stahování filmu jim pípne SMS, že datový limit je pryč a to je to, co se počítá. Navíc je to především věc poslední míle, která v řadě případů není nejkvalitnější.</p>

<p>Je velmi pravděpodobné, že operátoři LTE-U prosadí, již je součástí 3GPP standardů, ačkoliv není návrh kompletní. Je také logické, že operátoři se tím snaží jít proti podobné iniciativě z tábora WiFi, která umožní přenášet operátorské služby přes WiFi, na mysli mám technologie MAPCON, eSaMOG, IARP nebo WORM a obecně platformu heterogenních sítí zvanou “hetnet”. Tady je třeba říct, že se bojuje především o firemní klienty, v oblasti běžných uživatelů se zdá být dobojováno a s mírnou mírou podrazivosti klid zbraní na obou frontách do vynalezení další zbraně. </p>