---

author: Marisa Aigen
category: ai čipy
companies:
- Taalas Inc
date: '2026-02-20 01:22:59'
description: Startup Taalas Inc., který vyvíjí čipy optimalizované pro provoz specifických
  modelů umělé inteligence, získal 169 milionů dolarů financování. Mezi investory
  jsou Quiet Capital, Fidelity a polovodičový investor Pierre Lamond, celková podpora
  přesahuje 200 milionů dolarů.
importance: 4
original_title: Taalas raises $169M in funding to develop model-specific AI chips
publishedAt: '2026-02-20T01:22:59+00:00'
slug: taalas-raises-169m-in-funding-to-develop-model-spe
source:
  emoji: 📰
  id: null
  name: SiliconANGLE News
title: Taalas získal 169 milionů dolarů na vývoj AI čipů specifických pro jednotlivé
  modely
url: https://siliconangle.com/2026/02/19/taalas-raises-169m-funding-develop-model-specific-ai-chips/
urlToImage: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2026/02/Taalas.png
urlToImageBackup: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2026/02/Taalas.png
---

## Souhrn
Startup Taalas Inc. získal 169 milionů dolarů v nové investiční kole, které celkové financování navýšilo na více než 200 milionů dolarů. Společnost se zaměřuje na vývoj čipů přizpůsobených konkrétním modelům umělé inteligence, její první produkt cílí na open-source jazykový model Llama 3.1 8B. Tento čip dosahuje výrazně vyšší výkonnosti než standardní grafické karty Nvidia H200 při nižší spotřebě energie.

## Klíčové body
- Financování 169 milionů dolarů od investorů včetně Quiet Capital, Fidelity a Pierra Lamonda.
- První čip optimalizovaný pro Llama 3.1 8B generuje 17 000 výstupních tokenů za sekundu, což je 73násobek výkonu Nvidia H200.
- Spotřeba energie je jen 1/10 oproti H200 díky přizpůsobení hardwaru modelu.
- Customizace pouze dvou z více než 100 vrstev čipu s mask ROM recall fabric pro efektivní zpracování dat.
- Architektura využívá jeden tranzistor na modul pro maticové násobení, což snižuje náklady na vývoj.

## Podrobnosti
Taalas Inc. je startup specializující se na návrh polovodičových čipů, které jsou optimalizovány pro běh konkrétních modelů umělé inteligence, na rozdíl od univerzálních grafických procesorů (GPU) jako Nvidia H200. Tyto GPU jsou navrženy pro široké spektrum úloh, včetně hraní her nebo obecného výpočtu, což vede k zbytečným komponentám pro specifické AI workloady. Taalas tento problém řeší tím, že upravuje pouze dvě klíčové vrstvy z celkových více než 100 vrstev čipu. Většina vrstev obsahuje podpůrné prvky jako vedení pro přenos dat mezi sekcemi čipu, zatímco tranzistory jsou soustředěny v několika vrstvách.

Customizované vrstvy Taalas využívají mask ROM recall fabric, což je typ paměti ROM (read-only memory), kam lze data zapsat jedinkrát a následně je jen číst, ne upravovat. Každý modul této struktury ukládá čtyři bity dat a zpracovává je pomocí jediného tranzistoru, který provádí maticové násobení – základní operaci v neuronových sítích jazykových modelů. Tento přístup umožňuje nahradit nevyužitou paměť DRAM (dynamickou náhodnou přístupovou paměť) extra tranzistory, což zrychluje inference modelu Llama 3.1 8B. Tento model, vyvinutý Meta AI, je open-source velký jazykový model s 8 miliardami parametrů, vhodný pro generování textu, překlady nebo analýzu dat.

Výkon čipu Taalas dosahuje 17 000 výstupních tokenů za sekundu při spotřebě jen desetiny oproti H200, což znamená efektivnější provoz v datových centrech. Plný vývoj custom čipu je obvykle příliš drahý pro většinu AI projektů, proto Taalas snižuje náklady omezením úprav na minimum vrstev. Podle zdrojů jako Next Platform tato architektura umožňuje škálovat na další modely, ale zatím je první produkt zaměřený na Llama 3.1 8B.

## Proč je to důležité
Tento vývoj posiluje konkurenci v oblasti AI hardwaru, kde Nvidia dominuje s 80–90procentním podílem na trhu GPU pro AI. Specializované čipy mohou snížit závislost na Nvidia, zejména pro open-source modely jako Llama, kde efektivita při inference ovlivňuje náklady na nasazení v produkci. Pro průmysl to znamená potenciálně nižší provozní náklady v cloudu nebo edge zařízeních, kde spotřeba energie hraje klíčovou roli. Nicméně úspěch závisí na škálovatelnosti – customizace pro jeden model omezuje flexibilitu oproti univerzálním GPU. V širším kontextu AI ekosystému podporuje trend specializace hardwaru (např. Google TPU nebo Grok chips), což urychluje adopci LLM v reálných aplikacích jako chatboti nebo automatizace, ale vyžaduje koordinaci s vývojáři modelů.

---

[Číst původní článek](https://siliconangle.com/2026/02/19/taalas-raises-169m-funding-develop-model-specific-ai-chips/)

**Zdroj:** 📰 SiliconANGLE News
