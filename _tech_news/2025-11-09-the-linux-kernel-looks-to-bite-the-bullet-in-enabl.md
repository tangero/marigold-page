---
author: Marisa Aigen
category: programování
companies:
- Microsoft
date: '2025-11-09 14:51:00'
description: Vývojáři Linuxového jádra zvažují trvalé zapnutí přepínače -fms-extensions
  v kbuild, což by umožnilo používat Microsoft C Extensions při kompilaci kernelu
  s GCC i Clang a otevřelo cestu k úpravám stylu kódu i optimalizacím.
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
title: Linuxový kernel míří k povolení Microsoft C Extensions v celém build systému
url: https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext
urlToImage: https://www.phoronix.net/image.php?id=2025&image=ms_b
urlToImageBackup: https://www.phoronix.net/image.php?id=2025&image=ms_b
---

## Souhrn
Vývojový strom kbuild-next pro linuxové jádro obsahuje dva patche, které globálně zapínají volbu `-fms-extensions` pro GCC a LLVM/Clang. Tento krok by umožnil používat vybrané Microsoft C Extensions v kódu jádra, zejména anonymní vkládání označených struktur a unionů.

## Klíčové body
- Patch set v kbuild-next navrhuje globální povolení `-fms-extensions` pro celé jádro.
- Cílem je umožnit využití některých konstrukcí Microsoft C pro čitelnější a potenciálně úspornější kód.
- Změna se pravděpodobně zaměří na okno pro sloučení do Linuxu 6.19, pokud nebudou zásadní námitky.
- Diskuse trvá roky; dosud převažoval odpor k přidávání nestandardních rozšíření do build konfigurace.
- Rozhodnutí má dopady na konzistenci kódu, kompatibilitu překladačů i na dlouhodobou údržbu jádra.

## Podrobnosti
Navrhované patche v kbuild-next, což je vývojová větev build systému linuxového jádra, zapínají kompilátorový přepínač `-fms-extensions` pro všechny relevantní build cíle. Tento přepínač v GCC a LLVM/Clang aktivuje podporu vybraných nestandardních konstrukcí jazyka C/C++, které původně pocházejí z prostředí Microsoft Visual C/C++. V kontextu linuxového jádra se vývojáři zaměřují především na možnost anonymního vkládání „tagged“ struktur a unionů do jiných struktur/unionů. Prakticky to znamená, že některé datové struktury mohou být definovány kompaktněji a přístup k jejich členům může být přímější, aniž by se musely zavádět další vnořené názvy. To může vést k úspornějšímu, místy přehlednějšímu kódu a v některých případech i k menšímu využití zásobníku.

Historicky se návrhy na globální zapnutí `-fms-extensions` opakovaně objevovaly na mailing listu linuxového jádra, ale narážely na odpor z důvodu obav z roztříštěnosti jazyka, horší přenositelnosti a závislosti na specifických rozšířeních. Argumenty proti zahrnovaly zejména riziko, že se do jádra dostanou konstrukce, které nejsou standardizované a mohou se chovat odlišně mezi verzemi překladačů. Aktuální návrh však ukazuje posun: část vývojářů, včetně autorů patchů, tvrdí, že kumulativní přínos je vyšší než režie udržování „o něco ošklivějšího“ standardního kódu.

Pokud budou patche přijaty do Linuxu 6.19, oficiální build konfigurace jádra začne předpokládat konzistentní podporu Microsoft C Extensions v používaných verzích GCC a Clang. To je důležité i pro distributory, výrobce embedded zařízení a další, kteří kompilují kernel vlastními toolchainy – budou muset zajistit kompatibilitu s tímto nastavením.

## Proč je to důležité
Rozhodnutí globálně povolit `-fms-extensions` v linuxovém jádru je signálem, že kernel komunita je ochotná více pragmaticky využít nestandardní jazyková rozšíření, pokud zlepší udržovatelnost a efektivitu kódu. Pro průmysl to znamená:

- Posun v požadavcích na toolchain: build prostředí pro kernel musí důsledně podporovat Microsoft C Extensions, jinak hrozí build chyby nebo rozdílné chování.
- Potenciální zjednodušení interních struktur jádra, což může vývojářům usnadnit práci, ale současně zvýšit bariéru pro nové přispěvatele, kteří budou muset znát specifika těchto rozšíření.
- Další krok k tomu, že jádro nebude čistě referenční implementací striktního standardního C, ale pragmatickým projektem využívajícím konkrétní vlastnosti moderních překladačů.

Z pohledu stability a bezpečnosti je klíčové, aby tato změna byla důkladně zrecenzována: jakékoli subtilní rozdíly v implementaci rozšíření mezi GCC a Clang nebo mezi verzemi mohou přinést těžko odhalitelné chyby. Pokud však bude změna technicky disciplinovaně omezena na jasně definované konstrukce, může přinést praktický, byť nenápadný, benefit pro vývoj i dlouhodobou údržbu linuxového jádra.

---

[Číst původní článek](https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext)

**Zdroj:** 📰 Phoronix
