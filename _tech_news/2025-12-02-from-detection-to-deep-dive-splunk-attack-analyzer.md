---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Splunk
- Endace
date: '2025-12-02 08:00:58'
description: Na konferenci GovWare 2025 tým propojil Splunk Attack Analyzer prostřednictvím
  API s nástrojem Endace pro efektivní lov hrozeb. Tato integrace umožnila rychlý
  přechod od vysoké úrovně alertů k detailní forenzní analýze na úrovni paketů.
importance: 3
layout: tech_news_article
original_title: 'From Detection to Deep Dive: Splunk Attack Analyzer and Endace for
  GovWare 2025 Security'
publishedAt: '2025-12-02T08:00:58+00:00'
slug: from-detection-to-deep-dive-splunk-attack-analyzer
source:
  emoji: 📰
  id: null
  name: Cisco.com
title: 'Od detekce k hloubkové analýze: Splunk Attack Analyzer a Endace pro bezpečnost
  na GovWare 2025'
url: https://blogs.cisco.com/security/from-detection-to-deep-dive-splunk-attack-analyzer-and-endace-for-govware-2025-security
urlToImage: https://blogs.cisco.com/gcs/ciscoblogs/1/2025/12/FY26_Q2_from-detection-to-deep-dive-splunk-attack-analyzer-and-endace-for-govware-2025-security_blog_social_card.jpeg
urlToImageBackup: https://blogs.cisco.com/gcs/ciscoblogs/1/2025/12/FY26_Q2_from-detection-to-deep-dive-splunk-attack-analyzer-and-endace-for-govware-2025-security_blog_social_card.jpeg
---

## Souhrn
Na konferenci GovWare 2025 tým zabezpečení využil integraci Splunk Enterprise a Splunk Attack Analyzer s nástrojem Endace k ochraně živé události s tisíci účastníků. Tato kombinace propojila detekci anomálií v síti s hloubkovou analýzou podezřelých souborů a URL, což umožnilo rychlou validaci hrozeb. Klíčovým prvkem bylo automatické odesílání zdrojů z Endace do Splunk Attack Analyzer pro sandboxovou analýzu.

## Klíčové body
- Propojení API Splunk Attack Analyzer s Endace pro automatické odesílání podezřelých souborů a URL z síťového provozu.
- Detekce zip archivu obsahujícího malwarový soubor .exe s hodnocením 100 bodů v Splunk Attack Analyzer.
- Integrace s Cisco Secure Malware Analytics (dříve Threat Grid) pro sandboxovou analýzu, kde 22 z 28 detekcí pocházelo z tohoto nástroje.
- Použití Zeek v Endace pro identifikaci podezřelých zdrojů v reálném čase.
- Aplikace v prostředí s dočasnými sítěmi a mnoha zařízeními na konferenci.

## Podrobnosti
Zabezpečení živé konference jako GovWare 2025 představuje výzvu kvůli rozmanitosti zařízení, dočasným sítím, dočasným přihlašovacím údajům a tisícům uživatelů. Hrozby musí být identifikovány a řešeny v reálném čase, což vyžaduje nejen detekci anomálií, ale i rychlý přechod k forenzní analýze na úrovni síťových paketů. Tým tedy integroval Splunk Enterprise a Splunk Attack Analyzer (SAA), což je nástroj pro sandboxovou analýzu podezřelých objektů, s platformou Endace. Endace je specializovaný nástroj pro pokročilé záznam síťového provozu, který poskytuje viditelnost na úrovni jednotlivých paketů a slouží k dlouhodobému ukládání a reprodukci provozu pro forenzní vyšetřování.

Propojení probíhalo přes robustní API Splunk Attack Analyzer. Endace, využívající open-source framework Zeek pro analýzu síťového provozu, automaticky identifikoval a odeslal podezřelé soubory a URL (nazývané „resources“) do SAA. Z 28 odeslaných souborů byla většina neškodná, ale jeden zip archiv získal skóre 100, což signalizovalo vysokou pravděpodobnost malwaru. Uvnitř archivu byl nalezen spustitelný soubor .exe. Tým tento soubor analyzoval v sandboxu Cisco Secure Malware Analytics (SMA), který je integrován se SAA a dříve fungoval pod názvem Threat Grid. Tento sandbox simuluje reálné prostředí pro bezpečné spuštění a pozorování chování malwaru, přičemž 22 z 28 detekcí pocházelo právě odtud. V záložce „Normalized Forensics“ v SAA byly vidět normalizované forenzní údaje, které pomohly pochopit chování souboru, včetně aplikované detekční logiky.

Tato workflow umožnila týmům rychle pivotovat od alertů v Splunk k packet-level forenzice v Endace, což je klíčové pro validaci hrozeb důkazy z paketů. Splunk Enterprise slouží k agregaci a analýze logů z různých zdrojů, zatímco SAA rozšiřuje schopnosti o dynamickou analýzu v izolovaném prostředí.

## Proč je to důležité
Tato integrace demonstruje praktické využití propojení bezpečnostních nástrojů v prostředích s vysokou zátěží, jako jsou konference nebo velké akce, kde tradiční detekce nestačí. V širším kontextu kyberbezpečnosti posiluje přechod od reaktivního monitoringu k proaktivnímu lovu hrozeb, což snižuje čas na reakci. Pro průmysl znamená, že firmy jako Splunk a Endace nabízejí škálovatelné řešení pro sítě s vysokou diverzitou, kde je packet capture nezbytný pro soudní důkazy. Kriticky lze říci, že i když je integrace efektivní, závislost na sandboxech jako SMA vyžaduje pravidelné aktualizace detekčních podpisů, aby odolala obcházením malwaru. Celkově přispívá k lepší viditelnosti v hybridních sítích, což je aktuální trend v éře rostoucích útoků na veřejné události.

---

[Číst původní článek](https://blogs.cisco.com/security/from-detection-to-deep-dive-splunk-attack-analyzer-and-endace-for-govware-2025-security)

**Zdroj:** 📰 Cisco.com
