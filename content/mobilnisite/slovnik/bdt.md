---
slug: "bdt"
url: "/mobilnisite/slovnik/bdt/"
type: "slovnik"
title: "BDT – Background Data Transfer"
date: 2026-01-01
abbr: "BDT"
fullName: "Background Data Transfer"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bdt/"
summary: "Background Data Transfer (BDT) je služba 5G umožňující efektivní, naplánovaný přenos dat pro aplikace, které nejsou citlivé na časové zpoždění. Optimalizuje vytížení síťových prostředků tím, že umožňu"
---

BDT je služba 5G pro efektivní, naplánovaný přenos dat v nekritických aplikacích, která optimalizuje síťové prostředky tím, že umožňuje operátorům spravovat přenosy na pozadí za účelem snížení přetížení sítě.

## Popis

Background Data Transfer (BDT) je standardizovaná funkce služby 5G zavedená ve specifikaci 3GPP Release 15, která umožňuje síťovým operátorům spravovat a plánovat přenosy dat pro aplikace nevyžadující okamžité doručení. Služba funguje na základě rámce řízeného politikami, kde síť určuje optimální přenosová okna na základě stavu sítě, profilů předplatitelů a požadavků aplikací. BDT je implementována v rámci funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) a funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) 5G jádra sítě a spolupracuje s funkcí uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) k vynucení politik plánovaného přenosu dat.

Architektura BDT zahrnuje několik klíčových komponent: aplikační funkci ([AF](/mobilnisite/slovnik/af/)), která vyžaduje možnosti přenosu na pozadí, funkci řízení politik (PCF), která vytváří a spravuje BDT politiky, funkci správy relací (SMF), která tyto politiky vynucuje na úrovni relace, a funkci uživatelské roviny (UPF), která implementuje skutečné plánování přenosu dat. Funkce vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) může být také zapojena, pokud třetí strany vyžadují služby BDT prostřednictvím externích [API](/mobilnisite/slovnik/api/). Systém využívá standardizovaná rozhraní včetně N5 (PCF-AF), N7 (SMF-PCF) a N4 (SMF-UPF) ke koordinaci operací BDT napříč síťovými funkcemi.

BDT funguje ve více krocích: nejprve aplikace nebo síťová funkce identifikuje provoz způsobilý pro přenos na pozadí na základě požadavků QoS a charakteristik aplikace. PCF následně vytvoří BDT politiky specifikující parametry, jako je maximální povolené zpoždění, preferovaná časová okna, limity objemu dat a podmínky sítě pro aktivaci. Tyto politiky jsou předány SMF, která je převádí na konkrétní pravidla pro relaci. UPF tato pravidla implementuje vyrovnáváním, zpožďováním nebo plánováním přenosů dat podle stanovených parametrů. Systém průběžně monitoruje stav sítě a může dynamicky upravovat parametry BDT pro optimalizaci výkonu.

Služba podporuje různé provozní režimy včetně plánování na základě času (konkrétní časová okna), plánování na základě stavu sítě (když je zatížení sítě pod určitou mezí) a hybridní přístupy. Politiky BDT lze aplikovat na různých úrovních podrobnosti: na předplatitele, na aplikaci, na název datové sítě ([DNN](/mobilnisite/slovnik/dnn/)) nebo na síťový řez. Systém obsahuje mechanismy pro řešení konfliktů politik, korelaci účtování pro plánované přenosy a hlášení stavu provádění BDT jak síťovým funkcím, tak externím aplikacím, pokud je to povoleno.

## K čemu slouží

BDT byla vytvořena, aby řešila rostoucí problém přetížení sítě způsobeného obrovským množstvím naléhavého datového provozu v sítích 5G. S rozšiřováním nasazení IoT a všudypřítomností aplikací, jako jsou softwarové aktualizace, zálohy do cloudu a synchronizace obsahu, se sítě potýkaly s rostoucím tlakem provozu na pozadí, který soupeřil s aplikacemi citlivými na zpoždění. Tradiční přístupy zacházely se všemi daty stejně, což vedlo k neefektivnímu využití prostředků v době špičky a ke zhoršení výkonu pro kritické služby.

Předchozí specifikace 3GPP postrádaly standardizované mechanismy pro efektivní správu provozu na pozadí. Operátoři implementovali proprietární řešení nebo se spoléhali na základní diferenciaci QoS, což se ukázalo jako nedostatečné pro rozsah a složitost případů užití v 5G. Mezi omezení patřila neschopnost koordinovat přenosy napříč více aplikacemi, nedostatek standardizovaných [API](/mobilnisite/slovnik/api/) pro integraci třetích stran a nedostatečná podrobnost v řízení plánování. BDT poskytuje standardizovaný rámec, který umožňuje předvídatelné síťové chování při zachování kvality služeb pro všechny aplikace.

Technologie řeší několik klíčových problémů: snižuje přetížení sítě v době špičky přesunutím nenaléhavého provozu do mimošpičkových období, zlepšuje energetickou účinnost jak síťové infrastruktury, tak uživatelských zařízení optimalizací časování přenosů, umožňuje nové obchodní modely pro diferencované služby dat na pozadí a poskytuje operátorům sítí nástroje pro správu exploze komunikací typu stroj-stroj v sítích 5G. Tím, že vytvořila standardizovaný přístup, zajistila 3GPP interoperabilitu mezi dodavateli a umožnila globální nasazení efektivních řešení pro správu dat na pozadí.

## Klíčové vlastnosti

- Plánování řízené politikami v PCF
- Více režimů plánování (časový, na základě stavu sítě, hybridní)
- Podrobné uplatňování politik (na předplatitele, aplikaci, DNN nebo řez)
- Standardizované vystavení externím stranám prostřednictvím API NEF
- Dynamické přizpůsobování na základě stavu sítě v reálném čase
- Integrované možnosti účtování a hlášení

## Definující specifikace

- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.519** (Rel-19) — UDR Usage for Policy & Exposure Data
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 29.548** (Rel-19) — SEAL Data Delivery Server Services Stage 3
- **TS 29.549** (Rel-19) — SEAL API Specification for Vertical Applications
- **TS 29.554** (Rel-19) — 5G Background Data Transfer Policy Control Service

---

📖 **Anglický originál a plná specifikace:** [BDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/bdt/)
