---
category: kybernetická bezpečn
date: '2025-10-22 22:35:41'
description: Vývojáři nejpoužívanějšího DNS softwaru BIND odhalili dvě kritické zranitelnosti,
  které útočníkům umožňují podvrhnout DNS záznamy a přesměrovat uživatele na škodlivé
  stránky.
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
title: BIND varuje před chybami umožňujícími otrávení DNS cache
url: https://arstechnica.com/security/2025/10/bind-warns-of-bugs-that-could-bring-dns-cache-attack-back-from-the-dead/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/06/browser-security-threat-1152x627.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/06/browser-security-threat-1152x627.jpg
---

## Souhrn

Vývojáři BIND, nejrozšířenějšího softwaru pro překlad doménových jmen na internetu, varují před dvěma závažnými zranitelnostmi umožňujícími útok typu DNS cache poisoning. Chyby s označením CVE-2025-40778 a CVE-2025-40780 mají hodnocení závažnosti 8,6 z 10 a mohou útočníkům umožnit nahradit legitimní IP adresy škodlivými, čímž přesměrují uživatele na podvržené stránky.

## Klíčové body

- Dvě kritické zranitelnosti v BIND s hodnocením 8,6/10 umožňují otrávení DNS cache
- CVE-2025-40778 vznikla kvůli logické chybě, CVE-2025-40780 kvůli slabosti v generování pseudonáhodných čísel
- Podobné zranitelnosti odhaleny také v DNS resolveru Unbound (hodnocení 5,6/10)
- Útok připomína slavnou zranitelnost z roku 2008 odhalenou Danem Kaminským
- Záplaty pro všechny tři zranitelnosti jsou k dispozici od středy

## Podrobnosti

Zranitelnosti postihují DNS resolvery používané tisíci organizacemi po celém světě. BIND je dominantní software pro překlad doménových jmen na IP adresy, což je základní funkce internetu umožňující uživatelům navštěvovat webové stránky pomocí čitelných názvů místo číselných adres.

První zranitelnost (CVE-2025-40778) vznikla kvůli logické chybě v kódu, zatímco druhá (CVE-2025-40780) je způsobena nedostatečně kvalitním generátorem pseudonáhodných čísel. Obě umožňují útočníkům provést takzvaný DNS cache poisoning – útok, při kterém se do mezipaměti DNS resolveru vloží falešné záznamy. Když pak uživatel zadá například adresu banky, resolver mu místo správné IP adresy vrátí adresu kontrolovanou útočníkem.

Problém je obzvláště závažný, protože připomína historickou zranitelnost z roku 2008. Tehdy bezpečnostní výzkumník Dan Kaminsky odhalil kritickou chybu v DNS protokolu, která umožňovala masové útoky na uživatele internetu. Zranitelnost vznikla kvůli použití UDP paketů v DNS komunikaci – protože tyto pakety jsou jednosměrné, neexistoval způsob, jak ověřit identitu odesílatele pomocí hesel nebo jiných přihlašovacích údajů.

Po Kaminského odhalení proběhla koordinovaná celosvětová akce, při které tisíce poskytovatelů DNS služeb implementovaly opravy. Současné zranitelnosti však ukazují, že ochranné mechanismy zavedené po roce 2008 mohou být oslabeny.

Vývojáři konkurenčního DNS resolveru Unbound také varovali před podobnými zranitelnostmi nahlášenými stejnými výzkumníky, ačkoli s nižším hodnocením závažnosti 5,6.

## Proč je to důležité

DNS infrastruktura je kritickou součástí internetu a její kompromitace může mít devastující dopady. Úspěšný útok typu cache poisoning umožňuje útočníkům přesměrovat tisíce uživatelů na podvržené stránky, které jsou od originálu k nerozeznání. Uživatelé vidí správnou adresu v prohlížeči, ale ve skutečnosti komunikují se škodlivým serverem.

Také útoky mohou být využity pro krádež přihlašovacích údajů, distribuci malwaru nebo phishingové kampaně. Vzhledem k tomu, že BIND je nejpoužívanější DNS software na světě, potenciální dopad těchto zranitelností je enormní. Organizace provozující vlastní DNS resolvery by měly okamžitě aplikovat dostupné záplaty a ověřit, že jejich systémy nejsou zranitelné.

---

[Číst původní článek](https://arstechnica.com/security/2025/10/bind-warns-of-bugs-that-could-bring-dns-cache-attack-back-from-the-dead/)

**Zdroj:** 🔬 Ars Technica
