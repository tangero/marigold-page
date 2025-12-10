---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Google
date: '2025-12-09 12:15:16'
description: Google popsal bezpečnostní opatření pro agentické funkce v prohlížeči
  Chrome, které chrání model Gemini i uživatele před hrozbami. Hlavní zaměření je
  na obranu proti nepřímým injekcím promptů z webových stránek.
importance: 4
layout: tech_news_article
original_title: Google outlines security protections in Chrome's agentic capabilities
publishedAt: '2025-12-09T12:15:16+00:00'
slug: google-outlines-security-protections-in-chromes-ag
source:
  emoji: 📰
  id: null
  name: Ghacks Technology News
title: Google popisuje bezpečnostní ochrany agentických schopností Chrome
url: https://www.ghacks.net/2025/12/09/google-outlines-security-protections-in-chromes-agentic-capabilities/
urlToImage: https://www.ghacks.net/wp-content/uploads/2025/12/Google-outlines-security-protections-in-Chromes-agentic-capabilities.png
urlToImageBackup: https://www.ghacks.net/wp-content/uploads/2025/12/Google-outlines-security-protections-in-Chromes-agentic-capabilities.png
---

## Souhrn
Google zavádí vícevrstvou obranu proti bezpečnostním hrozbám v agentických funkcích Chrome, které pohání model Gemini. Tyto funkce umožňují AI autonomně vykonávat úkoly na základě uživatelských požadavků, jako je procházení webu nebo plánování akcí. Klíčovou novinkou je User Alignment Critic, který kontroluje shodu plánovaných kroků s původním záměrem uživatele.

## Klíčové body
- Hlavní hrozba: indirect prompt injection z škodlivých webů, iframeů nebo falešných recenzí, které mohou vést k neoprávněným akcím jako finanční transakce nebo únik dat.
- První vrstva obrany: User Alignment Critic (UAC), izolovaný model kontrolující plánované akce pouze na základě metadat.
- Celková strategie: Kombinace determinismkých a probabilistických obran, které zvyšují náklady pro útočníky.
- Rollout: Funkce se zavádějí pro uživatele v USA, s důrazem na izolaci od nespolehlivého webového obsahu.

## Podrobnosti
Google nedávno spustil agentické funkce v Chrome pro americké uživatele, což znamená, že model Gemini může na základě uživatelského příkazu autonomně plánovat a vykonávat akce, například prohledávat stránky, vyplňovat formuláře nebo interagovat s webovými prvky. Tyto schopnosti přinášejí rizika, protože AI agenti jsou zranitelní vůči indirect prompt injection – technice, kdy škodlivý webový obsah nenápadně ovlivní AI prompt, aby provedl nežádoucí akce. Příkladem je návštěva kompromitované stránky v iframe, kde skrytý text přesměruje AI na odeslání citlivých údajů, nebo falešné uživatelské recenze generované AI, které se šíří napříč weby.

Pro řešení toho Google navrhuje vrstvenou obranu. Základní vrstvou je User Alignment Critic (UAC), samostatný model oddělený od hlavního Gemini. UAC se aktivuje po dokončení plánování: analyzuje navržené akce, jejich metadata (jako cíl, parametry a kontext) a posuzuje, zda odpovídají uživatelskému záměru. Nemá přístup k webovému obsahu, což zabraňuje kontaminaci. Pokud detekuje nesoulad – například pokus o neoprávněnou transakci – zablokuje akci, poskytne zpětnou vazbu plánovacímu modelu a vrátí řízení uživateli. Tento proces je znázorněn v diagramu, který ukazuje sekvenci: uživatelský požadavek → plánování Gemini → kontrola UAC → buď provedení, nebo reformulace.

Další vrstvy zahrnují probabilistické mechanismy, jako detekce anomálií v chování, a determinismké filtry na vstupy. Google zdůrazňuje, že taková strategie zvyšuje obtížnost útoků a jejich náklady, protože útočníci musí obcházet více bariér současně. Agentické funkce v Chrome slouží k automatizaci rutinních úkolů, jako je srovnávání cen nebo plánování cest, ale bez těchto ochran by mohly vést k vážným incidentům. Srovnání s jinými systémy: podobné problémy řeší i OpenAI v ChatGPT s pluginy nebo Anthropic v Claude, kde prompt injection zůstává otevřenou výzvou.

## Proč je to důležité
Tento přístup posiluje důvěru v agentické AI v prohlížečích, kde se očekává masové nasazení. Pro uživatele znamená menší riziko úniku dat nebo zneužití, což je klíčové pro širokou adopci. V širším kontextu urychluje vývoj autonomních agentů, ale odhaluje ongoing výzvy v AI bezpečnosti – izolace modelů jako UAC je solidní, avšak útočníci se adaptují rychle. Pro průmysl nastavuje standard pro vrstvenou obranu, který by měly kopírovat i Microsoft v Edge nebo Apple v Safari při integraci AI. Dlouhodobě to může omezit škody z zero-day exploitů v AI, ale vyžaduje kontinuální testování v reálném prostředí.

---

[Číst původní článek](https://www.ghacks.net/2025/12/09/google-outlines-security-protections-in-chromes-agentic-capabilities/)

**Zdroj:** 📰 Ghacks Technology News
