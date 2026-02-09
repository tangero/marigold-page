---
author: Marisa Aigen
category: neuroprotézy
date: '2026-02-08 00:00:00'
description: Dekódování motorických záměrů z periferních nervů zůstává náročné. Autoři
  nahrávali intraneurální aktivitu sciatického nervu u pacientů s transfemorální amputací
  a použili spiking neural network k dekódování pohybů fantomové nohy. Tyto nálezy
  podporují vývoj obousměrně neurálně řízených protéz.
importance: 4
layout: tech_news_article
original_title: Decoding phantom limb movements from intraneural recordings
publishedAt: '2026-02-08T00:00:00+00:00'
slug: decoding-phantom-limb-movements-from-intraneural-r
source:
  emoji: 📰
  id: null
  name: Nature.com
title: Dekódování pohybů fantomové končetiny z intraneurálních nahrávek
url: https://www.nature.com/articles/s41467-026-69297-0
---

## Souhrn
Výzkumníci provedli intraneurální nahrávky z distálních větví sciatického nervu u dvou pacientů s transfemorální amputací nohy. Pomocí transversal intrafascicular multichannel electrodes (TIME) identifikovali multiunit activity spojenou s voličními pohyby fantomové nohy, jako jsou pohyby kolene, kotníku a prstů. Spiking neural network sloužící k dekódování těchto pohybů překonal konvenční metody a po integraci s intermuskulárními signály dosáhl vyšší přesnosti.

## Klíčové body
- Nahrávání multiunit activity s modulací specifickou pro klouby (koleno, kotník, prsty) a směry pohybu napříč elektrodami.
- Spiking neural network decoder překonal lineární diskriminační analýzu (LDA) a Kalmanův filtr v predikci pokusů o pohyb.
- Integrace intraneurálních signálů s povrchovými EMG signály z reziduálních svalů zlepšila výkon dekodéru.
- Minimální překrytí mezi motorickými a senzorickými mapami v sciatickém nervu naznačuje časnou segregaci signálů.
- Všechna data a kód jsou volně dostupné na GitHubu (https://github.com/rossicecilia/intraneural_phantom_leg.git).

## Podrobnosti
Amputace dolní končetiny vede k výrazným sensorimotorickým deficitům, které protézy nedokážou plně kompenzovat. Přímé nahrávání signálů z reziduálních periferních nervů představuje biomimetický přístup k ovládání protéz, ale nízké amplitudy signálů a obtíže s interfacingem nervů brzdily jeho adopci. Autoři implantovali TIME elektrody – vícekanálové intrafascikulární elektrody procházející příčně fascikuly nervu – do distálních větví sciatického nervu u dvou pacientů s amputací stehna. Tyto elektrody umožnily stabilní přístup k motorickým signálům ze ztracených svalů.

Během experimentů pacienti vykonávali voliční pohyby fantomové nohy, jako flexe/extenze kolene, dorsální/plantární flexi kotníku nebo pohyby prstů. Nahrávaná multiunit activity vykazovala modulaci specifickou pro jednotlivé klouby a směry, distribuovanou napříč kanály elektrod. Pro dekódování pohybů použili spiking neural network (SNN), který simuluje biologické spiking neuronů a je vhodný pro zpracování časově variabilních neurálních signálů. SNN decoder predikoval pokusy o pohyb s vyšší přesností než tradiční regresory, jako LDA nebo Kalmanův filtr. Další zlepšení přinesla fúze intraneurálních dat s povrchovými EMG signály z reziduálních svalů stehna, což ukazuje na komplementární informace z těchto zdrojů.

Motorické a senzorické mapy v nervu vykazovaly minimální překrytí, což potvrzuje segregaci signálů již v periferním sciatickém nervu. Studie zahrnuje podrobný protokol klinického výzkumu a poskytuje deidentifikovaná data pro reprodukovatelnost. Omezením je malý počet participantů (dvě osoby), což vyžaduje validaci na větší kohortě, ale kvalita nahrávek a dostupnost dat umožňují další analýzy.

## Proč je to důležité
Tento výzkum posouvá oblast brain-computer interfaces (BCI) směrem k periferním nervům, podobně jako Neuralink zaměřený na centrální nervový systém. Umožňuje vývoj obousměrných protéz, kde pacient ovládá protézu myšlenkou (effrentní signály) a zároveň dostává senzorický feedback (afferentní signály). V praxi to znamená přirozenější chůzi bez nutnosti tréninku na myoelektrické signály, které jsou náchylné k únavě svalů. Pro průmysl to otevírá cestu k komerčním neuroprotézám s vyšší autonomií, snižuje zátěž na baterie a zlepšuje mobilitu amputovaných. V širším kontextu podtrhuje roli SNN v neurotechnologiích, kde tradiční feedforward modely selhávají na spiking datech, a podporuje open science díky plné dostupnosti dat a kódu.

---

[Číst původní článek](https://www.nature.com/articles/s41467-026-69297-0)

**Zdroj:** 📰 Nature.com
