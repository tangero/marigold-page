---
ID: 1488
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/bankovni-momentky-byl-tvurce-netbanky-pricetny

  '
post_date: 2005-01-24 08:09:00
post_excerpt: ''
published: true
summary_points:
- Fio banka neotevřela autorovi eBroker účet kvůli občanskému průkazu.
- Patria poskytla certifikát XETRA nejdříve na disketě, poté na CD.
- Živnobanka (UniCredit) má problémy s funkčností internetového bankovnictví Netbanka.
- Netbanka vyžaduje specifickou verzi JVM a má problémy s registrací certifikátu.
title: Bankovní momentky -  byl tvůrce NetBanky příčetný?
---

<p>Měl jsem tři bankovní momentky v průběhu minulého týdne, které na mne zanechaly nesmazatelné stopy. Tak zaprvé jsem se rozhodl otevřít si <a href="http://www.e-broker.cz/">eBroker </a> účet u Fio, protože jsem potřeboval nakoupit nějaké akcie na XETRA, německé burze - a to mi můj účet u Ameritrade neumožňuje. Myslel jsem, že to vyřídím, jak češi říkají, ajn-cvaj. Vyřídil. Naklusal jsem do Fio, vystál jsem si frontičku, dal jsem slečně občanku, úlisně pravil, že chci otevřít eBroker účet a ona popatřila na občanku s ustříhlým rohem a přilepeným papírem, že jsem ženat. A děla, že s tímto mi neotevře ničeho, ledaže dveře. I byl jsem hotov, jak češi říkají, ajn-cvaj. A taky jsem pochopil, proč mi PH v prosinci dával přednášku o tom, že svatba je jen obrovské bumážkování a jinak nic. </p>

<p>Abych se nějak na Xetru dostal, rozhodl jsem se obnovit svůj certifikát u Patrie, kde xetru také zavedli a kde účet otevřený mám, takže mi nemohou dělat nohy za občanku. Dorazil jsem do Patrie, slečna mne usadila do kožené klubovky, přinesla obálku s certifikátem a já se díval na černý plastový čtvereček se stříbrným plíškem. &#8220;To je co&#8221;, otázal jsem se. &#8220;Disketa,&#8221; pravila slečna. Ojé - a jakpak já ji dostanu do notebooku, který disketovou jednotku nikdy neviděl? Slečna pochopila, že s disketou u mne neuspěje a kamsi odspěchala. Za pět minut mi přinesla certifikát na CDčku a bylo všechno vyřešeno. Fio příšlo o zákazníka, k Patrii se jeden vrátil. </p>

<p>V neděli jsme si doma dali pokračování certifikátového šílenství. Tentokráte s Netbankou, internetovým bankovnictvím Živnobanky. Živnobanku jsem jako instituci míval rád, vždycky když jsem něco vyjednával Na příkopech, živě jsem viděl pana Petscheka (rok to osmatřicátý), kterak s Jaroslavem Preissem dojednává odprodej svých dolů a panové Kolben a Škoda s tímtéž krytí svých exportních zakázek. Ta doba je už bohužel pryč a Živnobanku koupila italská UniCredito (jak <a href="http://www.netmag.cz/db/L20031004143723.zbynek.html">ZP kdysi vhodně poznamenal, UniKretyno</a>). Namísto modrožlutého majáku je červená tečka, <a href="http://akabelog.blogspot.com/2005/01/tahle-banka-bt-dobr-banka.html">jazykově nesmyslná meníčka</a> a opruz. </p>

<p>Opruz v tom, že už přes půl roku se snažíme rozchodit Netbanku. Po dvou letech fungování prostě přestala fungovat a házela prázdnou stránku. Nakonec jsem kvůli tomu přeinstaloval celý počítač a do Netbanky jsem se dostal. Až na problém, že nešlo registrovat podpisový certifikát, takže jsme jenom viděli, že v bance máme peníze, dělat se s nimi nic nedá. </p>

<p>O víkendu jsem pokračoval v dalším kole, protože přes týden jsem načerpal v mnoha konfereních řadu zkušeností a vygoogloval podstatnou informaci, že Netbanka VYŽADUJE jednu jedinou konkrétní verzi JVM. A že tvůrce Netbanky jaksi přehlédl, že existuje Win XP SP2, kde je řada věcí jinak, než v SP1. A neřkuli, přehlédl i fakt, že JVM je již v mnoha novějších verzích, jenže v žádné jiné, než té 1.3.1, Netbanka nefunguje. Přeinstaloval jsem JVM na kýženou verzi, provedl pár úprav v SP2, restartoval a nahrál Netbanku. Propracoval jsem se až k registraci certifikátu. Zaregistroval jsem ho, aplikace ohlásila Pokusil jste se registrovat certifikát a konec. Po dalších hodinách informování se se ukázalo, že vyexpirovalo nějaké dočasné heslo a že musíme celý proces s vyžádáním nových hesel (poštou) opakovat. No super. Navrhoval Netbanku někdo příčetný?
</p>