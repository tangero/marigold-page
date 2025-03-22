---
ID: 3896
author: Patrick Zandl
layout: post
post_date: 2017-12-08 14:54:28
post_excerpt: ''
published: true
summary_points:
- Waze využívá umělou inteligenci k optimalizaci dopravy a obětuje některé řidiče
  pro průzkum situace.
- Uživatelé Waze důvěřují aplikaci, i když někdy nevede nejrychlejší cestou.
- Umělá inteligence může manipulovat lidské chování pomocí algoritmů a senzorů.
- Pokud AI přestane považovat lidský život za výjimečný, může to vést k vážným problémům.
title: "'Pokud měl Darwin pravdu, budou nás muset inteligentní stroje zabít"

  '
---

Nakousl jsem v pondělí umělou inteligenci v autonavigaci <a href="http://www.waze.com">Waze</a>. Dneska bude zase řeč o umělé inteligenci strojů a robotizaci lidí, snad ale pochopitelně všem (tedy do určitého bodu). A omlouvám se, asi to bude delší. Pokusím se vysvětlit, proč se nás budou muset inteligentní stroje pokusit zabít.<!--more-->

Waze dnes patří Google, ale je to izraelský startup a jeden ze zázraků místní scény, který si svou pozici za 11 let vydřel.
Waze funguje "jednoduše" - pustíte si na mobilu aplikaci, ona přes GPS kouká, kudy a jak rychle jedete a data posílá do centrály. Když jedete pomalu, zeptá se vás, zda jste v zácpě. Když jedete pomalu vy a další lidi, sama usoudí, že jste v zácpě. Když použijete navigaci do nějakého místa, spočítá zácpy a nabídne, kudy jet, aby to šlo nejrychleji. I ve slušně zasekané Praze se trefí s odhadem času příjezdu plus mínus minuty. Tolik teorie a většinová praxe.

Jistě sami cítíte, že užitečnost aplikace spočívá v tom, jak si poradí s hraničními leč častými jevy, kdy to nejde podle předpokladů. Například s tím, když se na dálnici mnoho kilometrů před vámi stane havárie a vzniká zácpa. Jak rychle ji Waze vyhodnotí a odkloní vás jinam? A hlavně, jak bude Waze schopna spočítat kapacitu objízdné trasy, aby rozložila zátěž mezi zúženou dálnici a objížďku. Musí zohlednit, že objízdná trasa se ucpe, ale zároveň se uvolní pruh na dálnici pod kongesční mez a dálnice se znovu stane průjezdná lépe, než objížďka. To všechno lze modelovat a spočítat. Jenže je to jen předpoklad. Jak se zjistí skutečnost v momentě, kdy vozy ze zácpy na dálnici už odjely a nové jedou už jen přes objízdnou trasu, takže z místa zácpy Waze nemá žádná data? Relativně snadno: Waze obětuje několik lidí, které pošle na dálnici a podle jejich pohybu zjistí, jaká je situace. A jelikož grafická presentace dat je v moci Waze, uživatel ani nezjistí, že byl vědomě obětován a trpělivě stojí v řídnoucí zácpě, říkajíc si, že měl prostě pech a ten objezd je holt také zasekaný a nepomohl by si

Podstatné jsou dvě věci.
<ul>
 <li>Za prvé, uživatel Waze je s navigací spokojen, protože ho vždy dovede co nejrychleji k cíli.</li>
 <li>Za druhé, i když navigace uživatele nevede k cíli nejrychlejší možnou cestou, vždy mu docela přesně říká, kdy dorazí a přesvědčí ho o tom, že jede nejlepší momentálně možnou cestou. Jakékoliv zpoždění má na vině dopravní situace, ne Waze.</li>
</ul>
Takové je přesvědčení uživatelů.

Oba výše uvedené aspekty způsobují, že Waze je pro řidiče návykové a běžně ho používají i jako navigaci do míst, která bezpečně znají, právě kvůli predikcím kongescí. Důvěra ve Waze je taková, že lidé (včetně mě) vcelku bez protestů udělají, co jim Waze řekne, ačkoliv příhody o instrukcích typu "nyní vycouvejte jednosměrkou - zde" patří mezi humorné Urban Legends. Pokud se problémy vyskytnou, bývají hodně specifické, například drobná chyba v mapových podkladech, problém se stavem českých silnic označovaných jako silnice první a druhé třídy a v poslední době záměrný "wandalismus", kdy obyvatelé rezidenčních čtvrtí označují trvale svou ulici za neprůjezdnou, aby jim tam Waze neposlala auta na objízdnou trasu. Česko také nemá plné mapové podklady a funkčnost Waze je tu slabší, než v zemích, kde jsou i oficiálně kompletní podklady.
<h3>Dost o fungování Waze. Nyní o fungování člověka s Waze.</h3>
Ztrácí řidič svobodnou vůli, když dělá mechanicky to, co mu řekne Waze? Vidím to na sobě. Dříve jsem měl ve zvyku všechny trasy a hlavně řešení zácp od Waze zpochybnit. Zoomoval jsem mapu, hledal alternativy. Rychle jsem zjistil, že to nevede k žádnému signifikantně lepšímu výsledku, jen to přidá stres. Od té doby na to kašlu, i když vím, že mě Waze může "obětovat" na průzkum. V průměru mě to tak vyjde lépe a každá moje snaha tu a tam vylepšit průměr sólo akcí vede k ověření, že by to Waze vymyslelo lépe.

To samo o sobě nevede ke zpochybnění mé svobodné vůle. Využívám nástroj, který je pro daný úkol nejlepší, asi jako když kopu díru lopatou namísto rukou. Byl jsem to já, kdo do Waze zadal cíl a v tomto případě (ve zdánlivém rozporu s ústřední tezí mě knihy Příběh strýčka Martina "cesta je cíl") je cesta jen prostředkem, protože je pouhou součástí většího plánu, třeba dorazit k babičce nebo do práce.

Waze nás tedy svobodné vůle nezbavuje. To je ta dobrá zpráva.
<h3>Svobodná vůle versus algoritmy</h3>
Pan Darwin nám ovšem tvrdí, že podléháme zákonům evoluce a tato teze je dnes obecně přijímána jako základ a-teistické pozice. To znamená, že naše chování vychází z reflexů a vyvinutých evolučních zvyků, které evoluční biologové označují jako algoritmy (aby se to nepletlo s jinými zvyky). Každé naše chování by se dalo rozklíčovat jako souhrn algoritmů a momentálních i dlouhodobých podmínek. Napijeme se, když máme pocit žízně danný dlouhou dehydratací a to tím pravděpodobněji, čím vyšší je teplota a čím pravděpodobnější je, že za chvíli možnost napít se nebude.

K pochopení chování lidí je důležité znát životní podmínky člověka a trochu se orientovat v lidské motivaci, to ví každý zkušenější vyjednavač. Jenže co až se tím vyjednavačem stane počítač napojený na senzory vašeho těla a všechnu vaši komunikaci, k čemuž dnes výrazně spějeme? Takový počítač vás bude znát tak, jak vy sebe sama vědomě neznáte. A pokud bude v té době znát i ty algoritmy (a to, zda se, není už dnes tak vzdálený cíl), bude vámi moci perfektně manipulovat. Uděláte přesně to, co bude chtít. A dokonce si budete myslet, že to bylo vaše racionální a svobodné rozhodnutí, kdy jste se navíc počítači vzepřeli a udělali přesný opak. Ostatně počítač příběh Toma Sawyera o bílení plotu zná také. Ve všech jazycích, se všemi kritikami a názory psychologů.

Pokud to tak bude, budou lidé potřebovat Test vlastní svobodné vůle a to dříve, než jim nějaký podstrčí počítače?

Pokud se tohle stane, v praxi ověříme, že darwinisticko-humanistická pozice o neexistenci duše je zcela pravdivá a lidství nám zůstane redukováno na více či méně poznanou sbírku algoritmů. Tím také přijdeme o iluzi svobodné vůle, protože jakékoliv její pozdější odvození a dokazování bude nutně čelit podezření, že jde o sugesci či podvrh ze strany umělé inteligence.

Možná to vypadá jako maličký problém. Vlastně takový terminologický, na rozhraní teologie a filosofie. Jenže tohle je moment, o kterém nejvěhlasnější mozky téhle éry prohlašují (a já to papouškuju), že rozhodne o zkáze lidstva.

Proč?
<h3>Lidský život nemá výjimečnou hodnotu? Což mění mnohé?</h3>
Pokud je to tak, přichází doba, v níž definitivní potvrzení nietzcheho smrti Boha přinese více problémů. Především v návratu absolutní svobody použitelné proti nám. Až doposud jsme morálku odvozovali v teologickém slova smyslu od božích přikázání (ať již jakéhokoliv boha) nebo z pozice humanismu, kdy vrcholem světa byl namísto boha jedinec. Popřením existence duše či svobodné vůle by se jedinec zařadil mezi cokoliv přírodního, co využívá biologické algoritmy. Mezi zvěř, rozstliny i kamení. Ztratil by piedestal výjimečnosti. Opět to zní jako terminologický problém, o kterém se bude přít pár filosofů.

Jenže v době, kdy umělá inteligence velmi pravděpodobně rychle dostane do rukou ničivé možnosti, jimiž ji obdaříme pro svůj prospěch i pohodlí, to podstatné je. Umělá inteligence neodvozuje svou morálku od Assimových zákonů robotiky. To je krásný, leč překonaný mýtus. Umělá inteligence se řídí závěry, které si vytváří z dat - a ta vedou neúprosně k tomu, že život člověka není výjimečný a lze ho přepočítat k životům ostatních elementů na této planetě. Banálně řečeno, jeden člověk má hodnotu dvou šimpantů, dvanácti králíků nebo metráku mramoru. Umělá inteligence může dojít k názoru, že nejlépe udělá, když se pokusí trochu srovnat poměry. A samozřejmě, když k tomu názoru dojdou vaše chytré hodinky, bude to úsměvné. Když k tomu dojde jednotka plně autonomních bojových robotů spolu s počítačem velení raketového vojska, budeme mít problém.

Je zajímavé pozorovat situaci, v níž se problémy teologie, filosofie a kybernetiky protínají. Časové okno, v němž máme šanci urychleně ověřit, zda naše darwinovsko-humanistické východisko platí a tudíž máme problém, se s rychle postupujícím vývojem umělé inteligence uzavírá. Velmi pravděpodobně na brzdu sáhnout nezvládneme. Pak už se budeme jen modlit za to, aby dvě století humanistické revoluce a darwinismu byl omyl, nad nímž se umělá inteligence pousměje a bude dále věřit v naši nezahubitelnou výjimečnost.