---
ID: 2106
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/stream-umozni-vlozit-video-do-vasich-stranek-a-priklad-u-fona

  '
post_date: 2007-05-17 10:02:27
post_excerpt: ''
published: true
summary_points:
- Stream umožňuje vkládat uživatelská videa do stránek pomocí vygenerovaného HTML
  kódu.
- Stream má pro český trh lepší distribuční síť než Youtube.
- Stream ztěžuje uložení videa z distribuční sítě na lokální disk.
- Pro vkládání videa do HTML se používá Script, nikoliv embeded object.
title: Stream umožní vložit video do vašich stránek a&nbsp;příklad U-fona
---

Tahle funkce nakonec trvala o něco déle, než jsme čekali, protože nás pohltila příprava virtuálního studia. O něm ale někdy jindy, protože je to dost zajímavé na to, aby se to dalo odbýt pár slovy. 

<strong>Vkládání videí do vašich stránek</strong> je funkce, kterou proslavil už Youtube. Video stačí nahrát na server a pak vzít vygenerovaný HTML kód ze stránky videa a vložit jej do stránky. Takto například vypadá, když vložím do stránky reportáž Stream TV věnovanou startu U-fona (který jsem jinak nestihl zapsat, takže to berte jako náhradu mého komentu, což je pro MobilKom výhoda, nebyl by tak kladný, jako repka):

<script src="http://www.stream.cz/include/3701?w=400&h=300"></script>

<h3>Jaké jsou výhody a nevýhody uložení videa na Streamu</h3>

Přehrávač určený pro cizí stránky je graficky neutrální.

Do stránek lze <strong>vložit jen uživatelská videa</strong> (nově u nás v menu označená za Vaše videa). Sám jsem <a href="http://www.stream.cz/clanek/928-u-fon-priletel-co-je-zac">reportáž o U-fonovi</a> musel přehodit i do Uživatelských videí, což ostatní udělat nemohou. Proč to tak je? Prvně považujeme za důležité, aby lidi mohli vkládat do svých stránek hlavně svůj vlastní obsah, aniž by si k tomu museli vytvářet nějakou infrastrukturu nebo zabírat místo na disku. Omezení z naší strany je pořád 100 MB dat na jeden snímek, počet snímků nemáte omezený. A po druhé je tu problém technický: naše vlastní reportáže jsou zaobálkované a skládají se z více videí, jenže do stránky lze vložit přes tento kód jen jedno konkrétní video. Jak to udělat u více, zatím filosoficky řešíme, ale není to priorita, protože stejně si asi lidé budou vkládat hlavně vlastní obsah. 

Proč používat vkládání videí přes Stream? Správná otázka. Můžete použít Youtube, když se smíříte s nižší technickou kvalitou (nižší bitrate a nižší rozlišení obrazu) a především nižší přenosovou rychlostí. Tohle bych považoval za hlavní argumenty pro český / slovenský trh, protože máme distribuční síť podstatně lépe vytvořenou pro pokrytí lokálního trhu a na slušnější lince (cokoliv nad 512 Kb/s včetně, s průměrným jitterem) se můžete na video dívat online bez přerušení. 

Vlastností (kterou můžete brát jako výhodu a také jako nevýhodu, záleží na vás) je <strong>obtížná možnost uložení videa z distribuční sítě Streamu</strong> na lokální disk. Ne, že by to nešlo, ale jde to podstatně hůře, než z Youtube a jiných zahraničních distribučních serverů. 

Pěkně vyřešený máme full screen režim, to jsou ty dva čtverečky úplně vpravo. Ten je fakt fajný.  

Pro vkládání do HTML stránky se používá Script. Ten nám umožní plynule upravovat podle požadavků vlastnosti distribuce videa. Z několika důvodů to nechceme vkládat přímo přes embeded object jako Flash prvek, snažili jsme si zmapovat výhody a nevýhody. Zatím jedinou nevýhodou pro Script nám vychází, že některé redakční systémy příkazy scriptu odstraňují, což ale dělají někdy u object. 

Komentáře jsou vítány, otázky zodpovíme. 

Jednou upozornění: script se odvolává zatím na adresu test.stream.cz - tento týden bude změněna na ostrý server, takže si klidně to test opravte na www. Jinak lze měnit šířku a výšku videa atributy W a H s tím, že stranový poměr by měl být 4:3 - jinak se video deformuje, tak na to pamatujte :). 

Takže, chcete si udělat vlastní televizi po svém a ušetřit náklady za infrastrukturu? Nyní máte možnost. Jděte do toho, ukažte nám, jak to uděláte lépe :)
 
Poděkování: Franci, Péťa, Japan, Michal, Ethan :)
Next task: Live video upload.