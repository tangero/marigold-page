---
author: Marisa Aigen
category: windows aktualizace
companies:
- Microsoft
date: '2025-11-03 10:12:47'
description: Po instalaci říjnové volitelné aktualizace Windows 11 se Správce úloh
  nedá řádně ukončit a běží na pozadí v desítkách instancí, což způsobuje problémy
  s výkonem systému.
importance: 3
layout: tech_news_article
original_title: 'Microsoft: Windows Task Manager won’t quit after KB5067036 update
  - BleepingComputer'
publishedAt: '2025-11-03T10:12:47+00:00'
slug: microsoft-windows-task-manager-wont-quit-after-kb5
source:
  emoji: 📰
  id: null
  name: BleepingComputer
title: 'Microsoft potvrdil chybu: Správce úloh ve Windows 11 se po aktualizaci KB5067036
  nedá ukončit'
url: https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-task-manager-wont-quit-after-kb5067036-update/
urlToImage: https://www.bleepstatic.com/content/hl-images/2025/09/22/Windows-11.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2025/09/22/Windows-11.jpg
---

## Souhrn

Microsoft potvrdil známý problém v říjnové volitelné aktualizaci Windows 11 (KB5067036), který brání uživatelům řádně ukončit Správce úloh. Aplikace po kliknutí na křížek pokračuje v běhu na pozadí, což vede k hromadění desítek instancí procesu taskmgr.exe a způsobuje zpomalení systému, zasekávání a problémy s procesorem.

## Klíčové body

- Aktualizace KB5067036 vydaná 28. října 2025 způsobuje, že Správce úloh nelze ukončit standardním tlačítkem zavřít
- Proces taskmgr.exe pokračuje v běhu na pozadí i po zavření viditelného okna aplikace
- Při opakovaném otevírání se hromadí desítky instancí, které spotřebovávají systémové prostředky
- Microsoft zatím neposkytl opravu, ale nabízí dočasné řešení přes příkazový řádek
- Problém se týká pouze volitelné aktualizace, kterou si uživatelé instalují dobrovolně

## Podrobnosti

Chyba se projevuje tak, že po zavření Správce úloh pomocí standardního tlačítka s křížkem v pravém horním rohu okna se proces taskmgr.exe neukončí kompletně. Při každém dalším otevření aplikace se vytvoří nová instance, zatímco předchozí pokračují v běhu na pozadí bez viditelného okna. Tyto procesy jsou viditelné v záložce Procesy jako "Task Manager" a v záložce Podrobnosti jako "Taskmgr.exe".

Podle Microsoftu má několik běžících instancí Správce úloh minimální dopad na většinu systémů, problém však nabývá na závažnosti, když se jich nahromadí desítky. To může vést k výraznému zpomalení ostatních aplikací, zasekávání systému a zvýšenému zatížení procesoru.

Microsoft problém stále vyšetřuje a oficiální oprava zatím není k dispozici. Společnost však poskytla dočasné řešení, které vyžaduje manuální ukončení procesů. Uživatelé mohou buď jednotlivě ukončovat každou instanci v novém okně Správce úloh pomocí tlačítka "Ukončit úlohu", nebo použít příkazový řádek pro ukončení všech instancí najednou příkazem taskkill.

Aktualizace KB5067036 je volitelná preview aktualizace, což znamená, že ji uživatelé nemusí instalovat povinně. Tyto aktualizace slouží k testování nových funkcí a oprav před jejich začleněním do pravidelných měsíčních bezpečnostních aktualizací.

## Proč je to důležité

Tento problém ilustruje pokračující potíže Microsoftu s kvalitou aktualizací Windows 11. Správce úloh je kritický systémový nástroj, který uživatelé používají právě k řešení problémů s výkonem a zamrzlými aplikacemi. Ironie spočívá v tom, že nástroj určený k ukončování problematických procesů se sám stal zdrojem problémů s výkonem.

Pro běžné uživatele to znamená nutnost vyhnout se instalaci této volitelné aktualizace, dokud Microsoft nevydá opravu. Ti, kteří ji již nainstalovali, musí buď čekat na patch, nebo používat příkazový řádek k ručnímu čištění nahromadělých procesů. Situace opět zdůrazňuje důležitost opatrnosti při instalaci volitelných aktualizací a připomíná, že i základní systémové funkce mohou být aktualizacemi narušeny.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-task-manager-wont-quit-after-kb5067036-update/)

**Zdroj:** 📰 BleepingComputer
