---
author: Marisa Aigen
category: mobilní aplikace
companies:
- Google
date: '2025-11-10 23:29:00'
description: Google zavádí nový metriky pro sledování nadměrných „partial wake locks“
  v Android aplikacích. Aplikace, které výrazně zatěžují baterii na pozadí, budou
  hůře viditelné v obchodě Play a mohou dostat varovné označení pro uživatele.
importance: 3
layout: tech_news_article
original_title: Google Play will soon warn about apps that cause excessive battery
  drain - 9to5Google
publishedAt: '2025-11-10T23:29:00+00:00'
slug: google-play-will-soon-warn-about-apps-that-cause-e
source:
  emoji: 📰
  id: null
  name: 9to5google.com
title: Google Play začne varovat před aplikacemi s nadměrnou spotřebou baterie
url: http://9to5google.com/2025/11/10/google-play-battery-wake-locks/
urlToImage: https://i0.wp.com/9to5google.com/wp-content/uploads/sites/4/2024/09/Pixel-battery-widget-changes-in-Android-15.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1
urlToImageBackup: https://i0.wp.com/9to5google.com/wp-content/uploads/sites/4/2024/09/Pixel-battery-widget-changes-in-Android-15.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1
---

## Souhrn
Google zavádí do systému Android vitals novou metriku pro sledování nadměrných „partial wake locks“, tedy situací, kdy aplikace brání zařízení přejít do hlubšího spánku a tím zbytečně vybíjí baterii. Od 1. března 2026 začne Google Play omezovat viditelnost problémových aplikací a může u nich zobrazovat varování, že mohou spotřebovávat více energie na pozadí, než je očekávané.

## Klíčové body
- Google zavádí metriku „excessive partial wake locks“ vyvinutou společně se Samsungem.
- Za nadměrné se považuje, pokud aplikace drží více než 2 hodiny nevyňatých wake locks během 24 hodin.
- Prahová hodnota špatného chování je stanovena na 5 % uživatelských relací za posledních 28 dní.
- Problémové aplikace budou méně propagovány v Google Play a mohou dostat červené upozornění o nadměrné spotřebě baterie.
- Změny vstoupí v platnost 1. března 2026 a jsou doplněny o nové nástroje pro vývojáře.

## Podrobnosti
Google rozšiřuje Android vitals o metriku, která konkrétně sleduje „excessive partial wake locks“. Wake lock je mechanismus, kterým aplikace udržuje procesor nebo části systému aktivní i při zhasnuté obrazovce. Je to legitimní nástroj pro funkce jako přehrávání hudby, navigace nebo uživatelem iniciované přenosy dat, ale při nesprávném použití vede k trvalému běhu na pozadí a rychlému vybíjení baterie.

Nová definice říká, že jednotlivá uživatelská relace se považuje za nadměrnou, pokud aplikace nasbírá více než 2 hodiny kumulativních nevyňatých (non-exempt) wake locks v rámci 24 hodin. Exempt jsou pouze systémové nebo jasně uživatelsky přínosné případy, které již nelze rozumně optimalizovat – typicky audio, některé notifikace či explicitně zahájené přenosy dat. Google navíc aplikuje prahovou hodnotu špatného chování: pokud alespoň 5 % všech relací aplikace za posledních 28 dní překročí tuto hranici, aplikace je označena jako problematická.

Dopad je dvoustupňový. Za prvé, takové aplikace budou v Google Play méně viditelné: nebudou se objevovat na prominentních místech, jako jsou personalizovaná doporučení nebo výběry. Za druhé, u vybraných titulů se může objevit výrazné červené varování ve stylu „Tato aplikace může používat více baterie, než je obvyklé, kvůli vysoké aktivitě na pozadí.“ To je přímý signál pro uživatele při rozhodování o instalaci. Google zároveň poskytuje vývojářům nové diagnostické nástroje pro analýzu wake locks, aby mohli optimalizovat plánování úloh, práci se službami na pozadí a využití systémových API pro úsporu energie.

## Proč je to důležité
Tento krok je pro ekosystém Android praktický a zároveň restriktivnější vůči špatně napsaným nebo agresivním aplikacím. Uživatelský dojem z telefonu je často degradován nikoliv hardwarem, ale několika aplikacemi, které trvale drží zařízení vzhůru. Cílené měření „excessive partial wake locks“ a přímé propojení s viditelností v Google Play vytváří pro vývojáře jasný ekonomický motiv chovat se zodpovědněji.

Z hlediska bezpečnosti a transparentnosti jde o posun k modelu, kde obchod s aplikacemi aktivně upozorňuje na konkrétní technické riziko – nadměrné využití baterie na pozadí – a ne jen na oprávnění či hodnocení. To může snížit prostor pro aplikace, které zneužívají běh na pozadí například k intenzivnímu sběru dat, reklamním SDK nebo neefektivní komunikaci se serverem. Pro výrobce zařízení, jako je Samsung, které se na metrice podílely, to zároveň znamená menší tlak na hardware a méně stížností na „slabou baterii“, které jsou ve skutečnosti způsobeny softwarem. Výsledek je pragmatický: vývojáři budou nuceni optimalizovat architekturu aplikací, uživatelé získají více informací a celý ekosystém se posune k efektivnějšímu využití energie bez nutnosti zásahů na úrovni uživatelských triků a externích nástrojů.

---

[Číst původní článek](http://9to5google.com/2025/11/10/google-play-battery-wake-locks/)

**Zdroj:** 📰 9to5google.com
