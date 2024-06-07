---
ID: 2211
title: 'iPhone a&nbsp;podpora Javy či&nbsp;Flashe &#8230; hm&#8230;'
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/iphone-a-podpora-javy-ci-flashe-hm
published: true
post_date: 2008-03-10 20:07:17
---
O tom, že by iPhone měl podporovat Flash i Javu se v minulých pár dnech mluvilo. A když už jsem se pustil do iphonování, tak dokončím i tohle, ostatně <a href="http://blog.macich.net/clanky/java-pro-iphone-nebude/">po přečtení článku Jirky Macicha</a> mi přišlo, že ne každý pochopil pointu Javy v mobilních telefonech. 

Vzpomínejme: pointa Javy měla kdysi být v tom, že seberete kód z jednoho počítače a on poběží na jiné mašině i v případě, že operační systém nedodala ta samá firma. Byla to vznešená idea, která oslovila i vývojáře pro desktop, než se ukázalo, že start Java Virtual Machine starajícího se o "interpretaci" spouštěného programu, vytíží systém běžného tehdejšího počítače na dost dlouho na to, aby uživatele bavilo čekat. Chystané "office" like balíky, které měly v Javě pokořit nativní Office na Windows, odpískal Corel/Wordpress i IBM a bylo po žížalkách. Pamatuju si je, byly hezké, ale víte, co je komické? Neuměly o mnoho více, než dnešní Google Docs a jim podobné aplikace. Ani nebyly hezčí. A už vůbec ne rychlejší. 
<!--more-->


Java tím nevychcípala na úbytě, jak se dalo čekat, ale ubytovala se na serverech a v hájemství firemních serverových aplikací, kde vývojáři ocenili objektivitu jazyka v době, kdy jiné jazyky pro vývoj serverových a webových aplikací objektovosti moc nehověly. Tím by bylo kouzlení s Javou zavřeno nebýt toho, že Sunu se podařilo protlačit ji do mobilních telefonů. Tam byla situace poněkud odlišná: vzletné heslo "writte once, run many" sice na mobilech taky nefungovalo ani náhodou (model od modelu se všechno musí dodneška opravovat a testovat), jenže na mobily jiný obecně použitelný jazyk nebyl. A kdo chtěl dělat aplikace na mobily, jinou šanci neměl, bez ohledu na to, že pro každý nový mobil se musela aplikace trochu upravit a znovu přetestovat. Portace her mezi mobily je dodneška opruz pro každého vývojáře a slušně žijí firmičky nabízející dálkový přístup na osmset různých mobilních telefonů pro testování aplikací. Pronájem strojového času v tomto případě žije - a slušně. 

V případě iPhone je situace opět odlišná. iPhone je počítač s telefonem, ne naopak. Místo toho, abyste používali limitovanou a nevalně rychlou Javu, máte k dispozici Objective C s Cocoa frameworkem, což je brutální rozdíl v pohodlí, rychlosti i přístupu k systémovým zdrojům. Stojí za to zmínit, že Java v mobilech (tedy J2ME) má řadu omezení a například až MIDP 2.0 umí zprostředkovat Java aplikaci přístup do telefonního adresáře atd. Securiti issues.

To je důvod, proč J2ME do iPhone je zajímavé pro fanoušky a bájezpytce, těžko ale pro realisticky uvažující vývojáře. Herní firmy sáhnou po nativním jazyku, který jim nabídne výkon i přístup k iPhone features jako multi-touch, grafickou akceleraci nebo náklonoměr. Myšlenka, že by stačilo vzít dnešní mobilní hry a "překompilovat je" na J2ME v iPhone, je mylná: nestačilo, bude na tom hromada práce. Zhruba stejně, jako vzít hry z Mac OS X a "překompilovat" je na Mac OS v iPhone. Je to hezká manažersko-novinářská myšlenka, která se skvěle vyjímá v powerpoint presentaci nebo kritickém článku, ale jak dorazí z boardmeetingu do programátorských slují v suterénu dané vývojářské společnosti, začnou se ozývat slova jak nad rybníčkem Brčálníkem.

Posledním důvodem jsou podmínky pro SDK: program vyvinutý na iPhone SDK nesmí spouštět jiné kódy, což mimo jiné zamezuje oficiální distribuci různých programovacích jazyků i software umožňujícímu instalovat pluginy. Neoficiálně to jde: na iPhone běží Ruby, Perl a další krasavci, ale to mluvíme o světlé zóně Jailbreaku. Takže suchým vývojem přes SDK to nepůjde, Sun by se musel dohodnout a Apple v tom smysl nevidí. Dlužno dodat, že v tom se s Apple shoduji: přínos J2ME pro iPhone vidím jako nulový. Rozebráno <a href="http://www.itwire.com/content/view/17038/1103/">anglicky třeba zde</a>. 

<h3>Flash</h3>

S Flashem je to jiná káva. Flash by se v iPhone užil, protože je to přirozené krmivo pro řadu webových kouzel. Není to tak dávno, co se začalo šuškat o tom, že by ho iPhone přeci jen mohl dostat, ale ven se dostalo prohlášení Steve Jobse, že Flash v iPhone nebude. Důvodem má být problém s výkonem: implementovat celý Flash, na to výkon iPhone nestačí a dávat tam Flash Lite zase nemá smysl, protože ten stále podporuje málokdo a sada funkcí je příliš oškubaná na to, aby to k něčemu bylo. Pravda je, že ve Flash Lite videa Streamu nepřehrajete (proto taky mám privátní iPhone verzi), ale to jen tak na okraj, to asi Stevemu na srdci neleželo. Mně už by více. 

Je otázkou, nakolik Steve kecá. iPhone má procesor 400 MHz, paměti hafo, <a href="http://www.appleinsider.com/articles/08/03/05/steve_jobs_pans_flash_on_the_iphone.html">rozebírají třeba zde</a>, zda to stačí. To vede skupinky spekulantů k domněnce, že Apple využívá tanečky kolem Flash/iPhone k tomu, že tlačí na ústupky ve věci PDF. Jaké přesně, mi není známo, sám tomu nedávám zase tak vysokou pravděpodobnost, že by šlo o PDF se mi nezdá. Ale že by v něčem Apple tlačil, to se zase stát může, Adobe mu ostatně před dvěmi lety slušně podtrhla stoličku, když Jobsovi vzkázala, že kvůli tomu, že on se rozhodl přejít u Macků na Intel procesory, nebude přeci Adobe vydávat žádnou zvláštní verzi svých software a že si bude muset Apple počkat na běžná release. Adopci Intel Macků to zpomalilo o více jak rok, protože pro designery je Adobe Photoshop/Ilustrator klíčovou záležitostí.  Že by to Steve Jobs vracel přes iPhony, se mi zdá příliš laciné, ale teorie samozřejmě bují. 

Soudil bych ovšem smířlivě, že v tomto případě jde o peníze: Apple z toho nevidí přínos pro sebe, což může znamenat také to, že v tom nevidí přínos pro zákazníky. Pravdou je, že ve Flashi jsou na webu zhusta hlavně reklamy a těch mi na iPhone líto není. Zahraniční aplikace rychle přispěchaly s iPhone verzí, Youtube videa jsou v H.264 na iPhone viditelná a komu jsem už demonstroval kvalitativní rozdíl mezi mobilním videem, videokvalitou podporovanou v rámci Flashe a H.264 optimalizovaného pro iPhone, mi jistě dá za pravdu, že v případě iPhone má optimalizovaná verze co dát světu. 

Vše výše uvedené ale nic nemění na tom, že spolu s ostatními iPhonisty želím nemožnosti bez doprošování se u Apple vyvinout Skype (ten dnešní webový iPhone mi moc nevoní) a některé další utilitky, které by vysely jako procesy stále.  

Po Flashi se mi zasteskne místy, po J2ME vůbec. Sorry Sune.