---
author: Marisa Aigen
category: cloudové úložiště
date: '2025-12-05 20:40:00'
description: Článek rozebírá běžné chyby při konfiguraci S3 bucketů pro tabulky Delta
  Lake a nabízí řešení pro snížení nákladů a zlepšení výkonu. Zaměřuje se na konflikty
  verzování, třídy úložišť a přenos dat.
importance: 3
layout: tech_news_article
original_title: Expensive Delta Lake S3 Storage Mistakes (And How to Fix Them)
publishedAt: '2025-12-05T20:40:00+00:00'
slug: expensive-delta-lake-s3-storage-mistakes-and-how-t
source:
  emoji: 📰
  id: null
  name: Databricks.com
title: Drahé chyby v úložišti S3 pro Delta Lake (a jak je opravit)
url: https://www.databricks.com/blog/expensive-delta-lake-s3-storage-mistakes-and-how-fix-them
urlToImage: https://www.databricks.com/sites/default/files/2025-12/expensive-delta-lake-s3-storage-mistakes-og-image.png
urlToImageBackup: https://www.databricks.com/sites/default/files/2025-12/expensive-delta-lake-s3-storage-mistakes-og-image.png
---

## Souhrn
Článek identifikuje časté chyby v nastavování S3 bucketů pro Delta Lake tabulky v Lakehouse architektuře, které vedou k zbytečným nákladům na úložiště a síťový provoz. Popisuje tři klíčové oblasti: verzování objektů oproti verzování tabulek, třídy úložišť a náklady na přenos dat. Nabízí praktické kroky k detekci a opravě pomocí nástrojů Databricks a AWS služeb.

## Klíčové body
- Konflikt mezi nativním S3 object versioning a verzováním Delta Lake tabulek vede k duplicitnímu ukládání dat a vyšším nákladům.
- Nesprávné použití storage classes (hot, cool, cold, archive) brání automatickému přesunu starších dat do levnějších tříd.
- Lifecycle policies umožňují automatizaci přesunů dat bez zásahu do Delta Lake logů.
- Optimalizace přenosu dat mezi S3 a výpočetními clustery snižuje síťové poplatky.
- Doporučené nasazení bucketů zahrnuje oddělené buckety pro data a logy.

## Podrobnosti
Cloudové úložiště jako S3 tvoří základ Lakehouse architektury, kde Delta Lake slouží k správě tabulek s podporou transakcí, verzování a časového cestování. Delta Lake ukládá každou transakci jako manifest soubor v JSON nebo Parquet formátu v adresáři _delta_log/, který odkazuje na podkladové Parquet soubory s daty. Při přidání, úpravě nebo smazání dat se vytvářejí nové soubory, což zajišťuje ACID vlastnosti bez nutnosti externího verzování.

Problém nastává, když se zapne nativní S3 object versioning, které verziuje každý objekt samostatně. To je v rozporu s Delta Lake, protože obě mechanismy řeší retenci dat jinak: Delta Lake verzuje na úrovni tabulky, S3 na úrovni objektu. Výsledek je duplicitní úložiště verzí, což zvyšuje objem dat a náklady. Řešení spočívá v vypnutí S3 versioning pro Delta Lake buckety a spoléhání se výhradně na Delta Lake time travel, které umožňuje vrátit tabulku do minulého stavu pomocí příkazů jako RESTORE TABLE.

Další oblastí jsou storage classes. S3 nabízí třídy jako Standard (hot pro častý přístup), Intelligent-Tiering (automatický přesun), Glacier (cold pro vzácný přístup) nebo Deep Archive (pro dlouhodobé archivace). Pro Delta Lake tabulky s rostoucím objemem dat z ETL pipelineů nebo dotazů je ideální nastavit lifecycle policies, které po určité době (např. 30 dnů) přesunou starší Parquet soubory do levnějších tříd. Databricks Unity Catalog pomáhá monitorovat velikost tabulek a identifikovat kandidáty na optimalizaci. Například příkaz DESCRIBE HISTORY tabulka ukáže verze a jejich velikosti.

Náklady na přenos dat (data transfer) mezi S3 a Databricks clustery lze minimalizovat výběrem clusterů ve stejné AWS region a zóně. Použití S3 Select nebo Databricks Delta Cache zrychluje čtení bez plného stahování. Pro detekci problémů slouží AWS Cost Explorer a Databricks System Tables pro analýzu úložišť.

## Proč je to důležité
S rostoucím objemem dat v Lakehouse architektuře mohou náklady na S3 rychle překročit rozpočet, zejména pokud ETL procesy generují tisíce verzí denně. Optimalizace versioning a storage classes může snížit náklady o desítky procent bez ztráty funkčnosti Delta Lake, jako je časové cestování nebo schema enforcement. V širším kontextu big data ekosystému to umožňuje škálovat datové jezera udržitelně, což je klíčové pro firmy závislé na Databricks a AWS. Bez těchto opatření hrozí neefektivita, která brzdí inovace v analýze dat.

---

[Číst původní článek](https://www.databricks.com/blog/expensive-delta-lake-s3-storage-mistakes-and-how-fix-them)

**Zdroj:** 📰 Databricks.com
