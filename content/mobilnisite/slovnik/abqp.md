---
slug: "abqp"
url: "/mobilnisite/slovnik/abqp/"
type: "slovnik"
title: "ABQP – Aggregate BSS QoS Profile"
date: 2025-01-01
abbr: "ABQP"
fullName: "Aggregate BSS QoS Profile"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/abqp/"
summary: "Aggregate BSS QoS Profile (ABQP) je koncept definovaný v 3GPP TS 48.018 pro GSM/EDGE rádiovou přístupovou síť (GERAN). Představuje složený QoS profil pro sadu kontextů paketových toků (PFC) asociovaný"
---

ABQP je agregovaný profil kvality služeb BSS (Aggregate BSS QoS Profile), což je složený QoS profil pro sadu kontextů paketových toků, který umožňuje systému základnových stanic efektivně spravovat rádiové prostředky pro mobilní stanici.

## Popis

Aggregate [BSS](/mobilnisite/slovnik/bss/) QoS Profile (ABQP) je funkční konstrukce v architektuře [GERAN](/mobilnisite/slovnik/geran/), podrobně popsaná ve specifikaci protokolu BSS [GPRS](/mobilnisite/slovnik/gprs/) ([BSSGP](/mobilnisite/slovnik/bssgp/)) (TS 48.018). Funguje na rozhraní mezi podpůrným GPRS uzlem ([SGSN](/mobilnisite/slovnik/sgsn/)) a systémem základnových stanic (BSS), který zahrnuje řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) a základnové přenosové stanice ([BTS](/mobilnisite/slovnik/bts/)). ABQP není samostatný protokol, ale logický profil používaný BSS k pochopení a správě souhrnných požadavků na QoS všech aktivních kontextů paketových toků ([PFC](/mobilnisite/slovnik/pfc/)) pro danou mobilní stanici (MS). Každý PFC odpovídá konkrétnímu datovému toku (např. pro PDP kontext) s vlastními QoS atributy, jako je třída provozu, priorita, zpoždění a spolehlivost.

Z architektonického hlediska je SGSN zodpovědný za vytváření a správu jednotlivých PFC pro MS na základě jejích aktivních kontextů paketového datového protokolu (PDP). Z pohledu BSS by však bylo vysoce neefektivní spravovat každý PFC nezávisle pro přidělování rádiových prostředků, zejména když má MS více souběžných toků (např. prohlížení webu a hlasový hovor). ABQP tento problém řeší tím, že poskytuje konsolidovaný pohled. BSS vypočítá nebo odvodí ABQP agregací parametrů QoS ze všech aktivních PFC pro danou MS. Tento proces agregace bere v úvahu nejpřísnější požadavky napříč toky, aby bylo zajištěno, že složený profil dokáže uspokojit všechny individuální servisní závazky.

Během provozu BSS používá ABQP k činění klíčových rozhodnutí o správě rádiových prostředků. Například při plánování rádiových bloků na uplink a downlink na paketovém datovém kanálu (PDTCH) se BSS odvolává na ABQP, aby určil odpovídající úroveň priority, požadovanou propustnost a přijatelné meze zpoždění pro agregovaný provoz dané MS. To umožňuje efektivní multiplexování prostředků napříč více toky bez nutnosti zvlášť kontrolovat každý PFC při každé plánovací události. ABQP je dynamický; mění se při vytváření, modifikaci nebo uvolňování PFC. BSS musí aktualizovat svou interní reprezentaci ABQP po přijetí zpráv BSSGP od SGSN, které mění stav PFC, jako jsou zprávy RA-CONTROL nebo FLUSH-LL.

Klíčové komponenty spojené s ABQP zahrnují vrstvu BSSGP, která přenáší zprávy pro správu PFC, a funkce správy rádiových prostředků (RR) uvnitř BSC. Role ABQP je klíčová při převádění QoS politik jádrové sítě (od SGSN) na akční parametry rádiového rozhraní. Slouží jako most mezi podrobnou, na tok specifickou signalizací QoS z jádrové sítě a mechanismy agregovaného plánování, které jsou nezbytné v rádiové přístupové síti s omezenými prostředky. To zajišťuje, že QoS závazky od jádra sítě jsou dodržovány co nejefektivněji přes rozhraní vzdušného rozhraní, vyvažujíce výkon pro uživatele s více toky s celkovou kapacitou a stabilitou BSS.

## K čemu slouží

ABQP byl zaveden, aby řešil inherentní složitost a signalizační režii spojenou se správou více nezávislých QoS toků pro jednoho uživatele v prostředí GERAN s omezenými prostředky. Před jeho konceptualizací musel BSS sledovat a vyhodnocovat každý kontext paketového toku individuálně pro každé rozhodnutí o přidělení rádiových prostředků. Tento přístup byl neefektivní a mohl vést k suboptimálnímu plánování, zvýšenému zatížení procesoru BSC a potenciálním nekonzistentnostem v uplatňování QoS napříč různými toky patřícími stejnému uživateli.

Primární problém, který ABQP řeší, je efektivní překlad parametrů QoS jádrové sítě do praktických akcí na rádiovém rozhraní. V sítích GPRS a EDGE jsou rádiové prostředky (časové sloty) vzácné a sdílené mezi mnoha uživateli. Vytvoření ABQP poskytlo mechanismus, pomocí kterého může BSS syntetizovat jedinou, koherentní QoS politiku z potenciálně konfliktních nebo různorodých požadavků toků. Tato syntéza umožňuje plánovači BSS zacházet s agregovaným datovým provozem uživatele s jednotnou strategií priority a přidělování prostředků, čímž zjednodušuje algoritmy a zlepšuje rozhodování v reálném čase. Byl motivován potřebou podporovat sofistikovanější služby s diferencovanou QoS (nad rámec best-effort) v sítích 2G/2.5G, jako je streamování a interaktivní provoz, bez nutnosti zásadní přestavby základní architektury BSS.

Historicky, jak se GPRS vyvíjelo k podpoře vylepšených QoS funkcí v pozdějších vydáních, koncept ABQP poskytl stabilní základ pro správu QoS v GERAN. Odstranil omezení správy na úrovni jednotlivých toků zavedením abstraktní vrstvy. Tato abstrakce je klíčová pro škálovatelnost, umožňuje BSS podporovat uživatele s více souběžnými aplikacemi (běžný scénář s nástupem chytrých telefonů) při zachování předvídatelného výkonu a dodržování dohodnutých QoS profilů. Představuje důležitý krok ve vývoji správy QoS od paradigmat přepojování okruhů k flexibilnějším, na tok orientovaným modelům potřebným pro mobilní data s přepojováním paketů.

## Klíčové vlastnosti

- Agreguje parametry QoS z více kontextů paketových toků (PFC) do jediného profilu
- Umožňuje efektivní plánování rádiových prostředků BSS a stanovení priorit pro uživatele s více toky
- Dynamicky se aktualizuje při vytváření, modifikaci nebo uvolňování PFC ze strany SGSN
- Zjednodušuje logiku uplatňování QoS uvnitř řadiče základnových stanic (BSC)
- Překládá signalizaci QoS z jádrové sítě na akční parametry rádiového rozhraní
- Poskytuje konsolidovaný pohled pro funkce správy BSS, jako je řízení zahlcení

## Související pojmy

- [BSSGP – Base Station System GPRS Protocol](/mobilnisite/slovnik/bssgp/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 48.018** (Rel-19) — BSS-SGSN Interface for GPRS Control

---

📖 **Anglický originál a plná specifikace:** [ABQP na 3GPP Explorer](https://3gpp-explorer.com/glossary/abqp/)
