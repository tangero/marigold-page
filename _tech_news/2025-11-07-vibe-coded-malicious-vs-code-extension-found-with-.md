---
author: Marisa Aigen
category: kybernetika
companies:
- Microsoft
date: '2025-11-07 06:48:00'
description: Útočníci publikovali škodlivé rozšíření pro VS Code s funkcemi ransomwaru
  a falešné balíčky v registru npm. Incident ukazuje, jak snadno lze zneužít důvěru
  v otevřený ekosystém vývojářských nástrojů a automatizované AI generování kódu.
importance: 3
layout: tech_news_article
original_title: Vibe-Coded Malicious VS Code Extension Found with Built-In Ransomware
  Capabilities - The Hacker News
publishedAt: '2025-11-07T06:48:00+00:00'
slug: vibe-coded-malicious-vs-code-extension-found-with-
source:
  emoji: 📰
  id: null
  name: Internet
title: Zneužitá VS Code rozšíření a falešné npm balíčky ukazují nový typ cíleného
  malwaru
url: https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html
urlToImage: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Dcu9T1Afix71Yt-8QCNjFUC__8eCH-PwqBYQbkqtmzclCd1DmtyV89McDlT1wJxv4qRnRmxQiEFsnpzw1a0k3EMPCBIpxwJysacU-wUGg6-tCUrTKFlPVtrR3Yw4qO5Yk_trwmpT5AMqUgSkFJMEvMYJL522Wjn4FOYfFAzFaZUvZ9ufXSV82U7lUFA3/s790-rw-e365/vide-code-ransomware.jpg
urlToImageBackup: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Dcu9T1Afix71Yt-8QCNjFUC__8eCH-PwqBYQbkqtmzclCd1DmtyV89McDlT1wJxv4qRnRmxQiEFsnpzw1a0k3EMPCBIpxwJysacU-wUGg6-tCUrTKFlPVtrR3Yw4qO5Yk_trwmpT5AMqUgSkFJMEvMYJL522Wjn4FOYfFAzFaZUvZ9ufXSV82U7lUFA3/s790-rw-e365/vide-code-ransomware.jpg
---

## Souhrn
Útočníci zneužili ekosystém Visual Studio Code a registr npm k šíření škodlivého kódu, který simuluje nebo přímo obsahuje funkce ransomwaru. Článek ukazuje, že otevřený software a AI nástroje pro generování kódu lze relativně snadno využít k tvorbě důvěryhodně vyhlížejících, ale škodlivých rozšíření.

## Klíčové body
- Škodlivé VS Code rozšíření obsahovalo zabudované schopnosti pro šifrování souborů a potenciální ransomware útok.
- Falešné npm balíčky imitovaly legitimní knihovny a cílily na vývojáře při instalaci závislostí.
- Útočníci zjevně využili AI nástroje k generování kódu a popisů, aby zvýšili důvěryhodnost.
- Incident potvrzuje slabiny v důvěře k oficiálním marketplace a balíčkovacím registrům.
- Doporučuje se zpřísnit ověřování rozšíření, závislostí a build řetězců ve vývojářských týmech.

## Podrobnosti
Publikované informace ukazují konkrétní scénář, kdy útočníci nahráli na oficiální marketplace pro Visual Studio Code rozšíření, které se tvářilo jako užitečný nástroj pro vývojáře, ale obsahovalo skrytý škodlivý kód. Tento kód byl navržen tak, aby měl schopnosti podobné ransomwaru: přístup k souborům uživatele, možnost jejich úpravy či šifrování a komunikaci s externím serverem. Zároveň byly v ekosystému npm identifikovány falešné balíčky, které napodobovaly názvy a popisy populárních knihoven. Cílili zejména na situace, kdy vývojář udělá drobnou překlepovou chybu v názvu balíčku nebo bez kontroly přejímá konfigurace build nástrojů.

Klíčovým aspektem je využití AI při přípravě těchto útoků. AI může útočníkům pomoci generovat technicky konzistentní zdrojový kód, dokumentaci, popisy funkcí i marketingové texty, které vypadají legitimně a zapadají do běžného standardu open-source projektů. Výsledkem je, že škodlivý software vypadá profesionálně a méně vzbuzuje podezření, zejména v rychlém vývojovém prostředí, kde se na detailní manuální kontrolu každé závislosti často rezignuje.

Pro vývojáře a firmy to znamená nutnost přehodnotit způsob práce s rozšířeními a závislostmi. VS Code rozšíření i npm balíčky je nutné vybírat z ověřených zdrojů, kontrolovat historii verzí, počet stažení, reputaci autorů a v kritické infrastruktuře provádět statickou i dynamickou analýzu. Bezpečnostní týmy by měly zavést interní mirrory balíčků, schvalovací procesy pro nové závislosti a automatizované nástroje pro detekci anomálií v kódu třetích stran. Incident zapadá do širšího trendu útoků na softwarový dodavatelský řetězec, který se stává primárním vektorem namísto přímého útoku na koncové systémy.

## Proč je to důležité
Tento případ ukazuje, že důvěra v "oficiální" repozitáře a marketplace už nestačí. Útoky na vývojářské nástroje zasahují přímo do build a deployment řetězců, kde kompromitované rozšíření nebo knihovna může ovlivnit velké množství projektů současně. Zapojení AI snižuje bariéru pro tvorbu sofistikovaného malwaru a zvyšuje kvalitu podvodných projektů. Pro průmysl to znamená nutnost systematicky zabezpečovat celý životní cyklus vývoje: od lokálního prostředí vývojáře přes správu závislostí až po produkční kontejnery a runtime. Firmy, které tuto vrstvu ignorují, riskují skrytou kompromitaci kódu, únik dat nebo nasazení ransomwaru přímo z vlastního vývojového prostředí.

---

[Číst původní článek](https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html)

**Zdroj:** 📰 Internet
