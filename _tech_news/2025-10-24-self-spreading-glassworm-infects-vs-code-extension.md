---
category: kybernetická bezpečn
companies:
- Microsoft
- Google
date: '2025-10-24 07:00:00'
description: Malware GlassWorm se šířil prostřednictvím 14 infikovaných rozšíření
  pro Visual Studio Code, ukradl přihlašovací údaje a vyprázdnil 49 kryptoměnových
  peněženek Solana.
importance: 4
layout: tech_news_article
original_title: Self-Spreading 'GlassWorm' Infects VS Code Extensions in Widespread
  Supply Chain Attack - The Hacker News
publishedAt: '2025-10-24T07:00:00+00:00'
slug: self-spreading-glassworm-infects-vs-code-extension
source:
  emoji: 📰
  id: null
  name: Internet
title: Červ GlassWorm napadl rozšíření VS Code v rozsáhlém útoku na dodavatelský řetězec
url: https://thehackernews.com/2025/10/self-spreading-glassworm-infects-vs.html
urlToImage: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghcP3Kooks9KjeygfquG2lCkBRvM1V9_zlYuOlz1vXhgU_qDiAErqbPmukvMP6fFUYJzqjCB5xavFDH8WzPA350BLCWwMXU88eP-ReBZWQGo9sfbgoh_3e5Gw_bp6cuJ2O1vercvYxepJppsOAXPuwK-R4v4WYjmKyYQ1_CpEkUSHEGlpJQu5gQYlFQIZ1/s790-rw-e365/code-vscode.jpg
urlToImageBackup: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghcP3Kooks9KjeygfquG2lCkBRvM1V9_zlYuOlz1vXhgU_qDiAErqbPmukvMP6fFUYJzqjCB5xavFDH8WzPA350BLCWwMXU88eP-ReBZWQGo9sfbgoh_3e5Gw_bp6cuJ2O1vercvYxepJppsOAXPuwK-R4v4WYjmKyYQ1_CpEkUSHEGlpJQu5gQYlFQIZ1/s790-rw-e365/code-vscode.jpg
---

## Souhrn

Bezpečnostní výzkumníci odhalili rozsáhlý útok na dodavatelský řetězec, při kterém se malware nazvaný GlassWorm šířil prostřednictvím 14 kompromitovaných rozšíření pro Visual Studio Code. Útočníci využili kombinaci command and control serverů napojených na Solana blockchain a Google Calendar, ukradli přihlašovací údaje vývojářů a vyprázdnili 49 kryptoměnových peněženek.

## Klíčové body

- GlassWorm infikoval 14 rozšíření pro VS Code, populární vývojové prostředí od Microsoftu používané miliony programátorů
- Malware využíval netradiční C2 infrastrukturu založenou na Solana blockchainu a Google Calendar pro komunikaci s útočníky
- Útok vedl ke krádeži přihlašovacích údajů vývojářů a vyprázdnění 49 kryptoměnových peněženek
- Jedná se o útok na dodavatelský řetězec, kdy kompromitované nástroje mohou infikovat tisíce dalších vývojářů
- Incident zdůrazňuje rostoucí rizika spojená s rozšířeními třetích stran ve vývojářských nástrojích

## Podrobnosti

GlassWorm představuje sofistikovanou hrozbu zaměřenou přímo na vývojářskou komunitu. Útočníci zvolili VS Code, které je podle průzkumů nejpoužívanějším editorem kódu s podílem přes 70% mezi profesionálními programátory. Kompromitováním rozšíření získali přístup k citlivým datům přímo v pracovním prostředí vývojářů.

Neobvyklá je především infrastruktura command and control. Místo tradičních serverů útočníci využili Solana blockchain a Google Calendar jako komunikační kanály. Tato technika ztěžuje detekci, protože provoz vypadá jako legitimní komunikace s běžně používanými službami. Bezpečnostní nástroje typicky neblokují přístup ke Google Calendar nebo blockchain explorers.

Malware se zaměřoval na krádež přihlašovacích údajů uložených ve VS Code, včetně tokenů pro přístup k Git repozitářům, cloud službám a dalším vývojářským nástrojům. Současně skenoval systémy obětí pro kryptoměnové peněženky, konkrétně zaměřené na ekosystém Solana. Útočníkům se podařilo vyprázdnit 49 peněženek, přičemž celková výše škody zatím nebyla zveřejněna.

Útok na dodavatelský řetězec je obzvláště nebezpečný, protože jeden kompromitovaný nástroj může infikovat tisíce dalších systémů. Vývojáři často instalují rozšíření bez důkladné kontroly, spoléhají se na reputaci marketplace a počet stažení.

## Proč je to důležité

Tento incident odhaluje zásadní bezpečnostní problém v ekosystému vývojářských nástrojů. VS Code marketplace obsahuje desítky tisíc rozšíření, z nichž většina pochází od nezávislých vývojářů nebo menších týmů. Microsoft sice provádí základní kontroly, ale sofistikované malware může projít sítem.

Útok má potenciál dalekosáhlých dopadů. Kompromitovaní vývojáři mohou neúmyslně zanést škodlivý kód do projektů, na kterých pracují, čímž se útok dále šíří. Pokud útočníci získali přístup k Git tokenům nebo cloud credentials, mohli kompromitovat celé firemní infrastruktury.

Případ GlassWorm také ukazuje rostoucí kreativitu kybernetických zločinců v oblasti C2 infrastruktury. Využití Google Calendar a blockchainu jako komunikačních kanálů je inovativní přístup, který obchází tradiční bezpečnostní opatření. Organizace budou muset přehodnotit své přístupy k monitorování síťového provozu a detekci anomálií.

---

[Číst původní článek](https://thehackernews.com/2025/10/self-spreading-glassworm-infects-vs.html)

**Zdroj:** 📰 Internet
