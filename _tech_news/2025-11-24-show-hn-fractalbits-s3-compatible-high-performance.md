---
author: Marisa Aigen
category: úložiště dat
date: '2025-11-24 19:39:39'
description: Fractalbits je nový systém objektového úložiště kompatibilní se S3, který
  slibuje extrémní výkon pro úlohy jako AI trénování a analýzu dat. Je postaven na
  kombinaci Rustu a Zig a aktuálně se nachází ve fázi beta testování.
importance: 3
layout: tech_news_article
original_title: 'Show HN: Fractalbits – S3 compatible high performance storage with
  Rust and Zig'
publishedAt: '2025-11-24T19:39:39+00:00'
slug: show-hn-fractalbits-s3-compatible-high-performance
source:
  emoji: 📰
  id: null
  name: Github.com
title: Fractalbits – vysoce výkonné úložiště kompatibilní se S3, postavené na Rustu
  a Zig
url: https://github.com/fractalbits-labs/fractalbits-main
urlToImage: https://opengraph.githubassets.com/8c237d9400737bcccdfb9667d3b7a264c924378e65a69b64d302786eeeb8615e/fractalbits-labs/fractalbits-main
urlToImageBackup: https://opengraph.githubassets.com/8c237d9400737bcccdfb9667d3b7a264c924378e65a69b64d302786eeeb8615e/fractalbits-labs/fractalbits-main
---

## Souhrn
Fractalbits je nový open-source systém objektového úložiště kompatibilní se S3, který dosahuje až 1 milionu IOPS při čtení 4KB objektů s latencí kolem 5 ms (p99). Systém je navržen pro náročné úlohy jako trénování AI modelů nebo zpracování velkých dat, kde jsou klíčové nízká latence a atomické operace.

## Klíčové body
- Až 1 milion IOPS pro jeden bucket s latencí ~5 ms (p99)
- Nativní podpora atomického přejmenování objektů i adresářů – funkce, kterou standardní S3 nemá
- Dvouvrstvé úložiště: NVMe SSD pro „horké“ malé objekty, S3 backend pro větší soubory
- Metadata řeší vlastní Fractal ART (Adaptive Radix Tree) s plnou cestou, což eliminuje nutnost distribuovaných transakcí
- Implementace v Rustu (API gateway, řídicí rovina) a Zig (metadata engine, datová rovina) s využitím io_uring pro asynchronní I/O

## Podrobnosti
Fractalbits řeší dlouhodobý problém tradičních objektových úložišť – absence skutečné podpory pro adresářovou strukturu a atomické operace. Využitím Fractal ART, který ukládá metadata jako celé cesty místo klasického inode systému, se vyhýbá nákladným distribuovaným transakcím a zároveň poskytuje sémantiku adresářů včetně atomického přejmenování. To je kritické pro AI workflogy, kde se často přepisují nebo přesouvají celé datové sady nebo checkpointy modelů.

Architektura systému je dvouvrstvá: malé, často čtené objekty jsou ukládány na lokální NVMe SSD s jednočíslicovou milisekundovou latencí, zatímco větší objekty jsou ukládány do levnějšího S3 backendu. Tím se optimalizují náklady i výkon. Kombinace Rustu pro bezpečnou a robustní řídicí rovinu a Zig pro výkonnou datovou rovinu umožňuje dosáhnout vysokého počtu operací za sekundu při zachování nízké latence.

## Proč je to důležité
Fractalbits přináší alternativu k drahým cloudovým řešením jako AWS S3 Express One Zone, zejména pro workloady založené na malých objektech. Jeho schopnost poskytovat atomické operace a adresářovou sémantiku v S3-kompatibilním rozhraní může zjednodušit architekturu datových pipeline v AI a analytických systémech. I když se jedná o beta software, jeho přístup k řešení metadata a úložiště představuje zajímavý posun v návrhu objektových úložišť.

---

[Číst původní článek](https://github.com/fractalbits-labs/fractalbits-main)

**Zdroj:** 📰 Github.com
