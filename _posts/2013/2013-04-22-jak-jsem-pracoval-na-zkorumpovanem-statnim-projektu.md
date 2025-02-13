---
ID: 2648
author: Patrick Zandl
categories:
- Politika
- Korupce
layout: post
oldlink: 'https://www.marigold.cz/item/jak-jsem-pracoval-na-zkorumpovanem-statnim-projektu

  '
post_date: 2013-04-22 13:34:28
post_excerpt: ''
published: true
summary_points:
- Státní IT projekty jsou komplexní kvůli zátěži, škálování a státní infrastruktuře.
- Ochrana dat a propojení s registry zvyšují náročnost státních IT systémů.
- Vstup a výstup dat z různých systémů komplikuje státní IT projekty.
- Analýza státních IT projektů vyžaduje rozsáhlou dokumentaci a zkušenosti.
title: 'Jak jsem pracoval na zkorumpovaném státním projektu

  '
---

<p>Nadpis přehání, ale je to úkol nadpisů, nalákat na něco, co není až tak pravda. Chtěl jsem vysvětlit, proč mám mírný odstup od současného obecného dojmu, že co stát dělá, dělá z korupčního důvodu, ačkoliv nevylučuji, že je to tak v netriviálním množství případů.</p>

<p>Zkušenost je nedávná - loňská. Oslovil mne kamarád pracující na ministerstvu, zda bych jim nepomohl podívat se na potenciální problémy u jednoho IT projektu (nekonkrétní jsem, jistě chápete, záměrně). Zjistit, zda je někde neodírá dodavatel a kde je co špatně, pokud je něco špatně. Rozměrově bych řekl, že to byl projekt na úrovni Registru jízdních kol. Když nad tím tak od stolu přemýšlíte, jde o věc tak za pár desítek tisíc: formulář, kde se data vkládají, jiný, kde se vyhledávají, k tomu trocha omáčky okolo. Za dvě odpoledne to má programátor, za další víkend grafik a můžeme vyjet. Asi takhle jsem k tomu ze začátku přistupoval a když jsem se dozvěděl, že aplikace stojí miliony, omývalo mne. I se vší marží a ambaláží okolo může jít maximálně o statisíce, říkal jsem si.</p>


<p>Pak jsem se ponořil do smluv a požadavků. Za prvé řešení už od počátku počítalo s určitou zátěží, takže bylo třeba loadbalancovat, škálovat, nemalou položku dělaly požadavky státní infrastruktury (tady bych řekl, že systémově předražené služby České pošty jsou jedním z podkladových problémů). Dobře, ani s tím by to nemuselo stát dvacku.</p>

<p>Další problémy byly v tom, co si většinou neumíme od stolu představit. Státní řešení požaduje určité úrovně ochrany dat a propojení. Například položka propojení na Centrální registr obyvatel (CRO), díky čemuž se postupně změny adres trvalého bydliště samy aktualizují v rejstřících. A díky čemuž služba občas dává smysl. A ochrana dat? Státní správa má určitou hierarchii, kdo k datům může přistupovat a kdo je může i měnit. To kvůli kontrole, aby nemohl nějaký nízko pověřený úředník vyčmuchat vaše data a prodat je dál. Svou nevýhodu to má, když se to špatně vymyslí a udělá, tak obsluhující personál nemá oprávnění získat nějaké vaše potvrzení a nasírá vás tím, že tam máte dorazit. Vše se musí logovat, evidovat a v relativně reálném čase ověřovat, takže další komplikace, ale ve výsledku se dá systém obstojně nastavit tak, aby zachovával anonymitu i v relativně citlivých otázkách (tím ale registr kol není, tento případ ovšem byl).</p>

<p>Lahůdkou je také vstup dat. Ve většině státní agendy již existují nějaká pořízená data a je třeba je do systému dostat. Často jsou v různých systémech a formátech, z části papírově, z části digitálně. Část dat se pořizuje při jiném úředním úkonu jiným systémem, jehož výstup nelze momentálně upravit, takže se musí udělat dlouhodobě fungující a podporovaný konverzní filtr. Například si představte, že při namátkové kontrole cyklistů bude policista opisovat sériové číslo kola a údaje o majiteli do stávající aplikace (a někde ji nemají, tak do formulářů). Prostě bordel. My jsme napočítali zhruba dvacítku vstupních zdrojů dat, z nichž nejvíce mi hnulo žlučí nějaké Wordové makro. Když jsem se pídil po tom, zda by KURVA NEŠLO, že by ta data nějkdo místo do formuláře ve Wordu přepsal do formuláře na webu, tak se ukázalo, že Word obsluhuje stará paní dva roky před důchodem a je levnější udělat konverzní filtr, než ji řešit, vysvětlovat, dávat odstupné atd. A protože mzdové náklady jsou oddělenou kapitolou rozpočtu, bylo to opravdu těžko řešitelné, musela by to projednat řada lidí, jejichž čas/nervy byly nakonec opravdu dražší a nikomu se s tím nechtělo kvůli těm pár desetitisícům patlat.</p>

<p>To samé s výstupem dat. Řada vnitrostátních informačních systémů používá komplexní XML formát, v němž se data dají vyměňovat komforntě, ale řada starých systémů dožívá v datech obtížně či vůbec nestrukturovaných či dokonce stále papírových. To vše bylo třeba projít, analyzovat, co se změnou stane a podle toho vytvořit množinu výstupních dat.</p>

<p>Poslední bod, u kterého se zastavím, je analýza. Zatímco v případě Registru jízdních kol pro běžné uživatele na webu by analýza byla tak na půl stránky A4 a obsahovala šestiobrazovkový wireframe, v tomhle případě bylo potřeba zmapovat stávající použití systém, co se od něj očekává, kudy do něj data proudí a kudy mají lézt ven, aby se nestalo, že bude odříznut nějaký návazný systém a nebude se vědět, jak toto odříznutí vyřešit. Řešila se přístupová práva, nezapomínejte, že ne každý úředník smí vidět všechno, takže se muselo zamezit tomu, aby se na určitém úkonu muselo podílet více úředníků.</p>

<p>Otázkou analýzy byla i bezpečnost a to nejenom ta běžná "máme to zmáklý, hesla hashujeme se solí", ale i instalace a správa. Je potřeba zajistit, aby při instalaci aplikace nemohlo dojít ke kompromitaci datových úložišť státní správy, se kterými ale systém má komunikovat. Je tedy třeba "instalatéra" odstínit, sandboxovat, používat testovací prostředí, zkrátka vymyslet, co s tím, aby dodavatel předal práci, tu odběratel rozchodil a bylo jasné a viditelné, čí chyba je, že nechodí, co chodit mělo a zároveň nebyla dotčena bezpečnost. A aby se nějak inteligentně řešila budoucí správa ve vztahu k bezpečnosti a ekonomice provozu, tedy aby to vždycky nemělo svůj samostatný fyzický hardware.</p>

<p>Když jsme to sečetli, měla dokumentace k celé věci zhruba stovku stran, dodatečné podklady k formátům další dvě stovky. Jen analýza zabrala stovky hodin. Uřídit ji, aby k něčemu směřovala, chtělo pořádný nervy a zkušenosti. Mimochodem, zakázku zajišťovala taková ta dobře znějící a známá firma, velkou část vývoje ovšem dělaly outsourcované firmy. Když jsem štoural do toho, proč, tak se ukázalo, že to byla právě ta analýza - menší firmy neměly prostě zkušenosti na to, aby celou věc probraly a prošťouraly ze všech stran a aby se podchytily záležitosti, které u ne-státních zakázek člověka nenapadnou a nejsou. Firma si to logicky nechala zaplatit za slušné peníze, na druhou stranu oprávněně.</p>

<p>Rozuzlení? Zajímavé v tom, že si většinou neumíme bez předchozích zkušeností představit, co všechno obnáší a jak je rozsáhlá státní zakázka, která vypadá, jako prcek. To byl první poznatek. Druhý poznatek byl, že dnes se státní zakázky většinou soutěží a problém vzniká při kontrole jejich průběhu. Není tu příliš velký tlak na hodinovou cenu, pokud se pohybuje v obvyklých mantinelech, potíže jsou ale s víceprácemi - v tomhle projektu se řada peněz ušetřila tím, že se vyškrtaly věci, které se podle dodavatele realizovat měly, ve skutečnosti ale nebyly zásadně (či vůbec) potřeba.</p>

<p>Navíc se státní projekty pojímají velmi komplexně. V běžném IT (a zejména na webu) panuje taktika "fast start, fast fail", kdy se vypustí něco, co má základní obslužnost a další věci se dodělávají postupně. Ve státní IT je dopředu stanoven značně komplexní systém, který se musí vytvořit a až časem se ukáže, že i velké části z něj nakonec bude třeba předělávat (a to už nebývá možné), nebo nebyly vůbec potřeba. To je problém monstrózních software, na které přispívá EU a kde panuje dojem (zřejmě daný grantovými kritérii), že se musí vymyslet všechno, protože později už se do toho nesáhne. Jenže málokdo ve státní správě je schopen takovou záležitost navrhnout a uhlídat (a to za běžného provozu). Hrdě jsme zrušili ministerstvo informatiky, které se o takovéhle věci snažilo, takže jsme to dnes převedli na soukromé subjekty, ale jejich zájmy jsou poněkud jiné, ty hlavně hájí své příjmy a kůži. Proto tolik problémů s dalšími víceprácemi.</p>

<p>Asi největší problém tedy byl v tom, že úřady zřejmě běžně nemají k dispozici lidi se zkušenostmi z větších IT zakázek a takové lidi si vlastně najímají, jenže v té pozici, kdy sedí na druhé straně - u dodavatele - a starají se o to, jestli to, co bude dodáno, bude obhajitelné vůči smlouvě.</p>

<p>Samotný projekt prošuměl bez zájmu, šlo také spíše o interní systém než o frontend mezi státem a občanem. I tak se dva novináři (co jsem zaznamenal) neopomněli otřít se o další ministerskou malou domů, aniž by k tomu měli více důkazů, než jen svůj osobní dojem. Nakonec jsem největší finanční problém způsobil asi já, když jsem odmítl honorář (on na něj taky v rozpočtu nebyl žádný velký prostor), jenže se mnou byla sepsána smlouva a ta honorář předpokládala, jinak bych nemohl mít přístup k podkladům. A nemohl jsem účtovat konzultace za 100Kč/hodina, protože to by tlouklo do očí s běžnou smluvní cenou konzultací. Takže jsem vyúčtoval dvě hodiny po osmnácti stovkách a přiživil se tak na státní zakázce (koupil jsem si za to tehdy, jestli se dobře pamatuji, jednu pneumatiku - tři další už šly z plateb privátního sektoru).</p>

<p>V každém případě to byla zajímavá zkušenost, která mě donutila přidat si mezi proklatá slovíčka termíny jako "vícepráce" nebo "normativní" či "řešení obvyklé v místě a čase". Nemyslím, že se ukradne všechno, co proteče státním sektorem. Myslím, že hodně věcí se dělá zbytečně, hodně špatným investičním systémem, hodně bez zkušeností, protože nejsou lidi, kteří by tyhle zkušenosti měli - a ti, co je nyní získají, budou dál dělat svou práci a ty zkušenosti s IT projektem v nejbližší době už nepoužijí. Hodně vadí chybějící nebo degradovaná osobní zodpovědnost ať už za úkoly a někdy i celek.  </p>

<p>Svádět to všechno na korupci, to nejde.</p>