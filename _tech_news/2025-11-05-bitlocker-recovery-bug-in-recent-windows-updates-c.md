---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Microsoft
date: '2025-11-05 16:57:00'
description: Nedávné aktualizace Windows 10 a 11 mohou u části uživatelů vyvolat nečekanou
  obrazovku BitLocker Recovery. Pokud nemají uložený recovery klíč, hrozí ztráta přístupu
  k systému i k datům.
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
title: Chyba v aktualizacích Windows spouští BitLocker Recovery a může vést ke ztrátě
  dat
url: https://www.pcworld.com/article/2963041/bitlocker-recovery-bug-in-recent-windows-updates-could-brick-your-pc.html
urlToImage: https://www.pcworld.com/wp-content/uploads/2025/11/preboot-pin.png?w=1024
urlToImageBackup: https://www.pcworld.com/wp-content/uploads/2025/11/preboot-pin.png?w=1024
---

## Souhrn
Aktualizace Windows vydané po 14. říjnu způsobují u některých zařízení nečekané spuštění BitLocker Recovery, které vyžaduje zadání obnovovacího klíče. Uživatelé, kteří tento klíč nemají zálohovaný, riskují úplnou ztrátu přístupu k systému i datům. Problém se týká především Windows 11 verzí 24H2 a 25H2 a Windows 10 verze 22H2, zejména na zařízeních s Intel procesory a funkcí Connected Standby.

## Klíčové body
- Problém souvisí s aktualizacemi Windows vydanými po 14. říjnu.
- Dotčeny jsou Windows 11 (24H2, 25H2) a Windows 10 (22H2), hlavně na Intel zařízeních s Connected Standby.
- Systém může naběhnout do BitLocker Recovery obrazovky a vyžadovat jednorázově recovery klíč.
- Uživatelé bez uloženého recovery klíče riskují nevratnou ztrátu dat.
- Microsoft vydává opravu, ve firemním prostředí je nutné její manuální nasazení.

## Podrobnosti
Podle vyjádření Microsoftu, citovaného serverem Windows Latest, může po instalaci některé z říjnových aktualizací dojít k situaci, kdy se zařízení po restartu nespustí standardně, ale zobrazí obrazovku BitLocker Recovery. BitLocker je nástroj pro šifrování disku integrovaný ve Windows, který chrání data při ztrátě nebo odcizení zařízení. Přístup k zašifrovanému disku je v nouzových situacích podmíněn znalostí obnovovacího (recovery) klíče.

V popisovaném scénáři postižené zařízení „zamkne“ přístup k systému a vyžaduje zadání recovery klíče. Po jeho zadání by měl systém podle Microsoftu naběhnout normálně a chyba by se neměla opakovat. Problém se zjevně častěji vyskytuje na zařízeních s procesory Intel a funkcí Connected Standby, která slouží k udržení síťového připojení v režimu nízké spotřeby. To ukazuje na pravděpodobnou souvislost mezi řízením napájení, stavem šifrování a změnami zavedenými říjnovými aktualizacemi.

Kontroverzní je, že informace o chybě a jejím průběžném řešení byla zpočátku dostupná primárně uživatelům s licencemi Microsoft 365 Business a Windows 11 Enterprise, tedy firemním zákazníkům. Domácí uživatelé s Windows 10/11 Pro či Home se tak o riziku často dozvídají až ve chvíli, kdy je systém vyzve k zadání recovery klíče, který si mnozí nikdy vědomě neuložili. V takovém případě je šance na obnovu závislá na tom, zda je klíč automaticky uložen v účtu Microsoft, v Azure AD či ve firemní správě.

Microsoft uvádí, že oprava je již distribuována. Ve firemním prostředí je ale potřeba její cílené nasazení správci, aby se předešlo výpadkům pracovních stanic. Pro běžné uživatele je nyní klíčové ověřit, zda mají recovery klíče bezpečně uložené.

## Proč je to důležité
Tato chyba není jen drobný bug, ale praktický test toho, jak dobře mají uživatelé i organizace nastavené procesy pro správu šifrovacích klíčů a zálohování. BitLocker jako bezpečnostní nástroj funguje správně – brání přístupu bez klíče. Selhání nastává v kombinaci aktualizací, firmware a napájecích režimů, což spustí ochranný mechanismus v situaci, kdy k tomu z pohledu uživatele nemá dojít.

Dopady jsou výrazné: domácí uživatel může jednou nečekanou obrazovkou přijít o rodinná data, firma o pracovní stanice a citlivé dokumenty. Z pohledu ekosystému Windows to znovu otevírá otázku kvality testování aktualizací, transparentnosti komunikace směrem k nefiremním zákazníkům a nutnosti považovat správu recovery klíčů za povinnou součást základní bezpečnostní hygieny. Pro IT oddělení i pokročilé uživatele je to jasný signál zkontrolovat politiku BitLockeru, umístění klíčů (Microsoft účet, doména, MDM) a nastavení Connected Standby na kritických zařízeních.

---

[Číst původní článek](https://www.pcworld.com/article/2963041/bitlocker-recovery-bug-in-recent-windows-updates-could-brick-your-pc.html)

**Zdroj:** 📰 PCWorld
