---
author: Marisa Aigen
category: aws
companies:
- AWS
date: '2025-12-02 15:40:15'
description: První den konference AWS re:Invent 2025 přinesl klíčové oznámení o rozšíření
  služby AWS Transform o AI agenta pro modernizaci celého zásobníku Windows aplikací
  včetně databází. Tento nástroj automatizuje převod .NET aplikací a SQL Server databází
  na PostgreSQL a nasazuje je do kontejnerů na AWS infrastruktuře.
importance: 3
layout: tech_news_article
original_title: What’s New at AWS re:Invent 2025 – Day 1 Highlights
publishedAt: '2025-12-02T15:40:15+00:00'
slug: whats-new-at-aws-reinvent-2025-day-1-highlights
source:
  emoji: 📰
  id: null
  name: Cloudnsqlsailor.com
title: Co nového na AWS re:Invent 2025 – Nejlepší momenty z prvního dne
url: https://cloudnsqlsailor.com/2025/12/02/whats-new-at-aws-reinvent-2025-day-1-highlights/
urlToImage: https://cloudnsqlsailor.com/wp-content/uploads/2025/12/img_1643.jpg?w=1024
urlToImageBackup: https://cloudnsqlsailor.com/wp-content/uploads/2025/12/img_1643.jpg?w=1024
---

## Souhrn
Na prvním dni konference AWS re:Invent 2025 společnost Amazon Web Services oznámila rozšíření služby AWS Transform o nového AI agenta určeného k modernizaci celého zásobníku Windows aplikací. Tento agent automaticky převádí .NET aplikace a databáze Microsoft SQL Server na open-source alternativu PostgreSQL v podobě Amazon Aurora PostgreSQL a nasazuje je do kontejnerů na Amazon ECS nebo Amazon EC2 Linux. Proces zrychluje pětkrát a snižuje provozní náklady až o 70 procent.

## Klíčové body
- AWS Transform rozšiřuje své možnosti z modernizace .NET aplikací na full-stack Windows modernizaci včetně databází.
- Automatická transformace SQL Server databází z instancí Amazon EC2 nebo Amazon RDS na Amazon Aurora PostgreSQL.
- Skenování .NET aplikačního kódu přímo z repozitářů zdrojového kódu.
- Nasazení do kontejnerů na Amazon ECS nebo Amazon EC2 s Linuxem.
- Zrychlení modernizace pětkrát a úspora nákladů až 70 procent.

## Podrobnosti
Služba AWS Transform, která slouží k automatizaci migrace a modernizace aplikací, dosud podporovala především agent pro modernizaci .NET aplikací. Nový AI agent přináší komplexní přístup k celému zásobníku Windows, což zahrnuje jak aplikační vrstvu, tak databázovou. Pro firmy, které provozují tisíce instancí SQL Server, představuje modernizace významné výzvy: vysoké licenční poplatky Microsoftu, složitost při velkém objemu systémů a časová náročnost, která brzdí vývojářské týmy.

AI agent funguje tak, že skenuje databáze SQL Server v instancích Amazon EC2 nebo Amazon RDS a zároveň analyzuje .NET kód z git repozitářů. Na základě těchto dat automaticky generuje ekvivalentní verzi v PostgreSQL, přizpůsobuje aplikační logiku pro kompatibilitu a připravuje kontejnerizované nasazení. Výstupem je plně funkční aplikace na Amazon Aurora PostgreSQL, což je plně spravovaná databáze kompatibilní s PostgreSQL, optimalizovaná pro AWS cloud. Nasazení probíhá buď na Amazon ECS pro serverless kontejnery, nebo na Amazon EC2 s Linuxem pro tradičnější virtuální stroje.

Tento přístup řeší běžné bolesti: PostgreSQL nabízí silnou komunitní podporu, nižší náklady a otevřenost oproti proprietárnímu SQL Serveru. AWS Transform tak umožňuje automatizovanou detekci, transformaci a nasazení, což minimalizuje manuální zásahy. Například firmy s legacy systémy mohou nyní rychleji přejít na cloud-native architekturu, což zlepšuje škálovatelnost a snižuje závislost na Windows prostředí. Kriticky lze poznamenat, že i když je agent založen na AI, stále vyžaduje validaci výstupů, protože automatizace složitých databázových schémat nemusí být vždy dokonalá – zvláště u specifických SQL Server funkcí jako CLR nebo proprietární extensí.

## Proč je to důležité
Tato novinka usnadňuje migraci z Microsoft ekosystému do AWS, kde firmy čelí rostoucím licenčním nákladům a touze po open-source řešeních. V širším kontextu podporuje trend cloudové modernizace, kde AI agenti přebírají rutinní IT úkoly, což uvolňuje kapacity pro inovace. Pro průmysl znamená zrychlení 5x a úsporu 70 procent konkurenční výhodu pro AWS zákazníky, ale zároveň posiluje vendor lock-in v rámci AWS služeb jako Aurora nebo ECS. V éře AI-driven DevOps představuje krok k automatizaci, který může ovlivnit tisíce podniků závislých na Windows legacy systémech.

---

[Číst původní článek](https://cloudnsqlsailor.com/2025/12/02/whats-new-at-aws-reinvent-2025-day-1-highlights/)

**Zdroj:** 📰 Cloudnsqlsailor.com
