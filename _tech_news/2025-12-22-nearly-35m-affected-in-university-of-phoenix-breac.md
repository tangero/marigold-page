---
author: Marisa Aigen
category: datový únik
companies:
- Oracle
date: '2025-12-22 23:43:27'
description: Univerzita Phoenix potvrdila datový únik postihující téměř 3,5 milionu
  současných a bývalých studentů, zaměstnanců, pedagogů a dodavatelů. Útok využil
  zero-day zranitelnost v systému Oracle E-Business Suite, kterou zneužila ransomware
  skupina Clop v srpnu 2025.
importance: 5
layout: tech_news_article
original_title: Nearly 3.5M affected in University of Phoenix breach tied to Clop-linked
  Oracle EBS exploit
publishedAt: '2025-12-22T23:43:27+00:00'
slug: nearly-35m-affected-in-university-of-phoenix-breac
source:
  emoji: 📰
  id: null
  name: SiliconANGLE News
title: Téměř 3,5 milionu postiženo v datovém úniku University of Phoenix spojeném
  s exploit Oracle EBS od Clop
url: https://siliconangle.com/2025/12/22/nearly-3-5m-affected-university-phoenix-breach-tied-clop-linked-oracle-ebs-zero-day-exploit/
urlToImage: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/12/universityofphoenix.png
urlToImageBackup: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/12/universityofphoenix.png
---

## Souhrn
Univerzita Phoenix, jedna z největších soukromých univerzit v USA zabývající se převážně online vzděláváním, potvrdila datový únik postihující téměř 3,5 milionu osob včetně studentů, zaměstnanců a dodavatelů. Útok provedla kyberzločinecká skupina Clop prostřednictvím dříve neznámé zranitelnosti v systému Oracle E-Business Suite (EBS), což je enterprise software pro řízení podnikových zdrojů jako finance, HR a dodavatelské řetězce. Přístup útočníků byl detekován 21. listopadu 2025 po zveřejnění na dark webu, přestože krádež dat proběhla již v srpnu.

## Klíčové body
- **Počet postižených**: Téměř 3,5 milionu osob, včetně plných jmen, kontaktních údajů, dat narození, čísel sociálního zabezpečení (SSN) a bankovních údajů (čísla účtů a směrovací čísla).
- **Časový rámec**: Neoprávněný přístup od srpna 2025, exploit aktivní od září, detekce 21. listopadu po zveřejnění na leak site Clop.
- **Cílový systém**: Zero-day zranitelnost v Oracle EBS, umožňující laterální pohyb do systémů s citlivými daty.
- **Skupina Clop**: Specializuje se na velké datové extorce bez šifrování systémů, zaměřuje se na zero-day v enterprise software.
- **Další oběti**: Clop exploitoval stejnou zranitelnost u více firem, což vedlo k varovným e-mailům v listopadu.

## Podrobnosti
Útok na University of Phoenix byl součástí širší kampaně skupiny Clop, která letos cílí na zero-day zranitelnosti v široce používaných enterprise systémech. Oracle E-Business Suite slouží k integraci podnikových procesů jako účetnictví, mzdy, nákupy a reporting, což z něj činí atraktivní cíl pro útočníky hledající finanční a osobní data. Podle zprávy Bleeping Computer útočníci získali přístup v srpnu 2025 a pohybovali se laterálně napříč sítí, aby exfiltrovali data bez šifrování systémů – typický přístup Clop k maximalizaci extorce.

První veřejné zmínky o exploitu Oracle EBS se objevily na začátku listopadu, kdy manažeři více firem obdrželi e-maily s tvrzením o ukradených datech. Clop následně zveřejnil University of Phoenix na svém dark web leak site, což vedlo k oficiálnímu potvrzení. Univerzita sice Clop přímo neobvinila, ale shoda s veřejnými tvrzeními skupiny a charakter dat (SSN, bankovní údaje) jasně ukazuje na jejich zapojení. Paul Bischoff, expert na soukromí z Comparitech, uvedl, že Clop tento rok eskaloval útoky na zero-day v enterprise software, což ohrožuje tisíce organizací.

Tento incident navazuje na předchozí kampaně Clop, jako exploit MOVEit v roce 2023, kde ukradli data milionům. Oracle zatím zranitelnost neoznámil jako opravenou, což zvyšuje riziko pro další uživatele EBS. Postižení studenti a zaměstnanci čelí riziku krádeže identity, podvodů s bankovními účty nebo daňových útoků, protože SSN slouží v USA k identifikaci pro sociální zabezpečení, daně i finance.

## Proč je to důležité
Tento útok podtrhuje zranitelnost enterprise systémů jako Oracle EBS vůči zero-day exploitům, které umožňují rychlou exfiltraci masivních objemů dat bez okamžité detekce. Pro průmysl znamená varování pro tisíce firem a institucí závislých na EBS – nutnost okamžitého auditu, segmentace sítí a rychlých patchů. Clopova strategie extorce bez ransomware šifrování zvyšuje tlak na oběti k výplatám, protože data se rychle objeví na dark webu. Pro uživatele to přináší dlouhodobé riziko: monitorování úvěrů, změna hesel a ochrana proti phishingu. V širším kontextu IT bezpečnosti to zdůrazňuje potřebu zero-trust architektur a lepšího sdílení informací o hrozbách mezi vendory jako Oracle a uživateli, aby se zabránilo dalším masivním únikům.

---

[Číst původní článek](https://siliconangle.com/2025/12/22/nearly-3-5m-affected-university-phoenix-breach-tied-clop-linked-oracle-ebs-zero-day-exploit/)

**Zdroj:** 📰 SiliconANGLE News
