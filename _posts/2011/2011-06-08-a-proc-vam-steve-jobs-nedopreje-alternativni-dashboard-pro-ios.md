---
ID: 2388
author: Patrick Zandl
categories:
- Apple
- iPhone
layout: post
oldlink: 'https://www.marigold.cz/item/a-proc-vam-steve-jobs-nedopreje-alternativni-dashboard-pro-ios

  '
post_date: 2011-06-08 08:47:43
post_excerpt: ''
published: true
summary_points:
- Apple neumožňuje dashboardy kvůli optimalizaci výdrže baterie a výkonu.
- Jailbreaknuté iPhony mají dashboardy, což ukazuje, že omezení je politické, ne technické.
- iOS centralizuje úlohy na pozadí přes API pro efektivní správu baterie.
- Centrála notifikací v iOS 5 je alternativou k dashboardu s odlišnou technologií.
title: A proč vám Steve Jobs nedopřeje alternativní dashboard pro iOS?
---

<p>To je dobrá otázka, která padla v komentářích <a href="/item/proc-nema-iphone-dashboard">k mé minulé mikrostati věnované dashboardu</a>, takové té "úvodní obrazovce", kam se na vás valí všechny záležitosti, které musíte vyřídit, abyste žili se svým zařízením v míru. Proč vám Apple nedopřeje možnost instalovat dashboard jako alternativu? Proč nám vnucuje jedinou cestu?</p>


<p><img style="float: right;" src="http://www.marigold.cz/wp-content/uploads/jailbreak.jpg" border="0" alt="Today obrazovka - dashboard pro Cydia. Oficiálně jej ovšem nenainstalujete." width="320" height="480" /></p>

<p>Za prvé je vhodné poznamenat, že několik dashboardů či alternativních launcherů existuje, ale jen pro jailbreaknuté iPhony, protože se instalují přes Cydii. Takže to není omezení v návrhu systému, ale omezení v politice systému.Pokud už jste si nějaký neofiko dashboard instalovali, víte patrně odpověď.</p>


<p>Důvodem je výdrž baterie. iOS je, co se výdrže baterie týká, velmi obsesivní zařízení. Původní zákaz multitaskingu neplynul z toho, že by operační systém nebo procesor neutáhli multitask, ale z toho, že nebyly mechanismy, jak kontrolovat, kolik která aplikace žere baterky.</p>


<p>Řešením, s nímž se multitasking "povolil", bylo jednoduché. Systém telefonu bude mít své vnitřní API, jemuž každý program předá úlohy, které se mají vykonávat na pozadí. A těchto úloh je předem definovaná sada (tuším šest nebo sedm), například čtení polohy a zavolání programu v závislosti na ní (víme, že čtení polohy u iOS nemusí nutně znamenat zapnutí GPS, záleží na požadované přesnosti). Nebo třeba poslouchání z internetu na portu a zavolání aplikace, pokud něco přijde.</p>


<p>Je možná zřejmé, o co je takový přístup lepší: věci, které vyžadují značné zdroje baterie, jsou centralizovány a řízeny operačním systémem. Je jedna centrála, která se stará o to, zda a jaké porty a adresy z netu se poslouchají či pingají a to v intervalech, které systém uváží za optimální. Kdyby se o to starala každá aplikace zvláště, při takových pěti spuštěných aplikacích by telefon byl trvale na datovém provozu a baterka by šla do kopru za několik hodin. Například WP7 tento systém více či méně převzal také, naopak Symbian ani Android jej nemají a na výdrži baterie se to projevuje brutálně.</p>


<p>Běžná iOS aplikace se tedy spustí a když ji chcete "mutlitasknout", předá do API požadavky, kdy se má znovu zavolat (například u IM programu se má znovu zavolat, až přijde zpráva na port) a uklidí se z paměti. A protože visí v API, iOS vám ji mazaně ukazuje, jako žijící aplikaci, ačkoliv se celý IM program uklidil a neběží, kromě toho, že je registrovaný do chráněných procesů systému. Elegantní věc, které si vývojář většinou ani nevšimne. Až nastane událost, přijde vám na kecálek zpráva, API se mrkne, pro jaký program ta zpráva je (to mu řekla aplikace při uklízení), ten zavolá s patřičnými parametry a IM aplikace se obnoví i s oknem, že vám přišla zpráva. A vy si pořád myslíte, že se někde něco multitaskuje. Kulový kulový. Skutečný multitasking je v iOS vyhrazen jen některým aplikacím.</p>


<p>No a co to má společného s dashboardem? Aby dashboard fungoval, musel by viset na pozadí v multitasku a aktualizovat události na základní obrazovce podle toho, co se právě stalo. Čímž by systém předal vládu nad zdroji neznámé aplikaci, kterou může kdokoliv zbastlit podle svého. A nejde o grafický vzhled, jde o zdroje. Blbě naprogramovaný dashboard, který se bude příliš často aktualizovat, bude náročný jak na baterku, tak na výkon procesoru. A že by dobře naprogramovaný dashboard zkrátil životnost baterky spíše o jednotky procent, než o desítky? To je první věc, kterou se iOS konstruktéři naučili: procenta jsou hodně, únosná jsou až promile. Dejte procento k procentu a baterka je prázdná za půl dne, což je přesně to, co je nežádoucí.</p>


<p>Až budete přemýšlet o nějakém "monopolistickém omezení", které iOS předkládá, vysvětlení zpravidla bude jednoduché: jde buďto o snížení nároků na odběr enegie, nebo na využití procesoru, nebo na obojí. Prioritou iOS zařízení je co nejvyšší výdrž a konstantní (=rychlá) uživatelská odezva. Že by to Apple mohl nechat na uživatelích, co si instalují? Ale prosím vás, to by dopadl jako Symbian a Android (i ten už se brání), které si uživatelé zaplevelí vším možným softwarem a pak se diví, že jim baterka zdechne ještě před večerem, ačkoliv když ten telefon kupovali, tak vydržela dva dny v kuse…</p>


<p>PS: Už minule jsem naznačoval, že v iOS 5 ze šlamastiky "není povolen dashboard" Apple solidně vybruslil Centrálou Notifikací. A hned se ozvaly hlasy, že tím zkopíroval notifikace od Androidu, protože je posadil do horního řádku. No, je to komentář založený na tom, že to vypadá podobně. Ale pod kapotou je to diametrálně jiná technologie, která umožní ledasco. To, že letadlo a rogalo vypadá podobně, ještě neznamená, že to poskytne stejnou službu a pro notifikace prostě jiné logické místo není, než horní stavový řádek, který už od iOS pravěku se pro oznámení používá.... Ale o tom snad někdy příště.</p>