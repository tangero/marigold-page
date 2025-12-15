---
author: Marisa Aigen
category: kyberbezpečnost
date: '2025-12-14 15:00:00'
description: Bezpečnost SaaS selhává ne na okraji sítě – útoky založené na AI, které
  zneužívají identity, ji obcházejí úplně. Podle zprávy AppOmni zažilo 75 % organizací
  incident související se SaaS.
importance: 4
layout: tech_news_article
original_title: 'Inside the AI-powered assault on SaaS: why identity is the weakest
  link'
publishedAt: '2025-12-14T15:00:00+00:00'
slug: inside-the-ai-powered-assault-on-saas-why-identity
source:
  emoji: 📰
  id: techradar
  name: TechRadar
title: 'Uvnitř AI útoků na SaaS: proč je identita nejslabším článkem'
url: https://www.techradar.com/pro/inside-the-ai-powered-assault-on-saas-why-identity-is-the-weakest-link
urlToImage: https://cdn.mos.cms.futurecdn.net/JFKDCP2HdEKqSGJCkLNprB-1100-80.jpg
urlToImageBackup: https://cdn.mos.cms.futurecdn.net/JFKDCP2HdEKqSGJCkLNprB-1100-80.jpg
---

## Souhrn
Útoky na SaaS platformy se posunuly od tradičních metod jako malware nebo brute-force k AI podporovaným zneužitím ukradených identit. Útočníci tak impersonují legitimní uživatele a pohybují se nepozorovaně v důvěryhodných prostředích. Podle zprávy AppOmni State of SaaS Security 2025 zažilo 75 % organizací incident související se SaaS, převážně kvůli ohroženým přihlašovacím údajům nebo špatně nastaveným přístupovým pravidlům, přesto 91 % firem věří své bezpečnosti.

## Klíčové body
- 75 % organizací mělo SaaS incident, většinou kvůli ukradeným přihlašovacím údajům nebo chybným přístupovým politikám.
- AI umožňuje útočníkům impersonovat uživatele, obcházet MFA kódy, API klíče a OAuth tokeny.
- Identita se stala novým perimetrem, protože SaaS nemá fyzickou hranici jako on-premise sítě.
- Firemní data v SaaS (komunikace, HR, finance, vývoj kódu) jsou ohrožena, pokud útočník zdědí oprávnění legitimního uživatele.
- Viditelnost je vysoká, ale kontrola nad přístupy zaostává.

## Podrobnosti
AppOmni, firma specializující se na bezpečnost SaaS aplikací, ve své zprávě State of SaaS Security 2025 analyzuje, jak se kybernetické útoky změnily. Tradiční obrana jako firewally nebo ochrana koncových zařízení selhává, protože útoky začínají uvnitř – ukradenými identitami. Útočníci cílí na hesla, API klíče (používané pro autentizaci mezi aplikacemi), OAuth tokeny (pro delegovanou autorizaci bez sdílení hesel) a dokonce MFA kódy, které generují jednorázové ověřovací údaje.

V SaaS prostředích, kde firmy ukládají citlivá data do nástrojů jako Slack pro komunikaci, Workday pro HR, Salesforce pro finance nebo GitHub pro vývoj kódu, není žádná společná fyzická hranice. Každý přístup závisí na identitě. Pokud útočník ovládne účet zaměstnance, získá stejná oprávnění: čtení e-mailů, editaci dat nebo spouštění workflow. AI zde hraje klíčovou roli – generuje chování podobné legitimnímu uživateli, například přirozené dotazy v chatu nebo sekvence API volání, což oklame detekční systémy založené na anomáliích.

Martin Vigo, hlavní bezpečnostní výzkumník AppOmni, zdůrazňuje, že identita není jen kontrolním bodem, ale celým povrchem útoku. Zpráva ukazuje rozpor: firmy mají dobrou viditelnost (logy, monitoring), ale chybí aktivní kontrola přístupů. Například misconfigured access policies umožňují přístup více uživatelům než potřebují, což zvyšuje riziko laterálního pohybu po kompromitaci jednoho účtu. AI nástroje útočníků navíc automatizují reconnaissance – sběr informací o cílové firmě z veřejných zdrojů – a generují credential stuffing útoky, kde testují ukradené údaje napříč platformami.

## Proč je to důležité
Tento trend znamená, že tradiční bezpečnostní modely selhávají v hybridním cloudu. Pro firmy to implikuje nutnost posunout fokus na identity and access management (IAM) systémy, jako Okta nebo Azure AD, s pokročilými funkcemi jako zero-trust architektura, která ověřuje každou akci bez ohledu na identitu. V širším kontextu AI posiluje útočníky, což urychluje závod v zbrojení mezi obranou a útokem. Pokud 91 % firem podceňuje rizika přes vysoké incidenty, hrozí masivní úniky dat. Doporučuje se implementace behaviorální analýzy poháněné AI pro detekci impersonace a pravidelné rotace credentialů, aby se minimalizoval dopad.

---

[Číst původní článek](https://www.techradar.com/pro/inside-the-ai-powered-assault-on-saas-why-identity-is-the-weakest-link)

**Zdroj:** 📰 TechRadar
