---
author: Marisa Aigen
category: průmyslové sítě
companies:
- Red Hat
date: '2025-11-18 00:00:00'
description: V průmyslovém prostředí je předvídatelnost a přesná synchronizace kritická.
  Red Hat Enterprise Linux nyní demonstruje schopnost poskytovat deterministický výkon
  potřebný pro časově citlivé sítě (TSN) na úrovni operačního systému.
importance: 3
layout: tech_news_article
original_title: Red Hat Enterprise Linux delivers deterministic performance for time-sensitive
  networking
publishedAt: '2025-11-18T00:00:00+00:00'
slug: red-hat-enterprise-linux-delivers-deterministic-pe
source:
  emoji: 📰
  id: null
  name: Redhat.com
title: Red Hat Enterprise Linux zajišťuje deterministický výkon pro časově citlivé
  sítě
url: https://www.redhat.com/en/blog/red-hat-enterprise-linux-delivers-deterministic-performance-industrial-tsn
urlToImage: https://www.redhat.com/themes/custom/rhdc/img/red-hat-social-share.jpg
urlToImageBackup: https://www.redhat.com/themes/custom/rhdc/img/red-hat-social-share.jpg
---

## Souhrn
Red Hat Enterprise Linux (RHEL) prokázal schopnost zajistit deterministický výkon na úrovni operačního systému, což je nezbytné pro časově citlivé sítě (Time-Sensitive Networking, TSN) v průmyslových aplikacích. Společně s Intelem byla provedena technická validace, která potvrzuje, že RHEL a Red Hat Device Edge splňují nároky na přesnost a spolehlivost v reálném čase.

## Klíčové body
- Deterministický výkon je zajištěn pomocí real-time jádra v RHEL.
- Systém minimalizuje jitter způsobený přerušeními, výměnou paměti nebo náročnými aplikacemi (např. AI nebo video).
- Validace byla provedena ve spolupráci s Intelem a zaměřena na průmyslové scénáře jako řízení pohybu nebo kritické procesní smyčky.
- Red Hat Device Edge poskytuje jednotnou platformu pro edge zařízení v OT/IT prostředí.

## Podrobnosti
Časově citlivé sítě (TSN) jsou rozšířením standardu Ethernet, které zavádí determinismus a zaručený čas doručení paketů – klíčové pro průmyslovou automatizaci, kde zpoždění nebo kolísání (jitter) mohou způsobit selhání celého procesu. Avšak samotná síťová infrastruktura nestačí: operační systém na koncových zařízeních musí být schopen vytvářet a odesílat pakety s přesně definovaným časováním. Běžné operační systémy, včetně standardních distribucí Linuxu, nejsou pro tento úkol vhodné kvůli nepředvídatelnému chování plánovače úloh, zpracování přerušení nebo konkurence o systémové zdroje.

Red Hat řeší tento problém nasazením real-time jádra v RHEL, které používá deterministický plánovač, striktní řízení přerušení a minimalizaci kontextových přepínání. To umožňuje prioritním úlohám (např. řídicím algoritmům) běžet v pevně daných časových rámcích. Validace s Intelem ukázala, že RHEL dokáže udržet jitter na úrovni mikrosekund, což je v souladu s požadavky průmyslových standardů jako IEC 61158 nebo IEEE 802.1Qbv. Platforma Red Hat Device Edge navíc umožňuje správu edge zařízení v rámci jednotného operačního modelu, což usnadňuje integraci OT a IT systémů.

## Proč je to důležité
Tento krok posiluje pozici open-source řešení v průmyslové automatizaci, kde dosud dominovaly proprietární real-time systémy. Schopnost spoléhat se na standardizovaný, bezpečný a podporovaný operační systém jako RHEL snižuje náklady na vývoj a údržbu průmyslových edge zařízení. Zároveň umožňuje integraci moderních technologií – jako je AI pro prediktivní údržbu – bez ohrožení časové přesnosti kritických úloh. V kontextu růstu průmyslového IoT a konvergence OT/IT sítí je tato schopnost klíčová pro budoucí architektury průmyslových podniků.

---

[Číst původní článek](https://www.redhat.com/en/blog/red-hat-enterprise-linux-delivers-deterministic-performance-industrial-tsn)

**Zdroj:** 📰 Redhat.com
