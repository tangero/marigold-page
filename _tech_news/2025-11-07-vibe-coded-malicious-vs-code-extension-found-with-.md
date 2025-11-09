---
author: Marisa Aigen
category: kybernetika
companies:
- Microsoft
- OpenAI
- Google
- Apple
- NASA
date: '2025-11-07 06:48:00'
description: Útočníci využili AI k vytvoření škodlivého rozšíření pro VS Code a falešných
  balíčků v npm, čímž ukazují, jak snadno lze zneužít důvěru v open-source ekosystémy
  a vývojářské nástroje.
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
title: Zneužití AI k tvorbě škodlivého rozšíření pro VS Code s vestavěnými funkcemi
  ransomwaru
url: https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html
urlToImage: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Dcu9T1Afix71Yt-8QCNjFUC__8eCH-PwqBYQbkqtmzclCd1DmtyV89McDlT1wJxv4qRnRmxQiEFsnpzw1a0k3EMPCBIpxwJysacU-wUGg6-tCUrTKFlPVtrR3Yw4qO5Yk_trwmpT5AMqUgSkFJMEvMYJL522Wjn4FOYfFAzFaZUvZ9ufXSV82U7lUFA3/s790-rw-e365/vide-code-ransomware.jpg
urlToImageBackup: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Dcu9T1Afix71Yt-8QCNjFUC__8eCH-PwqBYQbkqtmzclCd1DmtyV89McDlT1wJxv4qRnRmxQiEFsnpzw1a0k3EMPCBIpxwJysacU-wUGg6-tCUrTKFlPVtrR3Yw4qO5Yk_trwmpT5AMqUgSkFJMEvMYJL522Wjn4FOYfFAzFaZUvZ9ufXSV82U7lUFA3/s790-rw-e365/vide-code-ransomware.jpg
---

## Souhrn
Objevené škodlivé rozšíření pro VS Code, vytvořené s využitím AI, obsahovalo vestavěné schopnosti ransomwaru a bylo doplněno falešnými balíčky v registru npm. Případ ukazuje, jak útočníci systematicky zneužívají důvěru v open-source nástroje a automatizovanou tvorbu kódu k útokům na vývojářské prostředí.

## Klíčové body
- Škodlivé VS Code rozšíření bylo navrženo tak, aby mělo schopnosti ransomwaru a manipulace se soubory.
- Útočníci použili AI k rychlé generaci a obcházení detekce kódu, včetně obfuskace a modulárního návrhu.
- Falešné balíčky v npm imitovaly legitimní knihovny a cílily na vývojáře při instalaci závislostí.
- Incident potvrzuje rostoucí trend útoků na vývojová prostředí a dodavatelský řetězec (supply chain) software.
- Organizace musí zpřísnit procesy ověřování rozšíření, balíčků a konfigurací ve vývojové infrastruktuře.

## Podrobnosti
Podvodné rozšíření pro Visual Studio Code, primárně používaný editor mezi vývojáři, bylo šířeno jako zdánlivě užitečný nástroj pro práci s kódem, ale obsahovalo mechanismy umožňující chování podobné ransomwaru. Konkrétně šlo o schopnost přistupovat k lokálním souborům projektu, upravovat je, případně je šifrovat nebo exfiltrovat, často s využitím nenápadných triggerů, jako je otevření konkrétního typu souboru nebo spuštění příkazu v prostředí editoru. Tato forma útoku je nebezpečná zejména tím, že se zaměřuje přímo na vývojáře, kteří spravují citlivý zdrojový kód, přístupové klíče, konfigurační soubory a interní API.

Kromě samotného rozšíření byly zjištěny i falešné balíčky v registru npm, které imitovaly názvy či rozhraní běžně používaných knihoven. Tyto balíčky jsou typicky nasazovány technikou typosquatting (například záměna jednoho znaku v názvu) nebo vydáváním se za "utility" či "helper" moduly. Po instalaci mohou stahovat škodlivý obsah, sbírat přihlašovací údaje, upravovat build skripty nebo vkládat zadní vrátka do produkčního kódu.

Využití AI v tomto kontextu znamená, že útočník nemusí mít hluboké programátorské schopnosti. AI nástroje jsou schopny generovat funkční rozšíření, skripty pro build systémy a obfuskovaný JavaScript tak, aby vypadal věrohodně a zároveň byl hůře čitelný při rychlé kontrole. To snižuje bariéru vstupu pro útočníky a zrychluje iteraci nových variant malwaru. Pro vývojáře a firmy to vytváří prostředí, kde standardní důvěra v populární nástroje a repozitáře přestává být bezpečná a musí být nahrazena systematickým ověřováním zdrojů, kontrolou oprávnění rozšíření a centralizovanou správou závislostí.

## Proč je to důležité
Tento incident je významný, protože potvrzuje několik trendů: přesun útočníků k dodavatelskému řetězci software, zneužívání AI k automatizaci a urychlení tvorby škodlivého kódu a cílení přímo na vývojáře jako vstupní bod do organizace. Jakmile je kompromitováno vývojové prostředí, útočník může nenápadně ovlivnit výsledný produkt, vložit zadní vrátka, získat přístupové tokeny k repozitářům či cloudovým službám a následně škálovat útok napříč infrastrukturou.

Pro průmysl to znamená nutnost zavést přísnější zásady pro používání rozšíření a balíčků: využívat interní zrcadla balíčků, provádět statickou a dynamickou analýzu kódu, omezovat oprávnění rozšíření v nástrojích jako VS Code a zavádět přehledné schvalovací procesy pro nové závislosti. Organizace by měly aktivně monitorovat neobvyklé chování v build procesech a vývojových stanicích, školit vývojáře v oblasti supply chain útoků a nespoléhat se pouze na reputaci registrů nebo počty stažení. Tento případ není izolovanou anomálií, ale ukázkou standardizující se taktiky, která bude s dalším rozšířením AI nástrojů častější a sofistikovanější.

---

[Číst původní článek](https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html)

**Zdroj:** 📰 Internet
