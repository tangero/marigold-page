---
author: Marisa Aigen
category: kybernetika
companies:
- Amazon
date: '2025-12-15 23:34:40'
description: Dlouhodobá soustředěnost na západní kritickou infrastrukturu. Hlavní
  správa rozvědky Ruska (GRU) provádí kampaň proti energetice, telekomunikacím a dodavatelům
  technologií, kde kradou přihlašovací údaje a kompromitují špatně nastavená zařízení
  na AWS pro trvalý přístup k sítím.
importance: 5
layout: tech_news_article
original_title: Amazon security boss blames Russia's GRU for years-long energy-sector
  hacks
publishedAt: '2025-12-15T23:34:40+00:00'
slug: amazon-security-boss-blames-russias-gru-for-years-
source:
  emoji: 📰
  id: null
  name: Theregister.com
title: Šéf bezpečnosti Amazonu obviňuje ruskou GRU z dlouhodobých útoků na energetický
  sektor
url: https://www.theregister.com/2025/12/15/amazon_ongoing_gru_campaign/
urlToImage: https://regmedia.co.uk/2022/03/18/russian_bear_shutterstock.jpg
urlToImageBackup: https://regmedia.co.uk/2022/03/18/russian_bear_shutterstock.jpg
---

## Souhrn
Šéf bezpečnosti Amazonu CJ Moses obviňuje ruskou Hlavní správu rozvědky (GRU) z dlouhodobé kyberkampaně, která od roku 2021 cílí na západní kritickou infrastrukturu, především energetický sektor. Útočníci kompromitují špatně nakonfigurovaná síťová zařízení hostovaná na AWS, kradou přihlašovací údaje a získávají trvalý přístup k citlivým sítím. Amazon doporučuje firmám posílit ochranu okrajových zařízení a monitorovat útoky na opětovné použití přihlašovacích údajů.

## Klíčové body
- GRU útočí na energetické firmy, jejich dodavatele, telekomunikační operátory a poskytovatele technologií v Severní Americe a Evropě.
- Cílí na podnikové routry, VPN koncentrátory, brány pro vzdálený přístup a zařízení pro správu sítí.
- Využívají chyby jako CVE-2022-26318 v zařízeních WatchGuard Firebox a XTM, která umožňuje neověřenému uživateli spustit libovolný kód.
- Kradou přístupové údaje z nástrojů pro spolupráci, wiki platforem a cloudových systémů pro správu projektů.
- Kampaň pokračuje dodnes, Amazon Threat Intelligence ji mapuje od roku 2021.

## Podrobnosti
CJ Moses, hlavní bezpečnostní důstojník (CISO) divize Amazon Integrated Security, to uvedl v pondělní zprávě o hrozbách. Podle něj kampaň demonstruje soustředěný zájem Ruska o západní kritickou infrastrukturu, zejména energetiku, s operacemi od roku 2021 po současnost. Amazon Threat Intelligence dohledala útoky na globální infrastrukturu GRU, která začínala exploitací špatně nakonfigurovaných zařízení a zero-day chyb. Konkrétně CVE-2022-26318 v zařízeních WatchGuard Firebox a XTM – firemní firewall a bezpečnostní brány pro ochranu sítí – umožnila neautentizovaným uživatelům provést libovolný kód přes vystavený manažerský přístup. WatchGuard je americký výrobce bezpečnostních zařízení pro malé a střední firmy i podniky.

Útočníci se zaměřují na zařízení na okraji sítě (network edge), jako jsou routry pro směrování provozu, VPN koncentrátory pro šifrovaný vzdálený přístup, brány pro dálkové připojení zaměstnanců a nástroje pro centrální správu sítí. Tyto zařízení často slouží jako první obranná linie a jejich kompromitace umožňuje trvalý přístup hluboko do sítě. GRU navíc útočí na firemní systémy přes platformy pro týmovou spolupráci (jako wiki nebo chaty), kde se ukládají citlivé dokumenty, a cloudové nástroje pro správu projektů, které koordinují vývoj a nasazení infrastruktury. AWS odmítl komentovat počet obětí. Moses varuje před útoky typu credential replay, kdy útočníci opakovaně používají ukradené přihlašovací údaje. Do roku 2026 firmy podle něj musí priorizovat ochranu těchto zařízení a monitorování provozu.

## Proč je to důležité
Tato kampaň od státního aktéra jako GRU představuje dlouhodobou hrozbu pro kritickou infrastrukturu, kde selhání může vést k výpadkům energie nebo sabotážím. V kontextu eskalujících geopolitických napětí, jako válka na Ukrajině, ukazuje, jak Rusko testuje slabiny Západu před možnými konflikty. Pro energetické firmy a dodavatele to znamená nutnost revize konfigurací na AWS a podobných cloudových platformách, kde běží mnoho edge zařízení. Širší IT průmysl musí posílit detekci laterálního pohybu v síti a multifaktorové ověřování. Obvinění od Amazonu, jednoho z největších poskytovatelů cloudu, zvyšuje povědomí o státních hrozbách a může vést k novým regulacím v kyberbezpečnosti EU a USA. Celkově to podtrhuje, že zero-day exploity a misconfigurace zůstávají hlavními vstupními body pro pokročilé persistentní hrozby (APT).

---

[Číst původní článek](https://www.theregister.com/2025/12/15/amazon_ongoing_gru_campaign/)

**Zdroj:** 📰 Theregister.com
