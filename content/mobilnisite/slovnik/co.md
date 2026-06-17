---
slug: "co"
url: "/mobilnisite/slovnik/co/"
type: "slovnik"
title: "CO – Conditional Optional"
date: 2026-01-01
abbr: "CO"
fullName: "Conditional Optional"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/co/"
summary: "Mechanismus specifikací 3GPP, kdy jsou určité funkce, parametry nebo požadavky označeny jako volitelné, ale stávají se povinnými, jsou-li splněny konkrétní podmínky. Umožňuje flexibilní implementace s"
---

CO je mechanismus specifikací 3GPP, kdy jsou funkce nebo parametry volitelné, ale stávají se povinnými, jsou-li splněny určité podmínky, čímž se vyvažuje flexibilita implementace s interoperabilitou.

## Popis

Conditional Optional (CO) je formalizovaná metodika specifikací ve standardech 3GPP, která definuje, kdy se volitelné prvky stanou povinnými na základě konkrétních implementačních podmínek. Na rozdíl od čistě volitelných funkcí, které lze zcela vynechat, nebo povinných funkcí, které musí být vždy implementovány, existují prvky CO v podmíněném stavu. Metodika funguje prostřednictvím explicitních podmíněných výroků v technických specifikacích, které spouštějí povinnou implementaci, když jsou přítomny určité síťové konfigurace, kombinace funkcí nebo scénáře nasazení. Tím vzniká dynamický rámec specifikací, kde se požadavky přizpůsobují na základě skutečných implementačních voleb.

Z architektonického hlediska je CO implementováno prostřednictvím přesného normativního jazyka v technických specifikacích (TS) a technických zprávách (TR) 3GPP. Specifikace jako 3GPP TS 28.821 (Management and orchestration; Concepts, use cases and requirements) a specifikace řady 32 definují rámec pro uplatňování podmíněné volitelnosti. Když je funkce označena jako CO, specifikace obsahuje explicitní podmínky, za kterých přechází z volitelné na povinnou. Tyto podmínky typicky zahrnují závislosti mezi funkcemi, specifické modely nasazení sítě nebo konkrétní požadavky služeb, které vytvářejí implementační závislosti.

Klíčové součásti mechanismu CO zahrnují definice podmíněných spouštěčů, mapování závislostí mezi funkcemi a specifikaci implementačních požadavků. Podmíněné spouštěče jsou pečlivě definovány tak, aby se předešlo nejednoznačnosti a zajistil konzistentní výklad napříč různými implementacemi. Mapování závislostí stanovuje vztahy mezi různými síťovými funkcemi a vlastnostmi a určuje, kdy implementace jedné funkce vyžaduje implementaci jiné. Implementační požadavky specifikují přesné chování, rozhraní nebo parametry, které se stanou povinnými při splnění podmínek.

Úloha CO v sítích 3GPP spočívá v poskytování strukturované flexibility při zachování nezbytné interoperability. Ve složitých telekomunikačních systémech s mnoha volitelnými funkcemi a variacemi nasazení CO zajišťuje, že když jsou zvoleny určité implementační cesty, je konzistentně implementována veškerá potřebná podpůrná funkcionalita. Tím se předchází fragmentaci a zároveň umožňuje dodavatelům a operátorům přizpůsobit implementace konkrétním tržním potřebám, scénářům nasazení nebo nákladovým hlediskům bez ohrožení klíčových bodů interoperability.

## K čemu slouží

Conditional Optional byl vytvořen, aby řešil základní napětí mezi přísností standardizace a flexibilitou implementace v rozvíjejících se telekomunikačních sítích. Jak specifikace 3GPP narůstaly na složitosti s mnoha volitelnými funkcemi, objevila se potřeba jemnějšího přístupu než prostá dichotomie povinné/volitelné. Předchozí přístupy buď činily funkce povinnými (což omezovalo flexibilitu implementace), nebo zcela volitelnými (což riskovalo problémy s interoperabilitou při interakci funkcí). CO poskytuje střední cestu, která zachovává interoperabilitu v kritických scénářích a zároveň umožňuje implementační volby.

Historický kontext vývoje CO zahrnuje rozšíření specifikací 3GPP tak, aby pokrývaly různé scénáře nasazení, od tradičního mobilního širokopásmového přístupu přes IoT, síťové slicing až po privátní sítě. Každý scénář nasazení může vyžadovat různé kombinace funkcí, ale určité interakce funkcí vytvářejí závislosti, které je nutné řešit. CO to řeší tím, že činí funkce podmíněně povinnými pouze tehdy, když jsou aktivovány jejich závislosti. Tento přístup snižuje zbytečnou zátěž implementace a zároveň zajišťuje, že při nasazení složitých kombinací funkcí jsou přítomny všechny potřebné komponenty a jsou interoperabilní.

CO řeší omezení předchozích specifikačních přístupů tím, že poskytuje explicitní podmíněnou logiku v rámci standardizačních dokumentů. Před zavedením CO se složité závislosti často řešily prostřednictvím implementačních směrnic nebo byly ponechány na výkladu dodavatele, což vedlo k potenciálním problémům s interoperabilitou. Formalizací podmíněných požadavků v samotných specifikacích CO vytváří jasnější implementační požadavky při zachování flexibility potřebné pro různorodá nasazení sítí. To je obzvláště důležité, protože 5G a následující generace zavádějí stále složitější síťové architektury s mnoha volitelnými vylepšeními a variacemi nasazení.

## Klíčové vlastnosti

- Dynamická specifikace požadavků na základě implementačních podmínek
- Explicitní podmíněné spouštěče definované v technických specifikacích
- Mapování závislostí mezi síťovými funkcemi a vlastnostmi
- Mechanismus přechodu z volitelného na povinný stav
- Strukturovaná flexibilita pro implementaci sítě
- Zachování interoperability v podmíněných scénářích

## Definující specifikace

- **TS 28.821** (Rel-13) — UML Model Repertoire for FMC Management
- **TS 32.153** (Rel-19) — IRP Technology-Specific Templates Specification
- **TS 32.156** (Rel-20) — UML Modeling for Network Management Systems
- **TS 32.160** (Rel-20) — Mgmt service component spec templates

---

📖 **Anglický originál a plná specifikace:** [CO na 3GPP Explorer](https://3gpp-explorer.com/glossary/co/)
