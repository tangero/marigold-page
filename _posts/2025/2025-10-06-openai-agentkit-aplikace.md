---
author: Patrick Zandl
categories:
- AI
- OpenAI
- ChatGPT
- AMD
- Agenti
layout: post
post_excerpt: OpenAI představil aplikace uvnitř ChatGPT, vývojářské nástroje pro agenty a API pro GPT-5 Pro i Sora 2. Součástí oznámení byla i dohoda s AMD na dodávky čipů v hodnotě až 6 gigawattů. A AI Agenti. Pojďme si všechny novinky projít. 
summary_points:
- OpenAI uzavřel s AMD dohodu na dodávku až 6 gigawattů výpočetního výkonu s možností získat 10% podíl ve firmě
- ChatGPT nyní nabízí přímou integraci aplikací třetích stran včetně Coursera, Zillow a Canva
- AgentKit umožňuje vývojářům vytvářet a nasazovat AI agenty během několika minut
- GPT-5 Pro je dostupný přes API pro náročné úkoly, GPT Realtime Mini nabízí levnější hlasové možnosti
- Sora 2 byla zpřístupněna přes API pro generování videí
- OpenAI nyní slouží 800 milionům týdenních uživatelů a čtyřem milionům vývojářů
title: OpenAI představil aplikace uvnitř ChatGPT, AgentKit a uzavřel dohodu s AMD
thumbnail: https://www.marigold.cz/assets/Visual__Agent_Builder_Template_Assets.webp
---

OpenAI na vývojářské konferenci DevDay oznámil řadu novinek, které mění ChatGPT z nástroje na platformu. Nejviditelnější změnou je možnost spouštět aplikace přímo uvnitř rozhraní ChatGPT, což uživatelům umožní pracovat s dalšími službami bez nutnosti přepínat mezi různými aplikacemi. Součástí oznámení byla i významná dohoda s AMD na dodávky čipů pro strojové učení.

Před zahájením konference OpenAI podepsal šéf společnosti Sam Altman dohodu s AMD, která společnosti umožní získat až desetiprocentní podíl v této firmě zabývající se výrobou procesorů. Dohoda počítá s nasazením až šesti gigawattů GPU AMD Instinct během několika let. Tento objem odpovídá kapacitě několika největších datových center na světě dohromady a představuje jeden z největších projektů výstavby infrastruktury pro strojové učení. Dohoda dává OpenAI větší nezávislost na dodávkách od Nvidie, která dosud dominovala trhu s čipy pro strojové učení. Pro AMD znamená nejen kapitálovou injekci, ale také validaci jejich platformy Instinct, což může urychlit její adopci u dalších zákazníků.

## Růst platformy

Sam Altman na začátku konference sdílel čísla ukazující růst platformy. V roce 2023 mělo ChatGPT dva miliony vývojářů a sto milionů týdenních uživatelů. Nyní platforma dosáhla čtyř milionů vývojářů a více než 800 milionů týdenních uživatelů. Tento osminásobný růst uživatelské základny za necelé dva roky ukazuje rychlé rozšíření používání velkých jazykových modelů.

## Aplikace uvnitř ChatGPT

Hlavní novinkou DevDay bylo představení App SDK, které vývojářům umožňuje vytvářet aplikace běžící přímo uvnitř rozhraní ChatGPT. Uživatelé tak mohou pracovat s externími službami bez nutnosti opouštět prostředí ChatGPT. OpenAI na konferenci ukázal integraci s Coursera, platformou pro online vzdělávání, což se projevilo šestiprocentním růstem akcií této společnosti. Další demonstrace zahrnovaly Zillow, portál s nemovitostmi, a Canva, nástroj pro grafický design.

Tato funkce má potenciál výrazně zvýšit čas, který uživatelé stráví v ChatGPT, protože eliminuje nutnost přepínat mezi různými aplikacemi. Seznam partnerů zahrnuje desítky známých služeb a platforma je otevřená dalším vývojářům. Tento krok staví ChatGPT do přímé konkurence s obchody s aplikacemi od Apple a Google, které ročně generují přibližně 200 miliard dolarů. Jak tito hráči zareagují na pokus OpenAI zasáhnout do jejich teritoria, ukáže budoucnost. Očekávat lze brzké oznámení monetizačních modelů pro tyto integrace. 

![Booking v chatgpt](/assets/Booking_16x9__3_.webp)

OpenAI tak rozvíjí koncept GPTs, který ovšem byl značně limitovaný, do jisté míry ale umožnil spouštět aplikace třetích stran uvnitř ChatGPT.

## Nástroje pro vývoj agentů

OpenAI [představil AgentKit](https://openai.com/index/introducing-agentkit/), vývojářské prostředí pro tvorbu AI agentů s vizuálním rozhraním AgentBuilder Během demonstrace trvalo sedm minut vytvořit a nasadit funkčního agenta na web, přičemž původní odhad činil osm minut. Altman přirovnal AgentKit k Canvas. Nástroj je již dostupný.

![AgentKit](/assets/Visual__Agent_Builder_Template_Assets.webp)

Součástí oznámení byl i ChatKit, který umožňuje vývojářům vložit konverzační rozhraní poháněné ChatGPT do jejich vlastních aplikací nebo webů. Agenti navíc získali vestavěné nástroje pro evaluaci, což usnadňuje testování a kontrolu jejich chování. Tyto funkce mají za cíl usnadnit nasazení AI agentů v produkčním prostředí a zvýšit závislost firemních zákazníků na platformě OpenAI.

Musím říct, že mi to zatím přijde dost nepřehledné a hony za N8N... Ale ještě tomu dám šanci. 

## Codex pro vývoj softwaru

Codex, autonomní agent pro vývoj softwaru od OpenAI, je nyní veřejně ostupný. Codex slouží k automatizaci softwarového vývoje a umožňuje vytvářet aplikace pomocí přirozeného jazyka místo tradičního programování. Nástroj je zaměřen na urychlení vývoje a snížení bariér vstupu pro ty, kteří neumí programovat.

## Aktualizace API

OpenAI zpřístupnil přes API model GPT-5 Pro, určený pro náročné úkoly vyžadující hluboké zpracování, jako jsou právní analýzy nebo vědecké výpočty. Publikum na konferenci reagovalo na toto oznámení velmi pozitivně. Společnost také představila GPT Realtime Mini, menší a levnější variantu s plnou hlasovou expresivitou předchozích modelů.

Překvapivým krokem bylo zpřístupnění Sora 2 přes API. Sora 2 je nástroj pro generování videí na základě textových popisů. Tento krok přichází v době, kdy se kolem generování multimediálního obsahu objevují otázky duševního vlastnictví a možného šíření dezinformací. Reklamní odvětví pravděpodobně začne tento nástroj rychle testovat. Během demonstrace bylo ukázáno, jak lze vytvářet vizualizace hraček, přičemž kvalita výstupu závisí na schopnosti uživatele formulovat přesné zadání nebo vytvořit vstupní materiál.

## zhodnocení

Náročná situace po tomto oznámení bude pro integrátory typu Zapier či Make.com, platformami založenými na prohlížeči a jakýmikoli službami závislými na přepínání uživatelů mezi kontexty. Bude zajímavé sledovat, kolik služeb se rozhodne poskytnout přístup svým datům a funkcím. Google pravděpodobně zareaguje změnami v prohlížeči Chrome.

Obchod s aplikacemi nyní existuje uvnitř chatbota. AgentKit, ChatKit, Codex a GPT-5 Pro společně umožňují automatizaci práce v masivním měřítku. Agenti automatizují pracovní postupy, Codex odstraňuje bariéry programování, Sora 2 vytváří vizuální obsah. Důsledek je strukturální: ChatGPT se posouvá z role nástroje do role operační základny. Tradiční dodavatelé SaaS softwaru a programátoři staré školy náhle působí jako relikvie minulosti. OpenAI se nyní postavil do centra digitální produkce pro množství agentur a firem ještě více, než tomu bylo dosud.

Otázka nyní je existenční: čím se OpenAI vlastně chce stát? Může být současně laboratoří, výrobcem hardwaru, sociální sítí a obchodním motorem? Nebo Altman a jeho tým riskují kolaps pod tíhou vlastních ambicí? Dnešní dohoda s AMD naznačuje, že tým má vizi. Nyní možná začínáme vidět i konkrétní plán.