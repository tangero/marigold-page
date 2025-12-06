---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Apple
date: '2025-12-01 17:27:21'
description: Podvodníci málem ukradli Apple účet zneužitím podpůrného systému autentickými
  tikety a telefonáty. Uživatelé se mohou chránit základními bezpečnostními kroky,
  jako je ověřování zdrojů komunikace.
importance: 3
layout: tech_news_article
original_title: Real Apple support emails used in new phishing scam
publishedAt: '2025-12-01T17:27:21+00:00'
slug: real-apple-support-emails-used-in-new-phishing-sca
source:
  emoji: 📰
  id: fox-news
  name: Fox News
title: Skutečné e-maily od podpory Apple zneužité v novém phishingovém podvodu
url: https://www.foxnews.com/tech/real-apple-support-emails-used-new-phishing-scam
urlToImage: https://static.foxnews.com/foxnews.com/content/uploads/2025/11/apple-email-photo-1.jpg
urlToImageBackup: https://static.foxnews.com/foxnews.com/content/uploads/2025/11/apple-email-photo-1.jpg
---

## Souhrn
Nový phishingový podvod zneužívá skutečné podpůrné tikety v systému Apple, které generují oficiální e-maily z domény společnosti. Podvodníci tak oklamávají uživatele, aby jim poskytli přístup k iCloud účtům. Eric Moret, zaměstnanec firmy Broadcom zabývající se polovodiči, podrobně popsal na platformě Medium, jak málem přišel o svůj účet po sérii autenticky působících upozornění a telefonátů.

## Klíčové body
- Podvodníci vytvářejí reálné podpůrné tikety v Apple systému bez jakékoli ověření identity.
- Tyto tikety spouštějí oficiální e-maily z apple.com domény, což buduje důvěru.
- Následují telefonáty od klidných „agentů podpory“, kteří nabízejí pomoc s bezpečnostními incidenty.
- Cílem je získat ověřovací kódy nebo přihlašovací údaje k iCloud.
- Slabina spočívá v absenci verifikace při vytváření tiketů, což umožňuje zneužití systému.

## Podrobnosti
Podvod začíná záplavou upozornění na dvoufázové ověřování (2FA), která tvrdí, že někdo se pokouší přistoupit k iCloud účtu uživatele. Tyto notifikace přicházejí na mobilní zařízení a e-mail. Krátce poté následují telefonáty od osob, které se představují jako agenti Apple podpory. Volají z čísel, která vypadají legitimně, a mluví klidně a profesionálně, což zesiluje dojem autenticity.

Klíčový prvek podvodu je zneužití chyby v Apple podpůrném systému. Každý může bez ověření vytvořit podpůrný ticket (support ticket) v jménu libovolného uživatele. Tento ticket pak Apple systém automaticky zpracuje a pošle uživateli oficiální e-mail z domény @apple.com s číslem ticketu a odkazem na stav. Uživatel tak vidí legitimní komunikaci přímo od Apple, což snižuje jeho ostražitost. V případě Erica Moreta podvodníci tento ticket použili k navázání telefonátu, kde ho přesvědčovali, aby sdílel ověřovací kódy nebo umožnil vzdálený přístup.

Moret popsal celý průběh krok za krokem: nejdříve falešné 2FA upozornění, pak e-mail s ticketem, následně volání s nabídkou pomoci. Podvodníci se snažili získat plný přístup k jeho Apple ID, což by znamenalo ztrátu dat z iCloud, včetně fotografií, kontaktů a plateb. Apple systém tiketů slouží k řešení problémů s produkty jako iPhone, Mac nebo službami iCloud, ale absence verifikace umožňuje jeho zneužití. Moret se podvodu vyhnul včasným odhalením, ale varuje, že setup byl natolik propracovaný, že by mnozí uživatelé podlehli. Tento případ není o zero-day exploitech, ale o sociálním inženýrství kombinovaném se systémovou slabinou.

## Proč je to důležité
Tento podvod odhaluje systémové riziko v podpůrných mechanismech velkých technologických firem, jako je Apple. Bez ověření při vytváření tiketů lze snadno generovat důvěryhodnou komunikaci, což oslabuje ochranu uživatelů. Pro miliony vlastníků Apple zařízení to znamená vyšší riziko ztráty dat a identity, zejména u méně zkušených uživatelů. V širším kontextu kyberbezpečnosti to podtrhuje nutnost zlepšení: Apple by měl zavést ověření e-mailem nebo telefonem při registraci tiketů. Uživatelé by měli vždy kontrolovat zdroje komunikace přímo v oficiálních aplikacích Apple, nikdy neodpovídat na nevyžádané volání a aktivovat pokročilé bezpečnostní funkce jako Advanced Data Protection pro iCloud. Tento incident může vést k aktualizacím v podpůrných systémech nejen Apple, ale i Google nebo Microsoft, kde podobné mechanismy existují.

---

[Číst původní článek](https://www.foxnews.com/tech/real-apple-support-emails-used-new-phishing-scam)

**Zdroj:** 📰 Fox News
