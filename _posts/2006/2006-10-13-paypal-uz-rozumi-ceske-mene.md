---
ID: 2025
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/paypal-uz-rozumi-ceske-mene

  '
post_date: 2006-10-13 08:55:27
post_excerpt: ''
published: true
summary_points:
- PayPal nově plně podporuje českou korunu pro platby a převody.
- Přijímání CZK vyžaduje aktivaci měny v nastavení PayPal účtu.
- Kód měny pro platby v českých korunách přes PayPal je CZK.
- Poplatky pro příjemce na business účtu činí 10 Kč + 3,2 % z částky.
title: "PayPal už rozumí české měně"
---

<p>Včera pozdě v noci se PayPal stal plnohodnotným platebním systémem pro český internet. Po možnosti peníze přijímat totiž přidal i možnost pracovat s českou korunou (a pár dalšími měnami). Do té doby mohly převody probíhat v eurech, dolarech a pár dalších měnách. </p>

<p>Pokud chcete přijímat české koruny, musíte se přihlásit na svůj PayPal účet a přidat si v přehledu měn vedených k účtu českou korunu přes tlačítko Manage Currency. </p>

<p>Zřízení české měny je zdarma, stejně jako používání PayPalu. </p>

<p>Pokud provozujete obchod a chcete, aby vám lidé platily přes PayPal, nezapomínejte na to, že kód měny je CZK. Takže v URL musíte předávat currency_code s hodnotou CZK.</p>

<p>Příklad <a href="https://www.paypal.com/cgi-bin/webscr?cmd=p/sell/mc/mc_wa-outside">je zde</a>.</p>

<p>Tlačítko pro podporu serveru v Kč s přednastavenou platbou 50 Kč vypadá takto a můžete v klidu vyzkoušet :)</p>

	<form action="https://www.paypal.com/cgi-bin/webscr" method="post">
<input type="hidden" name="cmd" value="_xclick" />
<input type="hidden" name="business" value="patrick.zandl@marigold.cz" />
<input type="hidden" name="item_name" value="Marigold cesky" />
<input type="hidden" name="item_number" value="2" />
<input type="hidden" name="amount" value="50.00" />
<input type="hidden" name="no_shipping" value="2" />
<input type="hidden" name="no_note" value="1" />
<input type="hidden" name="currency_code" value="CZK" />
<input type="hidden" name="tax" value="0" />
<input type="hidden" name="lc" value="CZ" />
<input type="hidden" name="bn" value="PP-DonationsBF" />
<button type="submit" style="background: url(/wp-includes/20061019-pp.png); border: 0; width: 110px; height: 23px; font: bold 11px bold arial; line-height: 23px; cursor: hand;">Podpořte nás!</button>
</form>
<p>Posledním problémem Paypalu je fakt, že rozhraní není česky.
</p>

<p><strong>Update:</strong> Poplatky za převod jsou pro příjemce peněz na business account 10 Kč + 3,2% převáděné částky. V případě, že překročí obchodník určitou hranici, tak se ta procenta snižují.
</p>