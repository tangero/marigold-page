---
slug: "aluid"
url: "/mobilnisite/slovnik/aluid/"
type: "slovnik"
title: "ALUID – Application Layer User ID"
date: 2025-01-01
abbr: "ALUID"
fullName: "Application Layer User ID"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aluid/"
summary: "ALUID je identifikátor na aplikační vrstvě pro služby 3GPP Proximity Services (ProSe), který umožňuje identifikaci uživatele a aplikace bez prozrazení trvalé mobilní identity uživatele. Poskytuje ochr"
---

ALUID je identifikátor na aplikační vrstvě pro 3GPP ProSe, který umožňuje ochranu soukromí při vyhledávání a komunikaci mezi blízkými zařízeními bez prozrazení trvalé mobilní identity uživatele.

## Popis

Application Layer User ID (ALUID) je identifikátor citlivý na soukromí definovaný v architektuře služeb 3GPP Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)), primárně specifikovaný v TS 23.303. Funguje na aplikační vrstvě, odděleně od podkladových identifikátorů mobilní sítě, jako je [IMSI](/mobilnisite/slovnik/imsi/) nebo [MSISDN](/mobilnisite/slovnik/msisdn/). ALUID používají aplikace s podporou ProSe k identifikaci uživatelů nebo zařízení během procedur ProSe Discovery a ProSe Direct Communication. Jeho hlavní funkcí je umožnit, aby byla aplikace uživatele vyhledatelná nebo mohla komunikovat s aplikacemi jiných blízkých uživatelů, a přitom chránit trvalou identitu předplatitele před odhalením přes rozhraní vzduchu.

Z architektonického hlediska je ALUID spravován ve spolupráci s funkcí ProSe v síti. Zařízení uživatele (UE s podporou ProSe) si může u funkce ProSe zaregistrovat jeden nebo více ALUID. Tyto ALUID jsou typicky odvozeny nebo namapovány z identifikátorů specifických pro aplikaci (jako je uživatelské jméno na sociální síti), ale jsou formátovány a spravovány podle specifikací 3GPP, aby byla zajištěna interoperabilita a bezpečnost v rámci systému ProSe. Funkce ProSe funguje jako důvěryhodná entita, která ověřuje ALUID a může pomáhat při vyhledávání tím, že udržuje mapování mezi ALUID a dalšími identifikátory ProSe, jako jsou ProSe Application Codes nebo ProSe Restricted Codes, v závislosti na modelu vyhledávání (např. Model A „Jsem tady“ nebo Model B „Kdo je tam?/Jsi tam?“).

Během ProSe Discovery vysílající UE vysílá ProSe Application Code, což je dočasný, často se měnící identifikátor odvozený z nebo spojený s jeho registrovaným ALUID. Monitorující UE, která tento kód přijme, může dotazovat funkci ProSe (přes rozhraní PC3), aby přeložila kód na odpovídající ALUID oznamujícího uživatele, ale pouze pokud je k tomu oprávněna podle zásad vyhledávání. Tento proces překladu umožňuje aplikaci monitorujícího uživatele identifikovat oznamujícího uživatele na aplikační vrstvě (pomocí ALUID), aniž by se kdy dozvěděla jeho mobilní identitu. Pro ProSe Direct Communication (přímé datové cesty mezi UE typu jeden k jednomu nebo jeden k mnoha) lze ALUID použít v signalizaci při navazování relace k identifikaci komunikujících stran na aplikační vrstvě.

Bezpečnostní a soukromostní aspekty ALUID jsou klíčové. Specifikace jako TS 33.303 podrobně popisují bezpečnostní mechanismy. Použití ALUID v kombinaci s efemérními ProSe Application Codes a síťově asistovaným autorizováním zabraňuje sledování trvalé identity uživatele na základě signálů vyhledávání přenášených vzduchem. Funkce ProSe zajišťuje, že překlad ALUID podléhá přísným zásadám, včetně souhlasu uživatele a kontrol předplatného. Samotný ALUID se typicky nepřenáší v čitelné podobě přes přímé rozhraní PC5 mezi zařízeními; místo toho se používají jeho odvozené dočasné kódy, což přidává další vrstvu ochrany soukromí.

## K čemu slouží

ALUID byl vytvořen, aby řešil základní problémy s identitou a soukromím, které jsou vlastní službám komunikace zařízení zařízení ([D2D](/mobilnisite/slovnik/d2d/)) založeným na blízkosti, standardizovaným v 3GPP Release 12 a novějších. Před [ProSe](/mobilnisite/slovnik/prose/) mobilní sítě primárně identifikovaly uživatele pomocí identifikátorů síťové vrstvy ([IMSI](/mobilnisite/slovnik/imsi/), [IMEI](/mobilnisite/slovnik/imei/), [MSISDN](/mobilnisite/slovnik/msisdn/)) pevně svázaných s předplatným a SIM kartou. Přímé použití těchto identifikátorů pro vyhledávání mezi blízkými zařízeními přenášené vzduchem by vytvořilo vážná rizika pro soukromí, umožňující sledování, profilování a nevyžádaný kontakt. Dále vývojáři aplikací potřebovali způsob, jak integrovat uživatelské identity z vlastních ekosystémů (např. uživatelská jména v aplikacích) s podkladovou mechanikou služby blízkosti 3GPP.

Hlavní problém, který ALUID řeší, je umožnit rozpoznatelnost uživatele a aplikace pro služby blízkosti a zároveň vynutit ochranu soukromí již při návrhu. Umožňuje, aby byla pro vyhledávání a komunikaci použita sociální, bezpečnostní nebo komerční aplikační identita uživatele, aniž by byla tato identita přímo spojena s jeho soukromou, fakturovatelnou mobilní identitou. Toto oddělení bylo zásadní pro soulad s předpisy (např. pro služby veřejné bezpečnosti používané vládními agenturami) a pro přijetí uživateli u komerčních funkcí typu „najít lidi v okolí“. Motivace vycházela z případů užití, jako je komunikace mezi záchranáři veřejné bezpečnosti, vyhledávání na sociálních sítích a místní reklama, které všechny vyžadují nějakou představu uživatelské identity, ale musí chránit soukromí předplatitele.

ALUID také poskytuje standardizované rozhraní mezi možnostmi sítě 3GPP ProSe a nadstavbovými aplikacemi. Definováním formálního identifikátoru aplikační vrstvy umožnilo 3GPP aplikačním serverům a funkcím ProSe vzájemně bezpečně spolupracovat (přes rozhraní jako PC2 a PC4). To umožňuje síťovým operátorům nabízet ProSe jako podpůrnou službu poskytovatelům aplikací, kteří pak mohou používat ALUID k identifikaci svých uživatelů v rámci systému ProSe, což usnadňuje vznik ekosystému služeb přesahujícího pouhé síťové připojení.

## Klíčové vlastnosti

- Identifikace uživatele s ochranou soukromí pro vyhledávání přenášené vzduchem
- Oddělení od trvalých identifikátorů předplatitele (IMSI, MSISDN)
- Sémantika aplikační vrstvy, mapovatelná na uživatelská jména specifická pro aplikaci
- Spravován a ověřován síťovou funkcí ProSe
- Používá se v procedurách ProSe Discovery i ProSe Direct Communication
- Umožňuje autorizační zásady založené na souhlasu uživatele a předplatném

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 23.303** (Rel-19) — Proximity Services (ProSe) Stage 2
- **TS 29.343** (Rel-19) — PC2 Reference Point Stage 3 Specification
- **TS 29.345** (Rel-19) — Diameter-based PC6/PC7 interfaces for ProSe
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS

---

📖 **Anglický originál a plná specifikace:** [ALUID na 3GPP Explorer](https://3gpp-explorer.com/glossary/aluid/)
