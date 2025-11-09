---
author: Marisa Aigen
category: kybernetika
date: '2025-11-07 06:48:00'
description: Útočníci zneužili důvěru v otevřený software a využili AI k tvorbě škodlivého
  rozšíření pro VS Code a falešných balíčků v repozitáři npm, které mohou vést k ransomware
  útokům a kompromitaci vývojářských prostředí.
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
title: Zákeřné VS Code rozšíření generované pomocí AI obsahovalo vestavěné ransomware
  funkce
url: https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html
urlToImage: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Dcu9T1Afix71Yt-8QCNjFUC__8eCH-PwqBYQbkqtmzclCd1DmtyV89McDlT1wJxv4qRnRmxQiEFsnpzw1a0k3EMPCBIpxwJysacU-wUGg6-tCUrTKFlPVtrR3Yw4qO5Yk_trwmpT5AMqUgSkFJMEvMYJL522Wjn4FOYfFAzFaZUvZ9ufXSV82U7lUFA3/s790-rw-e365/vide-code-ransomware.jpg
urlToImageBackup: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Dcu9T1Afix71Yt-8QCNjFUC__8eCH-PwqBYQbkqtmzclCd1DmtyV89McDlT1wJxv4qRnRmxQiEFsnpzw1a0k3EMPCBIpxwJysacU-wUGg6-tCUrTKFlPVtrR3Yw4qO5Yk_trwmpT5AMqUgSkFJMEvMYJL522Wjn4FOYfFAzFaZUvZ9ufXSV82U7lUFA3/s790-rw-e365/vide-code-ransomware.jpg
---

## Souhrn
Škodlivé rozšíření pro Visual Studio Code, částečně generované pomocí AI, bylo odhaleno s vestavěnými schopnostmi ransomware útoku a s napojením na falešné balíčky v repozitáři npm. Incident ukazuje, jak útočníci zneužívají důvěru v otevřený ekosystém vývojářských nástrojů, automatizované generování kódu a nedostatečnou kontrolu rozšíření a závislostí.

## Klíčové body
- Škodlivé VS Code rozšíření obsahovalo funkce pro šifrování souborů a potenciální vyděračské útoky.
- Útočníci využili AI k generování kódu, aby urychlili vývoj a zamaskovali škodlivé funkce.
- Falešné npm balíčky imitovaly legitimní knihovny a mohly být vtaženy do projektů přes běžné závislosti.
- Cílem je kompromitace vývojářských stanic a dodavatelského řetězce software (supply chain).
- Případ potvrzuje, že důvěra v otevřený software bez ověření je zásadní riziko pro firmy i jednotlivé vývojáře.

## Podrobnosti
Útočníci publikovali rozšíření pro Visual Studio Code, které se tvářilo jako běžný nástroj pro zlepšení produktivity vývojářů, ale ve skutečnosti obsahovalo skrytý kód schopný provádět ransomware operace. Konkrétně šlo o funkce, které umožňovaly přístup k souborovému systému, enumeraci souborů a jejich šifrování s následným znepřístupněním. Rozšíření bylo navrženo tak, aby působilo legitimně a technicky konzistentně s ekosystémem VS Code, což zvyšuje pravděpodobnost, že si ho vývojáři nainstalují bez hlubší kontroly.

Část škodlivého kódu byla zjevně generována pomocí AI nástrojů, což je pro útočníky výhodné: mohou rychle vytvářet varianty, měnit signatury a snáze obcházet jednoduché detekční mechanismy. Současně byly publikovány falešné balíčky v npm, které napodobovaly názvy nebo strukturu populárních knihoven. Npm je veřejný repozitář JavaScriptových a TypeScriptových balíčků, běžně používaný při vývoji webových aplikací a backendových služeb. Pokud vývojář nepozorně přidá podobně pojmenovaný balíček nebo přebere konfiguraci z neověřeného zdroje, může do projektu zavléct škodlivý kód.

Nebezpečí je dvojí: útočník může přímo zašifrovat data na vývojářském stroji, nebo zneužít přístup k repozitářům, CI/CD systémům a produkčním tajným klíčům. Takový útok se pak šíří v rámci dodavatelského řetězce, kde škodlivý kód končí v knihovnách, interních nástrojích nebo přímo v produktech nasazených u zákazníků. Incident zapadá do trendu cílících na vývojářské nástroje (VS Code, IDE pluginy, npm, PyPI, Docker Hub), protože představují efektivní vektor k útokům na větší organizace.

## Proč je to důležité
Tento případ potvrzuje, že vývojářské prostředí je kritická součást bezpečnostního perimetru a již dávno není „interní“ a bez rizika. Kombinace AI generovaného kódu, snadné distribuce rozšíření a otevřených balíčkovacích ekosystémů výrazně snižuje bariéru pro tvorbu sofistikovaného malware. Pro firmy to znamená nutnost zavést přísnější politiku pro instalaci VS Code rozšíření, validaci npm balíčků, používání interních zrcadel repozitářů, automatizované skenování závislostí a monitoring anomálního chování v build a runtime prostředí.

Pro bezpečnostní komunitu je to další signál, že supply chain útoky zůstávají jedním z nejefektivnějších vektorů. Pouhé spoléhání se na reputaci marketplace nebo otevřených repozitářů je nedostatečné; je nutné kombinovat manuální kontrolu, nástroje pro analýzu kódu, omezení práv rozšíření a důsledné oddělení vývojových, testovacích a produkčních prostředí.

---

[Číst původní článek](https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html)

**Zdroj:** 📰 Internet
