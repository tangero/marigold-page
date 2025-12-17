---
author: Patrick Zandl
categories:
- AI
- Meta
- Alibaba
- Qwen
- Llama
- open-source
layout: post
post_excerpt: Meta údajně používá čínský model Qwen od Alibaby k trénování nového AI modelu Avocado. Jde o zásadní obrat oproti situaci před dvěma lety, kdy čínské firmy stavěly na americké Llamě.
summary_points:
- Meta podle Bloomberg používá Qwen od Alibaby k trénování uzavřeného modelu Avocado
- Čínské open-source modely poprvé předstihly americké v celosvětových stahováních
- Llama 4 zklamala vývojářskou komunitu slabým výkonem a kontroverzními benchmarky
- Yann LeCun odchází z Meta založit vlastní startup zaměřený na world models
- Meta najala 28letého Alexandr Wanga za 14,3 miliardy dolarů jako nového šéfa AI
- Distilace modelů představuje právně i eticky spornou techniku v AI průmyslu
title: Meta údajně trénuje nový model na čínském Qwen. Jak si stojí v AI závodu?
thumbnail: https://www.marigold.cz/assets/yann-lecun.jpeg
---

Před dvěma lety čínské technologické firmy stavěly své jazykové modely na základech americké Llamy od Meta a západní analytici to interpretovali jako důkaz zaostávání Číny v oblasti umělé inteligence. Dnes se role obrátily. Podle zprávy Bloomberg Meta používá open-source model [Qwen](https://huggingface.co/Qwen) od čínské Alibaby jako jeden ze zdrojů pro trénování svého nového modelu s kódovým označením Avocado. Tento vývoj ilustruje zásadní posun v globální konkurenci velkých jazykových modelů. A přináší otázky ohledně schopností Meta inovovat v oblasti AI.

Projekt Avocado vzniká v nově zřízené laboratoři TBD Lab v rámci divize Meta Superintelligence Labs. Podle Bloombergu tým provádí takzvanou distilaci: kontroverzní techniku, při které se výstupy existujících modelů používají k urychlení trénování nového modelu. Kromě Qwen využívá TBD Lab také modely Gemma od Google a gpt-oss od OpenAI. Důležitým aspektem je plánovaný přechod k uzavřenému modelu: Avocado má být dostupné pouze přes API, což představuje odklon od dosavadní open-source strategie, kterou Meta prosazovala s řadou Llama.

## Proč Meta sahá po čínských modelech

Proč? Zklamání z modelu [Llama 4](https://ai.meta.com/llama/), který Meta představila v dubnu 2025. Přestože společnost prezentovala model jako průlomový, nezávislé testování ukázalo podstatně horší výsledky, než naznačovaly interní benchmarky. Na platformě LiveBench se model Llama 4 Maverick umístil na dvacátém místě a zaostal za konkurenčními modely GPT-4o a Gemini 2.0 Flash. Situaci zhoršily kontroverze kolem způsobu testování, když Meta použila pro hodnocení na LMArena experimentální verzi modelu, která nebyla veřejně dostupná.

Rootly AI Labs provedla nezávislé testování a zjistila, že Llama 4 v programátorských úlohách výrazně zaostává za předchozí generací Llama 3 i za specializovanými modely od Alibaby a OpenAI. Diskrepance mezi marketingovými tvrzeními Meta a reálným výkonem vedla k poklesu důvěryhodnosti a otevřela prostor pro alternativy. Kromě toho Zuckerberg v AI komunitě začal působit poněkud... nevěrohodně... 

Mezitím čínské modely zaznamenaly prudký růst. Podle studie MIT a Hugging Face publikované v listopadu 2025 čínské open-source modely poprvé předstihly americké v podílu na celosvětových stahováních: 17,1 procenta oproti 15,8 procenta. Většinu tohoto podílu tvoří modely DeepSeek a Qwen. Model Qwen od Alibaby, konkrétně verze [Qwen3](https://www.alibabacloud.com/blog/alibaba-introduces-qwen3-setting-new-benchmark-in-open-source-ai-with-hybrid-reasoning_602192), dosáhl k prosinci 2025 přibližně 385 milionů stažení na platformě Hugging Face a předstihl tak Llamu s 346 miliony.

## Organizační změny v Meta AI

Rok 2025 přinesl zásadní reorganizaci AI aktivit Meta. V červnu společnost investovala 14,3 miliardy dolarů do firmy Scale AI, čímž získala 49procentní podíl oceňující startup na více než 29 miliard dolarů. Součástí dohody byl příchod zakladatele Scale AI, osmadvacetiletého Alexandra Wanga, na pozici prvního Chief AI Officer v historii Meta. Wang nyní vede [Meta Superintelligence Labs](https://www.meta.com/media-gallery/executives/alexandr-wang/) a dohlíží na vývoj modelu Avocado.

Wang před příchodem do Meta budoval Scale AI od roku 2016, kdy jako devatenáctiletý odešel z MIT. Firma se specializuje na přípravu dat pro trénování AI modelů a spolupracovala s většinou předních laboratoří v oboru. Wang je zastáncem uzavřených modelů, což kontrastuje s dosavadním směřováním Meta. A intenzivní zapojení Marka Zuckerberga do každodenního řízení AI projektů má vyvolávat interní napětí. 

Napětí se projevilo rozhodnutím Yanna LeCuna opustit Meta na konci roku 2025. LeCun, nositel Turingovy ceny a jeden z průkopníků hlubokého učení, založil v roce 2013 laboratoř FAIR (Fundamental AI Research) a dvanáct let formoval výzkumnou strategii společnosti. V listopadu oznámil záměr založit vlastní startup zaměřený na takzvané _world models_ – systémy schopné porozumět fyzickému světu a plánovat komplexní akce. LeCun dlouhodobě kritizoval přeceňování velkých jazykových modelů a tvrdil, že nepředstavují cestu k obecné umělé inteligenci. Meta bude partnerem jeho nového podniku a bude licencovat vznikající technologie.

Další personální změny postihly samotnou laboratoř FAIR. Joelle Pineau oznámila odchod z pozice vedoucí laboratoře krátce před kontroverzním vydáním Llamy 4. Bývalí zaměstnanci označili FAIR za organizaci procházející „pomalou smrtí", přičemž poukazovali na přesun zdrojů směrem k produktově orientovaným týmům a omezení přístupu k výpočetnímu výkonu pro základní výzkum.

## Distilace jako kontroverzní praxe

Použití distilace k trénování modelu Avocado otevírá právní a etické otázky. Distilace, technika poprvé popsaná Geoffreyem Hintonem v roce 2015, umožňuje přenést znalosti z velkého „učitelského" modelu do menšího „studentského" modelu prostřednictvím analýzy výstupů. V praxi to znamená opakované dotazování existujícího modelu a využití jeho odpovědí jako trénovacích dat.

Právní rámec pro distilaci zůstává nejasný. Podmínky služeb OpenAI, Anthropic, Mistral i xAI obsahují ustanovení zakazující používání jejich výstupů k vývoji konkurenčních modelů. Otázkou je, zda taková ustanovení obstojí při soudním přezkoumání a zda výstupy AI modelů vůbec požívají autorskoprávní ochrany. Americký Úřad pro autorská práva dosud odmítá přiznávat copyright obsahu generovanému plně umělou inteligencí.

Kontroverze kolem distilace eskalovala v lednu 2025, kdy OpenAI obvinila čínskou firmu DeepSeek z neoprávněného využití výstupů ChatGPT. Paradoxem situace je, že OpenAI sama čelí žalobám za využití autorskoprávně chráněného obsahu při trénování svých modelů. Firma argumentuje principem _fair use_. Kritici poukazují na nekonzistentnost pozice, kdy velké společnosti požadují ochranu pro své výstupy, ale samy využívají cizí materiály bez souhlasu.

Alibaby Qwen je vydáván pod licencí Apache 2.0, která v zásadě neomezuje použití včetně distilace. Pokud Meta využívá veřejně dostupné verze Qwen v souladu s licenčními podmínkami, její postup nemusí být právně napadnutelný. Nicméně využívání čínského modelu americkou společností, která současně lobuje za vládní podporu domácího AI průmyslu v soutěži s Čínou, představuje minimálně komunikační výzvu.

## Posun v globální AI konkurenci

Vývoj ilustruje širší trend v oblasti open-source AI. Jensen Huang, generální ředitel Nvidia, začátkem prosince konstatoval, že „Čína je značně napřed v open-source". Čínské laboratoře vydávají nové modely v týdenních intervalech oproti měsíčním cyklům amerických firem. Kombinace algoritmické efektivity a ochoty sdílet výsledky vytváří dynamiku, která přitahuje vývojářskou komunitu.

Qwen dosáhl úspěchu díky několika faktorům: podpoře více než 100 jazyků, pravidelnému vydávání nových verzí v různých velikostech a efektivnímu běhu na dostupném hardwaru. Řada Qwen3 zahrnuje osm modelů od 600 milionů do 235 miliard parametrů, všechny dostupné pod open-source licencí. Podle dat Alibaby generovala rodina modelů Qwen více než 100 000 derivátů (odvozených verzí) na platformě Hugging Face.

Pro Metu představuje současná situace těžké a strategické dilema. Otevřenost modelů Llama byla klíčovým rozdílem oproti uzavřeným systémům OpenAI a Google. Přechod k uzavřenému modelu Avocado smazává tuto odlišnost a staví Meta do přímé konkurence s firmami, které mají v monetizaci AI služeb delší zkušenosti. A jejichž modely jsou výrazně kvalitnější. Současně ztráta vedoucí pozice v open-source segmentu oslabuje argument, že americké hodnoty formují globální AI ekosystém.

| Metrika | Qwen (Alibaba) | Llama (Meta) |
|---------|----------------|--------------|
| Stažení na Hugging Face (prosinec 2025) | ~385 milionů | ~346 milionů |
| Podíl na globálních stahováních | 17,1 % | 15,8 % |
| Počet derivátů na Hugging Face | 100 000+ | méně |
| Licence | Apache 2.0 | Llama Community License |
| Frekvence vydávání | týdně | měsíčně až čtvrtletně |

## Další vývoj

Meta prý plánuje představit model Avocado na jaře 2026. Zda se podaří překonat konkurenci a obhájit pozici v přední linii AI vývoje, či se dostat mezi úplnou elitu, zůstává otevřenou otázkou. Personální změny, odchod klíčových výzkumníků a strategický obrat k uzavřeným modelům představují značné faktory nejistoty.

Situace také naznačuje limity geopolitické rétoriky v technologickém odvětví. Zuckerberg v lednu 2025 na podcastu Joea Rogana varoval před vlivem čínské cenzury na tamní AI modely a prosazoval vládní podporu pro americké firmy. O několik měsíců později jeho společnost využívá čínský model jako jeden ze základních kamenů nejambicióznějšího projektu. Pragmatismus inženýrských týmů se ukazuje být silnější než politické prohlášení.

---

*Zdroje: [Bloomberg](https://www.bloomberg.com/news/articles/2025-12-10/inside-meta-s-pivot-from-open-source-to-money-making-ai-model), [South China Morning Post](https://www.scmp.com/tech/big-tech/article/3336073/ai-race-meta-reported-use-alibabas-qwen-avocado-model-likely-win-china), [MIT/Hugging Face studie](https://news.cgtn.com/news/2025-11-27/China-overtakes-U-S-in-global-open-source-AI-model-market-study-1IEdTnDqRyM/p.html), [Scale AI](https://scale.com/blog/scale-ai-announces-next-phase-of-company-evolution), [CNBC](https://www.cnbc.com/2025/11/19/meta-chief-ai-scientist-yann-lecun-is-leaving-the-company-.html)*
