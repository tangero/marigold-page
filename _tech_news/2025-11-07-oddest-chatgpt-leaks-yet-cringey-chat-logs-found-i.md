---
author: Marisa Aigen
category: ai
companies:
- OpenAI
- Google
- Microsoft
date: '2025-11-07 16:49:53'
description: V Google Search Console se objevily dlouhé a citlivé dotazy z ChatGPT,
  což naznačuje chybnou integraci a možný scraping Google dat ze strany OpenAI. Případ
  vyvolává otázky o ochraně soukromí, transparentnosti a metodách trénování AI modelů.
importance: 4
layout: tech_news_article
original_title: 'Oddest ChatGPT leaks yet: Cringey chat logs found in Google analytics
  tool - Ars Technica'
people:
- Elon Musk
- Sam Altman
- Ilya Sutskever
publishedAt: '2025-11-07T16:49:53+00:00'
slug: oddest-chatgpt-leaks-yet-cringey-chat-logs-found-i
source:
  emoji: 🔬
  id: ars-technica
  name: Ars Technica
title: 'Kuriózní úniky ChatGPT: citlivé chaty se objevily v Google Search Console'
url: https://arstechnica.com/tech-policy/2025/11/oddest-chatgpt-leaks-yet-cringey-chat-logs-found-in-google-analytics-tool/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/11/chatgpt-private-chats-1152x648.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/11/chatgpt-private-chats-1152x648.jpg
---

## Souhrn
V nástroji Google Search Console se měsíce objevovaly extrémně dlouhé a citlivé texty připomínající uživatelské konverzace s ChatGPT, včetně osobních i obchodních problémů, které měly zůstat soukromé. Analýza konzultantů Jasona Packera a Slobodana Maniće naznačuje, že OpenAI využívala uživatelské dotazy i data z Google vyhledávání způsobem, který vedl k nechtěným únikům, a tím otevřela zásadní otázky ohledně zpracování dat, ochrany soukromí a závislosti AI firem na datech vyhledávačů.

## Klíčové body
- V Google Search Console se objevily více než 300znakové dotazy odpovídající částem konverzací z ChatGPT.
- Incident odhalil možnou kombinaci uživatelských promptů a dotazů směrovaných na Google Search, což naznačuje, že OpenAI aktivně pracovala s daty z vyhledávání.
- Analytik Jason Packer (Quantable) a konzultant Slobodan Manić provedli testy, které považují za první přímý důkaz scrapingových praktik OpenAI vůči Google Search.
- OpenAI problém označila za „vyřešený“ a popsala jej jako dočasnou chybu směrování malého počtu dotazů, ale odmítla detailněji vysvětlit rozsah a mechanismus.
- Případ vyvolává pochybnosti o transparentnosti OpenAI a o tom, jak bezpečně jsou zpracovávány citlivé uživatelské informace.

## Podrobnosti
Podle zjištění provozovatelů webů se od září v Google Search Console (GSC) začaly objevovat velmi neobvyklé dotazy. Místo běžných klíčových slov se v přehledech vyhledávání zobrazovaly dlouhé texty, často přesahující 300 znaků, formulované jako kompletní prompt pro AI asistenta. Obsahoval osobní zpovědi, obchodní strategie, interní informace nebo intimní problémy, které uživatelé zjevně zadávali do rozhraní ChatGPT s očekáváním důvěrnosti.

Jason Packer, majitel analytické konzultační firmy Quantable, která se zabývá měřením návštěvnosti a optimalizací webů, incident detailně popsal na svém blogu. Společně se Slobodanem Manićem, konzultantem v oblasti webové optimalizace, provedli sérii testů: simulovali specifické dotazy, sledovali jejich chování v čase a porovnávali je s daty v GSC. Na základě těchto experimentů dospěli k závěru, že některé uživatelské prompty byly využívány k dotazům na Google, přičemž jejich části skončily viditelné v účtech provozovatelů webů.

Jejich interpretace je, že OpenAI v rámci svých mechanismů pro vyhledávání informací a doplňování odpovědí mohla směrovat části promptů nebo generovaných dotazů do Google Search, čímž:
- jednak přímo či nepřímo využívala Google jako zdroj aktuálních informací,
- jednak neúmyslně vystavila části citlivých textů třetím stranám prostřednictvím GSC.

OpenAI na dotazy serveru Ars Technica nereagovala konkrétní technickou analýzou. Uvedla pouze, že si byla problému vědoma, identifikovala chybu v routování malého množství vyhledávacích dotazů a tu opravila. Neobjasnila ale, jak přesně chyba vznikla, jak dlouho trvala, kolika uživatelů se týkala ani zda šlo o strukturální součást integrace s externími vyhledávači.

## Proč je to důležité
Případ podtrhuje několik zásadních problémů současného ekosystému AI:

Za prvé, otázku důvěry v poskytovatele AI služeb. Uživatelé očekávají, že prompty obsahující osobní, právní či obchodní informace zůstanou důvěrné. Jakýkoliv únik do nástrojů třetích stran, jako je Google Search Console, ukazuje na nedostatečnou kontrolu nad datovými toky a architekturou napojení na externí služby.

Za druhé, zpochybňuje se transparentnost velkých AI firem ohledně toho, odkud berou data pro své modely a jakým způsobem využívají vyhledávače. Pokud OpenAI nebo jiné společnosti směrují části promptů do vyhledávání, otevírá to právní i regulatorní otázky (GDPR, ochrana obchodního tajemství, souhlas se zpracováním dat).

Za třetí, incident je varováním pro podniky a státní instituce, které používají ChatGPT nebo podobné AI nástroje pro práci s citlivými dokumenty. I krátkodobá „chyba“ může znamenat únik informací bez možnosti zjistit rozsah. Firmy by proto měly přísně hodnotit podmínky zpracování dat, používat enterprise verze s jasně definovanými pravidly a omezit vkládání citlivých údajů do veřejných AI služeb.

Celkově nejde jen o technický bug, ale o signál, že AI poskytovatelé musí výrazně zpřísnit kontrolu nad integracemi, logováním a využíváním uživatelských promptů. Jinak budou podobné kauzy dál oslabovat důvěru v použití AI v kritických oblastech.

---

[Číst původní článek](https://arstechnica.com/tech-policy/2025/11/oddest-chatgpt-leaks-yet-cringey-chat-logs-found-in-google-analytics-tool/)

**Zdroj:** 🔬 Ars Technica
