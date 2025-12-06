---
author: Marisa Aigen
category: hardware
date: '2025-12-02 12:00:26'
description: Projekt ukazuje, jak postavit zařízení detekující chytré brýle Meta prostřednictvím
  Bluetooth signálu. Používá ESP32 modul k rozpoznání MAC adresy a rozsvítí varovný
  nápis „GLASSHOLE“.
importance: 3
layout: tech_news_article
original_title: Build Your Own Glasshole Detector
publishedAt: '2025-12-02T12:00:26+00:00'
slug: build-your-own-glasshole-detector
source:
  emoji: 📰
  id: null
  name: Hackaday
title: Vytvořte si vlastní detektor Glasshole
url: https://hackaday.com/2025/12/02/build-your-own-glasshole-detector/
urlToImage: https://hackaday.com/wp-content/uploads/2025/11/had_metaglass_detect_feat.png
urlToImageBackup: https://hackaday.com/wp-content/uploads/2025/11/had_metaglass_detect_feat.png
---

## Souhrn
Projekt vývojáře [sh4d0wm45k] umožňuje sestavit kompaktní detektor chytrých brýlí Meta na bázi mikrokontroléru ESP32. Zařízení skenuje Bluetooth pakety v okolí, rozpoznává specifické MAC adresy přidružené k těmto brýlím a aktivuje bílé LED diody s nápisem „GLASSHOLE“. Tento hack reaguje na obavy ze soukromí v souvislosti s nahrávajícími chytrými brýlemi.

## Klíčové body
- Použití ESP32 vývojové desky pro pasivní skenování Bluetooth paketů bez nutnosti párování.
- Detekce na základě prvních tří bajtů MAC adresy (OUI – Organizationally Unique Identifier), které identifikují výrobce zařízení.
- Custom PCB s řadami bílých LED pro vizuální upozornění.
- Open-source kód umožňující snadné přidávání dalších OUI pro jiné Bluetooth zařízení.
- Potenciál pro integraci do jiných Arduino projektů nebo přepsání pro jiné platformy.

## Podrobnosti
Vývojář [sh4d0wm45k] navrhl toto zařízení jako odpověď na rostoucí popularitu chytrých brýlí, jako jsou Ray-Ban Meta smart glasses od společnosti Meta (dříve Facebook). Tyto brýle integrují kameru, mikrofony a AI pro nahrávání videa, fotografií i zvuku, přičemž data streamují na vzdálené servery pro zpracování. ESP32, levný a výkonný mikrokontrolér s vestavěným Bluetooth Low Energy (BLE) a Wi-Fi, slouží k neustálému monitorování bezdrátového prostoru. Kód filtruje příchozí Bluetooth advertising pakety – krátké zprávy, které zařízení vysílá pro objevování se ostatními – a porovnává jejich MAC adresy s předdefinovanou databází OUI.

OUI představuje prvních šest hexadecimálních číslic (tři bajty) MAC adresy, které jednoznačně identifikují organizaci-výrobce podle standardu IEEE. Pro Meta brýle lze tuto hodnotu získat z veřejných databází nebo empirickým testováním. Pokud shoda proběhne, aktivují se LED diody na custom PCB, která obsahuje dvě řady bílých světel tvořících nápis „GLASSHOLE“ – slangový termín pro uživatele chytrých brýlí, kteří bezostyšně natáčejí okolí. Kód je minimalistický, napsaný v Arduino IDE, a zaměřuje se na efektivitu: ESP32 zpracovává pakety v reálném čase bez výrazného zatížení procesoru.

Tento přístup lze rozšířit na detekci libovolných Bluetooth zařízení tím, že uživatel přidá další OUI do konfiguračního souboru. Například lze integrovat do domácího IoT zařízení nebo přepsat pro Raspberry Pi. Historicky se debata o chytrých brýlích rozhořela s Google Glass v roce 2014, kdy uživatelé čelili sociálnímu odporu kvůli neustálému nahrávání. Meta brýle tento trend oživily díky pokročilému AI zpracování (např. rozpoznávání objektů v reálném čase), což zvyšuje rizika pro soukromí v veřejných prostorech jako bary nebo doprava.

## Proč je to důležité
Tento projekt zdůrazňuje napětí mezi pokrokem v wearables a ochranou soukromí v éře ubiquity propojených zařízení. Zatímco Meta propaguje brýle jako nástroj pro zdokumentování života, ignorují anti-sociální dopady: nechtěné nahrávání cizích lidí bez souhlasu vede k pocitům nebezpečí. Hack demonstruje, jak open-source hardware umožňuje jednotlivcům bránit se komerčním technologiím – podobně jako Bluetooth jamming proti iPhonům. V širším kontextu to stimuluje debatu o regulacích AR zařízení, kde by indikátory nahrávání nestačily. Pro developery to ukazuje praktičnost ESP32 v bezpečnostních aplikacích, potenciálně vedoucí k sofistikovanějším systémům, jako spoofing paketů pro dočasné deaktivaci detekovaných zařízení.

---

[Číst původní článek](https://hackaday.com/2025/12/02/build-your-own-glasshole-detector/)

**Zdroj:** 📰 Hackaday
