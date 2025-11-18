---
author: Marisa Aigen
category: bezpečnostní aktuali
companies:
- Microsoft
date: '2025-11-16 21:47:14'
description: Microsoft tento týden vydal bezpečnostní aktualizace pro více než 60
  zranitelností ve Windows a dalších produktech, včetně alespoň jednoho zero-day,
  který je již aktivně zneužíván útočníky.
importance: 4
layout: tech_news_article
original_title: Microsoft Patch Tuesday, November 2025 Edition
publishedAt: '2025-11-16T21:47:14+00:00'
slug: microsoft-patch-tuesday-november-2025-edition
source:
  emoji: 📰
  id: null
  name: Krebs on Security
title: Microsoft vydal nouzové bezpečnostní záplaty pro více než 60 zranitelností,
  včetně aktivně zneužívaného zero-day
url: https://krebsonsecurity.com/2025/11/microsoft-patch-tuesday-november-2025-edition/
---

## Souhrn
Microsoft vydal v rámci listopadového Patch Tuesday 2025 bezpečnostní záplaty pro více než 60 zranitelností napříč svým ekosystémem, včetně alespoň jednoho zero-day (CVE-2025-62215), který je již aktivně zneužíván. Mezi opravenými produkty patří Windows, Office, SharePoint, SQL Server, Visual Studio, GitHub Copilot a Azure Monitor Agent.

## Klíčové body
- Zero-day CVE-2025-62215 je chyba poškození paměti ve Windows, která vyžaduje předchozí přístup útočníka k zařízení.
- Kritická zranitelnost CVE-2025-60274 v grafické knihovně GDI+ ohrožuje širokou škálu aplikací, včetně Office a webových serverů.
- Další kritická chyba CVE-2025-62199 v Microsoft Office umožňuje vzdálené spuštění kódu.
- Microsoft opravil také chybu bránící některým uživatelům Windows 10 využít prodlouženou podporu zabezpečení.

## Podrobnosti
Nejvážnější zranitelností měsíce je CVE-2025-62215 – chyba poškození paměti (memory corruption) v jádru Windows. I když ji Microsoft klasifikuje jako „důležitou“ (Important) a ne „kritickou“ (Critical), je již aktivně zneužívána. Podle Johanna Ullricha ze SANS Technology Institute se jedná o součást složitějšího řetězce útoků, ale její zneužití je relativně jednoduché díky existenci podobných dřívějších chyb.

Zvláštní pozornost si zaslouží CVE-2025-60274 – kritická zranitelnost v knihovně GDI+ (Graphics Device Interface Plus), která je používána tisíci aplikacemi, včetně Microsoft Office a serverů zpracovávajících obrázky. Bezpečnostní expert Ben McCarthy z firmy Immersive (specializující se na kybernetickou bezpečnost firemních sítí) varuje, že i přes Microsoftovo hodnocení „Exploitation Less Likely“ představuje tato chyba s CVSS skóre 9,8 extrémní riziko kvůli univerzálnímu nasazení GDI+.

Další vážná chyba, CVE-2025-62199 v Microsoft Office, umožňuje vzdálené spuštění kódu bez potřeby zvýšených oprávnění. Alex Vovk, CEO společnosti Action1 (poskytovatel cloudového řešení pro správu a zabezpečení zařízení), zdůrazňuje, že tato zranitelnost je nízké složitosti a proto prioritní pro opravu.

## Proč je to důležité
Tento měsíční balík záplat přesahuje běžný rámec rutinních bezpečnostních aktualizací. Přítomnost aktivně zneužívaného zero-day a kritických chyb v univerzálně používaných komponentách jako GDI+ či Office zvyšuje riziko masivních útoků, zejména proti podnikovým sítím. Rychlá aplikace záplat je nezbytná, protože tyto chyby mohou být využity k přetrvávání v systému, exfiltrace dat nebo nasazení ransomwaru. Vzhledem k tomu, že zranitelnosti postihují i Windows 10 – stále široce používaný operační systém – je třeba zajistit, že i starší systémy jsou aktualizovány, což Microsoft usnadnil opravou chyby bránící některým uživatelům využít prodlouženou bezpečnostní podporu.

---

[Číst původní článek](https://krebsonsecurity.com/2025/11/microsoft-patch-tuesday-november-2025-edition/)

**Zdroj:** 📰 Krebs on Security
