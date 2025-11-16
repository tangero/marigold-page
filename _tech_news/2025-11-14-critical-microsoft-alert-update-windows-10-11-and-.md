---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Microsoft
date: '2025-11-14 14:58:04'
description: Microsoft potvrdil aktivně zneužívanou zero-day zranitelnost v jádru
  Windows, která umožňuje útočníkům získat systémová oprávnění. Uživatelé musí co
  nejdříve nainstalovat bezpečnostní záplaty.
importance: 5
layout: tech_news_article
original_title: Critical Microsoft Alert — Update Windows 10, 11 And Server Right
  Now - Forbes
publishedAt: '2025-11-14T14:58:04+00:00'
slug: critical-microsoft-alert-update-windows-10-11-and-
source:
  emoji: 💼
  id: null
  name: Forbes
title: Kritické varování od Microsoftu – okamžitě aktualizujte Windows 10, 11 a Server
url: https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/
urlToImage: https://imageio.forbes.com/specials-images/imageserve/636b2aa808a3b5319a7fde55/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
urlToImageBackup: https://imageio.forbes.com/specials-images/imageserve/636b2aa808a3b5319a7fde55/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds
---

## Souhrn
Microsoft vydal urgentní bezpečnostní upozornění kvůli aktivně zneužívané zero-day zranitelnosti v jádru operačního systému Windows (CVE-2025-62215). Tato chyba umožňuje útočníkům eskalovat oprávnění a získat plnou kontrolu nad systémem. Odborníci doporučují okamžitou aktualizaci všech zařízení s Windows 10, 11 a Windows Server.

## Klíčové body
- Zranitelnost CVE-2025-62215 je umístěna v jádru Windows a již byla využita v reálných útocích.
- Útočníci pravděpodobně tuto chybu využívají až po počátečním průniku do systému (např. prostřednictvím phishingu).
- Microsoft vydal opravu v rámci nejnovějšího balíku bezpečnostních aktualizací.
- Paralelně Google vydal nouzovou opravu pro prohlížeč Chrome kvůli jiné závažné chybě.
- Celkem bylo v posledním cyklu Patch Tuesday opraveno 63 zranitelností, z toho jedna kritická zero-day.

## Podrobnosti
Zranitelnost CVE-2025-62215 je chybou typu „race condition“ v jádru Windows, která umožňuje lokální eskalaci oprávnění. Podle Satnama Naranga, senior staff research engineer ve společnosti Tenable (bezpečnostní firma specializující se na správu rizik a zranitelností), byla tato chyba potvrzena jako aktivně zneužívaná v reálném prostředí. To znamená, že útočníci ji již využívají k posílení své pozice v systému po počátečním průniku – typicky přes phishingové e-maily nebo jiné vstupní vektory. Jádro operačního systému (kernel) je nejcitlivější částí systému, a jakákoli chyba zde může vést k plné kontrole nad zařízením. Microsoft tuto zranitelnost opravil v nejnovější vlně bezpečnostních záplat, které jsou k dispozici prostřednictvím Windows Update. Uživatelé a správci IT infrastruktury by měli aktualizovat všechna zařízení bez odkladu, protože zpoždění zvyšuje riziko kompromitace.

## Proč je to důležité
Tato událost patří mezi nejzávažnější bezpečnostní incidenty v ekosystému Windows v posledních měsících. Zero-day zranitelnosti v jádru systému jsou vzácné, ale extrémně nebezpečné – umožňují útočníkům obejít všechny bezpečnostní mechanismy a získat neomezený přístup. Vzhledem k tomu, že Microsoft potvrdil aktivní zneužívání, jde o reálnou a okamžitou hrozbu pro miliony uživatelů i podnikové sítě. Současně s tím Google vydal nouzovou opravu pro Chrome, což naznačuje širší vlnu cílených útoků na klíčové softwarové platformy. Pro uživatele to znamená, že bezpečnostní aktualizace nejsou jen rutinní úkon, ale nezbytná obrana proti sofistikovaným hrozbám.

---

[Číst původní článek](https://www.forbes.com/sites/daveywinder/2025/11/14/new-microsoft-alert---update-windows-10-and-11-now-attacks-underway/)

**Zdroj:** 💼 Forbes
