---
author: Marisa Aigen
category: programování
companies:
- Microsoft
date: '2025-11-09 14:51:00'
description: Vývojáři Linuxového kernelu zvažují plošné zapnutí přepínače -fms-extensions
  pro GCC a Clang, což by umožnilo využít vybrané konstrukce z Microsoft C Extensions
  a zjednodušit část kódu jádra.
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
title: Linuxový kernel míří k povolení Microsoft C Extensions napříč kompilací
url: https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext
urlToImage: https://www.phoronix.net/image.php?id=2025&image=ms_b
urlToImageBackup: https://www.phoronix.net/image.php?id=2025&image=ms_b
---

## Souhrn
Linuxový kernel se připravuje na krok, který byl roky předmětem debat: plošné povolení přepínače `-fms-extensions` v systému sestavení (kbuild). Dva patche zařazené do větve `kbuild-next` mají umožnit použití vybraných Microsoft C Extensions při kompilaci jádra pomocí GCC i LLVM/Clang, primárně kvůli jednoduššímu a kompaktnějšímu zápisu některých datových struktur.

## Klíčové body
- Dva patche v `kbuild-next` navrhují globální zapnutí `-fms-extensions` pro kompilaci Linuxového kernelu.
- Rozšíření cílí zejména na možnost anonymního vkládání označených `struct` a `union` do jiných struktur.
- Změna se očekává pro merge okno Linux 6.19, pokud nebudou zásadní námitky od klíčových vývojářů včetně Linuse Torvaldse.
- Historicky byly podobné návrhy odmítány kvůli obavám z dalšího ne-standardního chování kompilátoru.
- Zastánci argumentují čitelnějším kódem, potenciální úsporou paměti a praktičtější prací s datovými strukturami.

## Podrobnosti
Návrh vychází z dlouhodobé diskuse na mailing listu Linuxového kernelu o tom, zda je rozumné přidávat další ne zcela standardní rozšíření jazyka C do oficiálního build procesu. Přepínač `-fms-extensions`, podporovaný jak GCC, tak LLVM/Clang, aktivuje podmnožinu chování známého z Microsoft Visual C/C++ kompilátoru. V kontextu Linuxového kernelu nejde o přibližování se Windows API, ale o využití konkrétních syntaktických možností pro definici datových struktur.

Klíčovým příkladem je možnost zahrnout „tagged“ `struct` nebo `union` anonymně do jiné struktury. Tím lze vytvářet vrstvené datové typy, kde se polím vnořených struktur přistupuje příměji, bez nutnosti vkládat další pojmenovanou úroveň. Výsledkem je kompaktnější, přehlednější kód a v některých případech lepší rozložení na zásobníku a v paměti. Návrh předložil mimo jiné Rasmus Villemoes, který zdůrazňuje, že jednotlivé dílčí případy sice vždy šlo obejít, ale kumulativně vzniká zbytečná zátěž v syntaxi a údržbě.

Dosud se podobné návrhy nedařilo prosadit, protože přidání dalšího globálního přepínače znamená:
- potenciální riziko vzniku kódu využívajícího méně zřejmé Microsoft-specifické konstrukce,
- komplikace pro alternativní toolchainy nebo statickou analýzu, které počítají se striktně standardním C,
- nutnost pečlivě hlídat kompatibilitu napříč architekturami a konfiguracemi jádra.

Zařazení patchů do `kbuild-next` však ukazuje, že část maintainerské komunity je ochotná „kousnout do kyselého jablka“ a akceptovat omezené ne-standardní rozšíření výměnou za dlouhodobé zjednodušení kódu. Finální rozhodnutí pravděpodobně padne během merge okna pro Linux 6.19, kde se ukáže, zda proti změně vystoupí klíčové osobnosti vývoje kernelu.

## Proč je to důležité
Tento krok není mediálně efektní, ale má praktický význam pro celý ekosystém okolo Linuxového kernelu:

Zaprvé, ovlivňuje standardy psaní kódu jádra a tím i tisíce vývojářů, kteří vytvářejí ovladače, subsystémy a out-of-tree moduly. Povolení Microsoft C Extensions otevírá dveře k využívání nových idiomů v kódu, ale zároveň zvyšuje nároky na disciplínu: je nutné držet se jen těch částí rozšíření, které jsou srozumitelné, dobře dokumentované a podporované všemi relevantními kompilátory.

Zadruhé, změna zasahuje do oblasti přenositelnosti a nástrojové podpory. Nástroje pro statickou analýzu, formální verifikaci a alternativní build systémy musí spolehlivě pracovat s kódem, který využívá `-fms-extensions`. Pokud se ekosystém přizpůsobí, může to vést k robustnější infrastruktuře, ale přechodné období může odhalit skryté chyby a nekonzistence.

Zatřetí, jde o signál ohledně pragmatismu vývoje Linuxového kernelu: preferuje se praktičnost a údržovatelnost před ideologicky čistým držením se standardu C. To může do budoucna ovlivnit i další rozhodnutí, například ohledně podpory nových jazykových vlastností v C, rozšíření pro bezpečnější paměťové modely nebo integraci Rustu a dalších jazyků v kritických částech systému.

---

[Číst původní článek](https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext)

**Zdroj:** 📰 Phoronix
