---
author: Marisa Aigen
category: kyberbezpečnost
date: '2026-01-28 18:59:38'
description: Od ruských a čínských státních agentů po obyčejné finančně motivované
  zločince všichni zneužívají dlouho opravenou zranitelnost WinRAR k šíření infostealerů
  a trojských koní pro vzdálený přístup (RAT). Chyba CVE-2025-8088 umožňuje skryté
  umístění škodlivého kódu na systém pomocí alternativních datových proudů (ADS) ve
  Windows.
importance: 5
layout: tech_news_article
original_title: Everybody is WinRAR phishing, dropping RATs as fast as lightning
publishedAt: '2026-01-28T18:59:38+00:00'
slug: everybody-is-winrar-phishing-dropping-rats-as-fast
source:
  emoji: 📰
  id: null
  name: Theregister.com
title: 'Všichni využívají WinRAR phishing: RATy se šíří rychlostí blesku'
url: https://www.theregister.com/2026/01/28/winrar_bug_under_attack/
urlToImage: https://regmedia.co.uk/2016/04/20/root_rat.jpg
urlToImageBackup: https://regmedia.co.uk/2016/04/20/root_rat.jpg
---

## Souhrn
Různé kyberzločinné skupiny, včetně ruských a čínských státních aktérů, nadále zneužívají opravenou zranitelnost CVE-2025-8088 v WinRAR k distribuci malware. Tato chyba typu cesta procházení (path traversal) umožňuje útočníkům skrýt škodlivý kód v RAR archivech a spustit ho při otevření návnady, jako je PDF soubor. Google Threat Intelligence Group varuje, že exploit cílí především na vojenské, vládní a technologické subjekty.

## Klíčové body
- Zranitelnost CVE-2025-8088 (CVSS 8.8) byla opravena ve WinRAR 7.13 v červenci 2025, ale slouží jako zero-day pro skupiny jako RomCom, APT44, Turla a čínskou skupinu.
- Exploit využívá alternativní datové proudy (ADS) v Windows k ukrytí malware v RAR souborech s návnadami.
- Ruské skupiny (RomCom, APT44/Frozenbarents, Temp.Armageddon/Carpathian, Turla/Summit) cílí ukrajinské vojenské a vládní entity.
- Čínská skupina distribuuje RAT PoisonIvy přes BAT soubor do složky Startup.
- ESET objevil a nahlásil chybu, Google potvrzuje pokračující zneužívání v lednu 2026.

## Podrobnosti
WinRAR, oblíbený nástroj pro kompresi a dekompresi souborů na Windows, obsahoval zranitelnost CVE-2025-8088, která umožňuje procházení cest (path traversal). Tato chyba umožňuje útočníkům zapisovat soubory do libovolných umístění na disku oběti. Exploit funguje tak, že útočníci vytvoří RAR archiv s návnadným souborem, například PDF dokumentem, který skrývá malware v alternativních datových prouzích (ADS) – speciální funkci Windows pro připojení metadat k souborům bez viditelných stop. Při otevření archivem ve starší verzi WinRAR se malware automaticky extrahuje a spustí, často jako infostealer pro krádež citlivých dat nebo RAT pro vzdálenou kontrolu systému.

ESET, firma specializující se na detekci pokročilých hrozeb, zranitelnost objevila a nahlásila, WinRAR ji opravil v verzi 7.13 vydané 30. července 2025. Krátce po vydání patchu ESET informoval, že skupina RomCom, známá kombinací ransomware útoků a špionáže pro Rusko, exploitovala chybu jako zero-day. RomCom používá geopolitické návnady směřující na ukrajinské cíle. Další ruské skupiny jako APT44 (také Frozenbarents), Temp.Armageddon (Carpathian) a Turla (Summit) – všechny napojené na Kremel – podobně zneužívají CVE-2025-8088 pro útoky na stejné sektory v Ukrajině.

Podle zprávy Google Threat Intelligence Group z ledna 2026 se k exploitu přidala i neidentifikovaná čínská skupina (PRC-based), která distribuuje RAT PoisonIvy – starší, ale efektivní trojský kůň pro vzdálený přístup umožňující klávesové záznamy, screenshoty a příkazovou řádku. Malware se instaluje přes BAT skript do složky Startup pro automatické spuštění. Tyto aktivity ukazují, jak běžný software jako WinRAR zůstává atraktivní vektorem i po opravě, protože mnoho uživatelů neaktualizuje.

## Proč je to důležité
Tato situace zdůrazňuje rizika zero-day exploitů v široce používaném softwaru, kde patchování nestačí bez okamžitého nasazení. Státní aktéři jako Rusko a Čína cílí kritickou infrastrukturu, což zvyšuje geopolitické napětí v kyberprostoru, zejména v kontextu války na Ukrajině. Pro uživatele a firmy znamená nutnost okamžité aktualizace WinRAR, kontroly ADS v souborech a používání sandboxů pro neznámé archivy. V širším ekosystému to ukazuje na slabiny Windows funkcí jako ADS, které usnadňují stealth útoky, a nutnost lepší detekce v antiviru. Pokračující zneužívání signalizuje, že i opravené chyby zůstávají hrozbou pro miliony systémů.

---

[Číst původní článek](https://www.theregister.com/2026/01/28/winrar_bug_under_attack/)

**Zdroj:** 📰 Theregister.com
