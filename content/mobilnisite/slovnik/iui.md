---
slug: "iui"
url: "/mobilnisite/slovnik/iui/"
type: "slovnik"
title: "IUI – International USIM Identifier"
date: 2025-01-01
abbr: "IUI"
fullName: "International USIM Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/iui/"
summary: "IUI je jedinečný identifikátor pro USIM (Universal Subscriber Identity Module) v mobilních sítích, zavedený ve 3GPP Rel-4. Odlišuje jednotlivé aplikace USIM na kartách UICC a umožňuje zabezpečenou aut"
---

IUI je jedinečný identifikátor aplikace USIM na kartě UICC, který umožňuje zabezpečenou autentizaci účastníka a správu služeb v mobilních sítích.

## Popis

International [USIM](/mobilnisite/slovnik/usim/) Identifier (IUI) je globálně jedinečný identifikátor přiřazený aplikaci USIM (Universal Subscriber Identity Module) umístěné na UICC (Universal Integrated Circuit Card) v mobilních zařízeních. Definovaný ve specifikacích 3GPP, jako jsou TS 21.905 a TS 22.975, slouží IUI k jednoznačné identifikaci instance USIM, což je klíčové pro autentizaci účastníka, přístup k síti a poskytování služeb v sítích 3G a novějších. Funguje v rámci vrstev zabezpečení a správy identit síťové architektury a komunikuje s autentizačními centry a prvky jádra sítě za účelem ověření přihlašovacích údajů účastníka. IUI je strukturován tak, aby zajišťoval jedinečnost napříč všemi USIM na světě, typicky zahrnuje prvky odkazující na vydávající orgán nebo poskytovatele aplikace a je bezpečně uložen na UICC spolu s dalšími daty USIM, jako je [IMSI](/mobilnisite/slovnik/imsi/) a autentizační klíče. Z hlediska fungování se IUI používá během počátečních procedur připojení k síti, kdy mobilní zařízení představuje identitu USIM síti. Síť po přijetí IUI může korelovat tento identifikátor s profily účastníka v databázích, jako je [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server), a zahájit procesy autentizace a dohody o klíčích. Tento identifikátor umožňuje síti rozlišit mezi více aplikacemi USIM na jedné kartě UICC, čímž podporuje pokročilé funkce, jako jsou multi-SIM schopnosti nebo samostatné profily pro různé služby. Mezi klíčové součásti patří hardware UICC, aplikační software USIM a síťové entity jako [MME](/mobilnisite/slovnik/mme/) (Mobility Management Entity) v LTE nebo [AMF](/mobilnisite/slovnik/amf/) (Access and Mobility Management Function) v 5G, které IUI zpracovávají pro řízení přístupu. Role IUI v síti přesahuje pouhou identifikaci; usnadňuje zabezpečený roaming tím, že umožňuje navštíveným sítím identifikovat domovskou síť USIM, podporuje zákonné odposlechy poskytnutím sledovatelné identity a napomáhá předcházení podvodům tím, že zajišťuje přístup k síťovým službám pouze pro autorizované USIM. V průběhu následujících vydání 3GPP byl IUI zachován jako stabilní identifikátor, což odráží jeho zásadní důležitost v ekosystému identity účastníka, a to i při vývoji sítí od UMTS přes LTE až po 5G, kde zůstává zabezpečení založené na USIM prvořadé.

## K čemu slouží

IUI byl vytvořen za účelem poskytnutí standardizovaného, jedinečného identifikátoru pro aplikace [USIM](/mobilnisite/slovnik/usim/), který řeší potřebu přesné identifikace v kontextu vývoje mobilního zabezpečení a víceaplikačních karet UICC. Zavedený ve 3GPP Rel-4 se objevil v době rozšiřování sítí 3G a rostoucí sofistikovanosti USIM, které začaly podporovat nejen základní autentizaci, ale i přidané služby a aplikace. Motivací za zavedením IUI bylo překonání omezení dřívějších schémat identit, která nemusela dostatečně rozlišovat mezi různými instancemi USIM na jedné kartě, což by mohlo vést k bezpečnostním slabinám nebo konfliktům služeb v pokročilých síťových scénářích. Historicky se identifikátory jako [IMSI](/mobilnisite/slovnik/imsi/) zaměřovaly na účastníka, ale jak začaly karty UICC hostit více aplikací (např. pro bankovnictví nebo dopravu), stal se vyhrazený identifikátor USIM nezbytným pro správu aplikací-specifického zabezpečení a síťových interakcí. IUI řeší problémy související se zabezpečenou autentizací, umožňuje sítím jednoznačně ověřit každou aplikaci USIM, což je klíčové pro prevenci klonovacích útoků a zajištění, že přístup získají pouze legitimní USIM. Také podporuje růst komunikace mezi stroji (M2M) a IoT, kde mohou být USIM vestavěny do různorodých zařízení vyžadujících robustní správu identit. Standardizací IUI poskytlo 3GPP konzistentní rámec, který zvýšil interoperabilitu mezi operátory a dodavateli zařízení, a usnadnilo tak globální roaming a nasazení zabezpečených mobilních služeb napříč generacemi.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro aplikace USIM na kartách UICC
- Definován ve specifikacích 3GPP TS 21.905 a TS 22.975
- Podporuje zabezpečenou autentizaci a řízení přístupu k síti
- Umožňuje rozlišení mezi více USIM na jedné kartě UICC
- Usnadňuje roaming a správu identit mezi operátory
- Integruje se s bezpečnostními entitami jádra sítě, jako je HSS

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements

---

📖 **Anglický originál a plná specifikace:** [IUI na 3GPP Explorer](https://3gpp-explorer.com/glossary/iui/)
