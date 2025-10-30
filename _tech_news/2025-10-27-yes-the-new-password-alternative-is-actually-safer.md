---
category: kybernetická bezpečn
date: '2025-10-27 17:00:00'
description: Passkeys nahrazují tradiční hesla a nabízejí bezpečnější způsob přihlašování
  bez rizika úniku dat nebo phishingu.
importance: 3
layout: tech_news_article
original_title: Yes, the new password alternative is actually safer - MakeUseOf
publishedAt: '2025-10-27T17:00:00+00:00'
slug: yes-the-new-password-alternative-is-actually-safer
source:
  emoji: 📰
  id: null
  name: MakeUseOf
title: Passkeys jako bezpečnější alternativa k heslům
url: https://www.makeuseof.com/passkeys-much-safer-than-old-passwords/
urlToImage: https://static0.makeuseofimages.com/wordpress/wp-content/uploads/2025/10/passkey-sign-in-on-tablet-with-passkey-icon.jpg?w=1600&h=900&fit=crop
urlToImageBackup: https://static0.makeuseofimages.com/wordpress/wp-content/uploads/2025/10/passkey-sign-in-on-tablet-with-passkey-icon.jpg?w=1600&h=900&fit=crop
---

## Souhrn

Passkeys představují novou metodu autentizace, která má nahradit tradiční hesla. Místo zapamatování tajného řetězce znaků využívá passkey kryptografické klíče uložené v zařízení, které prokazují identitu uživatele bez nutnosti sdílet jakékoli tajemství se serverem. Technologie eliminuje hlavní slabiny hesel včetně možnosti úniku dat, phishingu nebo opakovaného použití stejného hesla.

## Klíčové body

- Passkeys fungují na principu asymetrické kryptografie, kdy soukromý klíč zůstává v zařízení a nikdy není sdílen
- Eliminují rizika spojená s tradičními hesly: úniky databází, phishing, keyloggery a opakované použití hesel
- Přihlášení probíhá pomocí biometrie nebo PIN kódu zařízení, což je rychlejší než psaní hesla
- Každý účet má unikátní pár klíčů, takže kompromitace jedné služby neohrozí ostatní
- Dvoustupňové ověření (2FA) se stává zbytečným, protože passkeys jsou inherentně bezpečnější

## Podrobnosti

Tradiční hesla představují fundamentální bezpečnostní problém, který nelze vyřešit pouhým zvyšováním složitosti. I když uživatel vytvoří silné heslo s kombinací velkých a malých písmen, čísel a symbolů, heslo zůstává statickým tajemstvím, které může být zkopírováno, ukradeno nebo unikne při narušení databáze služby. Problém se prohlubuje tím, že lidé často používají stejné nebo podobné heslo pro více účtů.

Passkeys tento model zcela mění. Při registraci na službu vytvoří zařízení pár kryptografických klíčů - soukromý klíč zůstává bezpečně uložen v zařízení (telefonu, počítači nebo hardwarovém tokenu), zatímco veřejný klíč se odešle službě. Při přihlášení služba pošle výzvu, kterou zařízení podepíše soukromým klíčem. Služba ověří podpis pomocí veřejného klíče, aniž by soukromý klíč kdy opustil zařízení uživatele.

Tato architektura má několik zásadních výhod. Phishingové útoky se stávají neúčinnými, protože neexistuje žádné heslo, které by mohl útočník ukrást. Keyloggery jsou zbytečné, protože uživatel nic netypuje. Úniky databází ztrácejí na závažnosti - i když útočník získá veřejný klíč, nemůže ho použít k přihlášení. Každý účet má navíc unikátní pár klíčů, takže kompromitace jedné služby neohrozí ostatní.

Pro uživatele je proces přihlášení jednodušší - stačí potvrdit identitu pomocí biometrie (otisk prstu, Face ID) nebo PIN kódu zařízení. Synchronizace mezi zařízeními probíhá šifrovaně přes cloudové služby výrobců (Apple iCloud Keychain, Google Password Manager).

## Proč je to důležité

Passkeys představují první skutečně masovou alternativu k heslům s podporou všech hlavních technologických firem včetně Apple, Google a Microsoft. Jde o standardizovanou technologii postavenou na protokolu FIDO2, což zajišťuje kompatibilitu napříč platformami. Pro běžné uživatele to znamená konec neustálého resetování zapomenutých hesel a vyšší bezpečnost bez nutnosti používat správce hesel. Pro firmy jde o snížení nákladů na helpdesk a významné posílení bezpečnostního profilu. Adopce passkeys však bude postupná - vyžaduje podporu ze strany webových služeb a aplikací, což bude trvat roky.

---

[Číst původní článek](https://www.makeuseof.com/passkeys-much-safer-than-old-passwords/)

**Zdroj:** 📰 MakeUseOf
