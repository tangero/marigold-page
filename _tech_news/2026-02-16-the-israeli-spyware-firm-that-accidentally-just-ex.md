---
author: Marisa Aigen
category: kyberbezpečnost
date: '2026-02-16 12:00:42'
description: Izraelská společnost vyvíjející špionážní software se nechtěně prozradila
  díky chybě v konfiguraci infrastruktury. Výzkumník odhalil jejich servery a nástroje
  používané pro sledování mobilních zařízení.
importance: 4
layout: tech_news_article
original_title: The Israeli spyware firm that accidentally just exposed itself
publishedAt: '2026-02-16T12:00:42+00:00'
slug: the-israeli-spyware-firm-that-accidentally-just-ex
source:
  emoji: 📰
  id: null
  name: Substack.com
title: Izraelská firma se spywarem, která se omylem právě odhalila
url: https://ahmedeldin.substack.com/p/the-israeli-spyware-firm-that-accidentally
urlToImage: https://substackcdn.com/image/fetch/$s_!-Wnv!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FHA5T-uhboAAD2xT.jpg
urlToImageBackup: https://substackcdn.com/image/fetch/$s_!-Wnv!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FHA5T-uhboAAD2xT.jpg
---

## Souhrn
Izraelská firma zabývající se vývojem spyware pro vládní klienty se omylem odhalila prostřednictvím veřejně dostupných záznamů DNS a otevřených serverů. Výzkumník Ahmed Eldin v článku na Substacku analyzuje, jak chyba v registraci domény a konfiguraci odhalila jejich command and control servery a nástroje pro zero-click infekce. Toto přidává další příklad k izraelskému průmyslu špionážního softwaru.

## Klíčové body
- Firma byla identifikována přes doménu registrovanou v Izraeli, spojovanou s C&C servery pro spyware.
- Jejich nástroje umožňují instalaci malware bez interakce uživatele na zařízeních s iOS a Androidem.
- Souvislosti s bývalými členy izraelských kyberjednotek, jako Unit 8200.
- Odhalení zahrnuje IP adresy, malware vzorky a vývojové repository.
- Žádné komentáře na Hacker News, ale zájem komunity (10 bodů).

## Podrobnosti
Izraelské firmy jako NSO Group (Pegasus), Candiru nebo Paragon dominují trhu se spywarem určeným pro státní aktéry. Tyto společnosti vyvíjejí software, který infikuje cílové telefony zero-click exploity – zranitelnostmi, které umožňují nainstalovat malware pouhým odesláním zprávy nebo návštěvou webu, bez nutnosti kliknutí uživatele. Spyware poté extrahuje data jako zprávy, kontakty, polohu, nahrávky z mikrofonu a kamery, a to často neomezeně dlouho.

Tato konkrétní firma, identifikovaná výzkumníkem Ahmedem Eldinem, se odhalila díky lidské chybě: vývojáři zaregistrovali doménu přímo související s jejich operacemi, která se objevila v analýzách malware vzorků na platformách jako VirusTotal. Další stopu poskytly DNS záznamy ukazující na servery v Evropě a USA sloužící jako command and control (C&C) servery – centrale pro ovládání infikovaných zařízení a sběr dat. Nástroje Shodan a Censys odhalily otevřené porty na těchto serverech, což umožnilo prohlédnout konfigurace.

Článek popisuje, jak Eldin spojil doménu s izraelskou firmou prostřednictvím WHOIS záznamů a LinkedIn profilů zaměstnanců, kteří mají zkušenosti z izraelských vojenských kyberjednotek. Firma pravděpodobně prodává své služby autoritářským režimům pro sledování odpůrců. Malware vzorky ukazují podobnosti s Pegasus: payload se maskuje jako legitimní aktualizace, využívá chain zero-day zranitelností v jádře systému.

Pro běžné uživatele to znamená riziko i pro aktualizovaná zařízení – jediná obrana je rychlé patche od Apple a Google, detekce anomaly (např. vysoká spotřeba baterie) a nástroje jako MVT od Amnesty International pro skenování. V průmyslu to posiluje potřebu lepšího opatrování vývojových procesů u těchto firem.

## Proč je to důležité
Odhalení ukazuje, že i specializované firmy na státní úrovni dělají banální chyby, což umožňuje civilním výzkumníkům mapovat jejich aktivity pomocí otevřených zdrojů. V širším ekosystému kyberbezpečnosti poskytuje nové indikátory kompromitace (IoC) – IP adresy, domény, hash malware – pro firemní SOC a antiviry. Zvyšuje tlak na regulace, jako americké embargo na prodej spyware nepřátelům, a posiluje globální debatu o etice sledování. Pro IT experty zdůrazňuje důležitost nástrojů jako Shodan pro recon a bezpečné konfigurace cloudových služeb.

---

[Číst původní článek](https://ahmedeldin.substack.com/p/the-israeli-spyware-firm-that-accidentally)

**Zdroj:** 📰 Substack.com
