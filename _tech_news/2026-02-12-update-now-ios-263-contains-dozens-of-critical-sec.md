---
author: Marisa Aigen
category: kyberbezpečnost
date: '2026-02-12 12:15:00'
description: Apple vydal iOS 26.3 a iPadOS 26.3 s přes 35 bezpečnostními záplatami,
  včetně opravy zero-day zranitelnosti v Dynamic Link Editor (dyld), která byla již
  využita v cílených útocích. Aktualizace chrání před neoprávněným přístupem k datům
  i na uzamčených zařízeních.
importance: 5
layout: tech_news_article
original_title: Update now! iOS 26.3 contains dozens of critical security fixes
publishedAt: '2026-02-12T12:15:00+00:00'
slug: update-now-ios-263-contains-dozens-of-critical-sec
source:
  emoji: 📰
  id: null
  name: Macworld
title: Aktualizujte nyní! iOS 26.3 obsahuje desítky kritických bezpečnostních oprav
url: https://www.macworld.com/article/3058798/update-now-ios-26-3-contains-dozens-of-critical-security-fixes.html
urlToImage: https://www.macworld.com/wp-content/uploads/2026/02/iphone-ios-update.jpg?quality=50&strip=all&w=1024
urlToImageBackup: https://www.macworld.com/wp-content/uploads/2026/02/iphone-ios-update.jpg?quality=50&strip=all&w=1024
---

## Souhrn
Apple v aktualizacích iOS 26.3, iPadOS 26.3 a odpovídajících verzích pro Mac vydal přes 35 bezpečnostních oprav, které řeší vážné zranitelnosti. Nejvážnější je zero-day chyba v Dynamic Link Editor (dyld), načítacím mechanismu knihoven pro aplikace, která umožnila spuštění libovolného kódu a byla využita v sofistikovaných útocích na vybrané cíle. Další opravy se týkají jádra systému, aplikace Photos a přístupnosti, což ohrožovalo data i na uzamčených zařízeních.

## Klíčové body
- Přes 35 bezpečnostních záplat pro iOS, iPadOS a macOS, včetně zero-day v dyld.
- Zranitelnost dyld umožnila aplikacím s možností zápisu do paměti spustit libovolný kód.
- Tři chyby v jádru (kernel), z nichž jedna umožnila získání root práv pro škodlivé aplikace.
- Chyba v aplikaci Photos umožňovala fyzickému útočníkovi prohlížet fotografie z uzamčené obrazovky.
- Dva defekty v Accessibility vystavovaly citlivé uživatelské údaje na uzamčeném zařízení.

## Podrobnosti
Apple pravidelně vydává bezpečnostní aktualizace pro své operační systémy, aby uzavřel známé zranitelnosti a zabránil neoprávněnému přístupu k zařízením a datům uživatelů. Tentokrát jde o iOS 26.3 a iPadOS 26.3, které ne přinášejí nové funkce, ale zaměřují se výhradně na bezpečnost. Podle oficiální stránky bezpečnostních aktualizací Applu obsahují tyto verze 35 oprav, z nichž některé jsou kritické.

Nejzávažnější je zero-day zranitelnost v Dynamic Link Editor (dyld), což je součást systému, která dynamicky načítá knihovny potřebné pro běh aplikací. Tato chyba umožnila aplikacím s omezenou možností zápisu do paměti provést libovolný kód, což by mohlo vést k úplné kompromitaci zařízení. Apple potvrzuje, že tato zranitelnost byla využita v extrémně sofistikovaném útoku na specifické jednotlivce používající starší verze iOS. Zero-day exploity jsou obzvláště nebezpečné, protože nejsou známy předem a útočníci je mohou použít bez varování.

Další vážné chyby se týkají jádra (kernel) operačního systému, které řídí hardware a spravuje procesy na nejnižší úrovni. Jedna z tří opravených chyb umožnila škodlivé aplikaci získat root práva, tedy nejvyšší úroveň přístupu, což by umožnilo úplnou kontrolu nad zařízením, instalaci malware nebo krádež dat. Aplikace Photos, sloužící k ukládání a prohlížení fotografií a videí, měla chybu, která umožňovala osobě s fyzickým přístupem k zařízení prohlížet obsah z uzamčené obrazovky. Podobně dva defekty v systému Accessibility, který pomáhá uživatelům se zdravotním postižením (např. voiceover, zvětšení obrazovky), umožňovaly zobrazení citlivých informací jako hesla nebo kontakty i na zamčeném displeji.

Aktualizace se vztahují i na macOS, kde je většina těchto záplat k dispozici. Apple doporučuje okamžitou instalaci, protože odložení zvyšuje riziko. Proces aktualizace probíhá přes Nastavení > Obecné > Aktualizace software, kde systém stáhne a nainstaluje opravy bez ztráty dat. Pro IT specialisty je důležité, že Apple detailně popisuje změny na své bezpečnostní stránce, včetně CVE identifikátorů pro sledování.

## Proč je to důležité
Tato aktualizace představuje reakci na reálnou bezpečnostní krizi, protože zero-day exploit v dyld byl již aktivně využíván, což ukazuje na rostoucí sofistikovanost státních aktérů nebo pokročilých hackerů cílících na Apple ekosystém. Pro miliony uživatelů iPhone, iPad a Mac znamená riziko úniku osobních dat, špionáže nebo ransomware i na zařízeních považovaných za bezpečné díky uzamknutí. V širším kontextu posiluje to důraz na pravidelné aktualizace v IT bezpečnosti, kde zero-day útoky tvoří asi 20 % všech exploitů podle zpráv firmy Google. Pro průmysl to signalizuje potřebu rychlejšího patch managementu a lepšího monitoringu, zejména v podnikovém prostředí, kde Apple zařízení dominují. Odložení aktualizace zvyšuje expozici, což by mohlo vést k větším incidentům podobným nedávným útokům na Pegasus spyware.

---

[Číst původní článek](https://www.macworld.com/article/3058798/update-now-ios-26-3-contains-dozens-of-critical-security-fixes.html)

**Zdroj:** 📰 Macworld
