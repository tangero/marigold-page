---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Microsoft
date: '2025-12-30 15:22:48'
description: Skupina HoneyMyte, známá také jako Mustang Panda, použila nový backdoor
  ToneShell k útokům na vládní entity v Asii. Tento nástroj obchází detekci Microsoft
  Defender a umožňuje trvalý přístup do systémů.
importance: 5
layout: tech_news_article
original_title: HoneyMyte (aka Mustang Panda) Deploys ToneShell Backdoor in New Attacks
publishedAt: '2025-12-30T15:22:48+00:00'
slug: honeymyte-aka-mustang-panda-deploys-toneshell-back
source:
  emoji: 📰
  id: null
  name: HackRead
title: HoneyMyte (známý také jako Mustang Panda) nasazuje backdoor ToneShell v nových
  útocích
url: https://hackread.com/honeymyte-mustang-panda-toneshell-backdoor/
urlToImage: https://hackread.com/wp-content/uploads/2025/12/honeymyte-mustang-panda-toneshell-backdoor-1024x597.jpg
urlToImageBackup: https://hackread.com/wp-content/uploads/2025/12/honeymyte-mustang-panda-toneshell-backdoor-1024x597.jpg
---

## Souhrn
Skupina HoneyMyte, identifikovaná jako varianta čínské APT skupiny Mustang Panda, nasadila nový backdoor ToneShell v nedávných kybernetických útocích. Tento nástroj slouží k nenápadnému získání přístupu do počítačových systémů a obchází ochranu Microsoft Defender. Cílem jsou především vládní instituce v asijském regionu.

## Klíčové body
- HoneyMyte (Mustang Panda) je státně podporovaná skupina zaměřená na špionáž v Asii.
- ToneShell backdoor umožňuje vzdálené spouštění příkazů, sběr dat a eskalaci privilégií.
- Útok obchází Microsoft Defender tím, že maskuje svou aktivitu jako legitimní procesy.
- Cíle: vládní entity v Asii, včetně ministerstev a diplomatických zařízení.
- Doporučení: aktualizovat antivirový software a monitorovat síťovou komunikaci.

## Podrobnosti
HoneyMyte, známá také pod názvem Mustang Panda, je pokročilá perzistentní hrozba (APT) připisovaná čínským aktérům. Tato skupina se specializuje na dlouhodobou špionáž proti vládám a organizacím v Asii, často využívá spear-phishing a zranitelné servery k počátečnímu přístupu. V nedávných kampaních nasadila backdoor ToneShell, který je napsán v jazyce Rust pro lepší odolnost proti reverznímu inženýrství a menší detekovatelnost.

ToneShell funguje jako modulární nástroj pro post-exploitační fázi. Po infikci systému se připojuje k command-and-control (C2) serveru přes protokol HTTPS, maskovaný jako běžný webový provoz. Umožňuje útočníkům spouštět shell příkazy, stahovat další moduly, exfiltrovat soubory a monitorovat klávesnici. Klíčovou vlastností je obcházení Microsoft Defender for Endpoint: backdoor injectuje svůj kód do legitimních procesů, jako je explorer.exe, a používá techniky jako process hollowing k vyhnutí se heuristické detekci.

Útoky začínají typicky e-mailem s přílohou nebo odkazem na kompromitovaný web, který vede k stažení malware. Analýzy ukazují, že Mustang Panda aktualizovala svůj toolkit po detekci předchozích nástrojů, jako byl PlugX nebo Cobalt Strike. V tomto případě ToneShell slouží k udržení přístupu i po restartu systému díky perzistenci v registru Windows. Cílené entity zahrnují vládní sítě v zemích jako Tchaj-wan, Vietnam a Indie, kde došlo k úspěšnému kompromitování serverů.

Bezpečnostní firmy jako Recorded Future a ESET potvrdily tyto aktivity na základě indikátorů kompromitace (IoC), včetně specifických C2 domén a hashů souborů. Pro obranu je nutné implementovat behaviorální analýzu, segmentaci sítě a pravidelné audity. Microsoft již vydal aktualizace pro Defender, které detekují známé varianty ToneShell.

## Proč je to důležité
Tento útok demonstruje eskalaci v APT taktikách, kde státní aktéři cíleně oslabují komerční bezpečnostní řešení jako Microsoft Defender, což ohrožuje tisíce organizací. V kontextu rostoucího geopolitického napětí v Asii zvyšuje riziko úniku citlivých dat, které mohou ovlivnit národní bezpečnost. Pro průmysl znamená nutnost investic do zero-trust architektury a AI-detekce anomaly, protože tradiční signatur-based ochrana selhává. V širším ekosystému to podtrhuje zranitelnost cloudových a hybridních prostředí vůči sofistikovaným hrozbám.

---

[Číst původní článek](https://hackread.com/honeymyte-mustang-panda-toneshell-backdoor/)

**Zdroj:** 📰 HackRead
