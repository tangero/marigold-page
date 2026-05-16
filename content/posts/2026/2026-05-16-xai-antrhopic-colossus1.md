---
title: Proč xAI pronajalo konkurenčnímu Anthropic svůj datový cluster Colossus 1?
slug: xai-antrhopic-colossus1
author: Patrick Zandl
categories:
  - AI
summary_points: []
thumbnail: colossusSite.webp
audio_url: ''
hide: false
---

xAI v květnu 2026 pronajalo Anthropicu celý datový cluster Colossus 1 v Memphisu — 220 000 GPU, 300 MW výkonu. Většina komentářů to četla jako kapitulaci: Musk buduje AI lab za miliardy, pak předá klíče přímému konkurentovi. Jenže za tím rozhodnutím stojí konkrétní technické důvody, které z toho dělají spíš chytrou rotaci aktiv než bílou vlajku. 

## Colossus 1: rekordní cluster, který nefungoval

Colossus 1 vznikl rychle a s velkým humbukem. xAI do něj nasadilo přes 220 000 NVIDIA GPU — odhadem 150 000 H100, 50 000 H200 a 20 000 GB200. Tři různé generace křemíku v jednom clusteru. Architektura, které se říká heterogenní, a která pro distribuovaný trénink modelů představuje zásadní problém.

Důvod je prostý. Při distribuovaném tréninku musí všechny GPU dokončit jeden výpočetní krok současně, než cluster postoupí na další. Pokud GB200 skončí první, čeká na posledního H100 — nebo na jakýkoli čip, který narazil na problém se síťovým stackem. Tomuto jevu se říká _straggler efekt_ a v praxi znamená, že rychlost celého clusteru určuje nejpomalejší článek. Výsledek: MFU (Model FLOP Utilization — podíl teoretického výkonu, který cluster skutečně využije) se u xAI pohybovalo kolem 11 %. Meta a Google dosahují 40 % a více.

Nedosti na tom. Pak ještě přišel problém s GB200. Blackwell GPU odebírají výkon tak agresivně, že čip obsahuje hardwarový mechanismus pro vyhlazování příkonu. Software stack xAI byl optimalizovaný pro starší architekturu Hopper — a když GB200 namáhal nepravidelnou zátěží, hardware se fyzicky poškozoval. Doslova se tavil. Přepsat celý software stack od základu je práce na měsíce, ne týdny.

Výsledek: cluster za miliardy dolarů, který při tréninku frontier modelů nedosahoval ani čtvrtiny efektivity konkurence.

## Proč inference funguje tam, kde trénink selhal

Inference — tedy obsluha dotazů od skutečných uživatelů — má zásadně jiné nároky než trénink. A tady heterogenní architektura přestává být problémem.

Při inferenci GPU nezpracovávají jeden společný krok synchronně. Každý dotaz je relativně samostatná jednotka práce, která se rozdělí mezi dostupné čipy paralelně. Straggler efekt prakticky mizí — pokud jeden H100 trvá o trochu déle, nezastaví zbytek clusteru. Smíšená generace GPU najednou nevadí.

Druhý faktor je síťový šum. Ve velkých clusterech sdílených mezi více zákazníky vzniká tzv. _network jitter_ — nepředvídatelné latence způsobené tím, že různí nájemci generují provoz najednou. Anthropic obsadilo všech 220 000 GPU jako jediný tenant. Jitter prakticky zmizel.

Z technického pohledu je to téměř ideální situace: cluster, který byl noční můrou pro trénink, se stal přirozeným prostředím pro obsluhu miliard Claude dotazů. Dvě technické slabiny — heterogenní architektura a multi-tenancy jitter — se vzájemně neutralizovaly přechodem na jiný typ workloadu.

## Finanční logika: z technického dluhu na 6 miliard ročně

xAI mezitím dokončilo Colossus 2 — cluster postavený výhradně na Blackwell GPU, homogenní architektura, bez kompromisů. Trénink nových modelů přesunulo tam. Colossus 1, jehož přepsání software stacku by trvalo měsíce a výsledek by stále zaostával za homogenním clusterem, pronajalo Anthropicu.

Cena leasingu se pohybuje kolem 2,60 USD za GPU a hodinu (vážený průměr přes různé typy čipů). Při 220 000 GPU a plném vytížení to vychází na 5–6 miliard USD ročně. Podle [analýzy @jukan05](https://x.com/jukan05/status/2052957921563316619) toto číslo téměř přesně odpovídá anualizované čisté ztrátě xAI za první čtvrtletí 2026.

Jinými slovy: jeden deal přetáhl xAI z červených čísel na cca nulu. A to ještě před tím, než Colossus 2 začne generovat vlastní příjmy z Groku.

Kontext je důležitý. xAI se v roce 2026 sloučilo se SpaceX do entity SpaceXAI, která míří na IPO při valuaci 1,75 bilionu USD — a termín se spekuluje na červen 2026. Narativ _"AGI lab spalující peníze"_ je pro investory výrazně méně atraktivní než _"infrastrukturní pronajímatel stabilně generující cash flow."_ Pronájem clusteru Colossus 1 tento příběh mění jedním tahem do kýžené roviny. Zda je to geniální strategie nebo nutná improvizace po architektonickém průšvihu, záleží na úhlu pohledu — pravděpodobně obojí zároveň.

## A co když to prostě bylo jinak?

Příběh, který právě čtete, má jeden háček: stojí z velké části na jednom vlákně analytika korejské Mirae Asset Securities, publikovaném na X/Twitter začátkem května a řadou médií byl bez většího rozboru nekriticky přejat. Tvrzení o tavících se Blackwellech, o softwaru, který je třeba přepsat od základu, i konkrétní rozdělení 150 000 H100 / 50 000 H200 / 20 000 GB200 nepocházejí z xAI ani z Anthropicu. Jsou to rekonstrukce jednoho pozorovatele a tweety bývalých zaměstnanců. Mirae Asset je velký korejský broker s přímým zájmem na úspěchu chystaného IPO. To neznamená, že analýza je nepravdivá. Znamená to, že dost možná existuje prozaičtější výklad téhož dealu, který nenabízí žádné geniální plánování.

Ten výklad zní takto: Anthropic v prvním čtvrtletí 2026 zaznamenal podle vlastních slov Daria Amodeie osmdesátinásobný růst tržeb - místo plánovaného desetinásobku - a infrastruktura toto tempo přestala stíhat. Když potřebujete 220 000 GPU během měsíce, nestavíte datacentrum, berete to, co je hned. xAI zase má hardware, který nedokáže plně vytížit vlastním produktem - Grok deprecation 4.1 Fast s pouhým dvoutýdenním předstihem, oznámený den před dealem, signalizuje, že API byznys xAI moc neběží. Mimochodem - sám Musk si v podmínkách dealu vyhradil právo _"compute vzít zpět"_, pokud se mu Claude přestane líbit z hlediska "ne/škodění lidstvu". Co tento pojem znamená, definuje Musk sám. Pro firmu, která se profiluje na bezpečnosti AI, je to nepříjemný kompromis. Příběh o _"geniální rotaci aktiv"_ tedy možný je. Ale stejně tak možný je příběh "Anthropic platí 5 miliard ročně, aby se neutopil ve vlastní popularitě, a xAI bere ty peníze, protože vlastní produkt mu nefrčí". Obě varianty jsou pravdivé naráz - jen každá vypadá lépe pro jiné publikum.

## Co to znamená pro české vývojáře a firmy používající Claude

Praktický dopad přišel rychle. Od 6. května 2026 Anthropic zdvojnásobil limity pro Claude Code i API — a to je přímý důsledek toho, že najednou má k dispozici 220 000 GPU navíc. Latence Claude v EU podle dostupných informací klesla přibližně o 50 %.

Pro české AI startupy a vývojáře to znamená konkrétní věci. Rate-limit bolest — ta situace, kdy v půlce agentní session dostanete _429 Too Many Requests_ — by měla být výrazně méně častá. Produkční nasazení Claude agentů se stávají stabilnějšími. Rychlejší inference znamená kratší čekání v multi-turn konverzacích, kde každý krok závisí na výsledku předchozího.

Část kapacity Colossus 1 jde do Asie a Evropy přes AWS kvůli datové lokalizaci — pro české firmy s požadavky na GDPR to může být relevantní detail, i když konkrétní podmínky Anthropic zatím podrobně nespecifikoval. 

## Větší obraz: éra compute leasingu a co z ní plyne

Colossus 1 deal není izolovaná událost. Je součástí širšího trendu, kdy vlastnit GPU přestává být nutnou podmínkou pro provoz AI infrastruktury. CoreWeave, Lambda Labs, nyní xAI jako "neo-cloud" — hyperscale leasing se stává standardním modelem. Vývojáři a firmy platí za GPU-hodiny, ne za hardware.

Pro xAI to ale přináší otázku, kterou někteří komentátoři v reakcích na původní analýzu formulovali přesně: xAI se vzdalo 40 % své celkové GPU kapacity v době, kdy poptávka po inferenci globálně roste. Co se stane, až Grok — trénovaný na Colossus 2 — dosáhne úrovně, kde bude potřebovat masivní inference kapacitu? Colossus 1 bude obsazený Claudem. Smlouva s Anthropicem je dlouhodobá, podmínky nejsou veřejné, takže nevíme... 

Je možné, že xAI vsadilo na to, že Grok inference poptávka poroste pomaleji, než poroste kapacita Colossus 2. Je možné, že deal obsahuje klauzule o předčasném ukončení. Zatím to neumíme nezávisle ověřit.
