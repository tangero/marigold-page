---
author: Marisa Aigen
category: kybernetika
companies:
- Google
date: '2026-02-12 07:00:08'
description: Čínská hackerská skupina APT31, sankcionovaná USA za útoky na kritickou
  infrastrukturu, využila AI chatbot Gemini k automatické analýze zranitelností a
  plánování kyberútoků. Mezitím rostou útoky typu 'distilace' na krádež duševního
  vlastnictví.
importance: 5
layout: tech_news_article
original_title: 'Google: China''s APT31 used Gemini to plan cyberattacks against US
  orgs'
publishedAt: '2026-02-12T07:00:08+00:00'
slug: google-chinas-apt31-used-gemini-to-plan-cyberattac
source:
  emoji: 📰
  id: null
  name: Theregister.com
title: 'Google: Čínská APT31 použila Gemini k plánování kyberútoků na americké organizace'
url: https://www.theregister.com/2026/02/12/google_china_apt31_gemini/
urlToImage: https://regmedia.co.uk/2024/09/16/shutterstock_china_digital_eyeball.jpg
urlToImageBackup: https://regmedia.co.uk/2024/09/16/shutterstock_china_digital_eyeball.jpg
---

## Souhrn
Čínská státem podporovaná hackerská skupina APT31 experimentovala s využitím AI chatbota Gemini od Google k automatické analýze bezpečnostních zranitelností a tvorbě plánů kyberútoků na americké organizace. Podle zprávy Google Threat Intelligence nedošlo k úspěšným útokům, ale toto chování signalizuje rostoucí integraci AI do ofenzivních kyberoperací. Zároveň Google upozorňuje na nárůst 'distillation attacks', které slouží k odcizení duševního vlastnictví z AI modelů.

## Klíčové body
- APT31, známá také jako Violet Typhoon nebo Judgment Panda, použila Gemini k analýze exploitů včetně remote code execution a webových aplikačních firewallů.
- Skupina aplikovala strukturované prompty s 'expertním persona' v kyberbezpečnosti pro generování testovacích plánů.
- Využití open-source nástroje Hexstrike postaveného na Model Context Protocol (MCP) pro red-teaming aktivity.
- Žádné úspěšné útoky, ale varování před škálovatelnými 'agentickými' přístupy v kyberútocích.
- Rostoucí 'distillation attacks' cílí na krádež IP z proprietárních AI modelů.

## Podrobnosti
APT31 je pekingská hackerská skupina, kterou USA v březnu 2024 sankcionovaly a obvinily sedm členů z neoprávněného přístupu do počítačových sítí, e-mailových účtů a cloudového úložiště klíčových cílů, včetně kritické infrastruktury. Tato skupina letos v létě exploitovala série chyb v Microsoft SharePoint. Nejnovější aktivity s Gemini proběhly koncem loňského roku. Podle zprávy Google Threat Intelligence z února 2026 skupina použila vysoce strukturované přístupy: zadávala Geminimu prompty s personou experta na kyberbezpečnost, což umožnilo automatizovat analýzu zranitelností a generovat cílené testovací plány pro exploity jako remote code execution (spuštění kódu na dálku) nebo obcházení webových aplikačních firewallů (WAF, nástroje chránící webové aplikace před útoky).

V jednom případě integrvali APT31 open-source nástroj Hexstrike, který je navržen pro red-teaming – simulaci útoků z pohledu obránců – a běží na Model Context Protocol (MCP), což je protokol pro sdílení kontextu mezi AI modely. Tento nástroj umožňuje analyzovat různé exploity v reálném čase. John Hultquist, šéf analytiků Google Threat Intelligence, zdůraznil, že APT skupiny jako APT31 testují AI pro semi-autonomní ofenzivní operace a očekává se, že čínští aktéři budou rozvíjet 'agentické' systémy, které umožní masivní škálování útoků bez lidského zásahu.

Zpráva také poukazuje na paralelní trend: nárůst 'distillation attacks'. Tyto útoky fungují tak, že útočníci 'destilují' znalosti z proprietárních AI modelů tím, že je opakovaně dotazují a trénují na základě odpovědí vlastní modely, čímž kradou duševní vlastnictví (IP). Například lze z velkých jazykových modelů (LLM) jako Gemini nebo GPT získat proprietární data o bezpečnostních zranitelnostech nebo optimalizacích.

## Proč je to důležité
Toto odhaluje klíčové riziko democratizace AI: open-access modely jako Gemini, které jsou navrženy pro široké využití včetně bezpečnostní analýzy, se stávají nástroji pro státní aktéry. APT31 demonstruje, jak lze AI použít k urychlení reconnaisance fáze útoků – analýza zranitelností, která normálně trvá týdny, se zkrátí na hodiny. Pro průmysl to znamená nutnost implementovat rate-limiting, persona-based filtry a watermarking do AI API, aby se omezilo zneužití. V širším kontextu posiluje to debatu o bezpečnostních guardrailech v LLM: současné modely jako Gemini mají základní ochrany proti škodlivému obsahu, ale selhávají u sofistikovaných promptů. Pro uživatele to implikuje riziko eskalace kyberhrozeb, kde AI agenti budou autonomně prozkoumávat sítě. Google sice hlásí žádné úspěchy, ale trend směřuje k hybridním AI-lidským útokům, což vyžaduje globální koordinaci v kyberbezpečnosti. Celkově to podtrhuje, že AI není jen nástroj inovací, ale i zbraní v asymetrické válce, kde Čína vede v adopci pro ofenzivu.

---

[Číst původní článek](https://www.theregister.com/2026/02/12/google_china_apt31_gemini/)

**Zdroj:** 📰 Theregister.com
