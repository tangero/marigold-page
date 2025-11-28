---
author: Marisa Aigen
category: dálniční infrastrukt
date: '2025-11-26 00:00:00'
description: Výzkumníci vyvinuli rámec kombinující dálkové snímání, automatické generování
  trénovacích dat a 1D-CNN k rychlému a přesnému hodnocení stárnutí asfaltových vozovek
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
Výzkumníci představili nový rámec pro hodnocení stárnutí asfaltových vozovek v rozsáhlém měřítku, který využívá dálkové snímání, automatické generování trénovacích vzorků a hluboké učení. Metoda eliminuje závislost na časově náročných terénních průzkumech a dosahuje vysoké přesnosti klasifikace.

## Klíčové body
- Využití satelitních dat WorldView-3 pro analýzu stárnutí asfaltu
- Automatické generování trénovacích a validačních vzorků pomocí multi-endmember spektrálního unmixinu a filtru sousedství
- Nasazení jednorozměrné konvoluční neuronové sítě (1D-CNN) s unsupervised zero-shot transfer přístupem
- Celková přesnost klasifikace až 95,95 % a Kappa koeficient 0,9459 v jedné z testovacích oblastí
- Metoda je vhodná pro podporu rozhodování v údržbě silniční infrastruktury a zvyšování dopravní bezpečnosti

## Podrobnosti
Tradiční metody hodnocení stárnutí asfaltových vozovek vyžadují manuální terénní průzkumy, což je nákladné, pomalé a obtížně škálovatelné. Nový přístup využívá satelitní snímky WorldView-3, které poskytují vysoké spektrální a prostorové rozlišení. Na jejich základě výzkumníci automaticky generovali trénovací a validační vzorky pomocí techniky multi-endmember mixed pixel unmixing, která rozkládá smíšené pixely na spektrální komponenty odpovídající různým stupňům stárnutí asfaltu. Následně byla aplikována metoda filtru sousedství pro odstranění šumu a zvýšení kvality dat. Jako klasifikační model byla použita 1D-CNN, doplněná unsupervised zero-shot transfer technikou, což umožnilo efektivní trénování i při omezeném množství anotovaných dat. V testovacích oblastech ve Wu-chanu dosáhl model přesnosti 95,95 % (Kappa = 0,9459) a 89,70 % (Kappa = 0,8628), což svědčí o robustnosti metody i v různých podmínkách.

## Proč je to důležité
Tato metoda představuje významný krok směrem k automatizovanému monitorování silniční infrastruktury. Umožňuje rychle identifikovat úseky vozovek vyžadující údržbu, což může snížit náklady na opravy a zvýšit bezpečnost dopravy. V kontextu rozvoje inteligentních dopravních systémů a smart city řešení je schopnost kontinuálně a bezpečně monitorovat stav infrastruktury klíčová. Přístup je také škálovatelný na celonárodní úrovni a může být integrován do existujících GIS systémů pro správu dopravní infrastruktury.

---

[Číst původní článek](https://www.nature.com/articles/s41598-025-29966-4)

**Zdroj:** 📰 Nature.com
