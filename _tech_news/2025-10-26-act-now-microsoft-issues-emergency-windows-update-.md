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
title: Microsoft vydal mimořádnou aktualizaci Windows kvůli probíhajícím útokům
url: https://www.forbes.com/sites/daveywinder/2025/10/26/act-now---microsoft-issues-emergency-windows-update-as-attacks-begin/
urlToImage: https://imageio.forbes.com/specials-images/imageserve/68fc877d881b796e82ab5188/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
urlToImageBackup: https://imageio.forbes.com/specials-images/imageserve/68fc877d881b796e82ab5188/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
---

## Souhrn

Microsoft vydal mimořádnou bezpečnostní aktualizaci pro Windows Server v reakci na aktivní kybernetické útoky zneužívající kritickou zranitelnost označenou jako CVE-2025-59287. Americká agentura pro kybernetickou bezpečnost CISA potvrdila, že útoky již probíhají a vydala závaznou směrnici pro federální agentury, aby systémy okamžitě aktualizovaly.

## Klíčové body

- Zranitelnost CVE-2025-59287 postihuje Windows Server Update Service (WSUS) a umožňuje vzdálené spuštění škodlivého kódu přes síť
- CISA potvrdila aktivní útoky a vydala závaznou směrnici pro federální agentury
- Postiženy jsou pouze servery s aktivovanou rolí WSUS, která není ve výchozím nastavení zapnutá
- Jde o druhou kritickou zranitelnost Windows Server během necelého týdne
- Microsoft klasifikoval problém jako kritický s vysokou prioritou

## Podrobnosti

Windows Server Update Service je komponenta serverových verzí Windows, která umožňuje správcům centralizovaně řídit distribuci aktualizací v rámci podnikové sítě. Zranitelnost CVE-2025-59287 představuje vážné bezpečnostní riziko, protože útočníkům umožňuje vzdáleně spustit libovolný kód na zranitelném serveru bez nutnosti fyzického přístupu či předchozí autentizace.

Microsoft ve svém prohlášení zdůraznil, že riziku jsou vystaveny pouze servery s explicitně aktivovanou rolí WSUS. Tato služba není ve výchozím nastavení Windows Server zapnutá, což omezuje rozsah potenciálně postižených systémů. Nicméně v podnikových prostředích, kde je WSUS běžně využíván pro správu aktualizací stovek či tisíců počítačů, představuje tato zranitelnost významné riziko.

Situace je o to závažnější, že jde již o druhou kritickou zranitelnost Windows Server během necelého týdne. Před několika dny CISA varovala před probíhajícími útoky na protokol Server Message Block (SMB), což naznačuje koordinovanou kampaň zaměřenou na serverovou infrastrukturu.

Agentura CISA, která spadá pod americké ministerstvo vnitřní bezpečnosti, zařadila CVE-2025-59287 do svého katalogu známých zneužívaných zranitelností a nařídila federálním agenturám okamžitou instalaci záplaty. Tato směrnice je právně závazná pro vládní instituce.

## Proč je to důležité

Tato situace ilustruje rostoucí sofistikovanost kybernetických útoků zaměřených na podnikovou infrastrukturu. Skutečnost, že útočníci začali zranitelnost aktivně zneužívat ještě před širším rozšířením bezpečnostní záplaty, naznačuje buď únik informací o zranitelnosti, nebo její nezávislé objevení útočníky.

Pro správce IT infrastruktury to znamená nutnost okamžité akce. Organizace využívající WSUS by měly prioritizovat instalaci této aktualizace, ideálně v řádu hodin, nikoli dnů. Zároveň je vhodné zkontrolovat logy serverů pro případné známky kompromitace.

Širší kontext ukazuje na pokračující trend, kdy se útočníci zaměřují na kritickou infrastrukturu a služby pro správu systémů, které při kompromitaci umožňují ovládnout celé sítě najednou.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/10/26/act-now---microsoft-issues-emergency-windows-update-as-attacks-begin/)

**Zdroj:** 💼 Forbes
