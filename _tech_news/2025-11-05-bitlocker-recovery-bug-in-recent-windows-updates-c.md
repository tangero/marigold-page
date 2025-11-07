---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Microsoft
date: '2025-11-05 16:57:00'
description: Nedávné aktualizace Windows 10 a 11 způsobují, že některá zařízení náhle
  vyžadují BitLocker recovery key. Uživatelé bez zálohovaného klíče riskují kompletní
  ztrátu dat.
importance: 4
layout: tech_news_article
original_title: BitLocker recovery bug in recent Windows updates could brick your
  PC - PCWorld
publishedAt: '2025-11-05T16:57:00+00:00'
slug: bitlocker-recovery-bug-in-recent-windows-updates-c
source:
  emoji: 📰
  id: null
  name: PCWorld
title: Chyba v BitLockeru po říjnových aktualizacích Windows může znepřístupnit PC
  a vést ke ztrátě dat
url: https://www.pcworld.com/article/2963041/bitlocker-recovery-bug-in-recent-windows-updates-could-brick-your-pc.html
urlToImage: https://www.pcworld.com/wp-content/uploads/2025/11/preboot-pin.png?w=1024
urlToImageBackup: https://www.pcworld.com/wp-content/uploads/2025/11/preboot-pin.png?w=1024
---

## Souhrn
Říjnové aktualizace Windows mohou na části zařízení vyvolat nečekané zobrazení BitLocker recovery obrazovky a vyžadovat zadání obnovovacího klíče. Pokud uživatel klíč nemá bezpečně uložený, hrozí ztráta přístupu k systému i datům. Problém se týká zejména Windows 11 (24H2 a 25H2) a Windows 10 (22H2) na vybraných zařízeních s procesory Intel a funkcí Connected Standby.

## Klíčové body
- Chyba se objevuje po instalaci aktualizací vydaných od 14. října.
- Dotčeny jsou Windows 11 verze 24H2 a 25H2 a Windows 10 verze 22H2.
- Projeví se náhlým vyžádáním BitLocker recovery key při startu systému.
- Primárně jsou postižena zařízení s procesory Intel a podporou Connected Standby.
- Microsoft vydal nápravu, ale bez recovery key mohou uživatelé o svá data přijít.

## Podrobnosti
Problém se objevil po instalaci vybraných kumulativních aktualizací Windows vydaných po 14. říjnu. U části uživatelů se po restartu začala zobrazovat BitLocker recovery obrazovka, která vyžaduje zadání BitLocker recovery key. BitLocker je šifrování disku integrované ve Windows, které chrání data při ztrátě či krádeži zařízení; bez správného klíče nelze obsah disku dešifrovat.

Podle vyjádření Microsoftu, které je v plném znění dostupné zejména administrátorům s licencemi Microsoft 365 Business a Windows 11 Enterprise, jde o situaci, kdy zařízení po jednorázovém zadání obnovovacího klíče následně naběhne normálně a chyba se už neopakuje. Problém "primárně" zasahuje zařízení s procesory Intel a funkcí Connected Standby, což je režim nízké spotřeby umožňující udržet připojení k síti při uspání. Typicky jde o moderní notebooky a hybridní zařízení.

Kritický problém nastává u uživatelů, kteří svůj BitLocker recovery key nemají zálohovaný nebo o něm nevědí. V takovém případě není možné standardní cestou získat přístup k systému ani datům. Jedinou reálnou možností je zkusit klíč dohledat v účtu Microsoft (pokud bylo automatické uložení aktivní), v podnikových správcovských nástrojích (např. Azure AD / Entra ID, lokální Active Directory) nebo v dokumentaci od výrobce zařízení. Bez klíče může být nutné disk kompletně přeformátovat, což znamená ztrátu všech dat.

Microsoft uvádí, že opravná aktualizace je již distribuována. Ve firemním prostředí však může být vyžadováno ruční nebo řízené nasazení přes správcovské nástroje, což vytváří časové okno, kdy jsou zařízení potenciálně ohrožena. Zároveň je pozoruhodné, že informace o chybě nejsou jasně a transparentně komunikovány všem koncovým uživatelům, což komplikuje včasnou reakci.

## Proč je to důležité
Tento incident ukazuje rizika kombinace povinných bezpečnostních aktualizací, automatizovaného šifrování disku a nedostatečné informovanosti uživatelů. Chyba přímo neútočí na šifrování ani neoslabuje bezpečnost BitLockeru, ale efektivně působí jako "logická brick" – uživatel je uzamčen mimo vlastní zařízení. Pro domácí uživatele je to varování, že automaticky zapnutý BitLocker bez vědomí a správné správy klíčů může být problém, nikoliv jen skrytý benefit.

Pro firmy je to signál, že správa recovery klíčů a testování aktualizací není formalita, ale kritický procesní prvek kybernetické bezpečnosti. Incident zároveň ukazuje slabiny komunikace Microsoftu: klíčové informace byly cíleny hlavně na podnikové zákazníky, přestože problém dopadá i na spotřebitele. V širším kontextu to potvrzuje, že rostoucí reliance na šifrování a automatizované bezpečnostní mechanismy musí být doprovázena srozumitelným řízením klíčů, robustním zálohováním a lepším testováním aktualizací, aby nevznikaly situace, které fakticky vedou k nechtěnému zničení dat.

---

[Číst původní článek](https://www.pcworld.com/article/2963041/bitlocker-recovery-bug-in-recent-windows-updates-could-brick-your-pc.html)

**Zdroj:** 📰 PCWorld
