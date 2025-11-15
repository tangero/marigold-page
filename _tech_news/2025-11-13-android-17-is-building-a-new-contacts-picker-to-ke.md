---
author: Marisa Aigen
category: soukromí kontaktů
companies:
- Google
date: '2025-11-13 18:59:46'
description: Android 17 zavádí systémový nástroj pro výběr kontaktů, který umožní
  sdílet s aplikacemi pouze konkrétní kontakty místo celého adresáře.
importance: 3
layout: tech_news_article
original_title: Android 17 is building a new Contacts Picker to keep your address
  book private - Android Authority
publishedAt: '2025-11-13T18:59:46+00:00'
slug: android-17-is-building-a-new-contacts-picker-to-ke
source:
  emoji: 📰
  id: null
  name: Android Authority
title: Android 17 připravuje nový výběr kontaktů pro ochranu soukromí
url: https://www.androidauthority.com/android-17-contacts-picker-rumor-3615741/
urlToImage: https://www.androidauthority.com/wp-content/uploads/2024/04/Google-Contacts-app-logo-1.jpg
urlToImageBackup: https://www.androidauthority.com/wp-content/uploads/2024/04/Google-Contacts-app-logo-1.jpg
---

## Souhrn
Google pracuje na novém systémovém nástroji nazývaném Contacts Picker pro Android 17, který má řešit dlouhodobý problém s přístupem aplikací ke kontaktům. Místo dosavadního „vše nebo nic“ bude možné vybrat jednotlivé kontakty a sdílet s aplikací pouze tyto, a to i jen s konkrétními datovými poli.

## Klíčové body
- Nový Contacts Picker umožní sdílet pouze vybrané kontakty, nikoli celý adresář.
- Přístup bude jednorázový a omezený na konkrétní požadovaná data (např. jen telefonní číslo).
- Aplikace již nebudou potřebovat oprávnění READ_CONTACTS pro jednoduché operace jako sdílení kontaktu.
- Nástroj bude součástí systémového rozhraní Androidu, nikoli řešením na úrovni jednotlivých aplikací.

## Podrobnosti
Současný model přístupu ke kontaktům v Androidu je založen na oprávněních READ_CONTACTS a WRITE_CONTACTS. Jakmile uživatel udělí oprávnění, aplikace získá přístup ke všem kontaktům uloženým v lokální databázi zařízení, kterou spravuje systémová komponenta Contacts Provider. Tento přístup je problematický – mnoho aplikací (např. pro sdílení kontaktů, rezervace jízdenek nebo komunikaci) potřebuje pouze jeden kontakt nebo jeho část, ale musí požádat o přístup ke všem. Nový Contacts Picker bude fungovat jako systémový dialog, podobně jako výběr souborů v Androidu. Uživatel vybere konkrétní kontakt a aplikace obdrží pouze požadovaná data (např. jméno a telefon), nikoli přístup k celé databázi. Tento přístup je v souladu s principy minimalizace přístupu k soukromým datům a odpovídá podobným řešením v iOS, kde Apple zavádí kontextové výběry již několik let.

## Proč je to důležité
Tato změna posiluje soukromí uživatelů a snižuje riziko zneužití kontaktů, které jsou často cílem sběru dat pro reklamu nebo sociální grafy. Zároveň usnadňuje vývojářům implementaci funkcí bez nutnosti žádat o široká oprávnění, což může vést ke zvýšené důvěře uživatelů. V širším kontextu jde o další krok v trendu „privacy by design“, kdy operační systémy aktivně omezují přístup k citlivým datům a posouvají kontrolu do rukou uživatelů.

---

[Číst původní článek](https://www.androidauthority.com/android-17-contacts-picker-rumor-3615741/)

**Zdroj:** 📰 Android Authority
