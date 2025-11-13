---
author: Marisa Aigen
category: ai bezpečnost
companies:
- Google
- Apple
- OpenAI
date: '2025-11-11 21:34:10'
description: Google zavádí Private AI Compute, zabezpečené cloudové prostředí pro
  AI výpočty, které má díky hardwarově chráněnému provozu nabídnout stejnou úroveň
  soukromí jako lokální zpracování na zařízení a současně zpřístupnit výkonnější modely
  Gemini.
importance: 4
layout: tech_news_article
original_title: Google says new cloud-based “Private AI Compute” is just as secure
  as local processing - Ars Technica
publishedAt: '2025-11-11T21:34:10+00:00'
slug: google-says-new-cloud-based-private-ai-compute-is-
source:
  emoji: 🔬
  id: ars-technica
  name: Ars Technica
title: 'Google představuje cloudové „Private AI Compute“: bezpečnost na úrovni lokálního
  zpracování?'
url: https://arstechnica.com/google/2025/11/google-says-new-cloud-based-private-ai-compute-is-just-as-secure-as-local-processing/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/11/Google_Private_Inference-1152x648.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/11/Google_Private_Inference-1152x648.jpg
---

## Souhrn
Google zavádí Private AI Compute, nové cloudové prostředí pro provoz generativní AI, které má umožnit zpracování citlivých dat na vzdálené infrastruktuře bez přístupu provozovatele k obsahu. Řešení kombinuje vlastní čipy TPU, šifrované spojení z koncového zařízení a Trusted Execution Environment založené na technologiích AMD a má nabídnout bezpečnost srovnatelnou s lokálním zpracováním.

## Klíčové body
- Private AI Compute je izolované cloudové prostředí pro provoz modelů Gemini s důrazem na ochranu dat uživatelů.
- Využívá vlastní TPU s integrovanými bezpečnostními prvky a Trusted Execution Environment (TEE), který má bránit přístupu i ze strany Googlu.
- Data jsou přenášena přes šifrovaný kanál přímo do chráněného prostoru a nemají být dostupná běžným cloudovým službám ani administrátorům.
- Google tvrdí, že bezpečnost Private AI Compute odpovídá lokálnímu zpracování na zařízení, ale umožňuje výrazně vyšší výpočetní výkon než NPU v telefonech či laptopech.
- Systém cílí na spojení výhod edge AI (soukromí) a cloudu (výkon), podobně jako koncept Apple Private Cloud Compute.

## Podrobnosti
Private AI Compute je navrženo jako oddělená část cloudové infrastruktury Googlu, určená k provozu velkých modelů Gemini nad citlivými vstupy uživatele, aniž by došlo k běžnému sdílení dat v rámci interních systémů. Základem jsou specializované čipy Tensor Processing Units (TPU), které integrují bezpečnostní prvky pro ověřování firmware a kryptografické operace. Nad nimi běží Trusted Execution Environment (TEE) založený na technologiích AMD, který šifruje a izoluje paměť vůči hostitelskému systému a infrastruktuře provozovatele.

Z koncového zařízení (například telefonu Pixel nebo klientské aplikace) je navázáno šifrované spojení přímo do tohoto TEE. Data by neměla být dostupná standardním administrátorským nástrojům, logovacím systémům ani modelům mimo definovaný účel. Google tvrdí, že ani interní zaměstnanci nemají mít přístup k nezašifrovaným vstupům. Architektura tak má zabránit typickému riziku centralizovaného AI cloudu, kde je uživatel nucen věřit poskytovateli, že s daty nebude dále pracovat.

Služba má umožnit využití velkých modelů Gemini, které nelze efektivně provozovat lokálně na NPU v telefonech či noteboocích. Na rozdíl od menšího modelu Gemini Nano, běžícího přímo na zařízení pro jednodušší úlohy (lokální sumarizace, chytré odpovědi, offline asistenti), má Private AI Compute obsloužit náročnější scénáře: komplexní analýzu dokumentů, multimodální zpracování, firemní asistenty nebo pokročilé generování obsahu, aniž by firma či uživatel museli rezignovat na přísnější režim nakládání s daty.

Google se odvolává na nezávislý audit od bezpečnostní společnosti NCC Group, která má potvrzovat soulad s deklarovanými zásadami. Klíčová ale bude transparentnost technické dokumentace, možnosti nezávislé verifikace implementace a jasná smluvní omezení využití dat k trénování modelů.

## Proč je to důležité
Private AI Compute ukazuje, jak velcí poskytovatelé AI reagují na rostoucí tlak trhu: uživatelé a firmy chtějí využít velké modely, ale nechtějí odevzdat kontrolu nad svými daty. Pokud je architektura skutečně navržena tak, jak Google popisuje, jde o posun k modelu, kde cloudové AI nemusí automaticky znamenat datové riziko.

Z hlediska průmyslu to vytváří nový standard: kombinace hardwarově vynucené izolace (TEE), šifrovaného přenosu přímo do zabezpečeného prostředí a deklarovaného zákazu interního přístupu. Tento přístup bude relevantní pro banky, zdravotnictví, státní správu i technologické firmy, které doposud upřednostňovaly on-premise řešení či lokální inference. Současně ale platí, že uživatelé i regulátoři musí požadovat ověřitelnou implementaci – bez nezávisle kontrolovatelných důkazů zůstane část tvrzení pouze marketingem.

Private AI Compute také posiluje trend, kdy se hranice mezi "edge" a "cloud" stírá. Poskytovatelé se snaží nabídnout výkon cloudu s bezpečnostním narativem lokálního zpracování. Pro ekosystém AI bezpečnosti je zásadní, zda se z těchto tvrzení stanou reálně vymahatelné technické a právní závazky, nebo jen nový slovník pro tradiční centralizovaný sběr dat.

---

[Číst původní článek](https://arstechnica.com/google/2025/11/google-says-new-cloud-based-private-ai-compute-is-just-as-secure-as-local-processing/)

**Zdroj:** 🔬 Ars Technica
