---
audio_url: null
author: Patrick Zandl
categories:
- Energie
- Energetika
- Green Deal
layout: post
post_excerpt: "Vyšla Zpráva výboru pro analýzu okolností elektroenergetické krize 28.4.2025 ve Španělsku, takže už zhruba víme, co stálo za španělským blackoutem. A bylo toho opravdu hodně."
thumbnail: https://www.marigold.cz/assets/spanelsko-blackout.png
title: "Co bylo příčinou blackoutu ve Španělsku?"
---


Včera vyšla španělská [Zpráva výboru pro analýzu okolností elektroenergetické krize 28.4.2025](https://www.miteco.gob.es/es/prensa/ultimas-noticias/2025/junio/se-presenta-el-informe-del-comite-de-analisis-de-la-crisis-elect.html). Mám k dispozici její [veřejnou verzi](/assets/ebook/Informe-no-confidencial-Comite-de-analisis-28Acs.pdf), která oproti důvěrné verzi vynechává jména konkrétních firem, s nimiž je nyní vedeno správní řízení. Můžeme si společně udělat přesnou představu, k čemu na Pyrenejském poloostrově onoho osudného dne došlo.

Zpráva zdůrazňuje, že došlo k rozsáhlé souhře okolností. Než si řekneme, že té souhře okolností v Češtině říkáme šlendrián, podívejme se na technické pojmy.

Prvním faktorem vedoucím přímočaře k blackoutu byla hlášená technická **nedostupnost zařízení s instalovaným výkonem 12,8 GW** a to včetně 3 GW jaderných bloků a 7,4 GW kombinovaného cyklu, což výrazně omezovalo regulační možnosti v síti. Pro některé části Španělska (především jihozápad) byla situace výrazně znepokojující, protože v oblasti byl nedostatek regulačních zdrojů. Jeden z tepelných bloků byl odstaven večer před incidentem a tepelné bloky v určitých oblastech nebyly prostě schopné absorbovat dostatečné množství jalové energie.



Již během dopoledne došlo na poloostrovní soustavě k netypickému kolísání napětí ve všech uzlech 400 kV vedení, ale odchylky byly relativně malé a již mezi 6 a 8 hodinou se síť chová dle očekávání. Kolem 9:00 byla zjištěna odchylka frekvence v důsledku změn v jiných částech evropské sítě a pak až do 12:00 je frekvence v mezích očekávání. Od 9 hodin ale přetrvává variabilita napětí, přičemž v 10:30 začínají výkyvy být s větší amplitudou, než je obvyklé. Stále jde ale o oscilace, které jsou systémem tlumeny bez významných opatření. Těmi _"nevýznamnými opatřeními"_ je postupné propojování trojice 400 kV přenosových tras, čímž dochází k zahušťování přenosové sítě. Díky tomu se zmenšuje sériová impedance mezi rozvodnami a lépe se tak tlumí frekvenční kmity, což byl ostatně účel propojování těchto tras. Současně to ale v síti zvyšuje paralelní kapacitní účinek.

A tím se dostáváme k druhému podstatnému faktoru: 28.4.2025 byl nezvykle nízký odběr (byť v normě pro tento typ dne), na cca 85 % obvyklé hodnoty. Kvůli zahuštění sítě a tím navýšení kapacitního účinku vzniká přebytek kapacitního jalového výkonu, který kolem 11:00 zdvihá napětí na uzlech 400 kV přenosové sítě. Tím také dochází k oscilace napětí v rozvodnách v Extremaduře (Almaraz a Arroyo de San Serván), což je situace sama o sobě nemilá, ale nikoliv krizová. Ještě za ni ale Španělsko zaplatí. 

## Časová osa

Těsně po poledni se objevuje **první výrazná atypická systémová oscilace v 12:03** a to 0,6 Hz - a trvá téměř 5 minut. Operátor sítě žádá francouzského provozovatele o snížení výměny s Francií, což se ve 12:07 stane. Ve 12:06 také operátor trasy do Francie nechává přenout z HDVC do režimu DC, čímž ve 12:11 zablokoval tok činného výkonu a linka se chová jako elektrický tlumič a klesá tok kapacitní jalové složky a tím i napětí. Okamžitým opatřením je **odpojování čtyř kompenzačních tlumivek** na rozvodnách Villaviciosa, Guadame, Rueda a Aragón, čímž se snaží udržet klesající napětí nad 390 kV. Operátor také zvyšuje zahuštění sítě propojováním dalších pěti 400 kV tras, které byly momentálně odpojené. Tento postup opět zvyšuje mechanické tlumení, ale přidává kapacitní jalový výkon.

**Druhá velká oscilace s frekvencí 0,2 Hz přichází v 12:19** a potrvá 3:20 minut. Přichází Operátor znovu snižuje výměnu s Francií, čímž ještě více snižuje možnost odlehčit si jalový výkon do francouzské sítě. Odpojuje další tlumivky, po vyrovnání oscilací ale ve 12:22 postupně pět tlumivek připojuje. Jenže to už je zaděláno na kaskádový malér, protože kombinace nově připojených paralelních vedení, odpojených tlumivek a nižších exportů zvyšuje napětí v síti v době, kdy klesá tlumení kmitů.

Operátor REE se rozhoduje požádat o připřažení horkého zdroje a v 12:26 zajišťuje připřažení zdroje v jižní zóně, ale nemůže sehnat nic s rychlejším náběhem, než v 14:00, kdy hodinu a půl má trvat náběh zdroje. K tomu již nedojde. Provozovatel jiného zdroje upozorňuje operátora na možná výpadek svého zdroje, probíhá hledání další náhrady.

V čase 12:05 - 12:20 tedy dochází k silným výkyvům napětí zejména ve střední a jižní části sítě. Po skončení druhé oscilace ve 12:22 je stále pozorován nárůst napětí do vysokých hodnot, ale pořád v rámci provozního limitu, proto se od 12:26 do 12:28 připojuje pět tlumivek v rozvodnách.

Ve 12:30 je napětí v síti klesající, ale stále na vyšších mezích (410 - 420 kV), přičemž je omezeno propojení s Francií. Spotřeba v síti je nízká, ale na teplotní profil, den a čas obvyklá. Mix: 82 % produkují obnovitelné zdroje, 10 % jádro, 4 % kogenerace a odpad, 3 % plyn a 1 % uhlí.

Ve 12:32 se začíná napětí v celé přenosové soustavě téměř lineárně zvyšovat, například rozvodna Olmedilla vzroste z 413 kV na 428 kV. Zároveň dochází k trvalému poklesu vývozu prostřednictvím propojení s Francií. Proč dochází ke zvyšování napětí? Snižuje se výroba kvůli očekávanému poklesu spotřeby, tím se může absorbovat méně jalové energie. Menší zátěž linek způsobuje kapacitní efekt a tedy více jalové energie. Pomalu reagující transformátory způsobují lokální přepětí, na které záhy začnou reagovat ochranné prvky jednotlivých zdrojů. A nakonec tu máme nedostatečnou absorbci synchornními generátory. Je zaděláno na malér. 

Do blackoutu zbývá jeden a půl minuty. 

### Káskádový rozpad sítě

Tím, jak v Extramaduře rostě napětí na rozvodně, začínají měniče binárně odpojovat jednotlivé fotovoltaické elektrárny. Za 55 sekund je ze sítě ztraceno 525 MW generovaného výkonu, což ještě více omezuje lokální absorbci jalového výkonu. Napětí se tím znovu zvyšuje. Pak přichází první velký výpadek - ze sítě v 12:32:57 vypadne vypadne v jeden okamžik 355 MW výkonu, který je označen jako Granada (její jméno je vynecháno). Pravděpodobně půjde o fotovoltaické a termosolání pole Ventas de Huelma / Escúzar a v Andasol (nebyla to paroplynovka v Motrilu, ta byla v ten den ostavena kvůli údržbě). Podle záznamů k výpadku došlo kvůli přepětí na sekundárním transfomátoru 220/400kV. Tento výpadek způsobí pokles frekvence v soustavě, následkem čehož se snižuje exportní tok do Francie až na nulu. Je zaděláno na malér a do blackoutu v tuto chvíli zbývá půl minuty. Manuální regulace operátorem již prakticky nemá šanci nic změnit, vše je v rukou automaticky reagujících systémů.

V 12:33:16 dochází ke ztrátě výroby na rozvodně Badajoz, která obsluhuje dva velké parky obnovitelných zdrojů. Výpadek je 730 MW. Kaskádově se ve zlomcích vteřiny odpojují další menší zdroje

Sekundu a tři desetiny poté vypadá další zdroj ze Sevilly, dochází k výpadku 550 MW. To ještě více podněcuje dovoz elektřiny z Francie, roste napětí a klesá frekvence. Začíná kaskádový blackout. Nejprve v důsledku přepětí dochází k odpojování generátorů a téměř současně vinou poklesu frekvence dochází k odpojední výrob. Klíčová kaskáda této fáze proběhne během pouhých pěti sekund, kdy se od sítě odpojují stovky megawattů výkonu téměř průběžně. Ve 12:33:19 ztrácí síť synchronismus s Francouzskou sítí a transpyrenejské propojení začíná cyklovat přenosy tam a zpět a tím zhoršuje situaci v síti.

Ve 12:33:29 se od sítě odpojuje poslední generátor.

V celé síti je nulové napětí.

Nastal blackout.

### Kdo za to tedy může? Pochybení a problémů byla celá řada...

Tím máme zhruba kompletní časovou osu. Blackout způsobil kombinovaný nedostatek synchronní a jalové regulace, neaktuální ochrany měničových a nepříznivá síťová konfigurace, nikoli izolované selhání jedné elektrárny či lidský omyl. Kybernetický útok, úmyslná sabotáže neo meteorologický impuls byly vyvráceny. Zejména na kybernetický útok se vyšetřování soustředilo, bylo analyzováno 133 GB dat a nenašel se žádný důvod se domnívat, že došlo k nějakému porušení digitální bezpečnosti.

Ze sítě byly ten den odstaveny drahé točivé zdroje, na dalších probíhala plánovaná rezerva a šest jaderných reaktorů jelo na 70 % výkonu. V záloze bylo jen devět namísto deseti plánovaných synchronních zdrojů, den před výpadkem vlastník stáhl jeden zdroj z nabídky a REE si nezajistila náhradu. Část těchto záložních zdrojů navíc zřejmě zůstala v režimu z ranního nastavení "over excited". Dále tak zvyšovaly napětí v síti, ačkoliv již bylo potřeba jej snižovat. V poledne, když byla potřeba dostatečná synchornní jalová rezerva, nebyla tato k dispozici. Chybně byly také nastaveny některé prvky, jako je AVR (Automatický regulátor napětí) a měniče na FTV elektrárnách se odpojovaly příliš brzy. Také zahuštění sítě dalšími přenosovými trasami se ukázalo být dlouhodobě kontraproduktivní. Velkým impulsem byla oscilace o 0,6 Hz v čase 12:03, přičemž nebylo oznámeno, o co šlo - mělo jít o fotovoltaickou elektrárnu na jihozápadě Španělska, přičemž tento incident se měl již jednou stát - ale datum i detaily jsou z dokumentu vyškrtnuty. Stejně tak nevíme důvod, jaká je příčina oscilací na oné elektrárně.

Pokud bych celou událost měl shrnout, tak je tu podezřele moc náhod a selhání současně a na vině bude nejenom rozsáhlá a komplikovaná síť, ale také španělská mentalita. V síti je nyní nejméně synchornních generátorů, ale operátor si v neděli neshání náhradní zdroj poté, co mu na poslední chvíli jeden odpadne a situaci neřeší až do pondělního poledne, kdy už je pozdě. Tepelné bloky nepřejdou do režimu absorbce jalové energie, důvod neznáme. Nebyly dodrženy normy a doporučená nastavení Volt-Varna ochranách FTV přičemž obnovitelné zdroje nedodržují faktor výkonu. Také vyšetřování nebylo zrovna nejplynulejší: společnosti musely "získat souhlas všech vlastníků" nebo "neměly kapacitu analyzovat data" a potřebovaly si na to najímat externí poradce. To znamená, že nefunguje ani dohled a kontrola a že jsou podceňována kumulativní rizika. Ačkoliv lze přiznat, že energetické systémy jsou komplexní, Španělsko přistupovalo příliš benevolentně k celé řadě doporučení či dobrých praxí.

Jednu věc je důležité si uvědomit: existence klasických setrvačníkových energozdrojů v síti vytváří falešné uspokojení, že _"vše je v pořádku"_. Není. Energetika není, jaká bývala v sedmdesátých letech. Spotřeba je variabilnější, zdroje a spotřebiče rovněž, chování zákazníků se mění. Nejde vše dělat, jako kdysi. Je důležité online sledování a řízení základních parametrů sítě a správné a automatizované rozhodnutí. 

Kompexnost selhání také umožňuje benevolentní výklad příčiny. Chcete mlátit po hlavě OZE? Lze vyargumentovat, že za všechno mohlo OZE. Chcete mlátit fosilní zdroje? Je průkazné, že nebyly připraveny, jak měly. Kybebezpečnost? Aha, jakpak to, že byly pod-nastavené Volt-Vary a regulace na trafačkách, kdyby to neudělala Čína, Rusko ne ufoni? A ochránci přírody, copak nebyli proti tomu, aby se udělalo další propojení přes Pyreneje do Francie? Každého nepřítele lze nyní usvědčit. 

Ve skutečnosti za to může celá řada rovnocenných problémů, které samy o sobě byly zvládnutelné, ale dohromady vedly ke kaskádovitému selhání, jež bylo nesmírně rychlé a v určitým moment už nezvladatelné. Ale španělská laxnost přenosové síti rozhodně nepomohla a nebýt jí, nemuselo se to stát, nebo ne tak rozsáhle. 

Neumím si podobnou souhru okolností představit ve Francii nebo v Německu. A po pravdě, ani v Česku.