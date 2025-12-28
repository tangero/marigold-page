---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Apple
date: '2025-12-27 18:30:53'
description: Apple vydal nouzové bezpečnostní aktualizace pro dvě zero-day zranitelnosti
  v WebKit, které byly aktivně exploitovány v sofistikovaných útocích na konkrétní
  jednotlivce. Uživatelům iPhonu a iPadu se doporučuje okamžitě aktualizovat zařízení.
importance: 5
layout: tech_news_article
original_title: Apple patches two zero-day flaws used in targeted attacks
publishedAt: '2025-12-27T18:30:53+00:00'
slug: apple-patches-two-zero-day-flaws-used-in-targeted-
source:
  emoji: 📰
  id: fox-news
  name: Fox News
title: Apple opravuje dvě zero-day zranitelnosti využívané v cílených útocích
url: https://www.foxnews.com/tech/apple-patches-two-zero-day-flaws-used-targeted-attacks
urlToImage: https://static.foxnews.com/foxnews.com/content/uploads/2025/11/apple-store-new-york-city-iphone-sales.jpg
urlToImageBackup: https://static.foxnews.com/foxnews.com/content/uploads/2025/11/apple-store-new-york-city-iphone-sales.jpg
---

## Souhrn
Apple vydal nouzové bezpečnostní záplaty pro dvě zero-day zranitelnosti v WebKit, renderovacím enginu používaném v Safari a všech prohlížečích na iOS. Tyto chyby byly aktivně využívány v extrémně sofistikovaných útocích na specifické jednotlivce, což naznačuje operace typu spyware. Riziko spočívá v možnosti spuštění libovolného kódu pouhým navštívením škodlivé webové stránky, a proto Apple naléhá na okamžitou aktualizaci.

## Klíčové body
- **CVE-2025-43529**: Zranitelnost typu use-after-free v WebKit, která umožňuje arbitrary code execution při zpracování škodlivého webového obsahu.
- **CVE-2025-14174**: Druhá zero-day chyba v WebKit, exploitovaná ve stejných útocích.
- Ovlivněné verze: iOS před verzí 26, včetně iPhonu a iPadu.
- Charakter útoků: Vysoce cílené na jednotlivce, ne masové kampaně.
- Doporučení: Okamžitá instalace aktualizací pro eliminaci rizik.

## Podrobnosti
Apple v bezpečnostním bulletinu potvrdil, že obě zranitelnosti byly zneužity v reálných útocích, které postihly pouze vybrané cíle. WebKit je jádrem pro vykreslování webového obsahu na iOS zařízeních – slouží nejen Safari, ale i všem třetím aplikacím s webovým rozhraním, jako jsou e-mailové klienty nebo sociální sítě. CVE-2025-43529 patří do kategorie use-after-free, což je chyba v řízení paměti: program uvolní paměťový blok, ale později se k němu znovu přistoupí, což útočník může zneužít k přepsání paměti a vložení vlastního kódu. Tím lze získat plný přístup k zařízení, instalovat spyware pro sledování komunikace, polohy nebo kamer.

Druhá chyba CVE-2025-14174 není v poskytnutých informacích podrobně specifikována, ale Apple ji spojuje se stejnou vlnou útoků. Tyto exploity fungovaly na verzích iOS vydaných před iOS 26, což zahrnuje širokou škálu zařízení od starších iPhonů po nejnovější modely. Útoky nevyžadovaly žádnou interakci uživatele mimo navštívení stránky, což je typické pro zero-click exploity. Apple tyto incidenty označil za „extrémně sofistikované“, což odpovídá profilu státních aktérů nebo specializovaných skupin, jako ty za Pegasus spyware od NSO Group. Firma neidentifikovala útočníky ani oběti, ale omezený rozsah vylučuje masové kampaně jako ransomware.

Aktualizace jsou dostupné přes Nastavení > Obecné > Aktualizace software. Pro podnikové prostředí Apple poskytuje podrobné informace v security bulletin, včetně hashů souborů pro ověření integrity. Uživatelé by měli zároveň zvážit další opatření: vyhnout se podezřelým odkazům, používat VPN na veřejných sítích a aktivovat Lockdown Mode, který omezuje rizikové funkce WebKit pro vysoce ohrožené osoby jako novináři nebo aktivisté.

## Proč je to důležité
Tato událost podtrhuje pokračující zranitelnost uzavřeného ekosystému Apple vůči zero-day útokům, přestože firma investuje miliardy do bezpečnosti. I když útoky cílí na elitu, demonstrují schopnost překonat sandboxing a just-in-time kompilaci WebKit, což může inspirovat širší kampaně. V širším kontextu kyberbezpečnosti to signalizuje eskalaci spyware operací, kde státní aktéři obcházejí obchodní omezení Wassenaarovy dohody. Pro uživatele znamená nutnost pravidelných aktualizací – oneskorení i o dny zvyšuje riziko. Průmysl to nutí k rychlejší detekci zero-day v renderovacích enginech, protože WebKit ovlivňuje stovky milionů zařízení a slouží jako vstupní brána pro další exploity v appkách.

---

[Číst původní článek](https://www.foxnews.com/tech/apple-patches-two-zero-day-flaws-used-targeted-attacks)

**Zdroj:** 📰 Fox News
