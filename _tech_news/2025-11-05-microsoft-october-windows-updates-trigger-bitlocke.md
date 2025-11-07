---
author: Marisa Aigen
category: bezpečnostní aktuali
companies:
- Microsoft
date: '2025-11-05 08:56:22'
description: Microsoft varuje, že říjnové bezpečnostní aktualizace Windows způsobují
  na některých systémech spuštění režimu BitLocker recovery, který vyžaduje zadání
  obnovovacího klíče.
importance: 3
layout: tech_news_article
original_title: 'Microsoft: October Windows updates trigger BitLocker recovery - BleepingComputer'
publishedAt: '2025-11-05T08:56:22+00:00'
slug: microsoft-october-windows-updates-trigger-bitlocke
source:
  emoji: 📰
  id: null
  name: BleepingComputer
title: Říjnové aktualizace Windows spouštějí BitLocker recovery
url: https://www.bleepingcomputer.com/news/microsoft/microsoft-october-windows-updates-trigger-bitlocker-recovery/
urlToImage: https://www.bleepstatic.com/content/hl-images/2024/12/16/Windows.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2024/12/16/Windows.jpg
---

## Souhrn

Microsoft potvrdil, že říjnové bezpečnostní aktualizace Windows z roku 2025 způsobují na některých počítačích nečekaný přechod do režimu BitLocker recovery. Problém se týká především zařízení s procesory Intel podporujícími technologii Modern Standby, přičemž uživatelé musí po instalaci aktualizací jednorázově zadat obnovovací klíč.

## Klíčové body

- Aktualizace vydané 14. října 2025 a později způsobují problémy při restartu systému
- Postižena jsou především zařízení Intel s podporou Modern Standby (dříve Connected Standby)
- Problém se týká Windows 11 24H2 a 25H2 a Windows 10 22H2
- Po jednorázovém zadání obnovovacího klíče systém funguje normálně
- Microsoft nabízí řešení prostřednictvím Known Issue Rollback (KIR) pro IT administrátory

## Podrobnosti

BitLocker je bezpečnostní funkce Windows, která šifruje úložné disky a chrání data před krádeží. Systém Windows obvykle přechází do režimu BitLocker recovery po hardwarových změnách nebo aktualizacích Trusted Platform Module (TPM), aby uživatel mohl znovu získat přístup k chráněným diskům.

Podle servisního upozornění, které získal server BleepingComputer, se chyba projevuje především na zařízeních Intel s podporou technologie Modern Standby. Tato funkce umožňuje počítači zůstat připojený k síti i v režimu nízké spotřeby energie, podobně jako u mobilních zařízení.

Microsoft uvádí, že po instalaci aktualizací vydaných 14. října 2025 nebo později mohou některá zařízení narazit na problémy během restartu nebo spouštění systému. Postižené počítače se spustí do obrazovky BitLocker recovery, kde uživatel musí zadat obnovovací klíč. Po zadání klíče a restartu zařízení již systém funguje normálně bez dalších výzev k zadání BitLocker klíče.

IT administrátoři mohou problém zmírnit pomocí skupinové politiky distribuované prostřednictvím mechanismu Known Issue Rollback. Pro získání podrobností je však nutné kontaktovat podporu Microsoft Support for business.

## Proč je to důležité

Jde o opakující se problém, který Microsoft řeší již několikrát ročně. Společnost vydala nouzové aktualizace v květnu 2025 k řešení podobného problému s květnovými aktualizacemi Windows 10. V srpnu 2024 musel Microsoft řešit další známý problém způsobující výzvy BitLocker recovery po instalaci červencových bezpečnostních aktualizací.

Pro běžné uživatele to znamená potenciální komplikace při přístupu k počítači, zejména pokud nemají obnovovací klíč BitLocker snadno dostupný. Klíč je obvykle uložen v účtu Microsoft nebo vytištěn při první aktivaci šifrování. Opakování tohoto problému naznačuje systémové potíže s testováním aktualizací před jejich vydáním, což může vést k prostojům v podnikových prostředích a frustraci koncových uživatelů.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/microsoft/microsoft-october-windows-updates-trigger-bitlocker-recovery/)

**Zdroj:** 📰 BleepingComputer
