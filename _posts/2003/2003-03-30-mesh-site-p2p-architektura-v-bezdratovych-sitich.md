---
ID: 1071
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/mesh-site-p2p-architektura-v-bezdratovych-sitich

  '
post_date: 2003-03-30 20:08:00
post_excerpt: ''
published: true
summary_points:
- Mesh sítě jsou P2P sítě aplikované do bezdrátového světa, kde si zařízení jsou rovna.
- Mobilní síť je příklad, kde mesh adaptéry předávají signál mezi sebou.
- Vojenské využití bylo prvopočátkem mesh sítí, kde tanky distribuovaly data.
- Zastupitelnost, úspora pásma, nízké náklady a zvýšení dosahu jsou výhody mesh sítí.
title: Mesh sítě &#8211; P2P architektura v&nbsp;bezdrátových sítích
---

O mesh sítích jsme se tu již několikrát zmiňovali a slíbil jsem článek o tom, co je to zač. Takže tu je - mesh sítě jsou vlastně sítě typu peer to peer. A to v bezdrátových sítích není vůbec samozřejmostí.<!--more--><p>
Mesh sítě jsou u nás zatím málo známý pojem, přitom jde o velmi zajímavý fenomén. Zda tento fenomén dojde praktického uplatnění (a ziskovosti), teprve uvidíme. Přesto stojí za to říci si o něm více.</p>

<p>
Mesh sítě <STRONG>jsou aplikací P2P sítí do bezdrátového světa</STRONG>. Zatímco klasická bezdrátová síť je vystavěna tak, že k access pointu se uživatelé připojují klientským adaptérem, mesh síť tento rozdíl stírá. V mesh síti nejsou access pointy (pánové) ani klienti (sluhové) &#8211; v mesh síti jsou si zařízení rovna (proto taky spojení peer-to-peer) a libovolné mesh síťové zařízení je schopné poskytnout stejnou sadu služeb, jako jakékoliv jiné zařízení kdekoliv. 
<p>
Pokud chcete <STRONG>praktický příklad, ukážeme si to na mobilní síti</STRONG>. V mobilní síti máte základnovou stanici BTS a k ní je připojený mobilní terminál. Každý mobil, který chce volat, musí být v dosahu BTS. V mesh síti si signál mezi sebou předávají jednotlivé mesh adaptéry, takže k tomu, abyste se připojil do internetu, stačí připojit se k mesh adapteru, jenž má připojení do internetu &#8211; a to klidně i přes jiné mesh adaptery &#8211; vůbec nemusíte být v oblasti pokryté tím připojeným adaptérem, stačí mít možnost přes ostatní mesh adaptéry k tomu cílovému adaptéru &#8222;dohopsat&#8220;. 
<P align=center><A href="/wp-content/uploads/meshsite.jpg" target=_blank><IMG alt="Mesh sítě" src="/wp-content/uploads/meshsite.jpg" width=400 align=center border=1></A></p>

<p>
Mesh sítě jsou tedy založeny na takzvaném <EM>&#8222;ad hoc peer to peer routingu&#8220;</EM> &#8211; na směřování provozu mezi rovnocennými adaptéry podle potřeby. </p>

<p>
Asi nepřekvapí, že prvopočátky mesh sítí jsou ve <STRONG>vojenském využití</STRONG>. Už v osmdesátých letech se ukázalo, že je výhodnější, když spojení tanků s velitelstvím a leteckými podpůrnými prostředky zprostředkovává jeden tank distribuující data a signál mezi ostatní tanky &#8211; a přitom ho kterýkoliv z tanků může nahradit. Aktualizace dat mezi palubními počítači letadel, tanků a vrtulníků probíhá tak, že ji zachytí jedno letadlo a distribuuje ji do letadel ostatních. Tímto systémem se podařilo prodloužit dosah takové distribuce signálu, protože bojová technika si data mezi sebou &#8222;předávala&#8220;. 
<p>
Podobná idea se objevila u zařízení bluetooth a Ericsson se ji pokoušel rozvinout i do mobilních sítí a jak to tak vypadá, v prvotních náčrtcích systémů 5G by mohl uspět. Jenže zatím se nepostavily ani sítě 3G... ostatně podrobněji jsem o této koncepci psal kdysi na Mobil.cz zde <A href="http://www.mobil.cz/publicistika/zpravy-publicistika/peertopeergsm010424.html">a je první díl </A>a zde <A href="http://www.mobil.cz/publicistika/peertopeerII010425.html">díl druhý</A>. 
<p>
U bezdrátových sítí se &#8222;mešování&#8220; ujímá především u WiFi, kde také dává značný smysl. Mnoho zařízení připojených do WiFi sítě potřebuje relativně malou šířku pásma, ale nenachází se v dosahu sítě. Mešování signálu z jednoho zařízení na druhé až do internetu je tedy velmi zajímavá funkce. 
<p>
<STRONG>Mesh sítě mají své výhody:</STRONG></p>

<OL>
<LI><STRONG>zastupitelnost</STRONG> &#8211; při výpadku (nebo zničení) jednoho prvku mesh sítě ho může jakýkoliv jiný prvek nahradit.&#160;</LI>
<LI><STRONG>Úsporu pásma</STRONG> &#8211; v mesh sítích je potřeba méně pásma. Na první pohled to vypadá nesmyslně, jenže je to tak &#8211; spojení v mesh síti se sestaví jen tehdy, když je potřeba a na dobu, po kterou je potřeba. V jiných sítích bývá sestavené celou dobu, co jsou zařízení zapojena, protože připojování a odpojování ručně řídí obsluha. </LI>
<LI><STRONG>Nízké náklady na výstavbu a údržbu</STRONG> &#8211; takový síť se jednoduše staví a jednoduše udržuje, protože o všechno základní nastavení se stará routovací protokol.&#160;</LI>
<LI><STRONG>Zvýšení dosahu sítě</STRONG> díky většímu počtu adaptérů, které mohou předávat signál </LI></OL>
<p>
Mesh sítě mají jako hlavní nevýhodu fakt, že <STRONG>routování v nich musí být velmi dobře promyšlené</STRONG>. Kromě toho jsou také náročnější na odběr energie, což může být u mobilních zařízení problém &#8211; nicméně to řeší fakt, že předávání signálu může být v economy módu vypnuto. 
<p>
Mesh sítě vypadají jako další zajímavé pokračování pro komunitní sítě. Komu by se to nelíbilo, místo složité instalace nejrůznějších routovacích protokolů koupit krabičku vypadající jako dnešní access point a připojit se do velké sítě a tím ji ještě zvětšit. Však <IMG height=113 alt="Locustworld MeshAP" src="/wp-content/uploads/locustworld.jpg" width=150 align=right border=1>také do výzkumu mesh sítí investují velké firmy jako Intel, Mitsubishi nebo Cisco. A také firmy menší, jako <A href="http://www.meshnetworks.com/">MeshNetworks</A>&#160;<EM>(z jejich presentace je i obrázek, děkuji!)</EM>&#160;nebo <A href="http://www.locustworld.com/" target=_blank>LocustWorld</A>. Tyto posledně zmíněné firmy již svoje produkty dodávají &#8211; zatímco ta první je zaměřena spíše na velké projekty, produkt LocustWorld je zaměřen spíše na sítě komunitní a s cenou kolem 15 000 Kč nevypadá nijak nezajímavě. 
<p>
Většina takových projektů je založená na WiFi sítích (ačkoliv některé jsou univerzálně přenositelné na jakoukoliv bezdrátovou síť) a předpoklad je takový, že buďto máte mesh adaptér a pak můžete signál předávat i pro ostatní, nebo máte jen WiFi kartu bez mesh podpory a pak se můžete sice připojit přes jakékoliv zařízení v síti, sami ale signál předávat nemůžete. 
<p>
U <STRONG>LocustWorldu</STRONG> to funguje zajímavě. Kromě toho, že si zde můžete celé zařízení koupit, je také možné si sbastlit vlastní z vašich komponent a stáhnout si CD s veškerým software. Stačí mít libovolný počítač (alespoň pentium a CD by měl mít) s WiFi kartou &#8211; a máte svého meshe... Projekt vypadá sám o sobě velmi zajímavě, jen u nás s ním zřejmě nikdo neexperimentuje. 
<p>
Pro linuxáře jsou také informace na stránkách <A href="http://www.mitre.org/tech_transfer/mobilemesh/">projektu Mobile Mesh</A> - najdete tu i aplikace mesh routování. </p>