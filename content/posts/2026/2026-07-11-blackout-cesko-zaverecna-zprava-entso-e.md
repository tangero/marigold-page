---
author: Patrick Zandl
categories:
- Energie
- Energetika
- ČEPS
layout: post
post_excerpt: Rok po blackoutu vydal expertní panel ENTSO-E závěrečnou zprávu. 122 stran, které definitivně uzavírají, co se 4.7.2025 stalo. Potvrzují vadnou spojku i to, že výpadek Ledvic nebyl žádná nesouvisející náhoda. A přinášejí dvě zjištění, o kterých se u nás zatím moc nemluvilo - dispečink měl predikci kaskády celou dobu na stole a zákon mu zakázal udělat to jediné, co mohlo region zachránit. Pročetl jsem celou zprávu a tady to máte, opět ve dvou úrovních stručnosti. Včetně toho, kde jsem se ve svých předchozích rozborech mýlil já.
title: "⚡️📋 Blackout v Česku podruhé a snad naposledy: co říká závěrečná zpráva ENTSO-E"
thumbnail: https://www.marigold.cz/assets/spojka-energetika.jpg
audio_url: null
---

Skoro přesně rok od chvíle, kdy severozápad Česka a kus Prahy zhasly, vydal expertní panel ENTSO-E [závěrečnou zprávu o incidentu](/assets/ebook/entso-e_incident_report_CZ_final_report_260626_fv.pdf) (26.6.2026, 122 stran, anglicky). Zpráva zapadla bez většího ohlasu médií. Nicméně stojí za to se k ní vrátit. Události totiž oficiální zpráva nelíčí tak, jak ji vykládá ČEPS a ČEZ. Obě firmy si "přitáhly deku na svou stranu" a to z dobrého důvodu. Másla mají na hlavě dost. Krizovou komunikaci ale tyto firmy zvládly na výbornou, ačkoliv ve vině za blackout Česka si podle zprávy mohou podat ruce. 

U role médií se zastavíme na závěr na závěr. Byla tristní. 

Nejdříve k odbornosti. Panel vedl Donatas Matelionis z litevského Litgridu, sedělo v něm 18 expertů z ACER, národních regulátorů a evropských provozovatelů přenosových soustav - a ČEPS podle pravidel nesměl psát kapitoly o vlastních krocích. Je to tedy nejnezávislejší pohled na český blackout, jaký kdy budeme mít. A druhá věc: zpráva hned na začátku říká, že je zprávou technickou, nesnaží se hledat viníky, ale rekonstruuje skutečnost, běh událostí. I proto je potřeba "číst mezi řádky", ne snad z touhy zamlčet, ale prostě proto, že tohle je technická zpráva.

O blackoutu jsem psal [týden po události](/item/blackout-cesko/) a pak [v prosinci po vydání Rozboru ČEPS](/item/blackout-cesko-vysledky-zpravy/). Obojí si dovolím vzít jako závazek: když jsem tehdy rozdával hodnocení, musím teď férově přiznat, kde mi závěrečná zpráva dala za pravdu a kde jsem uklouzl. V obou kategoriích se něco najde.

Ve zkratce, co se stalo (a tentokrát už definitivně): Dne 4.7.2025 v 11:51 se na 400kV vedení V411 přetrhl vodič - selhala tahová spojka z havarijní opravy v prosinci 2024. Frekvenční ráz během čtyř vteřin vykopl Ledvice, Počerady a Opatovice z normální regulace do ostrovního režimu. Ledvickému bloku 6 při tom manévru odešel kotel a blok postupně ztratil všech 292 MW - jenže generátorový vypínač zůstal zapnutý a dispečink ČEPS šest minut viděl elektrárnu, která ve skutečnosti nedodávala nic. K tomu odpadlo 135 MW fotovoltaik a dalších 151 MW se ztratilo neznámo kde. Poslední spojnice regionu, 220kV vedení V208, se přetížila na 143 % a dispečer ji v 11:59:44 vypnul v přesvědčení, že se nic dalšího nestane. Jenže pravidelný report mu ukazoval pravý opak, jen si toho nikdo nevšiml. Za tři vteřiny vypadly i zbylé dva spoje, vznikl ostrov s deficitem 1 800 MW a ten se za necelou vteřinu zhroutil. Bez proudu 2 300 MW zátěže, 28 % české spotřeby. Obnoveno do 17:35, V411 opravena týž den ve 23:13.

Celý průběh jsem podle zprávy zrekonstruoval do interaktivní časové osy. Stiskněte ▶ a sledujte minutu po minutě, jak se zavíralo okno na záchranu - zelené body ukazují okamžiky, kdy šlo blackoutu ještě předejít, purpurový bod je moment, ze kterého už nebylo návratu:

<figure style="margin:1.5em 0">
  <iframe id="blackout-timeline" src="/assets/blackout/timeline.html?embed=1" width="100%" height="760" style="border:0;border-radius:14px;display:block" loading="lazy" title="Interaktivní časová osa blackoutu 4. 7. 2025"></iframe>
  <figcaption style="font-size:.85em;opacity:.75;margin-top:.5em">Interaktivní rekonstrukce blackoutu podle závěrečné zprávy ENTSO-E. Ovládat lze i klávesnicí (šipky, mezerník). <a href="/assets/blackout/timeline.html" target="_blank" rel="noopener">Otevřít na celé stránce</a> - tam najdete navíc rozbor Bodu bez návratu, čtyři okna prevence a všech devět doporučení.</figcaption>
</figure>
<script>
addEventListener('message',function(e){
  if(e.data&&e.data.blackoutTimelineH){
    var f=document.getElementById('blackout-timeline');
    if(f)f.style.height=(e.data.blackoutTimelineH+4)+'px';
  }
});
</script>

Hlavní závěry pro ty, kdo nemají čas na detail:

1️⃣ **Spojka definitivně potvrzena.** Kloknerův ústav prokázal nedotaženou hliníkovou část tahové spojky z opravy 2024. Proč se to montérům stalo, panel nezjistil.

2️⃣ **Báchorka o nesouvisejících jevech je mrtvá.** Strom příčin ENTSO-E kreslí od pádu V411 k výpadku ledvického kotle jako souvislý kauzální řetěz. Žádná pravděpodobnost 1:3 000 000 se nekoná. Kecali nám. 

3️⃣ **Nejtvrdší novinka: kaskáda byla predikovaná.** Pravidelný N-1 výpočet ČEPS v 11:55 správně ukázal, že vypnutí V208 shodí Krasíkov. Nikdo si toho nevšiml. Proč, to je temná výtka zprávy, kterou nutno číst i mezi řádky. 

4️⃣ **Právní past.** Ruční odepnutí spotřebitelů vyžadovalo vyhlášení stavu nouze, což trvá desítky minut. Jediné opatření, které mohlo region udržet, bylo právně nedostupné. Tady musím korigovat i svůj prosincový text.

5️⃣ **Odstávky zpráva nekritizuje.** Můj prosincový "tichý zabiják" v závěrech panelu oporu nemá. Ubírám.

6️⃣ **A fotovoltaika taky nebyla úplně bez viny.** 135 MW odpadlých zdrojů, z toho 35 MW v rozporu s předpisy. Není to příčina blackoutu, ale "žádný podstatný dopad", jak jsem napsal v prosinci, to také nebyl.

Pojďme na to podrobněji.

### 🔧 1. Spojka: případ uzavřen

Ta „jedna blbá spojka", o které jsem psal pět dní po události, dostala definitivní potvrzení. Vzorek putoval přes Policii ČR do certifikované laboratoře a Kloknerův ústav ČVUT našel přesně to, co se u lisovaných spojek najít dá: ocelové jádro slisované správně, hliníková část nedostatečně. Vyšší přechodový odpor, lokální ohřev, tepelná degradace ocelového jádra, přetržení. Učebnicový mechanismus.

Dva detaily stojí za pozornost. Zaprvé, když Klokner po opravě v roce 2024 testoval demontované lano a shledal je vyhovujícím, platilo to - jak zpráva suše poznamenává - pro lano samotné, ne pro spojku. Selhala přesně ta součást, kterou nikdo netestoval. Zadruhé, panel výslovně přiznává, že se mu nepodařilo zjistit, proč renomovaná firma s dlouholetou praxí spojku špatně slisovala. A doporučení R1 (fotodokumentace kritických kroků montáže, termovize po havarijních opravách) neadresuje zhotovitele, ale provozovatele soustav. Přeloženo: chybu udělal dodavatel, ale systém, který ji měl zachytit, je starost ČEPS. Mimochodem - mimořádná letecká termovize po události našla na V411 další závady. Jen tak dál...

### 🔗 2. Konec báchorky o náhodě

Tisková zpráva ČEPS z prosince vyprávěla o „vzájemně nesouvisejících poruchách" s pravděpodobností souběhu 1:3 000 000. Už tehdy jsem psal, že tomu může věřit leda ten, kdo věří na zázraky. Závěrečná zpráva to uzavírá elegantně: v Root Cause Tree, stromu příčin na straně 113, vede od výpadku V411 k výpadku ledvického kotle nepřerušená šipka. Ráz z výpadku vedení → přechod bloků do ostrovní regulace → regulátor turbíny si přivřené ventily vzal jako nový setpoint → otevírání obtokových stanic → vysoká teplota páry → zásah ochran kotle. Bezprostředním bodem selhání bylo vadné relé pohonu obtokového ventilu, latentní vada, která si počkala na první ostrý manévr. Ale ten manévr si vyžádala síť. Bez pádu V411 by relé vesele chátralo dál a nikdo by o něm nevěděl. A v praxi to tak je, že tyto skryté vady se projeví v momentě, kdy se děje něco nestandardního, čili eskalují eskalaci. 

ČEZ ve zprávě dvakrát opakuje, že porucha relé „nijak nesouvisela" s ostrovním režimem - a panel to pokaždé uvozuje opatrným „podle vyjádření elektrárny", bez vlastního potvrzení. Zpráva navíc v doporučení R5 přiznává, že vyšetřování brzdila chybějící data od výrobců a distributorů. Otázka, kterou jsem položil loni v červenci - zda lze bez nezávislé analýzy dat z řídicího systému brát vyjádření ČEZ za směroplatné - tedy zůstává formálně otevřená i po závěrečné zprávě. Panel verzi s relé převzal, neověřil. Zřejmě neměl jak. 

A Ledvice mají ve zprávě ještě dva vroubky. Blok 4 měl v ostrovním režimu nastavený droop (statiku regulátoru) na 0 %, tedy teoreticky nekonečné zesílení - kodex předepisuje 4 až 10 %. Blok se rozkmital a jeho oscilace se propsaly do okolních vedení i do telemetrie. A protože je připojený do distribuce, ČEPS jeho nastavení nikdy necertifikoval a certifikovat nemohl. A blok 6 po výpadku kotle zůstal připojený se zapnutým vypínačem, zpětná ochrana kvůli oscilacím nezareagovala a chybná validace signálů v řídicím systému elektrárny poslala dispečinku telemetrii bez oscilací. Fantomový stav, o kterém jsem psal v prosinci, potvrzen do posledního detailu včetně telefonátu v 11:58:25, kterým si dispečink stav Ledvic konečně ověřil.

### 🖥️ 3. Přehlédnutá predikce: nejtvrdší zjištění zprávy

Tohle je novinka, kterou prosincový Rozbor ČEPS takhle ostře neformuloval. Jeho dispečer před vypnutím V208 provedl ad-hoc výpočet toků a N-1 v takzvaném study módu a vyšlo mu, že vypnutí nebude mít další následky. Jenže pravidelný N-1 výpočet, který běží automaticky každé dvě minuty, už v 11:55 správně ukazoval, že vypnutí V208 přetíží spojku v Krasíkově nad limit její ochrany. Citace ze zprávy: tento efekt „nebyl v danou chvíli identifikován".

Jinými slovy: informace, že ruční vypnutí V208 spustí rozpad, ležela čtyři minuty v systému, který ji spočítal, zobrazil a nikdo ji v záplavě alarmů nezaznamenal. A aby toho nebylo málo, výsledky onoho ad-hoc výpočtu, na jehož základě dispečer rozhodl, se neukládají - takže panel nemohl zrekonstruovat, co přesně dispečer viděl a proč mu vyšel opak. ČEPS za to dostal dvě doporučení: R6 s prioritou High na vizualizaci kaskádních rizik a R9 na archivaci study-mode výpočtů. Obojí je diplomatický jazyk pro „vaše nástroje v krizi selhaly a my to ani nemůžeme pořádně prošetřit".

K dispečerům samotným zpráva zůstává férová a já se pod to podepisuji i podruhé: rozhodovali pod tlakem, s legitimní obavou z provisu vedení nad Prahou, s telemetrickou lží od Ledvic a s výpočtem, který jim dal zelenou. Selhalo rozhraní mezi stroji a lidmi, ne lidé.

### ⚖️ 4. Právní past aneb kde musím korigovat sám sebe

V prosinci jsem napsal, že kdyby dispečer věděl o skutečném stavu Ledvic, okamžitě by odepínal velké spotřebitele a situace by se zvládla bez rozpadu. Zněla to logicky. Závěrečná zpráva tenhle můj kontrafaktuál bourá: ruční odepínání zátěže vyžaduje podle českého práva vyhlášení stavu nouze, což trvá desítky minut. Redispečink byl příliš pomalý, navýšení výkonu distribuovaných zdrojů technicky nemožné, přečerpávací Dlouhé Stráně se nedaly zastavit včas. Dispečer neměl k dispozici žádné opatření, které by deficit regionu vyřešilo v řádu minut - ani s dokonalou informací.

To je možná vůbec nejzávažnější systémové zjištění celé zprávy a zaslouží si pozornost zákonodárce, ne jen energetiků: jediný nástroj, který mohl zabránit rozpadu, byl vyloučený zákonem. Doporučení R7 (priorita High) výslovně vyzývá, aby TSO navrhli regulatorní a legislativní změny tam, kde právní překážky brání včasné aktivaci nouzových opatření. Stav nouze byl nakonec vyhlášen - zpětně, k 12:00, když už bylo po všem. Kafkovsky dokonalé.

### ☠️ 5. Odstávky: kde ubírám

Můj prosincový text stál na tezi, že klíčovým spoluviníkem byla kumulace plánovaných odstávek - 13 vypnutých vedení, „vykostěná" síť, selhání managementu rizik. Počet sedí (10 vedení 400 kV a jedno 220 kV plánovaně, dvě další v opravě). Jenže závěrečná zpráva tuhle interpretaci nepodpořila. Kritérium N-1 bylo splněno nejen papírově, ale i reálně: model v 11:51 ukazoval, že po výpadku V411 poběží V208 v limitu. Všechny plánovací procesy včetně evropských regionálních center proběhly bez nálezu. A především: mezi devíti doporučeními není jediné, které by se týkalo koordinace odstávek.

Panel tím implicitně říká: topologie nebyla příčina. Slabší síť zmenšila rezervy, ale s korektně fungujícími zdroji by výpadek V411 v pohodě ustála. Krizi vyrobily nečekané ztráty výroby po přechodovém jevu - a to je fenomén, na který klasické N-1 nemyslí, ať máte odstávek kolik chcete. Moje úvaha o hazardu s odstávkami zůstává legitimní otázka k diskusi, ale závěry nezávislého panelu ji nepotvrzují a já to tímto přiznávám.

### ☀️ 6. Fotovoltaika: kde ubírám taky, ale jinak, než čekáte

V prosinci jsem napsal, že obnovitelné zdroje neměly na situaci žádný podstatný dopad. To bylo přestřelené - jen opačným směrem, než střílejí obvyklí démonizátoři OZE. Po výpadku V411 odpadlo 135 MW distribuovaných zdrojů, převážně fotovoltaik: 5 MW legitimně na frekvenční ochrany, 130 MW na ochrany napěťové. Z toho 95 MW jsou zdroje ze solárního boomu 2009-2010, které žádnou povinnost překlenout poruchu (fault-ride-through) nikdy neměly - a 35 MW zdrojů, které ji mít měly, a stejně odpadly. Perlička: měření na 110kV stranách transformátorů ukazují, že napětí v distribuci během poruchy vůbec neopustilo pásmo dovoleného trvalého provozu. Ty elektrárny odpadly na ochrany nastavené mimo realitu místa připojení.

V kontextu: ve fázi, kdy se rozhodovalo o přetížení V208, tvořilo těch 135 MW zhruba třetinu deficitu. K tomu připočtěme 151 MW, které se ztratily neznámo kde - panel je považuje za pravděpodobně další neidentifikovanou distribuovanou výrobu, ale chybí mu data. Všimněte si té ironie: identifikovaná ztráta v distribuci (160 MW) je skoro stejná jako ta neidentifikovaná (151 MW). Do poloviny toho, co se v distribuci děje, prostě nikdo nevidí, přesně jak jsem varoval v bodě 5 prosincového textu.

Takže ano, dědictví solárního boomu je reálná systémová zranitelnost a riziko hromadného odpadávání distribuované výroby dostalo doporučení R2 s prioritou High. A zároveň ne, blackout nezpůsobila zelená elektřina - způsobila ho spojka, relé a lhající telemetrie. Kdo z téhle zprávy vyčte „za blackout může fotovoltaika", neumí číst. Kdo z ní vyčte „fotovoltaika s tím neměla nic společného", neumí číst taky.

A teď ta druhá perlička. Zpráva odpadlé fotovoltaiky neidentifikuje. Tabulky jsou anonymní, jen výkony a data připojení. Jenže ta zdaleka největší z nich, která sama tvoří většinu oněch 35 MW odpojených v rozporu s předpisy, je popsána parametry: instalovaný výkon 55,763 MW, připojena v prosinci 2010 do 110kV oblasti napájené z transformátoru T401 Bezděčín. Odpadla na napěťovou ochranu hned v 11:51:05, ačkoliv napětí v místě podle měření nikdy neopustilo pásmo dovoleného provozu. Tahle signatura odpovídá na tři parametry přesně komplexu FVE Ralsko + Mimoň Ra 3: 55,8 MWp celkem, spuštěno v prosinci 2010, mezi Mimoní a Mnichovým Hradištěm, tedy v oblasti napájené právě z Bezděčína. Největší solární elektrárna v ČR. Vlastník: ČEZ. Prokázat to nemohu, zpráva jména neuvádí - ale parametrová signatura je dostatečně výmluvná.

### 👏 7. Co fungovalo

Aby to nevyznělo jen jako litanie: ochranná technika zafungovala kompletně podle nastavení.  V411, spojka v Krasíkově, transformátor T401 i frekvenční ochrany bloků. Počerady a Chvaletice úspěšně přešly do vlastní spotřeby, což zásadně urychlilo obnovu. Frekvenční odlehčování stihlo při pádu frekvence rychlostí 3,5 Hz/s aktivovat jen dva stupně ze šesti, ale na ostrov s deficitem 1 800 MW není stavěné a panel konstatuje, že fungovalo, jak mělo. Obnova top-down ze dvou stran: Praha kolem 13:00, všechny rozvodny do 14:09, kompletní zátěž do 17:35, V411 opravená týž den. A bilanci po rozpadu podržely dovozy regulační energie, hlavně z Německa - 2 578 MWh záporné aFRR. Propojená Evropa opět v roli pojistky, která zafungovala. Za tohle všechno palec nahoru. A pamatujete na to, jak první zprávy hned vinily "přetoky OZE z Německa"?

### 🎬 Závěrem

Kdo tedy za to může? Závěrečná zpráva z principu nikoho nejmenuje jako viníka, ale strom příčin a adresáti doporučení mluví jasně. Selhaly čtyři nezávislé subjekty naráz:

- **Montážní firma**, která v prosinci 2024 špatně slisovala spojku - a **ČEPS**, jehož přejímka to nezachytila.
- **ČEZ v Ledvicích**, hned třikrát: vadné relé, droop 0 % na bloku 4 v rozporu s kodexem a telemetrie, která šest minut lhala dispečinku. A napočtvrté zřejmě i špatně nastavená FVE patřící ČEZu, která situace pomohla zhoršit. 
- **Dispečerské nástroje ČEPS**, které správnou predikci kaskády spočítaly a nedokázaly ji dostat k člověku.
- **Český právní rámec**, který jediné účinné opatření podmínil procedurou na desítky minut.

V prosinci jsem napsal, že za výpadek v plném rozsahu může ČEPS. Po přečtení závěrečné zprávy to musím přeformulovat: ČEPS nese největší díl nápravných opatření - pět z devíti doporučení včetně dvou nejpalčivějších jde primárně za ním - ale obraz jediného viníka zpráva nepodporuje. Je to kolektivní selhání, ve kterém má každý svůj podíl a nikdo se nemůže tvářit, že se ho to netýká. Což je mimochodem horší zpráva než jeden viník: jednoho viníka opravíte, systémovou prohnilost napříč firmami, úřady a paragrafy nikoliv. Jenže takhle to v české energetice je - léta jsme se holedbali její robustností, jak úžasní jsme proti světu, ve skutečnosti si ale stále titíž lidé poplácávali ramena, jak jsou dobří, nechali se oslavovat médii, která vlastní vlastníci elektráren a tím vznikl nepravdivý obraz. 

Na mýtu o nejrobustnější přenosové soustavě světa trvám: je mrtvý. Soustava, která splní všechny normy, projde všemi kontrolami evropských koordinačních center a přesto ji položí jedna spojka, jedno relé a jeden nevšimnutý řádek v N-1 reportu, robustní není. Je normou vzorně zdokumentovaná. Jak přesně říká zpráva: soustava nebyla bezpečná už v N-0, šest minut před rozpadem. Všechno ostatní byla jen otázka času.

PS: O koordinaci odstávek ani o zdvojení V411 není ve 122 stranách jediné doporučení. Stavba V411/811 má být podle harmonogramu MPO hotová v roce 2027. Držme si palce, ať do té doby drží spojky a ČEZ si potajmu a v tichosti zkontroluje nastavení svých elektráren...

## Smutná zpráva o českých médiích

Dejme si smutný závěr. Napadlo mne podívat se, jak se vyrovnaly se závěrečnou zprávou česká média. A je to velmi smutné. Naprostá většina zpráv, která vyšla v červnu k vyhodnocení blackoutu, papouškovala tiskovou zprávu ČEPSu, respektive její převyprávění přes ČTK. Jistě, úlohou ČTK není dělat investigativu, takže ČTK je v tomhle nevinně. Přesto ji bez čehokoliv dalšího převzala média, která přesně před rokem dělala skandalizující články a velké odhalení, jako je oEnergetice (hluboké zklamání!), INFO.cz (tam také víme, že je to hlásná trouba uhelné energetiky) Česká televize (jak se jí to stalo?), iDNES, Hrot24 nebo TZB-info. Všechna tato média převzala zcela nekriticky ČTK postavenou na tiskové zprávě ČEPS. A to včetně titulkové teze "experti potvrdili souběh vzájemně nezávislých událostí", což je formulace pana Vnoučka z ČEPS, kterou závěrečná zpráva ENTSO-E nikde nepoužívá.

iDNES k vysvětlení ČEPS přidala jediné: připomínku spekulací o přetocích z Německa a Polska - tedy rekapitulaci už dávno vyvrácené teorie. Žádný vlastní vhled, žádný z klíčových nálezů. U druhého největšího zpravodajského webu v zemi je to příšerně slabý výkon. 

Lídrem nezájmu byla CNN Prima News i TV Nova, které (podle archivu) o zprávě nereferovaly pro jistotu vůbec, ačkoliv blackout na Kubě je zajímal hodně. Co mne překvapilo, že o nějaké pokrytí se nepokusil ani Deník N ani Aktuálně.cz. 

**Vlastní čtení zprávy tak zvládly jen tři redakce:** [Hospodářské noviny](https://byznys.hn.cz/c1-67899390-co-se-stalo-pri-ceskem-skoro-blackoutu-selhaly-ochrany-solaru-a-dispeceri-se-v-klicovy-moment-rozhodli-na-zaklade-chybneho-vypoctu) (nejlepší, leč za paywallem - titulek přímo jmenuje selhání ochran solárů a chybný výpočet dispečerů), [iRozhlas](https://www.irozhlas.cz/zpravy-domov/otazky-a-odpovedi-bod-zlomu-nastal-po-odpojeni-kabelu-jak-blackout-pred-rokem_2607041300_jos) (Jana Klímová doslova citovala pasáž o přehlédnuté predikci a rozstřílela Babišovu německou verzi) a [Ekonomický deník](https://ekonomickydenik.cz/lonsky-blackout-ceps-expertni-zpravy/). Ten si jediný vyžádal reakci ČEPS na nález o V208 a přidal kontext březnového odvolání šéfa ČEPS Durčáka. Všem třem redakcím upřímně blahopřeju, protože obstály. 

Seznam Zprávy bylo jednou z mála výjimek, které si [obstaraly komentáře třetích stran](https://www.seznamzpravy.cz/clanek/ekonomika-firmy-lonsky-vypadek-elektriny-byl-shoda-okolnosti-potvrdili-experti-309429), neměly ale šťastnou ruku, protože oba citovaní (Kotrba i Macenauer) jen papouškovali vysvětlení ČEPSu a zcela minuli to, co skutečně technická zpráva říká. Proč, zda se se zprávou nestihli seznámit, suď bůh. Tento článek nedopadl nejlépe, naštěstí [komentář Jiřího Nádoby ukazuje, že si v Seznamu tu zprávu někdo přečetl](https://www.seznamzpravy.cz/clanek/ekonomika-firmy-lonsky-vypadek-elektriny-byl-shoda-okolnosti-potvrdili-experti-309429#comment-) a že nemusíte být energetický expert, abyste viděli, že tam něco nesedí.

Média jsem procházel přes jejich vyhledávání, ne přes monitoring médií, čili vycházím z jejich vlastních dat. Všeobecně česká média dopadla velmi špatně. Chápal bych, kdyby to byla třetiřadá informace, ta po roce není podstatná. Ale tohle byla stěžejní událost dotýkající se bezpečnosti státu, s velkými ekonomickými i společenskými dopady. Proto je pro mne těžké se jen tak přenést přes nezájem, který vzbudila. A přes přístup, jaké jednotlivé redakce (čest těm výjimkám) zaujaly. Předpokládám, že to je také důvod obecné nedůvěry v česká média. Ztrácí svou schopnost informovat, zůstala jim jen schopnost nějak nás bavit. Opět čest výjimkám (a tady nechápu ten Deník N).
