---
author: Marisa Aigen
category: kybernetika
companies:
- Microsoft
date: '2025-11-07 06:48:00'
description: Odhalení škodlivého rozšíření pro VS Code a falešných balíčků v registru
  npm ukazuje, jak útočníci zneužívají důvěru v open-source ekosystém, automatizované
  nástroje a AI k šíření ransomwaru a krádeži dat.
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
title: Zákeřné VS Code rozšíření s AI generovaným kódem obsahovalo vestavěné ransomwarové
  funkce
url: https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html
urlToImage: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Dcu9T1Afix71Yt-8QCNjFUC__8eCH-PwqBYQbkqtmzclCd1DmtyV89McDlT1wJxv4qRnRmxQiEFsnpzw1a0k3EMPCBIpxwJysacU-wUGg6-tCUrTKFlPVtrR3Yw4qO5Yk_trwmpT5AMqUgSkFJMEvMYJL522Wjn4FOYfFAzFaZUvZ9ufXSV82U7lUFA3/s790-rw-e365/vide-code-ransomware.jpg
urlToImageBackup: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Dcu9T1Afix71Yt-8QCNjFUC__8eCH-PwqBYQbkqtmzclCd1DmtyV89McDlT1wJxv4qRnRmxQiEFsnpzw1a0k3EMPCBIpxwJysacU-wUGg6-tCUrTKFlPVtrR3Yw4qO5Yk_trwmpT5AMqUgSkFJMEvMYJL522Wjn4FOYfFAzFaZUvZ9ufXSV82U7lUFA3/s790-rw-e365/vide-code-ransomware.jpg
---

## Souhrn
Nově odhalené škodlivé rozšíření pro Visual Studio Code, obsahující tzv. "vibe-coded" (AI generovaný nebo maskovaný) kód, ukazuje, že útočníci integrují ransomwarové funkce přímo do vývojářských nástrojů. Spolu s falešnými balíčky v registru npm to potvrzuje trend zneužívání open-source ekosystému a důvěry vývojářů pomocí automatizace a AI.

## Klíčové body
- Škodlivé VS Code rozšíření obsahovalo skryté ransomwarové funkce schopné šifrovat soubory a manipulovat s lokálním prostředím vývojáře.
- Útočníci využili falešné npm balíčky napodobující legitimní projekty ke krádeži přístupových údajů a exfiltraci dat.
- Součástí útoku byla technika AI-asistovaného kódu ("vibe-coded"), která ztěžuje manuální i automatizovanou analýzu.
- Cílem jsou vývojáři a CI/CD prostředí, kde kompromitace nástroje snadno vede k napadení produkčních systémů.
- Incident potvrzuje, že důvěra v open-source registry a marketplace bez důsledného ověřování je zásadní slabina dodavatelského řetězce.

## Podrobnosti
Škodlivé rozšíření pro VS Code se vydávalo za užitečný nástroj pro vývojáře a po instalaci získávalo přístup k lokálním souborům, klíčům a konfiguracím. VS Code rozšíření jsou běžně používána k rozšíření funkcí editoru (lintování, formátování kódu, integrace s Git, ladění), a proto jim mnoho vývojářů implicitně důvěřuje. V tomto případě útočníci tuto důvěru využili k nasazení kódu, který dokázal mapovat souborový systém, odesílat data na vzdálený server a spouštět šifrovací logiku podobnou ransomware.

Současně byly identifikovány falešné npm balíčky, které napodobovaly názvy populárních knihoven. npm slouží jako centrální registr balíčků pro ekosystém Node.js a JavaScript, využívaný v serverových aplikacích, front-end projektech i nástrojích pro automatizaci buildů. Útočníci sázeli na překlepy v názvech balíčků (typosquatting), nedostatečnou kontrolu závislostí a automatizované build procesy. Po instalaci tyto balíčky spouštěly skripty pro exfiltraci tokenů, SSH klíčů, proměnných prostředí a přístupů k repozitářům či cloudové infrastruktuře.

Termín "vibe-coded" odkazuje na kód, který je částečně generovaný pomocí AI nebo stylizovaný tak, aby působil jako legální a organicky napsaný, přičemž skrývá škodlivé části v obfuskovaných funkcích, netradičních strukturách a nejasné logice. To komplikuje statickou analýzu i detekci pomocí signatur. Z hlediska praxe to znamená, že standardní kontrola zdrojových kódů, letmý audit rozšíření nebo spoleh na reputaci platformy přestává být dostačující.

Pro firmy, které používají VS Code a npm v CI/CD, to představuje přímé riziko kompromitace build pipeline. Jediné nedůvěryhodné rozšíření nebo balíček může vést k vložení zadních vrátek do produkčního kódu, úniku tajných klíčů, následnému ransomwarovému útoku či zneužití cloudových zdrojů.

## Proč je to důležité
Tento případ je dalším důkazem, že útoky na dodavatelský řetězec se přesouvají přímo do nástrojů vývojářů. Útočníci si uvědomují, že kompromitace vývojového prostředí je efektivní cesta k přístupu do produkčních systémů a infrastrukturních tajemství. V kombinaci s využitím AI k generování „přirozeně“ vypadajícího kódu a s masovým zneužíváním open-source registrů se zvyšuje tlak na:

- Zavedení přísnějších interních pravidel pro instalaci VS Code rozšíření a npm balíčků (whitelist, interní mirrory, povinný audit).
- Používání software bill of materials (SBOM) a nástrojů pro skenování závislostí v reálném čase.
- Kontinuální monitoring chování rozšíření a balíčků (nejen statická analýza kódu, ale i sledování síťové komunikace a přístupu k souborům).
- Vzdělávání vývojářů, že marketplace a registry nejsou automaticky důvěryhodné a že každá nová závislost je potenciální vektor útoku.

Pro celý technologický ekosystém to znamená nutnost posunout bezpečnost z úrovně aplikace na úroveň nástrojů, závislostí a automatizovaných procesů. AI již není pouze nástroj pro obranu, ale i prostředek útočníků ke generování sofistikovaného, snadněji maskovaného malware.

---

[Číst původní článek](https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html)

**Zdroj:** 📰 Internet
