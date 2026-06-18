---
slug: "u-csi"
url: "/mobilnisite/slovnik/u-csi/"
type: "slovnik"
title: "U-CSI – USSD CAMEL Subscription Information"
date: 2025-01-01
abbr: "U-CSI"
fullName: "USSD CAMEL Subscription Information"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/u-csi/"
summary: "Funkce CAMEL umožňující interakce prostřednictvím USSD (Unstructured Supplementary Service Data) se sítí. Umožňuje operátorům nabízet interaktivní služby, jako jsou kontroly zůstatku nebo menu-řízené"
---

U-CSI je funkce CAMEL, která umožňuje interakce prostřednictvím USSD a umožňuje operátorům nabízet interaktivní služby, jako jsou kontroly zůstatku, prostřednictvím krátkých kódů rozšířením řízení služeb CAMEL na USSD relace.

## Popis

U-CSI ([USSD](/mobilnisite/slovnik/ussd/) [CAMEL](/mobilnisite/slovnik/camel/) Subscription Information) je datový prvek předplatitelského profilu CAMEL (Customized Applications for Mobile network Enhanced Logic) definovaný ve specifikacích 3GPP. Je uložen v [HLR](/mobilnisite/slovnik/hlr/) (Home Location Register) nebo [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) jako součást profilu účastníka. Když mobilní uživatel zahájí USSD relaci – obvykle vytočením krátkého kódu, jako je *123# – síť zkontroluje přítomnost dat U-CSI. Pokud jsou přítomna, spustí se CAMEL procedury.

Klíčový mechanismus spočívá v tom, že [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre) nebo [SGSN](/mobilnisite/slovnik/sgsn/) (Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node) detekuje USSD požadavek. Dotazuje se HLR/HSS na předplatitelská data, získá U-CSI a na základě jeho obsahu naváže dialog s určeným gsmSCF (CAMEL Service Control Function). gsmSCF, což je externí aplikační server, poté řídí USSD relaci. Může odesílat USSD řetězce do uživatelského terminálu, přijímat odpovědi a řídit složitou servisní logiku, jako je dotazování databáze nebo zahájení transakce, než vrátí konečný USSD výsledek uživateli.

Z architektonického hlediska U-CSI odkazuje na konkrétní adresu gsmSCF a obsahuje servisní klíč, triggery a další CAMEL parametry. Integruje USSD, jednoduchý textový přenosový mechanismus, do inteligentního, událostmi řízeného CAMEL rámce. To umožňuje, aby se USSD relace staly programovatelnými a interaktivními nad rámec základních síťových příkazů, a tím umožňuje přidané služby. Jeho úlohou je propojit transportní mechanismus USSD s možnostmi řízení služeb CAMEL, čímž se USSD stává nástrojem pro aplikace definované operátorem.

## K čemu slouží

U-CSI bylo zavedeno za účelem využití široké dostupnosti [USSD](/mobilnisite/slovnik/ussd/) jako jednoduchého a spolehlivého komunikačního kanálu mezi terminály a sítí. Před integrací s CAMEL bylo USSD primárně používáno pro statické, síťové interní příkazy (jako je kontrola hlasové schránky). Vytvoření U-CSI řešilo potřebu učinit USSD dynamickým a aplikací řízeným.

Vyřešilo problém nabízení interaktivních, menu-řízených služeb bez nutnosti složitého klientského softwaru v terminálu nebo bez závislosti na SMS, které mohly být pomalejší a dražší. Propojením USSD s CAMEL mohli operátoři nasazovat služby specifické pro účastníka, jako jsou dotazy na zůstatek u předplacených služeb, menu-řízené informační služby nebo dokonce jednoduché interakce mobilního bankovnictví. Tím se CAMEL paradigma – původně zaměřené na řízení hovorů a SMS – rozšířilo i na doménu USSD a poskytlo jednotný mechanismus pro řízení služeb napříč více typy přenosových médií.

Historicky se objevilo ve vydání 4 jako součást širších vylepšení CAMEL fáze 3, jejichž cílem bylo rozšířit dosah CAMEL na nové služby a relace. Umožnilo operátorům vytvářet standardizované, sítí řízené interaktivní aplikace, čímž obohatilo nabídku služeb bez závislosti na schopnostech terminálu.

## Klíčové vlastnosti

- Spouští CAMEL procedury při zahájení USSD relace
- Umožňuje externímu gsmSCF řídit USSD dialog
- Podporuje dynamické, interaktivní menu-řízené služby prostřednictvím USSD
- Integruje přenosové médium USSD do rámce řízení služeb CAMEL
- Umožňuje aplikační logiku definovanou operátorem pro USSD interakce
- Používá standardní CAMEL parametry, jako je Service Key a adresa gsmSCF

## Související pojmy

- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [U-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/u-csi/)
