---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Microsoft
date: '2026-02-18 16:22:12'
description: Asistent Microsoft Copilot v Microsoft 365 má kritickou chybu, která
  umožňuje umělé inteligenci skenovat a shrnovat e-maily označené jako důvěrné v Outlooku,
  včetně složek Odeslané a Koncepty. Microsoft zavádí opravu, ale není jasný časový
  rámec, což zvyšuje obavy z ochrany soukromí a spolehlivosti AI.
importance: 5
layout: tech_news_article
original_title: Copilot bug allows ‘AI’ to read confidential Outlook emails
publishedAt: '2026-02-18T16:22:12+00:00'
slug: copilot-bug-allows-ai-to-read-confidential-outlook
source:
  emoji: 📰
  id: null
  name: PCWorld
title: Chyba v Copilot umožňuje AI číst důvěrné e-maily v Outlooku
url: https://www.pcworld.com/article/3064782/copilot-bug-allows-ai-to-read-confidential-outlook-emails.html
urlToImage: https://www.pcworld.com/wp-content/uploads/2026/02/image_930daa.png?w=1024
urlToImageBackup: https://www.pcworld.com/wp-content/uploads/2026/02/image_930daa.png?w=1024
---

## Souhrn
Microsoft Copilot, AI asistent integrovaný do Microsoft 365, trpí chybou označenou jako CW1226324, která umožňuje skenovat a shrnovat e-maily označené jako důvěrné v aplikaci Outlook. Tato chyba obchází ochranné mechanismy určené k blokování automatizovaných nástrojů a postihuje složky Odeslané a Koncepty. Microsoft potvrzuje problém a zavádí opravu pro postižené účty, avšak bez specifikace, kdy bude dostupná pro všechny uživatele.

## Klíčové body
- **Chyba CW1226324**: Copilot Chat v Microsoft 365 čte důvěrné e-maily v Outlooku navzdory označení, které má bránit automatizovanému zpracování.
- **Postižené složky**: Primárně Odeslané (Sent) a Koncepty (Drafts), kde se často ukládají citlivá data jako smlouvy nebo lékařské informace.
- **Oprava v procesu**: Microsoft ji postupně nasazuje, ale rozsah dopadu se může měnit a plný report je viditelný jen pro administrátory Microsoft 365.
- **Žádné údaje o počtu uživatelů**: Firma neuvádí, kolik účtů je ovlivněno, což zvyšuje nejistotu.
- **Zdroj**: Zpráva pochází přímo od Microsoftu, shrnuto na PCWorld a BleepingComputer.

## Podrobnosti
Chyba CW1226324 odhaluje fundamentální slabinu v integraci AI do produktivních nástrojů jako je Microsoft 365. Copilot, což je AI asistent založený na velkých jazykových modelech (LLM), slouží k automatizaci úkolů jako shrnutí e-mailů, generování odpovědí nebo analýza obsahu. V tomto případě však ignoruje označení „důvěrné“ (confidential), které je v Outlooku navrženo specificky pro blokování skenování automatizovanými systémy, včetně AI. To znamená, že Copilot může načíst obsah e-mailů obsahujících obchodní smlouvy, právní korespondenci, údaje z policejních vyšetřování nebo osobní zdravotní informace.

Problém se projevuje v Copilot Chat, což je rozhraní pro konverzaci s AI přímo v Microsoft 365 aplikacích. Uživatelé, kteří aktivují funkci shrnutí e-mailů, riskují nechtěné zpracování citlivých dat. Tyto data mohou být následně zpracována modelem, potenciálně uložena v logách nebo – v nejhorším případě – použita pro trénink modelů, jak je běžné u cloudových AI služeb. Microsoft sice tvrdí, že data nejsou automaticky posílána do tréninkových sad, ale absence transparentnosti v bug reportu (dostupném jen pro adminy) brání plnému posouzení rizik.

Oprava je nasazována postupně, ale bez časového rámce. To je typické pro enterprise prostředí, kde aktualizace probíhají v waves podle tenantů. Zatímco běžní uživatelé nemohou report prohlédnout, zdroje jako BleepingComputer a PCWorld potvrzují detaily na základě uniklých informací. Tento incident navazuje na předchozí kontroverze kolem Copilotu, jako je nechtěné sdílení dat mezi uživateli nebo nesprávné shrnutí, což ukazuje na nezralost AI v citlivých prostředích.

## Proč je to důležité
Tato chyba podtrhuje systémové rizika integrace AI do firemních systémů, kde důvěrnost dat je klíčová. V širším kontextu posiluje skepsi vůči spolehlivosti LLM v produktech gigantů jako Microsoft, kde AI slibuje produktivitu, ale často selhává v bezpečnostních základů. Pro uživatele Microsoft 365 to znamená nutnost okamžitého omezení přístupu Copilotu k důvěrným složkám, zatímco firmy čekají na fix. V kyberbezpečnostním ekosystému to zvyšuje tlak na regulace jako EU AI Act, který vyžaduje transparentnost u vysokorizikových AI systémů. Pokud se rozsah dopadu rozšíří, může to vést k žalobám nebo ztrátě důvěry, což brzdí adopci AI v podnicích. Celkově to ilustruje, proč bezpečnostní objevy v AI patří mezi průlomové – odhalují chyby, které mohou mít reálné dopady na miliardy uživatelů.

---

[Číst původní článek](https://www.pcworld.com/article/3064782/copilot-bug-allows-ai-to-read-confidential-outlook-emails.html)

**Zdroj:** 📰 PCWorld
