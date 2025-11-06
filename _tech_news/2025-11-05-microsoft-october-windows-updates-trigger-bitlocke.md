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

Microsoft potvrdil, že říjnové bezpečnostní aktualizace Windows z roku 2025 způsobují na některých počítačích nečekaný přechod do režimu BitLocker recovery při restartu systému. Problém se týká především zařízení s procesory Intel podporujícími technologii Modern Standby, která umožňuje udržovat síťové připojení i v režimu nízké spotřeby.

## Klíčové body

- Aktualizace vydané 14. října 2025 a později způsobují spuštění BitLocker recovery obrazovky při restartu
- Postižena jsou zařízení s procesory Intel podporujícími Modern Standby (dříve Connected Standby)
- Problém se týká Windows 11 24H2 a 25H2 i Windows 10 22H2
- Uživatelé musí jednorázově zadat obnovovací klíč BitLocker, poté systém funguje normálně
- Microsoft nabízí řešení prostřednictvím Known Issue Rollback (KIR) pro firemní zákazníky

## Podrobnosti

BitLocker je bezpečnostní funkce Windows, která šifruje úložné disky a chrání data před kráží. Systém Windows obvykle přechází do režimu BitLocker recovery po hardwarových změnách nebo aktualizacích Trusted Platform Module (TPM), aby znovu získal přístup k chráněným diskům.

Podle servisního upozornění, které získal server BleepingComputer, Microsoft uvedl, že chyba primárně postihuje zařízení Intel s podporou Modern Standby. Tato technologie umožňuje počítači zůstat připojený k síti i v režimu nízké spotřeby energie, podobně jako u mobilních zařízení.

Po instalaci aktualizací vydaných 14. října 2025 nebo později se některá zařízení při restartu nebo spuštění setkávají s problémy. Postižené počítače se spustí do obrazovky BitLocker recovery, která vyžaduje zadání obnovovacího klíče. Po jeho zadání a restartu zařízení funguje normálně bez dalších výzev BitLocker.

Pro firemní prostředí Microsoft nabízí zmírnění problému pomocí skupinové politiky distribuované přes Known Issue Rollback (KIR). Postižení zákazníci však musí kontaktovat podporu Microsoft Support for Business pro získání podrobností.

## Proč je to důležité

Tento incident není ojedinělý. Microsoft musel řešit podobný problém již v květnu 2025, kdy bezpečnostní aktualizace Windows 10 spouštěly BitLocker recovery po masivních hlášeních uživatelů. V srpnu 2024 se společnost potýkala s další známou chybou způsobující výzvy BitLocker recovery na Windows 10, 11 i Windows Server po instalaci červencových bezpečnostních aktualizací.

Opakující se problémy s BitLocker po bezpečnostních aktualizacích ukazují na systémový problém v testovacích procesech Microsoftu. Pro běžné uživatele to znamená potenciální komplikace při přístupu k počítači, zejména pokud nemají obnovovací klíč BitLocker snadno dostupný. Firemní prostředí jsou na tom lépe díky centralizované správě klíčů, ale i tak to představuje administrativní zátěž a možné výpadky produktivity.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/microsoft/microsoft-october-windows-updates-trigger-bitlocker-recovery/)

**Zdroj:** 📰 BleepingComputer
