---
category: kybernetická bezpečn
date: '2025-10-27 17:00:00'
description: Technologie passkeys nahrazuje tradiční hesla a nabízí bezpečnější způsob
  přihlašování bez nutnosti pamatovat si složité kombinace znaků.
importance: 3
layout: tech_news_article
original_title: Yes, the new password alternative is actually safer - MakeUseOf
publishedAt: '2025-10-27T17:00:00+00:00'
slug: yes-the-new-password-alternative-is-actually-safer
source:
  emoji: 📰
  id: null
  name: MakeUseOf
title: Přístupové klíče jsou skutečně bezpečnější než hesla
url: https://www.makeuseof.com/passkeys-much-safer-than-old-passwords/
urlToImage: https://static0.makeuseofimages.com/wordpress/wp-content/uploads/2025/10/passkey-sign-in-on-tablet-with-passkey-icon.jpg?w=1600&h=900&fit=crop
urlToImageBackup: https://static0.makeuseofimages.com/wordpress/wp-content/uploads/2025/10/passkey-sign-in-on-tablet-with-passkey-icon.jpg?w=1600&h=900&fit=crop
---

## Souhrn

Přístupové klíče (passkeys) představují novou metodu autentizace, která má nahradit tradiční hesla. Místo zapamatování tajného řetězce znaků vaše zařízení prokáže identitu pomocí kryptografických klíčů, což eliminuje rizika spojená s opakovaným používáním hesel, phishingem a úniky dat.

## Klíčové body

- Passkeys fungují na principu asymetrické kryptografie, kdy zařízení uchovává soukromý klíč a server pouze veřejný
- Eliminují riziko phishingu, keyloggerů a úniků databází hesel
- Nevyžadují zapamatování složitých kombinací znaků a symbolů
- Každý účet má unikátní pár klíčů, takže kompromitace jednoho účtu neohrozí ostatní
- Fungují napříč zařízeními a platformami

## Podrobnosti

Tradiční hesla představují zásadní bezpečnostní problém, který se desítky let nedaří vyřešit. Přestože uživatelé vytváří stále složitější kombinace velkých a malých písmen, čísel a symbolů, hesla zůstávají statická data, která lze zkopírovat, ukrást nebo získat při úniku databáze. Problém není v síle hesla, ale v samotném konceptu sdíleného tajemství, které se opakovaně přenáší mezi uživatelem a serverem.

Dvoufaktorová autentizace (2FA) tento problém pouze zmírňuje, ale neřeší. Sofistikované phishingové útoky dokážou obejít i 2FA, protože útočník může v reálném čase předat získané údaje legitimnímu serveru. Keyloggery zachytí heslo bez ohledu na jeho složitost. A při úniku databáze se kompromitují všechny účty, kde uživatel použil stejné nebo podobné heslo.

Passkeys fungují fundamentálně jinak. Při registraci se vytvoří pár kryptografických klíčů – soukromý zůstává bezpečně uložen ve vašem zařízení (telefon, počítač, hardware token) a veřejný se odešle serveru. Při přihlášení server pošle výzvu, kterou vaše zařízení podepíše soukromým klíčem. Server ověří podpis pomocí veřejného klíče, aniž by soukromý klíč kdy opustil vaše zařízení.

Tato architektura eliminuje většinu známých útoků. Phishing nefunguje, protože útočník nemá co ukrást – soukromý klíč nikdy neopustí zařízení. Keyloggery jsou neúčinné, protože nic netypujete. Úniky databází neškodí, protože veřejný klíč sám o sobě neumožňuje přihlášení. Každý účet má navíc unikátní pár klíčů, taktakže kompromitace jednoho účtu neovlivní ostatní.

## Proč je to důležité

Passkeys představují první skutečnou evoluci v autentizaci za poslední dekády. Zatímco správci hesel problém částečně řeší, stále pracují s fundamentálně zranitelným konceptem. Passkeys tento koncept nahrazují architekturou, která je z principu odolnější vůči současným i budoucím útokům. Podpora ze strany Apple, Google, Microsoft a dalších velkých hráčů naznačuje, že jde o standardizovanou technologii s dlouhodobou perspektivou, nikoli o dočasný experiment.

---

[Číst původní článek](https://www.makeuseof.com/passkeys-much-safer-than-old-passwords/)

**Zdroj:** 📰 MakeUseOf
