---
ID: 2998
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/presystemovano-aneb-mnoho-systemu-firmy-smrt-malo-systemu-taky-smrt

  '
post_date: 2015-05-19 12:07:33
post_excerpt: ''
published: true
summary_points:
- Energomonitor řeší integraci vnitrofiremních systémů, dříve sdíleli soubory přes
  Dropbox a Google Apps.
- Dropbox Business je drahý, proto firma přechází na Google Drive, i přes jeho nedostatky.
- Objednávky přicházejí přes eshop, email, telefon; data se exportují do OnePageCRM.
- Plánuje se zrušení Freshdesku a převod na Daktelu, řeší se komunikace přes Slack.
title: Přesystémováno aneb mnoho systémů, firmy smrt, málo systémů, taky smrt
---

<p>Jedna z věcí, na které v <a href="http://www.energomonitor.cz">Energomonitoru</a> neustále narážíme, jsou vnitrofiremní informační systémy. Respektive to, jak se s nimi vypořádat. Zatím situaci řešíme systémově a uvážlivě zřízením ředitelství pro integraci vnitrofiremních systémů - tedy pokusy o propojení již používaných systémů - ale pojďme se na to podívat, v čem tkví jádro pudla.</p>


<!--more-->

<p>Kdysi dávno nás bylo málo a jen jsme si sdíleli soubory. K tomu sloužil Dropbox, protože na něm je sdílení souborů jednoduché a jejich zpracování jak by smet. Jenže jsme si taky začali platit Google Apps, protože je používáme na firemní email (a v podstatě jen jako ten email). A v rámci Apps máje 30GB prostoru, což začalo být zajímavé v momentě, kdy 2GB volného prostoru na Dropboxu přestalo stačit. Problém je, že za Dropbox Business zaplatíte jedenáct dolarů na osobu, což u nás už představuje tři stovky dolarů měsíčně, za což dostaneme prostor navíc a pár funkcí, které by nám byly ukradené. Takže jsme začali šetřit, na Dropbox se dávaly finální verze, na Google Drive začaly být ty rozpracované a fotky. Jenže ani to nestačilo, takže se dneska kompletně stěhujeme do Google Drive, z čehož radost nemáme, ale co naplat. V Google Drive se překvapivě těžko dělají věci, které byste považovali za samozřejmé. Například je nelze nastavit tak, aby implicitně bylo všechno sdílené a jen nějaký adresář soukromý, jde to jen opačně a uživatel si to musí pořád uvědomovat. Je to drobnost, ale když si ji uvědomujete stokrát za den, tak trochu prudí. Je tam pár dalších takových drobností, které jsou opravdu prudící, ale dá se říci, že sdílení souborů by se dalo takto kontumačně vyřešit a i když více sympatií momentálně chováme třeba k OwnCloud, GApps už si platíme. S ohledem na to, jak kolaborativní GApps mají být, je až překvapivé, že tam nemůžete jednoduše vytvořit adresář sdílený pro celou firmu určený například k tomu, aby se všem lidem synchronizovali do mobilů čerstvé kontakty všech kolegů.</p>

<p>No, pojďme dále. Co potřebujeme ve firmě dále? Tak především přijímáme objednávky přes eshop, což je modul ve Wordpressu, který používáme pro webovou presentaci. Data je třeba exportovat do CRM, používáme OnePageCRM, aby je bylo vidět s veškerou zákaznickou komunikací, z Google Apps se tam přetahuje i korespondence s klientem. Jenže část objednávek také přichází emailem nebo telefonicky, zejména ty větší. Ty větší se doposud řešily odděleně v systému výroby, od něj pro jednoduchost abstrahujeme, menší se ručně přepisují do eshopu a dále se s nima postupuje jako s eshopovými.</p>

<p>Nyní malý chyták k objednávkám. Objednávky jsou buďto samoinstalační, kdy objednané zboží zasíláme a dále se nestaráme, nebo s naší instalací, kde musí přijet náš technik. A tak si co den musí manažer instalací vytáhnout data z eshopu, seřadit si objednávky podle měst a obvolat instalační techniky. Určitou touhou je, aby tuhle ruční práci v Excelu také převzal nějaký systém. Je to vcelku jednoduché, jen se zde sleduje, kdo na kdy přislíbil instalaci a zda ji provedl, trochu to předtřiďuje instalace podle měst, ale nic velkého to není - je to náš takový malý sen na letošní léto, dovést to do větší automatizace.</p>

<p>Přidejme k tomu nově zřizované callcentrum. Doposud mělo jedno číslo, jednoho člověka, jenže přibývají další dva a cílově letos pět, možná více lidí. To už chce VoIP ústřednu, volba padla na Daktelu s hezkou podporou callscriptů a vlastním prodrátovaným CRM. Takže máme zhruba něco jako třetí CRM. Otázka, co s tím. Jedna z úvah je, že se zbavíme OnePageCRM a všechno prodrátujeme s Daktelou, ale to uvidíme, jak se osvědčí v praxi. Historicky navíc máme čtvrtý systém, který se váže k CRM a tím je helpdeskový systém od Freshdesku. Je to skvělý systém na ticketování a zpracování došlých požadavků, jenže na něm běží jen česká emailová podpora a využívá se málo, krom toho je v ní něco jako FAQ systém, který běží na samostatném URL podpora.energomonitor.cz. Dlužno dodat, že na podporu se lze přihlásit, ale automaticky se sem nepropagují přihlašovací údaje z energomonitoru, ani to kvůli bezpečnosti nechceme (dávali bychom hesla klientů mimo náš systém) - ale lidi to dost mate, netuší, že si mají znovu zakládat přihlášení. Plán je Freshdesk rovněž zrušit, převést na Daktelácké či jiné centrální CRM (to daktelácké má za příplatek i helpdesk pro email) a FAQ převést na Wordpress.</p>

<p>Tím ale systémy nekončí. Dále tu máme softwarový vývoj. Ten se nějak plánuje (<a href="http://www.trello.com">Trello</a>), nějak dokumentuje (<a href="https://www.atlassian.com">Confluence</a>) a nějak vytváří (Github). Překvapuje mě, jak málo je variant ke Confluence - hostovaná Wiki s řízením přístupu.</p>

<p>Pak tu máme <a href="https://slack.com">Slack</a>, kterým technologická část firmy komunikuje, ta netechnologická ho moc ráda nemá. Protože za Slack neplatíme, nedá se v něm pořádně vyhledávat a je kromě realtime komunikace vlastně na prd. K realtime komunikaci se ještě masivně používají iMessages, kdo je nemá tak SMS (mezi Prahou a Valmezem, já denně pošlu přes stovku SMS/iMess zpráv) pak Skype a GTalk nebo jak se to dneska jmenuje. Co vadí na Slacku? Hlavně to, že kromě průběžné komunikace k ničemu není. Nelze tam pořádně zakládat témata a o těch se bavit a vracet se k tomu, když rozhovor ujede za horizont času, po který to Slack skladuje, zmizne to. Neumí vlákna, neumí reakce na něco, opravu mimo realtime komunikaci je to nepřehledné. Naopak Yammer se mezi programátory neujal, netechnické části firmy by ale vyhovoval více, jenže už máme hrůzu z dalšího systému.</p>

<p>Jednotlivá oddělení používají různé online nástroje, u nichž nepožadují spolupráci s celou firmou. Například UX používá Axure a Sketch, vygenerované náhledy ale už zpřístupňuje přes Confluence k firemní oponentuře či formou programátorského zadání a přes Google Drive. Stejně tak výrobní část firmy organizuje výrobu - na to dnes slouží jednoduché tabulky, ale zrovna jsem ve fázi hledání výrobního ERP systému, který nám zjednoduší generování objednávkových sestav, kusovníků, pro jednotlivé výrobní procesy. Jenže samotné vybírání není moc jednoduché. ERP systémů pro výrobu je v Česku celá řada, ale většina má hodně středověký vzhled vázaný na Windows, což nás odrazuje a kromě toho se obtížně o nich získávají informace na webu. Dema nejsou k dispozici, soupis funkcí většinou velmi obecný a malý - na to, že to nejsou levné systémy, jsou ty webové presentace nedostatečné. Je třeba do firem volat, ptát se, většinou se nám někdo tlačí na presentaci, jenže mi si chceme nejdříve projít naše požadavky. Takže jsme zpracovali formulář, kde se ptáme, zda systém umí náležitosti, co potřebujeme, zatím máme desítku odpovědí, ale nic nevypadá, že by nás vzalo za srdce a jít do amerického NetSuite už asi bude mimo naši ligu.</p>

<p>Už jenom procesy sepsat a zmapovat si vyžádalo práci jednoho člověka. Takhle nějak třeba vypadá objednávka, jak ji zakreslila Petra.</p>

<p><img title="objednavka-proces.png" src="http://www.marigold.cz/wp-content/uploads/objednavka-proces.png" alt="Proces objednávky" width="455" height="327" border="0" /></p>

<p>Ve výsledku jsou teď tři cesty pro řešení objednávek a instalací. Žádná mě netěší velmi. Je možnost ohýbat Daktelu nebo eshop modul. Obojí má spíše proti, než pro, ani jedno na to není určené. A lze si něco naprogramovat, jenže do toho se nám nechce, programátory potřebujeme na něco jiného. Lze si někoho najmout, ale na to dost spěcháme, abychom mohli v klidu vybírat. Existují systémy jako Zoho Creator, které umožňují si jednodušší aplikaci, která by nám vyhovovala, natypovat přes webové rozhraní. Nebo silnější a podstatně dražší <a href="http://quickbase.intuit.com">QuickBase</a>. Možná vyzkoušíme <a href="https://creator.zoho.com">Zoho Creator</a>. Komplexní ERP teď nemám ani čas, ani chuť vybírat, ještě ani nevíme, jak se nám to zajede a kolik změn bude potřeba.</p>

<p>Přemýšlím, kde jsme udělali chybu. Asi jsme dlouho váhali. Nebo nabídka flexibilních moderních řešení není ještě saturovaná. Nebo middlewarové systémy typu Zoho Creator mají velmi významné a nedoceněné místo na světě. Jo, kdybyste v Creatoru někdo výrazně uměli, ozvěte se :)</p>

<p> </p>

<p> </p>

<p> </p>