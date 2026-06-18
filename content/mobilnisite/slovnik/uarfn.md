---
slug: "uarfn"
url: "/mobilnisite/slovnik/uarfn/"
type: "slovnik"
title: "UARFN – UTRA Absolute Radio Frequency Number"
date: 2025-01-01
abbr: "UARFN"
fullName: "UTRA Absolute Radio Frequency Number"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uarfn/"
summary: "Číselný identifikátor střední frekvence nosné UTRA (UMTS Terrestrial Radio Access). Poskytuje standardizovaný a jednoznačný způsob odkazování na rádiové frekvence a jejich konfiguraci v sítích 3GPP, c"
---

UARFN (UTRA Absolute Radio Frequency Number) je číselný identifikátor střední frekvence nosné UTRA, který slouží k jednoznačné identifikaci a konfiguraci rádiových frekvencí v sítích 3GPP.

## Popis

[UTRA](/mobilnisite/slovnik/utra/) Absolute Radio Frequency Number ([UARFCN](/mobilnisite/slovnik/uarfcn/)) je základní parametr v sítích UMTS a [HSPA](/mobilnisite/slovnik/hspa/), který jednoznačně identifikuje nosnou frekvenci používanou pro komunikaci mezi uživatelským zařízením (UE) a základnovou stanicí Node B. Je definován pro oba směry přenosu: pro uplink (od UE k Node B) i downlink (od Node B k UE). UARFCN je celočíselná hodnota odvozená z konkrétního vzorce založeného na skutečné nosné frekvenci v MHz. Pro režim Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)), používaný ve většině nasazení UMTS, se UARFCN pro uplink a downlink počítají odděleně kvůli párovému uspořádání spektra s pevným duplexním odstupem. Tento vzorec zajišťuje vzájemně jednoznačné přiřazení mezi fyzickou frekvencí a jejím identifikátorem UARFCN, čímž odstraňuje nejednoznačnost.

V provozu sítě je UARFCN klíčovým parametrem vysílaným buňkou v blocích systémové informace (SIBs). Uživatelské zařízení (UE) tuto informaci využívá během počátečního výběru buňky, převýběru buňky a při přechodových procedurách k naladění svého přijímače na správnou frekvenci. Systémy správy sítě také používají UARFCN pro správu rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)), frekvenční plánování a koordinaci interference. Rozsah hodnot UARFCN je definován tak, aby pokryl všechna možná provozní pásma UTRA specifikovaná 3GPP, což zajišťuje globální použitelnost.

Specifikace UARFCN je úzce spojena s číslovacím schématem kanálů UTRA. Slouží jako abstraktní vrstva, která umožňuje protokolům vyšších vrstev a konfiguračním souborům sítě odkazovat se na frekvence pomocí jednoduchého čísla namísto surové frekvenční hodnoty. To zjednodušuje softwarovou implementaci, testování a interoperabilitu. Zatímco UARFCN je specifický pro UTRA ([WCDMA](/mobilnisite/slovnik/wcdma/)), byl později pro nosné LTE definován konceptuálně podobný identifikátor [EARFCN](/mobilnisite/slovnik/earfcn/) ([E-UTRA](/mobilnisite/slovnik/e-utra/) Absolute Radio Frequency Channel Number), který pokračuje v principu absolutního číslování kanálů v systémech 3GPP.

## K čemu slouží

UARFCN byl vytvořen, aby poskytl standardizovanou, na výrobci nezávislou metodu pro identifikaci nosných frekvencí UTRA. Před standardizací mohli různí výrobci zařízení používat proprietární schémata pro odkazování na frekvence, což komplikovalo integraci sítí, roaming a nasazení s více dodavateli. UARFCN tento problém řeší zavedením jednotného a jasného číslovacího systému definovaného ve specifikacích 3GPP.

Jeho zavedení s UMTS Release 99 bylo motivováno potřebou přesné frekvenční kontroly v systémech širokopásmového CDMA. Na rozdíl od GSM, které používalo relativní ARFCN, vyžadovalo UTRA absolutní referenci kvůli své širší šířce kanálu (5 MHz) a potřebě přesné frekvenční syntézy. UARFCN umožňuje konzistentní plánování sítě v různých geografických regionech s odlišným přidělováním frekvencí (pásma UTRA) a zajišťuje, že uživatelská zařízení (UE) mohou bezproblémově objevovat a připojovat se k buňkám kdekoli na světě díky interpretaci standardizovaného čísla.

UARFCN navíc abstrahuje fyzickou frekvenci, čímž do určité míry zajišťuje budoucí kompatibilitu systému. Když byla v pozdějších vydáních 3GPP přidávána nová frekvenční pásma, vzorec pro UARFCN je mohl zahrnout bez změny základních procedur pro vyhledávání a výběr buňky. Odstranil tak omezení nejednoznačných frekvenčních odkazů a stal se základním kamenem pro automatizovanou konfiguraci sítě a funkce samoorganizujících se sítí (SON) související s frekvenčním plánováním.

## Klíčové vlastnosti

- Jednoznačně identifikuje střední frekvenci 5MHz nosné UTRA.
- Definován standardizovaným vzorcem spojujícím frekvenci (MHz) s celočíselnou hodnotou.
- Samostatné hodnoty pro uplink a downlink v režimu FDD.
- Vysílán v systémové informaci pro výběr buňky a připojení uživatelského zařízení (UE).
- Pokrývá všechna provozní pásma UTRA definovaná 3GPP.
- Umožňuje jednoznačnou frekvenční konfiguraci v systémech správy sítě.

## Související pojmy

- [EARFCN – E-UTRAN Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/earfcn/)
- [ARFCN – Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/arfcn/)
- [UTRA – Universal Terrestrial Radio Access](/mobilnisite/slovnik/utra/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [UARFN na 3GPP Explorer](https://3gpp-explorer.com/glossary/uarfn/)
