---
author: Marisa Aigen
category: kybernetika
companies:
- MongoDB
date: '2025-12-29 22:57:09'
description: Kybernetické bezpečnostní úřady v USA a Austrálii upozorňují na aktivní
  exploitaci kritické zranitelnosti CVE-2025-14847 v MongoDB, která umožňuje útočníkům
  získat citlivé údaje z paměti databáze. Tato chyba ohrožuje tisíce veřejně dostupných
  instancí a CISA nařizuje federálním agenturám patchování do 19. ledna.
importance: 5
layout: tech_news_article
original_title: US and Australian agencies warn MongoBleed vulnerability in MongoDB
  is under active exploitation
publishedAt: '2025-12-29T22:57:09+00:00'
slug: us-and-australian-agencies-warn-mongobleed-vulnera
source:
  emoji: 📰
  id: null
  name: SiliconANGLE News
title: 'Americké a australské agentury varují: Zranitelnost MongoBleed v MongoDB je
  aktivně využívána'
url: https://siliconangle.com/2025/12/29/us-australian-agencies-warn-mongobleed-vulnerability-mongodb-active-exploitation/
urlToImage: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/12/mongobleed.png
urlToImageBackup: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/12/mongobleed.png
---

## Souhrn
Americké a australské bezpečnostní agentury varují před aktivním využíváním zranitelnosti MongoBleed (CVE-2025-14847) v MongoDB Serveru. Tato chyba v zpracování zlib-komprimovaných síťových zpráv umožňuje neautentizovaným útočníkům získat fragmenty neinicilizované paměti, včetně přihlašovacích údajů a session klíčů. Agentura CISA nařizuje všem federálním civilním institucím instalaci záplat do 19. ledna, zatímco Australian Signals Directorate hlásí globální exploitaci.

## Klíčové body
- **CVE-2025-14847 (MongoBleed)**: Chyba v dekompresní logice zlib, která vrací neinicilizovanou heap paměť klientům před autentizací.
- **Aktivní útoky**: Proof-of-concept kód zveřejněn na GitHubu 25. prosince 2025, následně detekovány automatizované skenování a exploitace.
- **Rozsah ohrožení**: Přibližně 87 000 MongoDB instancí vystavených na internetu, mnohé s výchozí zlib kompresí.
- **Mandáty**: CISA vyžaduje patchování federálních systémů do 19. ledna; Australian Signals Directorate potvrzuje globální aktivity.
- **Dopady**: Možný únik přihlašovacích údajů, session klíčů, interního stavu a dalších citlivých dat.

## Podrobnosti
MongoDB je open-source NoSQL databázový systém, který slouží k ukládání a správě dat v podobě flexibilních JSON-like dokumentů. Používá se pro aplikace vyžadující vysoký výkon a škálovatelnost, jako jsou webové platformy, big data analýzy nebo mobilní backendy. Zranitelnost MongoBleed pochází z nesprávného zpracování délkových parametrů v zlib-komprimovaných síťových zprávách. Při dekompresi dochází k chybě, která způsobí, že server pošle klientovi části neinicilizované paměti z heapu – oblasti paměti dynamicky alokované pro dočasná data – ještě před jakoukoli autentizací.

Útočník s přístupem k síťovému portu MongoDB (výchozí port 27017) může opakovat zprávy a postupně sbírat úniky paměti. Tyto fragmenty mohou obsahovat citlivé informace, jako jsou hesla, session klíče, interní konfigurace nebo dokonce části databáze. Bezpečnostní firma Tenable Holdings Inc., která se specializuje na monitorování sítí a detekci zranitelností, zveřejnila proof-of-concept exploit 25. prosince 2025 na GitHubu. Během několika dní byly detekovány automatizované skenovače hledající zranitelné instance a pokusy o exploitaci.

Skenovací služby odhalily kolem 87 000 MongoDB nasazení přístupných z internetu, z toho významná část s povolenou zlib kompresí, což je výchozí nastavení v mnoha konfiguracích. Cloudové prostředí, jako AWS nebo Azure, vykazují podobné trendy – mnoho instancí zůstává neupravených kvůli přehlížení bezpečnostních doporučení. CISA, americká agentura pro kybernetickou bezpečnost infrastruktury, označila chybu za „improper handling of length parameter inconsistency" a zařadila ji do svého Known Exploited Vulnerabilities Catalogu, což spouští povinné patchování pro federální entity. Australian Signals Directorate (ASD) potvrdila aktivní globální exploitaci a doporučuje okamžité opatření, včetně omezení síťového přístupu.

Patch je dostupný od MongoDB Inc. pro všechny podporované verze; doporučuje se také vypnutí zlib komprese a omezení přístupu na důvěrné IP adresy. Administrátoři by měli provést audit nasazení pomocí nástrojů jako Shodan nebo nmap pro identifikaci vystavených portů.

## Proč je to důležité
Tato zranitelnost představuje bezpečnostní krizi pro organizace závislé na MongoDB, který pohání miliony aplikací po celém světě. S 87 000 vystavenými instancemi hrozí masivní úniky dat, což by mohlo vést k kompromitaci celých systémů – od firemních databází po cloudové služby. Výchozí konfigurace s otevřenými porty a zlib ukazuje na dlouhodobý problém v praxi nasazení databází: mnoho správců podceňuje síťovou expozici. V širším kontextu kybernetické bezpečnosti to podtrhuje nutnost okamžitého patchování zero-day exploitů, zejména když státní agentury vydávají mandáty. Pro průmysl znamená riziko eskalace útoků na supply chain, kde kompromitovaná databáze může sloužit jako vstupní bod pro ransomware nebo špionáž. Organizace by měli priorizovat databázovou bezpečnost, včetně firewallech a autentizace, aby minimalizovaly budoucí hrozby.

---

[Číst původní článek](https://siliconangle.com/2025/12/29/us-australian-agencies-warn-mongobleed-vulnerability-mongodb-active-exploitation/)

**Zdroj:** 📰 SiliconANGLE News
