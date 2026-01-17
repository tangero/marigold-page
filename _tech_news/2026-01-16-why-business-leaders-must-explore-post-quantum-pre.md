---
author: Marisa Aigen
category: postkvantová kryptog
date: '2026-01-16 15:53:00'
description: S pokračujícím vývojem kvantových počítačů hrozí ohrožení současných
  kryptografických standardů. Článek vysvětluje, jak se firmy mohou připravit na postkvantovou
  kryptografii (PQC) a vyhnout se rizikům jako jsou útoky typu harvest now, decrypt
  later.
importance: 5
layout: tech_news_article
original_title: Why business leaders must explore post-quantum pre-quantum
publishedAt: '2026-01-16T15:53:00+00:00'
slug: why-business-leaders-must-explore-post-quantum-pre
source:
  emoji: 📰
  id: null
  name: Techtarget.com
title: Proč musí lídři firem prozkoumat postkvantovou kryptografii před kvantovou
  érou
url: https://www.techtarget.com/searchenterpriseai/tip/Why-business-leaders-must-explore-post-quantum-pre-quantum
urlToImage: https://www.techtarget.com/rms/onlineimages/arvr_g1200559136.jpg
urlToImageBackup: https://www.techtarget.com/rms/onlineimages/arvr_g1200559136.jpg
---

## Souhrn
Postkvantová kryptografie (PQC) představuje nutnou ochranu proti hrozbám kvantových počítačů, které ohrozí současné systémy veřejného klíče. NIST stanovil časový rámec, podle kterého budou staré šifrovací algoritmy do roku 2030 odebrány a do 2035 zakázány. Firmy musí nyní identifikovat své kryptografické aktiva, posoudit rizika a přejít na kryptograficky agilní architektury.

## Klíčové body
- NIST zveřejnil tři finální standardy PQC pro odolnost proti kvantovým útokům.
- Hrozba harvest now, decrypt later (HNDL): útočníci sbírají šifrovaná data nyní pro budoucí dešifrování.
- Postihnuté oblasti: šifrování veřejným klíčem, digitální podpisy a symetrické šifrování.
- Kroky přípravy: inventarizace aktiv, hodnocení rizik, adopce crypto-agility a školení týmů.
- Kritické sektory: obrana, zdravotnictví a výzkum, kde je důvěrnost dat klíčová.

## Podrobnosti
Článek od Nihad Hassana zdůrazňuje, že postkvantová kryptografie není jen technickou aktualizací, ale nezbytností pro ochranu digitálních interakcí firem. Současné systémy veřejného klíče, jako RSA nebo ECC, spoléhají na matematické problémy jako faktorizace celých čísel nebo diskrétní logaritmy, které kvantové počítače s algoritmy typu Shorova dokážou efektivně rozlousknout. PQC algoritmy naopak vycházejí z jiných matematických základů, jako mřížkové problémy nebo hash-funkce, které odolají i Groverovu algoritmu pro symetrické šifrování.

NIST v červenci 2024 oznámil tři standardizované algoritmy: ML-KEM (pro šifrování klíčů), ML-DSA (pro digitální podpisy) a SLH-DSA (pro podpisy bez stavu). Tyto standardy slouží jako vodítko pro migraci. Podle NIST časové osy budou legacy systémy veřejného klíče do 2030 označeny za nevhodné a do 2035 plně zakázány. Firmy tak mají omezený čas na přechod.

Hlavní hrozby zahrnují HNDL útoky, při kterých státní aktéři jako Čína nebo Rusko již sbírají šifrovaná data z protokolů TLS, SSH nebo VPN. Do tří let mohou kvantové počítače s tisíci stabilních qubitů tato data dešifrovat. Další rizika zahrnují expozici dat v cloudu, kde symetrické šifrování jako AES-256 vyžaduje dvojnásobnou délku klíčů proti Groverovu algoritmu.

Příprava vyžaduje systematický přístup: nejprve inventarizaci všech kryptografických aktiv v infrastruktuře, aplikacích a zařízeních IoT. Poté kvantové hodnocení rizik pomocí nástrojů jako CryptoSPIRAL od NSA. Adopce crypto-agility znamená návrh systémů, kde lze algoritmy měnit bez přeprogramování – například v knihovnách jako OpenSSL 3.0 nebo Bouncy Castle. Vyžaduje to investice od vedení a školení od vývojářů po IT správce. Firmy jako Google a Cloudflare již testují PQC v produkci, což ukazuje na nutnost akce.

## Proč je to důležité
Kvantové počítače představují existenciální hrozbu pro globální digitální ekonomiku, kde kryptografie chrání transakce v hodnotě bilionů dolarů denně. Bez PQC dojde k masivním únikům dat v klíčových odvětvích, což ohrozí národní bezpečnost a ekonomickou stabilitu. V širším kontextu urychluje to vývoj hybridních systémů, kde PQC doplňuje klasickou kryptografii, a nutí průmysl k rethinku celé bezpečnostní architektury. Pro firmy v EU podle NIS2 směrnice je to regulační povinnost, s pokutami až 10 milionů eur za nedbalost. Jako expert na IT bezpečnost vidím, že odklad migrace vede k nevratným ztrátám, zatímco včasná příprava zajistí konkurenční výhodu v postkvantové éře.

---

[Číst původní článek](https://www.techtarget.com/searchenterpriseai/tip/Why-business-leaders-must-explore-post-quantum-pre-quantum)

**Zdroj:** 📰 Techtarget.com
