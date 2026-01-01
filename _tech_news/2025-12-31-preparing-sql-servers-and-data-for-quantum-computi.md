---
author: Marisa Aigen
category: kvantové počítačství
date: '2025-12-31 00:00:00'
description: Kvantové počítače ohrozí současné šifrování na bázi RSA a ECC algoritmů,
  což vyžaduje přechod na kvantově odolné šifrování. Článek vysvětluje rizika pomocí
  Moscaovy věty a odhaduje časovou osu kolem let 2031–2033.
importance: 5
layout: tech_news_article
original_title: Preparing SQL Servers and Data for Quantum Computing
publishedAt: '2025-12-31T00:00:00+00:00'
slug: preparing-sql-servers-and-data-for-quantum-computi
source:
  emoji: 📰
  id: null
  name: Mssqltips.com
title: Příprava SQL serverů a dat na kvantové počítače
url: https://www.mssqltips.com/sqlservertip/11555/sql-server-and-quantum-computing/
urlToImage: https://www.mssqltips.com/wp-content/uploads/11555_Preparing-SQL-Server-and-Data-For-Quantum-Computing.webp
urlToImageBackup: https://www.mssqltips.com/wp-content/uploads/11555_Preparing-SQL-Server-and-Data-For-Quantum-Computing.webp
---

## Souhrn
Kvantové počítače budou schopny prolomit asymetrické šifrování jako RSA a ECC, což ohrozí data uložená v SQL serverech. Organizační riziko lze posoudit pomocí Moscaovy věty, která odhaduje, zda doba ochrany dat překročí dobu do kvantové dostupnosti. Příprava zahrnuje přechod na post-kvantovní kryptografii.

## Klíčové body
- Kvantové počítače prolomí RSA a ECC šifrování pomocí algoritmů jako Shorův algoritmus.
- Moscaova věta (X + Y > Z): X je doba ochrany dat, Y doba na migraci, Z kvantová dostupnost (odhad 2031–2033).
- SQL servery vyžadují upgrade na quantum-safe algoritmy pro klíče, certifikáty a data at rest.
- Riziko existuje i pro data zašifrovaná dnes, pokud budou relevantní po roce 2030 (harvest now, decrypt later).
- NIST standardizuje post-kvantovní algoritmy jako Kyber nebo Dilithium.

## Podrobnosti
Článek se zaměřuje na bezpečnostní přípravu SQL serverů na éru kvantových počítačů, kde algoritmy jako Shorův algoritmus umožní rychlé faktorizování velkých čísel a diskrétní logaritmy na eliptických křivkách. To znemožní současné asymetrické šifrování RSA a ECC, které se používá pro výměnu klíčů v TLS/SSL, certifikáty a šifrování dat v SQL Serveru (např. Transparent Data Encryption – TDE nebo Always Encrypted).

Moscaova věta pomáhá kvantifikovat riziko: pokud součet doby, po kterou musí být data chráněna (X), a doby nutné na přechod na nové šifrování (Y) překročí rok, kdy kvantové počítače stanou dostupnými a levnými (Z), je organizace ohrožena. Experti jako Michele Mosca odhadují Z na 2031 pro průlomové kvantové systémy schopné prolomit 2048-bitové RSA klíče. I plná migrace před rokem 2032 nemusí stačit kvůli hrozbě "harvest now, decrypt later", kdy útočníci sbírají zašifrovaná data dnes pro budoucí dešifrování.

Pro SQL Servery (verze 2016 a novější) to znamená:
- Nahrazení RSA/ECC certifikátů v TLS hybridními schématy (např. TLS 1.3 s post-quantum key exchange).
- Migraci TDE na quantum-safe algoritmy, jako CRYSTALS-Kyber pro key encapsulation.
- Aktualizaci Always Encrypted na post-quantum varianty.
NIST v roce 2024 finalizoval standardy (FIPS 203–205) pro algoritmy Kyber, Dilithium a Sphincs+, které jsou odolné vůči Groverovu algoritmu i Shorovu. Microsoft již testuje integraci do Azure SQL a plánuje podporu v SQL Serveru 2022+.

Organizace by měly provést audit: identifikovat dlouhodobě citlivá data (např. zdravotnické záznamy s 20+ lety relevance), odhadnout Y (migrace může trvat 3–5 let) a zahájit testování v sandboxu. Bezpečnostní experti doporučujují hybridní přístup: kombinovat klasické a post-quantum algoritmy pro kompatibilitu.

## Proč je to důležité
Tento vývoj ovlivní celý IT průmysl, včetně databází jako SQL Server, kde většina šifrovaných spojení a dat závisí na ohrožených algoritmech. V širším kontextu urychluje adopci post-quantum kryptografie, což ovlivní cloud providery (Azure, AWS), sítě a IoT zařízení. Pro firmy s dlouhodobými daty (finance, zdravotnictví) je to bezpečnostní krize srovnatelná s Y2K, ale s vyšším dopadem na globální ekonomiku – odhadované ztráty v bilionech dolarů bez přípravy. Kriticky: odhady Z jsou nejisté, ale konzervativní plánování od roku 2025 minimalizuje rizika v éře, kde kvantové systémy od IBM nebo Google již dosahují stovek qubitů.

---

[Číst původní článek](https://www.mssqltips.com/sqlservertip/11555/sql-server-and-quantum-computing/)

**Zdroj:** 📰 Mssqltips.com
