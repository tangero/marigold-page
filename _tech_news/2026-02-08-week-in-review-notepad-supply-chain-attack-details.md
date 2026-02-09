---
author: Marisa Aigen
category: kybernetika
date: '2026-02-08 09:00:42'
description: Přehled nejdůležitějších kybernetických zpráv minulého týdne zahrnuje
  útok na aktualizační mechanismus Notepad++, novou open-source mapu globálních hrozeb
  a exploitaci zranitelností státními hackery.
importance: 5
layout: tech_news_article
original_title: 'Week in review: Notepad++ supply chain attack details and targets,
  Patch Tuesday forecast'
publishedAt: '2026-02-08T09:00:42+00:00'
slug: week-in-review-notepad-supply-chain-attack-details
source:
  emoji: 📰
  id: null
  name: Help Net Security
title: 'Týdenní přehled: Podrobnosti o útoku na řetězec dodávek Notepad++, cíle a
  předpověď Patch Tuesday'
url: https://www.helpnetsecurity.com/2026/02/08/week-in-review-notepad-supply-chain-attack-details-and-targets-patch-tuesday-forecast/
urlToImage: https://img.helpnetsecurity.com/wp-content/uploads/2024/03/25124830/cybersecurity-week-review-1-1500.webp
urlToImageBackup: https://img.helpnetsecurity.com/wp-content/uploads/2024/03/25124830/cybersecurity-week-review-1-1500.webp
---

## Souhrn
Týdenní shrnutí klíčových událostí v kybernetické bezpečnosti zahrnuje podrobnosti o útoku na řetězec dodávek Notepad++, kde čínští státem sponzorovaní útočníci kompromitovali hostingový server a přesměrovali aktualizační provoz. Další témata zahrnují open-source platformu Global Threat Map pro real-time vizualizaci hrozeb, social engineering útoky obcházející MFA od skupiny ShinyHunters a exploitaci zranitelnosti CVE-2026-21509 ruskými hackery Fancy Bear v Microsoft Office.

## Klíčové body
- Čínská skupina Lotus Blossom (Billbug) zaútočila na Notepad++ tím, že ovládla sdílený hostingový server a přesměrovala aktualizace na notepad-plus-plus.org.
- Global Threat Map: open-source nástroj pro bezpečnostní týmy, který agreguje veřejné datové zdroje do interaktivní mapy malware, phishingu a útočného provozu podle regionů.
- Ruská APT 28 (Fancy Bear) exploituje nedávno opravenou zranitelnost CVE-2026-21509 v Microsoft Office.
- ShinyHunters používají MFA jako návnadu v social engineeringu pro krádež dat.
- Nový malware zneužívá deset let starý ovladač EnCase k deaktivaci 59 endpointových bezpečnostních produktů.

## Podrobnosti
Článek shrnuje události z oblasti kybernetické bezpečnosti za uplynulý týden, s důrazem na supply chain útok na Notepad++, populární open-source textový editor používaný pro úpravu kódu a konfiguračních souborů na Windows. Vývojář Don Ho potvrdil, že podezřelí čínští státem sponzorovaní útočníci kompromitovali sdílený hostingový server projektu. Tím převzali kontrolu nad aktualizačním mechanismem a přesměrovávali provoz určený pro doménu notepad-plus-plus.org na vlastní servery. Analytici firmy Rapid7 připisují útok skupině Lotus Blossom, známé také jako Billbug, která se zaměřuje na špionáž v organizacích jihovýchodní Asie. Poskytli indikátory kompromitace (IoC), včetně IP adres a domén použitých v kampani.

Další významnou zprávou je Global Threat Map, open-source projekt určený bezpečnostním týmům pro okamžité zobrazení globálních kybernetických hrozeb. Platforma sbírá data z veřejných zdrojů, jako jsou feeds o malwaru, phishingu a útočném provozu, a vizualizuje je na interaktivní mapě rozdělené podle geografických regionů. To umožňuje rychlou identifikaci trendů, například zvýšené distribuce malwaru v určité zemi.

Skupina ShinyHunters, známá pro krádeže dat, nyní zneužívá vícefaktorové ověřování (MFA) v social engineeringových útocích. MFA, které má bránit phishingu tím, že vyžaduje druhý faktor autentizace (např. SMS kód nebo appku), slouží zde jako záminka k získání přístupu. Útočníci předstírají potřebu MFA k přihlášení a tak obcházejí ochranu.

Ruské státem sponzorované hackery Fancy Bear (APT 28) aktivně exploitují CVE-2026-21509 v Microsoft Office, zranitelnost typu zero-day, pro kterou Microsoft vydal nouzovou záplatu minulý týden. Tato chyba umožňuje vzdálené spuštění kódu přes speciálně upravené dokumenty. Navíc útočníci používají nový malware, který zneužívá deset let starý ovladač EnCase – nástroje pro forenzní analýzu dat používaného policií a bezpečnostními firmami – k vypnutí 59 endpointových detekčních a reakčních (EDR) systémů, jako jsou ty od CrowdStrike nebo Microsoft Defender.

## Proč je to důležité
Tyto události podtrhují zranitelnost supply chain útoků, kde kompromitace jediného serveru ohrozí miliony uživatelů Notepad++, což vede k distribuci malwaru přímo přes důvěryhodné aktualizace. Pro uživatele to znamená nutnost ověřovat zdroje aktualizací a používat podpisy. V širším kontextu eskaluje státní kyberšpionáž: čínské skupiny cílí Asii, ruské Západ, což zvyšuje rizika pro firmy. Global Threat Map pomáhá v proaktivní obraně, zatímco exploit CVE-2026-21509 zdůrazňuje důležitost rychlého patchování. EDR killery ukazují, jak staré legitimní nástroje slouží k obraně proti obraně, což nutí výrobce EDR k lepší kernelové izolaci. Celkově to signalizuje rostoucí sofistikovanost útoků, kde MFA selhává proti social engineeringu a staré zranitelnosti zůstávají rizikem.

---

[Číst původní článek](https://www.helpnetsecurity.com/2026/02/08/week-in-review-notepad-supply-chain-attack-details-and-targets-patch-tuesday-forecast/)

**Zdroj:** 📰 Help Net Security
