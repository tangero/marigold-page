---
author: Marisa Aigen
category: cloudové úložiště
date: '2025-12-02 11:08:08'
description: AWS na konferenci re:Invent 2025 oznámil obecnou dostupnost služby Amazon
  S3 Vectors, která přidává nativní vektorové databázové funkce do úložiště S3. Tato
  technologie umožňuje ukládat a dotazovat vektorové embeddingy přímo v S3 pro AI
  aplikace, jako je semantické vyhledávání nebo paměť AI agentů.
importance: 3
layout: tech_news_article
original_title: AWS recalibrates data economics further with S3 Vectors, batch & Intelligent-Tiering
publishedAt: '2025-12-02T11:08:08+00:00'
slug: aws-recalibrates-data-economics-further-with-s3-ve
source:
  emoji: 📰
  id: null
  name: ComputerWeekly.com
title: AWS dále upravuje ekonomiku dat pomocí S3 Vectors, batch a Intelligent-Tiering
url: https://www.computerweekly.com/blog/CW-Developer-Network/AWS-recalibrates-data-economics-further-with-S3-Vectors-batch-Intelligent-Tiering
---

## Souhrn
AWS během konference re:Invent 2025 v Las Vegas uvedl do obecné dostupnosti službu Amazon S3 Vectors, která rozšiřuje objektové úložiště Amazon S3 o nativní podporu vektorových databází. Tato funkce umožňuje datovým vědcům ukládat a vyhledávat vektorové embeddingy – numerické reprezentace nestrukturovaných dat – přímo v S3, což zjednodušuje práci s AI modely. Novinka přináší vylepšení ve škálovatelnosti a výkonu pro aplikace jako semantické vyhledávání nebo doporučovací systémy.

## Klíčové body
- Amazon S3 Vectors je nyní obecně dostupné s výraznými zlepšeními výkonu a škálovatelnosti.
- Umožňuje ukládat vektorové embeddingy (numerické reprezentace textu, obrázků nebo audia) přímo v S3 bez potřeby externích databází.
- Podporuje propojení dat mezi objekty v S3, včetně vztahů mezi více než dvěma objekty.
- Cílí na AI aplikace, jako je semantické vyhledávání, paměť AI agentů a doporučovací systémy.
- S3 tak nabízí cenově efektivní alternativu k samostatným vektorům databázím.

## Podrobnosti
Amazon S3 je základní služba AWS pro objektové úložiště, která podle společnosti zásadně změnila ekonomiku ukládání dat díky nízkým cenám a vysoké škálovatelnosti. S3 Vectors toto úložiště rozšiřuje o nativní vektorové databázové možnosti. Vektorové embeddingy představují numerické vektory, které zachycují sémantický význam a vztahy v nestrukturovaných datech, jako je text, obrázky nebo zvuk. Tyto embeddingy vytvářejí AI modely, například velké jazykové modely (LLM), a slouží k transformaci datových bodů do vícedimenzionálního prostoru, kde lze efektivně hledat podobnosti.

Služba funguje prostřednictvím vektorových kbelíků (vector buckets) a indexů. Uživatelé mohou generovat embeddingy pomocí modelů jako ty z Amazon Bedrock nebo externích služeb a ukládat je přímo do S3. Dotazy pak probíhají pomocí vektorové podobnosti, což umožňuje rychlé vyhledávání relevantních dat na základě sémantiky, nikoli jen klíčových slov. Například v semantickém vyhledávání najde S3 Vectors dokumenty podobné ve významu, i když neobsahují přesné fráze. Pro AI agenty slouží k uchování kontextové paměti, kde se ukládají interakce a znalosti pro dlouhodobé učení. Doporučovací systémy pak využívají embeddingy k navrhování položek na základě uživatelských preferencí.

AWS zdůrazňuje, že tato integrace činí S3 cenově výhodnější než specializované vektorové databáze jako Pinecone nebo Weaviate, protože eliminuje potřebu přenosu dat mezi službami. S3 zvládá exabajty dat a nabízí vysokou dostupnost, což je ideální pro velké AI úlohy. Novinka přichází s vylepšeními v batch zpracování a Intelligent-Tiering, které automaticky optimalizuje náklady podle přístupových vzorců. Uživatelé tak mohou spouštět dotazy na miliardy vektorů s latencí v řádu milisekund.

Jako expert na AI a cloudové technologie oceňuji tuto integraci, protože řeší bolestivé body datových týmů: data v S3 zůstávají na místě a lze je ihned využít pro ML trénink nebo inference. Nicméně AWS není prvním hráčem v tomto prostoru – konkurenční cloudové platformy jako Google Cloud nebo Azure již podobné funkce nabízejí – takže výhoda spočívá především v ekosystému AWS pro stávající zákazníky.

## Proč je to důležité
Tato novinka posiluje pozici AWS v AI ekosystému tím, že spojuje masivní úložiště s pokročilým vyhledáváním, což snižuje náklady na AI aplikace o řádově desítky procent oproti hybridním řešením. Pro průmysl znamená snížení složitosti nasazení RAG (Retrieval-Augmented Generation) systémů, kde LLM čerpají z vlastních datových zdrojů. V širším kontextu urychluje adopci vektorového vyhledávání v odvětvích jako e-commerce, zdravotnictví nebo finance, kde je klíčová rychlost a přesnost. Dlouhodobě to může donutit konkurenci k podobným inovacím, což prospěje celému trhu s datovými službami.

---

[Číst původní článek](https://www.computerweekly.com/blog/CW-Developer-Network/AWS-recalibrates-data-economics-further-with-S3-Vectors-batch-Intelligent-Tiering)

**Zdroj:** 📰 ComputerWeekly.com
