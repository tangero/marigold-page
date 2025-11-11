---
author: Marisa Aigen
category: hardware
companies:
- Raspberry Pi
date: '2025-11-09 15:17:00'
description: Článek ukazuje praktický postup, jak z běžné staré televize vytvořit
  chytré zrcadlo s využitím minipočítače Raspberry Pi, dvoucestného zrcadla a otevřeného
  softwaru MagicMirror.
importance: 3
layout: tech_news_article
original_title: You Can Use Your Old TV As A Smart Mirror - Here's How - bgr.com
publishedAt: '2025-11-09T15:17:00+00:00'
slug: you-can-use-your-old-tv-as-a-smart-mirror-heres-ho
source:
  emoji: 📰
  id: null
  name: BGR
title: Jak proměnit starou televizi v chytré zrcadlo pomocí Raspberry Pi a MagicMirror
url: https://www.bgr.com/2014813/how-to-turn-old-tv-into-smart-mirror-raspberry-pi-guide/
urlToImage: https://www.bgr.com/img/gallery/you-can-use-your-old-tv-as-a-smart-mirror-heres-how/l-intro-1761933800.jpg
urlToImageBackup: https://www.bgr.com/img/gallery/you-can-use-your-old-tv-as-a-smart-mirror-heres-how/l-intro-1761933800.jpg
---

## Souhrn
Starou funkční televizi lze relativně snadno přeměnit na chytré zrcadlo, které zobrazuje počasí, kalendář, zprávy nebo další užitečná data. Kombinuje se dvoucestné zrcadlo, Raspberry Pi a open-source software MagicMirror, který slouží jako modulární ovládací panel.

## Klíčové body
- Využití staré televize jako skrytého displeje za dvoucestným zrcadlem.
- Použití minipočítače Raspberry Pi jako řídicí jednotky zařízení.
- MagicMirror jako otevřený, modulární software pro zobrazování informací.
- Nízké vstupní náklady oproti komerčním chytrým zrcadlům a možnost přizpůsobení.
- Praktický příklad rozšíření chytré domácnosti bez vendor lock-in.

## Podrobnosti
Koncept chytrého zrcadla spojuje klasické zrcadlo a informační panel. Základem řešení je dvoucestné (polopropustné) zrcadlo, za kterým je umístěn displej. Pokud je displej zapnutý, uživatel vidí zároveň svůj odraz a digitální obsah; pokud je vypnutý, chová se zařízení jako běžné zrcadlo.

V tomto návodu je jako zobrazovací prvek využita stará televize. Podmínkou je plně funkční panel a možnost připojení přes HDMI. Televize je umístěna za dvoucestným zrcadlem stejné nebo mírně větší velikosti. Dvoucestné zrcadlo je nutné volit v kvalitním provedení ze skla, protože umožňuje současně dostatečný odraz i čitelnost textu a grafiky.

Řídicí jednotkou je Raspberry Pi (doporučené jsou novější modely kvůli výkonu a síťovým možnostem). Raspberry Pi je malý jednodeskový počítač používaný běžně pro prototypování, automatizaci a IoT projekty. V projektu běží Raspberry Pi OS, na němž je nainstalován MagicMirror – open-source platforma napsaná v JavaScriptu a Node.js, navržená speciálně pro chytrá zrcadla. MagicMirror umožňuje pomocí modulů zobrazovat počasí, kalendáře, dopravní informace, zprávy, hodiny, seznam úkolů a další data, přičemž konfigurace probíhá úpravou textového konfiguračního souboru.

Výhodou je plná kontrola nad daty a vzhledem – uživatel si volí, které služby a API využije, jak bude rozložení vypadat a jaké informace budou na zrcadle viditelné. Díky standardnímu HDMI připojení a nízké spotřebě Raspberry Pi jde o technicky triviálnější řešení než stavba speciálního displeje. Zároveň se tím prodlužuje životní cyklus staré televize a snižuje se množství elektroodpadu.

## Proč je to důležité
Projekt ukazuje praktický směr, jak kombinací dostupného hardwaru a otevřeného software vytvořit funkční prvek chytré domácnosti bez závislosti na uzavřených ekosystémech velkých výrobců. Chytré zrcadlo založené na Raspberry Pi a MagicMirror poskytuje flexibilitu: lze integrovat vlastní moduly, připojit lokální senzory, využít domácí server, omezit sdílení dat s externími službami a snížit dlouhodobé náklady. Pro výrobce i uživatele je to příklad, že přidaná hodnota chytré domácnosti nemusí vycházet z nákupu drahých hotových produktů, ale z chytré integrace existujícího vybavení. Z pohledu širšího technologického ekosystému jde o typický DIY projekt, který podporuje udržitelnost, rozšiřuje využití IoT platforem a ukazuje, jak lze levně a relativně bezpečně implementovat informační rozhraní do každodenního prostředí domácnosti.

---

[Číst původní článek](https://www.bgr.com/2014813/how-to-turn-old-tv-into-smart-mirror-raspberry-pi-guide/)

**Zdroj:** 📰 BGR
