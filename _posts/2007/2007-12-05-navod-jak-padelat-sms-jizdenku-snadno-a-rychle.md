---
ID: 2180
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/navod-jak-padelat-sms-jizdenku-snadno-a-rychle

  '
post_date: 2007-12-05 12:43:37
post_excerpt: ''
published: true
summary_points:
- SMS jízdenky lze podvrhnout, úspěch závisí na revizorově kontrole.
- Revizoři často neověřují SMS jízdenky detailně, spoléhají na doručení zprávy.
- Podvržení SMS lze provést změnou jména kontaktu na telefonním čísle.
- SMS jízdenka je bezpečnější než papírová, problémem je školení personálu.
title: "Návod, jak padělat SMS jízdenku snadno a rychle"
---

... po mne požaduje v poslední době celá řada lidí. Tak mne napadlo, že bychom si mohli trochu zabádat a zalaborovat, jak je to se zabezpečením SMS aplikace na pražské SMS jízdenky.

<!--more-->

Bezpečnost ničeho takového nemůže být stoprocentní, laborovat s jízdenkama má podstatnou výhodu, že narozdíl od bankovek to nejsou ceniny, takže jejich "ovlivnění" není padělání. A své bezpečnostní problémy měly už klasické papírové jízdenky, o tom ale jindy, protože naše pokusy s papírovýmí jízdenkami jsou příčinou dobrého renomé české genetiky. 

Aplikace tohoto druhu by měla vykazovat několik stupňů možností ověření, přičemž úspěšnost podvržení falešné SMS jízdenky je závislá na přístupu testujícího subjektu ke kontrole. V posledních dnech jsem s tím ze zájmu trochu laboroval a zde jsou výsledky (na okraj: od mé stížnosti na opožděné chození SMS zpráv musím říct, že se to zlepšilo a většina přijde do dvou minut).


Prvním druhem kontroly je faktické konstatování, že potvrzovací SMS zpráva přišla. Revizor ji vidí v telefonu a to je první stupeň ověření. Jak se ukázalo, revizor v případě, že mu není majitel jízdenky podezřelý, zprávu dále neověřuje. Pravděpodobně proto, že byl instruován o důvěryhodnosti takové zprávy. 
<img src="http://www.marigold.cz/wp-content/uploads/smsjizdenka-iphone.jpg" width="320" height="480" alt="SMS jízdenky na iPhone" title="SMS jízdenky na iPhone" border="1" align="right" />

Jak to je? SMS zpráva odeslaná na číslo 9020620 je vždy zpoplatněna částkou 20 Kč s DPH. Lhostejno, zda dostanete zpět SMS jízdenku nebo chybovou hlášku, což je mimochodem chyba v návrhu aplikace, která lidi asi časem bude štvát (když pošlete třeba DPP, zaplatíte 20 Kč, ale jízdenku nedostanete!). A řekl bych, že při známém procentu překlepovosti je to také součást plánovaného výdělku z provozu aplikace. Zpět přichází zpráva z téhož čísla, což ostatně vyžaduje i Premium SMS kodex: odpovědní zpráva musí být z téhož čísla a tedy i téže cenové úrovně. 

Podvrhnout tuto zprávu by znamenalo možnost ovlivnit číslo odesilatele. To u standardního připojení Premium SMS není možné, ačkoliv číslo může poskytovatel SMS služby nastavit podle svého, operátor SMS zprávu na rozhraní nepřijme, pokud není korektní. Změna nastavení se neprovádí jen tak někomu a lze s klidem zavrhnout myšlenku, že by se k tomu dostal někdo, komu by stálo za to padělat SMS jízdenky, je to asi tak pravděpodobné, že to bude stát za to obsluze SMS centra u operátora. Výjimkou je testovací aplikace na ČVUT, tam by to nasimulovat asi šlo. Další výjimkou jsou zahraniční SMS centra, z nichž některá vás nechají nastavit si číslo odesilatele na kýžených 9020620. 

Existuje mnohem jednodušší varianta. SMS zprávu si odešlete z libovolného telefonu (třeba z vlastního) a vytvořte si kontakt s číslem odesilatele a jako jméno zadejte 9020620. Většina telefonů takto došlou zprávu zobrazí tak, že na první pohled není patrné, že byla odeslána z jiného čísla. 

Ověření tohoto triku ze strany revizora je opět snadné a offline. Většina telefonů umožní zobrazit Detail zprávy, tedy skutečné číslo odesilatele (odhalí trik s vytvořeným kontaktem) nebo použité SMS centrum (odhalí poslání z jiného SMS centra). Ale například na mém iPhone detail zprávy v telefonu zobrazit nejde. 

Třetím způsobem ověření je kód umístěný v SMS zprávě. Ten se  skládá ze dvou částí, první je viditelně nějaký hash kód (čísla a písmena), druhá část jsou jen čísla a přijde mi, že je to pořadové číslo odeslané SMS zprávy (zatím jsem narazil na jednu výjimku z číslování). To by znamenalo, že do dneška bylo posláno zhruba 100 000 sms zpráv. To mi přijde jako slušný úspěch. 

Číslo je zřejmě určené pro další offline validaci jízdenky. Revizor ví, kolik jízdenek bylo zhruba vydáno a primitivně podvrženou jízdenku takto snadno odhalí, když má nižší číslo. 

Pokud i po těchto třech krocích, které je možné učinit offline, má revizor pochybnosti, může přistoupit k ověření online.  Prý se může připojit přes PDA , v praxi jsem viděl, že někam telefonuje, PDA neměl. Přes telefon může zjistit podle telefonního čísla, zda jste zaplatili, i když už neznáte obsah SMS zprávy (došla baterka). Přes PDA může ověření proběhnout zřejmě také offline tím, že kód je nějakým hashem provedeným nad telefonním číslem a platností jízdenky, což zajistí časové i osobní vymezení jízdenky. Záleží na postupu, jak tato dvě čísla zahashovat tak, aby bylo prakticky "nerozluštitelné". 

Nejpraktičtější se mi jeví možnost jednou za čas (denně?) synchronizovat databázi hash kódů, což umožní používání offline ověření autenticity kódu (výhodné v Metru), minimalizuje to nutnost vymlacovat z nekooperujícího cestujícího dodatečné údaje a zároveň to ponechá možnost dynamicky měnit algoritmus a ponechat jeho unikátnost. Zda je to tak použito v případě DP Praha, nevím. 

Z praktického pohledu tedy lze říci, že SMS jízdenku lze podvrhnout do určité míry s vyhlídkou na úspěch. U "podezřelého" cestujícího provede revizor validaci, u toho "nepodezřelého" si tu práci asi odpustí. Ale berte to jen jako momentální osobní postřeh a své pokusy v tomto oboru dělejte na vlastní nebezpečí. 

Pokud je systém kódu v SMS navržen rozumně (což se mi z něj nepodařilo za krátkou chvíli odvodit), je SMS jízdenka pro dopravní podnik podstatně více bezpečná, než jízdenka papírová. Jediným praktickým problémem zůstává, jak proškolit personál v jejich rutinním ověřování.