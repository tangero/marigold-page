---
author: Marisa Aigen
category: zabezpečení systému
companies:
- Microsoft
date: '2025-11-05 16:57:00'
description: Říjnové aktualizace Windows způsobují nečekaný požadavek na obnovovací
  klíč BitLocker. Uživatelé bez zálohy klíče riskují ztrátu všech dat na počítači.
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
title: Chyba v aktualizacích Windows vyžaduje klíč BitLocker, jinak hrozí ztráta dat
url: https://www.pcworld.com/article/2963041/bitlocker-recovery-bug-in-recent-windows-updates-could-brick-your-pc.html
urlToImage: https://www.pcworld.com/wp-content/uploads/2025/11/preboot-pin.png?w=1024
urlToImageBackup: https://www.pcworld.com/wp-content/uploads/2025/11/preboot-pin.png?w=1024
---

## Souhrn

Microsoft čelí vážnému problému s aktualizacemi Windows vydanými od 14. října 2024, které u mnoha uživatelů vyvolávají nečekaný požadavek na zadání obnovovacího klíče BitLocker. Uživatelé, kteří tento klíč nemají zálohovaný, nemohou přistoupit ke svému počítači a hrozí jim ztráta všech dat. Problém postihuje zejména zařízení s procesory Intel podporujícími funkci Connected Standby.

## Klíčové body

- Chyba se týká Windows 11 verzí 25H2 a 24H2 a Windows 10 verze 22H2
- Postižená zařízení se při startu zastaví na obrazovce BitLocker Recovery a vyžadují zadání obnovovacího klíče
- Problém se primárně projevuje u počítačů s procesory Intel podporujícími Connected Standby
- Microsoft informaci o problému zveřejnil pouze pro uživatele s licencemi Microsoft 365 Business nebo Windows 11 Enterprise
- Oprava je již distribuována, firemní uživatelé ji mohou potřebovat nasadit manuálně

## Podrobnosti

BitLocker je šifrovací technologie integrovaná do Windows, která chrání data na disku před neoprávněným přístupem. Při aktivaci vytváří obnovovací klíč - dlouhý číselný kód, který slouží jako záchranné řešení pro situace, kdy systém nemůže automaticky dešifrovat disk. Tento klíč je kritický právě v situacích, jako je aktuální problém.

Podle oficiálního prohlášení Microsoftu se chyba projevuje tak, že postižená zařízení při startu zobrazí obrazovku BitLocker Recovery místo běžného přihlášení do Windows. Uživatel musí zadat 48místný obnovovací klíč, aby mohl pokračovat. Po zadání klíče a restartu by měl počítač fungovat normálně bez dalších výzev.

Zajímavostí je, že Microsoft informaci o problému zveřejnil pouze v administrátorském centru přístupném uživatelům s business a enterprise licencemi, což znamená, že běžní uživatelé Windows mohli být překvapeni bez předchozího varování. Problém se primárně týká zařízení s procesory Intel, která podporují funkci Connected Standby - technologii umožňující zařízení zůstat připojené k síti i v úsporném režimu, podobně jako u mobilních telefonů.

Uživatelé, kteří nemají přístup ke svému obnovovacímu klíči, se ocitají v kritické situaci. Klíč může být uložen v Microsoft účtu, vytištěný na papíře, uložený v souboru nebo v případě firemních počítačů spravovaný IT oddělením prostřednictvím Active Directory. Bez tohoto klíče je přístup k zašifrovaným datům prakticky nemožný - což je sice důkazem účinnosti šifrování, ale v tomto případě nežádoucí vedlejší efekt softwarové chyby.

## Proč je to důležité

Tento incident ukazuje křehkost vztahu mezi bezpečností a použitelností v moderních operačních systémech. BitLocker je důležitá bezpečnostní funkce, která chrání citlivá data, ale její nečekané aktivování může způsobit větší škody než prospěch. Pro miliony uživatelů Windows, kteří pravděpodobně ani nevědí, že mají BitLocker aktivovaný (je ve výchozím nastavení zapnutý na mnoha zařízeních s Windows 11), představuje tento problém vážné riziko ztráty dat.

Situace také zdůrazňuje důležitost pravidelného zálohování dat a ukládání obnovovacích klíčů na bezpečné místo. Microsoft sice distribuuje opravu, ale uživatelé, kteří již do problému narazili a nemají svůj klíč, čelí potenciální ztrátě všech dat. Pro firemní prostředí to může znamenat výpadky produktivity a nutnost nasazení opravy napříč celou organizací. Incident také vyvolává otázky ohledně testování aktualizací před jejich vydáním a komunikace kritických problémů směrem k běžným uživatelům.

---

[Číst původní článek](https://www.pcworld.com/article/2963041/bitlocker-recovery-bug-in-recent-windows-updates-could-brick-your-pc.html)

**Zdroj:** 📰 PCWorld
