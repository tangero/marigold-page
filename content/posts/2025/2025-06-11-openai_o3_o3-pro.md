---
slug: 'openai_o3_o3-pro'

author: Patrick Zandl
categories:
- AI
- OpenAI
- o3
- o3-Pro
- cenová politika
- konkurence
summary_points:
- OpenAI snížila cenu modelu o3 o 80 procent díky optimalizaci inference stacku
- Nový model o3-Pro nabízí vyšší výkon za 20/80 dolarů za milion tokenů
- Vývojáři oceňují dostupnost, kritici poukazují na stále vysoké ceny oproti konkurenci
- O3-Pro dosahuje 64% úspěšnosti v lidských testech oproti základnímu o3
- Změny interpretovány jako reakce na konkurenční tlak od Gemini a Deepseek
- Inference stack optimalizace zachovává původní výkon modelu bez degradace
thumbnail: https://www.marigold.cz/assets/openai-thumbnail.png
title: OpenAI snížila cenu modelu o3 o 80 % a představila o3-Pro
---

OpenAI oznámila výrazné snížení ceny svého modelu o3 o 80 procent spolu s uvedením nové varianty o3-Pro. Model o3 nyní stojí 2 dolary za milion vstupních [tokenů](/ai/tokeny-versus-slova/) a 8 dolarů za milion výstupních tokenů, zatímco dříve byla cena 10 a 40 dolarů. Současně byla představena výkonnější varianta o3-Pro.

Nový model o3-Pro je dostupný zatím jen přes API, tedy ne přes aplikaci nebo ChatGPT.com. Cena za použití je 20 dolarů za vstupní a 80 dolarů za výstupní [tokeny](/ai/tokeny-versus-slova/), což představuje 87procentní snížení oproti předchozímu modelu o1-Pro. I tak je to ale dost vysoká cena. Tomu odpovídají smíšené reakce vývojářů a uživatelů. Zatímco mnozí oceňují zvýšenou dostupnost, kritici poukazují na stále vysoké ceny ve srovnání s konkurencí.

## Technické pozadí snížení cen

Snížení ceny modelu o3 bylo dosaženo optimalizací inference stacku, systému zpracovávajícího požadavky na model. OpenAI zdůraznila, že se jedná o stejný model bez jakýchkoliv úprav výkonu - nebyly tedy použity techniky jako destilace nebo kvantizace, které by mohly snížit kvalitu výstupů. Tato optimalizace představuje významný technologický pokrok, když si uvědomíme, že původní testy modelu na benchmarku [ARC-AGI](https://arcprize.org) stály OpenAI stovky tisíc dolarů za jeden běh.

Inference stack optimalizace zahrnuje zlepšení způsobu, jakým jsou požadavky zpracovávány na serverové infrastruktuře, aniž by byl ovlivněn základní model nebo jeho schopnosti. Tento přístup umožňuje společnosti nabídnout stejnou kvalitu služby za výrazně nižší cenu, což je klíčové pro konkurenceschopnost na trhu jazykových modelů.

## Specifikace a možnosti o3-Pro

Model o3-Pro využívá stejný základní model jako standardní o3, ale s rozšířenými nástroji a delším časem na "přemýšlení". Mezi jeho hlavní funkce patří podpora pro Python, prohlížení webu, zpracování obrazových vstupů, volání funkcí a strukturované výstupy. Model je navržen pro řešení složitých problémů a některé požadavky mohou trvat několik minut, proto OpenAI zavedla nový background mode v Responses API pro předcházení timeoutům.

V benchmarkových testech dosahuje o3-Pro 64 % úspěšnosti ve srovnání se základním modelem o3 podle hodnocení lidských testerů. Nejvyšší výkon vykazuje v oblastech matematiky, kompetitivního kódování, vědeckých úloh a komplexního psaní. Model je dostupný jako 'o3-pro-2025-06-10' v Responses API a je optimalizován pro _agentic tool calling_ a _instruction following_.

> 💡 **Agentic tool calling** je schopnost AI modelu samostatně rozhodovat o tom, které externí nástroje nebo funkce použije k vyřešení konkrétního úkolu, a následně je aktivně volat v průběhu zpracování požadavku. Na rozdíl od tradičního function callingu, kde model pouze navrhne použití funkcí, agentic přístup umožňuje modelu vytvořit kompletní plán řešení, postupně volat různé nástroje podle potřeby, vyhodnocovat jejich výsledky a na základě toho upravovat svou strategii. Model tak může například při analýze dat automaticky načíst soubor, provést výpočty pomocí matematických funkcí, vyhledat dodatečné informace online a výsledky zkombinovat do finální odpovědi - vše bez nutnosti lidského zásahu mezi jednotlivými kroky. 

## Srovnání s konkurencí

| Model | Vstupní tokeny ($/1M) | Výstupní tokeny ($/1M) | Poskytovatel |
|-------|----------------------|------------------------|--------------|
| o3 | 2 | 8 | OpenAI |
| o3-Pro | 20 | 80 | OpenAI |
| GPT-4.1 | 2 | 8 | OpenAI |
| GPT-4o | vyšší než o3 | vyšší než o3 | OpenAI |
| Gemini 2.5 Pro | konkurenční cena | konkurenční cena | Google |
| Deepseek R1 | nižší než o3 | nižší než o3 | Deepseek |

Přestože OpenAI snížila ceny, model o3 zůstává dražší než některé alternativy, zejména open-source řešení jako Deepseek R1. Cena o3 je nyní shodná s GPT-4.1 za vstupní tokeny, ale výrazně levnější než GPT-4o, což ho činí atraktivní volbou pro kódování a úkoly vyžadující _agentic tool calling_.

## Reakce vývojářské komunity

Vývojáři a malé firmy reakci na snížení cen přivítali pozitivně. Mnoho z nich uvedlo, že nižší ceny jim umožní více experimentovat s modelem pro úkoly, které byly dříve finančně nedostupné, jako je shrnování obsahu nebo pokročilé kódování. Tvůrci služeb jako [Websim AI](https://websim.com) nebo [Cursor](/vibecoding/cursor) již oznámili plány na integraci modelu o3 do svých nástrojů.


Kritické hlasy však poukazují na několik problémů. Uživatelé na platformách jako Reddit označují model o3 za "přeceněný" vzhledem k jeho výkonu a upozorňují, že i po snížení zůstává dražší než konkurenční řešení. Někteří skeptici se ptají, zda snížení ceny neovlivnilo kvalitu modelu, ačkoliv OpenAI toto popírá.

## Strategické důvody změn

Snížení cen je interpretováno jako reakce na rostoucí konkurenční tlak ze strany modelů jako Gemini 2.5 Pro od Google DeepMind a Claude Opus 4 od Anthropic. Trh s velkými jazykovými modely se rychle vyvíjí a cenová konkurenceschopnost se stává klíčovým faktorem pro udržení tržního podílu.

OpenAI čelí také tlaku ze strany open-source alternativ, které nabízejí podobné schopnosti za výrazně nižší ceny. Deepseek R1 a další open-weight modely představují vážnou konkurenci, zejména pro nákladově citlivé projekty a startupy s omezenými rozpočty.

Uvedení o3-Pro lze chápat jako snahu diferencovat produktovou řadu a nabídnout prémiové řešení pro náročné úkoly, zatímco standardní o3 se stává dostupnějším pro běžné použití. Tato strategie následuje model freemium, kde základní funkcionalita je cenově dostupná a pokročilé funkce jsou zpoplatněny premium cenou.

## Technické využití a doporučení

OpenAI doporučuje model o3 především pro kódování, kde nyní nabízí stejnou cenu za [token](/ai/tokeny-versus-slova/) jako GPT-4.1, ale s lepším výkonem. Model je také vhodný pro úkoly vyžadující agentic tool calling, function calling a přesné následování instrukcí. Optimalizovaný inference stack činí o3 praktickou volbou pro produkční nasazení, kde byla dříve cena překážkou.

Model o3-Pro je určen pro komplexní problémy vyžadující delší čas na zpracování a vyšší výpočetní výkon. Jeho použití je ekonomicky opodstatněné pro kritické úkoly v oblasti výzkumu, pokročilého kódování a vědeckých aplikací, kde je kvalita výstupu důležitější než rychlost nebo cena.

Background mode v Responses API řeší praktický problém s timeouty při používání o3-Pro, což umožňuje zpracování komplexních požadavků bez rizika přerušení spojení. Tato funkce je klíčová pro integraci modelu do produkčních systémů, kde spolehlivost je prioritou.

Pro vývojáře je snížení cen za model o3 velmi atraktivní, protože je obecně chápán jako jeden z nejlepších modelů a pro řadu úloh by byl primární volbou, kdyby nebyl tak drahý - a to se nyní mění. 