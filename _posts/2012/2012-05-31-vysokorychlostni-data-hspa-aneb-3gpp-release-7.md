---
ID: 2428
author: Patrick Zandl
categories:
- LTE
- 3G
- Mobilní sítě
layout: post
oldlink: 'https://www.marigold.cz/item/vysokorychlostni-data-hspa-aneb-3gpp-release-7

  '
post_date: 2012-05-31 14:47:12
post_excerpt: Zásadní novinkou v Release 7 (R7) a Release 8 (R8) je další rozšíření
  vysokorychlostních datových přenosů HSPA na HSPA+, pod čímž se skrývá zvýšení rychlosti
  na downlinku i uplinku."
published: true
summary_points:
- HSPA+ rozšiřuje vysokorychlostní datové přenosy v Release 7 a 8.
- MIMO (vícecestný vstup/výstup) zlepšuje kvalitu signálu pomocí více antén.
- QAM modulace v R7 zvyšuje přenosovou rychlost bez MIMO.
- CPC (kontinuální paketové připojení) snižuje zátěž sítě a spotřebu energie.
title: Vysokorychlostní data HSPA+ aneb 3GPP Release 7
---

<p>V přehledu vývojových verzí UMTS/3G sítí jsem se zadrhl u <a href="http://www.marigold.cz/item/umts-release-6">Release 6</a> – další Release měly už tu smůlu, že jsem měl dost jiné práce. Tak alespoň zpětně a s ohledem na to, že funkcionality (vybrané) z nových Release se pomaličku dostávají i do českých mobilních sítí.</p>


<!--more-->


<p>Zásadní novinkou v Release 7 (R7) a Release 8 (R8) je další rozšíření vysokorychlostních datových přenosů HSPA na HSPA+, pod čímž se skrývá zvýšení rychlosti na downlinku i uplinku. Je ale také spravedlivé říct, že ačkoliv se HSPA+ někdy označuje za 4G, jde stále spíše o předpokoj – nikoliv jenom definičně, rychlostmi slíbenými a nedosahujícími předpokladů pro 4G, ale také architekturně. Sítě v Release 7 stále vypadají jako klasické UMTS sítě a zásadní struktzurální obměnu v podobě HetNet a SON mají před sebou. Jen tu a tam vypadne nějaká bedýnka nebo se přesune směrem k NodeB.</p>

<p>A do třetice je důležité připomenout, že HSPA+ (z hlediska uživatele největší přínos R7) kontinuálně pokračuje svůj rozvoj v Release 8. Zatímco R7 přináší jako největší vklad technologii MIMO, tedy vícecestný vstup a výstup signálu, R8 lze charakterizovat pomocí DC – Dual Carrier – přenosu signálu na dvou nosných, čili Dva Přenašeče. Namísto 5 MHz šířky pásma, jakou UMTS doposud předpokládalo, lze v DC použít dvojnásobek. Další vývoj (po Release 9) půjde směrem ke spřahování větších balíků přenašečů – čtyř a více a to dokonce v různých frekvenčních pásmech, R8 ještě bude kontumačně počítat s tím, že ony dva přenašeče jsou ve stejném pásmu, čili třeba 2,1 GHz. </p>

## MIMO

<p>Nejprve se tedy zastavme u MIMO – <strong>Vícecestného vstupu a výstupu signálu</strong> (Multiple In – Multiple Out). Technologie je známa delší dobu, dnes se s ní běžně setkáváme ve WiFi sítích – zařízení, která mají více antén. Základní úvaha je jednoduchá: pokud může zařízení vysílat z více antén a na více anténách signál přijímat, bude možné si vybrat lepší kvalitu signálu, případně se snažit o rekonstrukci dat. Je to možné díky vícecestnému odrazu, kdy do antény přijímače dorazí nejenom původní signál, ale i jeho odrazy od překážek, které jsou časově zpomaleny a fakticky se projevují jako šum. Do toho přidejme jinou komunikaci sousedních zařízení (plus jejich odrazy) a je jasné, že nějaká snaha šum odfiltrovat bude prospěšná. Což je to, o co se MIMO účinně snaží.</p>

<p>Jen pro pořádek připomenu, že integraci MIMO do uživatelského terminálu (aka mobilky aka UE) nemusíte na první pohled poznat, nejsou to dvě antény trčící z mobilu, ale spíše dvě integrované antény na opačných koncích telefonu nebo dokonce jedna rozdělená na dvě poloviny, jelikož s ohledem na vlnovou délku už těch pár centimetrů udělá své. Na základnové stanici se používá koncept dvou vertikálně polarizovaných antén vzdálených minimálně 10 lambda (cca 1,4 m) nebo jedna anténa s polarizační diverzitou posunutou o 45 stupňů.</p>

<p>V MIMO pro HSPA+ R7 se používá koncept 2x2 MIMO, tedy dvě antény na základnové stanici a dvě na uživatelském terminálu, mobilce. Teoretická přenosová rychlost zde může dosáhnout až 28 Mb/s pro downlink, pro uplink v HSPA+ není MIMO využíváno. Jde tedy pouze o zrychlení dat přijímaných na mobilku.</p>

<p><img style="float: right;" src="/assets/mimo-schema.png" alt="Schéma MIMO" width="467" height="379" border="0" /></p>

<p>Používaný technický postup se označuje jako D-TxAA, tedy Double Transmit Antenna Array a jak už jsme si řekli, je aplikován jen nad sdíleným vysokorychlostním downlink kanálem HS-DSCH. Přenášeny jsou dva nezávyslé datové proudy (transportní bloky) ve stejném kanálovém kódu WCDMA, každý je ale zpracováván zcela samostatně a to v závislosti na podmínkách příjmu, které reportuje na uplinku uživatelská mobilka. Oba transportní bloky mohou mít rozdílné modulační i kódovací schéma odvyslé od rychlosti přenosu i podmínkách na rádiovém kanálu. K tomu slouží odezvová signalizace od mobilky zvaná Precoding control Information (PCI) a Channel quality Indicator (CQI). V závislosti na těchto dvou odezvách se plánovač základnové stanice rozhodne distribuovat k mobilce jeden či dva datové streamy, jakou použije velikost packetu (transportního bloku) a jaké modulační schéma použije projednotlivé streamy. Pokud není prostor (z důvodů potíží na rádiu) pro dva transportní streamy, provede se zpravidla přechod na klasické datové schéma R99. </p>

<p>Je zřejmé, že MIMO musí podporovat i mobilka a tak vznikly čtyři další kategorie schopností pro datové přenosy, které mají splňovat mobilky pro MIMO. Kategorie 15 a 16 podporuje MIMO s modulačními schématy QPSK a 16QAM, nemá žádnou podporu pro schéma 64QAM. Kategorie 17 a 18 sice podporují 64QAM, ale nikoliv zároveň s MIMO. Podpora MIMO s 64QAM přijde v R8.</p>

<p>Na uplinku se úpravy pro mimo týkají výhradně signalizace, tedy HS-DPSCH (Highs Speed Dedicated Physical Control Channel), kde jsou přenášeny odezvy PCI a CQI a reakční odezvy HARQ-ACK.</p>

## HOM – Modulace vyššího řádu

<p>Vyšších přenosových rychlostí dosahuje R7 také (a především) novým modulačním schématem vyššího řádu, v tomto případě 64QAM. To umožňuje přenést šest mitů na symbol, oproti čtyřem v 16QAM a dvěma v QPSK, čímž se více blíží teoretické kapacitě přenosového kanálu, (buďme pamětlivi pana Shannona).</p>

<p>Značnou výhodou HOM je tedy zvýšení přenosové rychlosti zejména v případě, ze není k dispozici MIMO. Je velmi efektivní v případě mikrocell při indoor pokrytí a v případě, kdy je přímá viditelnost mezi mobilem a základnovou stanicí, takže nevzniká zašumění vícecestným přenosem signálu. Pro 64QAM nejsou potřeba žádné úpravy na kontrolním kanálu uplinku (HS-DPCCH) a jen málo změn na kontrolním kanálu downlinku (HS-SCCH). Samozřejmě je potřeba, aby 64QAM podporoval mobilní terminál a když už jsme u toho, operátor musí zvážit posílení přenosové sítě mezi buňkami sítě.</p>

<p>Přehled kategorií mobilek dle downlinku podle modulace a využití MIMO je v následující tabulce:</p>

<p><img style="display: block; margin-left: auto; margin-right: auto;" src="/assets/kategorie-hspa-ue.png" alt="Kategorie zařízení v UMTS" width="378" height="600" border="0" /></p>

<p>Na uplinku je nyní možno používat 16QAM, takže přenosová rychlost na uplink kanálu HSPA+ je nově až 11,5 Mb/s. V další tabulce jsou kategorie zařízení podle uplinku. </p>

<p><img style="display: block; margin-left: auto; margin-right: auto;" src="/assets/hsdupa-kategorie.png" alt="Kategorie mobilek pro uplink" width="456" height="280" border="0" /></p>

## Continuous Packet Connectivity (CPC)

<p>Další funkcí pro zrychlení mobilních dat, které se nedostává toliko pozornosti, je Kontinuální paketové připojení CPC. Tato funkce se snaží reagovat na vzrůstající počet lidí v mobilní síti, kteří jsou vlastně trvale datově připojeni – například na ICQ, ale obecně na jakýchkoliv službách, která si občas sahají do netu. Potíž je, že to většinou doposud znamenalo sestavit případně rozpojit spojení a to obnášelo zátěž na síť, která byla zbytečná, neproduktivní. A to se projevuje například na kontrolních signalizačních kanálech, kdy zejména u uplinku dochází k vysokému zarušení mobilek, které povídají najednou. Prvním předpokladem CPC je tedy odstranit přetížení uplinkových kontrolních kanálů. Předpokladem druhým je dosáhnout téhož na downlinkových kanálech, jejichž soustavný monitoring mobilním terminálem obnáší vytloukání jeho baterek. Do podrobností se pouštět nebudeme. </p>

## Result

<p>Sečteno a podtrženo, HSPA+ v Release 7 přináší zdvojnásobení kapacity pro data i pro hlasové přenosy při stejném objemu využitého rádiového spektra. Je dosaženo rychlejší odezvy datové sítě a nižší spotřeba energie.</p>

<p><img style="display: block; margin-left: auto; margin-right: auto;" src="/assets/mimo-rychlosti.png" alt="Rychlosti v Release 7" width="500" height="287" border="0" /></p>

<p>V tomto grafu vidíte simulované porovnání teoretické datové kapacity sektoru na nosné o šířce 5 MHz mezi HSPA (Release 6) a HSPA+ (Release 7): </p>

<p><img style="display: block; margin-left: auto; margin-right: auto;" src="/assets/release7-rychlosti.png" alt="Porovnání datové kapacity sektoru v HSPA a HSPA+" width="500" height="378" border="0" /></p>

<p>Uživatel má také k dispozici až 28 Mb/s pro download a až 11,5 Mb/s pro upload dat – pokud samozřejmě podmínky sítě dovolí. Jelikož ale část funkcí je dovedena k užitnému stavu v Release 8, používá se pro HSPA+ v praxi spřažená Release 7/8 – například 64QAM pro MIMO definguje až R8 a bylo by smutné, nemít ji k dispozici. Na další drobnosti z R8, které jsem tu nepostihl, se podíváme někdy jindy.</p>