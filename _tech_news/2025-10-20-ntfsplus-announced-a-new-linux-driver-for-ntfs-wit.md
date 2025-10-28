---
category: souborové systémy
companies:
- Microsoft
date: '2025-10-20 10:32:00'
description: Namjae Jeon, vývojář exFAT ovladače pro Linux, představil NTFSPLUS -
  nový ovladač souborového systému NTFS s podporou čtení i zápisu, který má nabídnout
  lepší výkon než stávající NTFS3.
importance: 3
layout: tech_news_article
original_title: 'NTFSPLUS Announced: A New Linux Driver For NTFS With Better Performance,
  More Features - Phoronix'
publishedAt: '2025-10-20T10:32:00+00:00'
slug: ntfsplus-announced-a-new-linux-driver-for-ntfs-wit
source:
  emoji: 📰
  id: null
  name: Phoronix
title: 'NTFSPLUS: Nový linuxový ovladač pro NTFS s lepším výkonem a funkcemi'
url: https://www.phoronix.com/news/Linux-NTFSPLUS-NTFS-Driver
urlToImage: https://www.phoronix.net/image.php?id=2025&image=ntfsplus
urlToImageBackup: https://www.phoronix.net/image.php?id=2025&image=ntfsplus
---

## Souhrn

Pro Linux vznikl další ovladač souborového systému NTFS s názvem NTFSPLUS. Vývoj vede Namjae Jeon, autor linuxového ovladače exFAT a správce kódu KSMBD serveru. Nový ovladač slibuje lepší výkon a více funkcí než současný NTFS3 ovladač v jádře Linuxu.

## Klíčové body

- NTFSPLUS nabízí plnou podporu čtení i zápisu na NTFS oddíly
- Vývoj vede Namjae Jeon, zkušený vývojář linuxových ovladačů souborových systémů
- Ovladač je založen na čistším kódu původního read-only NTFS ovladače
- Implementuje moderní technologie jako iomap a obchází zastaralý buffer-head
- Má nahradit špatně udržovaný NTFS3 a zastaralý NTFS-3G v uživatelském prostoru

## Podrobnosti

Linux má v současnosti několik možností pro práci s NTFS oddíly. Původní read-only ovladač byl nedávno odstraněn z jádra. NTFS-3G funguje v uživatelském prostoru přes FUSE a nabízí podporu zápisu, ale s nižším výkonem. NTFS3 od společnosti Paragon Software byl přidán do jádra v posledních letech s podporou čtení i zápisu, ale podle Jeona trpí mnoha problémy a je špatně udržovaný.

NTFSPLUS vychází z původního read-only NTFS kódu, který Jeon označuje za mnohem čistší a lépe zdokumentovaný. Nový ovladač přidává podporu zápisu a implementuje moderní požadavky linuxového jádra. Používá iomap místo zastaralého buffer-head mechanismu, což by mělo přinést lepší výkon. Součástí projektu jsou také utility pro práci se souborovým systémem a výsledky testů pomocí xfstests.

NTFS zůstává výchozím souborovým systémem Windows, takže kvalitní podpora v Linuxu je důležitá pro interoperabilitu. Uživatelé Linuxu často potřebují pracovat s NTFS oddíly na externích discích, USB flash discích nebo při dual-boot konfiguraci s Windows. Současná situace s NTFS3 není ideální - distribuce a uživatelé stále často spoléhají na starší NTFS-3G právě kvůli problémům s NTFS3.

## Proč je to důležité

Vznik NTFSPLUS ukazuje na přetrvávající problémy s podporou NTFS v Linuxu. Skutečnost, že zkušený vývojář jako Namjae Jeon považoval za nutné vytvořit další ovladač, naznačuje vážné nedostatky stávajícího řešení NTFS3. Pro uživatele Linuxu to může znamenat spolehlivější a výkonnější práci s NTFS oddíly, což je praktické zejména při sdílení dat mezi Linux a Windows systémy. Úspěch projektu bude záviset na tom, zda se ovladač dostane do hlavní vývojové větve linuxového jádra a zda získá podporu distribucí.

---

[Číst původní článek](https://www.phoronix.com/news/Linux-NTFSPLUS-NTFS-Driver)

**Zdroj:** 📰 Phoronix
