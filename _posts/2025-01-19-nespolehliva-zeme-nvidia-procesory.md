---
title: "Moderní AI procesory v Česku nebudou. Proč nás USA označily za nespolehlivé?"
author: Patrick Zandl
post_excerpt: "Americká administrativa nás nově zařadila mezi nespolehlivé státy, kterým američtí výrobci dodají jen přísně omezené množství hitech procesorů. Proč nebudeme dostávat skutečně výkonné AI procesory? Fialova vláda nezvládla situaci s jejich pašováním přes české firmy do nepřátelských států a přes četné varování nechala firmám volnou ruku..."
layout: post
categories: [Čína, AI, USA, Nvidia]
thumbnail: https://www.marigold.cz/assets/fiala-ai-nvidia.png
audio_url: 
---



Americká administrativa nově rozdělila státy mezi ty přátelské, jimž bude dodávat AI procesory, ty nepřátelské, jimž  je dodávat nebude a pak ty ostatní, neformálně nazývané nespolehlivé. Česká republika spadla mezi ty nespolehlivé, kterým američtí výrobci dodají jen přísně omezené množství. Skutečně výkonné AI procesory prakticky dostávat nebudeme. Proč? Fialova vláda nezvládla situaci s pašováním hitech procesorů přes české firmy do nepřátelských států a přes četné varování nechala firmám volnou ruku. 

A u tohoto problému se vyplatí zastavit. 

Na dodávky hi-tech technologií do nepřátelských regionů v USA funguje embargo již delší dobu a USA hledají možnosti, jak zpřísňovat podmínky a komplikovat Číně a Rusku technologické soupeření. Zákaz vývozu špičkových AI procesorů se masivně obcházel řetězem nákupů i krádeží, zhusta fingovaných. To je také důvod, proč se nikdo (krom těch, kdo mají vlastní serverovny) nechlubí tím, kolik Nvidia procesorů má. Nechce o ně přijít. 

Nvidia má zavedenou plnou trasovatelnost všech procesorů podle výrobního čísla. Ví, komu co prodává a kontroluje si, zda u něj technologie také skončila. V létě do Česka dorazil bezpečnostní tým Nvidia včetně jednoho z nejvyšších šéfů společnosti. V serverovně, která měla být po strop naplněná Nvidia DGX H100,  po AI procesorech nebylo ani památky...

Fakt, že se přes české společnosti a postsovětské republiky masivně na ruský a čínský trh dostávají embargované procesory, se nedal přehlédnout. Navíc Česká republika nebyla schopna (či ochotna) poskytnout součinnost a začít tyto díry uzavírat. Zatímco v Německu nebo Holandsku by se taková firma okamžitě dostala do přímých problémů s finančním úřadem za obcházení sankcí, v Česku v této oblasti panuje naprostá laxnost. 

USA reagovaly tak, jak musely. Země, které nespolupracují na tom, aby se špičkové technologie nedostaly do rukou, kam se podle USA dostávat nesmějí, o tyto technologie přijdou. Což se stalo Česku. Českým firmám nikdo nebude smět dodávat pokročilé AI čipy nad určitý (a poměrně nízký) limit. Na tuto skutečnost jsme byli několikrát upozorněni a pro změnu situace se neudělalo mnoho. 

Seznam Zprávy k situaci [vydaly rozhovor s Jiřím Házem z  Českého národního polovodičového klastru](https://www.seznamzpravy.cz/clanek/ekonomika-omezeni-vyvozu-cipu-z-usa-nedava-smysl-rika-cesky-cipovy-vedec-268169). Rozhovor je pro mne těžko dešifrovatelný. Jiří Háze je  člověk s výborným přehledem, takže si musí být vědom toho, že většina informací, které ve článku říká, zkrátka neodpovídají realitě. Česko dnes špičkové AI čipy prakticky nepoužívá. Výjimkou je Seznam a pár akademických pracovišť, kde ale zpravidla mají ty levnější a neembargované verze. Špičkovými čipy se nemyslí Nvidia Jetson, ale embargem dotčené H100 nebo A100, těch je v Česku pár a klidně bych se vsadil, že patřím se svou serverovou sestavou mezi největší provozovatele. 

Držet si přehled je snadné. V Česku mimo jiné ani neseženete lidi, kteří mají zkušenosti s těmito systémy, který umí řešit jejich správu a umí rutinně používat ekosystém CUDA používaný pro práci s AI a těch pár lidí, co tomu rozumí se zná a dělá prakticky pro každého v oboru. To opět odpovídá tomu, jak málo je AI v Česku běžná technologie z pohledu vývojáře. Pokud jste firma, která má dnes potřebu zajistit si kapacitu na trénink či fine-tuning svých služeb, jste v podstatě odkázáni na  nákup strojového výkonu v zahraničí. 

Česko v současné době nemá žádný špičkový AI výzkum, o kterém mluví Háze. Meteorologický model ČHMU, o kterém je řeč, utáhne „pár GPU“, které navíc ČHMU již má. Další rozvoj? Jaký? Používání meteorologického nástroje Google? Ten poběží v Google cloudu...

### Žádná vládní AI strategie

Neexistuje žádná vládní strategie ani žádná „vládní poptávka“. Zatímco v USA či v Číně se velmi jasně v jednotlivých kruzích říká, co se od AI očekává a jednotlivé instituce se podle toho chovají, v Česku máme na ČVUT Český institut informatiky, robotiky a kybernetiky (CIIRC), ale pokud si chcete udělat představu o tom, kde je český akademický a polo-komerční AI výzkum, projděte si [nositele loňské AI Awards](https://www.ciirc.cvut.cz/cs/ai-award-za-vyzkum-a-vyvoj-pro-josefa-sivice/). Tohle má být to top, co u nás existuje? Že ale žádná vládní strategie pro AI není, není zase tak podstatný problém: máme například strategii pro digitalizaci, ale vlastně všichni se smířili s tím, že ji neplníme a to, co plníme, jsou jen takové ty formální body, které by se staly tak jako tak... 

Děsivý je příběh Tomáše Mikolova, autora Word2vec a nejcitovanějšího českého odborníka na AI ve vědeckých pracích. Člověk jeho renomé pět let pobíhá po Česku a shání financování týmu při CIIRC: „Když jsem se v roce 2019 vracel do Česka, tak se tu hodně mluvilo o tom, jak je AI priorita, jak musíme dohnat svět. Teď je rok 2025, a stále to jsou jen ty stejné kecy, nic moc se nezměnilo. Peníze do výzkumu se investují naprosto nesmyslně nebo končí kdovíkde,“ říká v rozhovoru pro Wired. Jestli jste dneska ještě neměli depku, [rozhovor si přečtěte](https://www.wired.cz/clanky/k-lepsi-vede-v-cesku-by-mohly-pomoci-i-pohadky-svejkovani-tu-nevydrzi-vecne), garantuju vám ji. 
 
Je třeba říct si to na rovinu: AI v Česku nemá zatím žádnou perspektivu. Jakýkoliv základní výzkum tu táhnou nadšenci, jenže doba, kdy stačilo nadšení, je dávno pryč. Teď už jsou potřeba i tvrdé peníze. Jenže ty se v Česku ztrácí na nesmyslných projektech, které na sebe nenavazují, nemají žádné napojení na sebe a už vůbec ne výhled na aplikaci do praxe. Akademický výzkum AI z největší části slouží k tomu, aby se na pracovištích udržel status quo, aby podfinancování vysokoškolští pracovníci dostali aspoň nějaké peníze a vykázala se činnost. S výsledky se příliš nepočítá. Pokud bychom ho celý škrtli, nestalo by se prakticky nic zásadního pro výzkum jako takový. 

Nejlepší výzkum AI zbraňových systémů v české armádě dělají dva mladíci a financování probíhá tak, že jejich šéf zavírá oči nad tím, že dělají něco jiného, než na co je oficiálně najal a umí odepsat sešrotovaný dron. Jenže tohle není výzkum v country for the future. 

Co to znamená? Že český výzkum AI tak, jak běží, nedává žádný smysl. A tudíž jej ani nedostatek procesorů nemůže ohrozit. Vláda premiéra Fialy nezvládla nastartovat reformu univerzitního výzkumu a jeho převod do praxe v nejdůležitějším oboru, jaký dnes existuje -  jak je to v jiných oborech nevím, tam to nesleduji. Selhala v oblasti, kde měla mít nejbližší expertízu, neboť premiér Fiala z univerzitního prostředí pochází. 

Proto Házeho vyjádření v rozhovoru vůbec nechápu. Například, když říká, že si neumí představit, jak by se USA podařilo zabránit tomu, aby se čipy nedostaly na nežádoucí trhy. To je přeci naprosto jasné: USA/Nvidia prostě odříznou kohokoliv, jemuž jsou prodány procesory, které skončí na zakázaném trhu. A to je přesně to, co se stalo Česku. Blackwell procesory nekoupíte anonymně na krámě, je zcela zřetelné, kdo je koupil a dá se zjistit, kam je dodal. Není to o žádné kontrole kamionů. Těch věcí si musí být vědom. Zjevně se jen snaží nepodrazit Fialu a počítá s tím, že je vlastně úplně jedno, co v takovém rozhovoru říká, protože upřímnost nemá šanci nic změnit. 

Má vůbec něco šanci změnit české technologické zaostávání? 

Z věcí, které lze předpokládat, nic (nepočítám, že tu přistanou ufoni a věnují nám hyperprostorový pohon - to je jen zápletka knihy Flotila Země). Úspěchem v AI by nezískal výhodu nikdo z těch, na nichž politicky záleží - nikdo ze současných činitelů SPOLU nebo ANO není v AI (a ani v pokročilých technologiích) zainteresován. Možná by byla situace jiná, kdyby své politické příklony oficiálně vyhlásili čeští technologičtí miliardáři, většina z nich má ale jiné starosti. A tak se propadáme zpět k vzývání uhelných elektráren, mamutích jaderných projektů a spalování mrtvých dinosaurů.