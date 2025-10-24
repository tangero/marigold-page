---
category: windows aktualizace
companies:
- Microsoft
- BleepingComputer
date: '2025-10-21 16:56:36'
description: Microsoft potvrdil, že aktualizace Windows vydané od 29. srpna 2025 narušují
  autentizaci na systémech sdílejících duplicitní Security Identifiers (SID).
importance: 3
layout: tech_news_article
original_title: 'Microsoft: Recent Windows updates cause login issues on some PCs
  - BleepingComputer'
publishedAt: '2025-10-21T16:56:36+00:00'
slug: microsoft-recent-windows-updates-cause-login-issue
source:
  emoji: 📰
  id: null
  name: BleepingComputer
title: 'Microsoft: Nedávné aktualizace Windows způsobují problémy s přihlašováním'
url: https://www.bleepingcomputer.com/news/microsoft/microsoft-recent-windows-updates-cause-login-issues-on-pcs-sharing-security-ids/
urlToImage: https://www.bleepstatic.com/content/hl-images/2025/01/27/Windows.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2025/01/27/Windows.jpg
---

## Souhrn

Microsoft potvrdil závažný problém s aktualizacemi Windows vydanými od 29. srpna 2025, které způsobují selhání autentizace na systémech s duplicitními Security Identifiers (SID). Problém postihuje Windows 11 24H2, Windows 11 25H2 a Windows Server 2025, kde nové bezpečnostní kontroly blokují přihlašování uživatelů s platným heslem.

## Klíčové body

- Aktualizace od 29. srpna 2025 zavádějí přísnější kontroly Security Identifiers, což způsobuje selhání Kerberos a NTLM autentizace
- Postižené jsou systémy Windows 11 24H2, Windows 11 25H2 a Windows Server 2025 s duplicitními SID
- Uživatelé čelí chybám při přihlašování, nefunkčnímu vzdálenému připojení a odmítnutému přístupu k síťovým prostředkům
- Problém vzniká především při klonování nebo duplikaci instalací Windows bez správné přípravy pro imaging
- V Event Vieweru se objevují chyby SEC_E_NO_CREDENTIALS a varování o neshodě identifikátoru počítače

## Podrobnosti

Security Identifiers (SID) jsou alfanumerické řetězce, které Windows používá k identifikaci a správě uživatelských účtů, skupin a počítačových účtů. Operační systém je využívá interně pro řízení přístupu, správu oprávnění a bezpečnostní audit místo spoléhání na jména účtů. Každý SID by měl být unikátní, ale při nesprávném klonování nebo duplikaci instalací Windows mohou vzniknout duplicitní identifikátory.

Srpnové aktualizace přinesly zpřísněné bezpečnostní kontroly, které aktivně vynucují unikátnost SID. Když systém detekuje duplicitní identifikátory, autentizační handshake mezi zařízeními selže. To vede k řadě praktických problémů - uživatelé nemohou přistupovat ke vzdálené ploše, dostávají chyby "přístup odepřen" při pokusu o přístup k síťovým prostředkům a nemohou se přihlásit ani s platnými přihlašovacími údaji.

Typické chybové hlášky zahrnují "Pokus o přihlášení selhal", "Přihlášení selhalo/vaše přihlašovací údaje nefungovaly", "Částečná neshoda v identifikátoru počítače" nebo "Uživatelské jméno nebo heslo je nesprávné". V systémových protokolech se pak objevují varování, že lístek byl buď manipulován, nebo patří k jiné relaci spuštění.

Problém se týká především prostředí, kde administrátoři vytvářejí obrazy systému pro hromadné nasazení bez použití nástroje Sysprep, který zajišťuje generování unikátních SID pro každou instalaci.

## Proč je to důležité

Tato změna představuje významný zásah do fungování podnikových sítí a IT infrastruktury. Microsoft sice zvýšil bezpečnost systému, ale zároveň odhalil rozšířenou praxi nesprávné přípravy systémových obrazů. Organizace, které používaly klonování bez Sysprep, nyní čelí výpadkům a nutnosti přepracovat své postupy pro nasazování Windows. Jde o typický příklad konfliktu mezi bezpečností a zpětnou kompatibilitou, kdy oprava bezpečnostní mezery narušuje fungování systémů postavených na nesprávných postupech.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/microsoft/microsoft-recent-windows-updates-cause-login-issues-on-pcs-sharing-security-ids/)

**Zdroj:** 📰 BleepingComputer
