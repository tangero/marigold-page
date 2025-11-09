---
author: Marisa Aigen
category: kybernetika
companies:
- Microsoft
- OpenAI
- Google
- Github
- Amazon
date: '2025-11-07 06:48:00'
description: Útočníci využili důvěry v open-source ekosystém a Visual Studio Code
  rozšíření k distribuci škodlivého kódu s funkcemi ransomwaru, přičemž část kódu
  byla generována pomocí AI.
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
title: Zneužití VS Code rozšíření a falešných npm balíčků k šíření AI-generovaného
  ransomwaru
url: https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html
urlToImage: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Dcu9T1Afix71Yt-8QCNjFUC__8eCH-PwqBYQbkqtmzclCd1DmtyV89McDlT1wJxv4qRnRmxQiEFsnpzw1a0k3EMPCBIpxwJysacU-wUGg6-tCUrTKFlPVtrR3Yw4qO5Yk_trwmpT5AMqUgSkFJMEvMYJL522Wjn4FOYfFAzFaZUvZ9ufXSV82U7lUFA3/s790-rw-e365/vide-code-ransomware.jpg
urlToImageBackup: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Dcu9T1Afix71Yt-8QCNjFUC__8eCH-PwqBYQbkqtmzclCd1DmtyV89McDlT1wJxv4qRnRmxQiEFsnpzw1a0k3EMPCBIpxwJysacU-wUGg6-tCUrTKFlPVtrR3Yw4qO5Yk_trwmpT5AMqUgSkFJMEvMYJL522Wjn4FOYfFAzFaZUvZ9ufXSV82U7lUFA3/s790-rw-e365/vide-code-ransomware.jpg
---

## Souhrn
Objevené škodlivé rozšíření pro Visual Studio Code a falešné balíčky v repozitáři npm ukazují, jak snadno mohou útočníci zneužít důvěru vývojářů v open-source nástroje. Kód obsahoval zabudované schopnosti ransomwaru a některé části byly generovány pomocí AI, což dále komplikuje detekci a analýzu hrozeb.

## Klíčové body
- Škodlivé VS Code rozšíření obsahovalo funkce pro šifrování souborů a potenciální vyděračské scénáře.
- Útočníci publikovali falešné npm balíčky napodobující legitimní knihovny, aby zasáhli vývojářské prostředí.
- Část škodlivého kódu byla generována pomocí AI, což zvyšuje variabilitu a snižuje detekovatelnost.
- Incident potvrzuje, že samotná důvěra v open-source ekosystém bez ověřování původu a integrity balíčků je nedostatečná.
- Firmy musí zavést přísnější kontroly zásobníku závislostí, především v CI/CD a kontejnerech.

## Podrobnosti
Zachycené škodlivé rozšíření pro Visual Studio Code, dnes standardní nástroj pro vývojáře napříč jazyky a frameworky, bylo navrženo tak, aby po instalaci získalo přístup k lokálním souborům a následně mohlo spouštět kód se schopností jejich šifrování. Tyto funkce odpovídají prvkům ransomwaru: útočník může po aktivaci zašifrovat projekty, konfigurační soubory, klíče nebo části interního kódu a následně požadovat výkupné. Rozšíření se maskovalo jako nástroj usnadňující práci s kódem, případně jako užitečná pomůcka pro zvýšení produktivity, což je typický způsob, jak získat důvěru vývojářů.

Současně byly odhaleny falešné balíčky v ekosystému npm, které napodobovaly názvy populárních knihoven. npm slouží jako hlavní správce balíčků pro JavaScript a Node.js a je široce využíván v moderních webových a serverových aplikacích. Útočníci sázejí na překlepy, nepozornost nebo automatizované skripty v CI/CD pipeline, které balíčky stahují bez důkladné kontroly. V některých případech byl škodlivý kód generován pomocí AI, což umožňuje rychle vytvářet obfuskované, variabilní a méně předvídatelné škodlivé funkce, které se hůře detekují statickou analýzou.

Problém je zásadní zejména ve spojení s kontejnery a automatizovaným build procesem. Pokud CI/CD pipeline nekontroluje reputaci, podpisy a obsah balíčků či rozšíření, může být škodlivý kód zabalen přímo do kontejnerového obrazu a následně nasazen do produkce. To zvyšuje riziko laterálního pohybu, úniku klíčů, kompromitace tajných údajů i následného vydírání. Organizace by měly zavést politiky pro schvalování rozšíření, interní registry balíčků, kontrolu hashů, skenování závislostí a logování neobvyklého chování v běhovém prostředí.

## Proč je to důležité
Tento incident potvrzuje strukturální slabinu: moderní vývojářské prostředí stojí na řetězci důvěry, který není adekvátně ověřován. Kombinace open-source balíčků, rozšíření pro editor, CI/CD automatizace, kontejnerizace a nyní také AI-generovaného kódu vytváří útočníkům příležitost zasáhnout přímo dodavatelský řetězec softwaru. Pro firmy to znamená nutnost přestat spoléhat na implicitní důvěru k veřejným repozitářům a nástrojům a začít je řídit jako kritickou infrastrukturu: zavést povinné ověřování zdrojů, minimální počet důvěryhodných správců pro nové závislosti, skenování obrazu kontejnerů před nasazením a omezení instalace neschválených rozšíření. Pro jednotlivé vývojáře to je jasný signál instalovat pouze rozšíření a balíčky z ověřených zdrojů, sledovat anomálie v chování nástrojů a chápat, že útok dnes může začít přímo v jejich editoru kódu.

---

[Číst původní článek](https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html)

**Zdroj:** 📰 Internet
