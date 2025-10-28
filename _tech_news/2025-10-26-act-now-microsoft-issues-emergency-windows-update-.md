---
category: kybernetická bezpečn
companies:
- Microsoft
date: '2025-10-26 09:24:32'
description: Americká agentura CISA varuje před aktivními útoky zneužívajícími kritickou
  zranitelnost CVE-2025-59287 ve Windows Server Update Service. Microsoft vydal nouzovou
  záplatu.
importance: 5
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
- CISA potvrdila aktivní útoky a vydala závaznou směrnici pro federální instituce
- Postiženy jsou pouze servery s aktivovanou rolí WSUS, která není ve výchozím nastavení zapnutá
- Jedná se o druhou kritickou zranitelnost Windows Server během necelého týdne
- Microsoft klasifikoval problém jako kritický s vysokou prioritou

## Podrobnosti

Zranitelnost CVE-2025-59287 se nachází ve službě Windows Server Update Service, která slouží k centralizované správě a distribuci aktualizací Windows v podnikových sítích. Útočníci mohou tuto chybu zneužít ke vzdálenému spuštění libovolného kódu na zranitelných serverech bez nutnosti předchozí autentizace.

Microsoft ve svém bezpečnostním bulletinu zdůraznil, že riziku jsou vystaveny pouze servery s explicitně aktivovanou rolí WSUS. Tato služba není ve výchozím nastavení Windows Server zapnutá, což omezuje rozsah potenciálně postižených systémů. Přesto jde o vážný problém, protože WSUS je běžně využíván ve větších organizacích a podnikových prostředích.

Agentura CISA, která spadá pod americké ministerstvo vnitřní bezpečnosti, zařadila CVE-2025-59287 do svého katalogu známých zneužívaných zranitelností. Tento krok signalizuje, že útoky nejsou pouze teoretické, ale aktivně probíhají v reálném prostředí. CISA nařídila federálním agenturám aplikovat záplatu s okamžitou platností.

Jde již o druhou kritickou zranitelnost Windows Server v průběhu necelého týdne. Před méně než sedmi dny CISA varovala před útoky zneužívajícími protokol Server Message Block (SMB) postihující Windows Server, Windows 10 a Windows 11. Tato kumulace bezpečnostních incidentů vyvolává otázky ohledně bezpečnostní architektury serverových produktů Microsoft.

## Proč je to důležité

Mimořádné bezpečnostní aktualizace mimo standardní měsíční cyklus záplat signalizují vážnost situace. Microsoft obvykle vydává aktualizace v pravidelných intervalech, mimořádné záplaty jsou rezervovány pro kritické hrozby s aktivním zneužíváním.

Pro organizace využívající Windows Server s aktivním WSUS představuje tato zranitelnost existenční riziko. Úspěšný útok může útočníkovi poskytnout plnou kontrolu nad serverem, který často spravuje aktualizace pro stovky či tisíce dalších systémů v síti. Kompromitace WSUS serveru tak může sloužit jako odrazový můstek pro rozsáhlé útoky na celou infrastrukturu.

Časová blízkost dvou kritických zranitelností Windows Server naznačuje možnou koordinovanou kampaň nebo zvýšené úsilí bezpečnostních výzkumníků zaměřené na tuto platformu. Administrátoři by měli zvýšit ostražitost a prioritizovat bezpečnostní monitoring serverové infrastruktury.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/10/26/act-now---microsoft-issues-emergency-windows-update-as-attacks-begin/)

**Zdroj:** 💼 Forbes
