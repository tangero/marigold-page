---
author: Patrick Zandl
categories:
- AI
- LRM
layout: post
post_excerpt: Ještě nevyprchala včerejší přestřelka o tom, jak moc uvažování pomáhá
  v LLM a již tu máme další model. Mistral představuje dvě velikosti svých uvažovacích
  modelů nazvaných Magistral. Konečně někdo, kdo umí volit jména pro modely!
summary_points:
- Mistral AI uvedla Magistral, model pro logické uvažování ve dvou verzích.
- Magistral Medium dosahuje 73,6% úspěšnosti v matematickém benchmarku AIME2024.
- Magistral nativně uvažuje v několika jazycích, včetně angličtiny, francouzštiny
  a čínštiny.
- Magistral cílí na odvětví jako právo a finance díky sledovatelnosti rozhodování.
thumbnail: https://www.marigold.cz/assets/mistral-magistral.png
title: Mistral AI představil Magistral, svůj první model pro logické uvažování
---

Francouzská společnost Mistral AI uvedla svůj první specializovaný model pro logické uvažování nazvaný Magistral. Model je dostupný ve dvou variantách - open-source verzi Magistral Small s 24 miliardami parametrů a komerční verzi Magistral Medium. 

Magistral je zaměřen na transparentní uvažování v mnoha jazycích a dosahuje 73,6% úspěšnosti v matematickém benchmarku AIME2024. Model přináší údajně desetkrát vyšší rychlost (tvrdí Mistral) zpracování než konkurence a cílí na profesionální využití v regulovaných odvětvích, kde je nutná sledovatelnost rozhodovacích procesů.

## Technické parametry a výkonnost

Magistral Small obsahuje 24 miliard parametrů a je dostupný pod licencí Apache 2.0 pro volné použití. Jen pro jistoti připomínám, že váhy většího modelu nejsou otevřeně vydány a to je velká škoda. 

Komerční verze Magistral Medium nabízí vyšší výkonnost pro podnikové nasazení. Na matematickém benchmarku AIME2024 dosahuje Magistral Medium 73,6% úspěšnosti při jednotlivém pokusu a 90% při většinovém hlasování ze 64 pokusů. Menší model Magistral Small dosahuje 70,7% a 83,3% v týchž testech.

Srovnání s konkurencí ukazuje nadprůměrné výsledky napříč různými benchmarky. Na testu GPQA Diamond dosahuje Magistral Medium 70,8% úspěšnosti, na LiveCodeBench 59,4% a na Aider Polyglot 47,1%. Model překonává některé etablované modely jako GPT-4 nebo Claude v určitých kategoriích testů. Tady je pár podrobností, ale počkal bych si na nezávislé specializované testy.

![Mistral Magistral](/assets/plot-magistral.png)



## Vícejazyčné schopnosti

Magistral je navržen pro nativní uvažování v různých jazycích bez nutnosti překladu do angličtiny. Model dokáže udržet vysokou kvalitu logického uvažování v angličtině, francouzštině, španělštině, němčině, italštině, arabštině, ruštině a zjednodušené čínštině. Tato schopnost představuje pokrok oproti současným modelům, které často degradují při práci v jiných jazycích než angličtině.

Řetězec myšlení CoT (chain-of-thought) funguje přirozeně napříč globálními jazyky a alfabety, což umožňuje uživatelům sledovat rozhodovací proces modelu v jejich rodném jazyce. Pro uživatele v Česku to znamená možnost budoucí podpory češtiny, ačkoliv čeština není mezi explicitně podporovanými jazyky zmíněna.

## Rychlost a optimalizace

Funkcionalita Flash Answers v chatovací aplikaci Le Chat umožňuje Magistral Medium údajně dosahovat až desetkrát vyšší rychlosti zpracování [tokenů](/ai/tokeny-versus-slova/) než většina konkurence. Tato optimalizace činí model použitelným pro aplikace vyžadující odpovědi v reálném čase a umožňuje zpětnou vazbu od uživatelů ve velkém měřítku.

Rychlostní srovnání s ChatGPT ukazuje významnou převahu Magistralu v chatovacím rozhraní Le Chat. Model je také dostupný přes API na platformě La Plateforme, což umožňuje integraci do vlastních aplikací.

## Průmyslové aplikace

Magistral cílí na profesionály v právnictví, financích, zdravotnictví a veřejné správě. Model poskytuje sledovatelné uvažování, které splňuje požadavky na "compliance" - tedy regulatorní soulad s podmínky v odvětví. Každý závěr lze zpětně vysledovat přes logické kroky, což poskytuje auditovatelnost pro prostředí s vysokými nároky na spolehlivost.

Transparentnost rozhodovacího procesu je klíčová pro odvětví, kde jsou rozhodnutí podrobována regulatornímu dohledu. Model umožňuje verifikaci postupu uvažování, což je nezbytné pro právní analýzy nebo finanční modelování.

### Softwarové inženýrství

V oblasti vývoje softwaru Magistral vylepšuje plánování projektů, návrh backendové architektury, frontend design a datové inženýrství prostřednictvím sekvenovaných, vícekrokových akcí zahrnujících externí nástroje nebo API. Model významně překonává běžné jazykové modely bez schopnosti uvažování v programátorských úlohách.

Přiznám se ale, že zatím neznám nikoho, kdo by používal Mistral modely v kódování, musím to sám vyzkoušet - [Mistral Code](https://mistral.ai/news/mistral-code)


## Dostupnost a nasazení

Magistral Small je dostupný zdarma na platformě Hugging Face pro vlastní nasazení. Magistral Medium lze vyzkoušet v preview verzi v aplikaci Le Chat nebo přes API na La Plateforme. Komerční verze bude dostupná na Amazon SageMaker a v budoucnu na IBM WatsonX, Azure AI a Google Cloud Marketplace.

Pro podnikové zákazníky a vlastní řešení včetně on-premises nasazení nabízí Mistral AI kontakt s obchodním týmem. Model je také podporován vědeckou publikací pokrývající evaluace, trénovací infrastrukturu a algoritmy pro posilované učení.

## Technologické pozadí

Magistral využívá pokročilé algoritmy posilovaného učení optimalizované pro trénování uvažujících modelů. Architektura je speciálně navržena pro vícekrokovou logiku na rozdíl od univerzálních modelů. Mistral AI plánuje rychlé iterace modelu s konstantními vylepšeními.

Model rozšiřuje portfolio francouzské společnosti Mistral AI, která konkuruje americkým gigantům jako OpenAI nebo Anthropic. Mistral AI se zaměřuje na kombinaci open-source přístupu s komerčními řešeními pro podniky.

Komunitní přístup umožňuje vývojářům zkoumat, modifikovat a stavět na architektuře Magistralu. Předchozí open-source modely od Mistral AI již byly využity komunitou pro projekty jako ether0 a DeepHermes 3.

### Klíčové vlastnosti modelu:
- Transparentní uvažování s možností ověření každého kroku
- Nativní multijazyčnost bez ztráty kvality
- Specializace na doménově specifické problémy
- Vysoká rychlost zpracování v reálném čase
- Open-source dostupnost menší verze
- Podpora regulovaných odvětví s požadavky na auditovatelnost