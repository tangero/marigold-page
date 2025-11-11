---
author: Marisa Aigen
category: programování
companies:
- Microsoft
- GCC
- LLVM
- Clang
date: '2025-11-09 14:51:00'
description: Vývojáři Linuxového kernelu zvažují plošné zapnutí kompilátorové volby
  -fms-extensions, která umožní využití vybraných rozšíření jazyka C z prostředí Microsoftu
  pro úsporu paměti a zjednodušení kódu.
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
title: Linuxový kernel míří k plošnému povolení Microsoft C Extensions
url: https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext
urlToImage: https://www.phoronix.net/image.php?id=2025&image=ms_b
urlToImageBackup: https://www.phoronix.net/image.php?id=2025&image=ms_b
---

## Souhrn
Linuxový kernel se přibližuje k plošnému povolení přepínače -fms-extensions při kompilaci pomocí GCC a LLVM/Clang. Tento krok by umožnil využití vybraných Microsoft C Extensions uvnitř kernelového kódu, zejména anonymních vnořených struktur a unií, a mohl by přinést čistší kód a lepší práci s pamětí.

## Klíčové body
- Dva patche v kbuild-next navrhují globální zapnutí volby -fms-extensions pro kompilaci kernelu.
- Cílem je umožnit využití Microsoft C Extensions, zejména anonymních tagged struct/union uvnitř jiných struktur.
- Změna je plánována pro okno slučování Linux 6.19, pokud nenarazí na odpor klíčových vývojářů včetně Linuse Torvaldse.
- Dlouhodobě se diskutuje, zda přínosy „hezčího“ a efektivnějšího kódu vyváží závislost na dalším ne standardním kompilátorovém rozšíření.

## Podrobnosti
V experimentální větvi kbuild-next, která slouží jako přípravná základna pro změny v build systému Linuxového kernelu, se objevily dva patche navrhující globální povolení přepínače -fms-extensions pro všechny podporované kompilátory, konkrétně GCC a LLVM/Clang. Tento přepínač aktivuje Microsoft C Extensions, tedy sadu nestandardních jazykových konstrukcí původně podporovaných překladačem Microsoft Visual C/C++ a používaných v části ekosystému Windows.

Pro Linuxový kernel je v popředí zájmu především možnost vkládat pojmenované struktury (tagged struct) nebo unie do jiných struktur/unií anonymně, což zjednodušuje rozvržení datových struktur a přístup k jejich členům. Prakticky to může vést k přehlednějšímu kódu, eliminaci obalovacích polí a v některých případech k úspoře zásobníkové paměti i lepšímu zarovnání dat.

Myšlenka plošného povolení -fms-extensions není nová; v minulosti byla opakovaně navržena, ale nikdy nezískala konsenzus na mailing listu kernelu. Argumenty proti zahrnovaly zejména odpor k dalším nestandardním rozšířením, obavy z horší přenositelnosti, potenciální komplikace pro alternativní build nástroje a nástroje pro statickou analýzu a riziko postupného pronikání těžko přenositelných idiomů do kritické části kódu. Aktuální zařazení patchů do kbuild-next však naznačuje, že část maintainers začíná akceptovat pragmatický přístup: rozšíření je už dnes široce podporováno hlavními kompilátory a může ulevit od opakujících se konstrukcí, které jsou sice „snad snesitelné“, ale v součtu komplikují údržbu.

Pokud změna projde do Linuxu 6.19, vývojáři kernelu získají oficiálně podporovaný prostor pro využití vybraných Microsoft C konstrukcí, což může ovlivnit styl psaní subsystémů, ovladačů i architekturně specifického kódu.

## Proč je to důležité
Tento krok je významný především pro vývojáře a maintainer y Linuxového kernelu, nikoliv přímo pro běžné koncové uživatele. Odráží posun od striktního purismu jazyka C k pragmatickému využívání rozšíření, pokud jsou stabilně podporována vícero kompilátory. Plošné povolení -fms-extensions může:

- zjednodušit datové struktury v nízkoúrovňovém kódu a tím usnadnit jeho čitelnost a údržbu,
- přinést drobné optimalizace v práci s pamětí, což je důležité v jádře, ovladačích a na embedded platformách,
- zároveň ale zvýšit závislost na specifických kompilátorových vlastnostech, což může zkomplikovat práci alternativním nástrojům, formálním verifikačním metodám a menším projektům, které se snaží kernel analyzovat nebo překládat jinými prostředky.

Celkově jde o technicky zajímavý signál: Linuxový kernel je ochoten systematicky využít rozšíření historicky spojená s Microsoftím ekosystémem, pokud to přinese reálné benefity v kvalitě kódu, a současně si bude muset pohlídat, aby se tento krok nevymkl kontrole a neomezil dlouhodobou udržitelnost a přenositelnost projektu.

---

[Číst původní článek](https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext)

**Zdroj:** 📰 Phoronix
