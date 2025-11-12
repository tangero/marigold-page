---
author: Marisa Aigen
category: ai
date: '2025-11-10 12:00:01'
description: Tým z Tsinghua University a Peking University představil framework PhyE2E,
  který kombinuje generativní AI, symbolickou regresi a fyzikální znalosti k automatickému
  odvozování fyzikálních zákonů z neupravených dat, s důrazem na aplikace ve fyzice
  kosmického prostoru.
importance: 3
layout: tech_news_article
original_title: New AI framework can uncover space physics equations in raw data -
  Phys.org
publishedAt: '2025-11-10T12:00:01+00:00'
slug: new-ai-framework-can-uncover-space-physics-equatio
source:
  emoji: 📰
  id: null
  name: Phys.Org
title: Nový AI framework automaticky odhaluje fyzikální rovnice z neupravených dat
url: https://phys.org/news/2025-11-ai-framework-uncover-space-physics.html
urlToImage: https://scx2.b-cdn.net/gfx/news/hires/2025/new-ai-framework-can-u.jpg
urlToImageBackup: https://scx2.b-cdn.net/gfx/news/hires/2025/new-ai-framework-can-u.jpg
---

## Souhrn
Nový AI framework PhyE2E umožňuje automaticky hledat fyzikální zákony a rovnice přímo v neupravených pozorovacích datech, zejména v oblasti fyziky kosmického prostoru. Kombinuje generování syntetických dat pomocí velkého jazykového modelu, end-to-end učení a symbolickou regresi, aby z dat získal přesné a fyzikálně konzistentní matematické vztahy.

## Klíčové body
- PhyE2E propojuje generativní AI, symbolickou regresi a fyzikální omezení (physical priors) do jednoho end-to-end systému.
- Framework používá velký jazykový model k tvorbě syntetických trénovacích dat a rozšiřuje tak možnosti učení z omezených měření.
- Pomocí techniky "divide & conquer" rozkládá složité rovnice na dílčí podproblémy, které lze lépe numericky i symbolicky řešit.
- Modul MCTS (Monte Carlo Tree Search) s bezkontextovou gramatikou zpřesňuje navržené rovnice a hlídá matematickou i fyzikální konzistenci.
- Cíl: zrychlit objevování fyzikálních vztahů v datech ze satelitů, sond a dalších vědeckých měření a poskytnout ověřitelné, interpretovatelné modely místo čistě černých skříněk.

## Podrobnosti
Framework PhyE2E, publikovaný v Nature Machine Intelligence, představuje systematický přístup k automatickému odvozování fyzikálních rovnic z neupravených dat. Na rozdíl od běžných AI modelů, které se soustředí pouze na predikci, se PhyE2E pokouší rekonstruovat explicitní symbolické rovnice, které lze fyzicky interpretovat a ověřovat. 

Systém se skládá z několika vrstev. Nejprve je reálný trénovací soubor rozšířen syntetickými daty generovanými velkým jazykovým modelem, který vytváří dodatečné scénáře a kombinace proměnných. To je zásadní pro oblasti, jako je fyzika kosmického prostředí, kde jsou kvalitní měření omezená, nepravidelná nebo drahá. Následně framework využívá vícevrstvý perceptron (MLP) a techniku variable-interaction, která rozkládá původní úlohu symbolické regrese na menší podúlohy (divide & conquer). Tím se zmenšuje prostor možných rovnic a zvyšuje se stabilita trénování.

End-to-end model integruje tzv. physical priors, tedy předchozí fyzikální znalosti (například zachování energie, dimenzionální analýzu, známé tvarové závislosti), které fungují jako omezení pro vyhledávané rovnice. Tento krok je klíčový, protože zabraňuje tomu, aby AI generovala matematicky přesné, ale fyzikálně nesmyslné vztahy.

V poslední fázi PhyE2E používá modul Monte Carlo Tree Search s bezkontextovou gramatikou, která obsahuje základní "atomické" funkce a kandidátní rovnice. MCTS systematicky prohledává prostor vzorců, porovnává je s daty a metrikou RMSE a dolaďuje jejich strukturu. Výsledkem jsou kompaktní rovnice, které jsou dostatečně přesné pro predikci a zároveň transparentní pro vědce.

Pro praxi to znamená potenciální zrychlení práce týmů, které analyzují data ze satelitů, sond nebo plazmových experimentů: místo ručního navrhování modelů mohou využít AI nástroj, který automaticky navrhne kandidátní zákony, jež lze následně fyzikálně interpretovat a experimentálně ověřit.

## Proč je to důležité
PhyE2E je příkladem směru, který posouvá AI od čistě empirických černých skříněk k nástrojům pro objevování vědeckých zákonitostí. Pro oblast fyziky kosmického prostoru jde o praktický způsob, jak vytěžit stále rostoucí objem dat z misí a senzorů bez nutnosti manuálního procházení všech kombinací proměnných. 

Z pohledu technologického ekosystému tento přístup ukazuje, jak lze generativní AI a symbolickou regresi využít pro vysvětlitelné modelování v kritických doménách, jako je kosmické počasí, plazmová fyzika nebo materiálové vědy. Pro průmysl to znamená potenciální aplikace v návrhu satelitních systémů, předpovědi vlivu sluneční aktivity na infrastrukturu nebo optimalizaci fyzikálních simulací. Zároveň je však nutné zdůraznit, že tyto nástroje nenahrazují odborníky: slouží primárně jako prostředek pro rychlou generaci hypotéz, které musí být fyzikálně a experimentálně potvrzeny.

---

[Číst původní článek](https://phys.org/news/2025-11-ai-framework-uncover-space-physics.html)

**Zdroj:** 📰 Phys.Org
