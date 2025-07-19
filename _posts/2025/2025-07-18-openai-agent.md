---
author: Patrick Zandl
categories:
- AI
- OpenAI
- ChatGPT
- automatizace
- agentové systémy
layout: post
post_excerpt: OpenAI spustilo ChatGPT Agent, který kombinuje schopnosti webového prohlížení, výzkumu a konverzace do jednoho systému pro automatické vykonávání úkolů.
summary_points:
- OpenAI představilo 17. července 2025 ChatGPT Agent pro platící uživatele
- Systém kombinuje funkce nástrojů Operator a Deep Research s konverzačními schopnostmi ChatGPT
- Agent dokáže procházet weby, spouštět kód, vytvářet prezentace a připojovat se k externím službám
- Používá vlastní virtuální počítač s terminálem a přístupem k rozhraním API
- Pro uživatele Pro je k dispozici 400 zpráv měsíčně, pro ostatní 40 zpráv
- Systém obsahuje bezpečnostní opatření proti zneužití a vyžaduje povolení pro citlivé operace
title: "OpenAI představilo ChatGPT Agent - jednotný systém pro vykonávání úkolů"
---

OpenAI  spustilo službu ChatGPT Agent, sjednocený agentový systém, který rozšiřuje možnosti konverzačního modelu o schopnost samostatně vykonávat složitější úkoly na počítači. Nový nástroj kombinuje funkce dříve samostatných produktů Operator a Deep Research do jednoho systému dostupného přímo v rozhraní ChatGPT.

ChatGPT Agent představuje posun od  generování odpovědí k aktivnímu vykonávání činností. Systém dokáže analyzovat kalendář uživatele a připravit přehled nadcházejících schůzek na základě aktuálních zpráv, naplánovat a nakoupit ingredience pro přípravu japonské snídaně pro čtyři osoby nebo analyzovat tři konkurenty a vytvořit prezentaci. Oproti předchozím verzím ChatGPT tak nevydává pouze doporučení, ale skutečně úkoly realizuje.

## Technické možnosti systému

ChatGPT Agent pracuje s vlastním virtuálním počítačem a má přístup k sadě nástrojů pro vykonávání různých typů úkolů. Systém zahrnuje vizuální prohlížeč pro interakci s webovými stránkami prostřednictvím grafického rozhraní, textový prohlížeč pro jednodušší dotazy založené na logickém uvažování, terminál pro spouštění kódu a přímý přístup k rozhraním API OpenAI.

Významnou funkcí jsou konektory ChatGPT, které umožňují připojení k externím službám jako Gmail, Google Drive nebo GitHub. Agent tak může vyhledat relevantní informace v uživatelových aplikacích a využít je ve svých odpovědích. Uživatelé se mohou přihlásit na jakoukoliv webovou stránku převzetím kontroly nad prohlížečem, což agentovi umožňuje hlubší výzkum i vykonávání úkolů.

Při práci s webovými stránkami agent dokáže procházet obsah, filtrovat výsledky, klikat na odkazy a vyplňovat formuláře. Může spouštět kód v terminálu, provádět analýzu dat a generovat upravitelné tabulky nebo prezentace. V testech překonal ChatGPT Agent lidský výkon v několika srovnávacích úkolech zahrnujících práci s tabulkami Excel a analýzu dat.

## Dostupnost a využití

Funkce ChatGPT Agent se postupně zpřístupňuje uživatelům placených plánů. Uživatelé Pro získali přístup 17. července, uživatelé Plus a Team během následujících dnů. OpenAI plánuje rozšíření pro uživatele Enterprise a Education v nadcházejících týdnech.

Pro aktivaci je nutné vybrat “agent mode” z rozbalovací nabídky nástrojů v kompozitoru během konverzace. Uživatelé mohou v rámci stejného chatu přirozeně přecházet mezi běžnou konverzací a požadavky na vykonání akcí.

Uživatelé Pro mají k dispozici 400 zpráv měsíčně, zatímco ostatní platící uživatelé získávají 40 zpráv měsíčně s možností dokoupení dalšího využití prostřednictvím kreditového systému.

## Bezpečnostní opatření

OpenAI implementovalo několik vrstev bezpečnostních opatření pro minimalizaci rizik spojených s automatickým vykonáváním úkolů na internetu. Systém je navržen tak, aby požádal o povolení před provedením “akcí s důsledky” a uživatelé mohou úkoly kdykoli přerušit a dodat další instrukce.

Agent je vyškolen k odmítání vysoce rizikových úkolů jako bankovní převody. Společnost omezila data, k nimž má model přístup, a určité úkoly jako odesílání e-mailů vyžadují dohled uživatele. Systém obsahuje také ochranu proti adversariálním prompt injection útokům, které představují specifické riziko pro agentové systémy.

Generální ředitel OpenAI Sam Altman doporučil opatrnost při udělování přístupu k osobním informacím a popsal systém jako “špičkový a experimentální”. Podle jeho slov je vhodné poskytnutí přístupu ke kalendáři pro koordinaci skupinové večeře, ale agent nepotřebuje přístup ke kalendáři pro nákup oblečení.

ChatGPT Agent je postaven na existujících modelech jako GPT-4o a nejedná se o nový jazykový model, ale o vrstvu schopností umožňujících automatické vykonávání úkolů. Systém představuje další krok OpenAI v oblasti agentových technologií a konkuruje podobným snahám společností jako Google s jeho asistentem Gemini.

*Zdroje:*

- [OpenAI - Introducing ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/)
- [OpenAI - ChatGPT agent System Card](https://openai.com/index/chatgpt-agent-system-card/)
- [OpenAI Help Center - ChatGPT agent release notes](https://help.openai.com/en/articles/11794368-chatgpt-agent-release-notes)