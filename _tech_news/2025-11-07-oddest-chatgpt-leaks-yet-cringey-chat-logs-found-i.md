---
author: Marisa Aigen
category: ai
companies:
- OpenAI
- Google
- Microsoft
- Apple
- Meta
date: '2025-11-07 16:49:53'
description: Vyšetřování ukazuje, že osobní dotazy z ChatGPT končily v Google Search
  Console, což naznačuje možné přímé využití reálných uživatelských promptů při procházení
  webu a otevírá vážné otázky ohledně ochrany soukromí a datových praktik OpenAI.
importance: 4
layout: tech_news_article
original_title: 'Oddest ChatGPT leaks yet: Cringey chat logs found in Google analytics
  tool - Ars Technica'
people:
- Elon Musk
- Tim Cook
- Satya Nadella
publishedAt: '2025-11-07T16:49:53+00:00'
slug: oddest-chatgpt-leaks-yet-cringey-chat-logs-found-i
source:
  emoji: 🔬
  id: ars-technica
  name: Ars Technica
title: 'Nejpodivnější úniky ChatGPT: Citlivé konverzace se objevily v nástroji Google
  Search Console'
url: https://arstechnica.com/tech-policy/2025/11/oddest-chatgpt-leaks-yet-cringey-chat-logs-found-in-google-analytics-tool/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/11/chatgpt-private-chats-1152x648.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/11/chatgpt-private-chats-1152x648.jpg
---

## Souhrn
Vyšetřování analytiků odhalilo, že část citlivých konverzací z ChatGPT se objevovala v Google Search Console, nástroji pro sledování vyhledávacího provozu, kde nemají co dělat. Incident naznačuje, že OpenAI při procházení webu zřejmě využívala skutečné uživatelské prompty, což vyvolává zásadní otázky ohledně ochrany soukromí, nakládání s daty a transparentnosti AI platforem.

## Klíčové body
- Dlouhé a osobní dotazy z ChatGPT se začaly objevovat v Google Search Console od září.
- Analytici Jason Packer (Quantable) a Slobodan Manić provedli testy, které naznačují přímé použití reálných promptů při procházení Google Search.
- Zjištění jsou interpretována jako „první definitivní důkaz“, že OpenAI přímo využívá data z Google Search s reálnými uživatelskými vstupy.
- OpenAI připustila „chybu v směrování dotazů“, tvrdí, že problém vyřešila, ale neposkytla detailní vysvětlení.
- Událost posiluje tlak na regulaci a auditovatelnost AI služeb z hlediska soukromí a datových toků.

## Podrobnosti
Podstatou zjištění je, že správci webů začali v Google Search Console (GSC) pozorovat nezvykle dlouhé dotazy, často přes 300 znaků, které neodpovídaly běžnému chování uživatelů vyhledávače. GSC standardně zobrazuje krátké vyhledávací dotazy, které lidé zadávají do Google, aby našli obsah na konkrétním webu. Nově se však objevovaly celé věty a komplexní zadání, jasně psaná jako prompty pro ChatGPT – včetně intimních dotazů o vztazích, interních firemních informací a obchodních strategií.

Na problém jako jeden z prvních upozornil Jason Packer, majitel analytické konzultační firmy Quantable, která se zaměřuje na měření a optimalizaci webové návštěvnosti. Ve spolupráci se specialistou na optimalizaci webu Slobodanem Manićem provedli sérii testů. Jejich závěr: úniky vypadají jako vedlejší efekt toho, že OpenAI při procházení webu a generování odpovědí používá skutečné uživatelské prompty, které následně končí jako součást dotazů směrovaných přes infrastrukturu související s Google Search.

Podle jejich analýzy tak vznikl vzorec, který může představovat „první jednoznačný důkaz“, že OpenAI nejen trénuje a ladí modely na uživatelských vstupech, ale tyto vstupy mohou být v určitých případech přímo použity v automatizovaných dotazech vůči vyhledávačům. To má dva zásadní důsledky. Za prvé, jde o zjevné riziko pro soukromí – uživatelé očekávají, že jejich konverzace s ChatGPT zůstanou neveřejné a nebudou se objevovat v analytických nástrojích třetích stran. Za druhé, vyvolává to otázky ohledně férového přístupu k datům z vyhledávačů a možného obcházení omezení, která Google uplatňuje vůči externím subjektům.

OpenAI na dotazy redakce Ars Technica odpověděla pouze částečně. Firma potvrdila, že o incidentu ví, označila ho za „glitch“, tedy chybu v dočasném směrování malé části dotazů, a tvrdí, že problém byl vyřešen. Odmítla však detailně vysvětlit mechanismus, který k úniku vedl, ani nesdělila, jak velký objem dat byl dotčen a jaké konkrétní ochranné kroky byly zavedeny. Tento nedostatek transparentnosti je pro oblast AI služeb s citlivými daty zásadní problém.

## Proč je to důležité
Incident zpochybňuje důvěru v to, jak velcí hráči v AI nakládají s uživatelskými daty. Uživatelé vkládají do ChatGPT a podobných nástrojů detailní osobní, pracovně-právní, zdravotní či obchodní informace v domnění, že jsou chráněny a používány pouze v anonymizované podobě pro zlepšování služeb.

Skutečnost, že takové prompty mohou skončit jako součást interních technických procesů směrem k jiným platformám, jako je Google Search, ukazuje na strukturální slabinu: nedostatečně jasně vymezené hranice mezi trénováním modelů, provozními procesy a ochranou soukromí. Pro průmysl to znamená rostoucí tlak na:

- nezávislé audity datových praktik AI firem,
- striktní režimy oddělení citlivých uživatelských vstupů od provozních nástrojů,
- transparentnější smluvní podmínky, které jasně popíší, co se s daty děje,
- regulatorní zásahy (zejména v EU), které budou vyžadovat prokazatelné minimalizování a kontrolu datových toků.

Pro firmy využívající AI asistenty to je varování, že jakýkoli vklad citlivých dat do cloudových AI služeb musí být posuzován stejně přísně jako sdílení s externím dodavatelem: s právními, bezpečnostními a reputačními dopady v případě podobných úniků.

---

[Číst původní článek](https://arstechnica.com/tech-policy/2025/11/oddest-chatgpt-leaks-yet-cringey-chat-logs-found-in-google-analytics-tool/)

**Zdroj:** 🔬 Ars Technica
