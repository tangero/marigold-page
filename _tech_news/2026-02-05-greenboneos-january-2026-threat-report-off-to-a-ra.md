---
author: Marisa Aigen
category: kybernetika
date: '2026-02-05 07:04:27'
description: Rok 2026 začal výrazným nárůstem kritických zranitelností v široce nasazeném
  softwaru. Podle zprávy World Economic Forum 58 % manažerů vidí zvýšené riziko jejich
  exploitace. Doporučuje se pravidelné skenování infrastruktur pro detekci a prioritizaci
  oprav.
importance: 4
layout: tech_news_article
original_title: 'GreenboneOS: January 2026 Threat Report: Off to a Raucous Start'
publishedAt: '2026-02-05T07:04:27+00:00'
slug: greenboneos-january-2026-threat-report-off-to-a-ra
source:
  emoji: 📰
  id: null
  name: Greenbone.net
title: 'GreenboneOS: Zpráva o hrozbách za leden 2026: Bouřlivý začátek'
url: https://www.greenbone.net/en/blog/january-2026-threat-report-off-to-a-raucous-start/
urlToImage: https://www.greenbone.net/wp-content/uploads/evolving-cyber-risk-concerns.png
urlToImageBackup: https://www.greenbone.net/wp-content/uploads/evolving-cyber-risk-concerns.png
---

### Souhrn
Zpráva GreenboneOS o kybernetických hrozbách za leden 2026 zdůrazňuje vysoký počet kritických zranitelností v populárním softwaru. Podle průzkumu World Economic Forum Global Cybersecurity Outlook 2026 považuje 58 % respondentů riziko exploitace těchto zranitelností za vyšší než v předchozím roce. Firma Greenbone Networks, která vyvíjí open source nástroje pro detekci zranitelností na bázi OpenVAS, doporučuje časté skenování s jejich řešením OPENVAS BASIC, které nabízí dvoutýdenní zkušební verzi podnikového feedu OPENVAS ENTERPRISE FEED.

### Klíčové body
- **Nárůst kritických zranitelností**: Počet CVE s maximální závažností v široce používaném softwaru je podle zprávy alarmující.
- **WEF průzkum**: 58 % top manažerů očekává vyšší rizika exploitace; hlavní obavy zahrnují podvody, ransomware a narušení dodavatelských řetězců, přičemž zranitelnosti jsou třetím největším vektorem útoku.
- **Aktivně exploitovaná zranitelnost**: CVE-2025-37164 v HPE OneView (CVSS 9.8, EPSS ≥ 99. percentilu) byla zveřejněna v prosinci 2025 a zařazena do CISA Known Exploited Vulnerabilities.
- **Doporučení**: Organizace s vyšší kybernetickou odolností považují exploitaci zranitelností za druhou největší hrozbu.
- **Šetření**: Zapojilo se 873 respondentů z 99 zemí, včetně C-level manažerů a expertů z veřejného sektoru.

### Podrobnosti
GreenboneOS je operační systém určený pro správu zranitelností, vyvinutý společností Greenbone Networks, která se specializuje na open source řešení pro skenování sítí a detekci CVE. Zpráva analyzuje vývoj hrozeb na začátku roku 2026 a spojuje jej s čerstvě zveřejněnou publikací World Economic Forum Global Cybersecurity Outlook 2026. Tento výroční průzkum mapuje obavy 873 lídrů z oblasti kybernetické bezpečnosti a byznysu z 99 zemí, včetně akademiků, zástupců občanské společnosti a veřejného sektoru.

Klíčové zjištění ukazuje posun v prioritách: zatímco v roce 2025 dominovaly obavy z AI a phishingu, v roce 2026 se na popředí objevují podvody, ransomware a narušení dodavatelských řetězců jako největší dopady. Mezi vektory útoku vynikají AI, phishing a právě softwareové zranitelnosti. Organizace s vysokou kybernetickou odolností řadí exploitaci zranitelností na druhé místo hrozeb, zatímco ty se střední nebo nízkou odolností je hodnotí třetí. Grafy ve zprávě (Obrázek 1 a 2) ilustrují tento vývoj mezi roky 2025 a 2026.

Jako příklad vysokorizikové zranitelnosti zpráva uvádí CVE-2025-37164 v HPE OneView, softwaru pro centralizovanou správu Hewlett Packard Enterprise infrastruktur, jako jsou servery, úložiště a sítě v datových centrech. Tato chyba s CVSS skóre 9.8 (kritická závažnost) a EPSS pravděpodobností exploitace v 99. percentilu byla publikována v polovině prosince 2025 a rychle přidána do seznamu CISA Known Exploited Vulnerabilities. To znamená, že útočníci ji aktivně využívají v divokém prostředí, což vyžaduje okamžitou instalaci záplat u všech nasazených instancí. HPE OneView slouží k monitoringu, konfiguraci a aktualizaci hardware v enterprise prostředích, takže exploit může vést k úplné kompromitaci infrastruktury.

Zpráva zdůrazňuje nutnost pravidelného skenování celé infrastruktury pro identifikaci nových hrozeb a prioritizaci oprav podle dopadu na provoz, soulad s předpisy o ochraně dat (jako GDPR) a další compliance požadavky. Greenbone nabízí OPENVAS BASIC zdarma pro základní skenování, s možností upgradu na placený feed s aktuálními daty o tisících CVE.

### Proč je to důležité
Tato zpráva signalizuje zhoršující se situaci v kybernetické bezpečnosti na úsvitu 2026, kde rostoucí počet kritických zranitelností v legacy i novém softwaru zvyšuje rizika pro podniky. Pro IT týmy to znamená nutnost integrovat automatizované skenování do CI/CD pipeline a monitoringu, aby minimalizovali expozici. V širším kontextu to podtrhuje závislost na dodavatelských řetězcích – exploit jako v HPE OneView může ovlivnit tisíce firem závislých na HPE hardware. Pro průmysl to posiluje argument za investice do vulnerability managementu, jako je Greenbone, a zdůrazňuje, proč organizace s lepší odolností detekují rizika dříve. Bez okamžitých opatření hrozí eskalace ransomwarových útoků a narušení provozu.

---

[Číst původní článek](https://www.greenbone.net/en/blog/january-2026-threat-report-off-to-a-raucous-start/)

**Zdroj:** 📰 Greenbone.net
