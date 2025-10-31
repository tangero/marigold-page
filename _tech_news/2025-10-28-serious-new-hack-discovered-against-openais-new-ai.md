---
category: kybernetická bezpečn
companies:
- OpenAI
date: '2025-10-28 17:33:45'
description: Výzkumníci z NeuralTrust odhalili kritickou zranitelnost v prohlížeči
  Atlas od OpenAI, která umožňuje prompt injection útoky přímo přes adresní řádek.
importance: 4
layout: tech_news_article
original_title: Serious New Hack Discovered Against OpenAI’s New AI Browser - Futurism
publishedAt: '2025-10-28T17:33:45+00:00'
slug: serious-new-hack-discovered-against-openais-new-ai
source:
  emoji: 📰
  id: null
  name: Futurism
title: Vážná bezpečnostní chyba objevena v novém AI prohlížeči od OpenAI
url: http://futurism.com/artificial-intelligence/serious-new-hack-openai-ai-browser
urlToImage: https://futurism.com/wp-content/uploads/2025/10/serious-new-hack-openai-ai-browser_236135.jpg?w=1200
urlToImageBackup: https://futurism.com/wp-content/uploads/2025/10/serious-new-hack-openai-ai-browser_236135.jpg?w=1200
---

## Souhrn

Výzkumníci z bezpečnostní firmy NeuralTrust objevili vážnou zranitelnost v novém AI prohlížeči Atlas od OpenAI, která umožňuje útočníkům provádět prompt injection útoky přímo přes adresní řádek zvaný Omnibox. Na rozdíl od předchozích nepřímých útoků vložených do webových stránek tato zranitelnost zneužívá způsob, jakým prohlížeč zpracovává URL adresy zkopírované uživatelem.

## Klíčové body

- Prohlížeč Atlas s integrovaným ChatGPT obsahuje režim agenta, který dokáže autonomně provádět celé úkoly jako rezervaci letenek nebo nákup potravin
- Omnibox prohlížeče, který přijímá jak URL adresy tak přirozený jazyk, je extrémně zranitelný vůči prompt injection útokům
- Útočníci mohou zamaskovat škodlivé instrukce jako běžnou URL adresu, kterou uživatel zkopíruje a vloží do prohlížeče
- Prohlížeč nevaliduje správně některé upravené URL a místo toho je interpretuje jako důvěryhodné uživatelské příkazy
- Firma NeuralTrust již zranitelnost nahlásila OpenAI, která na problému pracuje

## Podrobnosti

Prohlížeč Atlas od OpenAI představený nedávno staví ChatGPT do centra prohlížecího zážitku. Jeho hlavní funkcí je režim agenta dostupný pro platící uživatele, který umožňuje prohlížeči autonomně vykonávat komplexní úkoly - od rezervace letů až po online nákupy. Právě tato autonomie však vytváří významné bezpečnostní riziko.

Bezpečnostní výzkumníci již dříve demonstrovali nepřímé prompt injection útoky, kdy škodlivé instrukce vložené do webových stránek dokázaly manipulovat chování prohlížeče. Například jeden výzkumník přinutil Atlas vypsat text "Trust No AI" místo vytvoření shrnutí dokumentu v Google Docs.

Nově objevená zranitelnost od NeuralTrust je však závažnější. Martí Jordà, softwarový inženýr ve firmě, vysvětlil, že problém spočívá v tom, jak Omnibox - textové pole v horní části prohlížeče přijímající URL i přirozený jazyk - zpracovává vstupy. Když uživatel vloží mírně upravenou URL adresu, prohlížeč ji nevaliduje jako webovou adresu, ale místo toho "zachází s celým obsahem jako s příkazem".

Tato chyba má vážné důsledky. Zamaskované instrukce v URL jsou interpretovány jako důvěryhodný záměr uživatele s menším množstvím bezpečnostních kontrol. "Agent vykonává vložené instrukce se zvýšenou důvěrou," napsal Jordà. To znamená, že útočník může připravit škodlivou URL, která vypadá legitimně, a když ji uživatel zkopíruje a vloží do Omniboxu, prohlížeč provede skryté škodlivé příkazy.

## Proč je to důležité

Tato zranitelnost odhaluje zásadní problém v designu AI prohlížečů a autonomních agentů obecně. Zatímco OpenAI a další firmy se snaží vytvořit AI asistenty schopné provádět složité úkoly jménem uživatelů, bezpečnostní mechanismy nestíhají tempo vývoje. Prompt injection útoky představují jednu z nejzávažnějších hrozeb pro AI systémy a jejich integrace do kritických nástrojů jako webové prohlížeče toto riziko znásobuje.

Pro běžné uživatele to znamená, že by měli být extrémně opatrní při kopírování URL adres z nedůvěryhodných zdrojů. Pro průmysl je to varování, že AI agenti s vysokou mírou autonomie vyžadují mnohem robustnější bezpečnostní architekturu než současné implementace nabízejí. OpenAI podle NeuralTrust na opravě pracuje, ale incident ukazuje, že cesta k bezpečným AI asistentům bude delší a složitější, než se původně předpokládalo.

---

[Číst původní článek](http://futurism.com/artificial-intelligence/serious-new-hack-openai-ai-browser)

**Zdroj:** 📰 Futurism
