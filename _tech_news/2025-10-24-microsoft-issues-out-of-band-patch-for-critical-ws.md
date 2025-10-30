---
category: bezpečnostní záplaty
companies:
- Microsoft
date: '2025-10-24 12:16:00'
description: Microsoft nečekaně vydal kritickou bezpečnostní záplatu pro Windows Server
  Update Services, která opravuje zranitelnost umožňující vzdálené spuštění kódu.
  Veřejně je dostupný proof-of-concept exploit.
importance: 4
layout: tech_news_article
original_title: Microsoft issues out-of-band patch for critical WSUS flaw - theregister.com
publishedAt: '2025-10-24T12:16:00+00:00'
slug: microsoft-issues-out-of-band-patch-for-critical-ws
source:
  emoji: 📰
  id: null
  name: Theregister.com
title: Microsoft vydal mimořádnou záplatu pro kritickou chybu ve WSUS
url: https://www.theregister.com/2025/10/24/windows_server_patch/
urlToImage: https://regmedia.co.uk/2015/06/17/spanner_hammer_screw_648.jpg
urlToImageBackup: https://regmedia.co.uk/2015/06/17/spanner_hammer_screw_648.jpg
---

## Souhrn

Microsoft vydal mimořádnou bezpečnostní aktualizaci pro Windows Server Update Services (WSUS) těsně před víkendem. Záplata opravuje kritickou zranitelnost CVE-2025-59287, která umožňuje neautentizovaným útočníkům vzdáleně spustit libovolný kód na postižených serverech. Problém se týká všech verzí Windows Server od 2012 do 2025 s aktivní rolí WSUS.

## Klíčové body

- Zranitelnost CVE-2025-59287 má maximální stupeň závažnosti "critical" a umožňuje vzdálené spuštění kódu (RCE)
- Příčinou je nebezpečná deserializace nedůvěryhodných dat v zastaralém serializačním mechanismu
- Veřejně je dostupný proof-of-concept exploit, což výrazně zvyšuje riziko zneužití
- Postiženy jsou pouze servery s aktivní rolí WSUS, která slouží k distribuci aktualizací Windows v podnikových sítích
- Aktualizace je kumulativní a zahrnuje i říjnové záplaty, pokud ještě nebyly nainstalovány

## Podrobnosti

Windows Server Update Services je komponenta Windows Server, která umožňuje správcům centrálně spravovat distribuci aktualizací Microsoft produktů v podnikové síti. Místo aby každý počítač stahoval aktualizace přímo z internetu, WSUS server je stáhne jednou a následně je distribuuje klientským počítačům v lokální síti.

Zranitelnost spočívá v tom, jak WSUS zpracovává příchozí data. Konkrétně jde o problém s deserializací - procesem, při kterém se data převádějí zpět do objektů v paměti. Pokud systém deserializuje nedůvěryhodná data bez řádné validace, útočník může připravit speciálně upravená data, která po deserializaci způsobí spuštění libovolného kódu na serveru.

Microsoft podle svého vyjádření identifikoval problém v "zastaralém serializačním mechanismu", což naznačuje, že jde o starší kód, který nebyl navržen s ohledem na moderní bezpečnostní standardy. To je běžný problém u Windows, které obsahuje velké množství legacy kódu z důvodu zpětné kompatibility.

Pro správce, kteří nemohou okamžitě nainstalovat záplatu, Microsoft doporučuje dvě dočasná řešení. První možností je úplné vypnutí role WSUS na postižených serverech, což ovšem znemožní distribuci aktualizací klientským počítačům. Druhá možnost je blokování příchozího provozu na portech 8530 a 8531 v hostitelském firewallu, což efektivně zastaví fungování WSUS.

Instalace aktualizace vyžaduje restart serveru, což může být problematické pro produkční prostředí, zejména když záplata přichází těsně před víkendem.

## Proč je to důležité

Tato mimořádná záplata má vysokou prioritu hned z několika důvodů. Především jde o kritickou zranitelnost umožňující vzdálené spuštění kódu bez nutnosti autentizace, což představuje extrémní bezpečnostní riziko. Útočník, který tuto zranitelnost zneužije, získá plnou kontrolu nad WSUS serverem.

Dalším zásadním faktorem je existence veřejně dostupného proof-of-concept exploitu. To znamená, že útočníci mají k dispozici funkční návod, jak zranitelnost zneužít, což dramaticky zkracuje čas mezi zveřejněním záplaty a prvními útoky v reálném prostředí.

WSUS servery jsou navíc atraktivním cílem pro útočníky, protože hrají klíčovou roli v podnikové infrastruktuře. Kompromitovaný WSUS server by mohl být zneužit k distribuci malwaru maskovaného jako legitimní aktualizace, což by útočníkovi umožnilo infikovat všechny počítače v síti.

Stojí za zmínku, že WSUS je na seznamu zastaralých technologií pro Windows Server - Microsoft jej již aktivně nevyvíjí, i když jej stále podporuje. Společnost nedávno po protestech uživatelů potvrdila, že bude pokračovat v podpoře synchronizace ovladačů do WSUS, ačkoli původně plánovala tuto podporu ukončit v dubnu 2025. To naznačuje, že Microsoft se snaží uživatele postupně přesunout na modernější řešení pro správu aktualizací.

---

[Číst původní článek](https://www.theregister.com/2025/10/24/windows_server_patch/)

**Zdroj:** 📰 Theregister.com
