---
category: kybernetická bezpečn
companies:
- Microsoft
date: '2025-10-25 08:43:46'
description: Americká agentura CISA varuje před aktivními kybernetickými útoky zneužívajícími
  kritickou zranitelnost ve Windows Server Update Service. Microsoft vydal nouzovou
  záplatu.
importance: 4
layout: tech_news_article
original_title: Act Now — Microsoft Issues Emergency Windows Update As Attacks Begin
  - Forbes
publishedAt: '2025-10-25T08:43:46+00:00'
slug: act-now-microsoft-issues-emergency-windows-update-
source:
  emoji: 💼
  id: null
  name: Forbes
title: Microsoft vydal mimořádnou aktualizaci Windows kvůli probíhajícím útokům
url: https://www.forbes.com/sites/daveywinder/2025/10/25/act-now---microsoft-issues-emergency-windows-update-as-attacks-begin/
urlToImage: https://imageio.forbes.com/specials-images/imageserve/68fc877d881b796e82ab5188/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
urlToImageBackup: https://imageio.forbes.com/specials-images/imageserve/68fc877d881b796e82ab5188/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
---

## Souhrn

Microsoft vydal mimořádnou bezpečnostní aktualizaci pro Windows Server v reakci na aktivní kybernetické útoky zneužívající kritickou zranitelnost označenou jako CVE-2025-59287. Americká agentura pro kybernetickou bezpečnost CISA potvrdila, že útoky již probíhají a federálním agenturám nařídila instalaci záplaty do dvou týdnů.

## Klíčové body

- Zranitelnost CVE-2025-59287 postihuje Windows Server Update Service (WSUS) a umožňuje vzdálené spuštění škodlivého kódu přes síť
- CISA potvrdila aktivní útoky a vydala závaznou směrnici pro federální agentury s dvoutýdenní lhůtou
- Ohroženy jsou pouze servery s aktivovanou rolí WSUS, která není ve výchozím nastavení zapnutá
- Jde o druhý závažný bezpečnostní incident postihující Windows Server během necelého týdne
- Microsoft vydal nouzovou záplatu, kterou je nutné nainstalovat před aktivací role WSUS

## Podrobnosti

Zranitelnost se nachází ve Windows Server Update Service, což je serverová komponenta umožňující správcům centralizovaně řídit distribuci aktualizací Windows v podnikových sítích. Útočníci mohou tuto chybu zneužít ke vzdálenému spuštění libovolného kódu na zranitelném serveru bez nutnosti předchozí autentizace, což z ní činí kritickou bezpečnostní hrozbu.

Microsoft ve svém prohlášení zdůraznil, že role WSUS není ve výchozím nastavení aktivní na Windows serverech. Servery bez aktivované role WSUS tedy nejsou zranitelné. Pokud však organizace tuto roli používá nebo plánuje aktivovat, musí nejprve nainstalovat bezpečnostní záplatu. V opačném případě se server stane okamžitě zranitelným vůči útokům.

Jde již o druhou závažnou zranitelnost Windows Server v průběhu necelého týdne. Před méně než týdnem CISA varovala federální agentury kvůli probíhajícím útokům na protokol Server Message Block (SMB), které postihují Windows Server, Windows 10 i Windows 11. Tato kumulace bezpečnostních incidentů naznačuje zvýšenou aktivitu útočníků zaměřených na serverovou infrastrukturu Windows.

CISA, která spadá pod americké ministerstvo vnitřní bezpečnosti, vydala závaznou směrnici vyžadující od federálních agentur instalaci záplaty do dvou týdnů. Současně důrazně doporučuje všem organizacím využívajícím WSUS okamžitou aktualizaci bez ohledu na to, zda spadají pod federální mandát.

## Proč je to důležité

Tato situace ilustruje rostoucí tlak na serverovou infrastrukturu a kritickou důležitost rychlé reakce na bezpečnostní hrozby. Windows Server Update Service je klíčovou komponentou pro správu aktualizací v podnikových prostředích, což z něj činí atraktivní cíl pro útočníky. Kompromitace WSUS serveru by mohla útočníkům umožnit distribuci škodlivých aktualizací do celé podnikové sítě.

Fakt, že CISA potvrdila aktivní zneužívání zranitelnosti, znamená, že nejde o teoretickou hrozbu, ale o reálné útoky probíhající v současnosti. Organizace využívající WSUS by měly aktualizaci považovat za prioritu nejvyšší úrovně. Dvoutýdenní lhůta stanovená pro federální agentury naznačuje vážnost situace a nutnost okamžitého jednání i pro soukromý sektor.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/10/25/act-now---microsoft-issues-emergency-windows-update-as-attacks-begin/)

**Zdroj:** 💼 Forbes
