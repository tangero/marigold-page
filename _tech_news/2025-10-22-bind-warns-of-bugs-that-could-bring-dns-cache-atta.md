---
category: kybernetická bezpečn
date: '2025-10-22 22:35:41'
description: Tvůrci nejpoužívanějšího DNS softwaru BIND odhalili dvě kritické zranitelnosti
  umožňující otrávení cache a přesměrování uživatelů na falešné stránky. Připomínají
  slavný Kaminsky útok z roku 2008.
importance: 4
layout: tech_news_article
original_title: BIND warns of bugs that could bring DNS cache attack back from the
  dead - Ars Technica
publishedAt: '2025-10-22T22:35:41+00:00'
slug: bind-warns-of-bugs-that-could-bring-dns-cache-atta
source:
  emoji: 🔬
  id: ars-technica
  name: Ars Technica
title: BIND varuje před chybami, které mohou oživit útoky na DNS cache
url: https://arstechnica.com/security/2025/10/bind-warns-of-bugs-that-could-bring-dns-cache-attack-back-from-the-dead/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/06/browser-security-threat-1152x627.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/06/browser-security-threat-1152x627.jpg
---

## Souhrn

Vývojáři BIND, nejrozšířenějšího softwaru pro překlad doménových jmen na internetu, varují před dvěma kritickými zranitelnostmi s hodnocením závažnosti 8,6 z 10. Chyby umožňují útočníkům otrávit celou cache DNS resolverů a přesměrovat uživatele na podvodné stránky, které jsou k nerozeznání od legitimních. Situace připomína slavný bezpečnostní problém objevený Danem Kaminským v roce 2008.

## Klíčové body

- Zranitelnosti CVE-2025-40778 a CVE-2025-40780 postihují BIND, software používaný tisíci organizacemi pro překlad DNS
- První chyba vznikla logickou chybou v kódu, druhá slabostí v generování pseudonáhodných čísel
- Podobné zranitelnosti (s hodnocením 5,6) byly objeveny i v konkurenčním DNS resolveru Unbound
- Útoky umožňují nahradit legitimní IP adresy (například 3.15.119.63 pro arstechnica.com) adresami kontrolovanými útočníky
- Záplaty pro všechny tři zranitelnosti byly vydány ve středu

## Podrobnosti

DNS (Domain Name System) funguje jako telefonní seznam internetu - překládá lidsky čitelná doménová jména na IP adresy, které počítače používají ke komunikaci. BIND je dominantním softwarem pro tuto úlohu a jeho zranitelnosti proto představují systémové riziko pro celý internet.

Obě nově objevené chyby umožňují takzvané otrávení DNS cache (cache poisoning). Útočník může zneužít těchto zranitelností k tomu, aby DNS resolver - server, který překládá doménová jména - uložil do své cache falešné záznamy. Když pak uživatelé zadají například adresu banky nebo e-mailové služby, resolver jim vrátí IP adresu kontrolovanou útočníkem místo legitimní adresy. Uživatelé se tak dostanou na podvodnou stránku, aniž by to poznali - v prohlížeči se zobrazí správná doména, ale obsah pochází z útočníkova serveru.

První zranitelnost (CVE-2025-40778) vznikla logickou chybou v implementaci, zatímco druhá (CVE-2025-40780) je způsobena nedostatečně kvalitním generátorem pseudonáhodných čísel. Problém je obzvláště závažný, protože DNS tradičně používá UDP protokol, který na rozdíl od TCP neposkytuje mechanismy pro ověřování identity komunikujících stran.

Situace připomíná rok 2008, kdy bezpečnostní výzkumník Dan Kaminsky odhalil fundamentální zranitelnost v DNS, která umožňovala právě tento typ útoku. Tehdy byla potřeba koordinovaná celosvětová akce tisíců poskytovatelů DNS služeb, výrobců prohlížečů a dalších aplikací, aby byla implementována obrana. Nové zranitelnosti potenciálně oslabují právě tyto obranné mechanismy zavedené po Kaminského odhalení.

## Proč je to důležité

DNS představuje kritickou infrastrukturu internetu a její kompromitace má dalekosáhlé důsledky. Na rozdíl od phishingových útoků, kde útočník musí přesvědčit oběť ke kliknutí na podezřelý odkaz, otrávení DNS cache postihuje všechny uživatele dané organizace automaticky. Administrátoři serverů používajících BIND nebo Unbound by měli okamžitě aplikovat vydané záplaty. Zranitelnost s hodnocením 8,6 patří mezi vysoce kritické a její zneužití by mohlo vést k rozsáhlým phishingovým kampaním, krádeži přihlašovacích údajů nebo šíření malwaru v dosud nevídaném měřítku.

---

[Číst původní článek](https://arstechnica.com/security/2025/10/bind-warns-of-bugs-that-could-bring-dns-cache-attack-back-from-the-dead/)

**Zdroj:** 🔬 Ars Technica
