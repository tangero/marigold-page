---
category: mobilní zařízení
companies:
- Google
date: '2025-10-20 19:41:15'
description: Google Pixel 10 jako první Android telefon podporuje GPU akceleraci pro
  linuxové aplikace v Terminálové aplikaci díky technologii Gfxstream, což výrazně
  zlepšuje jejich výkon.
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
title: Google Pixel 10 zvládá linuxové aplikace s GPU akcelerací lépe než ostatní
  Android telefony
url: https://www.androidauthority.com/pixel-10-linux-apps-gpu-acceleration-3608754/
urlToImage: https://www.androidauthority.com/wp-content/uploads/2025/10/google-pixel-10-pro-fold-back-holding-scaled.jpg
urlToImageBackup: https://www.androidauthority.com/wp-content/uploads/2025/10/google-pixel-10-pro-fold-back-holding-scaled.jpg
---

## Souhrn

Google přidává GPU akceleraci pro grafické linuxové aplikace do Terminálové aplikace v Androidu, ale funkce je zatím dostupná výhradně pro Pixel 10. Implementace využívá knihovnu Gfxstream, která přeposílá volání grafických API z virtuálního linuxového stroje přímo na GPU hostitelského Android zařízení, což umožňuje výrazně rychlejší vykreslování než dosavadní softwarové řešení.

## Klíčové body

- Google Pixel 10 získává jako první Android telefon podporu GPU akcelerace pro linuxové aplikace v Android 16 QPR2 Beta 3
- Funkce využívá technologii Gfxstream pro přímé přeposílání grafických volání na GPU zařízení
- Dosavadní řešení používalo softwarový renderer Lavapipe, který zatěžoval CPU místo GPU
- Implementace je zatím nestabilní a nedosahuje očekávaného výkonu blížícího se nativním aplikacím
- Ostatní Android zařízení budou i po vydání Android 16 QPR2 spoléhat na pomalejší softwarové vykreslování

## Podrobnosti

Google představil Terminálovou aplikaci pro Android v březnu 2025 jako nástroj pro spouštění plnohodnotných linuxových programů prostřednictvím virtualizace. Původní verze podporovala pouze aplikace s příkazovým řádkem, ale nadcházející aktualizace Android 16 QPR2 přináší podporu pro grafické desktopové linuxové aplikace.

Problémem současného řešení je použití softwarového rendereru Lavapipe, který provádí složité výpočty a rasterizaci (převod vektorové grafiky na pixely) pomocí CPU zařízení. Tyto operace dokáže GPU provádět mnohem rychleji a efektivněji, což vytváří výkonnostní úzké hrdlo při běhu grafických aplikací.

Gfxstream je technologie pro virtualizaci grafiky, která tento problém řeší přímým přeposíláním volání grafických API z hostovaného linuxového virtuálního stroje na hostitelské Android zařízení. Tím umožňuje GPU akcelerované vykreslování linuxových aplikací. V nastavení Terminálové aplikace se objevila nová sekce "Graphics Acceleration", která tuto funkci aktivuje.

Implementace je zatím v rané fázi vývoje. Ačkoliv je funkce dostupná v Android 16 QPR2 Beta 3 pro uživatele Pixel 10, obsahuje chyby a zatím nedosahuje očekávaného výkonu blížícího se nativním aplikacím. Google pravděpodobně bude na vylepšení stability a výkonu pracovat v následujících měsících.

## Proč je to důležité

Podpora GPU akcelerace pro linuxové aplikace představuje významný krok v konvergenci mobilních a desktopových platforem. Umožňuje spouštět na Android zařízeních výkonově náročnější linuxové aplikace, které dosud nebyly použitelné kvůli nedostatečnému výkonu softwarového vykreslování.

Exkluzivita pro Pixel 10 naznačuje, že funkce vyžaduje specifickou hardwarovou nebo softwarovou podporu, kterou ostatní zařízení zatím nemají. To dává Pixel telefonům konkurenční výhodu v segmentu pokročilých uživatelů a vývojářů, kteří potřebují na mobilních zařízeních pracovat s linuxovými nástroji. Zároveň to ukazuje směr, kterým se Google vydává v rámci integrace různých platforem a rozšiřování možností Android zařízení.

---

[Číst původní článek](https://www.androidauthority.com/pixel-10-linux-apps-gpu-acceleration-3608754/)

**Zdroj:** 📰 Android Authority
