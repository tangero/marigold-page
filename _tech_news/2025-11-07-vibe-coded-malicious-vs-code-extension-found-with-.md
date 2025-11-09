---
author: Marisa Aigen
category: kybernetika
companies:
- Microsoft
- OpenAI
- Apple
- Google
- IBM
date: '2025-11-07 06:48:00'
description: Nedávno odhalené škodlivé rozšíření pro Visual Studio Code a falešné
  balíčky v npm ukazují, jak útočníci zneužívají důvěru v open-source ekosystém a
  automatizaci pomocí AI k distribuci ransomware a dalším útokům na vývojářská prostředí.
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
Nově odhalené škodlivé rozšíření pro Visual Studio Code a falešné balíčky v registru npm potvrzují trend, kdy útočníci zneužívají důvěru ve vývojářské nástroje a open-source komponenty k nasazení ransomware a krádeži přístupových údajů. Incident ukazuje, jak snadno lze s pomocí AI generovat sofistikovanější malware, který se maskuje jako užitečné nástroje pro vývojáře.

## Klíčové body
- Škodlivé VS Code rozšíření obsahovalo přímo vestavěné ransomware funkce a další prvky pro vzdálené ovládání systému.
- Falešné npm balíčky napodobovaly legitimní knihovny a cílily na vývojáře při automatizovaných buildech.
- Útočníci využívají AI k rychlé tvorbě kódu malware a k přizpůsobení popisů a dokumentace tak, aby působily důvěryhodně.
- Zasažen může být celý řetězec vývoje: lokální prostředí, CI/CD, kontejnery i produkční infrastruktura.
- Organizace musí zpřísnit ověřování závislostí, rozšíření a dodavatelského řetězce software.

## Podrobnosti
Zachycené škodlivé rozšíření pro Visual Studio Code bylo publikováno pod jménem, které evokovalo legitimní nástroj pro zvýšení produktivity a analýzu kódu. Po instalaci rozšíření získalo přístup k uživatelskému prostředí, souborům projektu a systémovým oprávněním, a následně dokázalo stahovat a spouštět dodatečný škodlivý kód. Součástí byla funkce, která šifrovala soubory a generovala výkupné, tedy chování typické pro ransomware. Rozšíření navíc využívalo API editoru k tomu, aby se chovalo jako běžný doplněk a nevyvolávalo podezření.

Paralelně byly identifikovány falešné balíčky v registru npm, které napodobovaly názvy populárních knihoven používaných v JavaScript a TypeScript projektech. Tyto balíčky obsahovaly škodlivé skripty spouštěné při instalaci nebo během procesu build, což je zvláště nebezpečné v CI/CD prostředí, kde instalace probíhá automaticky a často s vyššími oprávněními. Útočníci zjevně využili AI k tvorbě popisů, README a komentářů tak, aby zapadaly do ekosystému a prošly základním „očkováním“ důvěry.

V praxi to znamená, že vývojář stačí, aby omylem nainstaloval škodlivé rozšíření nebo balíček s překlepem v názvu, a útočník může získat přístup k repozitářům, tajným klíčům, přístupovým tokenům, či přímo k infrastruktuře. Pro firmy je rizikem zejména kompromitace build pipeline, která následně může šířit škodlivý kód dál v rámci dodavatelského řetězce.

## Proč je to důležité
Tento incident zapadá do širšího trendu útoků na dodavatelský řetězec software, kde je cílem vývojář a jeho nástroje, nikoli pouze koncový uživatel. Kombinace důvěry v open-source, automatizace v CI/CD a snadné generování kódu pomocí AI výrazně snižuje práh pro útočníky. Organizace by měly zavést striktnější správu závislostí (allowlist balíčků, podpisy, kontrolu integrity), omezit oprávnění v build prostředí, auditovat rozšíření v editorech, sledovat neobvyklé síťové aktivity a pravidelně školit vývojáře v oblasti supply chain hrozeb. Bez těchto opatření se z vývojářského prostředí stává přirozený vstupní bod pro ransomware kampaně a cílené útoky na kritickou infrastrukturu.

---

[Číst původní článek](https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html)

**Zdroj:** 📰 Internet
