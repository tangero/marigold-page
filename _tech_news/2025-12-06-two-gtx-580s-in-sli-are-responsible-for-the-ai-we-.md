---
author: Marisa Aigen
category: ai
companies:
- Nvidia
date: '2025-12-06 13:00:00'
description: Šéf Nvidia Jensen Huang v nedávném podcastu Joea Rogana prohlásil, že
  vynálezci deep learningu spustili první síť strojového učení na dvojici GTX 580
  v SLI v roce 2012. Výzkumníci z University of Toronto tak položili základy současné
  éry umělé inteligence.
importance: 3
layout: tech_news_article
original_title: Two GTX 580s in SLI are responsible for the AI we have today — Nvidia's
  Huang revealed that the invention of deep learning began with two flagship Fermi
  GPUs in 2012
people:
- Jensen Huang
publishedAt: '2025-12-06T13:00:00+00:00'
slug: two-gtx-580s-in-sli-are-responsible-for-the-ai-we-
source:
  emoji: 📰
  id: null
  name: Tom's Hardware UK
title: Dva GTX 580 v SLI jsou zodpovědné za dnešní AI – Nvidia šéf Huang odhalil,
  že vynález deep learningu začal na dvou vlajkových Fermi GPU v roce 2012
url: https://www.tomshardware.com/tech-industry/artificial-intelligence/two-gtx-580s-in-sli-are-responsible-for-the-ai-we-have-today-nvidias-huang-revealed-that-the-invention-of-deep-learning-began-with-two-flagship-fermi-gpus-in-2012
urlToImage: https://cdn.mos.cms.futurecdn.net/SeFR7XjGGqt3DeeARQcBRb-2560-80.jpg
urlToImageBackup: https://cdn.mos.cms.futurecdn.net/SeFR7XjGGqt3DeeARQcBRb-2560-80.jpg
---

### Souhrn
Šéf Nvidia Jensen Huang v podcastu Joea Rogana (#2422) odhalil, že deep learning, základ současné AI, vznikl na dvou grafických kartách GTX 580 v konfiguraci SLI v roce 2012. Tyto karty, původně určené pro hraní her, použili výzkumníci Alex Krizhevsky, Ilya Sutskever a Geoffrey Hinton z University of Toronto k trénování sítě AlexNet. Tento model dramaticky zlepšil rozpoznávání obrázků a stal se průlomem v počítačovém vidění.

### Klíčové body
- GTX 580 (Fermi architektura, 3 GB GDDR5 paměti) byly první grafickými kartami, které spustily deep learning síť.
- AlexNet měla 8 vrstev a přibližně 60 milionů parametrů, kombinovala konvoluční vrstvy s hlubokými neuronovými sítěmi.
- Síť byla optimalizována pro dvě GPU v SLI, data se vyměňovala jen nutně, což zkrátilo trénink.
- V roce 2012 překonala AlexNet předchozí algoritmy o více než 70 % v úspěšnosti rozpoznávání obrázků na soutěži ImageNet.
- Nvidia tehdy investovala převážně do 3D grafiky a her, ne do AI.

### Podrobnosti
V roce 2011 výzkumníci z University of Toronto – Geoffrey Hinton, známý jako otec deep learningu, jeho student Ilya Sutskever (později spoluzakladatel OpenAI) a Alex Krizhevsky – hledali lepší metody pro rozpoznávání obrázků v počítačovém vidění. Tehdejší přístupy spoléhali na ručně navržené algoritmy detekující hrany, rohy a textury, což bylo pracné a neefektivní. Místo toho vytvořili AlexNet, architekturu hluboké neuronové sítě s osmi vrstvami, která se učí sama z dat pomocí konvolučních vrstev (convolutional layers), které extrahují vlastnosti jako tvary a objekty, a plně propojených vrstev pro finální klasifikaci.

Trénování probíhalo na dvou GTX 580, grafických kartách z řady Fermi vydaných v roce 2010. Každá měla 512 CUDA jader, 3 GB GDDR5 paměti a podporu SLI pro paralelní zpracování. CUDA, programovací platforma Nvidia pro paralelní výpočty na GPU, umožnila převést složité výpočty neuronových sítí na grafický hardware. Síť byla rozdělena mezi dvě karty, přičemž data se synchronizovala jen minimálně, což snížilo latenci a umožnilo trénovat na datasetu ImageNet s 1,2 milionu obrázků za rozumný čas – několik dní místo týdnů na CPU.

Na konferenci ImageNet Large Scale Visual Recognition Challenge v roce 2012 dosáhla AlexNet chybovosti 15,3 %, oproti 26,2 % u druhého místa. Tento skok – relativní zlepšení přes 70 % – upoutal pozornost akademiků i průmyslu. Bez GPU by deep learning zůstal neproveditelný kvůli výpočetní náročnosti; CPU nestačily na miliony parametrů a velké datasety. Nvidia tehdy CUDA propagovala hlavně pro fyzikální simulace a rendering, ne AI, přesto tento experiment ukázal potenciál konzumerního hardware.

### Proč je to důležité
Toto odhalení podtrhuje, jak neúmyslné použití herních GPU katalyzovalo revoluci v AI. GTX 580 nebyly navrženy pro machine learning, ale díky paralelizaci CUDA umožnily škálovat trénink neuronových sítí, což vedlo k dominanci Nvidia na trhu AI hardware dnes (např. H100, Blackwell). Pro průmysl znamená, že deep learning není jen o sofistikovanejších modelech jako GPT-4, ale o hardwarové podpoře – bez ní by současné velké jazykové modely (LLM) nebo autonomní systémy neexistovaly. Kriticky: přestože AlexNet byl průlom, dne se ukazuje, že škálování na tisíce GPU vede k úbytku efektivity (scaling laws se zpomalují), což klade otázky na budoucnost bez nových architektur. Pro uživatele to znamená, že AI nástroje jako image generátory (Stable Diffusion) nebo rozpoznávače tváří vycházejí z tohoto základu, ale závisí na dostupnosti výpočetního výkonu.

---

[Číst původní článek](https://www.tomshardware.com/tech-industry/artificial-intelligence/two-gtx-580s-in-sli-are-responsible-for-the-ai-we-have-today-nvidias-huang-revealed-that-the-invention-of-deep-learning-began-with-two-flagship-fermi-gpus-in-2012)

**Zdroj:** 📰 Tom's Hardware UK
