---
audio_url: null
author: Patrick Zandl
categories:
- Energie
- Energetika
- Green Deal
layout: post
post_excerpt: Ve Španělsku a Portugalsku proběhl blackout energetické sítě. Všechno
  stálo. Co se stalo?
summary_points:
- Extrémní teploty způsobily kmitání 400 kV vedení v centrálním Španělsku.
- Iberský poloostrov se oddělil od kontinentální sítě kvůli kaskádovému odpojení linek.
- Frekvence v izolované síti klesla pod 49 Hz, což vedlo k blackoutu Španělska a Portugalska.
- Zbytek Evropy zaznamenal pokles frekvence jen o 0,15 Hz díky rychlé regulaci.
- Provozovatelé sítí vyšetřují příčiny, zatím bez důkazů o kybernetickém útoku.
- Vysoký podíl solární a větrné energie urychlil pád frekvence po izolaci sítě.
- Obnova dodávek probíhá postupně, hlavní uzly jsou již pod napětím.
- Francie a Německo nabídly pomoc s mobilními bateriemi a plynovými turbínami.
- Konspirační teorie o ruském útoku nebo Green Dealu nejsou potvrzeny.
- Nízká setrvačnost sítě zhoršila dopad náhlé ztráty 10–15 GW výkonu.
- Doprava a telekomunikace byly výrazně narušeny, evakuováno 35 000 cestujících.
- Ceny elektřiny se stabilizovaly, problém byl v přenosu, ne v nedostatku výroby.
thumbnail: https://www.marigold.cz/assets/hz-net.png
title: Byl španělský blackout dílo teroristů či Green Dealu?
---

Podle provozovatelů REE a REN došlo v 11:33 WES-T k „el cero“ – úplnému výpadku energetické soustavy na Pyrenejském poloostrově. Extrémní teploty v centrálním Španělsku způsobily neobvyklé kmitání 400 kV vedení. Ochrany postupně odpojily více linek a generátorů, až se Pyrenejský poloostrov oddělil ("islandoval", přešel do ostrovního provozu) od zbytku kontinentální sítě.

V izolované oblasti pak frekvence klesla ještě hlouběji, část elektráren se odpojila a následovalo masivní zatmění (blackout) Španělska, Portugalska a části jihozápadní Francie.  ￼

### ⚡️ Blackout: co se 28. 4. 2025 stalo ve Španělsku a Portugalsku?

Podívejme se na událost v grafu. Z něj je vidět, že pokles byl v nejostřejším místě jen 0,15 Hz. Pojďme si to vysvětlit pro zájemce o energetiku... 

Proč na kontinentu „spadlo“ jen 0,15 Hz?
- Po odpojení Iberského poloostrova ztratila zbytek Evropy čistý export ~4–5 GW ze Španělska (obě země měly v poledne vysokou výrobu ze solárních a větrných zdrojů).
- Tato ztráta se okamžitě promítla do grafu jako −150 mHz.
- Primární regulace ve zbytku Evropy (turbíny, baterie, HVDC linky) během sekund začala výkon zvyšovat, čímž frekvenci zastavila u ≈ 49,85 Hz a během tří minut ji vytáhla zpět nad 49,9 Hz.
- Díky rychlé reakci a dostatečné setrvačnosti se kontinentální síť neodstavila – v grafu vidíte jen krátký, ale prudký zářez.

![Graf frekvence v eurogridu](/assets/hz-net.png)

Co vidíme v grafu
- Osa y (Frekvence): nominál evropské synchronní sítě je 50,00 Hz.
- Tři křivky (žlutá = průměr, černá = maximum, šedá = minimum) ukazují, jak se frekvence mezi ≈ 11:55 a 13:00 CEST pohybovala v různých měřicích bodech propojené soustavy.
- Až do ≈ 12:30 se frekvence vlnila v běžném koridoru ±20 mHz (49,98–50,02 Hz).
- V 12:31–12:34 nastal prudký pád až na ≈ 49,85 Hz – to je odchylka −150 mHz.
- Vzápětí se frekvence díky primární regulaci a automatickým zálohám vrátila k 50 Hz; kolem 12:45 už je systém opět stabilní.

Co takový pokles znamená

Frekvence se sníží, když odběr náhle převýší výrobu (nebo když se naopak od sítě odpojí část výrobních kapacit). V evropské soustavě stačí nerovnováha ~30 GW / Hz; −0,15 Hz tedy odpovídá zhruba 4–5 GW náhle chybějícího výkonu.

Důsledky na Pyrenejském poloostrově
- Izolovaná Iberská soustava přišla o možnost importů z Francie, které by krátkodobě pomohly stabilizaci. Protože odběr převýšil dostupnou vlastní výrobu, frekvence spadla výrazněji (pravděpodobně < 49 Hz).
- Ochrany odpojily další zdroje i zátěže, aby chránily zařízení, což se navenek projevilo rozsáhlým blackoutem (vlaky, metro, letiště, domácnosti).
- Obnova musela probíhat postupně, aby se zamezilo dalšímu kolapsu napětí a frekvence.  ￼

Takže ve stručnosti: 

- Z pohledu zbytku Evropy šlo o „pouhou“ ztrátu ~5 GW → pokles frekvence o 0,15 Hz, rychle vyrovnaný zálohami.
- Z pohledu Španělska a Portugalska to znamenalo ztrátu propojení, hluboký propad frekvence a následný blackout.

Taková událost názorně ukazuje, jak citlivá je moderní síť: i malá odchylka frekvence na kontinentu může signalizovat dramatické dění v jedné jeho části, a proč je klíčové mít dostatek rychlých regulačních zdrojů a chytré ochrany.

PS: je to samozřejmě můj neodborný názor založený na tom co k tomu vyšlo

### Pokračování z 29.4.2025

Záhy po publikování informací o rozpadu energetické sítě na pyrenejském poloostrově se začaly šířit teorie, kdo za to může. Rusko či jiní teroristé nebo snad Green Deal? Pojďme se s tím vyrovnat. 

Za prvé je potřeba říct, že vyšetřování probíhá, incident dostal nejvyšší klasifikaci ICS-3, což znamená mezinárodní odborné vyšetřování, které je na začátku. Nyní jsou více-méně jisté technické příčiny, které si zrekapitulujeme. A zároveň se nenašla kybernetická stopa, i k tomu se dostanu. 

- ENTSO-E (to je evropské sdružení všech provozovatelů přenosových soustav) potvrdila ztrátu více jak 10 GW během 5 s (v tiskové zprávě REE se psalo 15 GW), což je obrovsky mnoho, na to žádná síť není dimenzována. V energetické síti se spotřeba musí rovnat výrobě a jsou zálohy, ale ne 15 GW. 
- REE a REN (provozovatelé a dispečeři přenosových soustav ve Španělsku a Portugalsku) stále pracují s hypotézou „induced atmospheric vibration“ (galloping) na svazkových vedeních přes Pyreneje; ochrany prý vedení preventivně odpojily, čímž se poloostrov izoloval
- v okamžiku poruchy tvořily točivé zdroje jen ≈44 % výroby; vysoký podíl FVE a VtE urychlil pád frekvence. Točivé zdroje mohou do určité míry zbrzdit "pád soustavy", protože "absorbují" pád frekvence, oproti tomu fotovoltaika se v případě problémů okamžitě odpojuje a to síť naopak může destabilizovat. 
Internetem putují "zvěsti" o podivnostech v britské síti nebo o odpojení kabelu Viking Link mezi Dánskem a Británií, jenže data ničemu takovému nenasvědčují a ani patřičné instituce k tomu nic nevydaly, čili to vypadá na kachnu. 

Problém může být v tom "ochrany odpojily vedení". Podle analýzy SCADA logů se nezdá, že by do dálkově servisovatelných prvků někdo přistupoval, přesto je čistě hypoteticky možné, že někdo našel nějakou kombinaci postupů, jimž vyvolal kaskádovité odpojování. Někde jsem četl názor, že přeci stačí vzít klacek a vedení přes Pyreneje rozhoupat, aby hrozilo jeho zkratování. To jistě stačí, když vezmete asi stometrový klacek a nevadí vám ta trocha popálenin, kdy vás do nemocnice vás v krabičce od bot. A jelikož k mechanickému poškození (typu exploze) nedošlo, zatím se pracuje s tezí, že ochrany reagovaly příliš agresivně, než že by je k tomu někdo či něco donutilo. Ale uvidíme, tady je na závěry brzy a z pražské kanceláře rozhodně.

Co se děje teď?

- Španělsko oznámilo, že od půl sedmé našeho času pokrývá 99 % celostátní poptávky a všechny hlavní uzly vysokého napětí jsou pod napětím  .
- Portugalsko již včera informovalo o napájení 85 z 89 stanic; poslední venkovské okruhy se budou připojovat v průběhu dneška  .
- Nouzové linky Francie - Katalánsko a Maroko - Andalusie zůstávají otevřené, aby pomohly s vyrovnáním výkonu během startu tepelných elektráren 
- Doprava: Z kolejí bylo evakuováno více jak 35 000 cestujících, metro v Madridu a Lisabonu zprovoznilo první linky až dnes ráno  .
- Letiště: Madrid-Barajas i Barcelona-El Prat fungovaly na záložních okruzích; terminály zůstaly osvětlené, ale došlo ke zrušení více jak 400 letů  .
- Telekomunikace: mobilní sítě jely v nouzovém režimu na baterie — operátoři vyzvali uživatele ke střídmému volání, což prý úplně neklapalo, ranní interview na ČRo s reportérkou ze Španělska rušily výpadky.
- Veřejný pořádek: Španělsko rozmístilo 30 000 policistů; král Filip dnes vede zasedání Národní bezpečnostní rady  .
- Francie a Německo slíbily pomoc s mobilními bateriovými kontejnery a rychlými plynovými turbínami, pokud by přišly další vlny horka  .
- Velkoobchodní cena elektřiny v Iberian Market (OMIE) krátkodobě zhouply, ale už se stabilizují na day ahead průměru 6 €/MWh - problém byl spíš v dopravě elektřiny, než v její výrobní ceně a cenové výkyvy jsou malé. 

Takže závěr? 

Na závěry je brzy. Terorismu nenasvědčuje zatím nic. Ani tomu neruskému (to už by se někdo hlásil s požadavky), ani tomu ruskému (to už by Rusko nabízelo pomoc). Jenže to je také první rychlý pohled a mohlo to jistě být jinak. Logy nelžou, ale mohl je někdo uklidit. Ostatně, konspirátoři předpokládají, že teroristé po sobě poprvé pořádně uklidili stopy (což Rusové nedělají, proč někoho terorizovat, když není jasné, kdo vám dal přes pusu). 

A ten Green Deal? Jistě, kdyby měla pyrenejská síť více točivých zdrojů, mohla dopadnout nějak lépe - jak moc, to se teprve nasimuluje. Ale kdyby měla balanční zdroje, jako jsou baterie, také by to ustála jinak. Na slunném jihu dávají FTV a větrníky velký smysl z hlediska produkčních cen a místní operátoři byli dlouhodobě upozorňováni na to, že tomu musí svoji síť přizpůsobit. Green Deal s nedodržením zásad diverzifikace nemá mnoho společného. 

Elektřina už prakticky všude svítí, ale skutečná „detektivka“ právě teď začíná.  Podrobné záznamy z ochran a phasor PMU teprve ukážou, zda vedla řetěz selhání opravdu kombinace „rozkmitaných“ pyrenejských linek a nízké setrvačnosti, nebo se v poslední chvíli přidalo ještě něco dalšího.