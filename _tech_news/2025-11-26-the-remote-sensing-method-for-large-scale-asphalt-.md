---
author: Marisa Aigen
category: dálniční infrastrukt
date: '2025-11-26 00:00:00'
description: Výzkumníci vyvinuli nový rámec kombinující dálkové snímání, automatické
  generování dat a hluboké učení pro efektivní hodnocení stárnutí asfaltových vozovek
  na velkých územích.
importance: 3
layout: tech_news_article
original_title: The remote sensing method for large-scale asphalt pavement aging assessment
  with automated sample generation and deep learning
publishedAt: '2025-11-26T00:00:00+00:00'
slug: the-remote-sensing-method-for-large-scale-asphalt-
source:
  emoji: 📰
  id: null
  name: Nature.com
title: Metoda dálkového snímání pro hodnocení stárnutí asfaltových vozovek v rozsáhlém
  měřítku s automatickým generováním vzorků a hlubokým učením
url: https://www.nature.com/articles/s41598-025-29966-4
---

## Souhrn
Výzkumníci představili nový přístup pro hodnocení stárnutí asfaltových vozovek v rozsáhlém měřítku, který kombinuje dálkové snímání, automatické generování trénovacích vzorků a hluboké učení. Tento rámec umožňuje rychlejší a přesnější detekci degradace vozovek bez nutnosti náročných terénních průzkumů.

## Klíčové body
- Využití satelitních dat WorldView-3 pro analýzu stárnutí asfaltu
- Automatické generování kvalitních trénovacích a validačních vzorků pomocí spektrálního rozkladu smíšených pixelů
- Použití jednorozměrné konvoluční neuronové sítě (1D-CNN) s nulovým přenosem (zero-shot transfer)
- Celková přesnost klasifikace až 95,95 % v první testovací oblasti
- Metoda je vhodná pro podporu rozhodování v údržbě dopravní infrastruktury

## Podrobnosti
Tradiční metody hodnocení stárnutí asfaltových vozovek závisí na manuálních terénních průzkumech, které jsou časově náročné a nákladné. Nový přístup využívá satelitní data ze senzoru WorldView-3 a aplikuje techniku multi-endmember mixed pixel unmixing, která umožňuje rozložit spektrální signál smíšeného pixelu na příspěvky jednotlivých materiálů (např. asfalt, beton, vegetace). Následně jsou generovány trénovací vzorky pomocí filtru založeného na okolních pixelech, což zvyšuje jejich kvalitu a reprezentativnost. Klasifikace stáří asfaltu je prováděna pomocí 1D-CNN, doplněné o unsupervised zero-shot transfer přístup, který umožňuje aplikovat model i na data z jiných lokalit bez dalšího trénování. V testovacích oblastech ve Wu-chanu dosáhl model přesnosti 95,95 % (Kappa = 0,9459) a 89,70 % (Kappa = 0,8628). Tyto výsledky ukazují, že metoda je robustní i v různých podmínkách.

## Proč je to důležité
Tento výzkum představuje významný krok směrem k automatizaci monitorování dopravní infrastruktury. Schopnost rychle a přesně identifikovat degradované úseky vozovek umožňuje efektivnější plánování údržby, snížení nákladů a zvýšení bezpečnosti silničního provozu. I když se nejedná o průlom v AI jako takové, ukazuje praktické využití hlubokého učení v oblasti civilního inženýrství a geoinformatiky, kde jsou podobné aplikace stále vzácné. Metoda může být v budoucnu integrována do systémů inteligentní správy dopravní infrastruktury, zejména v městských aglomeracích s rozsáhlými silničními sítěmi.

---

[Číst původní článek](https://www.nature.com/articles/s41598-025-29966-4)

**Zdroj:** 📰 Nature.com
