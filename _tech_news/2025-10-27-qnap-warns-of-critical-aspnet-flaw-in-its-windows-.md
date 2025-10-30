---
category: kybernetická bezpečn
companies:
- QNAP
- Microsoft
date: '2025-10-27 16:55:02'
description: QNAP upozorňuje zákazníky na kritickou zranitelnost v ASP.NET Core, která
  postihuje i NetBak PC Agent - nástroj pro zálohování dat z Windows počítačů na síťová
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
  pro Windows
url: https://www.bleepingcomputer.com/news/security/qnap-warns-its-windows-backup-software-is-also-affected-by-critical-aspnet-flaw/
urlToImage: https://www.bleepstatic.com/content/hl-images/2025/01/23/QNAP.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2025/01/23/QNAP.jpg
---

## Souhrn

Tajwanský výrobce síťových úložišť QNAP varuje uživatele před kritickou bezpečnostní zranitelností v ASP.NET Core, která postihuje i jeho zálohovací software NetBak PC Agent pro Windows. Chyba umožňuje útočníkům s nízkými oprávněními odcizit přihlašovací údaje jiných uživatelů nebo obejít bezpečnostní kontroly prostřednictvím HTTP request smuggling.

## Klíčové body

- Zranitelnost CVE-2025-55315 postihuje webový server Kestrel v ASP.NET Core a získala nejvyšší hodnocení závažnosti v historii ASP.NET Core
- NetBak PC Agent při instalaci využívá komponenty Microsoft ASP.NET Core, čímž se stává zranitelným
- Útočníci mohou zneužít chybu k přihlášení jako jiný uživatel, obejití CSRF ochrany nebo provádění injection útoků
- QNAP doporučuje buď přeinstalovat NetBak PC Agent, nebo ručně aktualizovat ASP.NET Core Runtime
- Microsoft zranitelnost opravil před dvěma týdny

## Podrobnosti

Zranitelnost CVE-2025-55315 představuje bezpečnostní riziko typu security bypass v webovém serveru Kestrel, který je součástí ASP.NET Core frameworku od Microsoftu. Problém spočívá v možnosti provádět HTTP request smuggling - techniku, při které útočník manipuluje s HTTP požadavky tak, aby obešel bezpečnostní kontroly na front-endu aplikace.

NetBak PC Agent je zálohovací utilita pro Windows, která umožňuje uživatelům zálohovat data ze svých počítačů přímo na síťová úložiště NAS od QNAPu. Protože tento software při instalaci automaticky nainstaluje a využívá komponenty Microsoft ASP.NET Core, jsou počítače s touto aplikací potenciálně zranitelné, pokud nebyly aktualizovány na nejnovější verzi.

Barry Dorrans, bezpečnostní manažer pro .NET u Microsoftu, vysvětlil, že dopad úspěšného útoku závisí na konkrétní ASP.NET aplikaci. Útočník s autentizací může odeslat speciálně upravené HTTP požadavky na webový server, což může vést k neoprávněnému přístupu k citlivým datům, modifikaci souborů na serveru nebo k omezeným denial-of-service podmínkám.

Uživatelé mají dvě možnosti, jak zabezpečit své systémy. První variantou je kompletní přeinstalace NetBak PC Agent, která automaticky nainstaluje nejnovější verzi ASP.NET Core runtime komponent. Druhou možností je ruční aktualizace ASP.NET Core stažením a instalací nejnovějšího ASP.NET Core Runtime (Hosting Bundle) ze stránky .NET 8.0.

## Proč je to důležité

Tato situace ilustruje rostoucí problém v ekosystému moderního softwaru - závislosti na externích komponentách mohou vytvářet bezpečnostní rizika i v produktech, které samy o sobě neobsahují chyby. QNAP není výrobcem ASP.NET Core, přesto musí reagovat na zranitelnosti v této technologii, protože ji jeho software využívá.

Pro uživatele síťových úložišť QNAP je důležité si uvědomit, že bezpečnost jejich dat nezávisí pouze na aktualizacích firmwaru NAS zařízení, ale také na aktuálnosti všech komponent zálohovacího softwaru na jejich počítačích. Nejvyšší hodnocení závažnosti, které tato zranitelnost získala, podtrhuje naléhavost okamžité aktualizace.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/security/qnap-warns-its-windows-backup-software-is-also-affected-by-critical-aspnet-flaw/)

**Zdroj:** 📰 BleepingComputer
