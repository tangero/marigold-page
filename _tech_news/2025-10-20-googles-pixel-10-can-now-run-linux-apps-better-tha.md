---
category: mobilní zařízení
companies:
- Google
date: '2025-10-20 19:41:15'
description: Google přidává do Androidu 16 QPR2 podporu GPU akcelerace pro grafické
  Linuxové aplikace, zatím ale výhradně pro Pixel 10. Využívá technologii Gfxstream
  pro přímé předávání grafických volání na GPU zařízení.
importance: 3
layout: tech_news_article
original_title: Google’s Pixel 10 can now run Linux apps better than other Android
  phones - Android Authority
publishedAt: '2025-10-20T19:41:15+00:00'
slug: googles-pixel-10-can-now-run-linux-apps-better-tha
source:
  emoji: 📰
  id: null
  name: Android Authority
title: Google Pixel 10 jako první Android zvládá plnohodnotné Linuxové aplikace s
  GPU akcelerací
url: https://www.androidauthority.com/pixel-10-linux-apps-gpu-acceleration-3608754/
urlToImage: https://www.androidauthority.com/wp-content/uploads/2025/10/google-pixel-10-pro-fold-back-holding-scaled.jpg
urlToImageBackup: https://www.androidauthority.com/wp-content/uploads/2025/10/google-pixel-10-pro-fold-back-holding-scaled.jpg
---

## Souhrn

Google zpřístupňuje GPU akceleraci pro grafické Linuxové aplikace běžící v aplikaci Terminal na Androidu, ale tato funkce je prozatím dostupná pouze na telefonech Pixel 10. Technologie Gfxstream umožňuje přímé předávání grafických API volání z virtuálního Linuxového prostředí na GPU hostitelského Android zařízení, což výrazně zrychluje vykreslování oproti dosavadnímu softwarovému renderování.

## Klíčové body

- Google v březnu 2025 představil aplikaci Linux Terminal pro Android, která využívá virtualizaci k běhu plnohodnotných Linuxových programů
- Android 16 QPR2 přidává podporu grafických desktopových Linuxových aplikací, ale na většině zařízení poběží pomalu kvůli softwarovému renderování přes Lavapipe
- Pixel 10 jako první Android telefon získává GPU akceleraci pomocí technologie Gfxstream, která přeposílá grafická volání přímo na GPU zařízení
- Funkce je dostupná v Android 16 QPR2 Beta 3, ale zatím obsahuje chyby a nedosahuje očekávaného výkonu blížícího se nativnímu běhu
- V nastavení aplikace Terminal se objevila nová sekce "Graphics Acceleration" pro správu této funkce

## Podrobnosti

Aplikace Linux Terminal pro Android funguje na principu virtualizace, kdy vytváří plnohodnotný virtuální stroj s Linuxem uvnitř Android systému. Zatímco původní verze z března 2025 podporovala pouze příkazové řádkové aplikace, nadcházející aktualizace Android 16 QPR2 rozšiřuje možnosti o grafické desktopové aplikace.

Problém dosavadního řešení spočívá v použití softwarového rendereru Lavapipe. Tento nástroj provádí veškeré složité výpočty a rasterizaci (převod vektorové grafiky na pixely) pomocí CPU procesoru. Tyto operace jsou však mnohem efektivnější, když je provádí specializovaná grafická jednotka GPU, která je pro tyto úkoly přímo navržena.

Gfxstream představuje řešení tohoto problému. Jde o knihovnu pro grafickou virtualizaci, která funguje jako most mezi hostovaným Linuxovým systémem a hardwarem Android zařízení. Místo toho, aby Linux virtuální stroj vykresloval grafiku vlastními silami, Gfxstream přeposílá grafická API volání přímo na GPU hostitelského Android zařízení. Výsledkem je výkon blížící se nativnímu běhu aplikací.

Exkluzivita pro Pixel 10 naznačuje, že implementace vyžaduje specifickou hardwarovou nebo softwarovou podporu, kterou zatím ostatní Android zařízení nemají. Google pravděpodobně testuje technologii na vlastních telefonech před širším nasazením.

## Proč je to důležité

Tato funkce představuje významný krok k propojení světa Linuxu a mobilních zařízení. Umožňuje vývojářům a pokročilým uživatelům spouštět na Android telefonech plnohodnotné desktopové nástroje, vývojářská prostředí nebo specializované aplikace, které dosud vyžadovaly počítač. GPU akcelerace je přitom klíčová pro praktickou použitelnost - bez ní by grafické aplikace běžely příliš pomalu na to, aby byly skutečně využitelné.

Zároveň jde o pokračování trendu, kdy se mobilní zařízení stávají stále univerzálnějšími výpočetními platformami. Google tak konkuruje řešením jako Samsung DeX nebo různým Linuxovým distribucím pro mobilní zařízení. Omezení na Pixel 10 však ukazuje, že masové rozšíření této funkce na Android ekosystém bude ještě nějakou dobu trvat.

---

[Číst původní článek](https://www.androidauthority.com/pixel-10-linux-apps-gpu-acceleration-3608754/)

**Zdroj:** 📰 Android Authority
