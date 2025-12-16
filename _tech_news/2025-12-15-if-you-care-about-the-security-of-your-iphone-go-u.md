---
author: Marisa Aigen
category: mobilní bezpečnost
date: '2025-12-15 12:15:00'
description: Nové aktualizace iOS a iPadOS přinášejí 25 bezpečnostních oprav, včetně
  zero-day zranitelností v WebKit, které byly zneužity v sofistikovaných útocích na
  cílené jednotlivce. I pro uživatele starších verzí je k dispozici iOS/iPadOS 18.7.3
  s 20 klíčovými opravami.
importance: 5
layout: tech_news_article
original_title: If you care about the security of your iPhone, go update right now
publishedAt: '2025-12-15T12:15:00+00:00'
slug: if-you-care-about-the-security-of-your-iphone-go-u
source:
  emoji: 📰
  id: null
  name: Macworld
title: Pokud vám záleží na bezpečnosti vašeho iPhonu, aktualizujte ihned
url: https://www.macworld.com/article/3009978/if-you-care-about-the-security-of-your-iphone-go-update-right-now.html
urlToImage: https://www.macworld.com/wp-content/uploads/2025/12/ios26-2-hero-8.jpg?quality=50&strip=all&w=1024
urlToImageBackup: https://www.macworld.com/wp-content/uploads/2025/12/ios26-2-hero-8.jpg?quality=50&strip=all&w=1024
---

## Souhrn
Nové verze iOS/iPadOS 26.2 obsahují 25 bezpečnostních oprav, z nichž dvě zero-day zranitelnosti v WebKit byly podle Applu zneužity v vysoce sofistikovaném útoku na specifické cíle. Pro uživatele, kteří nemohou nebo nechtějí přejít na iOS 26, je dostupná aktualizace iOS/iPadOS 18.7.3 s 20 těmito opravami. Aktualizace řeší rizika jako arbitrární spuštění kódu přes škodlivý webový obsah.

## Klíčové body
- Zero-day chyby v WebKit umožňovaly spuštění libovolného kódu po návštěvě upraveného webu; Apple potvrzuje jejich zneužití v targeted attacku.
- Opravy v App Store (přístup k platebním tokenům), FaceTime (odhalení hesel při vzdálené kontrole) a Photos (přístup k ukrytým fotografiím bez autentizace).
- 25 oprav v iOS/iPadOS 26.2, 20 z nich v iOS/iPadOS 18.7.3.
- Další rizika zahrnují buffer overflows, race conditions a memory corruption v různých frameworkách.
- Doporučení: Okamžitá aktualizace pro všechny uživatele iPhonu a iPadu.

## Podrobnosti
Aktualizace iOS/iPadOS 26.2 a 18.7.3 se zaměřují především na bezpečnost, přestože přinášejí i nové funkce. Nejvážnější jsou dvě zranitelnosti v WebKit, což je renderingový engine používaný v Safari pro zpracování webového obsahu. Tyto chyby umožňovaly, že zpracování škodlivě upraveného webového obsahu mohlo vést k arbitrárnímu spuštění kódu na zařízení. Apple uvedl, že má zprávu o jejich využití v sofistikovaném útoku proti konkrétním jednotlivcům v předchozí verzi iOS před 26. Jedná se o zero-day exploity, tedy dříve neznámé chyby, které útočníci objevili a zneužili dříve, než je Apple opravil.

WebKit opravy nejsou ojedinělé – aktualizace řeší řadu podobných problémů, jako race conditions (závodní podmínky, kdy více procesů současně přistupují k datům), buffer overflows (přetečení bufferu, kdy data přesahují alokovaný prostor v paměti) a další triky s pamětí. Tyto chyby by po návštěvě speciálně připraveného webu umožnily útočníkům spustit svůj kód na iPhonu, což by mohlo vést k odcizení dat, instalaci malwaru nebo úplnému ovládnutí zařízení.

Další významné opravy zahrnují:
- **App Store**: Aplikace mohla získat přístup k citlivým platebním tokenům kvůli chybě v oprávněních. CVE-2025-46288, objeveno výzkumníky floeki a Zhongcheng Li z ByteDance IES Red Team (ByteDance je mateřská firma TikToku, zabývá se vývojem aplikací a bezpečnostním výzkumem).
- **FaceTime**: Při vzdálené kontrole zařízení se mohla nechtěně odhalit hesla v poli pro zadávání. CVE-2025-43542, Yiğit Ocak.
- **Photos**: Fotografie v ukrytém albu Photos byly přístupné bez autentizace. CVE-2025-43428, anonymní výzkumník a Michael Schmutzer z Technische Hochschule Ingolstadt (německá technická univerzita zaměřená na inženýrství).

Tyto opravy pokrývají širokou škálu frameworků a aplikací, což ukazuje na systematický přístup Apple k bezpečnosti. Pro uživatele znamená, že i bez upgrade na nejnovější verzi mohou získat ochranu proti známým hrozbám prostřednictvím 18.7.3.

## Proč je to důležité
Tyto zero-day exploity v WebKit podtrhují zranitelnost iPhonů vůči webovým útokům, které jsou jedním z nejčastějších vektorů pro mobilní zařízení. Cílené útoky na jednotlivce – často aktivisty, novináře nebo politiky – ukazují, že i uzavřený ekosystém Apple není neprolomný. V širším kontextu IT bezpečnosti to zdůrazňuje nutnost rychlých aktualizací, protože zero-days umožňují stealth útoky bez detekce. Pro průmysl to znamená rostoucí tlak na lepší sandboxing a memory safety v prohlížečích. Uživatelé by měli aktualizovat ihned, ale měli by si uvědomit rizika nových verzí, jako potenciální bugy v funkcích. Apple tak pokračuje v tradici reaktivních oprav, zatímco prevence zero-days zůstává výzvou pro celý sektor. (512 slov)

---

[Číst původní článek](https://www.macworld.com/article/3009978/if-you-care-about-the-security-of-your-iphone-go-update-right-now.html)

**Zdroj:** 📰 Macworld
