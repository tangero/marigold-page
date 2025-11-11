---
author: Marisa Aigen
category: linux kernel
companies:
- Microsoft
- GCC
- LLVM
- Clang
date: '2025-11-09 14:51:00'
description: Do vývojové větve kbuild-next zamířily záplaty, které vynucují kompilaci
  Linux kernelu s volbou -fms-extensions pro GCC i LLVM/Clang. Tento krok má umožnit
  využití vybraných konstrukcí Microsoft C Extensions, zjednodušit práci se strukturami
  a potenciálně optimalizovat paměťové nároky, ale současně otevírá debatu o standardizaci
  a dlouhodobé údržbě kódu.
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
title: Linux kernel míří k plošnému povolení Microsoft C Extensions při kompilaci
url: https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext
urlToImage: https://www.phoronix.net/image.php?id=2025&image=ms_b
urlToImageBackup: https://www.phoronix.net/image.php?id=2025&image=ms_b
---

## Souhrn
Linux kernel se připravuje na plošné povolení Microsoft C Extensions pomocí kompilátorské volby `-fms-extensions` v rámci všech podporovaných překladačů (GCC, LLVM/Clang). Změna je aktuálně v kbuild-next a míří do merge okna pro Linux 6.19, čímž se otevírá cesta k využití některých nestandardních konstrukcí známých z prostředí Microsoft Visual C.

## Klíčové body
- Záplaty v kbuild-next povolují `-fms-extensions` pro celý Linux kernel build.
- Hlavní motivací je možnost používat anonymní vkládání „tagged“ struct/union a psát kompaktnější kód.
- Předchozí pokusy o zavedení této volby opakovaně narazily na odpor na mailing listu.
- Rozhodnutí se očekává v rámci merge okna pro Linux 6.19, klíčové slovo budou námitky hlavních maintainerů a Linuse Torvaldse.
- Krok vyvolává otázky ohledně závislosti na nestandardním chování kompilátorů a udržitelnosti kódu.

## Podrobnosti
Zveřejněné záplaty v rámci kbuild-next modifikují systém kompilace Linux kernelu tak, aby se globálně používala volba `-fms-extensions`. Tato volba v GCC i LLVM/Clang umožňuje podporu vybraných nestandardních konstrukcí jazyka C, které původně vycházejí z Microsoft Visual C. V praxi jde zejména o flexibilnější práci se strukturami a uniemi, například anonymní vkládání označených (tagged) struktur a unií do jiných struktur bez nutnosti mezivrstvy, což může zpřehlednit kód a mírně zlepšit rozložení dat v paměti.

Rasmus Villemoes a další vývojáři argumentují, že sjednocené povolení `-fms-extensions` odstraní opakované „workaroundy“, které jsou sice funkční, ale méně čitelné a někdy vedou k horšímu využití zásobníku či paměti. Dosavadní přístup byl konzervativní: pro každý konkrétní případ se volilo raději standardní C, než přidání další globální kompilátorské volby. To však vytvářelo typickou situaci „slepice a vejce“ – bez povolení rozšíření se jejich přínos neprokáže, a bez prokázaného přínosu se rozšíření nepovolí.

Zařazení do kbuild-next znamená, že změna je brána vážně a je technicky připravená pro širší testování. Rozhodující bude, zda hlavní maintainerská část komunity nebude považovat závislost na Microsoft C Extensions za riziko pro přenositelnost, čistotu kódu a možnost budoucího využití alternativních kompilátorů či nástrojů pro analýzu kódu. Pokud projde, stane se `-fms-extensions` de facto součástí oficiálního build prostředí Linux kernelu.

## Proč je to důležité
Plošné povolení Microsoft C Extensions v Linux kernelu je signál posunu v přístupu ke kompilátorům a jazykovým rozšířením. Na jedné straně může přinést praktičtější a úspornější zápis některých datových struktur, potenciálně lepší využití paměti a vyšší expresivitu pro maintainery subsystémů, kteří dnes musí kód ohýbat podle striktního standardu. Na straně druhé vytváří závislost na konkrétním nestandardním chování, které musí dlouhodobě konzistentně podporovat GCC i LLVM/Clang.

Pro průmysl a firmy, které udržují vlastní patche proti kernelu (například výrobci čipů, síťových karet nebo bezpečnostních modulů), to znamená nutnost přehodnotit build prostředí a nástroje pro statickou analýzu. Vzniká také otázka kompatibility s alternativními či specializovanými kompilátory, které `-fms-extensions` nepodporují nebo implementují jen částečně. Rozhodnutí proto není jen estetické; jde o technický kompromis mezi čistotou standardu a praktickými požadavky na vývoj rozsáhlého, dlouhodobě udržovaného systému, jakým Linux kernel je.

---

[Číst původní článek](https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext)

**Zdroj:** 📰 Phoronix
