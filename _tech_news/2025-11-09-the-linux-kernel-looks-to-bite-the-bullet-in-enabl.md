---
author: Marisa Aigen
category: programování
companies:
- Microsoft
- GCC
- LLVM
- Clang
date: '2025-11-09 14:51:00'
description: Vývojáři Linuxového kernelu zvažují trvalé zapnutí přepínače -fms-extensions
  v GCC a Clang, což umožní použití vybraných rozšíření jazyka C z ekosystému Microsoftu
  a může ovlivnit styl, kompatibilitu a údržbu kernelového kódu.
importance: 3
layout: tech_news_article
original_title: The Linux Kernel Looks To "Bite The Bullet" In Enabling Microsoft
  C Extensions - Phoronix
publishedAt: '2025-11-09T14:51:00+00:00'
slug: the-linux-kernel-looks-to-bite-the-bullet-in-enabl
source:
  emoji: 📰
  id: null
  name: Phoronix
title: Linuxový kernel míří k povolení Microsoft C Extensions při kompilaci
url: https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext
urlToImage: https://www.phoronix.net/image.php?id=2025&image=ms_b
urlToImageBackup: https://www.phoronix.net/image.php?id=2025&image=ms_b
---

## Souhrn
Linuxový kernel se přibližuje rozhodnutí plošně povolit kompilátorový přepínač `-fms-extensions` v rámci svého build systému. Tento krok by umožnil využívat vybrané Microsoft C Extensions při kompilaci kernelu pomocí GCC i LLVM/Clang a otevřel prostor pro odlišný, potenciálně úspornější a čitelnější způsob práce se strukturami v jaderném kódu.

## Klíčové body
- Větve `kbuild-next` nově obsahují dvě záplaty, které zapínají `-fms-extensions` globálně pro kompilaci kernelu.
- Cílem je umožnit využití specifických konstrukcí Microsoft C, zejména anonymního vkládání strukturovaných typů (struct/union) s tagy.
- Změna je pravděpodobně zamýšlena pro Linux 6.19, pokud nebudou zásadní námitky od klíčových vývojářů nebo Linuse Torvaldse.
- Argumenty pro zahrnují „hezčí“ a kompaktnější kód, potenciální úsporu zásobníkové paměti a sjednocení chování mezi kompilátory.
- Kritickou otázkou je dlouhodobý dopad na přenositelnost, závislost na ne-standardních rozšířeních a stabilitu ekosystému kernelu.

## Podrobnosti
Rozšíření Microsoft C Extensions, aktivovaná volbou `-fms-extensions`, umožňují kompilátorům jako GCC a LLVM/Clang podporovat určité nestandardní konstrukce jazyka C, původně zavedené v Microsoft Visual C/C++. Jde například o specifické způsoby práce se strukturovanými typy, uniemi či anonymními členy, které nejsou plně v souladu se standardem C, ale v praxi zjednodušují zápis některých datových struktur.

V kontextu Linuxového kernelu je hlavním praktickým přínosem možnost anonymně vkládat „označené“ (tagged) struktury a unie do jiných struktur bez nutnosti obalových členů. To vede k přímočařejšímu přístupu k polím těchto vnořených typů, což může zjednodušit definice komplexních datových struktur používaných v podsystémech kernelu, jako jsou plánovač, síťový stack, ovladače nebo subsystémy správy paměti.

Historicky se návrhy na globální povolení `-fms-extensions` opakovaně objevovaly, ale končily na mailing listu s tím, že přínos není dostatečný vzhledem k přidání dalšího nestandardního prvku do build procesu. Tentokrát však návrh postoupil do větve `kbuild-next`, což je pracovní větev pro změny v build systému kernelu. To znamená, že pokud v následující fázi nepřijdou zásadní námitky, změna může být součástí vydání Linux 6.19.

Rasmus Villemoes a další vývojáři argumentují, že jednotlivé případy, kde by `-fms-extensions` pomohly, byly dosud posuzovány izolovaně a vždy považovány za „ne dost důležité“ na přidání nového přepínače. Tento přístup ale vytváří takzvaný „chicken-and-egg“ problém: bez aktivovaného přepínače se vývojáři těmto konstrukcím vyhýbají, a tudíž se nikdy neukáže kumulativní přínos. Globální povolení má tento blok odstranit a umožnit postupnou evoluci kódu.

Současně je nutné počítat s technickými riziky. Kernel je extrémně přenositelný projekt běžící na široké škále architektur a kompilátorů. Závislost na chování specifickém pro Microsoft C Extensions může zkomplikovat budoucí podporu alternativních nástrojových řetězců, zvýšit bariéru vstupu pro nové platformy a vystavit vývojáře jemným neslučitelným detailům mezi implementacemi kompilátorů. Proto lze očekávat detailní diskusi nad tím, které konkrétní prvky rozšíření budou v praxi využívány a jak omezit možnost jejich zneužití.

## Proč je to důležité
Tento krok je důležitý primárně pro vývojářský a systémový ekosystém kolem Linuxového kernelu, nikoli jako okamžitá změna pro koncové uživatele. Pokud dojde k trvalému přijetí `-fms-extensions`, kernelový kód se může postupně opřít o nestandardní vlastnosti jazyka C, což ovlivní:

- Přenositelnost: kompilace kernelu bude ještě více vázána na konkrétní chování GCC a Clang s podporou Microsoft C Extensions. Alternativní či experimentální kompilátory mohou mít problém držet krok.
- Údržbu kódu: jednodušší a kompaktnější datové struktury mohou zlepšit čitelnost pro zkušené vývojáře, ale zároveň zvýší komplexitu pro ty, kteří očekávají čistě standardní C.
- Ekosystém nástrojů: nástroje pro analýzu kódu, formální verifikaci či statickou analýzu budou muset správně rozumět těmto rozšířením, aby nedocházelo k falešným chybám nebo přehlédnutí skutečných problémů.

Celkově nejde o průlomový milník, ale o významnější posun v filozofii vývoje kernelu: pragmatické přijetí nestandardních jazykových rozšíření výměnou za konkrétní vývojářské a technické výhody. Pro profesionály v oblasti systémového programování je to signál, že Linux kernel může být do budoucna méně puristický a více ochotný využívat rozšíření definovaná praxí, nikoli pouze standardem.

---

[Číst původní článek](https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext)

**Zdroj:** 📰 Phoronix
