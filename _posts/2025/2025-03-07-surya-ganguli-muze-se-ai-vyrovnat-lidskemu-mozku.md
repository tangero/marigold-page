---
audio_url: null
author: Patrick Zandl
categories:
- mozek
- AI
- projev
layout: post
post_excerpt: Přepis přednášky profesora stanfordské univerzits Surya Ganguliho věnované
  umělé inteligenci a lidskému mozku.
summary_points:
- AI potřebuje biliony slov pro trénink, lidé efektivněji využívají data díky evoluci.
- Energetická náročnost AI je obrovská, lidský mozek spotřebuje jen 20 wattů.
- Vysvětlitelná AI pomáhá pochopit fungování mozku, například sítnice a Newtonovy
  zákony.
- Spojení mysli a stroje umožňuje číst myšlenky a vyvolávat [halucinace](/halucinace/) ovládáním neuronů.
thumbnail: https://pi.tedcdn.com/r/talkstar-assets.s3.amazonaws.com/production/talks/talk_145110/9b1dbc4f-436c-4833-af8e-64d1e5e96145/SuryaGanguli_2024S-embed.jpg
title: Surya Ganguli - Může se umělá inteligence vyrovnat lidskému mozku?
---

Přednáška neurovědce a stanfordského profesora Stanfordu Suryi Ganguliho s názvem [„Can AI Match the Human Brain?“](https://www.ted.com/talks/surya_ganguli_can_ai_match_the_human_brain), která zazněla 22. října 2024 na konferenci TEDAI v San Franciscu.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Z9VovH1OWQc?si=VNdkbsbyXuTzWhDx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Co se sakra stalo v oblasti umělé inteligence za posledních deset let? Jako by se na naší planetě objevil zvláštní nový typ inteligence, který se však lidské inteligenci nepodobá. Má pozoruhodné schopnosti, ale také dělá hrozivé chyby, kterých se my nikdy nedopouštíme. A zatím neumí hluboké logické uvažování, které umíme my. Má velmi záhadný povrch schopností i křehkostí a my téměř nic nechápeme o tom, jak funguje.

Chtěl bych hlubší vědecké poznání inteligence. Ale abychom umělou inteligenci pochopili, je užitečné zasadit ji do historického kontextu biologické inteligence.
Příběh lidské inteligence mohl klidně začít tímto malým tvorečkem. Je to poslední společný předek všech obratlovců. Všichni jsme jeho potomky. Žil asi před 500 miliony let. Pak evoluce pokračovala a vytvořila mozek, který zase během 500 let, od Newtona po Einsteina, vyvinul hlubokou matematiku a fyziku potřebnou k pochopení vesmíru od kvarků po kosmologii. A to vše bez konzultace s ChatGPT.

A pak je tu samozřejmě pokrok posledního desetiletí. Abychom skutečně pochopili, co se právě stalo v oblasti umělé inteligence, musíme spojit fyziku, matematiku, neurovědu, psychologii, informatiku a další obory, abychom vyvinuli novou vědu o inteligenci. Tato věda o inteligenci nám může současně pomoci pochopit biologickou inteligenci a vytvořit lepší umělou inteligenci. A tuto vědu potřebujeme hned, protože inženýrství inteligence značně předstihlo naši schopnost jí porozumět.

Chtěl bych vás provést naší prací v oblasti vědy o inteligenci, která se zabývá pěti kritickými oblastmi, v nichž se může umělá inteligence zlepšit:

- Efektivita dat
- Energetická účinnost
- Překročení evoluce
- Vysvětlitelnost
- Spojení mysli a strojů

Pojďme se postupně věnovat těmto kritickým nedostatkům.

### Efektivita dat: Obrovský apetit umělé inteligence

Umělá inteligence je mnohem náročnější na data než lidé. Například naše jazykové modely nyní trénujeme na řádově bilionech slov. No a kolik slov dostaneme? Pouhých 100 milionů. To je ta malá červená tečka uprostřed. Možná ji ani nevidíte. Přečíst zbytek z jednoho bilionu slov by nám trvalo 24 000 let.
Dobře, teď si možná řeknete, že to není fér. Jistě, umělá inteligence četla 24 000 let ekvivalentních lidským, ale lidé mají za sebou 500 milionů let vývoje mozku obratlovců. Ale má to háček. Celé dědictví evoluce je vám předáno prostřednictvím vaší DNA a vaše DNA má jen asi 700 megabajtů, tedy ekvivalentně 600 milionů slov. Takže kombinovaná informace, kterou získáme učením a evolucí, je mizivá ve srovnání s tím, co získá umělá inteligence. Všichni jste neuvěřitelně efektivní stroje na učení.

Jak tedy překleneme propast mezi AI a lidmi?

Tento problém jsme začali řešit tím, že jsme se vrátili ke slavným zákonům škálování. Zde je příklad škálovacího zákona, kde chyba klesá podle mocninného zákona s množstvím trénovacích dat. Tyto škálovací zákony zaujaly představivost průmyslu a motivovaly významné společenské investice do energie, výpočetní techniky a sběru dat.

Je tu však problém. Exponenty těchto škálovacích zákonů jsou malé. Takže abyste o něco snížili chybu, budete možná potřebovat desetinásobek množství trénovacích dat. To je dlouhodobě neudržitelné, a i když to krátkodobě vede ke zlepšení, musí existovat lepší způsob.

Vyvinuli jsme teorii, která vysvětluje, proč jsou tyto zákony škálování tak špatné. Základní myšlenka spočívá v tom, že velké náhodné soubory dat jsou neuvěřitelně redundantní. Pokud již máte miliardy datových bodů, další datový bod vám neřekne mnoho nového. Ale co kdybyste mohli vytvořit neredundantní soubor dat, kde by každý datový bod byl pečlivě vybrán tak, aby vám ve srovnání se všemi ostatními datovými body řekl něco nového?
Vyvinuli jsme teorii a algoritmy, které to umožňují. Teoreticky jsme předpověděli a experimentálně ověřili, že tyto špatné mocninné zákony můžeme ohnout na mnohem lepší exponenciály, kde přidáním několika dalších datových bodů můžete snížit svou chybu, a ne desetinásobně zvětšit množství dat.

Jakou teorii jsme tedy použili, abychom dosáhli tohoto výsledku? Použili jsme myšlenky ze statistické fyziky a toto jsou rovnice. Po zbytek celé této přednášky budu tyto rovnice postupně probírat. Myslíte si, že si dělám legraci? A vysvětlím vám je.

Dobře, máte pravdu. Dělám si legraci. Nejsem tak zlý, ale měli jste vidět obličeje organizátorů TEDu, když jsem řekl, že to udělám.

### Reimagining [Machine Learning](/ai/strojove-uceni-machine-learning/)

Pojďme si to trochu přiblížit a zamyslet se obecněji nad tím, co je potřeba udělat, aby umělá inteligence nebyla tak náročná na data. Představte si, že bychom naše děti trénovali stejným způsobem, jakým předtrénujeme naše velké jazykové modely, tedy pomocí predikce dalšího slova. Takže bych svému dítěti dal náhodný kus internetu a řekl: Mimochodem, tohle je další slovo. Dal bych mu další náhodný kus internetu a řekl, ano, tohle je další slovo. Kdybychom dělali jen tohle, trvalo by našim dětem 24 000 let, než by se naučily něco užitečného.

Ale my děláme mnohem víc. Když například učím svého syna matematiku, učím ho algoritmus potřebný k vyřešení úlohy. Pak dokáže okamžitě řešit nové problémy a zobecňovat s použitím mnohem méně tréninkových dat, než by zvládl jakýkoli systém umělé inteligence. Nepředkládám mu miliony matematických úloh.

Abychom umělou inteligenci skutečně zefektivnili z hlediska dat, musíme jít daleko za hranice našich současných tréninkových algoritmů a přeměnit [strojové učení](/ai/strojove-uceni-machine-learning/) na novou vědu o strojovém učení. A tady nám opravdu může pomoci neurověda, psychologie a matematika.

### Energetická účinnost: 20wattový mozek vs. umělá inteligence

Přejděme k dalšímu velkému rozdílu, k energetické účinnosti. Naše mozky jsou neuvěřitelně efektivní. Spotřebováváme pouze 20 wattů energie. Pro srovnání, naše staré žárovky měly příkon 100 wattů. Všichni jsme tedy doslova slabší než žárovky.

Ale co umělá inteligence? Trénování velkého modelu může spotřebovat až 10 milionů wattů a mluví se o jaderné energetice pro datová centra s výkonem 1 miliardy wattů.

Proč je tedy umělá inteligence o tolik náročnější na energii než mozek? Inu, na vině je samotná volba digitálního výpočtu, kdy se spoléháme na rychlé a spolehlivé převracení bitů v každém mezikroku výpočtu. Nyní termodynamické zákony vyžadují, aby každé rychlé a spolehlivé přehození bitů spotřebovalo hodně energie.

Biologie se vydala zcela jinou cestou. Biologie počítá správnou odpověď právě včas pomocí mezikroků, které jsou co nejpomalejší a nejnespolehlivější. Biologie v podstatě netočí svůj motor více, než je nutné.
Kromě toho biologie mnohem lépe přizpůsobuje výpočet fyzikálním zákonům. Vezměme si například sčítání. Naše počítače sčítají pomocí opravdu složitých, energeticky náročných tranzistorových obvodů, ale neurony prostě přímo sčítají svá vstupní napětí, protože Maxwellovy zákony elektromagnetismu již vědí, jak sčítat napětí. Biologie v podstatě přizpůsobuje své výpočty přirozené fyzice vesmíru.

Abychom tedy skutečně vytvořili energeticky úspornější umělou inteligenci, musíme přehodnotit celý náš technologický zásobník od elektronů po algoritmy a lépe sladit výpočetní dynamiku s fyzikální dynamikou. Jaké jsou například základní limity rychlosti a přesnosti jakéhokoli daného výpočtu vzhledem k energetickému rozpočtu? A jaké druhy elektrochemických počítačů mohou těchto základních limitů dosáhnout?

Nedávno jsme tento problém vyřešili pro výpočet snímání, což je něco, co musí dělat každý neuron. Podařilo se nám najít základní dolní meze nebo dolní limity chyby jako funkce energetického rozpočtu, to je ta červená křivka. A podařilo se nám najít chemické počítače, které těchto mezí dosahují. A pozoruhodné je, že se velmi podobaly receptorům spřaženým s G-proteiny, které každý neuron používá k vnímání vnějších signálů. To tedy naznačuje, že biologie může dosáhnout takové účinnosti, která se blíží základním limitům stanoveným samotnými fyzikálními zákony.

Neurověda nám nyní dává možnost měřit nejen nervovou aktivitu, ale také spotřebu energie například v celém mozku mouchy. Spotřeba energie se měří pomocí spotřeby ATP, což je palivo, chemické palivo, které pohání všechny neurony.


Nyní mi dovolte položit vám otázku. Řekněme, že v určité oblasti mozku se zvýší nervová aktivita. Stoupá nebo klesá množství ATP? Přirozený odhad by byl, že ATP klesá, protože nervová aktivita stojí energii, takže musí spotřebovávat palivo. My jsme zjistili přesný opak. Když nervová aktivita stoupá, ATP stoupá a zůstává zvýšená právě tak dlouho, aby mohla pohánět očekávanou budoucí nervovou aktivitu. To naznačuje, že mozek se řídí principem prediktivní alokace energie, kdy dokáže předvídat, kolik energie je kde a kdy potřeba, a dodává správné množství energie na správné místo po správnou dobu.

Je tedy zřejmé, že se máme co učit z fyziky, neurovědy a biologie, abychom mohli vytvořit energeticky účinnější systémy umělé inteligence.

Nemusíme se nechat omezovat evolucí. Můžeme jít nad rámec evoluce a kooptovat neuronové algoritmy objevené evolucí, ale implementovat je do kvantového hardwaru, na který evoluce nikdy nepřijde. Můžeme například nahradit neurony atomy. Různé stavy vypalování neuronů odpovídají různým elektronickým stavům atomů a synapse můžeme nahradit fotony. Stejně jako synapse umožňují komunikaci dvou neuronů, fotony umožňují komunikaci dvou atomů prostřednictvím emise a absorpce fotonů.

Co z toho můžeme vytvořit? Z atomů a fotonů můžeme vytvořit kvantovou asociativní paměť. Jedná se o stejný paměťový systém, který Johnu Hopfieldovi vynesl nedávnou Nobelovu cenu za fyziku, tentokrát se však jedná o kvantově mechanický systém sestavený z atomů a fotonů, a my můžeme analyzovat jeho výkonnost a ukázat, že kvantová dynamika přináší zvýšenou kapacitu paměti, robustnost a zapamatování.

Můžeme také vytvořit nové typy kvantových optimalizátorů postavených přímo z fotonů a můžeme analyzovat jejich energetickou krajinu a vysvětlit, jak řeší optimalizační problémy zásadně novým způsobem. Toto spojení neuronových algoritmů a kvantového hardwaru otevírá zcela novou oblast, kterou bych rád nazval kvantové neuromorfní výpočty.

### Využití vysvětlitelné umělé inteligence k pochopení mozku

Vraťme se k mozku, kde nám vysvětlitelná umělá inteligence může pomoci pochopit, jak funguje. Umělá inteligence nám umožňuje vytvářet neuvěřitelně přesné, ale složité modely mozku. Kam to všechno směřuje? Nahrazujeme prostě něco, čemu nerozumíme, mozek, něčím jiným, čemu nerozumíme, naším složitým modelem? Jako vědci bychom chtěli mít konceptuální porozumění tomu, jak mozek funguje, ne jen to, že nám tento model někdo předá.

Rád bych vám uvedl příklad naší práce v oblasti vysvětlitelné umělé inteligence aplikované na sítnici. Sítnice je vícevrstvý obvod fotoreceptorů, které jdou ke skrytým neuronům, jež jdou k výstupním neuronům. Jak to funguje? Nedávno jsme vytvořili nejpřesnější model sítnice na světě. Dokázal reprodukovat dvě desetiletí experimentů se sítnicí. To je fantastické. Máme digitální dvojče sítnice, ale jak toto dvojče funguje? Proč je navrženo tak, jak je?
Abych tyto otázky konkretizoval, rád bych probral jen jeden z experimentů, z těch dvou desetiletí experimentů, o kterých jsem se zmínil. Chtěl bych, abyste všichni, a tento experiment na vás provedeme právě teď. Chtěl bych, abyste se zaměřili na mou ruku a sledovali ji. Uděláme to ještě jednou. Možná jste byli mírně překvapeni, když moje ruka změnila směr, a měli byste být překvapeni, protože moje ruka právě porušila první Newtonův pohybový zákon, který říká, že předměty, které jsou v pohybu, mají tendenci zůstat v pohybu.

Kde ve vašem mozku se porušení prvního Newtonova zákona objevilo jako první? Odpověď je pozoruhodná. Je to ve vaší sítnici. Ve vaší sítnici jsou neurony, které se spustí pouze a jedině v případě, že je porušen první Newtonův zákon. Dělá to tedy náš model? Ano, dělá to. Reprodukuje ho. Ale teď je tu hádanka. Jak to model dělá?

Vyvinuli jsme metody, vysvětlitelné metody umělé inteligence, abychom mohli vzít jakýkoli podnět, který způsobí, že neuron začne hořet, a vyčlenili jsme základní podokruh odpovědný za toto hoření a vysvětlili, jak funguje. To se nám podařilo nejen u porušení prvního Newtonova zákona, ale i u dvou desetiletí experimentů, které náš model reprodukoval.


Tím se otevírá nová cesta k urychlení objevů v neurovědách pomocí umělé inteligence. V podstatě jde o to vytvořit digitální dvojčata mozku a pak pomocí vysvětlitelné AI pochopit, jak fungují. Ve Stanfordu se právě zabýváme velkým úsilím o vytvoření digitálního dvojčete celého zrakového systému primátů a vysvětlení jeho fungování.

### Spojení mysli a strojů

Můžeme jít ještě dál a využít naše digitální dvojčata ke splynutí myslí a strojů tím, že mezi nimi umožníme obousměrnou komunikaci. Představte si scénář, kdy máte mozek, pořídíte z něj záznam, sestavíte digitální dvojče a pak se pomocí teorie řízení naučíte vzorce nervové aktivity, které můžete zapsat přímo do digitálního dvojčete a ovládat ho. Pak vezmete tytéž vzory nervové aktivity a zapíšete je do mozku, abyste ho mohli ovládat. V podstatě se můžeme naučit jazyk mozku a pak s ním přímo mluvit.

Nedávno jsme tento program realizovali na myších, kde jsme mohli pomocí umělé inteligence číst myšlenky myši. V horním řádku vidíte obrázky, které jsme myši skutečně ukázali. A ve spodní řadě vidíte obrázky, které jsme dekódovali z mozku myši. Naše dekódované obrázky mají nižší rozlišení než skutečné obrázky, ale ne proto, že by naše dekodéry byly špatné. Je to proto, že vizuální rozlišení myši je špatné. Takže dekódované obrázky vám vlastně ukazují, jak by svět ve skutečnosti vypadal, kdybyste byli myší.

Nyní můžeme jít dál. Nyní můžeme do mozku myši zapsat vzorce nervové aktivity, takže ji můžeme přimět k halucinaci jakéhokoli konkrétního vjemu, který bychom chtěli, aby halucinovala. A jsme v tom tak dobří, že ji dokážeme spolehlivě přimět k halucinaci vjemu tím, že ovládáme pouze 20 neuronů v myším mozku, a to tak, že zjistíme, kterých 20 neuronů je třeba ovládat. V podstatě můžeme přímo řídit to, co myš vidí, tím, že do jejího mozku zapíšeme.
Možnosti obousměrné komunikace mezi mozkem a stroji jsou neomezené, aby bylo možné mozek pochopit, léčit a rozšířit.

### Jednotná věda o inteligenci

Doufám, že pochopíte, že snaha o jednotnou vědu o inteligenci, která zahrnuje mozky a stroje, nám může pomoci jak lépe pochopit biologickou inteligenci, tak vytvořit efektivnější, vysvětlitelnější a výkonnější umělou inteligenci. Je však důležité, aby toto úsilí probíhalo otevřeně, aby se o tuto vědu mohl podělit celý svět, a musí probíhat ve velmi dlouhém časovém horizontu.

Díky tomu je akademická sféra ideálním místem, kde se vědě o inteligenci věnovat. V akademické sféře jsme osvobozeni od tyranie čtvrtletních výkazů zisků. Jsme osvobozeni od cenzury právních oddělení firem. Můžeme být mnohem interdisciplinárnější než kterákoli společnost a naším samotným posláním je sdílet se světem to, co se naučíme.

Ze všech těchto důvodů vlastně budujeme na Stanfordu nové centrum pro vědu o inteligenci. Zatímco v průmyslu došlo k neuvěřitelným pokrokům v oblasti inženýrství inteligence, které se nyní stále častěji odehrávají za zavřenými dveřmi, jsem velmi nadšený z toho, čeho může věda o inteligenci dosáhnout na otevřeném prostranství.

V minulém století spočívalo jedno z největších intelektuálních dobrodružství v tom, že lidstvo nahlíželo do vesmíru, aby mu porozumělo, od kvarků po kosmologii. Myslím, že jedno z největších intelektuálních dobrodružství tohoto století bude spočívat v tom, že lidstvo bude nahlížet dovnitř, a to jak do sebe, tak do umělé inteligence, kterou vytvoříme, abychom dosáhli hlubšího, nového vědeckého pochopení inteligence.

Děkuji.