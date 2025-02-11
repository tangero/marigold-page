---
layout: post
title:  Amazon Sidewalk a renesance nízkoenergetických bezdrátových sítí s velkým dosahem
categories: [Amazon, Bezdrátové sítě, Technologie]
excerpt: WiFi a Bluetooth zná ledaskdo, málokdo ale zná nízkoenergetické bezdrátové sítě typu LPWAN (low-power WAN). LPWAN jsou bezdrátové sítě, které s maličkým vysílacím výkonem (a tedy vysokou výdrží na baterii) jsou schopné vysílat na slušný, několikakilometrový dosah, byť nevysokou rychlostí. Řekl bych, že populární a známá je třeba LoRa nebo Sigfox, ale lhal bych, nejsou ani populární, ani známé a to je ten problém.
---


WiFi a Bluetooth zná ledaskdo, málokdo ale zná nízkoenergetické bezdrátové sítě typu LPWAN (low-power WAN). LPWAN jsou bezdrátové sítě, které s maličkým vysílacím výkonem (a tedy vysokou výdrží na baterii) jsou schopné vysílat na slušný, několikakilometrový dosah, byť nevysokou rychlostí. Řekl bych, že populární a známá je třeba LoRa nebo Sigfox, ale lhal bych, nejsou ani populární, ani známé a to je ten problém.

Ponechme stranou, zda LPWAN nebudou pro běžného člověka něčím neviditelným po věky věků, něčím tak samozřejmým, jako je třeba SS7 nebo SIP, bez kterých by se telekomunikace ve své době neobešly, ale jejichž detaily rozhodně ponechávaly většinu uživatelů chladnými. A vlastně si možná odpovíme tím, že se podíváme na poslední dění kolem Sidewalku.

### Amazon Sidewalk propojí senzory s internetem

Technologii  [Sidewalk](https://www.amazon.com/sidewalk)  zmínil Amazon vloni, ale mnoho detailů se nevědělo. Už se jich pár ví, především to, jaká bude její architektura. Základním prvkem je Brána – Gateway. Na tu se připojuje koncové zařízení po frekvenci 900 MHz nebo přes Bluetooth LE protokolem Sidewalku a ona se postará o doručení informace do internetu. Nuda. Podstatné je, že branou Sidewalku budou koncová zařízení, která Amazon nabízí, především „domovní zvonky“ Ring a chytré reproduktory Echo (některé modely). Jejich majitelé se mohou rozhodnout, že nebudou (opt-out) služby Sidewalku nabízet všem zájemcům. Amazon uklidňuje, že jsou zde rychlostní omezení (80Kb/s přenosová rychlost) i kvóty (500MB na uživatele a všechna jeho zařízení), takže sdílení internetového připojení uživatelem pro Sidewalk nebude omezující.

Co je na tom podstatné? Ta podpora. Doposud bylo pro rozšíření sítě nutná výstavba, která je pro LPWAN sice jednodušší, než u mobilních sítí (ponechme stranou zajímavý blockchain koncept  [sítě Helium](https://www.helium.com/)), ale pořád představovala investice a administrativu. Chytrých reproduktorů Echo prodal Amazon přes 100 milionů, většina z nich je se Sidewalkem kompatibilní. Jen pro představu, koncem roku 2019 bylo v amerických domácnostech 157 milionů chytrých reproduktorů všech firem. Vůbec nejde o marginální trh, jak by se ze zpožděného českého trhu mohlo zdá.

### Ring a aplikace Neighbors

Tvůrce chytrých zvonků  [Ring](https://en.wikipedia.org/wiki/Ring_(company))  koupil Bezos v roce 2018 za miliardu dolarů. Proč, to nebylo úplně zřejmé, navíc Ring si prošel bezpečnostními pochybeními, ze kterých se ale nějak vzpamatoval i prostřednictvím AWS infrastruktury. Jen v prosinci 2019 se  [prodalo v USA přes 300 tisíc Ringů](https://www.vox.com/recode/2020/1/21/21070402/amazon-ring-sales-jumpshot-data), celková čísla prodeje jsou v milionech, kolik přesně se neví, ale firemní aplikace Neighbors patří mezi nejrychleji rostoucí „sociální sítě“ v USA. Proč ty uvozovky? Aplikace neslouží jen ke správě kamer a zvonků Ring, ale především umí upozornit na bezpečností incidenty v okolí vaší domácnosti a to i když žádnou Ring techniku nemáte. Prostě sociálně-kriminální síť, žádná koťátka a vařeníčko sem přidat nemůžete.

![Ring Neighbors aplikace](/assets/Neighbors-App-1.jpg)

_Aplikace Ring Heighbors v představách společnosti…_

I za to samozřejmě schytává Ring a Amazon kritiku, protože mnohým se zdá, že prostřednictvím kamer na zvoncích může vstupovat (a kdo ví, zda to nedělá) do soukromí lidí více, než by bylo zdrávo. Už proto, že do projektu se zapojují policejní oddělení, která mohou získat záznamy z kamer Ring v místě bezpečnostního incidentu. A také si postupně policie zvyká informovat pomocí Neighbors o trestných činech v oblasti. Nebo třeba proto, že  [utekly dokumenty](https://www.extremetech.com/extreme/302780-leaked-ring-document-details-creepy-facial-recognition-neighborhood-watch-feature), podle nichž Ring chce průběžně fotit lidi jdoucí kolem jeho kamer a katalogizovat je, aby mohl poslat výstrahu, když se v okolí objeví někdo podezřelý.

### Pokrytí formou software upgrade …

Zpět k Sidewalku, ačkoliv Neighbors bude ještě důležitý trend. Amazon přes softwarový upgrade může velmi rychle vybudovat základní pokrytí své sítě Sidewalk, protože dosah je až 1,5 kilometru. To je samozřejmě méně, než Sigfox či Lora, ale s hustotou bran, jakou nabídne Ring a Echo to bude úplně dostatečné, navíc kapacitně velmi dobře dimenzované. Plus zadarmo – zaplaceno uživatelem.

Zatím nejsou známy podmínky Sidewalku pro třetí strany, jediným vnějším partnerem je výrobce lokalizačních zařízení Tile, pro něhož je spojenectví s Amazonem určitým vykoupením z téměř jisté smrti, jakou mu uchystal Apple s podobným produktem. Není tedy zřejmé, jaká bude obchodní stránka věci, nicméně o funkční nízkoenergetickou síť s rozumným dosahem (a tedy slušnou výdrží na baterku), oboustrannou výměnou informací a dobrým pokrytím zájem bude. Zvláště, když Amazon zatím uvádí, že přístup do sítě je zdarma, živit ji zřejmě bude z toho, že infrastrukturu si poskytovatelé rozchodí nad AWS.

-   [For developers](https://developer.amazon.com/en-US/blogs/alexa/device-makers/2020/09/amazon-sidewalk-paves-the-way-for-more-connected-communities)
-   [Amazon Sidewalk privacy and security whitepaper](https://m.media-amazon.com/images/G/01/sidewalk/privacy_security_whitepaper_final.pdf)

Lze namítnout, že kartami zamíchá NB-LTE, jenže to je historka, kterou slýcháme příliš dlouho. Zatím se neumíchalo mnoho, zatím jsou slibné koncepty a rozjeté zkušební sítě a to je tak všechno. Palety svého zboží tak počítá ve svém Industry 4.0 jen málokdo a to nejenom v Česku.

Amazon nevsází na Industry 4.0 a sám se ohrazuje proti tomu, aby jeho Sidewalk byl porovnáván třeba s [protokolem Thread](https://en.wikipedia.org/wiki/Thread_(network_protocol)), za kterým stojí Google. Thread nabízí vyšší rychlosti, ale vzdálenosti do typicky 300 metrů. Tyhle vzdálenostní problémy hodně splývají, dosah 300 metrů a 1,5 kilometrů je vlastně jen otázka výstavby sítě, jenže Thread je spíše mesh topologie, zatímco Sidewalk klasická hvězdice se všemi výhodami a nevýhodami řešení. Nakonec půjde o cenu za použití, rozšíření řešení a jednoduchost jeho implementace, jak technickou, tak právní. A v tom by Sidewalk s mírnými limity na přenosovou kapacitu a cenovým požadavkem „jet na AWS“ mohl být zajímavý.

![Matice bezdrátových technologií podle přenosové rychlosti a vzdálenosti. ](/assets/IoT-Wireless-Tech.jpg)

Matice bezdrátových technologií ukazuje, jaký je jejich poměr přenosové rychlosti, dosahu a nákladů na implementaci. Bezlicenční Sidewalk je na příjemném konci spektra v nákladech i dosahu.

V Česku ani Ring, ani Echo nemají příliš silnou pozici, jenže Česko o budoucnosti technoligí nerozhoduje ani náznakem. Rozhodne to, co se chytí v USA a co se povolí v Číně. Přičemž Číně zrovna moc nevoní bezlicencované rádiové přenosy na dlouhé vzdálenosti…