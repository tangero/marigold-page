---
author: Marisa Aigen
category: kybernetika
companies:
- Microsoft
date: '2025-11-11 18:45:29'
description: Listopadová sada záplat Microsoftu (Patch Tuesday) přináší opravy 63
  zranitelností napříč produkty, včetně aktivně zneužívaného zero-day ve Windows Kernel,
  čtyř chyb hodnocených jako kritické a prvního balíčku rozšířené podpory pro Windows
  10.
importance: 4
layout: tech_news_article
original_title: Microsoft November 2025 Patch Tuesday fixes 1 zero-day, 63 flaws -
  BleepingComputer
publishedAt: '2025-11-11T18:45:29+00:00'
slug: microsoft-november-2025-patch-tuesday-fixes-1-zero
source:
  emoji: 📰
  id: null
  name: BleepingComputer
title: Microsoft v listopadu 2025 opravuje 63 zranitelností včetně aktivně zneužívaného
  zero-day ve Windows
url: https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2025-patch-tuesday-fixes-1-zero-day-63-flaws/
urlToImage: https://www.bleepstatic.com/content/hl-images/2024/10/08/patch_tuesday_microsoft.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2024/10/08/patch_tuesday_microsoft.jpg
---

## Souhrn
Microsoft v rámci listopadového Patch Tuesday 2025 vydal bezpečnostní aktualizace řešící 63 zranitelností napříč systémy Windows a dalšími produkty, včetně jedné aktivně zneužívané zero-day chyby v komponentě Windows Kernel. Záplaty zahrnují čtyři kritické zranitelnosti a zároveň zahajují program rozšířené bezpečnostní podpory (ESU) pro Windows 10, který je nyní oficiálně mimo běžný podporovaný životní cyklus.

## Klíčové body
- Celkem opraveno 63 zranitelností, z toho 1 aktivně zneužívaná zero-day ve Windows Kernel.
- Čtyři zranitelnosti klasifikované jako kritické (dvě RCE, jedno zvýšení oprávnění, jedno únik informací).
- Převaha chyb typu elevation of privilege (29) a remote code execution (16), které mají vysoký dopad na podnikové prostředí.
- První vydání rozšířených bezpečnostních aktualizací (ESU) pro Windows 10; ostatní uživatelé mají migrovat na Windows 11.
- Oprava mimo běžný cyklus (out-of-band update) řeší problém s registrací do ESU programu.

## Podrobnosti
Listopadový balíček záplat Microsoftu řeší široké spektrum slabin, které pokrývají běžné scénáře útoků v podnikových sítích. Struktura opravených chyb je následující: 29 zranitelností typu elevation of privilege, 2 security feature bypass, 16 remote code execution (RCE), 11 information disclosure, 3 denial of service a 2 spoofing. Nejrizikovější jsou RCE a EoP, protože umožňují útočníkům po úspěšném zneužití spustit libovolný kód, získat vyšší oprávnění a trvale se usadit v infrastruktuře.

Klíčovým prvkem je jedna aktivně zneužívaná zero-day zranitelnost ve Windows Kernel. Zero-day zde znamená, že chyba byla buď veřejně známa, nebo aktivně zneužívána před vydáním záplaty. Kernel je kritická součást systému; úspěšné zneužití často umožňuje obejít sandboxing, antivirové nástroje i některé EDR/EDR-XDR systémy. To z ní činí prioritu číslo jedna pro okamžitou instalaci aktualizací zejména na stanicích s přístupem k internetu a na systémech správců.

Významný posun nastává u Windows 10. Tento systém je mimo standardní podporu, a proto Microsoft spouští program Extended Security Updates (ESU), který poskytuje placené bezpečnostní záplaty pro organizace, které z různých důvodů nemohou migrovat na Windows 11 (kompatibilita aplikací, hardware, kritické provozní systémy). Microsoft musel vydat i mimořádnou aktualizaci (out-of-band), která řeší chybu bránící některým zákazníkům v registraci do ESU. Pro správce to znamená nutnost ověřit nejen nasazení listopadových záplat, ale i funkčnost kanálů pro distribuci ESU.

## Proč je to důležité
Zveřejněný balík potvrzuje pokračující posun hrozeb směrem k exploitaci jádra systému a zneužívání chyb umožňujících zvýšení oprávnění. Pro organizace je klíčové nespoléhat na perimetr, ale udržovat konzistentní proces patch managementu, protože kombinace RCE + EoP typicky stačí k plnému ovládnutí prostředí. Aktivně zneužívaná zero-day ve Windows Kernel znamená, že odkládání záplat reálně zvyšuje riziko ransomwarových a cílených útoků.

Zahájení programu ESU pro Windows 10 zároveň vytváří jasnou hranici: kdo nezaplatí za ESU nebo nepřejde na Windows 11, bude provozovat neaktualizovaný a z hlediska bezpečnosti neudržitelný systém. V kontextu regulatorních požadavků (např. NIS2, interní bezpečnostní standardy) to pro podniky prakticky znamená, že setrvání na nezaopatřeném Windows 10 je obtížně obhajitelné. Správci by měli tento Patch Tuesday využít jako impuls pro revizi inventáře, automatizaci nasazování aktualizací a audit kritických systémů, kde je zero-day v kernelu obzvlášť nebezpečná.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2025-patch-tuesday-fixes-1-zero-day-63-flaws/)

**Zdroj:** 📰 BleepingComputer
