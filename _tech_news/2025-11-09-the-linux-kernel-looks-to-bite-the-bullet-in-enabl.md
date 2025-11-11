---
author: Marisa Aigen
category: linux kernel
companies:
- Microsoft
- GCC
- LLVM
- Clang
date: '2025-11-09 14:51:00'
description: Vývojáři Linuxového kernelu zvažují plošné zapnutí volby -fms-extensions
  v GCC a Clang, což by umožnilo využití vybraných Microsoft C Extensions pro jednodušší
  práci se strukturami a potenciálně úsporu paměti.
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
title: Linuxový kernel míří k plošnému povolení Microsoft C Extensions při kompilaci
url: https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext
urlToImage: https://www.phoronix.net/image.php?id=2025&image=ms_b
urlToImageBackup: https://www.phoronix.net/image.php?id=2025&image=ms_b
---

## Souhrn
Linuxový kernel směřuje k plošnému povolení přepínače `-fms-extensions` v rámci build systému, což umožní využití vybraných Microsoft C Extensions v GCC a LLVM/Clang. Změna je aktuálně v testovací větvi kbuild-next a pokud nebude vetována klíčovými maintainery nebo Linusem Torvaldsem, může se objevit v jádře Linuxu 6.19.

## Klíčové body
- Návrh povolit `-fms-extensions` globálně pro kompilaci kernelu v GCC i Clang.
- Hlavní motivací je možnost anonymního vkládání označených (tagged) struktur a unii do jiných struktur/unií.
- Očekává se čitelnější a kompaktnější kód, v některých případech i úspora zásobníkové paměti.
- Změna je po letech diskusí nově zařazena do kbuild-next, což zvyšuje šanci na skutečné nasazení.
- Stále existuje prostor pro odmítnutí v rámci merge window, pokud se objeví silné technické námitky.

## Podrobnosti
Kbuild-next, testovací větev build systému Linuxového kernelu, aktuálně obsahuje dvojici patchů, které zapínají kompilátorový přepínač `-fms-extensions` pro všechny konfigurace. Tento přepínač v překladačích GCC a LLVM/Clang zpřístupňuje podmnožinu rozšíření jazyka C používaných původně kompilátorem Microsoft Visual C/C++. Pro Linuxové jádro je klíčová konkrétní vlastnost: možnost vkládat označenou strukturu nebo unii (tagged struct/union) anonymně do jiné struktury/union tak, aby její členy bylo možné přistupovat přímo, bez další úrovně zanoření.

Dosud se vývoj kernelu těmto rozšířením záměrně vyhýbal a preferoval čistší, standardní C, i za cenu poněkud méně elegantního kódu. Návrhy na plošné povolení `-fms-extensions` se objevují řadu let, ale narážely na odpor kvůli obavám z rozbití kompatibility, zvýšení závislosti na nestandardních vlastnostech a komplikacím při údržbě. Aktuální krok – zařazení patchů do kbuild-next – naznačuje posun v postoji části komunity: Rasmus Villemoes a další argumentují, že v praxi existuje dost případů, kdy použití těchto rozšíření zjednoduší struktury, sníží duplicitní kód a v některých scénářích i šetří zásobníkovou paměť (stack space), což je relevantní zejména pro nízkoúrovňové subsystémy a omezená embedded prostředí.

Z technického pohledu nejde o přebírání celého proprietárního ekosystému Microsoftu, ale o pragmatické využití rozšíření, která jsou již implementována v hlavních open source kompilátorech. Rizikem zůstává potenciální uzamčení na specifické chování překladačů a ztížení statické analýzy, formálních verifikací či portování nástrojů, které očekávají čistě standardní C.

## Proč je to důležité
Případné přijetí tohoto kroku by znamenalo formální posun v filozofii vývoje Linuxového kernelu směrem k větší toleranci k nestandardním jazykovým prvkům, pokud přinášejí praktický užitek. Pro vývojáře kernelu to může znamenat:

- čitelnější a strukturovanější datové typy, které lépe odrážejí skutečné hierarchie bez zbytečných obalů,
- možnost úspory paměti a zjednodušení přístupu ke členům struktur v kritických částech kódu,
- ale také nutnost pečlivěji hlídat, aby se nešířila závislost na méně podporovaných nebo problematických částech Microsoft C Extensions.

V širším ekosystému je to signál, že jádro klíčového open source projektu je ochotné přijmout kompatibilitu s rozšířeními historicky spojenými s Microsoftem, pokud jsou dostupná v otevřených nástrojích jako GCC a Clang. To může usnadnit interoperabilitu s částmi kódu a hlavičkových souborů, které z těchto konstrukcí vycházejí, a současně otevírá debatu o hranici mezi pragmatismem a udržitelnou čistotou kódu v kritické infrastruktuře.

---

[Číst původní článek](https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext)

**Zdroj:** 📰 Phoronix
