---
ID: 1313
author: Michal Krsek
layout: post
oldlink: 'https://www.marigold.cz/item/story-o-sousedskych-sitich-11

  '
post_date: 2004-09-13 08:30:00
post_excerpt: ''
published: true
summary_points:
- Směrovač Duron 700 Mhz nahrazen Celeronem 450 Mhz za méně než 4000 Kč.
- Nízká rychlost internetu bude řešena navýšením kapacity ze strany skorotchána.
- Konfigurace OSPF provedena, dynamické směrování funkční, připraveno na zakruhování
  topologie.
- ČD-Telekomunikace nabízí metalickou trasu pro páteřní síť, řeší se kvalita a zdroje.
title: Story o sousedských sítích (11.)
---

<p>
Během soboty se mi podařilo nahradit v roli směrovače skvělý Duron 700 Mhz novým Celeronem 450 Mhz, který sice nemá (tak) oslnivou pracovní frekvenci, ale zase vydrží pod střechou bez zasekávání (což kvituje s pověkem především skorotchán). Provedl jsem vyúčtování základní sestavy (bez věcí, které dělají APčko), které vyšlo na méně než 4.000 kaček (včetně DPH). Pochopitelně jsem neúčtoval vložený čas <img alt="" src="http://www.marigold.cz/nucleus/plugins/wysiwyg/editor/images/smiley/msn/regular_smile.gif"/>.</p>
<p>
Objevil se jiný problém a tím je nízká rychlost do Internetu. Tu nechám řešit skortchána zaplacením větší kapacity (rychlosti) do Internetu. Sobotní práce byla navíc komplikovaná tím, že poblíž byl proveden úspěšný útok na směrovač, přičemž duchovní vůdce byl mimo lokalitu (takže v sobotu jsme měli až do šesti s Internetem utrum). Předpokládám, že při nejbližší příležitosti se pokusíme vytipovat kritická místa infrastruktury a nějak je zalepíme.</p>
<p>
Na své straně jsem provedl konfiguraci ospf (pár kliknutí v grafické vzdálené konzoli mikrotiku) už v sobotu, v neděli udělal svou část práce také duchovní vůdce a teď již spokojeně směrujeme dynamicky a jsme připraveni na zakruhování topologie. Doufám, že další duchovní vůdce (další obce) bude připraven ještě dříve, než namrznou střechy.</p>
<p>
V lokalitě jedna, která se stala teď prioritou, je třeba namontovat anténu na střechu, nakonektovat kabel a připojit se k nějakému AP v dosahu. První část musí udělat sami, pak uvidíme, co s druhou atřetí částí.</p>
<p>
O lokalitě tři jsem vedl zajímavý hovor s člověkem z ČD-Telekomunikace. Podle mapy, kterou jsem dostal, prochází obcí a třemi osadami metalická trasa. Je otázkou, zda by nebylo možné tuto trasu (například po osazení S/VDSL modemy) použít jako páteřní síť. Je otázkou, zda to vůbec kvalita vedení umožňuje, stejně tak, kde na to vzít zdroje. Jako optimální se jeví použít zdrojů ze strukturálních fondů EU, nicméně stále zůstává k řešení první problém získat nadkritický počet uživatelů.</p>
<p>
<strong>Update</strong> (neděle večer): Asi hodinu po napsání článku jsem zjistil, že lokalita dvě je bez konektivity. Po chvíli pátrání jsme přišli na to, že původní konfigurace ospf je chybná (na mojí straně, jak jinak). Nícméně jsem získal přístup z Internetu do CZFree.Netu (i když to večer lezlo jak připojení pro celou univerzitu linkou 19.21 Kb/s v Plzni v roce 1992) a po nakonfigrování se to rozeběhlo. Jako smutná legrace mi přijde, že rozšíření dotyčné sítě prostřednictvím ospf trvalo přes tři směrovače více než 15 minut (kdyby takhle fungoval Internet, bylo by to fakt špatný).</p>