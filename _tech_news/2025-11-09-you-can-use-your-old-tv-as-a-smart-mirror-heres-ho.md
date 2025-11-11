---
author: Marisa Aigen
category: hardware
date: '2025-11-09 15:17:00'
description: Návod ukazuje, jak starou funkční televizi využít jako displej pro smart
  zrcadlo s Raspberry Pi a open-source softwarem MagicMirror místo jejího vyřazení.
importance: 3
layout: tech_news_article
original_title: You Can Use Your Old TV As A Smart Mirror - Here's How - bgr.com
publishedAt: '2025-11-09T15:17:00+00:00'
slug: you-can-use-your-old-tv-as-a-smart-mirror-heres-ho
source:
  emoji: 📰
  id: null
  name: BGR
title: Jak proměnit starou televizi ve smart zrcadlo pomocí Raspberry Pi
url: https://www.bgr.com/2014813/how-to-turn-old-tv-into-smart-mirror-raspberry-pi-guide/
urlToImage: https://www.bgr.com/img/gallery/you-can-use-your-old-tv-as-a-smart-mirror-heres-how/l-intro-1761933800.jpg
urlToImageBackup: https://www.bgr.com/img/gallery/you-can-use-your-old-tv-as-a-smart-mirror-heres-how/l-intro-1761933800.jpg
---

## Souhrn
Článek popisuje praktický způsob, jak znovu využít starou televizi jako smart zrcadlo kombinující klasické zrcadlo s informačním panelem. Pomocí minipočítače Raspberry Pi, dvoucestného skla a softwaru MagicMirror lze vytvořit domácí zařízení zobrazující počasí, kalendář, zprávy či další data.

## Klíčové body
- Využití staré televize jako zobrazovací jednotky místo vyhazování či skladování.
- Použití Raspberry Pi jako řídicí jednotky s nízkou spotřebou a dobrým ekosystémem.
- Open-source software MagicMirror umožňuje modulární nastavení obsahu (počasí, kalendář, zprávy, systémy chytré domácnosti).
- Dvoucestné zrcadlo (two-way mirror) umožňuje současně vidět svůj odraz i obraz z displeje.
- Projekt je relativně dostupný pro pokročilejší domácí uživatele, ale má i technická omezení (bezpečnost, ergonomie, spotřeba).

## Podrobnosti
Základní koncept smart zrcadla spočívá v kombinaci dvoucestného zrcadla a displeje umístěného za ním. V tomto případě stará televize funguje jako zobrazovač, který za dvoucestným sklem promítá jednoduché rozhraní s vybranými informacemi. Uživatel tak při běžném pohledu do zrcadla vidí vlastní odraz i přehled dat, jako je aktuální počasí, čas, nadcházející události z kalendáře nebo titulky zpráv.

Jako výpočetní jednotka se používá Raspberry Pi, tedy levný jednodeskový počítač s nízkou spotřebou, který je vhodný pro domácí projekty a běh nenáročných UI. Doporučují se hotové startovací sady (například CanaKit nebo Vilros), které obsahují microSD kartu s Raspberry Pi OS, napájecí adaptér, HDMI kabel a ochranný kryt. Tím se snižuje bariéra pro uživatele, kteří nechtějí řešit kompatibilitu jednotlivých komponent.

Klíčovým prvkem je dvoucestné sklo (two-way mirror). Na rozdíl od běžného zrcadla umožňuje z jedné strany částečně prosvítat světlu z displeje, takže světlé prvky uživatelského rozhraní jsou viditelné, zatímco tmavé pozadí zaniká a zůstává efekt zrcadla. Je důležité volit sklo o stejné nebo větší velikosti, než je aktivní plocha televize, a počítat s bezpečným uchycením.

Software MagicMirror je open-source platforma speciálně navržená pro smart zrcadla. Umožňuje pomocí modulů zobrazovat různé informace (počasí, kalendáře Google, RSS zprávy, hodiny, integrace chytré domácnosti přes API atd.). Rozhraní je textové a kontrastní, optimalizované pro čitelnost na mírnou vzdálenost. Pro technicky zdatnější uživatele je možné vytvářet vlastní moduly nebo integrovat data z lokálních serverů, IoT zařízení či AI asistentů.

Technicky jde o poměrně přímočarý projekt, ale vyžaduje minimální znalost Linuxu (nastavení Raspberry Pi OS), správné natočení a jas televize, skrytí kabeláže, bezpečnou montáž konstrukce a případné nastavení automatického spouštění MagicMirror po startu systému. Z pohledu energetické efektivity je nutné počítat s trvalou spotřebou televize a Pi, takže dává smysl přidat časovač, ovládání přes smart zásuvku nebo režimy úspory.

## Proč je to důležité
Projekt ilustruje rostoucí trend domácího bastlení, recyklace a prodlužování životního cyklu spotřební elektroniky místo jejího rychlého nahrazování. Místo nákupu drahého komerčního smart zrcadla lze využít existující hardware a open-source software, což je ekonomicky i ekologicky racionálnější. Z technického pohledu jde o dobrý vstupní projekt pro uživatele, kteří chtějí pracovat s Raspberry Pi, integrací API, domácí automatizací a jednoduchými UI.

Pro průmysl spotřební elektroniky je tento typ návodů signálem, že uživatelé stále více hledají otevřená a upravitelná řešení, nikoli uzavřené systémy bez možnosti modifikace. Posiluje to poptávku po dokumentaci, otevřených standardech a lepší opravitelnosti zařízení. Pro výrobce smart home řešení je to ukázka, že jednoduché informační rozhraní integrované do běžných předmětů domácnosti má praktickou hodnotu, pokud zůstává modulární, čitelné a nenutí uživatele do proprietárních ekosystémů.

---

[Číst původní článek](https://www.bgr.com/2014813/how-to-turn-old-tv-into-smart-mirror-raspberry-pi-guide/)

**Zdroj:** 📰 BGR
