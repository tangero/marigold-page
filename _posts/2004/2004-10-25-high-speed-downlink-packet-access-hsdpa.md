---
ID: 1370
author: Patrick Zandl
categories:
- UMTS
- 3G
- Turboúvod do mobilních sítí
layout: post
oldlink: 'https://www.marigold.cz/item/high-speed-downlink-packet-access-hsdpa

  '
post_date: 2004-10-25 08:16:00
post_excerpt: Jak fungují rychlá paketová data HSDPA v sítích UMTS/3G
published: true
summary_points:
- HSDPA (Release 5) zavádí rychlejší datové přenosy v UMTS sítích, očekávané kolem
  roku 2006.
- NodeB přebírá plánování a řízení dat (MAC-HS) od RNC, snižuje zpoždění.
- HS-DSCH kanál umožňuje sdílení vzdušného rozhraní více uživateli rychlostí až 14,4
  Mb/s.
- Release 6 plánuje vylepšení HSDPA, včetně rozšířeného reportování CQI a EUDCH pro
  uplink.
title: 'High Speed Downlink Packet Access (HSDPA)

  '
---

<p>
O datech v UMTS síti už něco málo víme, především to, kde jsou jejich zádrhely. Už tušíme, že to s rychostí nemusí být slavné, ale také to, že to slavné není ani se zpožděním a časovým rozptylem při přenosu dat, tedy se dvěma kvalitativními parametry, na které jsou služby vyžadující QoS háklivé. O HSDPA jsem již trochu psal, ale nyní to vezmeme maličko podrobněji. Jen připomínám, že HSDPA je systém rychlých dat pro stahování, tedy downlink, pro uplink se používá stávající mechanismus, případně se do Release 6 počítá s novým… </p>

<p>
Release 5 přichází s novým mechanismem pro přenos rychlých dat v UMTS síti a protože se očekává, že tento mechanismus se bude uplatňovat v sítích kolem roku 2006, lze také očekávat, že se s ním potkáme záhy i v ČR. Jde o HSDPA, High Speed Downlink Packet Access. </p>

<p>
HSDPA je založeno na několika inovacích architektury sítě, díky nimž se dosahuje nižšího zpoždění, rychlejších reakcí na změnu kvality kanálu a zpracování H-ARQ, tedy hybrid automatic repeat request, hybridního automatického požadavku na opakování přenosu.
</p>

<!--more--><p>
Další změny jsou provedeny přímo na radiové části sítě, tedy na RNC (Radio Network Controler) a NodeB (základnová stanice). Hlavní změnou, která přispívá ke zrychlení toku dat a odstranění zpoždění a rozptylu, je přesunutí některých úkolů ze samotného RNC na NodeB. Základnové stanice se nyní namísto RNC starají o plánování a řízení přímo na Vrstvě 1, většina funkcí MAC důležitých právě pro zpoždění a rozptyl dat je z RNC v Release 5 přesunuta na NodeB. Díky tomu data urazí kratší trasu před tím, než se dekódují a třeba se zjistí, že něco není s nimi v nepořádku a že je potřeba poslat je znovu. Snižují se tím nároky na dobu jejich přenosu, ale i na RNC, naopak je potřeba výkonnější hardware NodeB. MAC (Medium Access Control, Řízení přístupu k médiu) se v Release 5 nově nazývá MAC-HS, čímž dává tato funkce najevo, že je dislokována na NodeB. </p>

<p>
Oproti Release 99 zavádí HSDPA nová schémata pro přenos paketových dat. Namísto rychlého řízení vysílacího výkonu a proměnného faktoru rozprostření se používá dynamická adaptivní modulace a kódování, vícekódové operace, rychlé plánování a retransmise na fyzické vrstvě. O co jde, si řekneme záhy. </p>

<h4>High-Speed Downlink Shared CHannel (HS-DSCH)</h4>
<p>
Pro HSDPA je definovaný nový typ transportního kanálu nazvaný High-Speed Downlink Shared CHannel (HS-DSCH). Tento transportní kanál umožní více uživatelům sdílet dynamicky vzdušné rozhraní a to až o špičkových rychlostech 14,4 Mb/s. V HS-DSCH jsou použity 2 ms časové přenosové intervaly (TTI) a pevný rozprostírací faktor 16, umožňující využívat 15 paralelních kódů pro uživatelský provoz a signalizaci. </p>

<p>
Kanál HS-DSCH používá modulaci QPSK a 16-QAM, adaptaci linky a retransmisi na fyzické vrstvě pomocí H-ARQ. </p>

<p>
Řízení HSDPA přenosu má na starosti kanál High-Speed Shared Control CHannel (HS-SCCH), jenž přenáší informace o použité modulaci, rentrasmisi a další řídící informace. </p>

<h4>Rychlé plánování (Fast scheduling)</h4>
<p>
Plánování přenosu rychlých dat provádí v Release 99 RNC. Jak jsme si již řekli, u HSDPA jde plánování blíže k uživateli a provádí se přímo na NodeB. HSDPA využívá zpětnou informaci od mobilky o kvalitě kanálu, schopnostech mobilky, požadavcích na kvalitu služby a dostupných radiových zdrojích k tomu, aby přesněji plánovala a přenášela data. Plánování na straně NodeB je pro přenos dat pružnější, než když jej provádělo centrálně RNC. </p>

<h4>Rychlá retransmise a H-ARQ</h4>
<p>
Pokud se nepodaří dekódovat data přenášená na radiovém kanálu (interference atd), mobilka okamžitě požaduje znovupřenesení dat – retransmisi. Zatímco v Release 99 je retransmise požadována od RNC, v HSDPA je prováděna už NodeB. Retransmisi může NodeB nabídnout rovnou ze svého vyrovnávacího buferu, takže k ní dojde velmi rychle bez čekání na data uložená hlouběji v síti. Tyto operace na Vrstvě 1 jsou pojmenovány jako hybridní automatický požadavek na opakování přenosu – H-ARQ. </p>

<h4>Zpětná informace o kvalitě kanálu (Channel Quality Feedback)</h4>
<p>
Pro obsloužení Indikátorů kvality kanálu (CQI – Channel Quality Indications) a signalizace ACK/NACK pro H-ARQ směrem od mobilky je definován uplink kanál High-Speed Dedicated Physical Control CHannel (HS-DPCCH). Na tomto kanálu sbírá základnovka GQI každého aktivního uživatele a plánuje z těchto dat přidělení přenosového kanálu HS-DSCH</p>

<p>
V Release 5 je používána fixní velikost CQI a CQI obsahuje velikost transportního bloku na HS-DSCH, počet kódů a modulaci, s níž můžou být data přijímána při dané pravděpodobné chybovosti v periodě tří timeslotů. Je tedy zřejmé, že CQI je docela důležité pro správnou funkci rychlých dat a do Release 6 se připravuje několik jeho úprav, zatím neschválených. Mělo by především jít o možnost vyžádat si dodatečný CQI update přes vzkaz poslaný Vrstvou 1, použití dodatečných CQI v průběhu aktivity downlinku a především o schopnost mobilky ukládat CQI hodnoty po určitou dobu a reportování síti průměry těchto hodnot. To by bylo velmi důležité pro plánování a zjišťování průběžné kvality linky a osvobodilo by to od podobných operací samotnou síť. </p>

<p>
Release 6 také předpokládá rozšíření obsahu CQI reportů a jejich dynamické rozšiřování v použití na časovém duplexu TDD. </p>

<p>
Jak CQI probíhá, vidíte na obrázku. </p>

<p>
<img src="/assets/20041025-cqi.gif" alt="CQI" width="469" height="168" /></p>

<h4>Adaptivní modulace a kódování</h4>
<p>
Schopnost rychlého plánování HSDPA lze výhodně zúročit pomocí adaptivní modulace a kódování, díky čemuž se k uživateli dostane maximální možná rychlost dat, s jakou si linka jeho kvality dokáže poradit. Modulační a kódovací schémata jsou dynamicky měněna podle kvality radiové linky, zatímco výkon zůstává konstantní. </p>

<p>
Kromě modulace QPSK nabízí HSDPA také 16-QAM, která je výkonější, ovšem jen v příznivějších podmínkách. </p>

<h4>Výsledek změn</h4>
<p>
Po provedení uvedených změn v UMTS síti na Release 5 jsme došli k rychlému kanálu pro stahování dat zvanému HS-DSCH, jenž nabízí špičkové rychlosti až 14,4 Mb/s za sdílení cca 15 uživatelů. Hlavním hnacím motorem tohoto výkonu je 16-QAM mdoulace a hybridní automatický požadavek na opakování přenosu H-ARQ, jenž se také stará o snížení latence a rozptylu. Snížení latence je ale dosaženo především zkrácením TTI na 2ms z původních 10 ms uvedených v Release 99. </p>

<h4>Výhledy HSDPA pro Release 6 a dále</h4>
<p>
Některé důležité přepokládané zásahy do HSDPA v Release 6 jsme si již uvedli. Jde především o rozšířené reportování CQI a jeho dynamický rozsah v TDD. </p>

<p>
Další novinkou bude zřejmě vícenásobný současný přenos do mobilky v rámci HSDPA subframe. Zatím je v rámci subframe možno vykonat jen jeden přenos, ale někoho napadlo, že hromadící se H-ARQ požadavky by si zasloužily vícenásobný současný přenos, kdy by se zakomponovaly všechny nahromaděné požadavky do jednoho subframe a odeslaly se najednou. </p>

<p>
Znovupoužití rozprostíracích kódů je další důležitý aspekt, protože jejich počet je na HS-DSCH kanálu omezen. Znovupoužití kódů se v UMTS Release 99 řeší časovačem neaktivity, po němž kódy vyprší, jenže jsou typy aplikací, u kterých to dělá problém – například webový chat, kde se data obnovují jednou za čas a tento čas je delší, než časovač neaktivity v UMTS síti. Každé nové přidělení kódů uživateli data radikálně zdrží. </p>

<p>
Částečně přidělený fyzický kanál – stávající specifikace předpokládá, že každému uživateli HSDPA je vyhrazen kanál pro uplink a downlink. Samozřejmě by ale služby vyžadující nízkou přenosovou rychlost zbytečně blokovaly nevyužívaný kanál. Předpokládá se do budoucna, že by mělo stačit přidělit takový kanál &#8220;částečně&#8221; – tedy s tím, že ho mohou využívat i ostatní uživatelé. </p>

<p>
Výrazné změny by měly přijít také do režimu časového duplexu, který je v UMTS takovým odstrkovaným dítětem, o němž se sice tvrdí, že má větší perspektivu do budoucna, než frekvenční duplex, jeho standardizace a rozvoj ale o jednu třídu za FDD pokulhává. Zejména kvůli větší komplexnosti problému. </p>

<p>
Jak vidíme, HSDPA dotlačilo do UMTS specifikace určité prvky decentralizace. Funkce, dříve blíže přimknuté k Jádru sítě, se postupně přesouvají blíže uživateli, čímž se zkracuje doba nutná pro přenos a v případě chyby přenosu také pro opakování, tedy se eliminuje zpoždění a rozptyl. </p>

<p>
Zavedení výkonnějších modulačních a kódovacích schémat není samospasitelné a je třeba počítat s tím, že HSDPA bude fungovat spíše či především tam, kde zástavba základnových stanic bude dostatečné hustá a radiové prostředí dostatečně vyladěné na to, aby se minimializovaly interference a bylo možné použití těchto schémat. </p>

<p>
Novinkou v Release 6 pak má být nový kanál pro rychlé odesílání dat, jenž doprovodí HSDPA. Jmenuje se Enhanced Uplink for Dedicated CHannels (EUDCH) a z HSDPA vlastně reverzně přebírá všechny vlastnosti. </p>

<p>
Do dalších Release se počítá především s důsledným uplatněním inteligentních složených antén MIMO a také beamformingu, kdy základnové stanice mění směr svého pokrytí v závislosti na tom, kde jsou její uživatelé.
</p>