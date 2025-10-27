---
category: kybernetická bezpečn
companies:
- Microsoft
date: '2025-10-26 09:24:32'
description: Americká agentura CISA varuje před aktivními útoky zneužívajícími kritickou
  zranitelnost CVE-2025-59287 ve Windows Server Update Service. Microsoft vydal nouzovou
  záplatu.
importance: 4
layout: tech_news_article
original_title: Act Now — Microsoft Issues Emergency Windows Update As Attacks Begin
  - Forbes
publishedAt: '2025-10-26T09:24:32+00:00'
slug: act-now-microsoft-issues-emergency-windows-update-
source:
  emoji: 💼
  id: null
  name: Forbes
title: Microsoft vydal nouzovou aktualizaci Windows kvůli probíhajícím útokům
url: https://www.forbes.com/sites/daveywinder/2025/10/26/act-now---microsoft-issues-emergency-windows-update-as-attacks-begin/
urlToImage: https://imageio.forbes.com/specials-images/imageserve/68fc877d881b796e82ab5188/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
urlToImageBackup: https://imageio.forbes.com/specials-images/imageserve/68fc877d881b796e82ab5188/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
---

## Souhrn

Microsoft vydal nouzovou bezpečnostní aktualizaci pro Windows Server kvůli kritické zranitelnosti CVE-2025-59287 ve službě Windows Server Update Service (WSUS). Americká agentura pro kybernetickou bezpečnost CISA potvrdila, že útoky zneužívající tuto chybu již probíhají, a vydala závaznou směrnici pro federální agentury, aby systémy okamžitě aktualizovaly.

## Klíčové body

- Zranitelnost CVE-2025-59287 umožňuje útočníkům vzdálené spuštění škodlivého kódu přes síť
- Postižena je služba Windows Server Update Service (WSUS), která není ve výchozím nastavení aktivní
- CISA potvrdila aktivní útoky a vydala závaznou směrnici pro federální agentury
- Jde o druhou kritickou zranitelnost Windows Server během necelého týdne
- Microsoft již vydal nouzovou záplatu, instalace je nutná okamžitě

## Podrobnosti

Kritická zranitelnost se nachází ve Windows Server Update Service, což je komponenta Windows Server sloužící k centralizované správě a distribuci aktualizací v podnikových sítích. Chyba umožňuje útočníkům vzdálené spuštění libovolného kódu bez nutnosti předchozí autentizace, což z ní činí mimořádně nebezpečnou hrozbu.

Microsoft ve svém prohlášení zdůraznil, že role WSUS serveru není ve výchozím nastavení na Windows serverech aktivní, což znamená, že ne všechny instalace jsou zranitelné. Ohroženy jsou pouze servery, kde administrátoři explicitně povolili tuto službu pro správu aktualizací v rámci své infrastruktury.

Jde již o druhou vážnou bezpečnostní krizi Windows Server v krátkém časovém úseku. Před necelým týdnem CISA varovala před probíhajícími útoky zneužívajícími protokol Server Message Block (SMB), které postihly Windows Server, Windows 10 i Windows 11. Tato kumulace bezpečnostních incidentů vyvolává otázky ohledně celkové bezpečnostní architektury serverových produktů Microsoftu.

Nouzová aktualizace přichází krátce po podobném kroku společnosti Google, která vydala nouzovou záplatu pro prohlížeč Chrome. Tato souběžnost naznačuje možnou koordinovanou kampaň kybernetických útočníků zaměřenou na kritickou infrastrukturu.

## Proč je to důležité

Zranitelnost představuje vážné riziko především pro podnikové prostředí a vládní instituce, které běžně využívají WSUS pro centralizovanou správu aktualizací. Skutečnost, že útoky již probíhají, činí situaci akutní – není čas čekat na standardní cyklus aktualizací.

Závazná směrnice CISA pro federální agentury signalizuje mimořádnou závažnost hrozby. Podobné direktivy se vydávají pouze v případech, kdy existuje bezprostřední riziko kompromitace kritických systémů. Pro soukromý sektor sice směrnice není závazná, ale měla by sloužit jako jasné varování k okamžité akci.

Opakované bezpečnostní incidenty Windows Server během několika dní naznačují buď systematické slabiny v bezpečnostním designu, nebo koordinované úsilí útočníků najít a zneužít zranitelnosti v široce používané infrastruktuře. Pro správce IT systémů to znamená nutnost zvýšené ostražitosti a rychlé reakce na bezpečnostní výstrahy.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/10/26/act-now---microsoft-issues-emergency-windows-update-as-attacks-begin/)

**Zdroj:** 💼 Forbes
