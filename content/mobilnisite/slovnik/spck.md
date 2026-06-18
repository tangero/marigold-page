---
slug: "spck"
url: "/mobilnisite/slovnik/spck/"
type: "slovnik"
title: "SPCK – Service Provider Control Key"
date: 2025-01-01
abbr: "SPCK"
fullName: "Service Provider Control Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/spck/"
summary: "Kryptografický klíč používaný v systémech 3GPP k ověřování a zabezpečení komunikace mezi uživatelským zařízením (UE) a sítěmi poskytovatele služeb, který umožňuje řízený přístup k službám. Zajišťuje,"
---

SPCK je kryptografický klíč používaný v systémech 3GPP k ověřování a zabezpečení komunikace mezi uživatelským zařízením (UE) a sítěmi poskytovatele služeb, který umožňuje řízený přístup k službám pro autorizované uživatele.

## Popis

Service Provider Control Key (SPCK, klíč pro řízení poskytovatele služeb) je bezpečnostní mechanismus definovaný ve specifikacích 3GPP, například v TS 22.022, používaný k ověřování a řízení přístupu ke službám poskytovaným síťovými operátory nebo poskytovateli služeb třetích stran. Jedná se o kryptografický klíč, který je typicky bezpečně uložen v univerzální čipové kartě (UICC) uživatelského zařízení (UE) nebo v embedded [SIM](/mobilnisite/slovnik/sim/), a je využíván v ověřovacích protokolech k ověření autorizace UE pro konkrétní služby. SPCK funguje v rámci širší architektury zabezpečení 3GPP, spolupracuje s autentizačními centry (AuC) a home subscriber servery ([HSS](/mobilnisite/slovnik/hss/)) k validaci požadavků na služby.

Z architektonického hlediska je SPCK součástí hierarchie klíčů v systémech 3GPP, často odvozený z hlavních klíčů, jako je Ki (ověřovací klíč), nebo generovaný nezávisle pro účely specifické pro službu. Používá se v mechanismech výzva-odpověď, kde síť odešle náhodnou výzvu do UE, které vypočítá odpověď pomocí SPCK. Tento proces zajišťuje, že pouze UE s příslušným klíčem mohou získat přístup k řízeným službám, jako jsou prémiové funkce nebo omezené síťové řezy. Správa klíče zahrnuje bezpečnou distribuci a uložení, s možností aktualizací přes vzdušné rozhraní ([OTA](/mobilnisite/slovnik/ota/)) pro udržení bezpečnosti.

V provozu umožňuje SPCK poskytovateli služeb řídit různé funkčnosti, včetně aktivace, deaktivace a monitorování využití služeb. Může být například použit k ověření přístupu k přidaným službám, jako jsou streamovací nebo IoT platformy. Klíč funguje ve spojení s dalšími bezpečnostními prvky, jako jsou šifrovací algoritmy a ochrana integrity, aby chránil před neoprávněným přístupem a podvody. Jeho role je klíčová v prostředích s více poskytovateli, což operátorům umožňuje delegovat řízení služeb při zachování celkové síťové bezpečnosti.

## K čemu slouží

SPCK byl vytvořen k řešení potřeby detailního ověřování a řízení na úrovni služeb v sítích 3GPP, což umožňuje poskytovatelům služeb spravovat přístup ke konkrétním funkcím nezávisle na ověřování v jádru sítě. Před jeho zavedením byly bezpečnostní mechanismy primárně zaměřeny na přístup k síti a postrádaly detailní řízení pro různé služby. SPCK tento problém řeší tím, že poskytuje vyhrazený klíč pro autorizaci služeb.

Motivován růstem přidaných služeb a sítí s více klienty, umožňuje SPCK operátorům bezpečně nabízet přizpůsobené služby. Řeší omezení dřívějších systémů podporou flexibilní správy klíčů a integrace se stávajícími ověřovacími frameworky. Jeho vývoj odráží důraz 3GPP na zvýšenou bezpečnost pro vyvíjející se modely služeb, od 3G po 5G.

## Klíčové vlastnosti

- Kryptografický klíč pro ověřování poskytovatele služeb
- Bezpečně uložen v UICC nebo embedded SIM
- Používán v protokolech výzva-odpověď pro řízení přístupu ke službám
- Podporuje detailní autorizaci pro konkrétní služby
- Umožňuje správu a aktualizace klíčů přes vzdušné rozhraní (OTA)
- Integruje se s bezpečnostní architekturou 3GPP (např. AuC, HSS)

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G

---

📖 **Anglický originál a plná specifikace:** [SPCK na 3GPP Explorer](https://3gpp-explorer.com/glossary/spck/)
