---
author: Marisa Aigen
category: tech
date: '2025-12-02 19:53:33'
description: Konzultační firma zaměřená na open-source firmware 3mdeb zveřejnila příspěvek
  o portování svého odvozeného firmware Dasharo založeného na Coreboot na základní
  desku ASRock Rack SPC741D8/2L2T pro procesory Intel Xeon Sapphire Rapids a Emerald
  Rapids. Tento krok umožňuje širší podporu open-source řešení na recentním serverovém
  hardware.
importance: 3
layout: tech_news_article
original_title: 3mdeb Ports Their Dasharo Firmware To A Recent ASRock Rack Motherboard
publishedAt: '2025-12-02T19:53:33+00:00'
slug: A-3mdeb-ports-their-dasharo-firmware-to-a-recent-a
source:
  emoji: 📰
  id: null
  name: Phoronix
title: 3mdeb přenáší firmware Dasharo na novou serverovou základní desku ASRock Rack
url: https://www.phoronix.com/news/3mdeb-Dasharo-SPC741D8
urlToImage: https://www.phoronix.net/image.php?id=2025&image=asrock_coreboot
urlToImageBackup: https://www.phoronix.net/image.php?id=2025&image=asrock_coreboot
---

## Souhrn
Firma 3mdeb, specializující se na konzultační služby v oblasti open-source firmware, portovala svůj downstream fork Dasharo založený na Coreboot na serverovou základní desku ASRock Rack SPC741D8/2L2T. Tato deska podporuje procesory Intel Xeon ze Sapphire Rapids (4. generace) a Emerald Rapids (5. generace). Díky tomu je nyní k dispozici open-source firmware s rozšířenými funkcemi, včetně podpory spuštění Microsoft Windows 11.

## Klíčové body
- Portování Dasharo na ASRock Rack SPC741D8/2L2T, která je dostupná za 750–870 USD v online obchodech.
- Upstream Coreboot má základní podporu díky studentům z Karlsruhe Institute of Technology; 3mdeb přidala funkce z downstream větve.
- Dasharo umožňuje boot Microsoft Windows 11 a další rozšířené možnosti.
- 3mdeb prodává hotový server s touto deskou, CPU, RAM a předinstalovaným Dasharo pro okamžité použití.
- Firma dříve portovala open-source firmware na desktopové desky MSI a plánuje podporu AMD openSIL pro Ryzen/EPYC.

## Podrobnosti
Coreboot je open-source projekt nahrazující proprietární firmware jako BIOS nebo UEFI na mateřských deskách. Slouží k inicializaci hardwaru při startu počítače, umožňuje rychlejší bootování, lepší bezpečnost díky auditablemu kódu a customizaci pro specifické potřeby, například v embedded systémech nebo serverech. Dasharo je downstream fork od 3mdeb, který rozšiřuje Coreboot o proprietární prvky jako pokročilé ovladače a bezpečnostní moduly, které nejsou v upstream verzi kvůli licencím.

3mdeb převzala základní port pro ASRock Rack SPC741D8/2L2T z upstream Corebootu, který vytvořili studenti z Karlsruhe Institute of Technology. Tato deska je určená pro servery: podporuje duální socket LGA-4677 pro Xeon procesory s až 60 jádry na CPU, velké množství RAM (až 4 TB DDR5), více PCIe slotů pro GPU nebo storage a 10/25G Ethernet. 3mdeb implementovala další funkce z Dashara, jako je plná podpora periferií, bezpečnostní boot (např. TPM 2.0 pro Windows 11) a optimalizace pro stabilitu v datacentrech. Výsledek je firmware, který spolehlivě bootuje nejen Linux distribuce, ale i Windows 11, což je klíčové pro hybridní prostředí.

Pro uživatele, kteří nechtějí flashovat desku sami – což vyžaduje servisní režim a riziko znefunkčnění –, 3mdeb nabízí předkonfigurovaný server SPC741D8-2L2T/BCM s procesorem, pamětí a Dasharo. To usnadňuje nasazení open-source firmware na 4. a 5. generaci Xeon bez vendor lock-in od Intelu nebo ASRocku. Detaily portování jsou v blogu na 3mdeb.com, včetně kódu a instrukcí. Firma má zkušenosti z portů na MSI desktopové desky pro Intel a nyní cílí na AMD openSIL, což je open-source firmware pro AMD platformy sloužící k podobným účelům jako Coreboot.

## Proč je to důležité
Tento port posiluje ekosystém open-source firmware na serverovém segmentu, kde proprietární řešení dominují kvůli složitosti hardwaru. Pro datacentra a cloud providery znamená méně závislosti na dodavatelích, lepší audity proti zranitelnostem (jako Spectre/Meltdown v minulosti) a nižší náklady na customizaci. V kontextu rostoucího zájmu o suverénní hardware v EU (např. díky GAIA-X) je Dasharo praktickou alternativou. Pro IT specialisty to otevírá dveře k bezpečnějšímu nasazení Xeon serverů bez uzamčeného firmware, což je relevantní v éře edge computing a AI tréninku na serverech.

---

[Číst původní článek](https://www.phoronix.com/news/3mdeb-Dasharo-SPC741D8)

**Zdroj:** 📰 Phoronix
