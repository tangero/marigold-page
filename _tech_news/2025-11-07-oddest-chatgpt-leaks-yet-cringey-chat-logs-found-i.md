---
author: Marisa Aigen
category: ai
companies:
- OpenAI
- Google
- Microsoft
- Apple
date: '2025-11-07 16:49:53'
description: Vyšetřování analytiků odhalilo, že extrémně osobní dotazy z ChatGPT se
  objevovaly v Google Search Console, což naznačuje přímé využívání Google vyhledávání
  s reálnými uživatelskými promptami a otevírá vážné otázky ohledně ochrany soukromí
  a praktik OpenAI.
importance: 4
layout: tech_news_article
original_title: 'Oddest ChatGPT leaks yet: Cringey chat logs found in Google analytics
  tool - Ars Technica'
people:
- Elon Musk
- Sam Altman
- Greg Brockman
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
Z analýzy dat v Google Search Console (GSC) vyplynulo, že se v něm po měsíce objevovaly celé, vysoce osobní dotazy uživatelů ChatGPT, a to ve formě dlouhých řetězců, které do běžného vyhledávání nedávají smysl. Vyšetřování analytiků naznačuje, že OpenAI zřejmě posílal reálné uživatelské prompty do Google vyhledávání, což by znamenalo závažný problém z hlediska ochrany soukromí a nakládání s daty.

## Klíčové body
- Extrémně dlouhé a citlivé dotazy z ChatGPT se objevily v Google Search Console jako skutečné vyhledávací dotazy.
- Analytici Jason Packer (Quantable) a Slobodan Manić testováním dospěli k závěru, že OpenAI používal reálné prompty při dotazování na Google Search.
- OpenAI přiznal existenci „chyby v routování“ omezeného počtu dotazů a tvrdí, že problém byl vyřešen, odmítl však potvrdit detailní mechanismus.
- Incident otevírá zásadní otázky ohledně ochrany soukromí, souladu se zásadami zpracování dat a transparentnosti AI firem.
- Pro provozovatele webů i uživatele jde o varování, že obsah zadávaný do AI nástrojů může skončit mimo očekávaný ekosystém.

## Podrobnosti
Jádrem problému je zjištění, že správci webů začali od září v Google Search Console pozorovat nezvykle dlouhé dotazy, často přesahující 300 znaků. Nešlo o typické vyhledávací fráze, ale o kompletní věty a pasáže připomínající prompty zadávané do chatbotů, například žádosti o rady v oblasti vztahů, podnikání či pracovních problémů. Tyto dotazy byly dostatečně konkrétní a osobní na to, aby bylo zřejmé, že je tito lidé nepředpokládali jako veřejně dohledatelné.

Na problém upozornil Jason Packer, majitel analytické konzultační firmy Quantable, která se specializuje na webovou analytiku a měření návštěvnosti. Společně s konzultantem Slobodanem Manićem provedli cílené testy: zadávali specificky formulované prompty do ChatGPT a následně ověřovali, zda se tyto nebo podobné řetězce objeví v GSC na sledovaných doménách. Výsledky jejich testů podle nich představují přímý důkaz, že OpenAI v některých situacích posílal skutečné uživatelské dotazy do Google Search, pravděpodobně za účelem získávání aktuálních informací nebo validace odpovědí.

OpenAI na dotazy redakce Ars Technica reagoval stroze. Potvrdil, že o problému ví a že šlo o „glitch“, tedy chybu v tom, jak byla malá část dotazů směrována na vyhledávání, a že tato chyba byla opravena. Neodpověděl však na klíčové otázky: v jakém rozsahu k únikům docházelo, jak dlouho trvaly, jaký přesný mechanismus byl použit a zda byly prompty před odesláním anonymizovány. Bez těchto informací zůstává nejistota ohledně míry rizika pro uživatele.

Pro uživatele to znamená, že prompty zadávané do AI nástrojů, jako je ChatGPT, nelze považovat za plně soukromé, pokud poskytovatel neprokazuje přísnou izolaci, šifrování a kontrolu přístupu. Pro provozovatele webů je incident potvrzením, že do jejich datových sad se mohou dostat citlivé informace, aniž by o to stáli, a že musí být opatrní při jejich interpretaci a ukládání.

## Proč je to důležité
Tento incident je významný ve třech rovinách. Zaprvé, zásadně zpochybňuje předpoklad, že interakce s AI nástroji jsou důvěrné. Pokud poskytovatel AI použije reálné uživatelské prompty pro dotazování externích služeb, dochází potenciálně k porušení očekávání soukromí, interních i veřejných politik ochrany dat a v některých případech i právních předpisů, zejména v EU.

Zadruhé, spor otevírá otázku transparentnosti AI firem. OpenAI i další velcí hráči staví své produkty na masivním sběru dat, ale jen omezeně vysvětlují, jak přesně zacházejí s promptami, zda je používají pro trénink, jak jsou anonymizovány a jak jsou sdíleny s třetími stranami. Nedostatečně konkrétní reakce na tento incident oslabuje důvěru uživatelů i firemních zákazníků.

Zatřetí, pro širší technologický ekosystém jde o varování, že integrace AI s vyhledáváním, API a externími službami musí být navržena s předpokladem, že vstup může obsahovat vysoce citlivá osobní či obchodní data. Regulátoři, podniky i poskytovatelé AI budou muset zpřísnit smluvní podmínky, auditní mechanismy a technická opatření, aby se zabránilo dalším podobným únikům a posílila se odpovědnost za nakládání s daty uživatelů.

---

[Číst původní článek](https://arstechnica.com/tech-policy/2025/11/oddest-chatgpt-leaks-yet-cringey-chat-logs-found-in-google-analytics-tool/)

**Zdroj:** 🔬 Ars Technica
