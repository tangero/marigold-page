---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Microsoft
- OpenAI
- GitHub
- Amazon Web Services
- Google
date: '2025-11-07 06:48:00'
description: Nově odhalené škodlivé rozšíření pro VS Code a falešné balíčky v npm
  ukazují, jak útočníci zneužívají důvěru v otevřený software a nástroje pro vývojáře,
  včetně využití AI k automatizaci tvorby sofistikovaného malwaru.
importance: 3
layout: tech_news_article
original_title: Vibe-Coded Malicious VS Code Extension Found with Built-In Ransomware
  Capabilities - The Hacker News
publishedAt: '2025-11-07T06:48:00+00:00'
slug: vibe-coded-malicious-vs-code-extension-found-with-
source:
  emoji: 📰
  id: null
  name: Internet
title: AI-generované škodlivé rozšíření pro VS Code má vestavěné funkce ransomwaru
url: https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html
urlToImage: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Dcu9T1Afix71Yt-8QCNjFUC__8eCH-PwqBYQbkqtmzclCd1DmtyV89McDlT1wJxv4qRnRmxQiEFsnpzw1a0k3EMPCBIpxwJysacU-wUGg6-tCUrTKFlPVtrR3Yw4qO5Yk_trwmpT5AMqUgSkFJMEvMYJL522Wjn4FOYfFAzFaZUvZ9ufXSV82U7lUFA3/s790-rw-e365/vide-code-ransomware.jpg
urlToImageBackup: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Dcu9T1Afix71Yt-8QCNjFUC__8eCH-PwqBYQbkqtmzclCd1DmtyV89McDlT1wJxv4qRnRmxQiEFsnpzw1a0k3EMPCBIpxwJysacU-wUGg6-tCUrTKFlPVtrR3Yw4qO5Yk_trwmpT5AMqUgSkFJMEvMYJL522Wjn4FOYfFAzFaZUvZ9ufXSV82U7lUFA3/s790-rw-e365/vide-code-ransomware.jpg
---

## Souhrn
Odhalené škodlivé rozšíření pro Visual Studio Code s názvem „Vibe-Coded“ obsahuje vestavěné ransomwarové funkce a je distribuováno přes kanály, které napodobují legitimní open-source projekty. Souběžně byly identifikovány falešné balíčky v registru npm, které cílí na vývojáře a CI/CD prostředí. Incident ukazuje, jak útočníci využívají AI k rychlejší tvorbě a maskování malwaru a jak systematicky zneužívají důvěru v open-source dodavatelský řetězec.

## Klíčové body
- Škodlivé VS Code rozšíření s funkcemi pro šifrování souborů a vzdálené ovládání.
- Zneužití falešných balíčků v npm k implantaci backdoorů a exfiltraci dat.
- Pravděpodobné zapojení AI při generování kódu malwaru a jeho obfuskaci.
- Cílení na vývojáře, build servery a kontejnery v rámci dodavatelského řetězce software.
- Nutnost zpřísnit ověřování rozšíření, balíčků a bezpečnostních politik v CI/CD a IDE.

## Podrobnosti
Útočníci vytvořili rozšíření pro Visual Studio Code, které se tvářilo jako užitečný nástroj pro vývojáře, ale ve skutečnosti obsahovalo ransomware-like modul schopný šifrovat lokální soubory, upravovat projekty a potenciálně zasáhnout i připojené síťové disky. Visual Studio Code je široce používané integrované vývojové prostředí od Microsoftu, a jeho marketplace je dlouhodobě slabým místem, protože řada rozšíření prochází jen omezeným ověřením. Zneužití této distribuce znamená, že kompromitovaný může být přímo nástroj, ve kterém vývojáři pracují s produkčním kódem, přístupovými tokeny a konfiguracemi.

Paralelně byly identifikovány falešné balíčky v registru npm, které napodobují názvy populárních knihoven. Tyto balíčky jsou navrženy tak, aby po instalaci stahovaly a spouštěly škodlivý kód, otevíraly zadní vrátka (backdoor) nebo sbíraly přístupové údaje k repozitářům, cloudovým účtům a CI/CD systémům. npm je dominantní balíčkovací ekosystém pro JavaScript a Node.js, a jeho kompromitace má přímý dopad na webové aplikace, microservices a kontejnery.

Analýza kódu naznačuje využití AI pro generování části malwaru, obfuskaci řetězců, variace komunikace s řídicími servery a tvorbu věrohodné dokumentace. To snižuje náklady pro útočníky a zvyšuje obtížnost detekce: kód vypadá konzistentně, je formálně „čistý“, ale obsahuje záměrně ukryté škodlivé funkce. Riziko je významné pro týmy, které automaticky důvěřují marketplace rozšířením a npm balíčkům, nemají striktní povolovací seznamy (allowlisty) a neprovádějí kontrolu integrity.

## Proč je to důležité
Incident potvrzuje, že hlavním cílem útočníků jsou dnes vývojové nástroje, balíčkové registry a kontejnery – tedy samotná infrastruktura, na které stojí moderní software. Kompromitace VS Code rozšíření nebo npm balíčků umožňuje zasáhnout mnoho projektů současně, od interních nástrojů po produkční služby.

Pro organizace to znamená nutnost:
- zavést interní repozitáře schválených rozšíření a balíčků a blokovat přímou instalaci z neověřených zdrojů,
- auditovat CI/CD pipeline, build kontejnery a přístupové tokeny na přítomnost škodlivých komponent,
- používat nástroje pro analýzu dodavatelského řetězce software (SCA, SBOM, kontrola podpisů),
- přistupovat k AI-generovanému kódu i k „novým užitečným rozšířením“ s nedůvěrou a vyžadovat revizi kódu.

Trend využívání AI k automatizaci vývoje malwaru a zneužívání otevřených ekosystémů ukazuje, že obrana musí být přísnější, systematická a méně založená na implicitní důvěře v „populární“ či „dobře vypadající“ projekty.

---

[Číst původní článek](https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html)

**Zdroj:** 📰 Internet
