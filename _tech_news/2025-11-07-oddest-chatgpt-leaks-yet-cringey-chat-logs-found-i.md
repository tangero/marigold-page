---
author: Marisa Aigen
category: ai
companies:
- OpenAI
- Google
- Microsoft
date: '2025-11-07 16:49:53'
description: Vyšetřování ukazuje, že citlivé dotazy z ChatGPT se objevovaly v Google
  Search Console a naznačuje, že OpenAI přímo pracuje s daty z Google vyhledávání.
  OpenAI hlásí opravu „chybného směrování“ dotazů, ale neodpověděla na klíčové otázky
  ohledně rozsahu a mechanismu problému.
importance: 4
layout: tech_news_article
original_title: 'Oddest ChatGPT leaks yet: Cringey chat logs found in Google analytics
  tool - Ars Technica'
people:
- Sam Altman
- Elon Musk
- Tim Cook
publishedAt: '2025-11-07T16:49:53+00:00'
slug: oddest-chatgpt-leaks-yet-cringey-chat-logs-found-i
source:
  emoji: 🔬
  id: ars-technica
  name: Ars Technica
title: 'Nejpodivnější úniky ChatGPT: osobní konverzace se objevily v Google Search
  Console'
url: https://arstechnica.com/tech-policy/2025/11/oddest-chatgpt-leaks-yet-cringey-chat-logs-found-in-google-analytics-tool/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/11/chatgpt-private-chats-1152x648.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/11/chatgpt-private-chats-1152x648.jpg
---

## Souhrn
Citlivé a osobní dotazy z ChatGPT se několik měsíců objevovaly v nástroji Google Search Console (GSC), který slouží správcům webů ke sledování návštěvnosti z vyhledávání. Analýza konzultantů naznačuje, že OpenAI využívala uživatelské dotazy v kombinaci s Google Search, což vyvolává závažné otázky ohledně ochrany soukromí a způsobu trénování i provozu velkých jazykových modelů.

## Klíčové body
- V GSC se od září začaly objevovat extrémně dlouhé dotazy obsahující celé pasáže z konverzací s ChatGPT.
- Analytici Jason Packer (Quantable) a Slobodan Manić testováním dospěli k závěru, že jde o přímé využívání Google Search s reálnými uživatelskými promptami.
- OpenAI přiznalo „chybu v routování malého množství dotazů“, tvrdí, že problém vyřešilo, ale odmítlo detailně vysvětlit příčinu a rozsah.
- Incident zpochybňuje transparentnost OpenAI ohledně práce s uživatelskými daty a externími zdroji.
- Pro provozovatele webů, firmy i regulátory jde o nový typ rizika: únik promptů a kontextu přes integrační a monitorovací nástroje.

## Podrobnosti
Podle zjištění analytika Jasona Packera, který vede konzultační firmu Quantable zaměřenou na webová data a analytiku, se v Google Search Console začaly u některých webů objevovat velmi neobvyklé dotazy. Místo typických krátkých frází z vyhledávání obsahovaly celé věty či odstavce, často přes 300 znaků, psané stylem jasně odpovídajícím promptům pro AI asistenta. Šlo například o žádosti o pomoc s partnerskými problémy, obchodní strategií nebo interní firemní agendou – obsah, který uživatelé typicky vnímají jako důvěrný.

Packer společně s konzultantem Slobodanem Manićem provedli sérii experimentů. Podle jejich závěrů se podezřelé dotazy chovaly konzistentně s tím, jako by OpenAI či jí využívaná infrastruktura odesílala části uživatelských promptů do Google Search. Cílem může být obohacení odpovědí aktuálními informacemi bez přímého přístupu k interním datům Google. Z technického hlediska jde o scénář, kdy služba AI používá externí vyhledávač jako backend, přičemž části uživatelského vstupu se dostanou do logů Google a následně do GSC daných webů.

OpenAI na dotazy Ars Technica nereagovalo konkrétními technickými detaily. Společnost pouze přiznala existenci problému, popsala ho jako krátkodobou chybu v tom, jak byla „malá část vyhledávacích dotazů směrována“, a tvrdí, že již byla opravena. Nezaznělo však, jak přesně k routování došlo, kolik uživatelů bylo dotčeno, ani zda šlo o vedlejší efekt interních testů integrace s vyhledáváním, nebo součást běžného provozu.

Provozovatelé webů, kteří úniky zaznamenali, tak získali neúmyslný přístup k cizím citlivým informacím. To vytváří právní i etické riziko, protože prompt může obsahovat osobní údaje, neveřejné obchodní informace nebo interní dokumenty, které uživatelé vkládají do AI nástrojů v domnění, že zůstávají v rámci jedné služby.

## Proč je to důležité
Tento incident odhaluje slabiny v tom, jak jsou nástroje AI integrovány s externími systémy a službami. Ukazuje, že i bez klasického „hacku“ může docházet k únikům promptů přes legitimní kanály, jako jsou vyhledávače nebo analytické nástroje. Pro firmy, které používají AI asistenty k zpracování interních dokumentů, právních materiálů nebo zákaznických dat, je to varování: bez jasně definovaných datových toků, smluvních garancí a technických omezení může být soukromý obsah neúmyslně vystaven třetím stranám.

Pro OpenAI jde o reputační problém zdůrazňující nedostatečnou transparentnost ohledně využívání uživatelských dat a interakcí s ekosystémem Google. Pro regulátory v EU i jinde je to další argument pro přísnější požadavky na auditovatelnost systémů AI, logování datových toků a vynutitelné limity na to, co se smí dít s promptem po jeho odeslání. Pro celý sektor AI je to signál, že otázka soukromí a bezpečnosti uživatelských dotazů není detail implementace, ale klíčová vlastnost služby, která bude čím dál více ovlivňovat důvěru i obchodní využitelnost těchto technologií.

---

[Číst původní článek](https://arstechnica.com/tech-policy/2025/11/oddest-chatgpt-leaks-yet-cringey-chat-logs-found-in-google-analytics-tool/)

**Zdroj:** 🔬 Ars Technica
