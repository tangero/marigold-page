---
author: Patrick Zandl
categories:
- AI
- Anthropic
- Claude
- jazykové modely
layout: post
post_excerpt: Anthropic uvedl Claude Haiku 4.5, malý model s výkonem srovnatelným s pět měsíců starým Claude Sonnet 4, ale třikrát levnější a dvakrát rychlejší.
summary_points:
- Claude Haiku 4.5 nabízí výkon srovnatelný s Claude Sonnet 4 při třetinových nákladech a více než dvojnásobné rychlosti
- V programování dosahuje Haiku 4.5 73,3 % úspěšnosti na testu SWE-bench, čímž překonává GPT-5 Codex i Gemini 2.5 Pro
- Model je dostupný přes API za cenu 1 dolar za milion vstupních a 5 dolarů za milion výstupních tokenů
- Haiku 4.5 je klasifikován jako ASL-2, což z něj činí bezpečnostně nejbezpečnější model Anthropic
- Model umožňuje orchestraci více instancí pro paralelní zpracování složitých úkolů
- Haiku 4.5 předčí Claude Sonnet 4 v ovládání počítačů a vyniká v úkolах s nízkou latencí
title: Anthropic představil Claude Haiku 4.5, rychlý a dostupný model pro kódování

-----

Anthropic dnes zpřístupnil [Claude Haiku 4.5](https://www.anthropic.com/news/claude-haiku-4-5), malý jazykový model, který přináší výkon blízký hraničním modelům za zlomek ceny. Model, který je dostupný všem uživatelům, nabízí programátorský výkon srovnatelný s pět měsíců starým Claude Sonnet 4, ale při třetinových nákladech a více než dvojnásobné rychlosti zpracování.

![Claude Haiku 4.5 benchmarky](https://www.anthropic.com/images/haiku-4-5-benchmarks.png)

Claude Haiku 4.5 dosahuje výkonu, který by ještě nedávno patřil k nejlepším modelům na trhu. V testu programátorských schopností SWE-bench Verified, který měří schopnost modelů opravovat skutečné chyby v open-source projektech, dosáhl Haiku 4.5 úspěšnosti 73,3 procenta. To je lepší výsledek než GPT-5 Codex s 74,5 procenta nebo Gemini 2.5 Pro se 67,2 procenta. Model tak nabízí kvalitu blízkou mnohem větším modelům při výrazně nižších nákladech.

Haiku 4.5 v některých oblastech překonává i svého staršího sourozence Claude Sonnet 4. Zejména v ovládání počítačů, kde model dosahuje lepších výsledků při práci s grafickým rozhraním a automatizaci úkolů. Tyto schopnosti činí z modelu vhodnou volbu pro aplikace jako Claude for Chrome, kde se rychlost a schopnost interakce s webovým rozhraním ukazují jako klíčové.

Model je určen především pro úkoly vyžadující nízkou latenci a rychlé odpovědi. Jde o chatové asistenty, zákaznickou podporu nebo párové programování, kde uživatelé oceňují okamžitou odezvu. Uživatelé nástroje Claude Code, příkazového řádku pro automatizované programování, získají výrazně rychlejší zážitek při práci s více agenty nebo při rychlém prototypování.

Cenová politika činí z Haiku 4.5 atraktivní volbu pro vývojáře. Model je dostupný přes Claude API s označením `claude-haiku-4-5` za cenu 1 dolar za milion vstupních tokenů a 5 dolarů za milion výstupních tokenů. To je výrazně levnější než u větších modelů, přičemž kvalita zůstává na vysoké úrovni.

Claude Sonnet 4.5, který Anthropic vydal před dvěma týdny, zůstává vlajkovým modelem a nejlepším programátorským modelem na světě. Haiku 4.5 však otevírá nové možnosti použití modelů společně. Sonnet 4.5 může rozložit složitý problém do vícekrokového plánu a poté řídit tým několika instancí Haiku 4.5, které paralelně zpracovávají dílčí úkoly. Tento přístup kombinuje strategické schopnosti většího modelu s rychlostí a ekonomikou menšího.

Z hlediska bezpečnosti prošel Haiku 4.5 detailními testy. Model vykazuje nízkou míru problematického chování a je výrazně lépe sladěný než jeho předchůdce Claude Haiku 3.5. V automatizovaném hodnocení sladění dokonce prokázal statisticky významně nižší celkovou míru nežádoucího chování než Claude Sonnet 4.5 i Claude Opus 4.1. To z něj podle této metriky činí dosud nejbezpečnější model společnosti.

Bezpečnostní testování také ukázalo, že Claude Haiku 4.5 představuje pouze omezené riziko v oblasti produkce chemických, biologických, radiologických a jaderných zbraní. Z tohoto důvodu byl vydán pod standardem AI Safety Level 2 (ASL-2), na rozdíl od přísnějšího ASL-3 pro Sonnet 4.5 a Opus 4.1. Úplné zdůvodnění klasifikace modelu jako ASL-2 i podrobnosti o všech bezpečnostních testech jsou k dispozici v [systémové kartě Claude Haiku 4.5](https://www.anthropic.com/system-card-haiku-4-5).

Model je k dispozici nejen přes Claude API, ale také na platformách Amazon Bedrock a Google Cloud Vertex AI. Slouží jako přímá náhrada za Haiku 3.5 i Sonnet 4 při nejnižších nákladech v portfoliu Anthropic. Vývojáři tak mohou rychle migrovat stávající aplikace na novější a výkonnější model bez nutnosti zásadních změn v kódu.

Guy Gur-Ari, spoluzakladatel společnosti Augment, která se zabývá automatizovaným programováním, k modelu uvedl: “Claude Haiku 4.5 dosáhl optimálního bodu, který jsme považovali za nemožný. Kvalita programování blízká hraničním modelům s vysokou rychlostí a cenovou efektivitou. V hodnocení automatizovaného programování společnosti Augment dosahuje 90 procent výkonu Sonnet 4.5 a vyrovnává se mnohem větším modelům.”

Zach Lloyd, zakladatel a ředitel společnosti Warp, která vyvíjí pokročilý terminál pro vývojáře, dodává: “Claude Haiku 4.5 je pokrok v automatizovaném programování, zejména pro orchestraci podagentů a úkoly ovládání počítačů. Rychlost odezvy vytváří v nástroji Warp dojem okamžité interakce s asistencí umělé inteligence.”

Claude Haiku 4.5 potvrzuje trend v oblasti velkých jazykových modelů, kdy výkon, který byl před několika měsíci k dispozici pouze u největších a nejdražších modelů, se postupně stává dostupným v menších a efektivnějších verzích. Pro vývojáře to znamená možnost používat pokročilé schopnosti umělé inteligence při výrazně nižších provozních nákladech a vyšší rychlosti zpracování.​​​​​​​​​​​​​​​​