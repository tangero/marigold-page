---
author: Marisa Aigen
category: webové technologie
date: '2025-11-01 14:40:00'
description: Open-source vývojář Joel Severin úspěšně portoval linuxové jádro do WebAssembly
  a zprovoznil ho v běžných webových prohlížečích, včetně funkčního shellu.
importance: 3
layout: tech_news_article
original_title: Linux Kernel Ported To WebAssembly - Demo Lets You Run It In Your
  Web Browser - Phoronix
people:
- Joel Severin
publishedAt: '2025-11-01T14:40:00+00:00'
slug: linux-kernel-ported-to-webassembly-demo-lets-you-r
source:
  emoji: 📰
  id: null
  name: Phoronix
title: Linuxové jádro portováno do WebAssembly - demo běží přímo v prohlížeči
url: https://www.phoronix.com/news/Linux-Kernel-WebAssembly
urlToImage: https://www.phoronix.net/image.php?id=2025&image=linux_wasm_2
urlToImageBackup: https://www.phoronix.net/image.php?id=2025&image=linux_wasm_2
---

## Souhrn

Vývojář Joel Severin představil funkční port linuxového jádra do WebAssembly, který umožňuje spustit Linux přímo ve webovém prohlížeči bez nutnosti instalace či virtualizace. Jde o technologickou ukázku, která demonstruje možnosti platformy WebAssembly, byť s výraznými omezeními a problémy se stabilitou.

## Klíčové body

- Linuxové jádro bylo úspěšně portováno do WebAssembly a běží v prohlížečích podporujících WASM
- Demo umožňuje spouštět základní programy z příkazové řádky přímo v prohlížeči
- Implementace trpí problémy se stabilitou - při testování v Google Chrome docházelo k častým pádům
- Projekt vyžaduje upravené verze linuxového jádra, LLVM, Musl libc, initramfs a BusyBox
- Severin upozorňuje, že pro plnohodnotné nasazení by byly nutné zásadní změny jak v Linuxu, tak v ekosystému WebAssembly

## Podrobnosti

WebAssembly (WASM) je binární instrukční formát navržený pro běh v moderních webových prohlížečích s téměř nativním výkonem. Tento projekt představuje neobvyklé využití této technologie - místo běžných webových aplikací v něm běží celé operační systémové jádro.

Severin zdůrazňuje, že jde primárně o technologickou demonstraci možností, nikoli o produkčně použitelné řešení. Současná implementace naráží na řadu omezení vyplývajících z architektury WebAssembly i linuxového jádra. Autor upozorňuje, že pro hladký běh by bylo nutné provést fundamentální změny na obou stranách, což by vyžadovalo závazek jak od vývojářů Linuxu, tak od komunity kolem WebAssembly.

Při testování se ukázalo, že systém sice dokáže spustit základní programy z shellu, ale stabilita je problematická. Redaktor Phoronixu Michael Larabel reportoval časté pády při testování v prohlížeči Google Chrome. Projekt zahrnuje nejen upravené linuxové jádro, ale i modifikované verze kompilátoru LLVM, knihovny Musl libc, initramfs a sady nástrojů BusyBox.

Zájemci si mohou demo vyzkoušet přímo přes GitHub Pages, kompletní zdrojové kódy včetně všech patchů jsou dostupné v GitHub repozitáři projektu. Diskuze o projektu probíhá také na linuxovém mailingovém listu LKML.

## Proč je to důležité

Projekt demonstruje rostoucí možnosti WebAssembly jako platformy pro běh komplexního systémového softwaru, nejen webových aplikací. Ačkoli praktické využití takového portu je v současnosti omezené, ukazuje to směr, kterým by se mohla ubírat virtualizace a cloudové technologie - možnost spustit kompletní operační systém v izolovaném prostředí prohlížeče bez nutnosti instalace či složité konfigurace. Pro běžné uživatele to zatím nemá praktický dopad, ale pro vývojáře a výzkumníky jde o zajímavý proof-of-concept ukazující limity současných webových technologií.

---

[Číst původní článek](https://www.phoronix.com/news/Linux-Kernel-WebAssembly)

**Zdroj:** 📰 Phoronix
