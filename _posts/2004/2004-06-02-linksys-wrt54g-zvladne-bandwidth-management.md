---
ID: 1119
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/linksys-wrt54g-zvladne-bandwidth-management

  '
post_date: 2004-06-02 09:35:54
post_excerpt: ''
published: true
summary_points:
- Sveasoft vydal firmware pro Linksys WRT54G s řízením rychlosti uživatelů.
- Firmware se instaluje přes web administraci a přidává nové funkce.
- Nastavení rychlosti je shodné pro WiFi/LAN porty, lze penalizovat priority.
- Alternativy pro úpravu routerů zahrnují projekty EWRT a WiFi Box.
title: 'Linksys WRT54G zvládne bandwidth management

  '
---

<p>
Ptá se na to řada lidí dnes a denně - jak omezit rychlost lidí připojených přes WiFi nebo LAN a sdílejících jednu linku? Zatím bylo potřeba instalovat softwarový router na Linuxu, pokud jste se chtěli udržet v nějaké rozumné cenové relaci. Nyní je to o něco jednodušší. Firmička Sveasoft vydala vlastní firmware pro Linksys WRT54G, ve kterém se mimo řadu dalších zajímavých funkcí nachází i jednoduché, ale docela praktické řízení rychlosti připojených uživatelů. </p>

<div class="leftbox">
<img src="/wp-content/uploads/20040602-linksyswrt54.jpg" alt="Linksys WRT54G" width="170" height="120" /></div>
<p>
Nejdříve trocha omáčky okolo. O tom, že některé novější hardwarové routery lze hackovat a protože běží na Linuxu, instalovat si do nich i vlastní utility, jsem již dříve psal. Jenže zatím to bylo docela složité, protože se musely instalovat z Linuxu a kompilovat. Sveasoft přišla přímo s binární distribucí, kterou si jednoduše a prostě do svého routeru nahrajete přes web administraci, jak jste byli dosud zvyklí. A ona updatuje tu stávající administraci o řadu nových funkcí.</p>

<p>
Jak vypadá administrace řízení šířky pásma, vidíte na obrázku. </p>

<p>
<a href="/wp-content/uploads/20040602-linksys-bwmngmnt.gif" title="Linksys WRT54G administrace Sveasoft Satori 2.0.0.8.6" onclick="window.open('/wp-content/20040602-linksys-bwmngmnt.gif','Linksys WRT54G administrace Sveasoft Satori 2.0.0.8.6','width=616,height=789,directories=no,location=no,menubar=no,scrollbars=no,status=no,toolbar=no,resizable=no');return false">Linksys WRT54G administrace Sveasoft Satori 2.0.0.8.6</a></p>

<p>
Jak vidíte z obrázku, nastavování není zcela detailní, můžete nastavovat pouze shodnou rychlost pro všechny WiFi nebo LAN porty, nelze přidělit rozdílné rychlosti. Lze ale také penalizovat nižší prioritou určité porty (například 21 pro FTP) nebo netmasky. Pro základní zamezení toho, aby se lidi se kterými sdílíte na routeru linku přetahovali o přípojné pásmo, to bohatě postačí. </p>

<p>
Co dodat - patřičné firmware soubory si můžete stáhnout z <a href="ftp://ftp.sveasoft.com/pub">ftp://ftp.sveasoft.com/pub</a> - zde jsou jak binární tak ZIP verze, podle toho, zda dáváte přenost upgrade přes web nebo TFTP. Na této adrese <a href="http://www.sveasoft.com/modules/phpBB2/">najdete diskusní fórum</a>, tam vám ale budou radit pracovníci firmy po zaplacení 20 USD přes PayPal (který je pro platební karty z ČR nedostupný). A tady najdete <a href="http://sveasoft.cyberemail.org/">veškerou potřebnou dokumentaci</a>. </p>

<p>
Instalace u mne doma proběhla vcelku bez problémů, jen výslovně i já doporučuji neupdatovat při připojení přes WiFi, ale přes ethernet. Také bacha na to, že na webu nikde není čerstvý ETSI firmware, takže když něco zbuchne a budete přecházet na původný firmware Linksysu, stáhnete si z webu jen americkou verzi, čímž přijdete o jeden kanál. Žádná velká ztráta to ale není. Jak to funguje, jsem moc nevyzkoušel, protože jsem zrovna byl na routeru připojený sám, ale když jsem nastavil tok přes WiFi na 64/13 Kb/s, všechno se výrazně zpomalilo, rychlosti pro download odpovídali, upload jsem nezkoušel. Podrobnější <a href="http://members.cox.net/wrt54g/">návod k řízení rychlosti najdete zde</a> - pomůže vám zjištění, že pro rozchození řízení rychlosti musíte router rebootovat přes telnet - já než jsem na to přišel, tak jsem se divil, že to nechodí a nechodí... A pokud chcete ještě jednu blbou radu zdarma - tak si musíte ve web administraci telnet povolit, protože implicitně je zakázán. Pro zájemce o SSH je i to...</p>

<p>
Sveasoft má velkolepé plány - do dalších buildů svého firmware chystají i meshování, ačkoliv je možné, že další úpravy půjdou až na Linksys WRT54GS - to má dvojnásobnou paměť a dá se tam páchat více nepravostí. Do starého routeru ale prý ještě zvládnou napasovat software pro hotspoty, takže by člověk při prvním přihlášení přes WiFi byl přesměrován na titulní stránku, kde by o sobě vyplnil nějaké údaje a ty se uložily do routeru. Také chtěji rozdělit uživatele do skupin, které budou mít rozdílné rychlosti. Prostě paráda - na to, že jde o levný router s maličkým odběrem a nulovým hlukem a firmware hack je zadarmo, je to skvělá příležitost pro one-man ISP a sdíleče konektivity!
</p>

<p>
Zapoměl jsem: v tomto firmware je k dispozici také WDS (to Linksys WRT54G normálně neumí) a možnost přepnout router jako klienta. </p>

<p>
Pokud chcete další pokusy, můžete se podívat na <a href="http://www.portless.net/ewrt/">projekt EWRT</a> - i tam je omezování šířky pásma (na bázi Wondershaper+iproute2) a login přes NoCatSplash. A další podobný <a href="http://wifi-box.sourceforge.net/">WiFi Box projekt</a> najdete na SourceForge.
</p>

<p>
Poznámka na závěr - uvedená úprava se zřejmě týká i dalších routerů postavených na čipové sadě BroadCom, tedy Linksys wrt54g,Linksys wrt54gs, Linksys wap54g, Belkin 7130, 
Belkin 7230, Motorola WR850G, Trendnet TEW-411BRP, Asus wl300g, Asus wl500g, Dell Truemobile2300, Buffalo Airstation, Ravotek W54-RT a Ravotek W54-AP. U nich jsem to ale nevyzkoušel.
</p>