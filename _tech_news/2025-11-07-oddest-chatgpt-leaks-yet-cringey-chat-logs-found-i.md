---
author: Marisa Aigen
category: ai
companies:
- ChatGPT
- OpenAI
- Google
- Microsoft
- Apple
date: '2025-11-07 16:49:53'
description: Vyšetřování konzultantů odhalilo, že citlivé dotazy z ChatGPT se objevovaly
  v Google Search Console, což může potvrzovat, že OpenAI pracuje s reálnými uživatelskými
  prompty z Google a tím otevírá vážné otázky ochrany soukromí a transparentnosti.
importance: 3
layout: tech_news_article
original_title: 'Oddest ChatGPT leaks yet: Cringey chat logs found in Google analytics
  tool - Ars Technica'
publishedAt: '2025-11-07T16:49:53+00:00'
slug: oddest-chatgpt-leaks-yet-cringey-chat-logs-found-i
source:
  emoji: 🔬
  id: ars-technica
  name: Ars Technica
title: ChatGPT úniky v Google Search Console naznačují přímé sbírání dat z vyhledávání
url: https://arstechnica.com/tech-policy/2025/11/oddest-chatgpt-leaks-yet-cringey-chat-logs-found-in-google-analytics-tool/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/11/chatgpt-private-chats-1152x648.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/11/chatgpt-private-chats-1152x648.jpg
---

## Souhrn
Citlivé konverzace uživatelů s ChatGPT se nečekaně objevily v nástroji Google Search Console, který slouží správcům webů pro analýzu návštěvnosti z vyhledávání. Analýza konzultantů naznačuje, že šlo o kombinaci technické chyby a pravděpodobného přímého využívání vyhledávacích dotazů Google ze strany OpenAI, což otevírá zásadní otázky ohledně ochrany soukromí, sběru dat a způsobu trénování AI modelů.

## Klíčové body
- Dlouhé a intimní dotazy podobné promptům ChatGPT se objevily v Google Search Console u vybraných webů.
- Analytici Jason Packer (Quantable) a Slobodan Manić provedli testy, které naznačují, že OpenAI přímo pracuje s dotazy z Google Search.
- OpenAI přiznala existenci „chyby v routování dotazů“, tvrdí však, že problém byl omezený a již vyřešený.
- Firma odmítla detailně vysvětlit technické pozadí incidentu, rozsah úniku nebo přesný mechanismus sběru dat.
- Případ zvyšuje tlak na větší transparentnost AI firem ohledně zdrojů tréninkových dat a nakládání s uživatelskými vstupy.

## Podrobnosti
Google Search Console (GSC) je nástroj pro správce webů, který poskytuje statistiky o tom, jaké dotazy z Google Search vedou uživatele na jejich stránky. Standardně se v něm zobrazují krátké fráze či klíčová slova. Od září však někteří správci začali v přehledech nacházet výrazně delší texty, často přes 300 znaků, které měly formu plných promptů typu „napiš právní analýzu...“, „pomoz mi vyřešit problém ve vztahu...“ nebo detailní firemní scénáře. Tyto dotazy neseděly na běžné chování uživatelů vyhledávače, ale přesně odpovídaly stylu komunikace lidí s chatbotem.

Na problém upozornil Jason Packer, majitel analytické konzultační firmy Quantable, která se zaměřuje na datovou analýzu a optimalizaci webů. Společně se Slobodanem Manićem, konzultantem pro webovou optimalizaci, provedli cílené testy: generovali specifické prompty a sledovali, zda a jak se následně objeví v GSC. Na základě chování dat dospěli k závěru, že může jít o první konkrétní důkaz, že OpenAI přímo využívá dotazy z Google Search nebo na ně napojený tok dat pro své systémy, případně že interní mechanismy OpenAI posílají uživatelské prompty do prostředí viditelného pro správce webů.

OpenAI odmítla jejich hypotézu potvrdit, přiznala ale, že došlo k „dočasné chybě v routování malého počtu dotazů“, která byla podle firmy opravena. Neposkytla však technické detaily, jak k problému došlo, zda byly prompty uložené, jak dlouho byly viditelné, ani zda šlo o testovací prostředí nebo produkční systém. Tato neochota k detailnímu vysvětlení je problematická zejména vzhledem k tomu, že některé zachycené dotazy obsahovaly vysoce citlivé informace o osobních vztazích, pracovních konfliktech či interních procesech firem, které uživatelé vkládají do ChatGPT v domnění, že zůstanou neveřejné.

## Proč je to důležité
Incident ukazuje dvě zásadní roviny problému. Za prvé, uživatelé nemají reálný přehled o tom, jak jsou jejich prompty technicky zpracovávány, kudy data protékají a kdo k nim může získat nepřímý přístup. I relativně „malá“ chyba v routování dotazů může vést k tomu, že citlivý obsah skončí v nástrojích třetích stran, kde s ním lze pracovat, analyzovat ho a archivovat.

Za druhé, případ posiluje podezření, že velké AI společnosti agresivně využívají data z ekosystému webu a vyhledávání, aniž by transparentně popsaly, odkud přesně čerpají, jaká smluvní ujednání mají s poskytovateli a jaké mechanismy anonymizace skutečně používají. Pro firmy, které používají ChatGPT pro interní nebo obchodně citlivé úlohy, to je jasný signál nutnosti omezit sdílení konkrétních dat, oddělit veřejné a interní instance AI (on-premise, vyhrazené API) a požadovat smluvní záruky ohledně nakládání s dotazy.

V širším kontextu jde o další důkaz, že regulace v oblasti AI a ochrany dat bude muset řešit nejen trénování modelů na veřejných datech, ale i provozní toky dat, auditovatelnost a povinnost poskytovat technicky srozumitelné vysvětlení podobných incidentů.

---

[Číst původní článek](https://arstechnica.com/tech-policy/2025/11/oddest-chatgpt-leaks-yet-cringey-chat-logs-found-in-google-analytics-tool/)

**Zdroj:** 🔬 Ars Technica
