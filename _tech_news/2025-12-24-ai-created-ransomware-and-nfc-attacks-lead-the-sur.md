---
author: Marisa Aigen
category: kybernetika
date: '2025-12-24 17:35:00'
description: Umělá inteligence se už nepoužívá jen k tvorbě přesvědčivých phishingových
  e-mailů – používá se k budování ransomware. Výzkumníci ESETu objevili PromptLock,
  první ransomware řízený AI, který dynamicky generuje škodlivé skripty.
importance: 5
layout: tech_news_article
original_title: AI-created ransomware and NFC attacks lead the surge in new cyberattacks
  - here's how you can stay safe this holidays
publishedAt: '2025-12-24T17:35:00+00:00'
slug: ai-created-ransomware-and-nfc-attacks-lead-the-sur
source:
  emoji: 📰
  id: techradar
  name: TechRadar
title: Ransomware vytvořený umělou inteligencí a útoky přes NFC vedou k nárůstu nových
  kyberútoků – jak zůstat v bezpečí o svátcích
url: https://www.techradar.com/pro/security/ai-created-ransomware-and-nfc-attacks-lead-the-surge-in-new-cyberattacks-heres-how-you-can-stay-safe
urlToImage: https://cdn.mos.cms.futurecdn.net/ThNyuwnA55tfcixfqWcEcA-970-80.jpg
urlToImageBackup: https://cdn.mos.cms.futurecdn.net/ThNyuwnA55tfcixfqWcEcA-970-80.jpg
---

## Souhrn
Výzkumníci společnosti ESET, specialisty na detekci malwaru, odhalili PromptLock, první známý ransomware řízený umělou inteligencí. Tento proof-of-concept nástroj využívá model OpenAI přes Ollama API k dynamickému generování a spouštění škodlivých Lua skriptů, které prohledávají systém, exfiltrují data nebo je šifrují. Vedle toho roste počet útoků přes NFC, což zdůrazňuje potřebu aktualizací a záloh.

## Klíčové body
- PromptLock je první AI-driven ransomware, který generuje skripty za běhu pomocí AI modelu.
- Obsahuje statický hlavní modul pro komunikaci s AI serverem a dynamicky generované Lua skripty pro útoky.
- Skripty umožňují enumeraci souborového systému, exfiltraci dat, šifrování nebo jejich zničení na základě rozhodnutí AI.
- Zatím jen proof-of-concept s nízkým rizikem v reálném světě, ale signalizuje snadnější tvorbu sofistikovaných útoků.
- Doporučení: pravidelné aktualizace, zálohy a opatrné zacházení se soubory a nástroji.

## Podrobnosti
ESET Research ve své nejnovější zprávě o hrozbách popisuje PromptLock jako průlomový příklad, jak generativní umělá inteligence (GenAI) překračuje hranice phishingu a podvodů. Tento ransomware není statický program, ale adaptivní systém, který se chová podle situace na obětním počítači. Hlavní modul je statický a obsahuje pevně zakódované prompty pro AI model, který běží na vzdáleném serveru přes Ollama API – open-source rozhraní pro lokální nebo cloudové AI modely od OpenAI. Na základě těchto promptů AI generuje cross-platform Lua skripty, které se pak okamžitě spustí.

Lua je lehký skriptovací jazyk vhodný pro vestavěné systémy i desktopové aplikace, což z něj činí ideální volbu pro multiplatformní útoky na Windows, Linux nebo macOS. Tyto skripty plní několik funkcí: nejprve prohledávají lokální souborový systém (enumerace), identifikují citlivá data jako dokumenty, databáze nebo konfigurační soubory. Poté AI rozhodne, zda data exfiltruje na útočníkův server, zašifruje je pro výkupné nebo je jednoduše smaže, aby způsobil maximální škody. Tato autonomie znamená, že útočník nemusí předem programovat všechny varianty – AI to udělá dynamicky.

ESET zdůrazňuje, že PromptLock je zatím pouze proof-of-concept, tedy demonstrační verze bez šíření v divočině, což snižuje okamžité riziko. Nicméně jeho existence ukazuje, jak AI snižuje bariéry pro kyberzločince. Místo týmů vývojářů stačí nakonfigurovat AI model a poskytnout prompty. Vedle toho výzkumníci hlásí růst NFC malwaru – útoků přes Near Field Communication, technologii pro bezkontaktní platby a přenos dat mezi zařízeními. Tyto útoky infikují zařízení při blízkém kontaktu, například v davu, a vyžadují okamžité aktualizace firmware NFC čipů a vypnutí funkce, když není potřeba.

Pro uživatele to znamená, že standardní antiviry jako ESET Endpoint Security musí být aktualizovány, aby detekovaly chování AI-generovaných skriptů. Zálohy na externích médiích nebo cloudu s 3-2-1 pravidlem (3 kopie, 2 média, 1 off-site) jsou klíčové proti ransomware. Opatrnost při otevírání souborů z neznámých zdrojů a použití sandboxů pro testování nástrojů snižuje rizika.

## Proč je to důležité
PromptLock představuje zásadní posun v kybernetické bezpečnosti, kde AI nejen pomáhá útočníkům, ale stává se jádrem útoku. V širším kontextu to urychluje závod mezi obranou a útokem: zatímco LLM modely jako ty od OpenAI umožňují rychlou tvorbu kódu, bezpečnostní firmy musí integrovat AI detekci chování (behavioral analysis). Pro průmysl to znamená investice do AI-shieldů, které analyzují dynamicky generovaný kód v reálném čase. Pokud se PoC stane reálnou hrozbou, může zvýšit frekvenci ransomware útoků o desítky procent, jak ukazují trendy s AI-phishingem. Uživatelé by měli prioritizovat zero-trust architekturu a multifaktorové ověřování, aby minimalizovali dopady.

---

[Číst původní článek](https://www.techradar.com/pro/security/ai-created-ransomware-and-nfc-attacks-lead-the-surge-in-new-cyberattacks-heres-how-you-can-stay-safe)

**Zdroj:** 📰 TechRadar
