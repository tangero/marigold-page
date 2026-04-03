---

author: Marisa Aigen
category: kybernetika
companies:
- CarGurus
date: '2026-02-20 00:20:00'
description: Online tržiště automobilů CarGurus se stalo údajnou obětí hackingové
  skupiny ShinyHunters. Hackeři tvrdí, že prostřednictvím vishing útoků získali 1,7
  milionu záznamů s osobními údaji a interními korporátními daty.
importance: 5
original_title: Major CarGurus data breach reportedly sees 1.7 million corporate records
  stolen
publishedAt: '2026-02-20T00:20:00+00:00'
slug: major-cargurus-data-breach-reportedly-sees-17-mill
source:
  emoji: 📰
  id: techradar
  name: TechRadar
title: 'Velký únik dat z CarGurus: Údajně ukradeno 1,7 milionu korporátních záznamů'
source_url: https://www.techradar.com/pro/security/major-cargurus-data-breach-reportedly-sees-1-7-million-corporate-records-stolen
urlToImage: https://cdn.mos.cms.futurecdn.net/ThNyuwnA55tfcixfqWcEcA-970-80.jpg
urlToImageBackup: https://cdn.mos.cms.futurecdn.net/ThNyuwnA55tfcixfqWcEcA-970-80.jpg
---

## Souhrn
Online platforma pro nákup a prodej ojetých automobilů CarGurus byla údajně napadena hackingovou skupinou ShinyHunters. Skupina oznámila, že ukradla 1,7 milionu záznamů obsahujících osobně identifikovatelné informace (PII) a další interní korporátní data. CarGurus zatím na tyto obvinění nereagovala a na svých stránkách žádnou zmínku o incidentu neuvádí.

## Klíčové body
- ShinyHunters dali společnosti ultimátní lhůtu do 20. února 2026, jinak údaje zveřejní na dark webu spolu s dalšími digitálními problémy.
- Útok byl proveden vishingem, tedy hlasovým phishingem, který vedl k přístupu k jedinému přihlašovacímu systému (SSO) jako Okta, Entra ID nebo Google Workspace.
- CarGurus je patnáctou známou obětí této vlny útoků od ShinyHunters.
- Zkradená data zahrnují PII uživatelů a interní firemní informace, což ohrožuje bezpečnost zaměstnanců i zákazníků.
- Odborníci z Google a Mandiant popsali taktiku jako kombinaci vishingu s přizpůsobenou infrastrukturou pro rychlé kompromitování systémů.

## Podrobnosti
CarGurus je americká online platforma specializující se na srovnávání cen ojetých vozidel, recenze a nástroje pro kupující i prodejce automobilů. Podle oznámení na data leak stránce ShinyHunters hackeři použili vishing – formu phishingu, při které útočníci telefonicky kontaktují zaměstnance, vydávají se za technickou podporu nebo kolegy a přesvědčí je k sdílení přihlašovacích údajů nebo k instalaci škodlivého softwaru. Tento přístup umožnil kompromitovat SSO dashboardy, což jsou centrální systémy pro jednotné přihlašování do firemních aplikací, jako je Okta (slouží k autentizaci uživatelů v cloudu), Microsoft Entra ID (nástupce Azure AD pro správu identit) nebo Google Workspace (balík pro firemní spolupráci v cloudu).

ShinyHunters je notorická hackingová skupina, která v posledních letech zaútočila na desítky firem, včetně Ticketmasteru, Microsoftu nebo Coinbase. Jejich metoda je efektivní díky sociálnímu inženýrství: telefonátem získají počáteční přístup a poté nasadí vlastní infrastrukturu pro eskalaci privilegií a exfiltraci dat. Podle zprávy od expertů Google a Mandiantu, kterou cituje původní článek, útoky probíhají rychle – od telefonátu k plnému přístupu trvá často jen hodiny. V případě CarGurus skupina varovala: „Toto je konečné varování, kontaktujte nás do 20. února 2026, než údaje zveřejníme spolu s několika otravnými digitálními problémy.“ Společnost zatím mlčí, což je typické pro počáteční fázi incidentu, kdy firmy provádějí interní šetření a koordinují s úřady jako FBI nebo CISA.

Tento incident navazuje na vlnu podobných útoků, kde ShinyHunters kompromitovali přes tucet organizací stejným způsobem. Vishing obchází tradiční bezpečnostní vrstvy, jako jsou firewall nebo antiviry, protože spoléhá na lidský faktor. Pro CarGurus to znamená potenciální riziko pro data tisíců zaměstnanců a možná i zákazníků, pokud PII zahrnuje jména, adresy nebo platební údaje z platformy.

## Proč je to důležité
Tento únik podtrhuje zranitelnost SSO systémů vůči sociálnímu inženýrství, což je trend v kybernetických útocích v roce 2024. Pro průmysl to znamená nutnost zesílit školení proti vishingu, zavést hardware klíče pro dvoufázovou autentizaci (2FA) a monitorovat neobvyklé přihlášení. V širším kontextu kyberbezpečnosti ukazuje, jak skupiny jako ShinyHunters skalují útoky na masivní úniky dat, což vede k miliardovým škodám – od reputačních ztrát po žaloby podle zákonů jako GDPR nebo CCPA. Pro uživatele CarGurus to představuje riziko identity theft; doporučuji měnit hesla a sledovat kreditní zprávy. Jako expert v IT bezpečnosti vidím, že firmy jako CarGurus musí přejít od reaktivních opatření k proaktivní detekci, jinak se stanou součástí dlouhodobé vlny útoků.

---

[Číst původní článek](https://www.techradar.com/pro/security/major-cargurus-data-breach-reportedly-sees-1-7-million-corporate-records-stolen)

**Zdroj:** 📰 TechRadar
