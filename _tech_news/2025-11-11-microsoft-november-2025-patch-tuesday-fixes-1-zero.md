---
author: Marisa Aigen
category: kybernetická bezpečn
companies:
- Microsoft
date: '2025-11-11 18:45:29'
description: Listopadové záplaty Microsoftu řeší 63 bezpečnostních chyb ve Windows
  a souvisejících produktech, včetně jedné aktivně zneužívané zero-day zranitelnosti
  v jádře systému, a přinášejí první vlnu rozšířených bezpečnostních aktualizací (ESU)
  pro Windows 10.
importance: 3
layout: tech_news_article
original_title: Microsoft November 2025 Patch Tuesday fixes 1 zero-day, 63 flaws -
  BleepingComputer
publishedAt: '2025-11-11T18:45:29+00:00'
slug: microsoft-november-2025-patch-tuesday-fixes-1-zero
source:
  emoji: 📰
  id: null
  name: BleepingComputer
title: Microsoft v rámci listopadových záplat 2025 opravuje 63 zranitelností a jednu
  aktivně zneužívanou zero-day chybu
url: https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2025-patch-tuesday-fixes-1-zero-day-63-flaws/
urlToImage: https://www.bleepstatic.com/content/hl-images/2024/10/08/patch_tuesday_microsoft.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2024/10/08/patch_tuesday_microsoft.jpg
---

## Souhrn
Microsoft v rámci listopadového Patch Tuesday 2025 vydal bezpečnostní aktualizace opravující 63 zranitelností, z nichž jedna je aktivně zneužívaná zero-day chyba v jádře Windows. Záplaty zahrnují čtyři kritické zranitelnosti a zároveň zahajují program rozšířených bezpečnostních aktualizací (ESU) pro Windows 10, které je jinak již nepodporovaným systémem.

## Klíčové body
- Celkem 63 opravených zranitelností, včetně jedné aktivně zneužívané zero-day chyby v Windows Kernel.
- Čtyři zranitelnosti klasifikovány jako kritické: dvě remote code execution (RCE), jedna elevation of privilege a jedna information disclosure.
- Nejvíce chyb spadá do kategorií elevation of privilege (29) a remote code execution (16).
- Zahájení ESU programu pro Windows 10 a vydání mimořádné aktualizace pro řešení problému se zápisem do ESU.
- Doporučení k prioritní instalaci záplat zejména ve firemním prostředí a u systémů vystavených internetu.

## Podrobnosti
Listopadový Patch Tuesday 2025 přináší soubor bezpečnostních oprav zaměřený na klíčové komponenty Windows, včetně jádra systému (Windows Kernel), subsystémů pro správu oprávnění a mechanismů vzdáleného spouštění kódu. Microsoft opravuje celkem 63 zranitelností, rozdělených do několika kategorií: 29 elevation of privilege, 2 security feature bypass, 16 remote code execution, 11 information disclosure, 3 denial of service a 2 spoofing. Tato struktura ukazuje, že útočníci nadále cíleně zneužívají kombinaci zvýšení oprávnění a vzdáleného spuštění kódu pro kompletní převzetí systémů.

Nejdůležitějším prvkem tohoto vydání je oprava aktivně zneužívané zero-day chyby v Windows Kernel. Zero-day zranitelnost v jádře typicky umožňuje obejít izolaci procesů, získat vyšší oprávnění nebo stabilněji přetrvávat v systému, což je ideální pro pokročilé útoky včetně ransomwaru, průmyslové špionáže a cílených kampaní proti kritické infrastruktuře. Přestože dostupný výtah textu neuvádí přesné CVE označení, z charakteru zranitelnosti vyplývá, že k exploitaci může dojít po předchozím průniku, kdy útočník potřebuje eskalovat práva na úroveň SYSTEM.

Významnou roli hraje také spuštění programu Extended Security Updates (ESU) pro Windows 10. Windows 10 je mimo běžnou podporu, což znamená, že bez ESU zůstávají systémy bez záplat pro nově objevené chyby. Microsoft k tomu vydal mimořádnou (out-of-band) aktualizaci opravující chybu, která některým organizacím bránila do ESU programu vstoupit. Pro firmy, které stále provozují Windows 10 na koncových stanicích, v průmyslových systémech nebo v prostředí s kritickou závislostí na starších aplikacích, je správné nastavení ESU nyní zásadní bezpečnostní otázkou.

Upozornění se týká také správy prostředí, kde dochází k opožděnému nasazování Patch Tuesday aktualizací. Větší organizace často bojují s prioritizací, testováním kompatibility a viditelností nad tím, které systémy zůstávají nezáplatované. To je přesně prostor, kde moderní nástroje pro správu aktualizací a automatizaci patch managementu pomáhají minimalizovat dobu zranitelnosti.

## Proč je to důležité
Aktivně zneužívaná zero-day zranitelnost v jádře Windows je přímé riziko pro firmy i veřejnou správu. V kombinaci s RCE a elevation of privilege chybami umožňuje útočníkům provádět komplexní útoky: od počátečního průniku přes phishing nebo zranitelné služby, až po plnou kompromitaci doménové infrastruktury. Organizace, které odkládají aktualizace, se fakticky stávají snadnějším cílem, protože exploit kód se obvykle brzy po zveřejnění záplat objeví v běžně používaných útočných sadách.

Pro provozovatele Windows 10 je tato vlna záplat signálem, že provoz bez ESU nebo bez migrace na Windows 11 představuje reálné a rostoucí riziko. V širším kontextu kybernetické bezpečnosti tento Patch Tuesday potvrzuje dlouhodobý trend: klíčový boj se vede v oblasti správy zranitelností, rychlosti nasazení aktualizací a schopnosti udržet přehled o reálném stavu koncových bodů a serverů. Bez disciplinovaného patch managementu se i dobře navržené bezpečnostní architektury stávají formální a snadno obejitelnou překážkou.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2025-patch-tuesday-fixes-1-zero-day-63-flaws/)

**Zdroj:** 📰 BleepingComputer
