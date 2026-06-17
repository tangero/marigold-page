---
slug: "mae"
url: "/mobilnisite/slovnik/mae/"
type: "slovnik"
title: "MAE – MPEG-H Audio Metadata information"
date: 2025-01-01
abbr: "MAE"
fullName: "MPEG-H Audio Metadata information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mae/"
summary: "MAE označuje metadatovou informaci spojenou s MPEG-H Audio, pokročilým systémem zvukového kodeku standardizovaným pro imerzivní a interaktivní zvukové zážitky. Tato metadata umožňují funkce jako objek"
---

MAE je metadatová informace pro MPEG-H Audio, která umožňuje objektově založený zvuk, dynamickou adaptaci na přehrávací systémy a personalizované ztvárnění pro imerzivní zvukové služby v 5G vysílání.

## Popis

Metadatová informace MPEG-H Audio (MAE) zahrnuje strukturovaná data, která popisují a řídí ztvárnění bitových toků MPEG-H Audio. MPEG-H Audio ([ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 23008-3) je špičkový systém kodeku podporující kanálově založený, objektově založený a Higher Order Ambisonics ([HOA](/mobilnisite/slovnik/hoa/)) zvukový obsah. MAE není samotný zvukový signál, ale doprovodná informace, která definuje, jak má být zvuk interpretován a reprodukován.

Architektonicky je MAE vložena do nebo spojena s elementárním proudem MPEG-H Audio. Zahrnuje několik klíčových komponent: Prezentační informace, které definují, jak jsou zvukové prvky (objekty, kanály, HOA) mixovány pro různé výstupní konfigurace (např. stereo, 5.1.4, sluchátka); Interakční metadata, která umožňují uživatelský kontrolu nad zvukovými objekty (např. zesílení komentáře ve sportovním přenosu); a metadata pro řízení dynamického rozsahu ([DRC](/mobilnisite/slovnik/drc/)) pro přizpůsobení hlasitosti různým poslechovým prostředím. Metadata jsou typicky strukturována v binárním formátu definovaném standardem MPEG-H Audio.

Jak to funguje, zahrnuje dvoustupňový proces: doručení a ztvárnění. MAE je doručena spolu s komprimovanými zvukovými daty do přehrávacího zařízení, jako je smartphone, TV nebo set-top box. Dekodér a ztvárňovač MPEG-H Audio v zařízení pak tato metadata analyzují. Na základě Prezentačních informací ztvárňovač smíchá zvukové prvky tak, aby vyhovovaly konkrétnímu rozestavení reproduktorů zařízení. Interakční metadata, pokud jsou přítomna, umožňují uživatelskému rozhraní nechat posluchače upravovat parametry mixu (např. zesílení dialogů) a ztvárňovač dynamicky přizpůsobuje zvukový výstup v reálném čase. To umožňuje, aby jediný zvukový proud poskytoval optimální zážitek na čemkoli od základního stereo systému až po pokročilý domácí kino, a umožňuje uživatelskou personalizaci.

## K čemu slouží

MAE byl vyvinut, aby překonal omezení tradičních zvukových kodeků s pevným formátem (jako AC-3 nebo [AAC](/mobilnisite/slovnik/aac/)) v kontextu vyvíjejících se spotřebitelských zvukových systémů a poptávky po personalizovaných zážitcích. Tradiční kodeky dodávají pevný mix optimalizovaný pro jedno konkrétní rozestavení reproduktorů, který se často zhorší při přehrání na jiném uspořádání. Hlavním problémem, který MPEG-H Audio s MAE řeší, je dodávání budoucím potřebám přizpůsobitelného zvuku.

Jeho vytvoření bylo motivováno vzestupem objektově založené zvukové produkce ve filmu a vysílání a potřebou tento formát efektivně přenášet do domácností. MAE umožňuje, aby jediný vysílací proud nebo mediální soubor obsahoval kompletní popis zvukové scény. To umožňuje vysílatelům dodávat imerzivní služby UHDTV se zvukem, který se automaticky přizpůsobí konkrétním schopnostem přijímače diváka, ať už jde o soundbar nebo plný systém Dolby Atmos. Dále umožňuje nové interaktivní služby, jako je možnost uživatelů vybrat si preferovanou jazykovou stopu nebo upravit rovnováhu mixu mezi dialogy, efekty a hudbou. To dokonale koresponduje s cíli 5G pro vylepšenou mobilní širokopásmovou síť a mediální služby, neboť poskytuje bohatou, přizpůsobitelnou zvukovou vrstvu doplňující ultra vysokorozlišující video.

## Klíčové vlastnosti

- Umožňuje ztvárnění zvuku pro libovolné přehrávací systémy z jediného bitového toku.
- Podporuje interaktivní uživatelskou kontrolu nad zvukovými objekty a parametry mixu.
- Obsahuje Prezentační informace pro automatickou adaptaci na rozestavení reproduktorů.
- Zahrnuje metadata pro řízení dynamického rozsahu (DRC) pro konzistentní hlasitost napříč prostředími.
- Nedílná součást systému MPEG-H Audio pro imerzivní (3D) zvukové zážitky.
- Standardizovaný formát zajišťující interoperabilitu mezi zařízeními pro tvorbu obsahu a spotřebitelskými zařízeními.

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TR 28.908** (Rel-19) — AI/ML Management for 5GS

---

📖 **Anglický originál a plná specifikace:** [MAE na 3GPP Explorer](https://3gpp-explorer.com/glossary/mae/)
