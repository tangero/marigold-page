---

author: Marisa Aigen
category: kybernetika
companies:
- Discord
date: '2026-02-22 05:47:01'
description: Tři hacktivisti hledali obcházku ověřování věku na Discordu. Místo toho
  objevili jeho frontend vystavený na otevřeném internetu na serveru autorizovaném
  americkou vládou.
importance: 5
original_title: Hackers Expose Age-Verification Software Powering Surveillance Web
publishedAt: '2026-02-22T05:47:01+00:00'
slug: hackers-expose-age-verification-software-powering-
source:
  emoji: 📰
  id: null
  name: Therage.co
title: Hackeři odhalili software pro ověřování věku pohánějící síť sledování
url: https://www.therage.co/persona-age-verification/
urlToImage: https://www.therage.co/content/images/2026/02/the-rage-persona-age-verification.png
urlToImageBackup: https://www.therage.co/content/images/2026/02/the-rage-persona-age-verification.png
---

## Souhrn
Před deseti dny oznámila aplikace Discord zavedení nastavení „teen-by-default“ pro všechny nové i stávající uživatele po celém světě, což znamenalo omezený přístup k obsahu a povinné biometrické ověřování věku prostřednictvím startupu Persona. Bezpečnostní výzkumníci, včetně Celeste (pseudonym vmfunc), společně s dalšími dvěma kolegy hledali slabinu v tomto systému, ale místo toho odhalili exponovaný frontend software Persony na veřejném serveru. Discord v pondělí prohlásil, že s biometrickým ověřováním od Persony nepokračuje.

## Klíčové body
- Vystaveno 2 456 veřejně přístupných souborů kódu Persony na serveru autorizovaném americkou vládou.
- Software provádí rozsáhlé sledování uživatelů kombinací rozpoznávání obličeje, finančního reportování a verze přizpůsobené federálním agenturám.
- Persona je sanfranský startup podpořený Peterem Thielem s valuací 2 miliardy dolarů, nabízí řešení KYC a AML s biometrickým odhadem věku a kontrolou živosti proti AI-generovaným identitám.
- Klienti zahrnují OpenAI, Roblox, Heritage Bank a Lime; Discord byl plánován pro age-verification.
- Objev vedl k okamžitému zrušení spolupráce Discordu s Personou.

## Podrobnosti
Aplikace Discord, oblíbená pro hlasovou a textovou komunikaci mezi gamery a komunitami, oznámila aktualizaci, která měla zajistit „teen-appropriate“ prostředí pro všechny uživatele. To zahrnovalo omezené nastavení komunikace, blokování přístupu k prostorům omezeným podle věku a filtrování obsahu při zachování soukromí. Pro plný přístup bylo nutné podrobit se skenování obličeje, což vyvolalo vlnu kritiky a migraci komunit na jiné platformy.

Výzkumníci, vedení bezpečnostní expertkou Celeste (vmfunc), se pokusili najít obcházku v systému od firmy Persona Identity, Inc. Tato společnost, založená v San Franciscu a podpořená investorem Peterem Thielem, se specializuje na řešení pro ověřování identity podle principů Know Your Customer (KYC) a Anti-Money Laundering (AML). Její technologie využívá biometrické kontroly k odhadu věku uživatele pomocí proprietární kontroly živosti, která odliší reálné osoby od identit generovaných umělou inteligencí, jako jsou deepfakes. S valuací 2 miliard dolarů obsluhuje Persona velké hráče jako OpenAI pro ověřování uživatelů, Roblox pro bezpečí dětí, Heritage Bank pro finanční compliance nebo sdílecí službu Lime.

Místo slabin v ověřování výzkumníci narazili na exponovaný frontend Persony na serveru s autorizací americké vlády. V 2 456 veřejně dostupných souborech byl kód, který odhaluje hloubku sledování: rozhraní spojuje rozpoznávání obličeje s finančním reportováním a obsahuje paralelní implementaci zřejmě určenou pro federální agentury. Snímek obrazovky ukazuje notifikaci o systémech americké vlády. Tento objev zdůrazňuje rizika centralizovaných biometrických systémů, kde data o obličejích a finančních transakcích mohou být snadno zneužita.

## Proč je to důležité
Tento incident exponuje slabiny v rostoucím trendu biometrického ověřování věku na platformách jako Discord nebo Roblox, kde se snaží firmy chránit děti před nevhodným obsahem. Avšak kombinace facial recognition s finančním reportingem a vazbami na vládní servery naznačuje potenciál pro masivní surveillance, což ohrožuje soukromí milionů uživatelů. Pro průmysl to znamená nutnost přehodnocení dodavatelů jako Persona, jejíž technologie slouží k compliance v bankovnictví i AI službách, ale teď čelí kritice za nedostatečnou bezpečnost. Discordovo zrušení spolupráce ukazuje rychlou reakci, ale odhaluje širší problém: biometrická data jednou získaná nelze snadno smazat a mohou sloužit federálním agenturám k sledování. V kontextu AI-generovaných identit to zvyšuje tlak na robustnější, decentralizovaná řešení bezpečnosti, zatímco uživatelé ztrácejí důvěru v platformy nucené k takovým krokům regulacemi.

---

[Číst původní článek](https://www.therage.co/persona-age-verification/)

**Zdroj:** 📰 Therage.co
