---
ID: 1445
title: Chci bezdrátovou síť (6.2)
author: Noname
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/chci-bezdratovou-sit-6-2
published: true
post_date: 2004-12-15 10:10:00
---
<p>
Tento článek navazuje na <a href="/item/chci-bezdratovou-sit-6-1">předchozí kapitolu</a> a věnuje se detailně problematice pasivních retranslací. Část o aktivních bude následovat odpoledne</p>
<div class="rightbox">
<h5>Pasivní retranslace přesměrováním</h5>
<img src="/wp-content/uploads/cache/20041215-pasivretr1.gif" alt="Pasivní retranslace přesměrováním" width="250" height="158" /></div>
<h3>Pasivní retranslace</h3>
<p>
V předchozím části jsem psal, že pasivní retranslace využívá buď</p>

<ul>
<li>přesměrování signálu, nebo </li>
<li>odraz signálu. </li>
</ul>
<p>
Způsob řešení přesměrováním signálu je velmi jednoduchý — do bodů A i C dáte směrové antény, které nasměrujete na bod R. Do bodu R pak umístíte dvě antény, jedna bude směrovat na bod A, druhá na bod C, a tyto kabely prostě a jednoduše spojíte k sobě koaxiálním kabelem. Nic víc, nic míň.</p>

<!--more--><div class="rightbox">
<h5>Pasivní retranslace odrazem</h5>
<img src="/wp-content/uploads/cache/20041215-pasivretr2.gif" alt="Pasivní retranslace odrazem" width="250" height="156" /></div><p>
Řešení odrazem signálu je ještě jednodušší — svírají-li body A a C v bodě R malý úhel (řekněme &lt; 45%), můžeme do bodu R umístit odraznou desku a to tak, aby se signál z bodu A od této desky odrazil a podle zákona úhel dopadu = úhel odrazu, byl dále nasměrován do bodu C a vice-versa.</p>
<p>
Kdy použít řešení s pomocí přesměrování a kdy pomocí odrazu je složitější. V naprosté většině případů se používá řešení přesměrováním, odrazná plocha musí svírat malý úhel, respektive čím větší úhel svírá, tím větší musí být (protože tím méně plochy stojí v cestě signálu a tím méně signálu lze tedy odrazit). Plachta je také drahá, instalace složitější, vyžaduje větší místo budově atd. Jedinou odraznou desku, kterou znám je na budově hotelu Opatov (krásně viditelné z metra Opatov), zřejmě je to ale pro licencované pásmo a zde jsou zcela jiné kalkulace. Někdy se ale využívá místo odrazové desky přímo nějaká budova — prostě nasměrujete signál přímo na budovu a ten se od ní při troše štěstí odrazí v tom směru, který potřebujete, aby doputoval k cíli. Ovšem tady pozor, velmi často pak dochází k velkým změnám kvality signálu podle toho, zda je na této &#8220;odrazné budově&#8221; vlhká omítka po dešti, či jestli je sucho.</p>

<h5>Jaké jsou výhody a nevýhody a čím se liší pasivní retranslace oproti aktivní</h5>
<p>
Předně je třeba si uvědomit, že v bodě R není žádný prvek, který by signál zesiloval a &#8220;čistil&#8221;. Vyšlete-li z bodu A signál, je v bodě R zachycena anténou (či odražena panelem) jen velmi malá část signálu (např. 5%) a tato pak přeposlána dál na bod C, který zachytí opět např. 5% z těch původních 5% a tedy na protější stranu v tomto případě dorazí jen čtvrt procenta původně vyslaného signálu (nebo dvacetina signálu, který by dorazil, když by se jednalo jen o dvoubodový spoj A → R). Signál zároveň není znovu upraven aktivním prvkem a zbaven šumu, a tak se na vzdálenou anténu dostane šum jak z trasy A → R, tak z části R → C.</p>
<p>
Výhody pasivní retranslace jsou také zřejmé – na retranslačním místě nepotřebujete žádné prostory v technologické místnosti, temperované rozvaděče či elektrický proud a tak je možná instalace i na odlehlá místa typu strom, komín a podobně.</p>
<p>
Z toho vyplývá i <strong>kde a jak můžete pasivní retranslace využít</strong></p>

<ul>
<li><strong>pouze na krátké vzdálenosti</strong> (řekněme stovky metrů), </li>
<li>je třeba velmi velkých antén na všech bodech (a tedy je obtížné až nemožné dosáhnout splnění generální licence), optimální jsou plné paraboly (chytají i méně šumu), nejlevnější jsem našel na <a href="http://www.wifishop.cz/">WiFi Shopu</a> (<a href="http://www.wifishop.cz/inshop/scripts/set.asp?Level=81">již od 1730 Kč</a>), doporučoval bych ale používat antény větší než 20 dBi (a tedy <strong>jste na štíru s GL</strong>). </li>
<li>je prakticky nemožné udělat pasivní spoj s více než jednou retranslací, </li>
<li>ačkoliv se zdá, že nepřítomnost aktivního bodu může přinést úspory, nutnost použití větších antén, těžší správa atd. přináší větší náklady a pasivní retranslace tak bývá dražší, </li>
<li>pronajímáte-li si retranslační místo, potom často platíte podle velikosti zabrané plochy či velikosti antény a protože jsou antény či plachta podstatně větší než u aktivního řešení, můžete platit podstatně více, </li>
<li>na retranslačním bodě nemůžete vyvést Ethernet a není možné tak &#8220;platit&#8221; pronajímateli tím, že mu dáte Internet </li>
<li>retranslační bod by měl být čistě váš, protože je přenášen i šum, je složité dosáhnout jak dostatečného signálu, tak malého zašumění. </li>
<li>protože signál nezpracovává žádný aktivní prvek, je přenos malinko rychlejší </li>
<li>smysl to má tedy až na výjimky jen tehdy, <strong>když nemáte na retranslačním bodě elektřinu</strong> (stožár, komín atd.) a nebo když využíváte odrazu od nějakého sousedního baráku a nepotřebujete tak vlastně vůbec retranslační bod </li>
</ul>