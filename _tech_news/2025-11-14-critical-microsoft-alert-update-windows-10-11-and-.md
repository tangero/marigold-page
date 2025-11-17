---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Microsoft
date: '2025-11-14 14:58:04'
description: Microsoft potvrdil aktivně zneužívanou zero-day zranitelnost v jádru
  Windows, která umožňuje útočníkům získat systémová oprávnění. Uživatelé musí co
  nejdříve nainstalovat bezpečnostní záplatu.
importance: 5
layout: tech_news_article
original_title: Critical Microsoft Alert — Update Windows 10, 11 And Server Right
  Now - Forbes
publishedAt: '2025-11-14T14:58:04+00:00'
slug: critical-microsoft-alert-update-windows-10-11-and-
source:
  emoji: 💼
  id: null
  name: Forbes
title: Kritické varování od Microsoftu – okamžitě aktualizujte Windows 10, 11 a Server
url: https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/
urlToImage: https://imageio.forbes.com/specials-images/imageserve/636b2aa808a3b5319a7fde55/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
urlToImageBackup: https://imageio.forbes.com/specials-images/imageserve/636b2aa808a3b5319a7fde55/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
---

## Souhrn
Microsoft vydal naléhavé bezpečnostní upozornění kvůli aktivně zneužívané zero-day zranitelnosti v jádru operačního systému Windows (CVE-2025-62215). Útočníci ji již využívají k eskalaci oprávnění a získání plné kontroly nad kompromitovanými systémy. Odborníci doporučují okamžitou aktualizaci všech verzí Windows 10, 11 i Windows Server.

## Klíčové body
- Zranitelnost CVE-2025-62215 je umístěna v jádru Windows a umožňuje eskalaci oprávnění.
- Microsoft potvrdil aktivní zneužívání v reálném prostředí („in the wild“).
- Útok vyžaduje splnění race condition, ale je efektivní v rámci post-exploitační fáze.
- Zranitelnost byla zveřejněna v rámci listopadového balíku oprav (Patch Tuesday), který obsahuje celkem 63 chyb.
- Odborníci doporučují aktualizaci i přes neobvyklý termín – mimo standardní cyklus.

## Podrobnosti
Zranitelnost CVE-2025-62215 byla identifikována jako chyba v jádru Windows, která umožňuje útočníkovi získat oprávnění na úrovni systému (SYSTEM). Podle Satnama Naranga, senior staff research engineeru z bezpečnostní firmy Tenable, je tato chyba pravděpodobně využívána až po počáteční kompromitaci systému – například prostřednictvím phishingových e-mailů nebo jiné zranitelnosti. I když úspěšný útok vyžaduje splnění race condition (časově závislé podmínky), skutečnost, že je již aktivně zneužívána, zvyšuje její rizikový profil na maximum.

Microsoft tuto chybu opravil v rámci svého listopadového bezpečnostního balíku, který vyšel 12. listopadu 2025. Uživatelé systémů Windows 10, 11 i Windows Server by měli co nejdříve nainstalovat dostupné aktualizace prostřednictvím Windows Update nebo centrální správy v podnicích. Zároveň Microsoft vydal i další opravy pro další kritické chyby, které byly objeveny v posledních dnech.

## Proč je to důležité
Tato zranitelnost představuje vážné bezpečnostní riziko, protože jádro operačního systému je nejcitlivější jeho částí – kompromitace jádra umožňuje útočníkovi obejít všechny bezpečnostní mechanismy systému. Vzhledem k tomu, že je chyba již aktivně zneužívána, jde o klasickou zero-day hrozbu s reálným dopadem. Pro firmy i jednotlivce je tedy nezbytné provést aktualizaci bez odkladu. Tento případ také ilustruje rostoucí tlak na dodavatele softwaru, aby reagovali rychleji na objevené hrozby – zejména v době, kdy se kybernetické útoky stávají sofistikovanějšími a cílenějšími.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/)

**Zdroj:** 💼 Forbes
