---
ID: 2227
author: Patrick Zandl
categories:
- Média
layout: post
oldlink: 'https://www.marigold.cz/item/otestujte-si-celovecerni-film-renesance-online

  '
post_date: 2008-05-06 19:20:14
post_excerpt: ''
published: true
summary_points:
- Konfigurace balanceru způsobila chyby testerů, nyní je opravena.
- Stream.cz testuje inteligentní distribuci celovečerního filmu online.
- Používají Flash s H.264 pro plynulé přehrávání a streaming.
- Žádají uživatele o zpětnou vazbu na funkčnost a komfort přehrávání.
title: 'Otestujte si: celovečerní film Renesance online'
---

<b>Update:</b> našli jsme chybu, kvůli které nám to vyhazovalo testery. Poté, co jsme všechno rozkopali, se ukázalo, že u jedné komponenty jsme špatně zkopírovali konfiguraci balanceru a ten nám vyhazoval uživatele. Už jest to opraveno, takže: 
 
A máme tu pravidelnou testovačku pro natěšené experimentátory s videem. Úkol: jak inteligentně distribuovat celovečerní film po internetu v dostatečné kvalitě a komfortu. <a href="http://www.stream.cz/?m=stream&a=static&page_url=renesance">Naše řešení je zde ve formě technického testu</a> ... není to ostrý provoz, jen chceme na zkušenějších uživatelích netu (=vás) vyzkoušet, co na to říkáte. Takže než tam vlezete, možná si přečtěte následující.

Naši filmoví géniové si s tím hráli a hráli. Nechtěli jsme to řešit tak, že si uživatelé budou muset film nejdříve celý stáhnout a pak na něj koukat, jako je tomu u českých platforem videopůjčoven. Chtěli jsme, aby si uživatel kliknul na stránku a hned koukal. Jediný další krok je, že když se nechce dívat na film v malém okénku, klikne si na zvětšení do full screen režimu. Výhoda koukat hned podle nás převažuje nad výhodou moci koukat znovu bez stahování (kterou navíc jinde kripluje DRM omezení, takže další den je soubor k vyhození). Ano, to je zjednodušení našeho problému: nepředpokládáme, že se u nás za film bude platit, takže ho nepotřebujeme obskurně kriplovat. Použili jsme standardní Flash s H.264 (potřebujete verzi 9.0.115 a vyšší) - přehrávač je napsaný ve Flash s AS3, podporuje tedy i hardware akceleraci grafickou kartou. Významný posun v plynulosti obrazu na slabších procesorech. 

Celovečerní film přinesl nutnost nasazení streamingu oproti jinak na Stream.cz používanému progresivnímu downloadu. Technicky je to náročnější na nás, ale u progresiv downloadu mají soubory tendenci ukládat se do cache a až se vám tam uloží celovečerní film, podivíte se, jak hospodaříte s diskovou kapacitou. Navíc to prohlížečům (či spíše plugin přehrávačům) nedělá dobře a rády si žuchnou. Streaming také přinesl výhodu komfortního seekingu, tedy přeskakování na libovolné místo. Myslím, že nám to funguje velmi slušně, i když je tam malá prodleva, kterou se už nedaří odladit: je to tak půl vteřiny, dost na to, aby si uživatel všimnul, že se ukazatel posunul, ale ne film a začal panicky klikat. To už se bude muset holt doladit graficky nějakým nápisem "Přetáčíme film" - ostatně, kde u VHSky nebo DVD přejedete tak rychle a komfortně, tohle už je jen o optimalizaci uživatelského rozhraní. 

Berte to prosím jako technologické demo. Zajímají nás vaše zkušenosti z praxe: z různých počítačů, linek, operačních systémů. Když budete psát postřehy, nezapomínejte napsat, jakou přípojku a rychlost máme, co máte za OS a prohlížeč. S rezervou berte grafiku, ani přehrávač ani stránka žádnou nemá, pudrovat se to bude, až budeme spokojeni s technickým provedením.    

Aby bylo na co se dívat, vybrali jsme sci-fi film <strong>Renesance</strong> Christiana Volckmana (v českém znění). Až poněkud pozdě jsme si uvědomili, že to není zrovna barvou hýřící film, ale snad i tak oceníte, že kvalita obrazu je velmi dobrá i ve full screenu. To je ten čtvereček vpravo dole vedle ovladače zvuku. 

Abych <a href="http://www.stream.cz/?m=stream&a=static&page_url=renesance">nezapoměl URL, testovat můžete tady</a>, své připomínky a náměty, jak by podle vás mělo vypadat a chovat se přehrávání celovečerních filmů pište zase sem. Nepište si o filmy, tohle je technologický test :)