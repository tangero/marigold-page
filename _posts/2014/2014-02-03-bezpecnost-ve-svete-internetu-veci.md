---
ID: 2773
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/bezpecnost-ve-svete-internetu-veci

  '
post_date: 2014-02-03 08:23:08
post_excerpt: ''
published: true
summary_points:
- Internet věcí zvýší efektivitu spotřeby zdrojů při zachování životní úrovně.
- Bezpečnostní hrozby zahrnují kompromitaci dat, útoky na infrastrukturu a prvky sítě.
- Lokální oprávnění a anonymizace dat snižují riziko úniku informací.
- Rostoucí výpočetní výkon zvyšuje potenciál pro sofistikované bezpečnostní hrozby.
title: Bezpečnost ve světě Internetu věcí
---

<p>Už jsem kdysi předesílal, že "Internet věcí" bude podle mého soudu významným intenzifikačním faktorem pro udržení životní úrovně při snížení spotřeby limitovaných zdrojů (tedy snížení spotřeby zdrojů na hlavu). Bude podobnou revolucí ve spotřebě, jako vynález výroby z plastů nebo v Číně. Což má jeden háček. Bezpečnostní.</p>


<p>Internet věcí totiž obnáší počítače připojené do internetu, tedy podléhající všem zákonitostem tohoto prostředí. Včetně nejrůznějších typů útoků. A je dobré na to myslet již předem.</p>


<!--more-->

<p>V zásadě lze uvažovat o třech typech bezpečnostních hrozeb pro Internet věcí:</p>

<ul>
<li><strong>kompromitace dat</strong>, kdy se osoba nepovolaná dostane k datům, k nimž nemá mít přístup. Typickým příkladem je odchycení přístupového uživatele hesla k webu služby. </li>
<li><strong>útok proti infrastruktuře</strong>, kdy se někdo pokusí útokem na slabá místa složité infrastruktury vybudit její kolaps či převzít nad ní kontrolu. Příkladem může být DoS útok vůči infrastruktuře sítě. </li>
<li><strong>útok proti prvku</strong>, kdy se průnikem do chytrého prvku sítě někdo pokouší změnit fungování prvku sítě a využít jej k činnostem, pro něž nebyl určen. Příkladem může být úspěšná instalace bootnetu do prvků sítě.</li>
</ul>
<h3>Kompromitace dat</h3>
<p>Vcelku zmapovaná je část bezpečnostních hrozeb souvisejících s kompromitací dat, ke které také vlastně patří přístup k různým servisním a ladícím stránkám infrastrukturní částě onoho "internetu věcí". Na to, abyste donutili udělat chytré krokoměry, co potřebujete, nemusíte jeden po druhém složitě hackovat přes bluetooth, ale "stačí" se prolomit do servisního rozhraní služby a například podstrčit k update váš vlastní firmware. Právě tenhle bezpečnostní prvek se zatím řeší zhusta netriviálněji tím, že aktualizace firmware nelze z pohledu provozovatele služby servisovat (připravovat k distribuci) přes web rozhraní, ale přes co nejotřesnější rozhraní, například z příkazové řádky. Situace je tady podobná, jako u cloudu (jenž ostatně hodně za IoT stojí v pozadí) - musíte si být jisti, že úpravy, které jako provozovatel distribuujete dále do sítě, jsou ty správné.</p>

<p>Kompromitace dat může mít původ lokální, kdy je prolomena ochrana dat při přenosu na server někde po trase a data jsou odposlechnuta, nebo globální, kdy je kompromitován centrální server či cloud služby a útočník má přístup k těžko zjistitelnému úhrnu dat. Velké profesionální databáze by na tohle pamatovaly a mají celou řadu postupů, které jsou proti těmto rizikům rozumně preventivní či je alespoň zmapují, jenže Internet věcí spíše než na velkých databázích operuje s jinými formami ukládání dat, třeba se soubory - a tam se preventivní audit a monitoring podezřelých scénářů dělají o poznání hůře. Nejsou na to ještě standardizované nástroje, takže často ani nelze říci, jaká data a v jaké míře byla kompromitována.</p>

<p>Uživatele velmi často znervózňují hrozby lokálního úniku dat, kdy je nějak odposlechnuta trasa z uživatelského zařízení do datového cloudu. V případě energomonitoru byste například mohli zkoušet odposlouchávat odesílání dat o spotřebě energií do AWS. A protože odesílací zařízení je velmi jednoduchý osmibitový počítač Arduino, nelze jako dodatečnou vrstvu přidávat nějaké silnější šifrování. Volba silnějšího hardware by zase významně prodražila celé zařízení (nenechte se mýlit, rozdíl pár dolarů v nákupní ceně součástky dělá desítky dolarů v prodejní ceně). Řešení? Data posílat anonymizovaně, takže k jejich uplatnění potřebujete vypátrat jejich původce. A to je často to samé, jako u jeho zařízení rovnou sedět. U energomonitoru sice sada měřených dat putuje nešifrovaná, ale jde o inkrementy, ne celkové hodnoty a ve spojení s interním číslem sběrného zařízení, které není právě jednoduché spárovat s loginem uživatele, data se drží i v cloudu odděleně. Pravda, pro NSA asi drobné zdržení, ale běžný hacker se zapotí, pokud chce zjistit konkrétní spotřebu konkrétního uživatele.</p>

<h4>Koncept místního oprávnění</h4>
<p>Lze si povšimnout, že část bezpečnosti zůstává řešena požadavkem blízkosti. U řady zařízení nelze některé funkce měnit přes webové rozhraní, ale pouze místně. Pokud dotyčné zařízení nemá dostatečné vstupně/výstupní možnosti, děje se ovládání například přes aplikaci v mobilu a bluetooth. Tak se snadno zajistí, že zařízení je blízko tomu, kdo má právo jej ovládat a není třeba řešit rozsáhlejší koncept bezpečnosti přihlášením přes jméno a heslo, výměnu klíčů a další propriety. Takhle se například může řešit bezpečnostní klíč na senzorech vybavených low-power bluetooth či Wmbusem: klíč je prostě na senzoru a kdo chce, si jej přečte a zadá do svého zařízení. Je na majiteli senzoru, aby zařízení nikomu nepovolanému nedával a je to věc fyzického zabezpečení přístupu k zařízení. Tahle koncepce však má svou slabinu: jen málokteré zařízení vám dnes umožní zjistit, která zařízení klíč mají a přítup používají a můžete mít i problémy klíč změnit.</p>

<p>Jen tak pro představu, co se může stát: fitness sledovače FitBit mají režim tichého buzení, když se rozvibrují. Tiché buzení lze nastavit lokálně přes mobil, ale také na dálku přes web a typický otravný hack nastaví a distribuuje všem uživatelům Fitbitu buzení v nějakou velmi nepříjemnou hodinu. Zatím se tak nestalo - zřejmě i proto, že takové hromadné scénáře si Fitbit infrastruktura kontroluje. Tím se dostáváme k další nutné proprietě infrastruktury Internetu věcí: vnitřní bezpečnostní rutiny, které pravidelně vyhodnocují, zda se neděje něco divného, například zda si milion uživatelů vibračního náramku nenastavuje buzení ve stejný čas na stejný čas...</p>

<h3>Útok proti infrastruktuře</h3>
<p>Masivní útoky typu D/DoS, tedy útoky za účelem "odmítnutí služby" jsou dnes na internetu běžné. Již Bible píše: bušte a bude vám otevřeno. Vydírat provozovatele chytrých měřících krabiček s vlastní IP adresou hrozbou (a demonstrací) hromadného útoku patří mezi součásti dnešní běžné obchodní politiky. Ochrana je podobná, jako kdysi u počítačů. Buďto čekat, až to útočníka přestane bavit, nebo vytvářet a chránit virtuální sítě či využívat dosavadního zabezpečení. Běžné chytré elektroměry v businessu utilit jsou většinou součástí nějaké privátní sítě, do které z venku není přístup, což ale omezuje jejich užití zákazníkem a jakoukoliv jejich přidanou hodnotu nad "online fakturaci". Další řada zařízení to řeší tak, že funguje v rámci PANu, osobní sítě, takže ochranu přebírá za prvé síť nadřazená (zpravidla LAN) nebo samotný fakt obtížného podstrkávání informací do personální sítě. Dobrým příkladem jsou opět ty fitness náramky a gadgety: do sítě se připojují nárazově, zpravidla přes low-power bluetooth profil a jen si přes nadřízené zařízení vymění data s centrálním serverem. Všimněte si, že samotný mobil, přes který si Fitbit nebo Jawbone vyměňuje data, si aktualizaci dat pro mobilní aplikaci bere nikoliv ze zařízení, ale znovu ji stahuje z cloudu. To má své důvody nejenom výkonové, ale i z pohledu bezpečnostní architektury. Zaútočit DOS útokem na gadgety připojené přes PAN prakticky nemá smysl, protože se musíte vypořádat se zpravidla podstatně robustnější ochranou lokální sítě a jejího firewallu. Díky Bohu a opensource hnutí za to, že už i do nejlevnějších routerů se dostaly vcelku obstojné firewally.</p>

<p>Tahle situace se ale změní v momentě, kdy se více začne prosazovat WiFi Direct a další nové rozšířené profily WiFi. Ty umožní jednak nízkorežijní (a málo-baterku-žravý) přenos dat, jednak jednodušší oboustrannou iniciaci přenosu, takže bude možné laborovat s koncepty průniku blízko LAN síti a DoS útoky na gadgety vybavené WiFi Direct. Jsou představitelné bootnety, které zaútočí na cíl v rámci LANu přes WiFi Direct, zatímco u bluetooth je to hodně nepraktické.</p>

<p>DoS útoky na infrastrukturu připojenou přímo do internetové sítě budou asi nejvděčnější a z počátku nejrozšířenější, slibují za nejméně práce nejvíce výsledků a tady záleží hlavně na tom, zda výrobci IoT hraček nezapomenou na tradiční bezpečnostní politiku v sítích a budou ji podporovat. V řadě případů to bohužel vede k nutnosti volby silnějšího (a žravějšího) hardware, než by bylo nutno.</p>

<h3>Útok proti prvku sítě</h3>
<p>Vysokou školou hackování Internet of Things bude útok proti prvku sítě, tedy přímý útok na jednotlivé gadgety. Proč útočit přímo na prvky sítě, to ponechme stranou, motivace bývají různé a mezi sedmi miliardami lidí se pravděpodobně pár motivací najde. Jde o to, jak. Tady se původně zdálo, že situace bude hodně různorodá, protože většina IoT zařízení jsou nějaké jednoprocesorové speciálky. Jenže i tady se situace začíná usazovat a standardizovat, začínají se používat standardizovaná prostředí i systémy, předpřipravená řešení.</p>

<p>Dobře to vidíme v energomonitoru. Naše "klasické" řešení pro sběr naměřených dat je jednoduché Arduino s naším vlastním firmware, do kterého je těžké nabourat se už proto, že nevíte jak a dokumentace není veřejně dostupná. Jestli budete mít dost času, můžete si jedno objednat a experimentovat, abyste rychle zjistili, že firewall na LAN síti, drobná bezpečnostní opatření a 32 KB paměti (proto jsou opatření jen drobná) jsou dost účinnou brzdou pro průnik. Většina dnešních programátorů dnes do 32 KB paměti nenacpe ani "Hello World".</p>

<p>Horší je, když chcete jít za pouhý sběr dat a potřebujete už i robustnější podkladový systém. Psát si ten by bylo poněkud sebevražedné (nebo drahé), takže sáhnete po hotovém. V našem případě Android, velmi často je to též Linux, jenže Android vede, protože má řadu hezky zpracovaných věcí, jako je OTA aktualizace, které si do klasického Linuxu musíte řešit extra (i když jsou komponenty k mání). Ostatně, Android je Linuxu hodně blízko.</p>

<p>Navíc, má-li takové zařízení být otevřené, musí podporovat nějaký standardní systém výměny stavových zpráv. My jsme sáhli po MQTT, chytrém standardu od IBM určeného právě pro komunikaci mezi prvky Internetu věcí. Nic z toho ale neznamená, že bezpečnost máte automaticky zajištěnou, především OTA je potenciálně díra, ale musíte ji mít, protože jinak těžko na dálku aktualizujete zařízení, které potřebujete mít aktuální. Ve výsledku celá věc dopadá tak, že nám pod Android vrstvou běží ještě vlastní vrstva hlídající, zda je vše v pořádku.</p>

<p>Androidí či Linuxové mašinky připojené v rámci PAN nebo LAN budou živnou půdou pro průniky do infrastruktury. Zatím není mnoho známých konceptů, jak do nich pronikat, ale to je jen otázka času, úsilí a tedy "atraktivnosti" zisku z takového průniku. Pesimistické scénáře zatím dost chladí fakt, že domácí routery jsou zpravidla linuxové mašinky podobného typu a průniky do jejich software nejsou (až na tweekování) nijak obvyklé. Kritici ale připomínají, že to má řadu dobrých důvodů, jako jsou nemožnosti dálkové aktualizace, které u krabiček Internetu věcí nejsou dlouhodobě udržitelné.</p>

<p>Na závěr pamatujte s jednou věcí: v případě Internetu věcí nelze očekávat jakoukoliv chytrost od uživatele. Bezpečnostní otázky "Přejete si vymazat všechna vaše data" jsou tu od toho, aby na ně 96% uživatelů kliklo jako "Ano". A už jediné procento těch, kteří to učiní, vám udělá peklo ze života. Rada tady je jednoduchá: nenabízet uživatelům možnosti, kde by si mohli vybrat něco destruktivního nebo takového, že by to zapříčinilo nespokojenost se službou. To je také jeden z důvodů, proč si v energomonitoru zatím stále tak málo věcí mohou nastavit uživatelé. Odpojit si senzor měření z web rozhraní je sice nesmírně demokratické, ale počítejte s naštvaným uživatelem, který to přes pět varování potvrdil a teď si stěžuje, že mu to nefunguje. A naštvání uživatele něco stojí. Čas na supportu, blbé renomé a další nepříjemnosti. Uživatel je vždy bezpečnostním rizikem, které berete na svá bedra a musíte očekávat nejneočekávatelnější.</p>

<h3>Malé shrnutí</h3>
<p>Zatím je jednodušší poplašné scénáře psát, než realizovat, to v každém případě. Většina krabiček Internetu věcí je velmi jednoduchá a omezená, stejně tak jejich připojení. Při dodržení základních bezpečnostních postupů při návrhu se zatím není vcelku čeho bát, největší slabinou je vyzrazení vlastního hesla pro přístup do webové služby.</p>

<p>Spolu s tím, jak se zvyšuje výpočetní výkon a snižuje cena kompletů například nad ARM procesory, se ale budeme setkávat s výpočetním výkonem, jaký před deseti-patnácti lety příslušel spíše jen osobním počítačům. A kde bude možné nejrůznější eskapády realizovat podstatně pohodlněji, než na maličkém Arduinu. Tehdy přijde vzestup bezpečnostních technologií.</p>

<p>Zda si na to máte vsadit a pustit se do vývoje nějaké IoT security záležitost? Tady bych byl pesimistický, alespoň prozatím. Ani pro antiviry v mobilu podle mne zatím není dostatečný důvod, mobilní viry se do nějaké podstatně škodlivé fáze nedostaly. Mimo jiné i pro docela důslednou kontrolu v aplikačních obchodech provozovatelů. Ta je sice vývojářům nepříjemná, ale efekt oddělení mallware zatím plní skvěle, největšími incidenty jsou nedostatečné avizace o stažených kontaktech z vašeho mobilu.</p>

<p>Tím bych ale nechtěl říct, že není prostor pro bezpečnostní koncepty, které si dnes představujeme jen velmi těžko. I v energetice se dnes začíná pomalu mluvit o optimalizaci provozu v rozvodných sítích a o detekcích nepatřičností, což je z povahy elektřiny poněkud jiná úloha, než třeba pouhá implementace BGP routingu. Jak to pojmout, dnes umí málokdo říct - jestli to rozlousknete a ušetříte elektronům nějaké to cyklování po kabelech, v nichž vzniká ztráta, pár korun na tom jistě trhnete.</p>

<p>Nezapomínejme totiž na to, že selhání bezpečnosti v případě intenzifikace má vždycky dominová efekt: selhání například v rozvodých energetických sítích má následky přímo fatální. Proto nelze bezpečnost podceňovat a proto třeba u energetiky je dnes zcela legitimní koncept chytrých indikátorů, které jsou paralelní k tradiční energetické infrastruktuře a nenahrazují elektroměr (zařízení to vyzkoušené, prověřené a stabilní). I to je důvod, proč to tak děláme - ne proto, že bychom neuměli navrhnout nový elektroměr :)  </p>

<p>Tož, tolik ode mne pár poznámek k bezpečnosti Internetu věcí pod dojmem tohoto<a href="http://gigaom.com/2014/01/22/the-internet-of-things-needs-a-new-security-model-which-one-will-win/"> článku na GigaOmu</a>, od něhož jsem čekal více. Mé názory berte prosím jako osobní, prakticky nekompetentní zamyšlení.</p>

<p> </p>