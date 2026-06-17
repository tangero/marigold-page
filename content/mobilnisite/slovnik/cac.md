---
slug: "cac"
url: "/mobilnisite/slovnik/cac/"
type: "slovnik"
title: "CAC – Communication Admission Control"
date: 2025-01-01
abbr: "CAC"
fullName: "Communication Admission Control"
category: "QoS"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/cac/"
summary: "Communication Admission Control (CAC – řízení přístupu ke spojení) je síťový mechanismus, který rozhoduje, zda přijmout nebo odmítnout nové požadavky na spojení na základě dostupných prostředků a poža"
---

CAC (Communication Admission Control – řízení přístupu ke spojení) je síťový mechanismus, který rozhoduje, zda přijmout nebo odmítnout nové požadavky na spojení na základě dostupných prostředků a požadavků QoS, aby se předešlo přetížení a zachovala kvalita služeb.

## Popis

Communication Admission Control (CAC – řízení přístupu ke spojení) je základní funkcí správy kvality služeb (QoS) v sítích 3GPP, která funguje na okraji sítě nebo v kritických řídicích bodech za účelem regulace navazování nových komunikačních relací. Mechanismus vyhodnocuje příchozí požadavky na relaci vůči aktuální dostupnosti síťových prostředků, pravidlům politiky a požadavkům QoS jak požadované, tak existujících relací. Když dorazí nový požadavek na relaci, funkce CAC provede vícerozměrné posouzení, které typicky zahrnuje kontrolu dostupné šířky pásma, kapacity zpracování, paměťových prostředků a specifických parametrů QoS, jako je garantovaný bitový tok, maximální bitový tok, rozpočet zpoždění paketů a míra chybovosti paketů. Toto vyhodnocení zajišťuje, že přijetí nové relace nezhorší výkon již navázaných relací pod smluvně dohodnuté úrovně služeb.

Architektura CAC zahrnuje několik síťových prvků pracujících v koordinaci, včetně funkce pravidel pro politiku a účtování (PCRF), funkce vynucování politiky a účtování (PCEF) a různých síťových uzlů, jako je Entita pro správu mobility ([MME](/mobilnisite/slovnik/mme/)) v LTE nebo Funkce pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5G. Ve specifikacích 3GPP je CAC implementován prostřednictvím rozhodování založeného na politikách, kde PCRF poskytuje pravidla pro řízení přístupu PCEF, který je pak vynucuje na úrovni brány. Proces rozhodování zahrnuje jak statické politiky (předkonfigurovaná pravidla o prioritách služeb a alokacích prostředků), tak dynamické faktory (měření síťového zatížení a využití prostředků v reálném čase). U sítí založených na nosičích funguje CAC na úrovni nosiče a vyhodnocuje, zda má být zřízen nový nosič nebo modifikovány stávající.

Implementace CAC se liší v různých síťových doménách. V Radiové přístupové síti (RAN) Radiové řízení přístupu vyhodnocuje dostupnost rádiových prostředků a úroveň rušení před přijetím nových rádiových nosičů. V páteřní síti funkce CAC na branách a bodech vynucování politiky spravují přenosové a procesní prostředky. Mechanismus využívá různé algoritmy od jednoduchých přístupů založených na prahových hodnotách (odmítání požadavků při překročení předdefinovaného limitu využití prostředků) až po sofistikovanější prediktivní modely, které předpovídají budoucí požadavky na prostředky na základě charakteristik provozu a služeb. Pokročilé implementace CAC mohou také zohledňovat priority služeb, profily účastníků a požadavky na síťové segmenty v 5G systémech.

Role CAC přesahuje pouhou kontrolu prostředků a zahrnuje vynucování politik, diferenciaci služeb a ochranu příjmů. Tím, že CAC zabraňuje přetížení sítě, udržuje kvalitu služeb pro prémiové účastníky a kritické aplikace a zároveň zajišťuje spravedlivé přidělování prostředků všem uživatelům. V moderních sítích se CAC vyvinul tak, aby podporoval modely dynamického sdílení prostředků, řízení přístupu pro síťové segmenty a integraci s architekturami virtualizace síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)) a sítí definovaných softwarem (SDN). Mechanismus kontinuálně monitoruje stav sítě a může spustit modifikace relací nebo preventivní akce při zjištění omezení prostředků, čímž zajišťuje optimální výkon sítě při různých podmínkách zatížení.

## K čemu slouží

Communication Admission Control (CAC) byl vytvořen pro řešení základního problému omezených síťových prostředků v kontextu rostoucí poptávky po různorodých komunikačních službách s různými požadavky na kvalitu. Před standardizovanými mechanismy CAC sítě často zažívaly výrazné zhoršení výkonu při současném navázání příliš mnoha relací, což vedlo k přetížení, přerušeným hovorům a špatným uživatelským zážitkům pro všechny připojené uživatele. Nedostatek koordinovaného řízení přístupu měl za následek nepředvídatelnou kvalitu služeb a znemožňoval garantovat výkon pro kritické aplikace nebo prémiové služby. Rané mobilní sítě používaly zjednodušené plánování kapacity, které se nedokázalo přizpůsobit dynamickým charakteristikám provozu nebo rozlišovat mezi typy služeb.

Hlavní motivací pro vývoj CAC v rámci standardů 3GPP bylo umožnit diferenciaci služeb a záruky kvality v paketových sítích. Jak se sítě vyvíjely z okruhově přepínaných hlasových systémů na více službové platformy podporující hlasové, video a datové aplikace, potřeba inteligentního řízení přístupu se stala klíčovou. CAC řeší problém přetížení sítě tím, že proaktivně spravuje navazování relací na základě dostupnosti prostředků v reálném čase namísto spoléhání se na reaktivní mechanismy řízení přetížení. Tento přístup zabraňuje vzniku přetížení ještě před jeho výskytem, udržuje stabilní provoz sítě a zajišťuje, že přijaté relace po celou dobu jejich trvání dostávají smluvně dohodnutou úroveň QoS.

CAC také řeší obchodní požadavky tím, že umožňuje poskytovatelům služeb nabízet služby s různou kvalitou a zavádět diferencované modely účtování. Kontrolou toho, které relace jsou za jakých podmínek přijaty, mohou operátoři chránit síťové prostředky pro služby a účastníky s vysokou hodnotou a zároveň poskytovat základní konektivitu všem uživatelům. Technologie podporuje regulatorní požadavky na služby tísňového volání a kritické komunikace tím, že zajišťuje upřednostněný přístup těchto relací i během síťového přetížení. Jak se sítě vyvíjejí směrem k 5G a síťovým segmentům, stal se CAC nezbytným pro správu izolace segmentů a zajištění, že rozhodnutí o přístupu berou v úvahu jak požadavky vertikálních služeb, tak horizontální omezení prostředků napříč více síťovými doménami.

## Klíčové vlastnosti

- Rozhodování o přístupu založené na politikách
- Vícerozměrné vyhodnocování prostředků (šířka pásma, zpracování, paměť)
- Validace parametrů QoS (GBR, MBR, zpoždění, míra chybovosti)
- Dynamická adaptace na podmínky síťového zatížení
- Priorita služeb a diferenciace účastníků
- Integrace s architekturou řízení politik a účtování

## Definující specifikace

- **TS 22.519** (Rel-19) — NGN Business Communication Requirements
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 32.522** (Rel-11) — SON Policy NRM IRP Information Service

---

📖 **Anglický originál a plná specifikace:** [CAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cac/)
