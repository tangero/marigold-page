---
category: kybernetická bezpečn
companies:
- QNAP
- Microsoft
date: '2025-10-27 16:55:02'
description: QNAP upozorňuje zákazníky na kritickou zranitelnost v ASP.NET Core, která
  postihuje také NetBak PC Agent - nástroj pro zálohování dat z Windows na síťová
  úložiště NAS.
importance: 3
layout: tech_news_article
original_title: QNAP warns of critical ASP.NET flaw in its Windows backup software
  - BleepingComputer
publishedAt: '2025-10-27T16:55:02+00:00'
slug: qnap-warns-of-critical-aspnet-flaw-in-its-windows-
source:
  emoji: 📰
  id: null
  name: BleepingComputer
title: QNAP varuje před kritickou zranitelností ASP.NET ve svém zálohovacím softwaru
url: https://www.bleepingcomputer.com/news/security/qnap-warns-its-windows-backup-software-is-also-affected-by-critical-aspnet-flaw/
urlToImage: https://www.bleepstatic.com/content/hl-images/2025/01/23/QNAP.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2025/01/23/QNAP.jpg
---

## Souhrn

Tajwanský výrobce síťových úložišť QNAP varuje uživatele před kritickou bezpečnostní zranitelností v ASP.NET Core, která ovlivňuje také jejich zálohovací software NetBak PC Agent pro Windows. Chyba umožňuje útočníkům s nízkými oprávněními odcizit přihlašovací údaje jiných uživatelů nebo obejít bezpečnostní kontroly prostřednictvím HTTP request smuggling.

## Klíčové body

- Zranitelnost CVE-2025-55315 postihuje webový server Kestrel v ASP.NET Core a získala nejvyšší hodnocení závažnosti v historii ASP.NET Core
- NetBak PC Agent při instalaci používá komponenty Microsoft ASP.NET Core, což činí systémy s tímto softwarem zranitelnými
- Útočníci mohou zneužít chybu k přihlášení jako jiný uživatel, obejití CSRF ochrany nebo provádění injection útoků
- QNAP doporučuje buď přeinstalovat NetBak PC Agent, nebo ručně aktualizovat ASP.NET Core na nejnovější verzi
- Microsoft záplatu vydal již před dvěma týdny

## Podrobnosti

Zranitelnost CVE-2025-55315 představuje bezpečnostní bypass v Kestrel webovém serveru, který je součástí ASP.NET Core frameworku od Microsoftu. Problém spočívá v možnosti provádět HTTP request smuggling - techniku, při které útočník manipuluje s HTTP požadavky tak, aby obešel bezpečnostní kontroly na front-endu aplikace.

NetBak PC Agent je zálohovací utilita pro Windows, která umožňuje uživatelům zálohovat data z počítačů přímo na síťová úložiště NAS od společnosti QNAP. Při instalaci tento software automaticky nainstaluje potřebné komponenty Microsoft ASP.NET Core. Pokud uživatelé od té doby neaktualizovali svůj systém Windows, mohou mít nainstalovanou zranitelnou verzi.

Barry Dorrans, manažer pro bezpečnost .NET u Microsoftu, označil tuto zranitelnost za nejzávažnější v historii ASP.NET Core. Konkrétní dopady úspěšného útoku závisí na cílové aplikaci - útočník s autentizací může odeslat speciálně upravené HTTP požadavky, které mu umožní získat neoprávněný přístup k citlivým datům, modifikovat soubory na serveru nebo způsobit omezenou nedostupnost služby.

Uživatelé mají dvě možnosti, jak systémy zabezpečit. První variantou je kompletní přeinstalace NetBak PC Agent, která automaticky nahraje nejnovější verzi ASP.NET Core runtime komponent. Druhou možností je ruční aktualizace ASP.NET Core stažením a instalací nejnovějšího ASP.NET Core Runtime (Hosting Bundle) ze stránky pro stahování .NET 8.0.

## Proč je to důležité

Tato situace ilustruje rostoucí problém v ekosystému moderního softwaru - závislosti na komponentách třetích stran. I když QNAP není přímo zodpovědný za zranitelnost v ASP.NET Core, jeho zákazníci jsou ohroženi kvůli použití této technologie. Jde o připomínku, že bezpečnost systému závisí nejen na hlavní aplikaci, ale i na všech jejích závislostech. Pro uživatele síťových úložišť QNAP je aktualizace kritická, protože tato zařízení často obsahují citlivá firemní i osobní data a bývají vystavena útokům.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/security/qnap-warns-its-windows-backup-software-is-also-affected-by-critical-aspnet-flaw/)

**Zdroj:** 📰 BleepingComputer
