---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Microsoft
date: '2025-11-05 16:57:00'
description: Nedávné aktualizace Windows způsobují u části uživatelů nečekané vyžádání
  BitLocker recovery klíče při startu systému. Pokud uživatel klíč nemá zálohovaný,
  hrozí mu ztráta přístupu k počítači i k veškerým datům.
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
title: Chyba v aktualizacích Windows vyvolává BitLocker Recovery a může vést ke ztrátě
  dat
url: https://www.pcworld.com/article/2963041/bitlocker-recovery-bug-in-recent-windows-updates-could-brick-your-pc.html
urlToImage: https://www.pcworld.com/wp-content/uploads/2025/11/preboot-pin.png?w=1024
urlToImageBackup: https://www.pcworld.com/wp-content/uploads/2025/11/preboot-pin.png?w=1024
---

## Souhrn
Nedávné aktualizace Windows 10 a Windows 11 mohou na některých zařízeních vyvolat nečekané zobrazení BitLocker recovery obrazovky a požadavek na zadání obnovovacího klíče. Uživatelé, kteří nemají BitLocker recovery key bezpečně zálohovaný, riskují úplnou ztrátu přístupu k zašifrovaným datům. Microsoft problém přiznal, vydává opravu, ale komunikace je roztříštěná a část informací je viditelná pouze pro firemní zákazníky.

## Klíčové body
- Chyba se objevuje po instalaci aktualizací vydaných od 14. října a postihuje Windows 11 (24H2, 25H2) a Windows 10 (22H2).
- Projevem je nečekané nabootování do BitLocker recovery obrazovky a požadavek na zadání recovery klíče.
- Primárně jsou zasažena zařízení s procesory Intel a funkcí Connected Standby, která umožňuje zůstat připojená k síti v úsporném režimu.
- Bez dostupného BitLocker recovery key hrozí trvalá ztráta dat, pokud je disk plně zašifrován.
- Microsoft nasazuje opravu, ale organizace ji mohou potřebovat distribuovat ručně a komunikace směrem k běžným uživatelům je nedostatečná.

## Podrobnosti
BitLocker je šifrovací technologie integrovaná ve Windows, určená k ochraně dat na discích proti neoprávněnému přístupu. Při standardním provozu se uživatel s BitLockerem většinou nesetká – ověřování probíhá automaticky pomocí TPM (Trusted Platform Module) a dalších parametrů systému. Obnovovací klíč (BitLocker recovery key) je poslední záchrana, pokud se hardware nebo konfigurace zásadně změní, nebo pokud systém považuje prostředí za nedůvěryhodné.

Po instalaci aktualizací vydaných 14. října a později začali uživatelé hlásit, že jejich zařízení po restartu přímo nabootuje do BitLocker recovery obrazovky a vyžaduje zadání obnovovacího klíče. Teprve po jeho zadání systém pokračuje a následné starty probíhají normálně bez dalšího dotazu. Microsoft ve svém prohlášení uvádí, že problém se týká zejména zařízení s procesory Intel, která podporují Connected Standby (též Modern Standby), tedy režim, v němž je zařízení v nízké spotřebě, ale zůstává připojeno k síti a přijímá aktualizace či notifikace.

Závažným aspektem je, že informace o problému byla původně zveřejněna v kanálech dostupných hlavně uživatelům Microsoft 365 Business a Windows 11 Enterprise, zatímco běžní domácí uživatelé s edicemi Pro či Home často netuší, co se děje, kde obnovovací klíč hledat a jak vyhodnotit rizika. Pokud uživatel klíč nemá uložený (například v Microsoft účtu, v Azure AD, v Active Directory nebo offline v bezpečném úložišti), může být fakticky odříznut od dat, protože obcházení BitLocker šifrování není reálně možné bez narušení bezpečnosti celého ekosystému.

Microsoft podle dostupných informací již vydává aktualizaci, která problém zmírňuje nebo eliminuje. Firemní správci by měli ověřit distribuované aktualizace, průběžně kontrolovat chování zařízení po restartu a zkontrolovat, zda mají u všech strojů správně zálohované BitLocker recovery klíče. Domácím uživatelům lze doporučit: okamžitě zkontrolovat, zda je jejich recovery key uložen v Microsoft účtu, exportovat jej do bezpečného offline úložiště a před instalací dalších aktualizací se ujistit, že mají k tomuto klíči přístup.

## Proč je to důležité
Tato chyba ukazuje praktické riziko, kdy kombinace bezpečnostních mechanismů a chybné aktualizace může legitimním uživatelům znepřístupnit jejich vlastní data. Pro oblast kybernetické bezpečnosti je to připomínka, že i správně navržené šifrování, jako je BitLocker, se stává slabým článkem nikoli kvůli kryptografii, ale kvůli procesům aktualizací, testování kompatibility a komunikaci s uživateli.

Pro firmy to znamená nutnost přísnější správy šifrovacích klíčů, centrální evidence BitLocker recovery keys, důsledného zálohování a ověřování politik před nasazením aktualizací. Pro běžné uživatele je to signál, že automaticky aktivované šifrování disků (často u nových notebooků) vyžaduje vědomý přístup k zálohování obnovovacích klíčů, jinak může jediná chybná aktualizace vést k úplné ztrátě dat. V širším kontextu to zvyšuje tlak na Microsoft, aby transparentněji komunikoval podobné incidenty i mimo podnikové kanály a aby testování aktualizací na kombinace funkcí jako Connected Standby a BitLocker bylo systematičtější.

---

[Číst původní článek](https://www.pcworld.com/article/2963041/bitlocker-recovery-bug-in-recent-windows-updates-could-brick-your-pc.html)

**Zdroj:** 📰 PCWorld
