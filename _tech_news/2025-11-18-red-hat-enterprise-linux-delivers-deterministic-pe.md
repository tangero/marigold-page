---
author: Marisa Aigen
category: průmyslová automatiz
companies:
- Red Hat
date: '2025-11-18 00:00:00'
description: Red Hat potvrdil, že jeho operační systém Red Hat Enterprise Linux (RHEL)
  poskytuje deterministický výkon nezbytný pro průmyslové aplikace využívající časově
  citlivé sítě (TSN).
importance: 3
layout: tech_news_article
original_title: Red Hat Enterprise Linux delivers deterministic performance for time-sensitive
  networking
publishedAt: '2025-11-18T00:00:00+00:00'
slug: red-hat-enterprise-linux-delivers-deterministic-pe
source:
  emoji: 📰
  id: null
  name: Redhat.com
title: Red Hat Enterprise Linux zajišťuje deterministický výkon pro časově citlivé
  sítě
url: https://www.redhat.com/en/blog/red-hat-enterprise-linux-delivers-deterministic-performance-industrial-tsn
urlToImage: https://www.redhat.com/themes/custom/rhdc/img/red-hat-social-share.jpg
urlToImageBackup: https://www.redhat.com/themes/custom/rhdc/img/red-hat-social-share.jpg
---

## Souhrn
Red Hat Enterprise Linux (RHEL) nyní oficiálně podporuje deterministický výkon potřebný pro časově citlivé sítě (Time-Sensitive Networking, TSN), což je klíčové pro průmyslovou automatizaci. Společně s Intelem byla provedena technická validace, která prokázala schopnost RHELu zajistit předvídatelné zpracování síťových paketů i za zátěže.

## Klíčové body
- RHEL využívá real-time kernel s deterministickým plánovačem pro zajištění předvídatelného výkonu.
- Systém řeší problémy jako hardwarové přerušení, výměna mezipaměti a zátěž aplikacemi (např. AI nebo video).
- Validace byla provedena ve spolupráci s Intelem na reálném průmyslovém scénáři.
- Red Hat Device Edge rozšiřuje možnosti nasazení na periferii sítě (edge computing).
- Determinismus je zajištěn nejen na úrovni sítě, ale i na úrovni operačního systému.

## Podrobnosti
Časově citlivé sítě (TSN) jsou rozšířením standardu Ethernet, které zavádí záruky na doručení dat v přesně definovaném časovém okně – nezbytné pro průmyslové řídicí systémy, robotiku nebo pohybové řízení. Avšak samotná síť nestačí: pokud operační systém na koncovém zařízení (např. průmyslovém počítači nebo edge gateway) nezvládá předvídatelně zpracovávat a odesílat pakety, celý TSN řetězec selže. Red Hat proto nasadil real-time kernel, který minimalizuje latenci a jitter tím, že upřednostňuje kritické úlohy před běžnými procesy. Systém řídí zpracování přerušení, zamykání zdrojů a přepínání kontextu tak, aby vysokoprioritní úlohy běžely v pevně daných časových mezích. Validace s Intelem ukázala, že RHEL dokáže udržet deterministické chování i při běhu náročných aplikací, jako je AI inference nebo správa videa – běžné scénáře v moderních továrnách.

## Proč je to důležité
Tento krok umožňuje průmyslovým firmám využívat otevřený, standardizovaný operační systém místo proprietárních řešení. Red Hat tím posiluje konvergenci IT (informační technologie) a OT (operační technologie), což je dlouhodobý cíl digitalizace výroby. Deterministický Linux na periferii sítě také usnadňuje integraci AI a pokročilé analýzy dat přímo v továrně, bez nutnosti odesílat data do cloudu. Pro průmysl to znamená vyšší flexibilitu, snížení nákladů na licencování a lepší dlouhodobou udržitelnost systémů.

---

[Číst původní článek](https://www.redhat.com/en/blog/red-hat-enterprise-linux-delivers-deterministic-performance-industrial-tsn)

**Zdroj:** 📰 Redhat.com
