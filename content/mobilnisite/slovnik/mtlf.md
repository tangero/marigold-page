---
slug: "mtlf"
url: "/mobilnisite/slovnik/mtlf/"
type: "slovnik"
title: "MTLF – Model Training Logical Function"
date: 2026-01-01
abbr: "MTLF"
fullName: "Model Training Logical Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mtlf/"
summary: "Model Training Logical Function (MTLF) je funkce 5G sítě zodpovědná za trénování modelů strojového učení pomocí síťových dat. Umožňuje automatizovanou optimalizaci sítě, prediktivní analýzu a řízení ř"
---

MTLF je funkce (network function) 5G sítě, která trénuje modely strojového učení pomocí síťových dat, čímž umožňuje automatizovanou optimalizaci, prediktivní analýzu a řízení řízené umělou inteligencí.

## Popis

Model Training Logical Function (MTLF) je klíčová architektonická komponenta zavedená ve specifikaci 3GPP Release 17 jako součást podpory automatizace sítě a analýzy dat v systému 5G. Je definována v rámci frameworku Management Data Analytics ([MDA](/mobilnisite/slovnik/mda/)) a funguje jako logická funkce, kterou lze nasadit v rámci 5G Core Network nebo v manažerském systému. Primární role MTLF spočívá v příjmu, zpracování a analýze síťových dat za účelem trénování, validace a tvorby modelů strojového učení ([ML](/mobilnisite/slovnik/ml/)). Tyto modely jsou následně využívány k optimalizaci výkonu sítě, predikci poruch, správě zdrojů nebo zlepšení uživatelského zážitku. MTLF komunikuje s dalšími síťovými funkcemi a zdroji dat prostřednictvím standardizovaných rozhraní za účelem sběru trénovacích datových sad, které mohou zahrnovat výkonnostní měření, konfigurační data, informace o poruchách a analýzu uživatelské roviny.

MTLF pracuje podle definovaného pracovního postupu, který zahrnuje sběr dat, trénování modelu a publikaci modelu. Přijímá data od různých producentů, jako je funkce Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)), systémy Operations, Administration and Maintenance ([OAM](/mobilnisite/slovnik/oam/)) nebo jiné síťové funkce ([NF](/mobilnisite/slovnik/nf/)) prostřednictvím servisní operace Nnwdaf_MTLtraining_Request. Data jsou formátována podle analytických předplatných a mohou být surová nebo předzpracovaná. MTLF následně na tato data aplikuje algoritmy strojového učení – které jsou závislé na konkrétní implementaci, ale mohou zahrnovat regresi, klasifikaci, shlukování nebo techniky hlubokého učení – za účelem vytvoření natrénovaného modelu. Proces trénování může zahrnovat extrakci příznaků, výběr modelu, ladění hyperparametrů a validaci proti testovacím datovým sadám, aby byla zajištěna přesnost a zabránilo se přetrénování.

Jakmile je model natrénován a splňuje požadované výkonnostní metriky, MTLF jej publikuje do funkce Model Repository Function ([MRF](/mobilnisite/slovnik/mrf/)) nebo přímo ke spotřebiteli, jako je instance NWDAF, která bude provádět inferenci. Model je typicky reprezentován ve standardizovaném formátu, jako je Predictive Model Markup Language (PMML) nebo Open Neural Network Exchange (ONNX). MTLF také spravuje životní cyklus těchto modelů, včetně verzování, spouštěcích podmínek pro přetrénování (např. na základě změny dat, periodického plánu nebo degradace výkonu) a vyřazení. Lze ji konfigurovat pomocí trénovacích politik, které definují cíle, požadavky na data a výkonnostní prahové hodnoty.

Architektonicky je MTLF součástí širšího daty řízeného ekosystému v 5G. Spolupracuje s NWDAF (která se zaměřuje na analytickou inferenci a vystavení), MRF (pro ukládání modelů) a systémem OAM. Rozhraní jako Nnwdaf_MTLtraining_Request/Response (definované v TS 29.520) usnadňují komunikaci mezi NWDAF (jako spotřebitelem) a MTLF. Toto oddělení trénování (MTLF) a inference (NWDAF) umožňuje škálovatelná, specializovaná nasazení, kde lze výpočetně náročné trénování přesunout na dedikované platformy, zatímco odlehčená inference probíhá blíže k okraji sítě. MTLF umožňuje případy užití, jako je prediktivní vyvažování zátěže, detekce anomálií, úspora energie, optimalizace specifická pro síťové řezy a predikce Quality of Experience ([QoE](/mobilnisite/slovnik/qoe/)).

## K čemu slouží

Funkce Model Training Logical Function byla vytvořena, aby řešila rostoucí složitost 5G sítí a potřebu inteligentního, automatizovaného řízení. Tradiční správa sítě spoléhala na ruční konfiguraci a automatizaci založenou na pravidlech, která nedokázala efektivně reagovat na dynamické podmínky, předpovídat problémy nebo optimalizovat výkon v reálném čase. Exploze dat ze síťových funkcí, zařízení a služeb představovala příležitost využít strojové učení, ale neexistoval standardizovaný způsob, jak integrovat trénování [ML](/mobilnisite/slovnik/ml/) modelů do síťové architektury.

MTLF byla motivována vizí samoorganizujících se sítí (SON) vyvíjejících se v AI-nativní sítě. Řeší problém, jak systematicky generovat a aktualizovat ML modely pomocí živých síťových dat v rámci standardizovaného frameworku. Před MTLF byly možnosti ML proprietární řešení specifická pro dodavatele, kterým chyběla interoperabilita a ztěžovalo zajištění konzistentní kvality modelů nebo sdílení modelů napříč různými síťovými doménami. MTLF poskytuje standardizované, otevřené rozhraní pro vyžádání trénování modelů, což umožňuje síťovým funkcím, jako je NWDAF, konzumovat analytické modely bez vazby na konkrétní dodavatelskou trénovací platformu.

Její zavedení v Release 17, jako součást vylepšení fáze 5G Phase 2, konkrétně podporuje pokročilé scénáře automatizace sítě definované v architektuře systému 5G (TS 23.501) a frameworku Management and Orchestration (MANO). Umožňuje operátorům nasadit automatizaci s uzavřenou smyčkou, kde analytické poznatky z natrénovaných modelů přímo řídí síťové akce (např. prostřednictvím OAM nebo řízení politik). To je klíčové pro správu síťového řezání, kde každý řez může vyžadovat jedinečné výkonnostní modely, a pro splnění přísných požadavků na latenci, spolehlivost a efektivitu kladených 5G vertikálami.

## Klíčové vlastnosti

- Standardizovaná logická funkce pro trénování modelů strojového učení pomocí dat z 5G sítě.
- Podporuje servisně orientované rozhraní (Nnwdaf_MTLtraining_Request) pro přijímání trénovacích požadavků a dat od spotřebitelů, jako je NWDAF.
- Produkuje natrénované modely ve standardizovaných formátech (např. PMML, ONNX) pro publikaci do funkce Model Repository Function (MRF).
- Spravuje kompletní životní cyklus ML modelu včetně trénování, validace, verzování a spouštěného přetrénování.
- Umožňuje daty řízenou optimalizaci sítě, prediktivní údržbu a automatizaci s uzavřenou smyčkou.
- Navržena pro práci v rámci frameworku Management Data Analytics (MDA) spolu s NWDAF a MRF.

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)
- [MDA – Mobile Data Analytics](/mobilnisite/slovnik/mda/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows

---

📖 **Anglický originál a plná specifikace:** [MTLF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtlf/)
