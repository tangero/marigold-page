---
author: Marisa Aigen
category: kvantové počítače
date: '2025-12-27 05:47:01'
description: Výzkumníci vyvinuli 11-kubitový kvantový procesor na bázi jednotlivých
  atomů v křemíku, který dosahuje fidelití kvantových branek v rozmezí od 99,10 %
  do 99,99 %. Tento výkon představuje klíčový pokrok v křemíkových kvantových technologiích
  směrem k škálovatelným systémům.
importance: 5
layout: tech_news_article
original_title: An 11-qubit atom processor in silicon with all fidelities from 99.10%
  to 99.99% | Hacker News
publishedAt: '2025-12-27T05:47:01+00:00'
slug: an-11-qubit-atom-processor-in-silicon-with-all-fid
source:
  emoji: 📰
  id: hacker-news
  name: Hacker News
title: 11-kubitový atomový procesor v křemíku s fidelitami od 99,10 % do 99,99 %
url: https://news.ycombinator.com/item?id=46344222
---

## Souhrn
Výzkumníci z University of Melbourne a spolupracujících institucí představili 11-kubitový kvantový procesor postavený z atomů fosforu v křemíkové matrici. Procesor vykazuje fidelities kvantových operací od 99,10 % pro dvou-kubitové branky až po 99,99 % pro jednobitové operace, což je mezi nejvyššími hodnotami v křemíkových systémech. Studie publikovaná v Nature zdůrazňuje pokroky v přesnosti umístění atomů a jejich propojení.

## Klíčové body
- 11 qubitů realizovaných jako jednotlivé fosforové atomy v izotopicky čistém křemíku.
- Fidelity jednobitových branek až 99,99 %, dvou-kubitových 99,10 % a čtení 99,5 %.
- Použití precision placement technik, včetně STM (scanning tunneling microscopy) pro přesné umístění atomů.
- Pokroky v řešení problémů s zapojením (wiring) a vysokofidelitních propojeních.
- Kompatibilita s 2D uspořádáním, umožňující surface code pro korekci chyb.

## Podrobnosti
Křemík se dlouho považoval za méně příznivou platformu pro kvantové počítače ve srovnání s supravoďivými obvody nebo iontovými pastmi, ale poslední 2–3 roky přinesly významné pokroky. Tento procesor využívá spinové qubity z fosforových atomů implantovaných do křemíku-28, který je izotopicky čistý, aby se minimalizovaly dekoherenční efekty způsobené spinovou hloubkou jader okolí. Qubity jsou umístěny s nanoměrovou přesností pomocí technik jako scanning tunneling microscopy (STM), navazujících na práci z roku 2012, kde byly atomy přesouvány na požadovaná místa.

Propojení qubitů probíhá elektrostatickými branami, které umožňují dvou-kubitové interakce na bázi kontrolovaného fázového shiftu (CZ branka). Fidelity 99,10 % pro tyto branky znamená, že jen 0,9 % operací selže, což je klíčové pro delší sekvence výpočtů. Procesor demonstroval provedení Groverova algoritmu na 4 qubitech a simulaci molekuly H2, což ukazuje praktickou použitelnost pro malé úlohy. Diskuse na Hacker News zmiňuje související práce: Intel dosáhl 2D uspořádání qubitů (arxiv.org/abs/2412.14918), umožňujícího surface code; HRL Laboratories podobně (arxiv.org/abs/2502.08861); řešení wiring problému (Nature Nanotechnology, 2023) a vysokofidelitní interconnects (Nature, 2025).

Výroba spočívá v implantaci atomů a následném hledání ideálních konfigurací mezi tisíci pokusů, případně přímém umístění STM. I přes náhodné prvky je úspěšnost působivá – pro 11 qubitů včetně skupin po 4–5 propojených atomů. Křemík nabízí výhody kompatibility s CMOS výrobou, což by mohlo usnadnit škálování na tisíce qubitů.

## Proč je to důležité
Tento pokrok posouvá křemíkové qubity blíže k praktickým kvantovým počítačům tím, že dosahuje fidelity nutných pro fault-tolerant výpočty pomocí surface code, kde je požadováno přibližně 99,9 % pro efektivní korekci chyb. V širším kontextu kvantových technologií, kde supravoďivé systémy jako u IBM nebo Google bojují s chlazením a koherenční dobou, křemík slibuje stabilnější qubity při vyšších teplotách díky menší citlivosti na teplotní fluktuace. To by mohlo vést k hybridním systémům, kde křemíkové qubity slouží pro logiku a paměť.

Pro průmysl znamená snížení nákladů na výrobu díky existující silikonové infrastruktuře – Intel a TSMC již investují. Pokud se podaří škálovat na 2D mřížky s tisíci qubity, otevře to cestu k quantum advantage v optimalizaci, simulacích materiálů nebo kryptografii. Nicméně zůstávají výzvy jako prodloužení koherenční doby nad 1 ms a plná 2D integrace. Tento výzkum tak představuje milník v dlouhodobé honbě za univerzálním kvantovým počítačem.

---

[Číst původní článek](https://news.ycombinator.com/item?id=46344222)

**Zdroj:** 📰 Hacker News
