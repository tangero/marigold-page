---
author: Marisa Aigen
category: kvantové počítače
date: '2026-01-22 00:00:00'
description: Kvantové kódy low-density parity-check pro korekci chyb slibují vysoký
  výkon, ale vyžadují interakce mezi vzdálenými qubity. Dva z těchto kódů byly úspěšně
  implementovány na suprachiovodivém zařízení s 32 qubity.
importance: 4
layout: tech_news_article
original_title: Demonstration of low-overhead quantum error correction codes
publishedAt: '2026-01-22T00:00:00+00:00'
slug: demonstration-of-low-overhead-quantum-error-correc
source:
  emoji: 📰
  id: null
  name: Nature.com
title: Demonstrace kódů pro kvantovou korekci chyb s nízkou režii
url: https://www.nature.com/articles/s41567-025-03157-4
urlToImage: https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41567-025-03157-4/MediaObjects/41567_2025_3157_Fig1_HTML.png
urlToImageBackup: https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41567-025-03157-4/MediaObjects/41567_2025_3157_Fig1_HTML.png
---

### Souhrn
Výzkumníci demonstrovali na 32qubitovém kvantovém procesoru dva low-overhead kódy pro kvantovou korekci chyb: distance-4 bivariate bicycle code s čtyřmi logickými qubity a distance-3 punctured bivariate bicycle code se šesti logickými qubity. Tyto kódy umožnily současné měření všech stabilizátorů hmotnosti 6 pomocí efektivního obvodu pro extrakci syndromu. Dosahují logické chybovosti na logický qubit na cyklus 8,91 % resp. 7,77 %.

### Klíčové body
- Použití 32qubitového suprachiovodivého procesoru s dvourozměrnou architekturou a překrývajícími se dlouhodobými spojovacími prvky mezi qubity.
- Demonstrace distance-4 bivariate bicycle code (4 logické qubity) s chybovostí 8,91 ± 0,17 % na cyklus.
- Distance-3 punctured bivariate bicycle code (6 logických qubitů) s chybovostí 7,77 ± 0,12 % na cyklus.
- Současné měření všech nelokálních stabilizátorů hmotnosti 6 prostřednictvím periodického provádění syndromového obvodu.
- Potvrzení proveditelnosti kvantové korekce chyb na procesorech se suprachiovodivými qubity spojenými dlouhodobými spojovacími prvky.

### Podrobnosti
Kvantové počítače slibují řešení komplexních výpočetních problémů, které překonávají klasické počítače, ale kvantová informace je křehká a operace s ní jsou náchylné k chybám. Proto je klíčová kvantová korekce chyb, která umožňuje fault-tolerantní výpočty. Doposud demonstrované kódy, jako surface codes, mají nízkou encoding efficiency a vysokou režii na zdroje, což brání škálovatelnosti.

Tento experiment využil 32qubitový kvantový procesor se suprachiovodivými qubity uspořádanými ve dvourozměrné architektuře. Qubity jsou propojeny překrývajícími se long-range couplers, což umožňuje interakce mezi vzdálenými qubity nutné pro quantum low-density parity-check (LDPC) kódy. Tyto kódy mají řídkou strukturu kontrolních matic, což snižuje počet potřebných měření stabilizátorů oproti tradičním kódům.

Testované kódy patří do rodiny bivariate bicycle codes. První, distance-4 bivariate bicycle code, kóduje 4 logické qubity a vyžaduje měření stabilizátorů hmotnosti až 6. Druhý, distance-3 punctured verze, kóduje 6 logických qubitů po puncturování (odstranění některých qubitů pro zjednodušení). Syndromový obvod umožnil periodické a současné měření všech nelokálních stabilizátorů, což je výzva kvůli potřebě dlouhodobých interakcí.

Měřené logické chybové míry – 8,91 % pro první kód a 7,77 % pro druhý na cyklus – ukazují, že tyto kódy fungují na fyzickém hardwaru, i když jsou stále nad prahem pro fault-tolerance (obvykle pod 1 %). Procesor umožnil efektivní implementaci díky překrytí couplers, což minimalizuje overhead spojů.

### Proč je to důležité
Tato demonstrace potvrzuje proveditelnost low-overhead LDPC kódů na suprachiovodivých procesorech, které mají vyšší encoding efficiency než surface codes (např. více logických qubitů na fyzický qubit). To je klíčové pro škálování kvantových počítačů k tisícům logických qubitů nutným pro praktické aplikace, jako simulace molekul nebo optimalizace. Snižuje režii na qubity a měření, což urychluje cestu k fault-tolerantním systémům u firem jako IBM nebo Google. Nicméně chybové míry jsou stále vysoké, což vyžaduje další zlepšení fyzického hardwaru a dekódovacích algoritmů. V širším kontextu posiluje to důvěru v LDPC kódy jako alternativu k surface codes pro budoucí kvantové architektury.

---

[Číst původní článek](https://www.nature.com/articles/s41567-025-03157-4)

**Zdroj:** 📰 Nature.com
