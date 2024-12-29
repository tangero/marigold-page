---
layout: post
title: "Vývoj síťové architektury 3GPP: Od GSM přes 3G a LTE k 5G Advanced"
date: 2024-12-16
categories: [5G, 5G-Advanced, Mobilní sítě]
---
__Co konkrétně se v tomto článku dozvíte?__ 
* Obsah
{:toc}

Pokud mají moderní mobilní sítě nabízet zrychlení, znamená to mimo jiné, že je potřeba zjednodušovat jejich architekturu, neboť vzájemná komunikace jednotlivých komponent generuje prodlevy, jež uživatelům nevyhovují. Zjednodušení architektury mobilní sítě je tedy hnacím motivem nových generací mobilních sítí. 

Pro ty, kdo se ve schématech sítí moc nepohybují: Funguje tu celá řada akronymů, zkratek, které se částečně překrývají. Například základnovým stanicím se říká v sítích GSM BTS, v sítích UMTS NodeB a v LTE sítích eNodeB. Důvod je prostý: odlišit, že jde o základnovou stanici pro konkrétní technologii, čímž je dána i její rozdílná funkčnost. Zatímco základnová stanice je obecně jakákoliv rádiová jednotka obstarávající komunikaci sítě s koncovým zařízením, NodeB je taková základnová stanice v síti UMTS/3G. 

Je také zřejmé, že pro komunikaci s BTS či NodeB se používají rozdílně značené protokoly zajišťující v případě NodeB zpětnou kompatibilitu, schopnost obsloužit uživatele starší technologie. Aby toto bylo v nákresech zřejmé, používají se i k popisu vlastně “stejné funkce” vykonávajících protokolů jiná označení. Do takového detailu ale nepůjdeme tam, kde to není pro pochopení fungování sítě nutné.  



Projekt 3GPP (3rd Generation Partnership Project) se zásadním způsobem podílel na utváření prostředí mobilních telekomunikací. Od svého založení v roce 1998 3GPP neustále vyvíjí své standardy, aby vyhověl stále rostoucím požadavkům na vyšší přenosové rychlosti, nižší latenci a vyšší kapacitu. Tento článek se zabývá technologickou proměnou síťové architektury 3GPP od verze 98 přes zavedení 3G, 4G (LTE) a 5G až po nejnovější 5G Advanced ve verzi 18\. Zaměříme se na architektonické změny, nové síťové prvky, protokoly a zdůvodnění těchto konstrukčních rozhodnutí.


## **Přehled standardizace 3GPP**

Než se ponoříme do konkrétních verzí, je nezbytné porozumět procesu standardizace 3GPP. 3GPP se řídí fázovým přístupem, přičemž každá fáze se označuje jako „vydání“. Každá verze navazuje na předchozí, zavádí nové funkce a vylepšení a zároveň zachovává zpětnou kompatibilitu, kdykoli je to možné. To zajišťuje uživatelům a operátorům hladký přechod při modernizaci jejich sítí a zařízení.

| Verze | Vydáno | Hlavní novinky |
| :---- | :---- | :---- |
| Fáze 1 | 1992 | Funkce GSM |
| Fáze 2 | 1995 | Funkce GSM, kodek EFR |
| Vydání 96 | 1\. čtvrtletí 1997 | Funkce GSM, uživatelská datová rychlost 14,4 kbit/s |
| Vydání 97 | 1\. čtvrtletí 1998 | Funkce GSM, GPRS |
| Vydání 98 | 1\. čtvrtletí 1999 | Funkce GSM, kodek AMR, EDGE, GPRS pro PCS1900 |
| Vydání 99 | 2000 Q1 | Specifikoval první sítě UMTS 3G, které obsahují rozhraní CDMA |
| Vydání 4 | 2\. čtvrtletí 2001... | HSDPA |
| ... | ... | ... |
| Vydání 19 | 4\. čtvrtletí 2025 | 5G-Advanced |

Sítě 2G a 3G měly velmi podobné schéma, v němž existovaly základnové stanice (nazývané BTS ve 2G nebo Node B u 3G) obsluhující jednotlivé oblasti zvané buňky a komunikující s mobilními uživateli. Odděleně od základnových stanic existovaly jim nadřízené řídící systémy zvané Radiové kontrolery (ve 2G se jmenovaly BSC, u 3G o RNC). Kontrolery (česky béescéčka nebo erencéčka) dohlížely na několik desítek nebo stovek základnových stanic, jejich provoz koordinovaly. Jejich hlavním úkolem byla rádiová koordinace, tedy přidělování a uvolňování rádiových kanálů, na které základnové stanice komunikují s uživatelem a řízení kmitočtové matice pro Frequency Hopping (technologii dynamické změny frekvence pro lepší využití frekvenčního spektra a zvýšení bezpečnosti). Dále BSC koordinovalo handovery a sdružovalo provoz z podřízené části sítě do ústředny mobilní sítě zvané MSC. Mimo jiné také až BSC provádělo šifrování a dešifrování přenosů. 

S příchodem paketového přenosu dat GPRS (sítě 2.5G) se do BSC přidala část zvaná PCU starající se o obsluhu paketových dat. S příchodem technologie EDGE (2.75G) se pak BSC rozrostlo ještě o TRU, tedy transceiver starající se o novou modulaci, jíž si povídal mobilní telefon se základnovou stanicí (8-PKS). Díky tomu se upgrade sítě 2G na EDGE provedl snadno a bezbolestně, protože zapotřebí byl jen upgrade na BSC, ačkoliv v Česku i tak některým operátorům tento upgrade trval. 

## **Vývoj nepozemských sítí v rámci 3GPP**

Dalším důležitým aspektem standardizace 3GPP je integrace nepozemních sítí (NTN). NTN, jako jsou satelitní sítě, hrají klíčovou roli při rozšiřování mobilního pokrytí do vzdálených a nedostatečně obsluhovaných oblastí. 3GPP aktivně pracuje na začlenění NTN do svých norem a věnuje tomuto úsilí různé studie a pracovní body. \
[Nepozemské sítě NTN podrobněji rozebíráme zde](/mobilnisite/non-terrestrial-networks-ntn-5G-nezemske-site/). 

| REL | Akronym | Titul |
| :---- | :---- | :---- |
| REL-15 | FS\_NR\_nonterr\_nw | Studie o NR na podporu neterestrických sítí |
| REL-16 | FS\_NR\_NTN\_solutions | Studie o řešeních pro NR na podporu neterestrických sítí (NTN) |
| REL-17 | NR\_NTN\_solutions | Řešení pro NR na podporu neterestrických sítí (NTN) |
| ... | ... | ... |

Tyto snahy zdůrazňují význam NTN v budoucnosti mobilních sítí a závazek 3GPP poskytovat všudypřítomné připojení.

## **3GPP Release 99: Úsvit 3G**

Release 99 znamenala významný milník v podobě zavedení sítí 3G, které jako technologii rádiového přístupu zahrnují širokopásmový vícenásobný přístup s kódovým dělením (WCDMA). Tento přechod z 2G na 3G si vyžádal změny v architektuře sítě, aby se přizpůsobila novým požadavkům služeb 3G.

V sítích třetí generace se některé funkce přesunuly z kontrolérů (nově zvaných RNC) do základnových stanic NodeB. Část změn je dána tím, že v 3G se nepoužívá řízení přístupu po frekvencích a čase, ale podle kódů, takže všechny základnové stanice mohou vesele používat všechny frekvence. Tím si NodeB přebírají frekvenční řízení kompletně od RNC, hospodaří si s přidělenými frekvencemi a také provádějí mezifrekvenční handovery, což zvýšilo spolehlivost a snížilo prodlevu při handoverech. RNC provádí i staré činnosti, jakými je třeba vyhodnocování kvality signálu a příkazy k handoverům či se podílí na de/šifrování dat ze sítě. 

Na kontroleru RNC jsou také nové úlohy jako přidělování kódů používaných v kódovém sdílení přistupu do sítě (CDMA/WCDMA), což souvisí se změnou modulace z TDMA na CDMA. 

Tak vypadal záměr v nejstarším návrhu sítí UMTS, tedy evropského standardu 3G, dnes nejvíce používaného standardu. Tento standard se nazýval Release 99 podle roku 1999 kdy byl projednán, rovněž se kvůli kompatibilitě s dalším značením používá značení Release 3. Již další release ale záváděly další změny, většinou pravda v samotném jádře sítě.     

Ale již ve významné Release 5 (marketingově 3.5G) kvůli nové technologii rychlejšího stahování dat HSDPA došlo i na změny ve vztahu RNC a NodeB. NodeB přebírá kvůli zrychlení část funkcí od RNC, jde především o rozhodnutí znovu poslat chybně přenesená data nebo o přidělení jiného sdíleného kanálu. Pokud mobilní telefon přijal data, která byla vadná, nově mu data posílala NodeB, protože je zpravidla měla uložena ve vyrovnávací paměti, nemusela se posílat znovu přes RNC ze sítě. Podobně tomu bylo vůči technologii rychlého odesílání dat HSUPA z téže Release. 

V Release 6 došlo k sjednocení HSDPA a HSUPA do HSPA a ne, nešlo jen o přejmenování, ale podporu vzájemné koordinace obojího. Marketingově se tím dostáváme k pojmenování 3.75G. Pro nás významným mezníkem byla Release 7, která pro vylepšenou verzi HSPA+ odstranila z rádiové části sítě kontroler RNC - respektive jeho funkce přesunula do základnové stanice NodeB. Šlo o první experiment předcházející vzniku LTE. 

Architektuře UMTS sítí se [věnujeme podrobněji v tomto článku](/item/blaznuv-turbouvod-do-umts-jak-vypada-sit/).

### **Vývoj Jádra sítě (Core Network)**

Verze 99 zavedla pozemní rádiovou přístupovou síť UMTS (UTRAN). UTRAN, nový typ přístupové sítě, byla navržena tak, aby podporovala vyšší přenosové rychlosti a nové nosné služby nabízené systémem WCDMA 3. Aby se minimalizoval dopad na jádro sítě, zaměřilo se 3GPP na přizpůsobení stávající infrastruktury jádra sítě GSM/GPRS4. To zahrnovalo vytvoření nového rozhraní mezi jádrem sítě a přístupovou sítí a modernizaci signalizace jádra sítě tak, aby využívala možností sítě UTRAN.

Je důležité poznamenat, že v této době existovaly dvě architektury páteřní sítě definované ETSI a 3GPP: Release 99 a Release 4/5. Release 99, založená na platformě GPRS (General Packet Radio Service), umožnila operátorům využít jejich stávající investice do GPRS5. Naproti tomu verze 4/5 byla plně IP verzí páteřní sítě UMTS.

V případě sítě 3G tak fakticky došlo oproti předchozí generaci ke zvýšení složitosti sítě tím, že síť byla rozdělena na paketovou a okruhově spínanou doménu, respektive toto rozdělení bylo uplatněno ve stejném čase i na sítě GSM. Postupem doby se standard UMTS pokoušel toto rozdělení překlenout sjednocením [pod systémem IMS](/item/turbouvod-do-umts-ims-aneb-ip-multimedia-subsystem/), nakonec se ale provoz okruhově spínaných technologií jevil natolik neperspektivní a vývoj přenosu hlasu po IP vrstvě natolik pokročil, že bylo možné v sítích 4G napříště uvažovat pouze o paketovém přenosu a všechny služby přenášet v něm. Tím řada sítí 3G okruhové spínání vůbec neimplementovala, resp operátor implementoval rovnou LTE, které se v té době označovalo jako 3.99G, aby se naznačilo, že ještě nejde o plnohodnotné 4G tak, jak jej předpokládala ITU. 

### **Technologie a protokoly rádiového přístupu**

Přechod na 3G přinesl také změny v architektuře protokolů rádiového rozhraní. Verze 99 zavedla nové transportní kanály a fyzické kanály pro podporu [rádiového rozhraní WCDMA](/item/turbouvod-do-umts-kapacita-cdma-a-par-shannonovych-kouzel). To zahrnovalo přidání vyhrazených transportních kanálů pro data s přepojováním okruhů i pro data s přepojováním paketů, což umožnilo současné připojení s různými požadavky na kvalitu.

### **Další vývoj UMTS**

Po vydání verze 99 pokračoval vývoj UMTS v dalších verzích. Verze 5 a 6 zavedly vysokorychlostní paketový přístup (HSPA), který výrazně zvýšil rychlost přenosu dat. Verze 7 dále vylepšila HSPA zavedením technologie HSPA+ (Evolved HSPA)6. Tyto pokroky v technologii 3G připravily půdu pro vývoj 4G LTE.

## **Verze 3GPP Release 8: Vzestup LTE**

Verze [3GPP Release 8](/item/3gpp-release-8-system-architecture-evolution-sae-a-evolved-packet-core-epc-v-ramci-lte-siti) zahájila éru 4G zavedením technologie Long Term Evolution (LTE). Cílem LTE bylo výrazně zvýšit kapacitu a rychlost sítě využitím nových technik digitálního zpracování signálu a modulací. Toto vydání přineslo zásadní změnu v architektuře sítě, která se posunula směrem ke zjednodušenému, plně IP systému se sníženou latencí.

Asi nejmarkantnější jsou tedy následující odlišnosti mezi 3G a 4G

- došlo k odstranění kontrolerů RNC/BSC - respektive jejich činnost byla přesunuda do eNodeB
- všechny eNodeB mezi sebou mohou komunikovat pomocí standardního rozhraní X2, což je mimo jiné důsledek odstranění RNC, ale také možnost používat v síti základnové stanice různých výrobců. Dříve bylo potřeba je důsledně geograficky oddělovat, protože uměly komunikovat jen přes RNC stejného výrobce. 
- byly odstraněny všechny okruhově spínané služby, veškerý provoz je pouze packetový
- všechny kanály se mohou využívat pro přenos dat, nejsou vyhrazeny řídící kanály. 
- díky tomu bylo zpřehledněno dosavadní Jádro sítě do podoby Evolved Packet Core (EPC), které může používat komerčně dostupné servery, ne specializovaný hardware. 

### **Zploštění síťové architektury**

Klíčovou architektonickou změnou verze 8 bylo zploštění struktury sítě. Předchozí architektura s více síťovými prvky (NodeB, RNC, SGSN, GGSN) byla nahrazena jednodušší architekturou se dvěma prvky8. Tato nová architektura se skládala z rozšířené základnové (uzlové) stanice (eNodeB) v rádiové síti a přístupové brány (a-GW) v páteřní síti8. Brána a-GW se dále skládala z jednotky pro správu mobility (Mobility Management Entity \- MME) pro funkce řídicí roviny a z brány pro evoluci systémové architektury (System Architecture Evolution Gateway \- SAE-GW) pro funkce uživatelské roviny8 . Tato plošší architektura vedla ke snížení latence a zlepšení výkonu koncových uživatelů8 .

Kromě toho byly uzly Rel-6 (GGSN, SGSN a RNC) v LTE sloučeny do jediného uzlu nazvaného Access Core Gateway (ACGW)9 . Toto zjednodušení síťové architektury přispělo ke zvýšení efektivity a výkonnosti sítí LTE.

### **Technologie rádiového přístupu**

Verze 8 také zavedla ortogonální vícenásobný přístup s kmitočtovým dělením (OFDMA) v sestupném směru a vícenásobný přístup s jednou nosnou (SC-FDMA) ve vzestupném směru - [detaily  máme zde](/item/modulacni-technologie-pro-uplink-siti-4g-lte-a-wimax). Tyto nové technologie rádiového přístupu spolu s anténními schématy MIMO (Multiple-Input Multiple-Output) umožnily vyšší přenosové rychlosti a spektrální účinnost.

### **Alternativní přístupy**

Ačkoli pro LTE byly zvoleny [OFDMA a SC-FDMA](/item/modulacni-technologie-pro-uplink-siti-4g-lte-a-wimax), zvažovala se i jiná schémata vícenásobného přístupu. Hodnotila se například vícenásobný přístup s časovým dělením (TDMA) a vícenásobný přístup s kódovým dělením (CDMA). Nakonec však byly vybrány OFDMA a SC-FDMA kvůli jejich lepšímu výkonu z hlediska spektrální účinnosti a odolnosti vůči rušení.

## **3GPP verze 10: LTE-Advanced**

[Release 10](/mobilnisite/3gpp-release-10) dále vylepšilo standard LTE zavedením LTE-Advanced. Cílem tohoto vydání bylo splnit požadavky na mezinárodní mobilní telekomunikace-Advanced (IMT-Advanced), které stanovily vyšší rychlost přenosu dat a vyšší spektrální účinnost10. Koncem roku 2009 byla oficiálně předložena ITU-T jako kandidátská technologie 4G.

### **Agregace nosných sítí**

Jedním z klíčových prvků verze 10 byla agregace nosných sítí. Tato technologie umožňovala agregaci více komponentních nosných, aby se vytvořila větší celková šířka přenosového pásma, což umožňovalo vyšší přenosové rychlosti12. Technologie LTE-Advanced podporovala šířku pásma až 100 MHz kombinací až pěti 20MHz komponentních nosných.

### **Rozšířený vícenásobný přístup v horní části sítě**

Verze 10 také zavedla vylepšený vícenásobný přístup na vzestupném kanálu se sdruženým SC-FDMA10. Tím se zlepšila spektrální účinnost a rychlost přenosu dat ve směru nahoru (při odesílání). Kromě toho tato verze zahrnovala podporu heterogenních sítí, které kombinují makrobuňky s malými buňkami pro zlepšení pokrytí a kapacity.

### **Nové funkce**

Verze 10 zavedla několik nových funkcí pro zvýšení výkonu LTE:

* **Carrier Aggregation:** Jak již bylo zmíněno, agregace nosných sítí umožnila dosáhnout větší šířky pásma a vyšší rychlosti přenosu dat.  
* **Vylepšené techniky s více anténami (MIMO):** To zahrnovalo podporu až osmi antén pro downlink a čtyř antén pro uplink, což umožnilo pokročilé techniky MIMO, jako je formování paprsku a prostorový multiplex.  
* **Podpora reléových uzlů:** Byla zavedena podpora pro reléové uzly, aby bylo možné nákladově efektivním způsobem rozšířit pokrytí LTE.

### **Alternativní přístupy**

Ačkoli byla jako primární metoda pro zvýšení šířky pásma zvolena agregace nosné, byly zvažovány i další přístupy. Hodnotilo se například využití širších souvislých bloků spektra. Agregace nosných byla však upřednostněna díky své flexibilitě při využívání fragmentovaného spektra a schopnosti podporovat jak sousední, tak nesousední nosné.

## **3GPP Release 13: LTE-Advanced Pro**

Verze 13, známá také jako LTE-Advanced Pro, se zaměřila na další zdokonalení LTE s cílem uspokojit rostoucí poptávku po vyšších rychlostech přenosu dat a lepším výkonu. V tomto vydání byla také dokončena první sada specifikací pokrývající kritické služby, zejména pro aplikace záchranných systémů a veřejné bezpečnosti.

### **Klíčové funkce a vylepšení**

Verze 13 představila několik klíčových funkcí, včetně:

* **Vylepšení agregace nosných sítí:** Verze 13 rozšířila rámec agregace nosných sítí tak, aby podporoval až 32 komponentních nosných sítí, což výrazně zvýšilo dosažitelné rychlosti přenosu dat10 . Toto vylepšení řeší potřebu operátorů agregovat více operátorů, aby uspokojili rostoucí poptávku po datech.  
* **LTE v nelicencovaném spektru:** Tato verze umožnila využití nelicencovaného spektra ke zvýšení rychlosti přenosu dat agregací primární buňky pracující v licencovaném spektru se sekundární buňkou pracující v nelicencovaném spektru16. Tento přístup umožnil operátorům využívat nelicencované spektrum a zároveň zajistit spravedlivou koexistenci s jinými technologiemi, jako je Wi-Fi.  [Detaily máme zde](/item/lte-unlicenced-o-co-jde-v-pripade-lte-v-nelicencovanem-pasmu/). 
* **Vylepšení pro komunikaci strojového typu (MTC):** Verze 13 zavedla novou kategorii UE s nízkou složitostí, která podporuje sníženou šířku pásma a spotřebu energie pro aplikace internetu věcí 10. Tím se řešila potřeba nákladově a energeticky efektivních řešení pro připojení velkého počtu zařízení internetu věcí.  
* **In-door určování polohy:** Tato verze se zaměřila na zlepšení přesnosti určování polohy v objektech (in-door) vylepšením stávajících metod a zkoumáním nových technik určování polohy10 . Důvodem byla rostoucí poptávka po službách a aplikacích založených na určování polohy ve vnitřních prostorách.

### **Dopad na výkonnost sítě**

Verze 13 významně ovlivnila výkonnost sítě tím, že:

* **Snížení nákladů na zařízení:** Toho bylo dosaženo snížením špičkové rychlosti, požadavků na paměť a složitosti zařízení.  
* **Zlepšení výdrže baterie:** Byly zavedeny funkce PSM a eDRX, které umožňují delší výdrž baterie u zařízení, která přenášejí malé objemy dat jen zřídka.  
* **Zlepšení pokrytí:** Pokrytí bylo zlepšeno o 15 dB pro Cat-M a o 20 dB pro NB-IoT a GSM, což umožnilo širší venkovní pokrytí a lepší prostupnost signálu uvnitř budov.

### **Alternativní přístupy**

Přestože bylo zvoleno rozšíření agregace nosných na 32 CC, byly zvažovány i další alternativy. Hodnotilo se například zvýšení modulačního řádu nebo použití širších komponentních nosných. Rozšíření agregace nosných však bylo upřednostněno kvůli své škálovatelnosti a flexibilitě při využívání fragmentovaného spektra.

## **3GPP Release 15: Revoluce 5G**

Verze 15 znamenala významný skok vpřed zavedením 5G New Radio (NR), nové technologie rádiového přístupu navržené tak, aby splňovala rozmanité požadavky služeb 5G. Technologie 5G NR přinesla zásadní změnu v architektuře sítě a umožnila vyšší přenosové rychlosti, nižší latenci a vyšší kapacitu.

### **Jádro sítě 5G**

Jednou z klíčových architektonických změn ve verzi 15 bylo zavedení sítě [5G Core (5GC)](/item/5G_Core/). 5GC je cloudová architektura založená na službách, která ve srovnání s předchozí jádrovou sítí EPC poskytuje větší flexibilitu a škálovatelnost. 5GC podporuje network slicing, který umožňuje operátorům vytvářet na sdílené fyzické infrastruktuře více virtuálních sítí pro uspokojení různých požadavků na služby.

Tento přechod na 5GC představuje přechod od hardwarově orientované k softwarově orientované síťové architektuře. Tento softwarově orientovaný přístup umožňuje větší flexibilitu, škálovatelnost a automatizaci, které jsou klíčové pro podporu různorodých požadavků služeb 5G.

### **Frekvenční rozsahy**

Verze 15 také zavedla dva frekvenční rozsahy pro 5G NR: frekvenční rozsah 1 (FR1) od 450 MHz do 7,125 GHz a frekvenční rozsah 2 (FR2) od 24,25 GHz do 52,6 GHz19. To umožnilo provozovat 5G NR v nižších i vyšších frekvenčních pásmech a zajistit rovnováhu mezi pokrytím a kapacitou. [Podrobněji popisuji zde](/item/5G_NR_New_Radio/). 

### **Klíčové zásady návrhu**

Při návrhu 5G NR byly zohledněny tři klíčové zásady:

* **Provoz na vyšších frekvencích a flexibilita spektra:** Díky tomu může 5G NR pracovat v širším rozsahu frekvencí, včetně pásem mmWave, a podporovat tak vyšší rychlosti přenosu dat a kapacitu.  
* **Velmi štíhlá konstrukce:** To minimalizuje neustále zapnutý přenos, zlepšuje energetickou účinnost a umožňuje vyšší přenosové rychlosti22.  
* **Dopředná kompatibilita:** To zajišťuje, že se 5G NR může vyvíjet a přizpůsobovat budoucím požadavkům a technologiím.

### **Vylepšení zabezpečení**

Verze 15 zavedla několik bezpečnostních funkcí pro zvýšení bezpečnosti sítí 5G:

* **Vzájemné ověřování mezi zařízeními a sítí:** To zabraňuje falešným základnovým stanicím vydávat se za skutečné.  
* **Skrytí trvalého identifikátoru:** Chrání soukromí uživatelů tím, že skrývá trvalý identifikátor účastníka (SUPI) přes vzdušné rozhraní.  
* **SEcurity Protection Proxy (SEPP) pro roamingovou architekturu:** To zvyšuje bezpečnost v roamingových scénářích ochranou proti útokům skrze propojení přes internet.

### **Architektura Cloud-RAN**

Ve verzi 15 byla také zavedena [architektura Cloud-RAN (C-RAN)](/item/c-ran_vran_open_ran/). C-RAN centralizuje zpracování jednotek základního pásma (BBU) v cloudovém datovém centru, což umožňuje:

* **sdružování a sdílení zdrojů:** BBU lze sdílet a v případě potřeby vypnout, což snižuje náklady a zvyšuje efektivitu.  
* **Kooperativní rádiové techniky:** C-RAN umožňuje [koordinovaný vícebodový přenos (CoMP)](/item/koordinovane-vicebodove-spojeni-v-lte/), který snižuje rušení a zvyšuje výkon.

Síť C-RAN však přináší také výzvy, jako je potřeba vysokorychlostních, nízkozpožděných a přesně synchronizovaných sítí fronthaul pro připojení BBU a vzdálených rádiových hlavic (RRH).

### **Alternativní přístupy**

Přestože byla pro 5G zvolena architektura 5GC, byly zvažovány i jiné architektury páteřní sítě. Hodnotila se například evoluce stávajícího jádra sítě EPC. Nicméně 5GC byla upřednostněna díky svému cloudově nativnímu designu, architektuře založené na službách a podpoře network slicing, které poskytují větší flexibilitu a škálovatelnost pro služby 5G.

## **3GPP Release 18: 5G Advanced**

Verze [Release 18](/item/5G_advanced_3GPP_Release-18/), první verze 5G Advanced, staví na základech položených verzí 15 a zavádí další vylepšení systému 5G . Tato verze se zaměřuje na zlepšení efektivity sítě, latence, propustnosti a pokrytí, přičemž zvláštní důraz klade na případy použití v podnicích.

### **Klíčové cíle**

Cílem 5G Advanced je:

* **umožnit efektivnější zařízení a služby internetu věcí:** To zahrnuje podporu zařízení s rozšířenou sníženou kapacitou (RedCap) a přenos malých dat.  
* **Rozšířit 5G prakticky na všechna zařízení a případy použití:** To zahrnuje vylepšení stávajících technologií a zavedení nových technologií pro podporu širšího spektra aplikací a zařízení.

### **Klíčové funkce a vylepšení**

Mezi klíčové funkce verze 18 patří např:

* **Vylepšený RedCap**: Tato verze vylepšuje zařízení se sníženou kapacitou (RedCap), která jsou navržena s ohledem na nižší složitost a náklady, takže jsou vhodná pro nasazení v oblasti internetu věcí.  
* **Umělá inteligence (AI) a strojové učení (ML):** Vydání 18 zavádí techniky AI/ML na různých úrovních sítě s cílem zlepšit výkon a efektivitu sítě.  
* **Klíčové poznatky: V roce 2018 se v rámci projektu „Klíčové poznatky“ objevilo několik nových technologií, které se zaměřují na podporu a rozvoj sítí:** AI/ML hraje klíčovou roli při optimalizaci výkonu a efektivity sítě v 5G Advanced. Využitím AI/ML se sítě mohou přizpůsobovat měnícím se vzorcům provozu, optimalizovat přidělování zdrojů a zlepšovat uživatelskou zkušenost.  
* **Vylepšení rozdělení sítě:** Tato verze rozšiřuje možnosti slicingu sítě o podporu slicingu s více doménami a více poskytovateli, což poskytuje větší flexibilitu a škálovatelnost.  
* **Klíčové poznatky:** Síťový slicing je v 5G a 5G Advanced stále důležitější. Umožňuje operátorům vytvářet přizpůsobené síťové řezy se specifickými výkonnostními charakteristikami, které splňují různorodé požadavky různých služeb a aplikací.  
* **Nezemské sítě (NTN):** Verze 18 zavádí podporu NTN, jako je satelitní komunikace, pro rozšíření pokrytí 5G do vzdálených a nedostatečně obsluhovaných oblastí.  
* **Klíčový poznatek**: Integrace NTN do 5G Advanced představuje výzvy i příležitosti. Může sice zajistit všudypřítomné pokrytí, ale zároveň vyžaduje řešení problémů, jako je latence, šíření signálu a nákladově efektivní nasazení.

### **Časový plán vydání**

Finalizace verze 18 byla prodloužena o tři měsíce, aby pracovní skupina 2 pro architekturu systému a služby (SA2) mohla dokončit některé definice funkcí. Konečná specifikace fáze 2 byla dokončena v červnu 2023, přičemž návrh protokolu byl dokončen do března 2024\.

### **Úspory energie v síti**

Verze 18 klade velký důraz na úspory energie v síti. Důvodem jsou rostoucí náklady na energii, které se staly významnou součástí provozních nákladů sítě (OPEX), a potřeba dosáhnout cílů udržitelnosti.

### **Alternativní přístupy**

Ačkoli bylo vylepšení RedCapu zvoleným přístupem pro podporu zařízení IoT s nízkou složitostí, byly zvažovány i další alternativy. Hodnotilo se například zavedení nové technologie rádiového přístupu speciálně pro IoT. Vylepšení RedCapu však bylo upřednostněno kvůli jeho zpětné kompatibilitě se stávajícími nasazeními 5G NR a schopnosti využít stávající ekosystém 5G.

## **Důsledky pro budoucnost mobilních sítí a 6G**

Vývoj síťové architektury 3GPP má významné důsledky pro budoucnost mobilních sítí a vývoj 6G a dalších technologií. V budoucích generacích mobilních sítí bude pravděpodobně pokračovat trend směrem k softwarově orientovaným architekturám, network slicing a optimalizaci řízené AI/ML.

### **6G a dále**

Zatímco 5G Advanced se stále vyvíjí, výzkumné a vývojové úsilí pro 6G již probíhá. Předpokládá se, že 6G bude poskytovat ještě vyšší přenosové rychlosti, nižší latenci a větší kapacitu než 5G, a to díky potenciálním technologiím, jako jsou např:

* **Terahertzová (THz) komunikace:** To by mohlo umožnit extrémně vysoké rychlosti přenosu dat a nízkou latenci. O [nových frekvencích detailněji zde](/item/nova-frekvenci-pasma-5g-6g/).  
* **Inteligentní komunikační prostředí:** Jedná se o využití umělé inteligence a pokročilého zpracování signálu k optimalizaci bezdrátového prostředí.  
* **Bezbuněčná architektura:** To by mohlo zajistit rovnoměrnější pokrytí a kapacitu3.

Tyto pokroky budou pravděpodobně vyžadovat další vývoj síťové architektury, aby podporovala nové schopnosti a požadavky 6G.

## **Shrnutí toho, co jsme se dozvěděli**

Vývoj síťové architektury 3GPP od verze 98 po verzi 18 byl veden potřebou podporovat stále se zvyšující rychlost přenosu dat, nižší latenci a větší kapacitu. Tento vývoj zahrnoval významné změny v páteřní síti, technologiích rádiového přístupu a celkové architektuře sítě.

Mezi hlavní architektonické změny patří:

* **Zploštění síťové architektury:** To bylo zavedeno ve verzi 8 s LTE s cílem snížit latenci a zvýšit efektivitu.  
* **Přechod na softwarově orientovanou páteřní síť:** Tento krok byl zaveden ve verzi 15 s 5G s cílem umožnit větší flexibilitu, škálovatelnost a automatizaci.  
* **Zavedení rozdělení sítě na části:** To umožňuje operátorům vytvářet virtuální sítě na míru pro podporu různých požadavků na služby.

Mezi nové technologie a protokoly, které ovlivnily vývoj, patří např:

* **WCDMA**: Zavedeno ve verzi 99 pro 3G.  
* **OFDMA a SC-FDMA**: zavedeny ve verzi 8 pro 4G LTE.  
* **Agregace nosných sítí:** Zavedena ve verzi 10 pro LTE-Advanced.  
* **5G NR:** zavedena ve verzi 15 pro 5G.  
* **Techniky AI/ML:** Zavedeny ve verzi 18 pro 5G Advanced.

Mezi hnací faktory tohoto vývoje patří:

* **Rostoucí poptávka po datech:** Ta je stálým motorem vývoje mobilních sítí.  
* **Potřeba nižší latence:** To je zásadní pro aplikace, jako jsou online hry a rozšířená realita.  
* **Poptávka po větší kapacitě:** To je nezbytné pro podporu rostoucího počtu připojených zařízení.  
* **Zaměření na energetickou účinnost:** Je to dáno rostoucími náklady na energii a cíli udržitelnosti.

S dalším vývojem pokročilé sítě 5G a nástupem sítě 6G můžeme očekávat další pokroky v síťové architektuře. Tak si o nich dáme včas vědět. Pro celou historii vývoje mobilních sítí si projděte [rubriku Mobilní sítě](/mobilnisite). 

