---
layout: post
title:  Co přijde po 5G?
categories: [5G, Mobilní sítě, LTE, 6G]
excerpt: Odpověď je vlastně teoreticky jednoduchá. 6G. Jenže, jak může síť šesté generace vypadat, k čemu by mohla být a jaká k ní bude cesta?
---


Odpověď je vlastně teoreticky jednoduchá: 6G. Jenže, jak může síť šesté generace vypadat, k čemu by mohla být a jaká k ní bude cesta?

Z pohledu standardizace je dnes síť 5G v první fázi vývoje, kterou definuje standard 3GPP Release 15. Ten máme, definuje funkce jako Slicing, použití bezlicenčního spektra, architekturu založenou na službách, IoT a V2x (komunikace mezi vozidly) a samozřejmě rychlostní záležitost.

### Release 16

Nově chystaná Release 16 plánovaná na polovinu roku 2020 tyhle klíčové oblasti rozvíjí a prohlubuje. Tak například pro automobily (čili V2x) bude podporovat plnou autonomii, realtime komunikaci pro více senzorů a také vzdálené řízení. Pro kamiony především platooning, jízdu v konvoji (nenapadá mě lepší překlad). V2x je zajímavá oblast, neméně zajímavé je, že ji v rámci standardizace tlačí hlavně LG a Huawei.

Další rozvoj se chystá pro IoT, kde Rel 15 je rovněž spíše výkop a podpora opravdu low-power a zároveň dálkových přenosů bude až v Rel 16. Tady má přispět nový URLLC Ultra Reliable and Low Latency Communication režim.

Tato druhá fáze 5G má přinést větší podporu také pro kritickou komunikaci, například v režimu PMR pro drážní systémy. GSM-R, docela běžně používané (i u nás) se totiž blíží konci životnosti a tento nový systém by jej měl/mohl nahradit.

### Release 17 a rok 2022

Release 17 je plánována na začátek roku 2022. Má přinést hlavně změny v rádiovém spektru – NR Light bude jednodušší přístupový režim k rádiu, který nebude tolik spotřebovávat energii a nebude vyžadovat tak silnou elektroniku. Je určený pro svět Wearable zařízení a jiných jednodušších zařízení, které už nesplňují parametry IoT senzorů, je vhodné mít je připojené a přitom plnohodnotná elektronika a spotřeba u nich není realizovatelná.

V rádiu ještě zmíním plány na použití spektra nad 52 GHz, zejména vizi použití bezlicenčního pásma 60 GHz. To přinese zajímavé nové možnosti a kapacity.

Zvláště bych se zastavil u konceptu  **NR NTN**  neboli nového rádia neterestrické sítě. Myšlenka je, nahradit připojení základnových stanic nebo dokonce samotných mobilních terminálů už ve standardu satelitním či balonovým/dronovým připojením. Tedy signálem šířeným ze satelitů, balonů, dronů či jiných létajících zařízení. Zajímavá myšlenka, uvidíme, jak se chytne. Požadavky na ni byly zejména s ohledem na projekty Facebooku a Elona Muska.

![Vlastnosti jednotlivých druhů Ne-pozemních sítí](/assets/nepozemni-site.png)

Vlastnosti jednotlivých druhů Ne-pozemních sítí

Standardně by mělo být podporováno více SIM a měla by se zvýšit přesnost lokalizace polohy v síti. Už kvůli V2X je vhodné dostat se na decimetrové přesnosti a to včetně přesnosti odečtu výšky.

Tyto funkce bude následně rozvíjet Release 18 – asi si všímáte, že lichá release je iniciální uvedení funkce, sudá pak její rozvoj do výrazně použitelnější podoby. A jelikož u funkcí jako NR NTN a V2X polohy půjde o delší technický boj, předpokládá se, že další rozvoj těchto funkcí bude probíhat až do Release 20. Do roku 2025 by sítě 5G měly tedy získat velmi komplexní pokrytí výše zmíněných funkcí.

### Release 21 aka 6G  

Release 21 je už dost daleko, ale to by mělo být oním prvním 6G standardem. O jeho obsahu se můžeme dohadovat podle toho, co jednotlivé firmy tlačí a jak jsou s tím daleko. Je pravděpodobné, že se začne propagovat rozšíření Nového Rádia (NR) do frekvencí nad 100 GHz (D-Band) a tím přesun na terabitové rychlosti s ultranízko latencí pod desetinu sekundy. Polohování v indoor síti by se mělo dostat na centimetrové přesnosti a přijde i podpora zařízení s nulovou klidovou spotřebou. Do roku 2030 se v případě úspěchu Starlinku a podobných masivních VSAT sítí bude potřeba vyrovnat i s jejich integrací do komunikační sítě.

Nějakou chvíli se hovořilo o integraci blockchainu, ale to byl spíše chvilkový hype. Bylo by sice zajímavé udělat nějakou sdílenou autorizaci přístupu k síti a umožnit uživatele plynule migrovat mezi sítěmi třeba na bázi aukčního principu „kdo mě právě spojí nejlevněji“, technicky to možné je, výzkumy v tomto stádiu pokračují, ale tahle pomýlená taktika nepochybně přes operátory neprojde.

### K čemu to všechno?

Příštích deset let má být věnováno zasíťování všeho možného i nemožného. Právě automobily jsou nejvhodnějším pilotním prvkem. Většinou už dnes nějakou potřebu komunikace mají, minimálně pro update objížděk v mapách. Nějak to už také řeší. Nejsou skoupé na prostor ani na napájení, takže můžete experimentovat a nebát se rozměrových i žravostních omezení. Proto V2x. U něj se ostatně někdy zastavíme.

Pak jsou zařízení různě limitovaná rozměry, schopností vystrčit anténu a vůbec form-faktorem a zejména spotřebou. Na ně přichází řada postupně ve formě IoT podpory a NR Light. A také v postupné integraci světelné komunikace (tu jsem úplně pominul). Jinak pro představu – v pásmu 100 GHz se dnes dá komunikovat rychlostmi v řádu cca 100 Gb/s na vzdálenost několika desítek centimetrů, rozhodně to není záležitost dalekého dostřelu, stejně jako světelná komunikace.

![Scénáře, které by chtělo 5G pokrýt](/assets/emb.png)

A do třetice ještě přijdou zařízení, o kterých netušíme ničeho. Třeba taková, která nebudou mít hmotnou podstatu, ta se skrývají pod názvy Wireless Device as a Service – tedy možnost pronajmout si fyzický hardware a ten používat nebo ještě lépe pronajmout si takovou službu jen virtuálně, na dálku, přes nejrůznější virtualizační nástroje, které přenesou výstup takového zařízení. Jak to bude ve skutečnosti fungoovat, nám ukáže budoucnost, stejně jako uvidíme, zda to bude prakticky k něčemu, tenkolientní aplikace jsou dodnes spíše úsměvné, než prakticky použitelné, ale má to být „jen o dostatku kapacity“.

Velkou část kapacity má zkonzumovat virtualizace reality, tedy například obohacování obrazu do brýlí nebo kompletní generování obrazu do nich. Aby šlo o obraz oku lahodící, chtělo by to gigabitové rychlosti a nové generace displejů. To druhé se chystá, nutno nezaspat v tom prvním.

Úplně stranou jsem ponechal různé „open“ iniciativy jako OpenRAN, definující otevřená rozhraní v různých částech sítě (OpenRAN logicky v rádiové přístupové části sítě) – ty jsou tu od toho, aby se daly jednoduše propojovat systémy jednotlivých dodavatelů a případně do toho všeho mohl vstoupit i nějaký opensource projekt, což se různou měrou děje.