---
author: Marisa Aigen
category: umělá inteligence
date: '2025-12-05 22:05:42'
description: Nová fáze spolehlivosti softwaru nastává díky umělé inteligenci a agentickým
  AI systémům, které posouvají vývojové týmy za hranice tradiční detekce chyb k proaktivní
  automatizované prevenci. Vývojáři spoléhají na systémy, které nejen odhalují defekty,
  ale uvažují o potenciálních selháních před jejich realizací.
importance: 3
layout: tech_news_article
original_title: 'From observability to reasoning: How AI agents are catching bugs
  before they ship'
publishedAt: '2025-12-05T22:05:42+00:00'
slug: from-observability-to-reasoning-how-ai-agents-are-
source:
  emoji: 📰
  id: null
  name: SiliconANGLE News
title: 'Od sledování k uvažování: Jak AI agenti odhalují chyby před jejich nasazením'
url: https://siliconangle.com/2025/12/05/agentic-ai-bug-prevention-awsreinvent/
urlToImage: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/12/IMG_8881.jpg
urlToImageBackup: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/12/IMG_8881.jpg
---

## Souhrn
Sentry, firma specializující se na sledování chyb v produkčním softwaru, představuje vrstvu Seer, která využívá agentickou umělou inteligenci k analýze dat o chybách a jejich kořenovým příčinám. Tento přístup umožňuje nejen identifikaci problémů, ale i automatickou opravu kódu prostřednictvím interních kódovacích agentů a prevenci nasazení chybných verzí. Podle CEO Milina Desaieho dosahuje tento systém 95procentní přesnosti v určení kořenových příčin.

## Klíčové body
- Sentry přechází od pasivního sledování (observability) k aktivnímu uvažování (reasoning) pomocí AI.
- Vrstva Seer analyzuje produkční data o chybách a trasovací informace pro určení kořenových příčin.
- Integrace s kódovacími agenty umožňuje automatickou opravu a blokování chybného kódu před nasazením.
- Systém aktuálně zabraňuje statisícům chyb měsíčně, což mění reaktivní opravy na proaktivní prevenci.
- Prezentováno na konferenci AWS re:Invent v rozhovoru pro theCUBE.

## Podrobnosti
Sentry, právně známá jako Functional Software Inc., je platforma pro sledování chyb a výkonu aplikací v produkčním prostředí. Tradičně sbírá data o selháních, stack tracech a metrikách, aby vývojářům pomohla rychle identifikovat problémy. Nová vrstva Seer tento proces posouvá dál: bere hluboký kontext z produkčních chyb, tras a logů a aplikuje na ně modely umělé inteligence schopné uvažování. Výsledkem je nejen lokalizace kořenové příčiny s vysokou přesností, ale i uzavřená smyčka (closed-loop), kde AI navrhne nebo přímo napíše opravu.

Podle Milina Desaieho, CEO Sentry, tato technologie dosahuje 95procentní přesnosti v identifikaci kořenových příčin, což vývojáři dlouhodobě požadovali. Seer se neomezuje na interní data Sentry, ale integruje se s existujícími ekosystémy firem, jako jsou jejich kódovací agenti. Tyto agenti, poháněné AI, dokážou po určení problému generovat patche nebo dokonce zabránit mergeování chybného kódu do hlavní větve. Desai zmínil, že systém již nyní zabraňuje stovkám tisíc chyb před jejich nasazením do produkce, což je zásadní posun od detekce k prevenci.

Rozhovor proběhl na konferenci AWS re:Invent, kde Sentry demonstrovalo, jak agentická AI mění workflow vývojářů. Například v typickém scénáři: chyba v produkci spustí Seer, který analyzuje trace, identifikuje vadný kód v knihovně nebo algoritmu, navrhne fix a pošle ho do pull requestu. Pokud je chyba kritická, systém může automaticky zablokovat deploy. Tento přístup snižuje manuální práci, zrychluje remediation a zvyšuje celkovou spolehlivost softwaru. Nicméně přesnost 95 procent vyžaduje ověření v reálných nasazeních napříč různými projekty, protože složitost kódu a specifické prostředí mohou ovlivnit výsledky.

## Proč je to důležité
Tento vývoj ukazuje na širší trend v softwarovém inženýrství, kde agentická AI přechází od podpůrných nástrojů k autonomním systémům, které aktivně ovlivňují vývojový cyklus. Pro průmysl znamená méně výpadků v produkci, nižší náklady na údržbu a rychlejší iterace, což je klíčové pro cloudové služby a aplikace s vysokou zátěží. V kontextu rostoucí složitosti moderních systémů (mikroslužby, serverless) pomáhá udržet kvalitu kódu bez navyšování týmů. Pro uživatele to znamená stabilnější software, ale zároveň zdůrazňuje potřebu etických rámců pro AI, které upravují kód bez lidského dohledu. Sentry tak nastavuje standard pro budoucí devops nástroje, kde prevence chyb převáží nad jejich lovem.

---

[Číst původní článek](https://siliconangle.com/2025/12/05/agentic-ai-bug-prevention-awsreinvent/)

**Zdroj:** 📰 SiliconANGLE News
