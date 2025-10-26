---
category: kybernetická bezpečn
companies:
- Microsoft
date: '2025-10-25 08:43:46'
description: Americká agentura CISA varuje před aktivními útoky zneužívajícími kritickou
  zranitelnost ve Windows Server Update Service. Microsoft vydal nouzovou záplatu.
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

Microsoft vydal mimořádnou bezpečnostní aktualizaci pro Windows Server v reakci na aktivní kybernetické útoky zneužívající kritickou zranitelnost označenou jako CVE-2025-59287. Americká agentura pro kybernetickou bezpečnost CISA potvrdila, že útoky již probíhají a nařídila federálním agenturám instalaci záplaty do dvou týdnů.

## Klíčové body

- Zranitelnost CVE-2025-59287 postihuje Windows Server Update Service (WSUS) a umožňuje vzdálené spuštění škodlivého kódu přes síť
- CISA vydala závaznou směrnici pro federální agentury s dvoutýdenní lhůtou pro instalaci aktualizace
- Útočníci již aktivně zneužívají tuto zranitelnost v reálných útocích
- Role WSUS serveru není ve výchozím nastavení aktivní, riziku jsou vystaveny pouze servery s povolenou touto funkcí
- Jde o druhou kritickou zranitelnost Windows Server během necelého týdne

## Podrobnosti

Zranitelnost CVE-2025-59287 se nachází ve Windows Server Update Service, komponentě určené pro centralizovanou správu aktualizací Windows v podnikových sítích. WSUS umožňuje administrátorům kontrolovat, které aktualizace se budou instalovat na klientské stanice a servery v organizaci. Kritičnost této zranitelnosti spočívá v možnosti vzdáleného spuštění kódu (Remote Code Execution), což útočníkům poskytuje potenciál převzít plnou kontrolu nad napadeným serverem bez nutnosti fyzického přístupu.

Microsoft ve svém prohlášení zdůraznil, že ne všechny Windows servery jsou automaticky zranitelné. Role WSUS serveru musí být explicitně povolena, aby se server stal terčem útoku. Organizace, které tuto funkci nevyužívají, nejsou ohroženy. Pokud však byla role WSUS povolena před instalací bezpečnostní záplaty, server se stává zranitelným.

Tato mimořádná aktualizace přichází méně než týden poté, co CISA vydala varování ohledně jiných útoků zaměřených na Windows Server, Windows 10 a Windows 11 využívajících zranitelnosti v protokolu Server Message Block. Dvě kritické zranitelnosti v tak krátkém časovém úseku naznačují zvýšenou aktivitu útočníků zaměřených na serverovou infrastrukturu.

CISA, která spadá pod americké ministerstvo vnitřní bezpečnosti, má pravomoc vydávat závazné směrnice pro federální agentury. Dvoutýdenní lhůta pro instalaci aktualizace je neobvykle krátká a odráží závažnost situace. Agentura současně důrazně doporučuje instalaci záplaty i soukromým organizacím a firmám.

## Proč je to důležité

Tato situace ilustruje rostoucí sofistikovanost kybernetických útoků zaměřených na podnikovou infrastrukturu. Windows Server tvoří páteř IT infrastruktury většiny velkých organizací, a kompromitace WSUS serveru může mít kaskádový efekt na celou síť. Útočník s kontrolou nad WSUS může distribuovat škodlivé "aktualizace" na všechny připojené systémy, čímž efektivně ovládne celou podnikovou síť.

Fakt, že útoky již probíhají ještě před širším povědomím o zranitelnosti, naznačuje koordinovanou kampaň pravděpodobně státem sponzorovaných aktérů nebo organizovaných kyberzločineckých skupin. Pro administrátory IT je prioritou okamžitě ověřit, zda mají WSUS roli povolenou, a pokud ano, neprodleně nainstalovat poskytnutou záplatu. Organizace by měly také zvážit dočasné odpojení WSUS serverů od internetu, dokud nebude aktualizace aplikována.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/10/25/act-now---microsoft-issues-emergency-windows-update-as-attacks-begin/)

**Zdroj:** 💼 Forbes
