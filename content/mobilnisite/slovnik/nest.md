---
slug: "nest"
url: "/mobilnisite/slovnik/nest/"
type: "slovnik"
title: "NEST – Network Slice Template"
date: 2026-01-01
abbr: "NEST"
fullName: "Network Slice Template"
category: "Network Slicing"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nest/"
summary: "Standardizovaný, strojově čitelný datový model definující strukturu, atributy a požadavky síťového řezu. Umožňuje automatizovanou správu životního cyklu řezu tím, že poskytuje předlohu pro jeho vytvoř"
---

NEST (Network Slice Template) je standardizovaný, strojově čitelný datový model, který definuje strukturu a požadavky síťového řezu a slouží jako předloha pro jeho automatizovanou správu životního cyklu.

## Popis

Network Slice Template (NEST, předloha síťového řezu) je základní koncept v rámci 3GPP managementového rámce pro síťové řezy. Je definován jako formální, strukturovaný datový model popisující veškeré potřebné informace pro vytvoření a správu instance síťového řezu. Tato předloha není statickým dokumentem, ale strojově interpretovatelnou specifikací, typicky vyjádřenou pomocí modelovacího jazyka YANG nebo podobného, kterou mohou zpracovávat systémy pro správu a orchestraci, jako je Network Slice Management Function (NSMF) a Communication Service Management Function (CSMF). Předloha zahrnuje komplexní sadu charakteristik řezu, včetně výkonnostních požadavků (např. latence, šířka pásma, spolehlivost), smluv o úrovni služeb (SLA), požadavků na zdroje, topologických omezení a potřebných součástných síťových funkcí a podsíťových řezů.

Architektonicky NEST slouží jako vstup pro fázi návrhu a zavedení řezu. Definuje 'co' je síťový řez. Když je přijat požadavek na komunikační službu, CSMF namapuje požadavky služby na vhodnou NEST. NSMF následně tuto předlohu spotřebuje, aby rozložil požadavky řezu na požadavky na úrovni zdrojů pro podkladové síťové domény (např. RAN, Transport, Core), které spravují Domain Management Systems ([DMS](/mobilnisite/slovnik/dms/)) nebo Network Slice Subnet Management Function (NSSMF). Předloha zahrnuje parametry orientované jak na službu, tak na zdroje, čímž překlenuje propast mezi obchodním záměrem a technickou implementací.

Klíčové komponenty popsané v rámci NEST zahrnují Slice Service Type (eSST), Slice Differentiator (SD) a podrobný seznam profilů řezu. Profil řezu je klíčový prvek, který specifikuje požadavky na podsíťový řez (NSS), jež detailně popisují konkrétní chování a schopnosti potřebné od částí RAN a Core Network. To zahrnuje výběr síťových funkcí ([NF](/mobilnisite/slovnik/nf/)), jejich propojení prostřednictvím rozhraní založených na službách (SBI) a specifické konfigurace pro funkce jako je politika výběru síťového řezu (NSSP). Předloha také zahrnuje politiky správy životního cyklu, deskriptory monitorování pro zajištění řezu a požadavky na zabezpečení a izolaci.

Její role v síti je klíčová pro automatizaci a agilitu. Standardizací definice řezu NEST umožňuje interoperabilitu mezi více dodavateli a operátorům efektivně nabízet řezy jako službu (Slice-as-a-Service). Zajišťuje, že každá vytvořená instance řezu odpovídá předem ověřenému návrhu, což snižuje konfigurační chyby a umožňuje předvídatelný výkon. Předloha je uložena v katalogu nebo úložišti, což umožňuje opakované použití, správu verzí a efektivní správu portfolia řezů v celém jeho životním cyklu od přípravy přes zprovoznění, provoz až po vyřazení.

## K čemu slouží

NEST byl vytvořen, aby řešil základní výzvu efektivního řízení složitosti a rozmanitosti síťových řezů v 5G a dalších generacích. Před jeho standardizací bylo definování síťového řezu ad-hoc, manuální proces zahrnující rozsáhlé návrhové dokumenty a specifické konfigurace pro každý případ užití, jako je enhanced Mobile Broadband (eMBB), Ultra-Reliable Low-Latency Communication (URLLC) a massive Machine-Type Communication (mMTC). Tento přístup nebyl škálovatelný, náchylný k chybám a bránil rychlému nasazení služeb a dynamické alokaci zdrojů.

Hlavní problém, který NEST řeší, je absence společného, strojově čitelného jazyka pro popis síťového řezu. Bez něj byla automatizace správy životního cyklu řezu – vytvoření, modifikace, monitorování a ukončení – nemožná. Předloha poskytuje tento společný jazyk, což umožňuje automatizaci s uzavřenou smyčkou, kdy mohou manažerské systémy interpretovat požadavky služby, přeložit je do technických konfigurací a orchestraci potřebných zdrojů napříč více administrativními a technologickými doménami. To je zásadní pro naplnění vize 5G podporovat miliony současných připojení s různorodými a přísnými požadavky na sdílené fyzické infrastruktuře.

Historicky byly síťové služby monolitické a rigidní. Posun k cloud-nativním, softwarově definovaným sítím vyžadoval nové paradigma pro tvorbu služeb. NEST, zavedený v 3GPP Release 16 jako součást vylepšeného rámce pro správu a orchestraci, toto paradigma poskytuje. Řeší omezení předchozích deskriptorů síťových služeb tím, že je specificky přizpůsoben pro koncept end-to-end logické sítě řezu, zahrnující nejen konektivitu virtuálních síťových funkcí (VNF), ale také specifické chování RAN, charakteristiky transportu a přísné parametry SLA. Je to základní kámen pro komercializaci síťových řezů, který umožňuje operátorům produktizovat a nabízet standardizované předlohy řezů podnikovým zákazníkům.

## Klíčové vlastnosti

- Strojově čitelný datový model (např. YANG) pro automatizované zpracování
- Komplexní definice požadavků služby řezu a požadavků na zdroje
- Zahrnuje cílové parametry výkonu (latence, propustnost, dostupnost)
- Specifikuje součástné síťové funkce a topologie podsítí
- Definuje politiky správy životního cyklu a monitorování
- Umožňuje správu verzí a katalogizaci předloh pro opakované použití

## Definující specifikace

- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.880** (Rel-19) — Study on 5G Energy Efficiency & Saving
- **TR 32.847** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [NEST na 3GPP Explorer](https://3gpp-explorer.com/glossary/nest/)
