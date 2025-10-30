---
category: kybernetická bezpečn
companies:
- OpenAI
date: '2025-10-27 19:23:00'
description: Bezpečnostní firma LayerX odhalila zranitelnost v OpenAI Atlas, která
  útočníkům umožňuje pomocí CSRF útoků vkládat škodlivé instrukce do trvalé paměti
  ChatGPT.
importance: 4
layout: tech_news_article
original_title: Atlas vuln allows malicious memory injection into ChatGPT - theregister.com
publishedAt: '2025-10-27T19:23:00+00:00'
slug: atlas-vuln-allows-malicious-memory-injection-into-
source:
  emoji: 📰
  id: null
  name: Theregister.com
title: Zranitelnost Atlas umožňuje vkládání škodlivých instrukcí do paměti ChatGPT
url: https://www.theregister.com/2025/10/27/atlas_vulnerability_memory_injection/
urlToImage: https://regmedia.co.uk/2024/05/20/memory_shutterstock.jpg
urlToImageBackup: https://regmedia.co.uk/2024/05/20/memory_shutterstock.jpg
---

## Souhrn

Bezpečnostní výzkumníci ze společnosti LayerX objevili kritickou zranitelnost v novém AI prohlížeči Atlas od OpenAI, která umožňuje útočníkům vkládat škodlivé instrukce do trvalé paměti ChatGPT pomocí cross-site request forgery (CSRF) útoků. Zranitelnost, nazvaná "ChatGPT Tainted Memories", představuje riziko pro všechny uživatele ChatGPT, ale zejména pro uživatele prohlížeče Atlas, který byl spuštěn minulý týden pro macOS.

## Klíčové body

- Útok zneužívá CSRF zranitelnost a funkci trvalé paměti ChatGPT, která si pamatuje předchozí konverzace a preference uživatelů
- Vyžaduje sociální inženýrství - uživatel musí kliknout na škodlivý odkaz
- Uživatelé prohlížeče Atlas jsou podle testů LayerX až o 90 % více vystaveni phishingovým útokům než uživatelé Chrome a Edge
- Atlas ukládá autentizační tokeny přímo v prohlížeči, což útočníkům usnadňuje zneužití aktivní relace
- OpenAI zatím na zjištění nereagoval

## Podrobnosti

Útok funguje na principu zneužití CSRF zranitelnosti, kdy útočník využije aktivní relaci uživatele na webové stránce a přinutí prohlížeč odeslat škodlivý požadavek. Webová stránka tento požadavek zpracuje jako legitimní, protože pochází od autentizovaného uživatele. V případě ChatGPT to útočníkovi umožňuje získat přístup k systémům OpenAI, do kterých je uživatel přihlášen, a následně vložit škodlivé instrukce.

Klíčovým prvkem útoku je zneužití vestavěné funkce paměti ChatGPT. Tato funkce umožňuje chatbotu "pamatovat si" dotazy uživatelů, jejich preference a kontext předchozích konverzací napříč relacemi. Útočník může do této paměti vložit škodlivé instrukce, které ChatGPT následně považuje za legitimní uživatelské preference a řídí se jimi i v budoucích konverzacích.

Prohlížeč Atlas od OpenAI, který byl představen teprve minulý týden jako AI-poháněný webový prohlížeč pro macOS, je podle výzkumníků obzvláště zranitelný. Důvodem je, že uživatelé Atlas jsou typicky ve výchozím nastavení přihlášeni k ChatGPT, což znamená, že jejich autentizační tokeny jsou uloženy přímo v prohlížeči a mohou být zneužity během aktivní relace.

Společnost LayerX, která se zabývá zabezpečením prohlížečů, provedla testy a zjistila, že prohlížeč Atlas je až o 90 % více vystaven phishingovým útokům ve srovnání s etablovanými prohlížeči jako Chrome a Edge. Toto zjištění vyvolává vážné otázky ohledně bezpečnostní architektury nového produktu OpenAI.

## Proč je to důležité

Tato zranitelnost přichází v době, kdy OpenAI agresivně expanduje do nových produktových kategorií, včetně webových prohlížečů. Odhalení tak závažné bezpečnostní chyby krátce po spuštění Atlas poukazuje na potenciální problémy s bezpečnostním testováním a přípravou produktu před uvedením na trh.

Pro uživatele ChatGPT představuje tato zranitelnost reálné riziko. Útočník, který úspěšně vloží škodlivé instrukce do paměti chatbota, může ovlivnit všechny budoucí interakce uživatele s ChatGPT. To může vést k úniku citlivých informací, manipulaci s odpověďmi nebo jiným formám zneužití.

Širší kontext této zranitelnosti ukazuje na rostoucí bezpečnostní výzvy spojené s AI nástroji a prohlížeči. Jak se AI asistenti stávají stále více integrovanými do našich každodenních pracovních postupů a ukládají si kontextuální informace o uživatelích, stávají se také atraktivnějším cílem pro útočníky. Absence okamžité reakce ze strany OpenAI na toto odhalení je rovněž znepokojující a vyvolává otázky ohledně procesů řešení bezpečnostních incidentů ve společnosti.

---

[Číst původní článek](https://www.theregister.com/2025/10/27/atlas_vulnerability_memory_injection/)

**Zdroj:** 📰 Theregister.com
