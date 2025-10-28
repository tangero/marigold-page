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
- Jde o druhou kritickou zranitelnost Windows Server během necelého týdne, předchozí se týkala protokolu Server Message Block
- WSUS role není ve výchozím nastavení aktivní, zranitelné jsou pouze servery s explicitně povolenou WSUS rolí
- Microsoft klasifikoval zranitelnost jako kritickou s možností vzdáleného spuštění kódu

## Podrobnosti

Windows Server Update Service je komponenta serverových verzí Windows, která umožňuje administrátorům centralizovaně spravovat a distribuovat aktualizace operačního systému a dalšího softwaru v podnikových sítích. Zranitelnost CVE-2025-59287 v této službě představuje vážné bezpečnostní riziko, protože útočník může vzdáleně spustit libovolný kód bez nutnosti fyzického přístupu k serveru.

Podstatné je, že WSUS role není ve výchozím stavu na Windows serverech aktivní. To znamená, že ne všechny Windows servery jsou automaticky zranitelné - riziku čelí pouze ty organizace, které WSUS explicitně nasadily pro správu aktualizací ve své infrastruktuře. Typicky jde o střední a velké podniky, které potřebují centralizovanou kontrolu nad aktualizacemi desítek či stovek počítačů.

Cybersecurity and Infrastructure Security Agency, která spadá pod americké ministerstvo vnitřní bezpečnosti, nejen varovala před aktivními útoky, ale také vydala závaznou operativní směrnici. To je krok, který CISA podniká pouze v případě vážných hrozeb s potvrzeným zneužíváním. Federální agentury mají povinnost systémy aktualizovat v krátkém časovém horizontu.

Jde již o druhou kritickou zranitelnost Windows Server v průběhu necelého týdne. Předchozí se týkala protokolu Server Message Block, který se používá pro sdílení souborů a tiskáren v síti. Tato kumulace bezpečnostních problémů naznačuje intenzivní období pro správce Windows serverů.

## Proč je to důležité

Tato situace ilustruje rostoucí tlak na serverovou infrastrukturu a důležitost okamžité reakce na bezpečnostní hrozby. Windows Server tvoří páteř IT infrastruktury mnoha organizací po celém světě, a zranitelnosti umožňující vzdálené spuštění kódu patří mezi nejnebezpečnější typy bezpečnostních problémů. Útočník, který takovou zranitelnost úspěšně zneužije, může získat plnou kontrolu nad serverem a potenciálně se pohybovat laterálně po celé síti organizace.

Fakt, že CISA potvrdila aktivní útoky, znamená, že nejde o teoretickou hrozbu, ale o reálné nebezpečí s dokumentovanými případy zneužití. Organizace provozující Windows Server s aktivní WSUS rolí by měly aktualizaci považovat za prioritu nejvyšší úrovně. Zpoždění v nasazení záplaty může vést ke kompromitaci systémů, úniku dat nebo nasazení ransomwaru.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/10/26/act-now---microsoft-issues-emergency-windows-update-as-attacks-begin/)

**Zdroj:** 💼 Forbes
