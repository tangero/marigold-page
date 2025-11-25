---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Oligo Cyber Security Ltd
date: '2025-11-24 15:00:46'
description: Bezpečnostní společnost Oligo zveřejnila zprávu o pěti závažných zranitelnostech
  v open-source nástroji Fluent Bit, které umožňují útočníkům vzdáleně převzít kontrolu
  nad cloudovými úlohami.
importance: 4
layout: tech_news_article
original_title: Oligo report uncovers critical Fluent Bit flaws exposing cloud workloads
publishedAt: '2025-11-24T15:00:46+00:00'
slug: oligo-report-uncovers-critical-fluent-bit-flaws-ex
source:
  emoji: 📰
  id: null
  name: SiliconANGLE News
title: Oligo odhalil kritické zranitelnosti v Fluent Bit ohrožující cloudová prostředí
url: https://siliconangle.com/2025/11/24/oligo-report-uncovers-critical-fluent-bit-flaws-exposing-cloud-workloads/
urlToImage: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/11/fleuntbitvuln.png
urlToImageBackup: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/11/fleuntbitvuln.png
---

## Souhrn
Bezpečnostní firma Oligo odhalila řetěz pěti kritických zranitelností v open-source logovacím agentu Fluent Bit, který je široce používán v cloudových a kontejnerizovaných prostředích. Tyto chyby umožňují útočníkům obejít autentizaci, přepisovat soubory, manipulovat s logy a získat plnou vzdálenou kontrolu nad systémem.

## Klíčové body
- Nejzávažnější chyba (CVE-2025-12972) vzniká z neověřených tagů používaných při generování názvů výstupních souborů.
- Útočník může pomocí sekvence „../“ zapisovat nebo přepisovat libovolné soubory na disku.
- Další zranitelnosti umožňují podvrhování tagů, manipulaci s routovací logikou a vyvolání přetečení zásobníku.
- Fluent Bit je nasazen přes 15 miliardkrát a používán v Kubernetes, AI laboratořích, bankách i SaaS platformách.
- Chyby ohrožují celé observability pipeline, protože Fluent Bit zpracovává nedůvěryhodná data z kontejnerů a sítí.

## Podrobnosti
Fluent Bit je lehký open-source agent určený ke sběru, zpracování a předávání logů, metrik a tras v cloudových a kontejnerizovaných systémech. Je integrován do Kubernetes a často slouží jako první bod ingestování dat z aplikací do backendů jako jsou cloudové služby, databáze nebo SIEM systémy. Právě jeho pozice na hranici mezi nedůvěryhodnými zdroji (např. kontejnery, soubory, síťové endpointy) a důvěryhodným backendem činí jeho zranitelnosti zvláště nebezpečnými.

Nejzávažnější zranitelnost CVE-2025-12972 vzniká tím, že Fluent Bit používá neověřené tagy – metadata přiřazená k logovacím záznamům – přímo v názvech výstupních souborů. Útočník může vložit relativní cestu (např. „../../../etc/passwd“) a tím přepsat kritické systémové soubory nebo vložit spustitelný kód. Další chyby umožňují například uhodnout jeden znak tagu a tím podvrhnout logovací data, nebo vytvořit extrémně dlouhé názvy Docker kontejnerů, které způsobí přetečení zásobníku a možná i spuštění libovolného kódu.

## Proč je to důležité
Fluent Bit je klíčovou součástí observability infrastruktury v mnoha organizacích, včetně finančních institucí, AI laboratoří a poskytovatelů cloudových služeb. Zranitelnosti tohoto rozsahu a závažnosti mohou vést k masivním kompromitacím cloudových úloh, manipulaci s bezpečnostními logy nebo dokonce k převzetí celých clusterů. Vzhledem k tomu, že Fluent Bit často běží s vyššími oprávněními a zpracovává data z nedůvěryhodných zdrojů, je riziko exploatace vysoké. Tento případ znovu ukazuje, jak kritické je zabezpečení tzv. „data plane“ komponent v moderních distribuovaných systémech.

---

[Číst původní článek](https://siliconangle.com/2025/11/24/oligo-report-uncovers-critical-fluent-bit-flaws-exposing-cloud-workloads/)

**Zdroj:** 📰 SiliconANGLE News
