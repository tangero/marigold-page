---
ID: 3870
author: Patrick Zandl
layout: post
post_date: 2017-11-19 10:40:41
post_excerpt: ''
published: true
summary_points:
- Přechod z Androidu na iOS způsobuje problémy s krypto peněženkami, např. Mycelium.
- Mobilní peněženky na iOS mají nedostatky v transakčních poplatcích a funkcích.
- Bezpečnost mobilních peněženek je problematická, doporučuje se hardwarová peněženka.
- Doporučené mobilní peněženky pro iOS jsou Bread wallet a Airbitz, Mycelium se nedoporučuje.
title: Běžné potíže s peněženkami pro kryptoměny
---

<p>Nikdy před tím mě to nebralo. Skladování větších kryptočástek jsem nechal na cold wallet, případně zkušeným kolegům, na menší jsem prostě měl aplikaci v mobilu. Jenže pak jsem přešel z Androida zpět na iOS a znervózněl jsem. </p>


<!--more-->

<p>Víte, jak se vždycky říká, že těch dvanáct slov vám obnoví peněženku? Ono to funguje dobře. Jenže ne vždycky, ne všude a ne úplně. Tak například ta Mycelium peněženka - z Androidu na iOS software té samé firmy, tam to nefunguje. Nevidíte ani zůstatek, ani transakce. Googlováním zjistíte, že je to známá chyba, s níž se nic neděje. To samé při převodu na další peněženky. Nakonec se to dá spolehlivě rozchodit jen málokde a nejlepší řešení je z Mycelia utéct. Bohužel tím, jak je bitcoinový svět dost rozkolísaný, není moc jiných řešení.</p>

<p>Existuje celá řada vypulírovaných bitcoinových peněženek na iOS, jenže nestíhají vývoj. Nestíhají třeba nastavení poplatku za transakci, takže v dnešní době převádějí peníze jen za draho, neumí třeba alternativní měny, které jsou vhodné pro běžné užití (v tom se chytá Litecoin třeba). A často nemají jiné forky Bitcoinu jako Cash - což nevadí každému, ale výběr to může zúžit.</p>

<p>Z hlediska bezpečnosti jsem si říkal, že by bylo zajímavé podívat se na hardwarovou peněženku. Sympatický český Trezor právě představil novou verzi, bohužel se ještě neprodává a starou jsem chtěl. Takže jsem koupil Ledger Nano S. Bohužel to ukazuje většinu nevýhod, jaké lze od takového produktu čekat. Peněženka nefunguje samostatně bez počítače (leda s mobilem a mimochodem v českém app store nemá přístupnou aplikaci), nefunguje to bez aplikace použitelné jen přes Chrome/Chromium. Jestli jste si mysleli, že Ledgerem bezpečně zaplatíte i přes počítač, který plně neovládáte (třeba v internetové kavárně), tak na to asi můžete zapomenout.</p>

<p>Pro běžného uživatele je to stále těžké a matoucí. Použitelnost mobilních peněženek na iOS pokročila, ale tím se zase vytratila variabilita. Například většina peněženek neumí vymazat privátní klíč, abyste mobilní peněženku mohli používat jen pro prohlížení operací. Zejména u Bitcoinu, kde jsou stále dost vysoké transakční poplatky a používáte je jen pro větší platby, to pro řadu lidí má z pohledu bezpečnosti smysl, autorizaci dělají na počítači. Je to dobré tehdy, pokud peněženka umí více oddělených účtů, přičemž ten, na kterém máte větší množství prostředků, není běžně na mobilu určený k placení.</p>

<p>Na iOS doporučuju vykašlat se na dříve dost chybové Mycelium (nová verze to vylepšuje, ale stejně k ní nepanuje důvěra) a podívat se na Bread wallet (mám rád švýcary) nebo Airbitz, která má to hlavní: je deterministická/podporuje HD, <a href="https://en.bitcoin.it/wiki/Scalability#Simplified_payment_verification">SPV klienta</a> i bezpečnost přes TouchID. Pokud ovšem přecházíte z Mycelia na Androidu, prostě si peníze převeďte z androidí peněženky (klidně pomalu a za levno) do nové adresy. Jinak je to problematické.</p>

<p>Přitom oddělení kryptoměnové peněženky z počítače, který běžně používáte, má velký smysl. Je příliš snadno kompromitovatelný. Pro běžné použití je autorizace mobilem bezpečnější, jenže člověk implicitně nemá důvěru k tomu, že mobil neztratí. Záloha seedu je naprostou nutností, ale kdo ji dělá pořádně?</p>

<p>Samostatná hardware peněženka je dobrá věc, ale mají před sebou ještě dlouhou cestu. <a href="https://www.ledgerwallet.com">Ledger</a> táhne nižší cenou, ale je to výrazně osekaná věc. <a href="https://trezor.io">Trezor v nové verzi</a> neznám (hejhej, je to český, to bude dobrý!) a láká mě <a href="https://www.bitlox.com/">vyzkoušet BitLox</a>, který podle popisu by mohl být velmi zajímavý. Otázka je, jaký bude v praxi.</p>

<p>Jestli máte nějakou lepší zkušenost kolem peněženek s iOS, dejte vědět. Takový <a href="https://docs.google.com/document/d/1MJRW_rJ3D1JSOA8EX-AjPIky396cOp3ccA3X3yDBFhs/edit">fajn přehled peněženek je tady</a>. PS: O webových ani neuvažujte. </p>