---
author: Marisa Aigen
category: soukromí polohy
companies:
- Apple
date: '2026-01-31 17:21:34'
description: V iOS 26.3 Apple představil novou funkci soukromí, která omezuje data
  „přesné polohy“ poskytovaná mobilním sítím přes věžové stanice. Funkce je dostupná
  pouze na zařízeních s vlastním Apple modemem z roku 2025.
importance: 4
layout: tech_news_article
original_title: Mobile carriers can get your GPS location
publishedAt: '2026-01-31T17:21:34+00:00'
slug: mobile-carriers-can-get-your-gps-location
source:
  emoji: 📰
  id: null
  name: Dywa.ng
title: Mobilní operátoři mohou získat vaši GPS polohu
url: https://an.dywa.ng/carrier-gnss.html
---

## Souhrn
Apple v systému iOS 26.3 zavedl funkci, která brání mobilním operátorům získávat přesné GNSS polohové údaje (jako GPS, GLONASS, Galileo nebo BeiDou) z připojených zařízení. Tato data byla dosud předávána automaticky přes standardní protokoly buněčných sítí, jako je RRLP pro 2G a 3G nebo LPP pro 4G a 5G. Novinka je omezena na telefony s Apple modemem z roku 2025 a poskytuje operátorům pouze nepřesné údaje z triangulace věžových stanic.

## Klíčové body
- Mobilní sítě využívají control-plane protokoly (RRLP, RRC, LPP) k automatickému získávání GNSS polohy s přesností jednotek metrů, bez vědomí uživatele.
- Apple modem v zařízeních od roku 2025 umožňuje omezit tato data na nepřesnou polohu (desítky až stovky metrů).
- Funkce je součástí iOS 26.3 a reaguje na dlouhodobé praktiky operátorů i státních orgánů, jako bylo použití DEA v USA v roce 2006.
- GNSS výpočet zůstává pasivní na zařízení, ale protokoly sítě nutí k odeslání koordinátů.

## Podrobnosti
Mobilní sítě určují polohu zařízení na základě připojení k věžovým stanicím, což poskytuje přesnost desítek až stovek metrů, zejména v době před rozšířením 5G. Tento mechanismus triangulace je známý a byl použit například v soudních případech, kde státní orgány získaly data od operátorů. Méně známé je však, že buněčné standardy obsahují protokoly pro přímé získávání přesnějších GNSS údajů. V sítích 2G a 3G slouží Radio Resources LCS Protocol (RRLP) k tomu, aby síť vyslala požadavek na zařízení, které pak bez upozornění uživatele pošle své souřadnice s přesností srovnatelnou s mapovými aplikacemi, tedy jednotky metrů. Pro 4G a 5G je tento proces řízen LTE Positioning Protocol (LPP), který funguje podobně.

Tyto protokoly patří mezi nativní control-plane mechanismy, což znamená, že probíhají v jádru buněčné komunikace a jsou uživateli neviditelné. GNSS poloha se počítá pasivně na zařízení – příjem signálů ze satelitů nevyžaduje odesílání dat zpět, podobně jako čtení dopravní značky neoznamuje nikomu vaši pozici. Přesto sítě tyto údaje získávají pravidelně. Praktické použití sahá do minulosti: v roce 2006 americká DEA získala soudní příkaz na sledování polohy telefonu přes tyto protokoly, což ukazuje na jejich dlouhodobé využití vynucovacími orgány.

Apple nyní v iOS 26.3 toto chování mění výhradně na zařízeních s vlastním modemem, který firma vyvinula a začala nasazovat v roce 2025. Tento čip umožňuje filtrovat odpovědi na požadavky sítě, takže operátoři dostanou pouze hrubou polohu z věžových stanic. Starší zařízení s modemy od Qualcomm nebo jiných dodavatelů zůstávají náchylná k plnému přenosu dat. Funkce slouží k posílení soukromí polohy a lze ji aktivovat v nastavení soukromí, kde uživatel vidí, jaké údaje se sdílejí.

## Proč je to důležité
Tato změna odhaluje dlouhodobou slabinu v soukromí mobilních zařízení a nastavuje precedens pro omezení automatického sledování operátory. V širším kontextu posiluje Apple svou pozici v boji za soukromí, podobně jako u App Tracking Transparency nebo Intelligent Tracking Prevention v Safari. Pro uživatele znamená ménší riziko neoprávneného sledování bez souhlasu, což je klíčové v éře, kdy státní i soukromé subjekty využívají polohová data k profilování. Nicméně omezení na nový hardware znamená, že většina současných iPhonů zůstane zranitelná, což kritici považují za nedostatečné řešení. Pro průmysl to tlačí dodavatele modemů k podobným funkcím a může ovlivnit standardy 5G/6G, kde přesná lokalizace slouží k optimalizaci sítě i nouzovým službám. Celkově přispívá k diskuzi o rovnováze mezi uživatelským soukromím a požadavky infrastruktury.

---

[Číst původní článek](https://an.dywa.ng/carrier-gnss.html)

**Zdroj:** 📰 Dywa.ng
