---
author: Patrick Zandl
categories:
- AI
- Mistral AI
layout: post
post_excerpt: 'Francouzská společnost Mistral AI oznámila významnou aktualizaci svých
  LLM nástrojů a také své chatovací platformy le Chat. Nově umí vyhledávat i s citacemi,
  pracovat s dokumenty a má režim Canvas. Aktualizace se také dočkaly LLM. '
summary_points:
- Mistral AI aktualizoval open-source model blízký uzavřeným řešením.
- Le Chat nabízí webové vyhledávání s citacemi zdarma.
- Canvas umožňuje real-time spolupráci na kreativních projektech.
- Pixtral Large vylepšuje zpracování dokumentů a obrazových dat.
- Generování obrázků integrováno díky partnerství s Black Forest Labs.
- Le Chat Agents automatizují opakující se úkoly a workflow.
- Pixtral Large a Mistral Large 24.11 posouvají multimodální AI možnosti.
thumbnail: https://www.marigold.cz/assets/le-chat-mistral-ai.jpg
title: "'Mistral AI má Pixtral Large a Mistral Large 24.11 a rozšiřuje možnosti: vyhledávání,"
  canvas, zpracování dokumentů, obrázky '
---

Francouzská společnost Mistral AI oznámila významnou aktualizaci svých LLM nástrojů a také své chatovací platformy *le Chat* [/lə ʃa/]. Dotahuje tak svůj open-source model významně blízko k možnostem uzavřených řešení, jako je Claude nebo ChatGPT. 

## Klíčové novinky v le Chat

### 1. Webové vyhledávání s citacemi
Le Chat nyní disponuje schopností aktivně vyhledávat na internetu a poskytovat aktuální informace podložené citacemi. Tato funkce je particularly užitečná pro studenty a profesionály, kteří potřebují aktuální a ověřené informace pro svůj výzkum či práci. Na rozdíl od některých konkurenčních řešení je tato funkce dostupná zdarma.

### 2. Canvas - Nové rozhraní pro kreativní práci
Revoluční novinkou je představení funkce Canvas, která přináší zcela nový rozměr do interakce s AI. Canvas umožňuje:
- Přímou spolupráci s Mistral LLM na společných výstupech
- Vytváření a iteraci nápadů v reálném čase
- Modifikaci obsahu bez nutnosti regenerace celé odpovědi
- Verzování návrhů
- Náhled designů

Podobný režim Canvas má ChatGPT pro model 4o, také umožňuje iteraci nápadů a modifikaci obsahu bez regenerování celé odpovědi. 

Toto rozhraní je užitečné pro tvorbu dokumentů, prezentací, kódu a mockupů, přičemž překonává tradiční omezení chatovacích rozhraní.

### 3. Pokročilé zpracování dokumentů a obrazů
Implementace nového multimodálního modelu Pixtral Large přináší významné vylepšení v oblasti zpracování komplexních dokumentů:
- Analýza PDF dokumentů včetně grafů, tabulek a diagramů
- Zpracování matematických vzorců a rovnic
- Pokročilá sumarizace obsahu
- Sémantické porozumění komplexním vědeckým textům

Tento model představuje významný upgrade oproti předchozí verzi Pixtral 12B a je doplněn o experimentální model, o kterém společnost slibuje více informací v následujících týdnech. Podobnou funkcionalitu má jako experimentální funkci Claude od Antrhropicu, ukazuje se být velmi silnou při zpracování dokumentů a rozhodně je to dobrý směr. 

### 4. Generování obrázků
Díky partnerství s Black Forest Labs nabízí le Chat nyní i možnost generování vysoce kvalitních obrázků přímo v rámci chatovacího rozhraní. Tato integrace umožňuje uživatelům vytvářet vizuální obsah bez nutnosti přepínání mezi různými nástroji. V každém případě jde ale jen o integraci stávajícího řešení, na druhou stranu jeho provazbení do systému může být v budoucnu zajímavé a důležité. 

### 5. Le Chat Agents
Platforma nově podporuje vytváření automatizovaných workflow prostřednictvím agentů. Uživatelé mohou:
- Automatizovat opakující se úkoly
- Vytvářet vlastní agenty pro specifické případy užití
- Sdílet agenty s týmem
- Rekurzivně vylepšovat a kombinovat agenty pro komplexnější úlohy

Typické případy užití zahrnují:
- Skenování účtenek pro vykazování výdajů
- Vytváření souhrnů z dlouhých zápisů z jednání
- Zpracování faktur

Návod [na použití Le Chat Agents najdete zde](https://docs.mistral.ai/capabilities/agents/). Obdobou Agents jsou u ChatGPT nejspíše GPTs... 

## Pixtral Large a Mistral Large 24.11

Společnost Mistral AI také představila Pixtral Large, nejnovější multimodální model, a oznámila aktualizaci svého textového modelu Mistral Large. Tyto novinky posouvají možnosti le Chat a dalších nástrojů společnosti. 

### Pixtral Large: Špička v multimodální umělé inteligenci

Pixtral Large je 124B open-source multimodální model, který staví na textovém modelu Mistral Large 2. Tento model přináší výrazné zlepšení v oblasti zpracování obrazových dat a dokumentů, aniž by obětoval svou špičkovou schopnost porozumění textu.

![Porovnání LLM](/assets/pixtral-large-main-table.png)

Hlavní vlastnosti Pixtral Large:
•	Výkon na hranici možností: Špičkové výsledky na benchmarkech, jako jsou MathVista, DocVQA a VQAv2.
•	Pokročilá architektura: 123B parametrů pro dekodér textu a 1B parametrů pro vizuální enkodér.
•	Velká kapacita kontextu: Podpora až 128 tisíc tokenů, což umožňuje zpracování více než 30 snímků ve vysokém rozlišení najednou.
•	Multimodální aplikace: Model exceluje v úlohách jako analýza dokumentů, grafů, rovnic a vizuálních dat.

Pixtral Large dosahuje 69,4 % na MathVista, čímž překonává konkurenty jako GPT-4o a Gemini-1.5 Pro, a vyniká i na dalších testovacích sadách, jako jsou ChartQA a DocVQA.

Praktické příklady použití:

1.	OCR a matematické úlohy:
•	Model dokáže rozpoznat text z dokumentů a provádět složité výpočty, například z německých účtenek.
2.	Analýza grafů:
•	Identifikace bodů instability ve ztrátových křivkách při trénování modelů.
3.	Webové zpracování obrazu:
•	Výpis firem, které využívají modely Mistral AI, na základě screenshotu webové stránky.

Pixtral Large je k dispozici pod licencí Mistral Research License (MRL) pro výzkum a vzdělávání nebo pod Mistral Commercial License pro komerční využití.

### Příklad: Analýza grafů v praxi

![Analýza grafu v praxi](/assets/loss-curve.png)

> Prompt: When did things start to go wrong for dark dragon?
>
> Odpověď: U modelu „dark-dragon-50“ začíná tréninková ztráta vykazovat značnou nestabilitu kolem hranice 10 000 kroků. V tomto okamžiku dochází k výraznému nárůstu hodnoty ztráty a nestabilita pokračuje dalším výrazným nárůstem kolem hranice 20 000 kroků. Tyto skoky naznačují, že proces trénování modelu „dark-dragon-50“ se začal potýkat s problémy přibližně od hranice 10 000 kroků.



### Mistral Large 24.11: Vylepšený textový model

Nová verze modelu Mistral Large, označovaná jako 24.11, přináší klíčová zlepšení oproti předchozí verzi 24.07:
•	Dlouhý kontext: Vylepšené porozumění textům s dlouhým kontextem.
•	Přesnější funkční volání: Zlepšení v generování kódu a interpretaci příkazů.
•	Optimalizace systémových promptů: Přesnější a kontextově vhodnější výstupy.
•	Podpora podnikových aplikací: Model je optimalizován pro agentové workflow, správu znalostí a automatizaci úkolů.

Mistral Large 24.11 je dostupný na HuggingFace pod licencí MRL nebo komerční licencí Mistral AI a brzy bude k dispozici prostřednictvím poskytovatelů cloudových služeb, jako jsou Google Cloud a Microsoft Azure.


## Závěr

Tato aktualizace představuje významný milník nejen pro Mistral AI, ale pro celý evropský AI sektor. Ukazuje, že je možné vytvářet konkurenceschopné AI nástroje s důrazem na dostupnost a praktickou využitelnost, aniž by bylo nutné obětovat technologickou vyspělost. Pro uživatele to znamená přístup k pokročilým AI schopnostem v jednom integrovaném balíku, což může významně zvýšit jejich produktivitu a kreativní možnosti.

Le Chat je dostupný na [chat.mistral.ai](https://chat.mistral.ai), přičemž nové funkce budou postupně nasazovány v průběhu následujících týdnů.