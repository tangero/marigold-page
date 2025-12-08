---
author: Marisa Aigen
category: umělá inteligence
date: '2025-12-07 12:40:59'
description: Umělá inteligence vykazuje fenomen Jeopardy. Pokud používáte AI k generování
  kódu mimo vaši oblast expertizy, pravděpodobně vám to připadá v pořádku, zvláště
  pokud to hned funguje. Ale pokud jste s technologií intimně obeznámeni, odhalíte
  chyby.
importance: 3
layout: tech_news_article
original_title: The Jeopardy Phenomenon – Chris Coyier
people:
- Chris Coyier
publishedAt: '2025-12-07T12:40:59+00:00'
slug: the-jeopardy-phenomenon-chris-coyier
source:
  emoji: 📰
  id: null
  name: Chriscoyier.net
title: Fenomen Jeopardy – Chris Coyier
url: https://chriscoyier.net/2025/12/04/the-jeopardy-phenomenon/
urlToImage: https://jetpack.com/redirect/?source=sigenerate&query=t%3DeyJpbWciOiJodHRwczpcL1wvY2hyaXNjb3lpZXIubmV0XC93cC1jb250ZW50XC91cGxvYWRzXC8yMDI1XC8xMlwvaW1hZ2UucG5nIiwidHh0IjoiaWxsIHRha2UgXCJ1aCwgd3JvbmdcIiBmb3IgMTAwMCBhbGV4IiwidGVtcGxhdGUiOiJmdWxsc2NyZWVuIiwiZm9udCI6IiIsImJsb2dfaWQiOjc0MDc0MjQ4fQ.HQ--QctRQDIGKFajb5Aj2AgVkRc05oC612lmso_Xzy4MQ
urlToImageBackup: https://jetpack.com/redirect/?source=sigenerate&query=t%3DeyJpbWciOiJodHRwczpcL1wvY2hyaXNjb3lpZXIubmV0XC93cC1jb250ZW50XC91cGxvYWRzXC8yMDI1XC8xMlwvaW1hZ2UucG5nIiwidHh0IjoiaWxsIHRha2UgXCJ1aCwgd3JvbmdcIiBmb3IgMTAwMCBhbGV4IiwidGVtcGxhdGUiOiJmdWxsc2NyZWVuIiwiZm9udCI6IiIsImJsb2dfaWQiOjc0MDc0MjQ4fQ.HQ--QctRQDIGKFajb5Aj2AgVkRc05oC612lmso_Xzy4MQ
---

## Souhrn
Chris Coyier, zakladatel platformy CodePen pro sdílení a testování webového kódu, popisuje tzv. fenomen Jeopardy v kontextu umělé inteligence. Jedná se o situaci, kdy obsah mimo naši expertizu působí věrohodně, zatímco expert okamžitě pozná nesrovnalosti. Tento jev platí i pro kód generovaný AI, kde laik vidí úspěch, ale odborník odhalí nedostatky.

## Klíčové body
- Fenomen Jeopardy pochází z pozorování novinových článků: neznámé témata vypadají dobře, známá mají chyby.
- V kvízu Jeopardy působí otázky obtížně, pokud o tématu nevíte nic, ale expert je považuje za triviální.
- AI generovaný kód funguje na první pohled mimo expertizu, ale skrývá problémy v hlubších vrstvách.
- Coyier vyzývá k sdílení názorů a propaguje CodePen PRO.

## Podrobnosti
Coyier fenomen Jeopardy ilustruje na příkladech z každodenního života. Představte si čtení novin: článek o neznámé oblasti jako exotická politika se zdá vyvážený a informativní. Pak přijde článek o vaší profesi, například vývoji webových aplikací, a objevíte faktické chyby, zjednodušení nebo přímo nesmysly. Stejný princip platí pro televizní kvíz Jeopardy, kde odpovědi (v Jeopardy formě otázek) mimo vaši doménu působí složitě, ale v oblasti jako sbírání fantasy karetních her je „otázka" na úrovni Magic: The Gathering místo pokročilejšího Android: Netrunner – očividné pro znalce.

Přenáší to na umělou inteligenci, konkrétně na velké jazykové modely (LLM) jako GPT nebo Claude, které generují kód. Pokud jste například marketér a potřebujete JavaScript pro interaktivní webovou komponentu, AI vám poskytne funkční prototyp, který se spustí. Vypadá to profesionálně: použije CSS Flexbox pro layout, přidá event listenery a funguje na první otevření prohlížeče. Spokojenost zaručena. Ale webový vývojář s zkušenostmi uvidí problémy: kód ignoruje přístupnost (ARIA atributy chybí), není optimalizován pro mobilní zařízení (viewport meta tag absentní), obsahuje zbytečné globální proměnné nebo špatně řeší edge cases jako rychlé opakované kliknutí. Navíc může AI halucinovat neexistující API nebo navrhnout zastaralé praktiky, jako použití vanilla JavaScript místo moderních frameworků jako React, pokud není specifikováno.

Tento článek z 4. prosince 2025 (pravděpodobně chyba, reálně dříve) vychází z Coyierovy praxe na CodePen, platformě pro rychlé prototypování HTML, CSS a JavaScriptu. CodePen umožňuje sdílení snippetů, testování v prohlížeči a spolupráci; PRO verze přidává soukromé projekty, asset hosting a pokročilé analýzy. Coyier takto upozorňuje na past AI nástrojů jako GitHub Copilot nebo Cursor, které urychlují kódování, ale vyžadují validaci. V praxi to znamená, že vývojáři musí kód z AI nejen spustit, ale prozkoumat architekturu, bezpečnost (např. XSS zranitelnosti) a škálovatelnost. Pro laika to implikuje riziko zavádějících řešení, která selžou v produkci.

## Proč je to důležité
Tento fenomen odhaluje limity současných LLM v technických doménách, kde znalosti jsou hluboké a kontextuální. V éře, kdy AI generuje 40 % kódu v některých týmech (podle průzkumů Stack Overflow), zdůrazňuje potřebu lidského dohledu. Pro průmysl to znamená vyšší náklady na revize, ale i příležitost k lepším nástrojům – např. AI s verifikací proti best practices. Pro uživatele to upozorňuje: nedůvěřujte AI slepě mimo vaši expertizu, testujte důkladně. V širším ekosystému posiluje debatu o spolehlivosti AI, kde modely jako Llama nebo Gemini stále trpí halucinacemi, a volá po hybridních přístupech s lidskou expertizou.

---

[Číst původní článek](https://chriscoyier.net/2025/12/04/the-jeopardy-phenomenon/)

**Zdroj:** 📰 Chriscoyier.net
