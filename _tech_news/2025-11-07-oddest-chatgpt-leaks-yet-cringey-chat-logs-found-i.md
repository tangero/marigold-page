---
author: Marisa Aigen
category: ai
companies:
- OpenAI
- Google
- Microsoft
- Apple
- NVIDIA
date: '2025-11-07 16:49:53'
description: Měsíce unikaly osobní dotazy uživatelů ChatGPT do Google Search Console,
  což naznačuje problematické zpracování uživatelských vstupů a možné přímé skenování
  Googlu ze strany OpenAI.
importance: 4
layout: tech_news_article
original_title: 'Oddest ChatGPT leaks yet: Cringey chat logs found in Google analytics
  tool - Ars Technica'
publishedAt: '2025-11-07T16:49:53+00:00'
slug: oddest-chatgpt-leaks-yet-cringey-chat-logs-found-i
source:
  emoji: 🔬
  id: ars-technica
  name: Ars Technica
title: 'Nejpodivnější úniky ChatGPT: citlivé konverzace se objevily v nástroji Google
  Search Console'
url: https://arstechnica.com/tech-policy/2025/11/oddest-chatgpt-leaks-yet-cringey-chat-logs-found-in-google-analytics-tool/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/11/chatgpt-private-chats-1152x648.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/11/chatgpt-private-chats-1152x648.jpg
---

## Souhrn
Citlivé a osobní dotazy z konverzací s ChatGPT se objevily v Google Search Console (GSC), nástroji určeném pro správce webů k analýze vyhledávacího provozu. Analýza konzultantů naznačuje, že OpenAI použilo reálné uživatelské prompt dotazy při dotazování na Google, čímž mohlo dojít k narušení soukromí i k využití dat z vyhledávače způsobem, který není transparentní.

## Klíčové body
- V GSC se od září začaly objevovat extrémně dlouhé řetězce dotazů (300+ znaků), odpovídající promptům z ChatGPT, včetně intimních a obchodně citlivých informací.
- Problém identifikovali Jason Packer (Quantable) a konzultant Slobodan Manić, jejichž testy naznačují, že OpenAI přímo dotazovalo Google s reálnými uživatelskými vstupy.
- OpenAI odmítla detailně vysvětlit mechanismus, pouze uvedla, že „si problému byla vědoma“ a opravila „chybu v routování malé části dotazů“.
- Únik ukazuje na slabé procesy v oblasti ochrany soukromí, řízení promptů a nakládání s uživatelskými daty v AI službách.
- Incident posiluje tlak na regulaci generativní AI a transparentní nakládání s dotazy, které často obsahují vysoce citlivá data.

## Podrobnosti
V Google Search Console, kterou provozovatelé webů používají k monitorování, jaké dotazy z vyhledávání Google vedou na jejich stránky, se začaly objevovat nezvykle dlouhé a detailní dotazy. Nešlo o běžné fráze typu „návod“ nebo „recenze“, ale o kompletní prompt řetězce, například žádosti o pomoc s partnerskými problémy, právními otázkami, interními firemními strategiemi nebo citlivými finančními situacemi. Tyto texty jasně odpovídají stylu zadávání dotazů do ChatGPT a jiných chatbotů, nikoli klasickému vyhledávání.

Na problém upozornil Jason Packer, majitel analytické konzultační firmy Quantable, která se specializuje na měření a optimalizaci výkonu webů. Společně se Slobodanem Manićem, konzultantem pro webovou optimalizaci, provedli sérii testů. Podle jejich zjištění se zdá, že OpenAI pro některé funkce automatizovaně dotazovala Google Search a v rámci toho odesílala skutečné prompt texty uživatelů jako součást vyhledávacích dotazů. To by znamenalo, že soukromé dotazy uživatelů byly nepřímo sdíleny s Googlem a následně se objevovaly v GSC provozovatelů webů, pokud jejich stránky zachytily tyto dotazy.

OpenAI na dotazy Ars Technica nereagovala konkrétní technickou rekonstrukcí incidentu. Společnost pouze přiznala, že o problému ví a že opravila „glitch“, který dočasně ovlivnil směrování části vyhledávacích dotazů. Bez technických detailů však zůstává nejasné, jak široký byl zásah, jak dlouho trval, kolika uživatelů se týkal a zda byly prompt texty použity i pro další interní účely. Packer incident hodnotí jako rychle technicky vyřešený, ale otázka důvěry v zacházení s prompt daty zůstává otevřená.

## Proč je to důležité
Incident je významný ze tří důvodů. Zaprvé ukazuje, jak křehké jsou současné procesy ochrany soukromí v generativních AI službách. Uživatelé vkládají do ChatGPT a podobných nástrojů vysoce citlivé informace v domnění, že zůstávají v uzavřeném systému. Jakýkoli únik, byť nepřímý přes vyhledávací dotazy, zpochybňuje důvěru v tato řešení.

Zadruhé naznačuje možnost, že velcí poskytovatelé AI aktivně využívají data z webového vyhledávání k obohacení svých modelů či k lepším odpovědím, a to způsobem, který není transparentně komunikován. Pokud jsou skutečné uživatelské prompty používány při dotazování na Google, vzniká otázka, zda nejde o neoprávněné sdílení dat a porušení podmínek jak vůči uživatelům, tak vůči provozovateli vyhledávače.

Zatřetí incident posiluje argumenty pro regulaci a povinnou dokumentaci datových toků v AI: podniky i veřejné instituce budou muset počítat s tím, že prompt není „bezpečný formulář“, ale potenciální vstup do komplexního ekosystému API, logů a externích služeb. Pro firmy je to jasný signál, že do veřejných chatbotů nesmí vkládat neveřejné obchodní informace bez smluvních záruk, a pro poskytovatele AI je to test jejich ochoty otevřeně vysvětlit, jak s daty ve skutečnosti nakládají.

---

[Číst původní článek](https://arstechnica.com/tech-policy/2025/11/oddest-chatgpt-leaks-yet-cringey-chat-logs-found-in-google-analytics-tool/)

**Zdroj:** 🔬 Ars Technica
