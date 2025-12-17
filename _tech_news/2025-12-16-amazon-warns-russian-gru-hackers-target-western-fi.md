---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Amazon
date: '2025-12-16 12:15:00'
description: Výzkumníci Amazonu považují tuto kampaň za součást větší operace vedené
  ruskou vojenskou zpravodajskou službou GRU. Skupina změnila taktiku z exploitů zranitelností
  na útoky na chybně nastavená síťová hraniční zařízení zákazníků.
importance: 5
layout: tech_news_article
original_title: Amazon Warns Russian GRU Hackers Target Western Firms via Edge Devices
publishedAt: '2025-12-16T12:15:00+00:00'
slug: amazon-warns-russian-gru-hackers-target-western-fi
source:
  emoji: 📰
  id: null
  name: Infosecurity Magazine
title: 'Amazon varuje: Hackeři z ruské GRU cílí na západní firmy přes špatně nakonfigurovaná
  hraniční zařízení'
url: https://www.infosecurity-magazine.com/news/amazon-russian-gru-hackers-target/
urlToImage: https://assets.infosecurity-magazine.com/webpage/og/373d80ad-16a6-487c-be6e-b762c135a612.jpg
urlToImageBackup: https://assets.infosecurity-magazine.com/webpage/og/373d80ad-16a6-487c-be6e-b762c135a612.jpg
---

## Souhrn
Amazon Threat Intelligence identifikoval dlouhodobou škodlivou kampaň, kterou s vysokou jistotou připisuje ruské vojenské zpravodajské službě GRU. Skupina, dosud nepojmenovaná, se v roce 2025 odklonila od exploitů známých zranitelností a zaměřila se na kompromitaci špatně nakonfigurovaných hraničních zařízení sítí západních organizací. Cíle zahrnují kritickou infrastrukturu v energetice a cloudu v Severní Americe a Evropě.

## Klíčové body
- Připisováno GRU s vysokou jistotou; kampaň probíhá od roku 2021 do 2025.
- Dřívější taktiky: exploity v WatchGuard (CVE-2022-26318), Confluence (CVE-2021-26084, CVE-2023-22518) a Veeam (CVE-2023-27532).
- Nová taktika: útoky na misconfigurovaná hraniční zařízení jako routry, VPN koncentrátory, síťové manažerské zařízení, wiki platformy a cloudové systémy pro správu projektů.
- Chyby jsou na straně zákazníků, ne v infrastruktuře AWS.
- Cíle: energetické firmy, poskytovatelé kritické infrastruktury a organizace s cloudovou síťovou infrastrukturou.

## Podrobnosti
Výzkumníci Amazon Threat Intelligence popsali kampaň v zprávě z 15. prosince 2024. Skupina působí globálně a soustředila se na energetický sektor v západních zemích, poskytovatele kritické infrastruktury v Severní Americe a Evropě oraz organizace využívající cloudovou síťovou infrastrukturu. Mezi typickými cíli patří podnikové routry a směrovací zařízení, které slouží k propojení interní sítě s internetem; VPN koncentrátory a brány pro dálkový přístup, umožňující bezpečné připojení zaměstnanců; síťové manažerské spotřebiče pro monitorování a konfiguraci sítí; platformy pro spolupráci a wiki, jako Confluence pro sdílení znalostí v týmech; a cloudové systémy pro správu projektů, například Jira nebo podobné nástroje pro plánování úkolů.

Do roku 2024 skupina využívala exploity známých zranitelností: v letech 2021–2022 CVE-2022-26318 v zařízeních WatchGuard, což je firewall a VPN řešení pro ochranu sítí; v letech 2022–2023 CVE-2021-26084 a CVE-2023-22518 v Atlassian Confluence, systému pro tvorbu wiki stránek a týmovou spolupráci; a v roce 2024 CVE-2023-27532 ve Veeam Backup & Replication, softwaru pro zálohování a obnovu dat v hybridních prostředích. Tyto exploity umožňovaly získání počátečního přístupu k systémům.

V roce 2025 došlo k taktickému posunu: skupina nyní preferuje hledání a využívání chyb v konfiguraci hraničních zařízení zákazníků, včetně těch hostovaných na AWS. Amazon zdůrazňuje, že problémy nejsou v cloudu AWS, ale v nastavení zákaznických zařízení, jako otevřené porty, slabé hesla nebo nepovolené autentizace. Tento přístup umožňuje stejný výsledek – trvalý přístup k sítím kritické infrastruktury – bez nutnosti čekat na nové exploity. Amazon pozoroval tyto aktivity v období 2021–2025 a varuje, že kampaň je součástí širší operace GRU, ke které se váže několik kybernetických skupin.

## Proč je to důležité
Tento posun taktik znamená vyšší riziko pro organizace, protože konfigurace hraničních zařízení často podléhají lidským chybám a nejsou tak pečlivě monitorovány jako softwareové aktualizace. Pro energetické firmy a poskytovatele infrastruktury to ohrožuje bezpečnost sítí, což může vést k špionáži, sabotáži nebo přerušení dodávek. V širším kontextu posiluje důkazy o ruské státní kyberoperacích proti Západu, podobně jako případy NotPetya nebo SolarWinds. Firmy by měly okamžitě provést audit konfigurací edge zařízení, implementovat princip nejnižších práv a používat nástroje jako AWS GuardDuty pro detekci anomálií. Pro průmysl to podtrhuje nutnost posílit obranu proti APT skupinám, kde GRU hraje klíčovou roli v hybridních konfliktech.

---

[Číst původní článek](https://www.infosecurity-magazine.com/news/amazon-russian-gru-hackers-target/)

**Zdroj:** 📰 Infosecurity Magazine
