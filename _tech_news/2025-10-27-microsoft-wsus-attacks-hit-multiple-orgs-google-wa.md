---
category: kybernetická bezpečn
companies:
- Microsoft
- Google
date: '2025-10-27 23:54:00'
description: Microsoft vydal nouzovou záplatu pro kritickou zranitelnost CVE-2025-59287
  ve Windows Server Update Services, kterou útočníci aktivně zneužívají k útokům na
  organizace.
importance: 4
layout: tech_news_article
original_title: Microsoft WSUS attacks hit 'multiple' orgs, Google warns - theregister.com
publishedAt: '2025-10-27T23:54:00+00:00'
slug: microsoft-wsus-attacks-hit-multiple-orgs-google-wa
source:
  emoji: 📰
  id: null
  name: Theregister.com
title: Kritická zranitelnost WSUS pod aktivním útokem, varuje Google
url: https://www.theregister.com/2025/10/27/microsoft_wsus_attacks_multiple_orgs/
urlToImage: https://regmedia.co.uk/2024/04/19/shutterstock_bell.jpg
urlToImageBackup: https://regmedia.co.uk/2024/04/19/shutterstock_bell.jpg
---

## Souhrn

Kritická zranitelnost ve Windows Server Update Services (WSUS) označená jako CVE-2025-59287 je aktivně zneužívána útočníky k útokům na organizace. Google Threat Intelligence Group potvrdil útoky nové skupiny UNC6512 na více obětí, přičemž Microsoft vydal nouzovou záplatu a americká agentura CISA přidala chybu do katalogu známých zneužívaných zranitelností.

## Klíčové body

- Zranitelnost CVE-2025-59287 umožňuje neautentizovaným útočníkům vzdálené spuštění kódu na zranitelných serverech s Windows Server 2012 až 2025
- Google Threat Intelligence Group identifikoval novou skupinu útočníků UNC6512, která aktivně zneužívá tuto chybu k útokům na více organizací
- Microsoft vydal nouzovou záplatu, ale ve svém bezpečnostním doporučení stále neuvádí aktivní zneužívání v reálném prostředí
- Útočníci po získání přístupu provádějí průzkum kompromitovaných systémů a exfiltrují data
- Detekováno přibližně 100 000 pokusů o zneužití této zranitelnosti

## Podrobnosti

Zranitelnost CVE-2025-59287 postihuje Windows Server Update Services, službu Microsoftu pro centralizovanou správu aktualizací Windows v podnikových sítích. Problém spočívá v nebezpečné deserializaci nedůvěryhodných dat, což útočníkům umožňuje spustit libovolný kód na zranitelných systémech bez nutnosti autentizace. Postiženy jsou všechny verze Windows Server od roku 2012 do 2025, pokud mají aktivovanou roli WSUS.

Google Threat Intelligence Group ve svém vyjádření pro The Register potvrdil, že sleduje novou skupinu útočníků označenou jako UNC6512, která tuto zranitelnost aktivně zneužívá. Po získání počátečního přístupu útočníci spouštějí sérii příkazů pro průzkum kompromitovaného hostitele a celého prostředí. Bezpečnostní výzkumníci také zaznamenali exfiltraci dat z napadených systémů.

Microsoft sice vydal nouzovou záplatu a hodnotí zranitelnost jako "pravděpodobně zneužitelnou", ale ve svém oficiálním bezpečnostním doporučení stále uvádí, že chyba nebyla veřejně odhalena ani zneužita. Společnost odmítla odpovědět na dotazy The Register ohledně hlášených útoků s odůvodněním, že bezpečnostní doporučení obvykle neaktualizuje po vydání, pokud původní informace nebyly nepřesné.

Americká agentura pro kybernetickou bezpečnost CISA přidala CVE-2025-59287 do svého katalogu Known Exploited Vulnerabilities, což signalizuje vážnost situace. Bezpečnostní výzkumníci zaznamenali přibližně 100 000 pokusů o zneužití této zranitelnosti, což naznačuje rozsáhlou kampaň.

## Proč je to důležité

Tato situace ilustruje kritický problém v podnikové bezpečnosti. WSUS je klíčová služba pro správu aktualizací v podnikových prostředích, což z ní činí atraktivní cíl pro útočníky. Kompromitace WSUS serveru může útočníkům poskytnout rozsáhlý přístup k celé podnikové síti a umožnit distribuci škodlivého softwaru maskovaného jako legitimní aktualizace.

Nesoulad mezi veřejnými varováními bezpečnostních výzkumníků a oficiálním stanoviskem Microsoftu je znepokojující. Zatímco Google a další bezpečnostní týmy hlásí aktivní útoky na více organizací, Microsoft ve svém doporučení tuto skutečnost neuvádí, což může vést k podcenění rizika ze strany správců systémů.

Organizace používající WSUS by měly okamžitě aplikovat dostupnou záplatu a provést audit svých systémů na případné známky kompromitace. Tato zranitelnost představuje vážné riziko zejména pro větší podniky a vládní instituce, které WSUS běžně využívají pro správu tisíců koncových stanic.

---

[Číst původní článek](https://www.theregister.com/2025/10/27/microsoft_wsus_attacks_multiple_orgs/)

**Zdroj:** 📰 Theregister.com
