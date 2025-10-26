---
category: kybernetická bezpečn
companies:
- Microsoft
date: '2025-10-24 16:30:00'
description: Microsoft vydal nouzovou opravu pro kritickou zranitelnost CVE-2025-59287
  ve službě WSUS, která je již aktivně zneužívána útočníky v reálných útocích.
importance: 4
layout: tech_news_article
original_title: Newly Patched Critical Microsoft WSUS Flaw Comes Under Active Exploitation
  - The Hacker News
publishedAt: '2025-10-24T16:30:00+00:00'
slug: newly-patched-critical-microsoft-wsus-flaw-comes-u
source:
  emoji: 📰
  id: null
  name: Internet
title: Microsoft záplatuje kritickou chybu ve WSUS, která je aktivně zneužívána
url: https://thehackernews.com/2025/10/microsoft-issues-emergency-patch-for.html
urlToImage: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiboN42WiQTI7VcMEGEDyMaY3ZP7VsruF2cHNgK4XQ2SxW0adaaMaJYfa_3B5Og4rvc1KF9HS1L7IxA-jSa_ZWMOz5kAKexTlsbZHomhllf8esxYBqcv3-pL7GY5CCb7qZaSxFaM2s3sbLR6cw-KlYMQ0ZnyWbYpjxHph9tMZxDxGdsf6jQ8kdBWYsMdvol/s790-rw-e365/windows-update.jpg
urlToImageBackup: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiboN42WiQTI7VcMEGEDyMaY3ZP7VsruF2cHNgK4XQ2SxW0adaaMaJYfa_3B5Og4rvc1KF9HS1L7IxA-jSa_ZWMOz5kAKexTlsbZHomhllf8esxYBqcv3-pL7GY5CCb7qZaSxFaM2s3sbLR6cw-KlYMQ0ZnyWbYpjxHph9tMZxDxGdsf6jQ8kdBWYsMdvol/s790-rw-e365/windows-update.jpg
---

## Souhrn

Microsoft vydal kritickou bezpečnostní záplatu pro zranitelnost CVE-2025-59287 ve službě Windows Server Update Services (WSUS), která je již aktivně zneužívána útočníky. Chyba umožňuje vzdálené spuštění kódu a představuje vážné riziko pro podnikové sítě využívající WSUS pro správu aktualizací Windows.

## Klíčové body

- Kritická zranitelnost CVE-2025-59287 ve WSUS je aktivně zneužívána v reálných útocích
- Microsoft vydal mimořádnou bezpečnostní záplatu mimo standardní update cyklus
- Chyba umožňuje vzdálené spuštění kódu s vysokými privilegii
- Útočníci mohou zneužít WSUS infrastrukturu k distribuci malwaru v podnikových sítích
- Doporučuje se okamžitá instalace záplaty a audit WSUS serverů

## Podrobnosti

Windows Server Update Services (WSUS) je klíčová služba pro správu a distribuci aktualizací Windows v podnikových prostředích. Umožňuje administrátorům centralizovaně řídit, které aktualizace se nasadí na klientské stanice a servery v síti. Právě tato centrální role činí z WSUS atraktivní cíl pro útočníky.

Zranitelnost CVE-2025-59287 představuje kritické bezpečnostní riziko, protože útočník, který ji úspěšně zneužije, může získat možnost vzdáleně spustit libovolný kód na WSUS serveru. Vzhledem k tomu, že WSUS servery mají důvěryhodné postavení v síti a komunikují s velkým počtem klientských systémů, může kompromitace takového serveru vést k masivnímu šíření malwaru napříč celou organizací.

Skutečnost, že zranitelnost je již aktivně zneužívána, znamená, že útočníci mají funkční exploit a cílí na nezáplatované systémy. Microsoft vydal opravu mimo svůj standardní měsíční update cyklus Patch Tuesday, což podtrhuje závažnost situace. Společnost doporučuje okamžitou instalaci záplaty a provedení bezpečnostního auditu všech WSUS serverů.

V souvislosti s touto zranitelností OWASP vydala aktualizovaný přehled deseti nejčastějších bezpečnostních rizik v CI/CD pipeline, který obsahuje praktická doporučení pro snížení útočné plochy a posílení bezpečnosti vývojových procesů.

## Proč je to důležité

Tato zranitelnost představuje významné riziko pro podnikové prostředí, kde WSUS patří mezi základní infrastrukturní služby. Kompromitace WSUS serveru může útočníkům poskytnout ideální platformu pro laterální pohyb v síti a distribuci malwaru pod záminkou legitimních aktualizací. Aktivní zneužívání znamená, že organizace čelí reálnému a bezprostřednímu ohrožení. Incident opět ukazuje, že i kritická infrastrukturní služba od Microsoftu může obsahovat závažné chyby, a zdůrazňuje nutnost rychlé reakce na bezpečnostní záplaty a implementace defense-in-depth strategie v podnikových sítích.

---

[Číst původní článek](https://thehackernews.com/2025/10/microsoft-issues-emergency-patch-for.html)

**Zdroj:** 📰 Internet
