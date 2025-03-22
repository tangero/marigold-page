---
author: Patrick Zandl
categories:
- Patrickův newsletter
- Apple
- Google
- AI
- Sociální sítě
- Internet
- Startupy
- EU
- Automotive
date: '2023-07-04'
layout: post
original_newsletter: "Patrickův newsletter #64 \U0001F942 Jak Twitter padnul nezaplaceným
  účtem (a poslední AI dění)"
summary_points:
- Musk zavedl editační tlačítko na Twitteru, s historií úprav a za příplatek.
- Twitter omezil čtení tweetů kvůli nákladům na cloudové úložiště Googlu.
- Nový Twitter funguje agilně, testuje hypotézy v praxi a rychle opravuje chyby.
- Algoritmy Twitteru podporují toxicitu a polarizaci, což vede k odchodu uživatelů.
title: "Twitter se pod Muskovým vedením stal dynamickým"
---

Twitter byl řadu let známý svou rezistencí vůči změnám. Příslovečné to bylo na editačním tlačítku. Že by bylo hezké editovat odeslané tweety, se říkalo léta a uznávalo to i vedení Twitteru, jenže to “nebylo tak jednoduché”. Jak by se věrohodně zaručilo, že lidé nelajknou nějaký tweet a jeho autor ho po nějaké době nezmění na naprostý opak? To namítalo vedení Twitteru. A tak se Twitter s problémem crcal tak dlouho, až jej koupil Musk. A ten řešení vymlasknul ihned: editační tlačítko je pokud možno za příplatek, do půl hodiny po odeslání lze editovat vždy, pak se ukládá a zvýrazňuje historie editace. A komu se to nelíbí, ať táhne jinam, žádná etická komise o ničem rozhodovat nebude. Bylo vymalováno, v zásadě se trefil do toho, co komunita akceptovala. 

Konec června byl odlišný případ. Musk oznámil nejprve to, že Twitter neumožní čtení tweetů neregistrovaným uživatelům a následně také limity, kdy registrovaní platící uživatelé mohou za den přistoupit k 6000 tweetům, neplatící k desetině a nově registrovaní k ještě méně (čísla se měnila). O důvodu se spekulovalo, ale vcelku správně všichni odhadli, že je především finanční. A vskutku. Twitter totiž nedojednal prodloužení smlouvy s Googlem za pronájem cloudového úložiště a Google začal od začátku července účtovat interakce. Twitter se pokusil omezením počtu interakcí na uživatele zredukovat zátěž na servery a tím i výši účtu, která mu dorazí od Google. Jenže to mělo dopad na uživatele. Mimo jiné i v tom, že hned po prvním oznamu, který limitoval čtení Tweetů na registrované uživatele, se farmy scanující tweety anonymně přes web, přeorientovala na přihlášení k účtu. Což ovšem radikálně zvýšilo zátěž na servery a tedy cenu, kterou bylo třeba zaplatit za cloudy Googlu. Proto Twitter záhy přišel s omezením na počet interakcí. A mimochodem, tohle byl následek toho, že Musk propustil jednoho systémového architekta, který měl cenovou optimalizaci na starosti. Hezky popsáno [zde na The Verge](https://www.theverge.com/2023/3/6/23627875/twitter-outage-how-it-happened-engineer-api-shut-down). Podrobnější popis [opět na The Verge](https://www.theverge.com/2023/7/1/23781198/twitter-daily-reading-limit-elon-musk-verified-paywall). 

Ve skutečnosti to ukazuje, jak nový Twitter funguje: občas zmateně, ale velmi agilně a iterativně. Nadhodí se hypotéza a místo, aby se dlouho zvažovala, se implementuje a otestuje v praxi, na produkčním prostředí. Nebo, pokud si Musk není jistý přínosem dané věci nebo člověka, tak to prostě ukončí a dívá se, zda se to nějak projeví, v nejhorším případě, zda se něco pokazí. Firma se pak snaží rychle vychytat mouchy a zalepit díry - předešle popsaný lapsus byl nakonec dvoudenní záležitostí. Extra nároční uživatelé Twitteru frflají, těch se to dotklo, běžný uživatel si toho prakticky těžko mohl všimnout (sám jsem na limit nenarazil) - pokud mu skočila nějaká chybka, mohl ji spíše považovat za chybku v připojení atd. 

### Toxický Twitter

Fast Start, Fast Fail je princip vhodný u začínajících služeb, ne vždy se s ním ale setkáváme u služeb, které používají stamiliony uživatelů. Měli jsme to vždy spíše za doménu startupů, než u zavedených firem. Twitter se znovu stal startupem se vším všudy. Včetně ostré a nevyřčené redefinice toho, kdo je jeho uživatelem. 

Na Twitteru totiž ani tolik nevadí experimenty s novými funkcemi, jako spíše toxicita jeho algoritmů. Kdysi jste si v něm mohli udělat své bezpečné prostředí a když jste někoho vidět nechtěli, tak jste ho neviděli. Nově se Twitter se svými algoritmy řazení zpráv podobá spíše Tiktoku. Pokud má dojem, že byste na něco emotivně zareagovali, tak vám to do přehledu zpráv spíše frkne. Jenže tím se váš svět rozšiřuje především na názory, které vás štvou a které by jinak byly velmi pravděpodobně marginálními. Namísto vašeho klidného světa je italským manželstvím. I z toho důvodu řada dříve aktivních a zajímavých lidí Twitter opouští. Sám jej používám mnohem méně, neboť mi jeho toxicita přijde velmi demotivující. Namísto šíření zpráv a zajímavých informací (nebo upozornění na ně) k čemuž Twitter dlouho sloužil, je nyní nosičem polarizovaných komentářů: čím silnější vyjádření, tím štěpnější a tím pro algoritmy lepší. 

Rozkymácený Twitter je příležitost. Roste (nikoliv závratně) počet uživatelů Mastodonu a o svém Twitter-like programu uvažuje i Meta. Ta již omylem v Google Store na [chviličku publikovala program Threads](https://www.theverge.com/2023/7/1/23781271/instagram-threads-twitter-leak-android-google-play), který doplňuje Instagram a funguje vlastně stejně, jako Twitter. Možná je tu prosto na další sociální síť, má to ale být kopie Twitteru provozovaná další megasítí?

* * *

[![](https://substack-post-media.s3.amazonaws.com/public/images/d1b279e3-b82d-4b55-beca-21b5a73b18db_1200x500.png)](https://www.melvil.cz/kniha-myty-a-nadeje-digitalniho-sveta/)Moje kniha má také svou audioverzi… 

![](https://substack-post-media.s3.amazonaws.com/public/images/d1b279e3-b82d-4b55-beca-21b5a73b18db_1200x500.png)