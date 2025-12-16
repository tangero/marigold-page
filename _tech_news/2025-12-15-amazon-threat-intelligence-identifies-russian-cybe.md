---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Amazon
date: '2025-12-15 19:20:36'
description: Amazon Threat Intelligence na konci roku 2025 zveřejňuje poznatky o víceleté
  kampani sponzorované ruským státem, která představuje taktický posun v útocích na
  kritickou infrastrukturu. Hlavním vektorem přístupu se stala špatně nakonfigurovaná
  zařízení na okraji zákaznických sítí, zatímco využívání zranitelností kleslo.
importance: 5
layout: tech_news_article
original_title: Amazon Threat Intelligence identifies Russian cyber threat group targeting
  Western critical infrastructure
publishedAt: '2025-12-15T19:20:36+00:00'
slug: amazon-threat-intelligence-identifies-russian-cybe
source:
  emoji: 📰
  id: null
  name: Amazon.com
title: Amazon Threat Intelligence identifikuje ruskou kybernetickou hrozbu cílenou
  na západní kritickou infrastrukturu
url: https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-russian-cyber-threat-group-targeting-western-critical-infrastructure/
urlToImage: https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/19/security-4868162_1920-1-1260x630.jpg
urlToImageBackup: https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2025/11/19/security-4868162_1920-1-1260x630.jpg
---

## Souhrn
Amazon Threat Intelligence odhalil dlouholetou kampaň ruských kybernetických aktérů spojených s Hlavním spravodajským úřadem Ruska (GRU), která od roku 2021 cílí na západní kritickou infrastrukturu, především energetický sektor. Skupina, identifikovaná s vysokou jistotou jako Sandworm (také APT44 nebo Seashell Blizzard), přešla z exploitů zranitelností na zneužívání špatně nakonfigurovaných zařízení na okraji sítí, což snižuje riziko odhalení a náklady. Tento posun umožňuje stejné výsledky jako získávání přihlašovacích údajů a laterální pohyb v infrastruktuře.

## Klíčové body
- Kampaň probíhá od roku 2021 do současnosti s důrazem na energetiku v západních zemích.
- Primární vektor: špatně nakonfigurovaná zařízení na okraji sítí (network edge devices), např. firewally nebo VPN brány.
- Pokles exploitů zranitelností: CVE-2022-26318 (WatchGuard), CVE-2021-26084 a CVE-2023-22518 (Confluence), CVE-2023-27532 (Veeam).
- Doporučení: zajistit edge zařízení a monitorovat útoky typu credential replay.
- Připojení k GRU na základě překryvů infrastruktury a vzorců v datech Amazonu.

## Podrobnosti
Kampaň začala v letech 2021–2022 využíváním zranitelnosti CVE-2022-26318 v zařízeních WatchGuard, která slouží k ochraně sítí před neoprávněným přístupem. Amazon MadPot, honeypot systém pro sběr dat o útocích, tuto aktivitu zachytil. V následujícím období 2022–2023 došlo k exploitům v Atlassian Confluence (CVE-2021-26084 pro vzdálené spuštění kódu a CVE-2023-22518 pro zneužití autentizace), souběžně s prvním pozorováním útoků na špatně nakonfigurovaná zařízení. V roce 2024 převládl exploit CVE-2023-27532 v Veeam Backup & Replication, nástroji pro zálohování a obnovu dat v podnikových prostředích. Od roku 2025 se zaměření plně přesunulo na edge zařízení, jako jsou routery, firewally nebo VPN servery, která nejsou řádně zabezpečena proti veřejnému přístupu.

Tento taktický posun znamená, že aktéři dosahují stejných cílů – krádeže přihlašovacích údajů, laterální šíření v síti a přístup k online službám – s menším rizikem detekce. Špatná konfigurace umožňuje snadný credential harvesting bez nutnosti složitých exploitů, což snižuje nároky na zdroje. Amazon Threat Intelligence analyzoval překryvy infrastruktury, jako jsou IP adresy a domény, s dříve známými operacemi Sandwormu, což vedlo k vysoké důvěře v připojení k GRU. Cílení je globální, ale soustředěné na Západ, zejména energetiku, kde by úspěšný útok mohl způsobit výpadky.

## Proč je to důležité
Tato kampaň ukazuje adaptabilitu státních aktérů v kyberprostoru, kde se posun od exploitů k sociálně-technickým chybám administrátorů stává standardem. Pro organizace v kritické infrastruktuře to znamená nutnost revize konfigurací edge zařízení – například omezení veřejného přístupu k admin panelům a implementaci multi-faktorové autentizace. Monitorování credential replay útoků, kde se ukradené údaje opakovaně testují, je klíčové pro detekci. V širším kontextu posiluje to tlaky na kyberbezpečnost v energetice, kde už dříve Sandworm způsobil škody, jako útok na ukrajinskou elektrickou síť v roce 2015. Do roku 2026 očekávejte nárůst podobných taktik od jiných APT skupin, což vyžaduje proaktivní obranu na úrovni celého průmyslu.

---

[Číst původní článek](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-russian-cyber-threat-group-targeting-western-critical-infrastructure/)

**Zdroj:** 📰 Amazon.com
