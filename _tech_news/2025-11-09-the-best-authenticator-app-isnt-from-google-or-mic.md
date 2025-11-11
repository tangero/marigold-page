---
author: Marisa Aigen
category: kybernetická bezpečn
companies:
- Google
- Microsoft
date: '2025-11-09 18:00:00'
description: Článek upozorňuje na rizika závislosti na cloudových autentizátorech
  od velkých firem a vysvětluje, proč open-source aplikace Aegis Authenticator nabízí
  transparentnější a bezpečnější způsob správy 2FA kódů.
importance: 3
layout: tech_news_article
original_title: The best authenticator app isn’t from Google or Microsoft — it's actually
  open-source - MakeUseOf
publishedAt: '2025-11-09T18:00:00+00:00'
slug: the-best-authenticator-app-isnt-from-google-or-mic
source:
  emoji: 📰
  id: null
  name: MakeUseOf
title: Nejlepší autentizační aplikace není od Googlu ani Microsoftu. Otevřený Aegis
  dává uživateli větší kontrolu
url: https://www.makeuseof.com/best-authenticator-app-isnt-google-or-microsoft-its-open-source/
urlToImage: https://static0.makeuseofimages.com/wordpress/wp-content/uploads/wm/2025/11/aegis-2fa-app-login-screen-on-smartphone.jpg?w=1600&h=900&fit=crop
urlToImageBackup: https://static0.makeuseofimages.com/wordpress/wp-content/uploads/wm/2025/11/aegis-2fa-app-login-screen-on-smartphone.jpg?w=1600&h=900&fit=crop
---

## Souhrn
Článek rozebírá rozdíl mezi centralizovanými autentizačními aplikacemi (Google Authenticator, Microsoft Authenticator) a otevřeným řešením Aegis Authenticator pro Android. Upozorňuje, že pohodlí cloudové synchronizace může znamenat ztrátu kontroly nad citlivými 2FA klíči a že lokálně šifrované, auditovatelné řešení je pro dlouhodobou bezpečnost uživatelů robustnější.

## Klíčové body
- Aplikace jako Google Authenticator a Microsoft Authenticator ukládají tajné klíče v prostředí, které uživatel plně neřídí.
- Aegis Authenticator je open-source nástroj pro Android s lokálním šifrováním a možností bezpečných záloh.
- Lokální správa 2FA klíčů snižuje závislost na proprietárních cloudových ekosystémech.
- Podpora importu z jiných autentizátorů usnadňuje migraci bez ztráty přístupu.
- Přístup „klíče patří uživateli“ je relevantní pro běžné uživatele i pro bezpečnostně citlivé organizace.

## Podrobnosti
Dvoufaktorové ověřování (2FA) je základní bezpečnostní prvek pro ochranu účtů před zneužitím hesel. Většina aplikací pro jednorázové kódy (TOTP) pracuje se stejným principem: server a aplikace sdílí tajný klíč, ze kterého se generují časově omezené kódy. Kritická otázka není algoritmus, ale kde a jak jsou tyto tajné klíče uloženy a jak se s nimi nakládá při záloze a migraci.

Google Authenticator a Microsoft Authenticator jsou úzce svázány s účty svých poskytovatelů. Synchronizace přes jejich cloud sice zjednodušuje přechod na nový telefon, ale zároveň přesouvá důvěru do proprietárního systému, který nelze nezávisle auditovat. Uživatel reálně neví, jak jsou klíče spravovány, jaké logy vznikají a jaká interní oprávnění mají zaměstnanci poskytovatele. Ztráta zařízení nebo chyba v procesu obnovy pak může vést k nutnosti resetovat přístupy u více služeb, což je časově náročné a bezpečnostně citlivé.

Aegis Authenticator je open-source aplikace pro Android určená k správě 2FA tokenů. Všechny tajné klíče ukládá v šifrovaném „trezoru“ přímo v zařízení, typicky pomocí AES-256-GCM, přičemž odemykací klíč nikdy neopouští telefon. Uživatel může vytvářet zašifrované zálohy (například pro offline uložení nebo vlastní synchronizaci přes důvěryhodné úložiště), aniž by poskytoval klíče třetí straně. Otevřený kód umožňuje bezpečnostní audit komunitou a snižuje riziko skrytých mechanismů či nezdokumentovaného nakládání s daty.

Podpora importu z jiných 2FA aplikací usnadňuje přechod pro uživatele, kteří již používají Google či Microsoft Authenticator. Aegis je vhodný jak pro jednotlivce, tak pro firmy, které chtějí mít nad 2FA infrastrukturou větší kontrolu a preferují ověřitelnou implementaci před „černou skříňkou“ velkých poskytovatelů.

## Proč je to důležité
Diskuse kolem Aegis Authenticatoru upozorňuje na dlouhodobě podceňovaný problém: 2FA je sice doporučovaný bezpečnostní standard, ale způsob jeho implementace může vytvářet novou závislost na konkrétních korporátních ekosystémech. Centralizovaná správa tajných klíčů u velkých poskytovatelů znamená, že chyba, změna podmínek nebo regulatorní zásah mohou mít dopad na přístup k mnoha účtům zároveň.

Lokálně šifrované, otevřeně auditovatelné řešení, jako je Aegis, vrací kontrolu nad 2FA klíči přímo uživateli. To je důležité pro technicky orientované uživatele, správce IT i bezpečnostní týmy, které potřebují prokázat, že citlivé klíče nejsou vystaveny zbytečným rizikům. Článek tak zapadá do širšího trendu posilování digitální suverenity, preference open-source řešení a odmítání bezdůvodné důvěry v proprietární cloudové služby, zejména v oblasti autentizace a identity managementu.

---

[Číst původní článek](https://www.makeuseof.com/best-authenticator-app-isnt-google-or-microsoft-its-open-source/)

**Zdroj:** 📰 MakeUseOf
